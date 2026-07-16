import importlib.util
import io
import json
import sys
import tempfile
import types
import unittest
from contextlib import ExitStack, redirect_stderr, redirect_stdout
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import Mock, patch

from scripts import monitor_official_youtube as monitor


PROCESS_SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "process_slide_corpus_ai.py"
PROCESS_SPEC = importlib.util.spec_from_file_location("process_slide_corpus_ai_contract_test", PROCESS_SCRIPT)
PROCESS = importlib.util.module_from_spec(PROCESS_SPEC)
assert PROCESS_SPEC.loader
PROCESS_SPEC.loader.exec_module(PROCESS)

VISION_SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "interpret_slide_text_with_vision.py"
VISION_DEPENDENCY = types.ModuleType("improve_slide_ocr_rapidmerge")
VISION_DEPENDENCY.AUDIT_PATH = Path("/nonexistent-rapidmerge-audit.json")
VISION_DEPENDENCY.Candidate = object
VISION_DEPENDENCY.is_weak = lambda _text: True
VISION_DEPENDENCY.text_path = lambda base, slide: base / slide.parent.name / f"{slide.stem}.txt"


def _write_fixture_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


VISION_DEPENDENCY.write_text = _write_fixture_text
VISION_SPEC = importlib.util.spec_from_file_location("interpret_slide_text_contract_test", VISION_SCRIPT)
VISION = importlib.util.module_from_spec(VISION_SPEC)
assert VISION_SPEC.loader
with patch.dict(sys.modules, {"improve_slide_ocr_rapidmerge": VISION_DEPENDENCY}):
    VISION_SPEC.loader.exec_module(VISION)


RSS_XML = b"""<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom" xmlns:yt="http://www.youtube.com/xml/schemas/2015">
  <entry>
    <yt:videoId>video-1</yt:videoId>
    <title>World's Fair 2026 Test Talk</title>
    <published>2026-07-15T12:00:00+00:00</published>
    <updated>2026-07-16T12:00:00+00:00</updated>
  </entry>
</feed>
"""


class YoutubeMonitorTests(unittest.TestCase):
    def test_manifest_refresh_sets_distinguish_premieres_and_pending_captions(self):
        with tempfile.TemporaryDirectory() as directory:
            manifest = Path(directory) / "manifest.json"
            manifest.write_text(json.dumps({"videos": [
                {"id": "pending", "mediaType": "scheduled_premiere"},
                {"id": "caption-later", "mediaType": "talk_recording", "transcriptStatus": "pending"},
                {"id": "ready", "mediaType": "talk_recording"},
            ]}), encoding="utf-8")
            with patch.object(monitor, "OFFICIAL_VIDEO_MANIFEST", manifest):
                self.assertEqual({"pending"}, monitor.scheduled_manifest_video_ids())
                self.assertEqual({"pending", "caption-later"}, monitor.pending_manifest_video_ids())

    def test_multiline_frontmatter_speakers_are_parsed(self):
        text = '---\ntitle: "Talk"\nspeakers:\n  - Alex Bauer\n  - "Second Speaker"\ncategory: talks\n---\n'
        self.assertEqual(["Alex Bauer", "Second Speaker"], monitor.frontmatter_speaker_names(text))

    def test_wf26_promo_title_is_not_treated_as_an_event_recording(self):
        video = monitor.VideoEntry(
            "promo",
            "6 Things to Know about AIE World's Fair 2026",
            "2026-06-21T00:00:00+00:00",
            "2026-06-21T00:00:00+00:00",
            "https://www.youtube.com/watch?v=promo",
        )
        self.assertFalse(monitor.explicit_wf26_event_title(video))

    def test_rewritten_title_matches_schedule_description_and_exact_speaker(self):
        talks = [{
            "id": "talk-one",
            "title": "In Code They Act, In Proof We Trust",
            "speakers": '["Erik Meijer"]',
            "description": "AI agents today execute on blind trust, and the failure modes are already in the headlines. " * 2,
        }]
        video = monitor.VideoEntry(
            "video-1",
            '"I have never seen anything scarier than an LLM with tool calls." - Erik Meijer',
            "2026-07-13T00:00:00+00:00",
            "2026-07-13T00:00:00+00:00",
            "https://www.youtube.com/watch?v=video-1",
            description=talks[0]["description"] + " Speaker biography follows.",
        )

        self.assertEqual(["talk-one"], [row["id"] for row in monitor.verified_schedule_matches(video, talks)])

    def test_shared_speaker_without_schedule_text_is_not_event_association(self):
        talks = [{
            "id": "talk-one",
            "title": "Closing Keynote",
            "speakers": '["Example Speaker"]',
            "description": "TBD",
        }]
        video = monitor.VideoEntry(
            "video-1",
            "An unrelated interview - Example Speaker",
            "2026-07-13T00:00:00+00:00",
            "2026-07-13T00:00:00+00:00",
            "https://www.youtube.com/watch?v=video-1",
            description="A conversation from a different event.",
        )

        self.assertEqual([], monitor.verified_schedule_matches(video, talks))

    def test_upcoming_video_metadata_retains_release_state_without_captions(self):
        video = monitor.video_entry_from_metadata({
            "id": "premiere-1",
            "title": "On AI and Knowledge - Pablo Castro",
            "upload_date": "20260711",
            "release_date": "20260717",
            "live_status": "is_upcoming",
            "description": "Pending premiere",
            "subtitles": {"live_chat": []},
            "automatic_captions": {},
        })

        self.assertEqual("2026-07-11", video.published_date.isoformat())
        self.assertEqual("2026-07-17", video.release_date)
        self.assertEqual("is_upcoming", video.live_status)
        self.assertFalse(video.has_english_captions)

    @patch.object(monitor.time, "sleep")
    @patch.object(monitor, "urlopen")
    def test_fetch_rss_retries_network_and_parse_failures(self, mocked_open, mocked_sleep):
        mocked_open.side_effect = [
            OSError("temporary network failure"),
            Mock(read=Mock(return_value=b"not xml")),
            Mock(read=Mock(return_value=RSS_XML)),
        ]

        entries = monitor.fetch_rss(attempts=3)

        self.assertEqual(["video-1"], [entry.video_id for entry in entries])
        self.assertEqual(3, mocked_open.call_count)
        self.assertEqual([2, 4], [item.args[0] for item in mocked_sleep.call_args_list])
        request = mocked_open.call_args_list[-1].args[0]
        self.assertEqual("AIE-WF2026-Wiki-Monitor/1.0", request.get_header("User-agent"))

    @patch.object(monitor, "urlopen")
    def test_fetch_rss_records_each_failed_attempt(self, mocked_open):
        mocked_open.side_effect = OSError("offline")

        with patch.object(monitor.time, "sleep"), self.assertRaisesRegex(
            RuntimeError, r"attempt 1: OSError: offline; attempt 2: OSError: offline"
        ):
            monitor.fetch_rss(attempts=2)

    def test_snapshot_ignores_check_time_and_youtube_updated_churn(self):
        entry = monitor.VideoEntry(
            video_id="video-1",
            title="World's Fair 2026 Test Talk",
            published="2026-07-15T12:00:00+00:00",
            updated="2026-07-16T12:00:00+00:00",
            url="https://www.youtube.com/watch?v=video-1",
        )
        with tempfile.TemporaryDirectory() as directory:
            snapshot = Path(directory) / "snapshot.json"
            existing = {
                "checked_at": "2026-07-15T13:00:00+00:00",
                "channel_id": monitor.CHANNEL_ID,
                "source_url": monitor.CHANNEL_RSS,
                "entries": [{
                    "id": entry.video_id,
                    "title": entry.title,
                    "url": entry.url,
                    "published": entry.published,
                    "published_date": "2026-07-15",
                    "updated": "2026-07-15T13:00:00+00:00",
                    "channel": monitor.OFFICIAL_CHANNEL,
                    "source": "official_youtube_rss",
                }],
            }
            snapshot.write_text(json.dumps(existing), encoding="utf-8")
            before = snapshot.read_text(encoding="utf-8")

            with patch.object(monitor, "RSS_SNAPSHOT", snapshot):
                changed = monitor.update_channel_snapshot([entry])

            self.assertFalse(changed)
            self.assertEqual(before, snapshot.read_text(encoding="utf-8"))

    def test_snapshot_writes_a_new_stable_entry(self):
        entry = monitor.VideoEntry(
            video_id="video-2",
            title="World's Fair 2026 New Talk",
            published="2026-07-16T12:00:00+00:00",
            updated="2026-07-16T12:00:00+00:00",
            url="https://www.youtube.com/watch?v=video-2",
        )
        with tempfile.TemporaryDirectory() as directory:
            snapshot = Path(directory) / "snapshot.json"
            with patch.object(monitor, "RSS_SNAPSHOT", snapshot):
                changed = monitor.update_channel_snapshot([entry])

            self.assertTrue(changed)
            self.assertEqual("video-2", json.loads(snapshot.read_text(encoding="utf-8"))["entries"][0]["id"])

    def test_monitor_dry_run_does_not_write_status_stop_timer_or_open_browser(self):
        published = datetime.now(timezone.utc).isoformat()
        entry = monitor.VideoEntry("video-1", "World's Fair 2026 Test", published, published, "https://example.test/video")
        with tempfile.TemporaryDirectory() as directory:
            missing_resource = Path(directory) / "missing.md"
            patches = (
                patch.object(monitor, "fetch_rss", return_value=[entry]),
                patch.object(monitor, "read_talk_pages", return_value=[]),
                patch.object(monitor, "event_entries", return_value=[(entry, [])]),
                patch.object(monitor, "discover_recent_channel_event_rows", return_value=([], {"status": "fixture"})),
                patch.object(monitor, "scheduled_manifest_video_ids", return_value=set()),
                patch.object(monitor, "pending_manifest_video_ids", return_value=set()),
                patch.object(monitor, "resource_path", return_value=missing_resource),
                patch.object(monitor, "write_status"),
                patch.object(monitor, "stop_timer_if_present"),
                patch.object(monitor, "open_status_page"),
            )
            with patches[0], patches[1], patches[2], patches[3], patches[4], patches[5], patches[6], patches[7] as write_status, patches[8] as stop_timer, patches[9] as open_status:
                with redirect_stdout(io.StringIO()):
                    self.assertEqual(0, monitor.main(["--dry-run", "--open-status"]))

            write_status.assert_not_called()
            stop_timer.assert_not_called()
            open_status.assert_not_called()
            self.assertFalse(missing_resource.exists())

    def test_monitor_dry_run_failure_reports_mode_without_writing_status(self):
        stdout = io.StringIO()
        with patch.object(monitor, "main", side_effect=RuntimeError("offline")), patch.object(
            monitor, "load_json", return_value={}
        ), patch.object(monitor, "write_status") as write_status, redirect_stdout(stdout), redirect_stderr(io.StringIO()):
            self.assertEqual(1, monitor.run_entrypoint(["--dry-run"]))

        write_status.assert_not_called()
        report = json.loads(stdout.getvalue())
        self.assertTrue(report["dry_run"])
        self.assertEqual("degraded", report["state"])
        self.assertEqual("degraded", report["status"])
        self.assertEqual("RuntimeError", report["error"]["type"])

    def test_monitor_rejects_dry_run_prefix_before_work_or_failure_status(self):
        with patch.object(monitor, "fetch_rss") as generator, patch.object(
            monitor, "write_status"
        ) as write_status, redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as raised:
            monitor.run_entrypoint(["--dry"])

        self.assertEqual(2, raised.exception.code)
        generator.assert_not_called()
        write_status.assert_not_called()

    def test_monitor_caption_failure_is_top_level_degraded_and_nonzero(self):
        returncode, report, enrichment, publish = self._run_monitor_item(
            {"status": "chrome_caption_import_failed", "error": "caption boom"},
            {"status": "already_extracted"},
        )

        self.assertEqual(1, returncode)
        self.assertEqual("degraded", report["state"])
        self.assertEqual("degraded", report["status"])
        self.assertEqual(1, report["failure_count"])
        self.assertEqual(
            [{"id": "video-1", "component": "transcript", "status": "chrome_caption_import_failed", "error": "caption boom"}],
            report["item_failures"],
        )
        enrichment.assert_not_called()
        publish.assert_not_called()

    def test_monitor_slide_failure_is_top_level_degraded_and_nonzero(self):
        returncode, report, enrichment, publish = self._run_monitor_item(
            {"status": "captions_imported"},
            {"status": "slide_extraction_failed", "error": "slide boom"},
        )

        self.assertEqual(1, returncode)
        self.assertEqual("degraded", report["state"])
        self.assertEqual("degraded", report["status"])
        self.assertEqual(
            [{"id": "video-1", "component": "slides", "status": "slide_extraction_failed", "error": "slide boom"}],
            report["item_failures"],
        )
        enrichment.assert_not_called()
        publish.assert_not_called()

    def test_monitor_all_media_components_failed_is_top_level_failed(self):
        returncode, report, _enrichment, _publish = self._run_monitor_item(
            {"status": "chrome_caption_import_failed", "error": "caption boom"},
            {"status": "slide_extraction_failed", "error": "slide boom"},
        )

        self.assertEqual(1, returncode)
        self.assertEqual("failed", report["state"])
        self.assertEqual("failed", report["status"])
        self.assertEqual(2, report["failure_count"])

    def test_slide_corpus_dry_run_does_not_create_receipt(self):
        item = {"video_id": "video-1", "deck_kind": "slides", "images": 2}
        with tempfile.TemporaryDirectory() as directory, patch.object(PROCESS, "RUNS", Path(directory) / "runs"), patch.object(
            PROCESS, "selected_work", return_value=[item]
        ), patch.object(PROCESS, "completed", return_value=False), redirect_stdout(io.StringIO()):
            self.assertEqual(0, PROCESS.main(["--dry-run"]))
            self.assertFalse(PROCESS.RUNS.exists())

    def test_slide_corpus_item_failure_is_degraded_and_nonzero(self):
        item = {"video_id": "video-1", "deck_kind": "slides", "images": 2}
        failed = {**item, "elapsed_seconds": 0.1, "returncode": 1, "stdout": "", "stderr": "boom"}
        with tempfile.TemporaryDirectory() as directory, patch.object(PROCESS, "RUNS", Path(directory) / "runs"), patch.object(
            PROCESS, "selected_work", return_value=[item]
        ), patch.object(PROCESS, "completed", return_value=False), patch.object(
            PROCESS, "run_one", return_value=failed
        ), redirect_stdout(io.StringIO()):
            self.assertEqual(1, PROCESS.main([]))
            report_path = next(PROCESS.RUNS.glob("*.json"))
            report = json.loads(report_path.read_text(encoding="utf-8"))

        self.assertEqual("degraded", report["status"])
        self.assertEqual("failed", report["items"][0]["status"])
        self.assertEqual(1, report["failures"])

    def test_slide_corpus_exception_is_recorded_as_degraded(self):
        item = {"video_id": "video-1", "deck_kind": "slides", "images": 2}
        with tempfile.TemporaryDirectory() as directory, patch.object(PROCESS, "RUNS", Path(directory) / "runs"), patch.object(
            PROCESS, "selected_work", return_value=[item]
        ), patch.object(PROCESS, "completed", return_value=False), patch.object(
            PROCESS, "run_one", side_effect=TimeoutError("timed out")
        ), redirect_stdout(io.StringIO()):
            self.assertEqual(1, PROCESS.main([]))
            report = json.loads(next(PROCESS.RUNS.glob("*.json")).read_text(encoding="utf-8"))

        self.assertEqual("degraded", report["status"])
        self.assertIn("timed out", report["items"][0]["stderr"])

    def test_slide_corpus_parallel_progress_preserves_completed_key(self):
        item = {"video_id": "video-1", "deck_kind": "slides", "images": 2}
        succeeded = {**item, "elapsed_seconds": 0.1, "returncode": 0, "stdout": "", "stderr": ""}
        stdout = io.StringIO()
        with tempfile.TemporaryDirectory() as directory, patch.object(PROCESS, "RUNS", Path(directory) / "runs"), patch.object(
            PROCESS, "selected_work", return_value=[item]
        ), patch.object(PROCESS, "completed", return_value=False), patch.object(
            PROCESS, "run_one", return_value=succeeded
        ), redirect_stdout(stdout):
            self.assertEqual(0, PROCESS.main(["--workers", "2"]))

        progress = next(json.loads(line) for line in stdout.getvalue().splitlines() if '"finished"' in line)
        self.assertEqual(1, progress["completed"])
        self.assertEqual(progress["completed"], progress["finished"])
        self.assertEqual("succeeded", progress["status"])

    def test_vision_dry_run_does_not_probe_provider_or_write_audits(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(
            VISION, "AI_VISION_AUDIT", Path(directory) / "audit.json"
        ), patch.object(VISION, "AI_VISION_PAGE", Path(directory) / "audit.md"), patch.object(
            VISION, "candidate_slides", return_value=[Path("video/slide-001.jpg")]
        ), patch.object(VISION, "choose_provider") as choose_provider, redirect_stdout(io.StringIO()):
            self.assertEqual(0, VISION.main(["--dry-run"]))
            choose_provider.assert_not_called()
            self.assertFalse(VISION.AI_VISION_AUDIT.exists())
            self.assertFalse(VISION.AI_VISION_PAGE.exists())

    def test_vision_item_failure_is_degraded_and_nonzero(self):
        record = {"image": "video/slide-001.jpg", "attempted": True, "error": "provider failed"}
        with tempfile.TemporaryDirectory() as directory, patch.object(
            VISION, "AI_VISION_AUDIT", Path(directory) / "audit.json"
        ), patch.object(VISION, "choose_provider", return_value="openai"), patch.object(
            VISION, "candidate_slides", return_value=[Path("video/slide-001.jpg")]
        ), patch.object(VISION, "process_slide", return_value=record), patch.object(
            VISION, "write_audit_page"
        ), redirect_stdout(io.StringIO()):
            self.assertEqual(1, VISION.main(["--provider", "openai"]))
            audit = json.loads(VISION.AI_VISION_AUDIT.read_text(encoding="utf-8"))

        self.assertEqual("degraded", audit["status"])
        self.assertEqual(1, audit["failures"])

    def test_vision_malformed_model_json_uses_real_parser_and_fails_run(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            slide = root / "wiki" / "assets" / "slides" / "video-1" / "slide-001.jpg"
            slide.parent.mkdir(parents=True)
            slide.write_bytes(b"fixture")
            audit_path = root / "audit.json"
            with patch.object(VISION, "ROOT", root), patch.object(
                VISION, "CANONICAL_OCR", root / "canonical-ocr"
            ), patch.object(VISION, "AI_VISION_OCR", root / "vision-ocr"), patch.object(
                VISION, "AI_VISION_AUDIT", audit_path
            ), patch.object(VISION, "choose_provider", return_value="openai"), patch.object(
                VISION, "candidate_slides", return_value=[slide]
            ), patch.object(
                VISION, "interpret", side_effect=lambda *_args: VISION.parse_json("not valid JSON")
            ), patch.object(VISION, "write_audit_page"), redirect_stdout(io.StringIO()):
                self.assertEqual(1, VISION.main(["--provider", "openai"]))

            audit = json.loads(audit_path.read_text(encoding="utf-8"))
            self.assertEqual("degraded", audit["status"])
            self.assertEqual(1, audit["failures"])
            self.assertEqual(1, audit["slidesAttempted"])
            self.assertIn("malformed JSON", audit["records"][0]["error"])

    def _run_monitor_item(self, transcript_result, slide_result):
        published = datetime.now(timezone.utc).isoformat()
        entry = monitor.VideoEntry("video-1", "World's Fair 2026 Test", published, published, "https://example.test/video")
        with tempfile.TemporaryDirectory() as directory, ExitStack() as stack:
            missing_resource = Path(directory) / "missing.md"
            stack.enter_context(patch.dict(monitor.os.environ, {"AIE_WF2026_MONITOR_AUTO_PUSH": "0"}))
            stack.enter_context(patch.object(monitor, "fetch_rss", return_value=[entry]))
            stack.enter_context(patch.object(monitor, "update_channel_snapshot", return_value=False))
            stack.enter_context(patch.object(monitor, "read_talk_pages", return_value=[]))
            stack.enter_context(patch.object(monitor, "event_entries", return_value=[(entry, [])]))
            stack.enter_context(patch.object(monitor, "discover_recent_channel_event_rows", return_value=([], {"status": "fixture"})))
            stack.enter_context(patch.object(monitor, "scheduled_manifest_video_ids", return_value=set()))
            stack.enter_context(patch.object(monitor, "pending_manifest_video_ids", return_value=set()))
            stack.enter_context(patch.object(monitor, "update_official_video_manifest", return_value=False))
            stack.enter_context(patch.object(monitor, "resource_path", return_value=missing_resource))
            stack.enter_context(patch.object(monitor, "try_import_captions", return_value=transcript_result))
            stack.enter_context(patch.object(monitor, "try_extract_slides", return_value=slide_result))
            stack.enter_context(patch.object(monitor, "write_resource_page", return_value=False))
            stack.enter_context(patch.object(monitor, "update_talk_pages", return_value=0))
            enrichment = stack.enter_context(patch.object(monitor, "run_enrichment", return_value=[]))
            publish = stack.enter_context(patch.object(monitor, "maybe_commit_and_push", return_value={"enabled": False}))
            write_status = stack.enter_context(patch.object(monitor, "write_status"))
            returncode = monitor.main([])
            report = write_status.call_args.args[0]
        return returncode, report, enrichment, publish


if __name__ == "__main__":
    unittest.main()
