import importlib.util
import io
import json
import subprocess
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
VISION_DEPENDENCY.PROVENANCE_REPAIR_SUMMARY = Path(
    "/nonexistent-provenance-repair-summary.json"
)
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
    def test_official_playlist_baseline_contains_all_29_ids_and_private_items(self):
        self.assertEqual(29, len(monitor.OFFICIAL_PLAYLIST_BASELINE_IDS))
        self.assertEqual(29, len(set(monitor.OFFICIAL_PLAYLIST_BASELINE_IDS)))
        self.assertIn("Z3fP-eMEx-8", monitor.OFFICIAL_PLAYLIST_BASELINE_IDS)
        self.assertIn("PXXNCtfKZs0", monitor.OFFICIAL_PLAYLIST_BASELINE_IDS)

    def test_official_playlist_enumeration_retains_private_items_and_validates_owner(self):
        payload = {
            "id": monitor.OFFICIAL_PLAYLIST_ID,
            "title": "AIE World's Fair 2026 Complete Playlist",
            "channel_id": monitor.CHANNEL_ID,
            "entries": [
                {
                    "id": video_id,
                    "title": None if video_id in {"Z3fP-eMEx-8", "PXXNCtfKZs0"} else f"Video {video_id}",
                }
                for video_id in monitor.OFFICIAL_PLAYLIST_BASELINE_IDS
            ],
        }

        def metadata(video_id):
            if video_id in {"Z3fP-eMEx-8", "PXXNCtfKZs0"}:
                raise RuntimeError(f"{video_id}: Private video")
            return monitor.VideoEntry(
                video_id,
                f"Video {video_id}",
                "2026-07-16T00:00:00+00:00",
                "2026-07-16T00:00:00+00:00",
                f"https://www.youtube.com/watch?v={video_id}",
                channel_id=monitor.CHANNEL_ID,
                availability="public",
            )

        completed = Mock(returncode=0, stdout=json.dumps(payload), stderr="")
        with patch.object(monitor.subprocess, "run", return_value=completed), patch.object(
            monitor, "fetch_video_metadata", side_effect=metadata
        ):
            entries, report = monitor.fetch_official_playlist([])

        self.assertEqual(29, len(entries))
        self.assertEqual(2, report["unavailable_count"])
        private = {item.video_id: item for item in entries if item.video is None}
        self.assertEqual({"Z3fP-eMEx-8", "PXXNCtfKZs0"}, set(private))
        self.assertTrue(all(item.availability == "private" for item in private.values()))

        payload["entries"].append({"id": "extra000001", "title": "New official cut"})
        completed = Mock(returncode=0, stdout=json.dumps(payload), stderr="")
        with patch.object(monitor.subprocess, "run", return_value=completed), patch.object(
            monitor, "fetch_video_metadata", side_effect=metadata
        ):
            expanded, expanded_report = monitor.fetch_official_playlist([])
        self.assertEqual(30, len(expanded))
        self.assertEqual(1, expanded_report["new_since_baseline_count"])
        self.assertEqual(["extra000001"], expanded_report["new_since_baseline_ids"])
        payload["entries"].pop()

        def metadata_without_channel(video_id):
            item = metadata(video_id)
            return monitor.VideoEntry(
                item.video_id,
                item.title,
                item.published,
                item.updated,
                item.url,
                channel_id="",
                availability=item.availability,
            )

        completed = Mock(returncode=0, stdout=json.dumps(payload), stderr="")
        with patch.object(monitor.subprocess, "run", return_value=completed), patch.object(
            monitor, "fetch_video_metadata", side_effect=metadata_without_channel
        ), self.assertRaisesRegex(RuntimeError, "video owner mismatch"):
            monitor.fetch_official_playlist([])

        payload["channel_id"] = "wrong-channel"
        completed = Mock(returncode=0, stdout=json.dumps(payload), stderr="")
        with patch.object(monitor.subprocess, "run", return_value=completed), self.assertRaisesRegex(
            RuntimeError, "owner channel mismatch"
        ):
            monitor.fetch_official_playlist([])

    def test_authoritative_manifest_refresh_prunes_stale_non_playlist_primary_rows(self):
        upcoming_ids = {
            "uIiA6DquRiE",
            "RGSFUqzqErE",
            "VrpEyglYgeU",
            "Z2Erdirpudo",
            "eBUyTS7SzV4",
        }
        private_ids = {"Z3fP-eMEx-8", "PXXNCtfKZs0"}
        playlist_entries = []
        for index, video_id in enumerate(monitor.OFFICIAL_PLAYLIST_BASELINE_IDS, start=1):
            if video_id in private_ids:
                playlist_entries.append(
                    monitor.PlaylistEntry(video_id, index, "", "private", None)
                )
                continue
            playlist_entries.append(
                monitor.PlaylistEntry(
                    video_id,
                    index,
                    f"Playlist title {video_id}",
                    "public",
                    monitor.VideoEntry(
                        video_id,
                        f"Video title {video_id}",
                        "2026-07-16T00:00:00+00:00",
                        "2026-07-16T00:00:00+00:00",
                        f"https://www.youtube.com/watch?v={video_id}",
                        live_status="is_upcoming" if video_id in upcoming_ids else "not_live",
                        channel_id=monitor.CHANNEL_ID,
                        availability="public",
                    ),
                )
            )

        retained = [
            {
                "id": "4sX_He5c4sI",
                "mediaType": "event_livestream",
                "associationEvidence": "explicit_wf26_official_livestream",
            },
            {
                "id": "I2cbIws9j10",
                "mediaType": "event_livestream",
                "associationEvidence": "explicit_wf26_official_livestream",
            },
            {
                "id": "htM02KMNZnk",
                "mediaType": "event_livestream",
                "associationEvidence": "explicit_wf26_official_livestream",
            },
            {
                "id": "fakeStream01",
                "mediaType": "event_livestream",
                "associationEvidence": "explicit_wf26_official_livestream",
            },
            {"id": "o-zkvb0iFDQ", "mediaType": "talk_recording"},
            {"id": "sRpqPgKeXNk", "mediaType": "talk_recording"},
        ]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            raw = root / "raw" / "sources"
            wiki = root / "wiki"
            manifest = raw / "official-wf26-video-manifest.json"
            manifest.parent.mkdir(parents=True)
            manifest.write_text(json.dumps({"schemaVersion": 1, "videos": retained}), encoding="utf-8")
            with patch.object(monitor, "ROOT", root), patch.object(monitor, "RAW", raw), patch.object(
                monitor, "WIKI", wiki
            ), patch.object(monitor, "OFFICIAL_VIDEO_MANIFEST", manifest):
                self.assertTrue(
                    monitor.update_official_video_manifest(
                        [],
                        playlist_entries=playlist_entries,
                        prune_stale_non_playlist=True,
                    )
                )
            result = json.loads(manifest.read_text(encoding="utf-8"))

        videos = result["videos"]
        self.assertEqual(32, len(videos))
        retained_ids = {item["id"] for item in retained[:3]}
        self.assertTrue(retained_ids <= {item["id"] for item in videos})
        self.assertFalse(
            {"fakeStream01", "o-zkvb0iFDQ", "sRpqPgKeXNk"}
            & {item["id"] for item in videos}
        )
        counts = {}
        for item in videos:
            counts[item["mediaType"]] = counts.get(item["mediaType"], 0) + 1
        self.assertEqual(
            {
                "talk_recording": 22,
                "scheduled_premiere": 5,
                "event_livestream": 3,
                "unavailable_playlist_item": 2,
            },
            counts,
        )
        playlist = [item for item in videos if item.get("playlistId") == monitor.OFFICIAL_PLAYLIST_ID]
        self.assertEqual(29, len(playlist))
        self.assertTrue(
            all(item["associationEvidence"] == "official_wf26_playlist_membership" for item in playlist)
        )

    def test_retirement_receipt_uses_classifier_reported_update_count(self):
        with tempfile.TemporaryDirectory() as directory:
            wiki = Path(directory) / "wiki"
            (wiki / "talks").mkdir(parents=True)
            completed = Mock(
                returncode=0,
                stdout='classifier detail\n{"counts":{"supporting contextual video":1},"updated":1}\n',
                stderr="",
            )
            with patch.object(monitor, "WIKI", wiki), patch.object(
                monitor, "run", return_value=completed
            ):
                report = monitor.retire_primary_event_projections(
                    ["o-zkvb0iFDQ", "sRpqPgKeXNk"]
                )

        self.assertEqual(1, report["resource_updates"])
        self.assertEqual(1, report["resource_classifier"]["updated"])
        self.assertEqual(0, report["talk_updates"])

    def test_non_playlist_revalidation_rejects_two_concrete_stale_dates(self):
        metadata = {
            "o-zkvb0iFDQ": monitor.VideoEntry(
                "o-zkvb0iFDQ",
                "MCP UI: Extending the frontier",
                "2026-05-06T00:00:00+00:00",
                "2026-05-06T00:00:00+00:00",
                "https://www.youtube.com/watch?v=o-zkvb0iFDQ",
                channel_id=monitor.CHANNEL_ID,
            ),
            "sRpqPgKeXNk": monitor.VideoEntry(
                "sRpqPgKeXNk",
                "Trends Across the AI Frontier",
                "2025-07-08T00:00:00+00:00",
                "2025-07-08T00:00:00+00:00",
                "https://www.youtube.com/watch?v=sRpqPgKeXNk",
                description="Recorded at the AI Engineer World's Fair in San Francisco.",
                channel_id=monitor.CHANNEL_ID,
            ),
        }
        with tempfile.TemporaryDirectory() as directory:
            manifest = Path(directory) / "official-wf26-video-manifest.json"
            manifest.write_text(
                json.dumps(
                    {
                        "videos": [
                            {
                                "id": video_id,
                                "mediaType": "talk_recording",
                                "associationEvidence": "official_channel_plus_schedule_text",
                            }
                            for video_id in metadata
                        ]
                    }
                ),
                encoding="utf-8",
            )
            with patch.object(
                monitor, "OFFICIAL_VIDEO_MANIFEST", manifest
            ), patch.object(
                monitor,
                "fetch_video_metadata",
                side_effect=lambda video_id: metadata[video_id],
            ):
                rows, report = monitor.revalidate_manifest_non_playlist_rows([])

        self.assertEqual([], rows)
        self.assertEqual("ok", report["status"])
        self.assertEqual(
            [
                ("o-zkvb0iFDQ", "2026-05-06", "outside_wf26_date_gate"),
                ("sRpqPgKeXNk", "2025-07-08", "outside_wf26_date_gate"),
            ],
            [
                (item["id"], item["upload_date"], item["reason"])
                for item in report["rejected"]
            ],
        )

    def test_authoritative_prune_requires_complete_channel_and_revalidation_scans(self):
        complete_channel = {"status": "ok", "metadata_errors": []}
        complete_retained = {"status": "ok", "metadata_errors": []}
        self.assertTrue(
            monitor.authoritative_non_playlist_reconciliation_ready(
                complete_channel, complete_retained
            )
        )
        self.assertFalse(
            monitor.authoritative_non_playlist_reconciliation_ready(
                {"status": "channel_scan_failed", "metadata_errors": []},
                complete_retained,
            )
        )
        self.assertFalse(
            monitor.authoritative_non_playlist_reconciliation_ready(
                {"status": "ok", "metadata_errors": [{"id": "new"}]},
                complete_retained,
            )
        )
        self.assertFalse(
            monitor.authoritative_non_playlist_reconciliation_ready(
                complete_channel,
                {"status": "metadata_incomplete", "metadata_errors": [{"id": "old"}]},
            )
        )

    def test_playlist_manifest_keeps_reconciled_talk_matches(self):
        video = monitor.VideoEntry(
            "merge000001",
            "Owner-validated playlist video",
            "2026-07-16T00:00:00+00:00",
            "2026-07-16T00:00:00+00:00",
            "https://www.youtube.com/watch?v=merge000001",
            channel_id=monitor.CHANNEL_ID,
        )
        merged_matches = [
            {"id": "rss-talk", "title": "RSS Talk"},
            {"id": "playlist-talk", "title": "Playlist Talk"},
        ]
        playlist_item = monitor.PlaylistEntry(
            video.video_id,
            30,
            video.title,
            "public",
            video,
            matched_talks=(merged_matches[1],),
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            raw = root / "raw/sources"
            wiki = root / "wiki"
            manifest = raw / "official-wf26-video-manifest.json"
            manifest.parent.mkdir(parents=True)
            manifest.write_text('{"schemaVersion": 1, "videos": []}\n', encoding="utf-8")
            with (
                patch.object(monitor, "ROOT", root),
                patch.object(monitor, "RAW", raw),
                patch.object(monitor, "WIKI", wiki),
                patch.object(monitor, "OFFICIAL_VIDEO_MANIFEST", manifest),
            ):
                self.assertTrue(
                    monitor.update_official_video_manifest(
                        [(video, merged_matches)],
                        playlist_entries=[playlist_item],
                    )
                )

            result = json.loads(manifest.read_text(encoding="utf-8"))

        self.assertEqual(
            ["rss-talk", "playlist-talk"], result["videos"][0]["matchedTalks"]
        )
        self.assertEqual(
            "official_wf26_playlist_membership",
            result["videos"][0]["associationEvidence"],
        )

    def test_enrichment_uses_one_targeted_wiki_maker_update(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = root / "raw" / "sources" / "official-wf26-video-manifest.json"
            transcript = root / "raw" / "sources" / "youtube-transcripts" / "video-1.txt"
            manifest.parent.mkdir(parents=True)
            transcript.parent.mkdir(parents=True)
            manifest.write_text("{}", encoding="utf-8")
            transcript.write_text("transcript", encoding="utf-8")
            completed = Mock(returncode=0)
            with patch.object(monitor, "ROOT", root), patch.object(
                monitor, "RAW", root / "raw" / "sources"
            ), patch.object(
                monitor, "OFFICIAL_VIDEO_MANIFEST", manifest
            ), patch.object(
                monitor, "wiki_maker_executable", return_value="/tools/wiki-from-topic-maker"
            ), patch.object(monitor, "run", return_value=completed) as run:
                result = monitor.run_enrichment(1, ["video-1", "video-1"])

        self.assertEqual(
            [
                (
                    [
                        sys.executable,
                        "scripts/generate_attendance_calibration.py",
                        "--sync-current",
                    ],
                    900,
                ),
                (
                    [
                        "/tools/wiki-from-topic-maker",
                        "update",
                        str(root),
                        "--change-type",
                        "media",
                        "--source",
                        "raw/sources/official-wf26-video-manifest.json",
                        "--source",
                        "raw/sources/youtube-transcripts/video-1.txt",
                        "--json",
                    ],
                    7200,
                ),
                (
                    [
                        sys.executable,
                        "scripts/livestream_segment_projection.py",
                        "--check",
                    ],
                    900,
                ),
                (
                    [
                        sys.executable,
                        "scripts/generate_attendance_calibration.py",
                        "--check-current",
                    ],
                    900,
                ),
                (
                    [
                        sys.executable,
                        "scripts/audit_primary_media_roles.py",
                        "--phase",
                        "full",
                        "--root",
                        ".",
                    ],
                    900,
                ),
            ],
            [
                (call.args[0], call.kwargs["timeout"])
                for call in run.call_args_list
            ],
        )
        self.assertEqual(5, len(result))
        self.assertTrue(all(item["returncode"] == 0 for item in result))

    def test_enrichment_replans_once_when_maker_inputs_change(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = root / "raw" / "sources" / "official-wf26-video-manifest.json"
            manifest.parent.mkdir(parents=True)
            manifest.write_text("{}", encoding="utf-8")
            success = Mock(returncode=0, stdout="", stderr="")
            replan = Mock(
                returncode=1,
                stdout="",
                stderr=monitor.WIKI_MAKER_REPLAN_REQUIRED,
            )
            with patch.object(monitor, "ROOT", root), patch.object(
                monitor, "RAW", root / "raw" / "sources"
            ), patch.object(
                monitor, "OFFICIAL_VIDEO_MANIFEST", manifest
            ), patch.object(
                monitor,
                "wiki_maker_executable",
                return_value="/tools/wiki-from-topic-maker",
            ), patch.object(
                monitor,
                "run",
                side_effect=[success, replan, success, success, success, success],
            ) as run:
                result = monitor.run_enrichment(0, [])

        self.assertEqual(6, run.call_count)
        self.assertEqual(2, result[1]["attempts"])
        self.assertEqual(1, result[1]["first_returncode"])
        self.assertEqual(0, result[1]["returncode"])
        self.assertEqual(
            "deterministic_inputs_changed",
            result[1]["retry_reason"],
        )

    def test_enrichment_stops_when_canonical_attendance_sync_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            completed = Mock(returncode=1)
            with patch.object(monitor, "ROOT", root), patch.object(
                monitor, "RAW", root / "raw" / "sources"
            ), patch.object(monitor, "run", return_value=completed) as run, patch.object(
                monitor, "wiki_maker_executable"
            ) as maker:
                result = monitor.run_enrichment(0, [])

        self.assertEqual(
            [
                sys.executable,
                "scripts/generate_attendance_calibration.py",
                "--sync-current",
            ],
            run.call_args.args[0],
        )
        self.assertEqual(900, run.call_args.kwargs["timeout"])
        self.assertEqual(1, len(result))
        self.assertEqual(1, result[0]["returncode"])
        maker.assert_not_called()

    def test_playable_manifest_projection_ignores_private_and_upcoming_changes(self):
        before = {
            "videos": [
                {"id": "playable", "mediaType": "talk_recording", "title": "Recording"},
                {"id": "upcoming", "mediaType": "scheduled_premiere", "title": "Soon"},
                {"id": "private", "mediaType": "unavailable_playlist_item"},
            ]
        }
        nonplayable_changed = {
            "videos": [
                before["videos"][0],
                {"id": "upcoming", "mediaType": "scheduled_premiere", "title": "Later"},
                {
                    "id": "private",
                    "mediaType": "unavailable_playlist_item",
                    "unavailableReason": "private",
                },
            ]
        }
        playable_changed = {
            "videos": [
                {"id": "playable", "mediaType": "talk_recording", "title": "Updated"},
                *before["videos"][1:],
            ]
        }

        self.assertEqual(
            monitor.playable_manifest_projection(before),
            monitor.playable_manifest_projection(nonplayable_changed),
        )
        self.assertNotEqual(
            monitor.playable_manifest_projection(before),
            monitor.playable_manifest_projection(playable_changed),
        )

    def test_content_completion_separates_association_transcripts_and_slides(self):
        payload = {
            "videos": [
                {
                    "id": "complete-video",
                    "mediaType": "talk_recording",
                    "associationEvidence": "official_channel_plus_schedule_text",
                },
                {
                    "id": "transcript-pending",
                    "mediaType": "talk_recording",
                    "associationEvidence": "official_channel_plus_schedule_text",
                    "slideStatus": monitor.NO_SLIDES_STATUS,
                },
                {
                    "id": "scheduled-video",
                    "mediaType": "scheduled_premiere",
                    "associationEvidence": "official_wf26_playlist_membership",
                },
                {
                    "id": "unavailable-video",
                    "mediaType": "unavailable_playlist_item",
                    "associationEvidence": "official_wf26_playlist_membership",
                },
            ]
        }
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            raw = root / "raw" / "sources"
            wiki = root / "wiki"
            transcript = raw / "youtube-transcripts" / "complete-video.txt"
            transcript.parent.mkdir(parents=True)
            transcript.write_text("cached transcript\n", encoding="utf-8")
            slides = wiki / "slides" / "youtube-complete-video-slides.md"
            slides.parent.mkdir(parents=True)
            slides.write_text("# Slides\n", encoding="utf-8")
            with patch.object(monitor, "RAW", raw), patch.object(monitor, "WIKI", wiki):
                summary = monitor.content_completion_summary(payload)

        self.assertEqual("partial", summary["state"])
        self.assertEqual(4, summary["media_association"]["associated_count"])
        self.assertEqual(2, summary["media_association"]["playable_count"])
        self.assertEqual(1, summary["media_association"]["scheduled_premiere_count"])
        self.assertEqual(1, summary["media_association"]["unavailable_count"])
        self.assertEqual(
            {"state": "partial", "eligible_count": 2, "complete_count": 1, "pending_count": 1, "unavailable_count": 0},
            summary["transcripts"],
        )
        self.assertEqual(
            {"state": "complete", "eligible_count": 2, "complete_count": 2, "pending_count": 0, "unavailable_count": 0},
            summary["slides"],
        )

    def test_wiki_maker_override_fails_closed_when_missing(self):
        with patch.dict(monitor.os.environ, {monitor.WIKI_MAKER_ENV: "/missing/maker"}), patch.object(
            monitor.shutil, "which", return_value=None
        ), self.assertRaisesRegex(RuntimeError, monitor.WIKI_MAKER_ENV):
            monitor.wiki_maker_executable()

    def test_wiki_maker_prefers_project_pinned_runner(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            runner = root / "scripts" / "run_pinned_wiki_maker.py"
            runner.parent.mkdir(parents=True)
            runner.write_text("#!/usr/bin/env python3\n", encoding="utf-8")
            runner.chmod(0o755)
            with patch.dict(monitor.os.environ, {}, clear=True), patch.object(
                monitor, "ROOT", root
            ), patch.object(monitor.shutil, "which", return_value=None):
                self.assertEqual(str(runner), monitor.wiki_maker_executable())

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

    def test_manifest_artifact_refresh_records_same_run_cached_and_no_slides_statuses(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            raw = root / "raw" / "sources"
            wiki = root / "wiki"
            manifest = raw / "official-wf26-video-manifest.json"
            manifest.parent.mkdir(parents=True)
            manifest.write_text(
                json.dumps(
                    {
                        "videos": [
                            {
                                "id": "video-with-slides",
                                "mediaType": "talk_recording",
                                "transcriptStatus": "available_on_youtube",
                                "slideStatus": "pending",
                            },
                            {
                                "id": "video-without-slides",
                                "mediaType": "talk_recording",
                                "transcriptStatus": "available_on_youtube",
                                "slideStatus": "pending",
                            },
                        ]
                    }
                ),
                encoding="utf-8",
            )
            for video_id in ("video-with-slides", "video-without-slides"):
                transcript = raw / "youtube-transcripts" / f"{video_id}.txt"
                transcript.parent.mkdir(parents=True, exist_ok=True)
                transcript.write_text("cached transcript", encoding="utf-8")
            slide_page = wiki / "slides" / "youtube-video-with-slides-slides.md"
            slide_page.parent.mkdir(parents=True)
            slide_page.write_text("# Slides\n", encoding="utf-8")
            processed = [
                {
                    "id": "video-with-slides",
                    "transcript": {"status": "captions_imported"},
                    "slides": {"status": "slide_extraction_ran"},
                },
                {
                    "id": "video-without-slides",
                    "transcript": {"status": "captions_imported"},
                    "slides": {"status": monitor.NO_SLIDES_STATUS},
                },
            ]
            with patch.object(monitor, "ROOT", root), patch.object(
                monitor, "RAW", raw
            ), patch.object(monitor, "WIKI", wiki), patch.object(
                monitor, "OFFICIAL_VIDEO_MANIFEST", manifest
            ):
                self.assertTrue(monitor.refresh_manifest_artifact_statuses(processed))
                self.assertFalse(monitor.refresh_manifest_artifact_statuses(processed))

            rows = {
                item["id"]: item
                for item in json.loads(manifest.read_text(encoding="utf-8"))["videos"]
            }
        self.assertEqual("cached", rows["video-with-slides"]["transcriptStatus"])
        self.assertEqual("cached", rows["video-with-slides"]["slideStatus"])
        self.assertEqual("cached", rows["video-without-slides"]["transcriptStatus"])
        self.assertEqual(monitor.NO_SLIDES_STATUS, rows["video-without-slides"]["slideStatus"])

    def test_playlist_manifest_refresh_preserves_confirmed_no_slides_status(self):
        video = monitor.VideoEntry(
            "video-no-slides",
            "Official playlist talk",
            "2026-07-16T00:00:00+00:00",
            "2026-07-16T00:00:00+00:00",
            "https://www.youtube.com/watch?v=video-no-slides",
            channel_id=monitor.CHANNEL_ID,
            availability="public",
        )
        playlist_item = monitor.PlaylistEntry(
            video.video_id, 1, video.title, "public", video
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            raw = root / "raw" / "sources"
            wiki = root / "wiki"
            manifest = raw / "official-wf26-video-manifest.json"
            manifest.parent.mkdir(parents=True)
            manifest.write_text(
                json.dumps(
                    {
                        "videos": [
                            {
                                "id": video.video_id,
                                "slideStatus": monitor.NO_SLIDES_STATUS,
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            with patch.object(monitor, "ROOT", root), patch.object(
                monitor, "RAW", raw
            ), patch.object(monitor, "WIKI", wiki), patch.object(
                monitor, "OFFICIAL_VIDEO_MANIFEST", manifest
            ):
                self.assertTrue(
                    monitor.update_official_video_manifest(
                        [], playlist_entries=[playlist_item]
                    )
                )

            row = json.loads(manifest.read_text(encoding="utf-8"))["videos"][0]
        self.assertEqual(monitor.NO_SLIDES_STATUS, row["slideStatus"])

    def test_available_video_manifest_refresh_clears_stale_strict_matches(self):
        video = monitor.VideoEntry(
            "video-1",
            "Official playlist talk",
            "2026-07-16T00:00:00+00:00",
            "2026-07-16T00:00:00+00:00",
            "https://www.youtube.com/watch?v=video-1",
            channel_id=monitor.CHANNEL_ID,
            availability="public",
        )
        channel_video = monitor.VideoEntry(
            "channel-video",
            "Explicit WF26 recording",
            "2026-07-16T00:00:00+00:00",
            "2026-07-16T00:00:00+00:00",
            "https://www.youtube.com/watch?v=channel-video",
            channel_id=monitor.CHANNEL_ID,
            availability="public",
        )
        available = monitor.PlaylistEntry(
            video.video_id, 1, video.title, "public", video, matched_talks=()
        )
        unavailable = monitor.PlaylistEntry("private-1", 2, "", "private", None)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            raw = root / "raw" / "sources"
            wiki = root / "wiki"
            manifest = raw / "official-wf26-video-manifest.json"
            manifest.parent.mkdir(parents=True)
            manifest.write_text(
                json.dumps(
                    {
                        "videos": [
                            {"id": video.video_id, "matchedTalks": ["stale-talk"]},
                            {"id": channel_video.video_id, "matchedTalks": ["stale-talk"]},
                            {"id": "private-1", "matchedTalks": ["last-known-talk"]},
                        ]
                    }
                ),
                encoding="utf-8",
            )
            with patch.object(monitor, "ROOT", root), patch.object(
                monitor, "RAW", raw
            ), patch.object(monitor, "WIKI", wiki), patch.object(
                monitor, "OFFICIAL_VIDEO_MANIFEST", manifest
            ):
                self.assertTrue(
                    monitor.update_official_video_manifest(
                        [(channel_video, [])], playlist_entries=[available, unavailable]
                    )
                )

            rows = {
                item["id"]: item
                for item in json.loads(manifest.read_text(encoding="utf-8"))["videos"]
            }
        self.assertEqual([], rows[video.video_id]["matchedTalks"])
        self.assertEqual([], rows[channel_video.video_id]["matchedTalks"])
        self.assertEqual(["last-known-talk"], rows["private-1"]["matchedTalks"])

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

    def test_numeric_part_discriminator_prevents_multi_session_overmatch(self):
        description = (
            "A three-part workshop that shares one schedule description across "
            "each logical session. " * 3
        )
        talks = [
            {
                "id": f"part-{part}",
                "title": f"Setting Yourself Up for Success — Part {part}",
                "speakers": '["Jason Liu"]',
                "description": description,
            }
            for part in (1, 2, 3)
        ]
        video = monitor.VideoEntry(
            "video-part-1",
            "Setting Yourself Up for Success — Part 1 — Jason Liu, OpenAI",
            "2026-07-19T00:00:00+00:00",
            "2026-07-19T00:00:00+00:00",
            "https://www.youtube.com/watch?v=video-part-1",
            description=description,
        )

        self.assertEqual(
            ["part-1"],
            [row["id"] for row in monitor.verified_schedule_matches(video, talks)],
        )

    def test_curated_playlist_overrides_match_only_the_bound_schedule_session(self):
        talks = [
            {
                "id": "2026-07-01-theo-browne-closing-keynote-theo-browne",
                "title": "Closing Keynote - Theo Browne",
                "speakers": '["Theo Browne"]',
                "description": "TBD",
            },
            {
                "id": "different-talk",
                "title": "Different Talk",
                "speakers": '["Theo Browne"]',
                "description": "TBD",
            },
            {
                "id": (
                    "2026-06-30-ishan-anand-will-ai-predict-people-like-we-"
                    "predict-the-weather-alternate-title-a-field-guide-to-"
                    "synthetic-personas-for-market-research"
                ),
                "title": "Will AI predict people like we predict the weather?",
                "speakers": '["Ishan Anand"]',
                "description": "TBD",
            },
            {
                "id": (
                    "2026-06-29-manoj-nair-through-the-ai-fog-the-"
                    "architectural-decision-the-next-24-months-of-agentic-"
                    "security-depends-on"
                ),
                "title": "Through the AI Fog",
                "speakers": '["Manoj Nair"]',
                "description": "TBD",
            },
        ]
        cases = (
            (
                "xUnRQ9vLXxo",
                "What do we build now? - @t3dotgg",
                talks[0]["id"],
            ),
            (
                "YnNF55QV0zs",
                "Persona Engineering: A Field Guide to AI Synthetic Personas",
                talks[2]["id"],
            ),
            (
                "1EZdpEhwmNc",
                "Through the AI Fog: The Architectural Decision Agentic Security Depends On",
                talks[3]["id"],
            ),
        )
        for video_id, title, expected_talk_id in cases:
            video = monitor.VideoEntry(
                video_id,
                title,
                "2026-07-08T00:00:00+00:00",
                "2026-07-08T00:00:00+00:00",
                f"https://www.youtube.com/watch?v={video_id}",
            )
            self.assertEqual(
                [expected_talk_id],
                [
                    row["id"]
                    for row in monitor.verified_schedule_matches(video, talks)
                ],
            )

        video = monitor.VideoEntry(
            cases[0][0],
            cases[0][1],
            "2026-07-08T00:00:00+00:00",
            "2026-07-08T00:00:00+00:00",
            f"https://www.youtube.com/watch?v={cases[0][0]}",
        )
        unrelated_id = monitor.VideoEntry(
            "unrelated-id",
            video.title,
            video.published,
            video.updated,
            video.url,
        )

        self.assertEqual([], monitor.verified_schedule_matches(unrelated_id, talks))

        with tempfile.TemporaryDirectory() as directory:
            wiki = Path(directory) / "wiki"
            resource = wiki / "resources" / f"youtube-{video.video_id}.md"
            resource.parent.mkdir(parents=True)
            resource.write_text("# What do we build now?\n", encoding="utf-8")
            with patch.object(monitor, "WIKI", wiki):
                self.assertTrue(
                    monitor.resource_schedule_projection_needed(video.video_id, talks[:1])
                )
                resource.write_text(
                    "[[2026-07-01-theo-browne-closing-keynote-theo-browne]]\n",
                    encoding="utf-8",
                )
                self.assertFalse(
                    monitor.resource_schedule_projection_needed(video.video_id, talks[:1])
                )

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

    def test_opaque_metadata_placeholder_is_preserved_as_unavailable(self):
        payload = {
            "id": "PXXNCtfKZs0",
            "title": "youtube video #PXXNCtfKZs0",
            "availability": None,
            "live_status": None,
            "upload_date": None,
            "release_date": None,
            "timestamp": None,
            "release_timestamp": None,
            "channel_id": None,
            "description": None,
        }
        completed = Mock(returncode=0, stdout=json.dumps(payload), stderr="")

        with patch.object(monitor.subprocess, "run", return_value=completed):
            with self.assertRaisesRegex(
                RuntimeError, "reports unavailable video: PXXNCtfKZs0"
            ) as raised:
                monitor.fetch_video_metadata("PXXNCtfKZs0")

        self.assertEqual(
            "unavailable", monitor.metadata_unavailable_reason(raised.exception)
        )

    def test_upcoming_playlist_resource_is_association_metadata_not_content_evidence(self):
        video = monitor.VideoEntry(
            "premiere-1",
            "Pending official premiere",
            "2026-07-16T00:00:00+00:00",
            "2026-07-16T00:00:00+00:00",
            "https://www.youtube.com/watch?v=premiere-1",
            live_status="is_upcoming",
            release_date="2026-07-18",
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            page = root / "youtube-premiere-1.md"
            with patch.object(monitor, "ROOT", root), patch.object(
                monitor, "RAW", root / "raw"
            ), patch.object(monitor, "WIKI", root / "wiki"), patch.object(
                monitor, "resource_path", return_value=page
            ):
                self.assertTrue(
                    monitor.write_resource_page(
                        video,
                        [],
                        "pending_premiere",
                        "pending_premiere",
                        association_evidence="official_wf26_playlist_membership",
                    )
                )

            text = page.read_text(encoding="utf-8")
        self.assertIn("association metadata for a scheduled premiere", text)
        self.assertIn("do not use this page as recording, transcript, or slide-content evidence", text)
        self.assertNotIn("use as media/transcript/slide evidence", text)
        self.assertIn('sourceLayers: ["supporting_context"]', text)

    def test_generated_resource_source_layers_follow_playability(self):
        upcoming = monitor.VideoEntry(
            "premiere001",
            "Pending official premiere",
            "2026-07-16T00:00:00+00:00",
            "2026-07-16T00:00:00+00:00",
            "https://www.youtube.com/watch?v=premiere001",
            live_status="is_upcoming",
            release_date="2026-07-18",
        )
        playable = monitor.VideoEntry(
            "playable001",
            "Playable official recording",
            "2026-07-16T00:00:00+00:00",
            "2026-07-16T00:00:00+00:00",
            "https://www.youtube.com/watch?v=playable001",
        )
        unavailable = monitor.PlaylistEntry(
            "private0001", 3, "", "private", None
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            raw = root / "raw" / "sources"
            wiki = root / "wiki"
            with patch.object(monitor, "ROOT", root), patch.object(
                monitor, "RAW", raw
            ), patch.object(monitor, "WIKI", wiki):
                self.assertTrue(
                    monitor.write_resource_page(
                        upcoming,
                        [],
                        "pending_premiere",
                        "pending_premiere",
                        association_evidence="official_wf26_playlist_membership",
                    )
                )
                self.assertTrue(
                    monitor.write_resource_page(
                        playable,
                        [],
                        "already_cached",
                        "not_run",
                        association_evidence="official_wf26_playlist_membership",
                    )
                )
                self.assertTrue(monitor.write_unavailable_resource_page(unavailable))

            upcoming_text = (wiki / "resources/youtube-premiere001.md").read_text()
            playable_text = (wiki / "resources/youtube-playable001.md").read_text()
            unavailable_text = (wiki / "resources/youtube-private0001.md").read_text()

        self.assertIn('sourceLayers: ["supporting_context"]', upcoming_text)
        self.assertIn('sourceLayers: ["supporting_context"]', unavailable_text)
        self.assertNotIn("sourceLayers:", playable_text)

    def test_upcoming_playlist_talk_link_is_not_content_evidence(self):
        video = monitor.VideoEntry(
            "premiere-1",
            "Pending official premiere",
            "2026-07-16T00:00:00+00:00",
            "2026-07-16T00:00:00+00:00",
            "https://www.youtube.com/watch?v=premiere-1",
            live_status="is_upcoming",
            release_date="2026-07-18",
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            talk = root / "talk.md"
            talk.write_text("# Talk\n", encoding="utf-8")
            with patch.object(monitor, "ROOT", root), patch.object(
                monitor, "RAW", root / "raw"
            ), patch.object(monitor, "WIKI", root / "wiki"):
                self.assertEqual(
                    1,
                    monitor.update_talk_pages(
                        video,
                        [{"path": str(talk), "id": "talk", "title": "Talk"}],
                    ),
                )

            text = talk.read_text(encoding="utf-8")
        self.assertIn("event-association and premiere-state metadata only", text)
        self.assertIn("do not use it as recording, transcript, or slide-content evidence", text)
        self.assertNotIn("use this recording as media evidence", text)

    def test_talk_page_reconciliation_moves_and_removes_only_generated_video_block(self):
        video = monitor.VideoEntry(
            "video-1",
            "Official recording",
            "2026-07-16T00:00:00+00:00",
            "2026-07-16T00:00:00+00:00",
            "https://www.youtube.com/watch?v=video-1",
        )
        generated = "\n".join(
            [
                "- [[youtube-video-1]] — official AI Engineer YouTube channel recording published 2026-07-16.",
                "- Evidence status: transcript/slide enrichment pending.",
                "- Boundary: use this recording as media evidence; keep date/time/room facts tied to the official schedule.",
            ]
        )
        other_generated = generated.replace("video-1", "other-video")
        with tempfile.TemporaryDirectory() as directory:
            wiki = Path(directory) / "wiki"
            talks = wiki / "talks"
            talks.mkdir(parents=True)
            old_talk = talks / "old-talk.md"
            new_talk = talks / "new-talk.md"
            unrelated_talk = talks / "unrelated-talk.md"
            old_talk.write_text(
                f"# Old\n\n## Official YouTube Recording\n{generated.replace('[[youtube-video-1]]', '[[youtube-video-1|Official recording]]')}\n\nManual verification note.\n\n## Sources\n- Keep me.\n",
                encoding="utf-8",
            )
            new_talk.write_text("# New\n\n## Sources\n- Keep me.\n", encoding="utf-8")
            unrelated_talk.write_text(
                f"# Other\n\n## Official YouTube Recording\n{other_generated}\n",
                encoding="utf-8",
            )
            match = {"path": str(new_talk), "id": "new-talk", "title": "New Talk"}
            with patch.object(monitor, "WIKI", wiki):
                self.assertTrue(monitor.talk_page_projection_needed(video.video_id, [match]))
                self.assertEqual(2, monitor.update_talk_pages(video, [match]))
                self.assertFalse(monitor.talk_page_projection_needed(video.video_id, [match]))

                old_text = old_talk.read_text(encoding="utf-8")
                new_text = new_talk.read_text(encoding="utf-8")
                unrelated_text = unrelated_talk.read_text(encoding="utf-8")
                self.assertNotIn("[[youtube-video-1]]", old_text)
                self.assertNotIn("[[youtube-video-1|Official recording]]", old_text)
                self.assertIn("Manual verification note.", old_text)
                self.assertIn("## Sources\n- Keep me.", old_text)
                self.assertIn("[[youtube-video-1]]", new_text)
                self.assertIn("[[youtube-other-video]]", unrelated_text)

                self.assertTrue(monitor.talk_page_projection_needed(video.video_id, []))
                self.assertEqual(1, monitor.update_talk_pages(video, []))
                self.assertFalse(monitor.talk_page_projection_needed(video.video_id, []))

            new_text = new_talk.read_text(encoding="utf-8")
            unrelated_text = unrelated_talk.read_text(encoding="utf-8")
        self.assertNotIn("## Official YouTube Recording", new_text)
        self.assertIn("## Sources\n- Keep me.", new_text)
        self.assertIn("[[youtube-other-video]]", unrelated_text)

    def test_empty_schedule_projection_detects_stale_resource_link(self):
        with tempfile.TemporaryDirectory() as directory:
            wiki = Path(directory) / "wiki"
            resource = wiki / "resources" / "youtube-video-1.md"
            resource.parent.mkdir(parents=True)
            resource.write_text(
                "# Video\n\n## Matched Schedule Pages\n- [[stale-talk|Stale Talk]]\n\n## Link\n",
                encoding="utf-8",
            )
            with patch.object(monitor, "WIKI", wiki):
                self.assertTrue(monitor.resource_schedule_projection_needed("video-1", []))

    def test_manual_caption_acquisition_never_uses_browser_fallback(self):
        video = monitor.VideoEntry(
            "video-1",
            "Playlist video",
            "2026-07-16T00:00:00+00:00",
            "2026-07-16T00:00:00+00:00",
            "https://www.youtube.com/watch?v=video-1",
        )
        failed = Mock(returncode=1, stdout="", stderr="captions unavailable")
        with tempfile.TemporaryDirectory() as directory, patch.object(
            monitor, "ROOT", Path(directory)
        ), patch.object(monitor, "RAW", Path(directory) / "raw"), patch.object(
            monitor, "run", return_value=failed
        ), patch.object(monitor, "try_import_captions_with_chrome_agent") as browser:
            result = monitor.try_import_captions(video, allow_browser_fallback=False)

        self.assertEqual("caption_acquisition_pending", result["status"])
        browser.assert_not_called()

    def test_manual_no_caption_result_remains_pending(self):
        video = monitor.VideoEntry(
            "video-1",
            "Playlist video",
            "2026-07-16T00:00:00+00:00",
            "2026-07-16T00:00:00+00:00",
            "https://www.youtube.com/watch?v=video-1",
        )
        completed = Mock(returncode=0, stdout="", stderr="")
        with tempfile.TemporaryDirectory() as directory, patch.object(
            monitor, "ROOT", Path(directory)
        ), patch.object(monitor, "RAW", Path(directory) / "raw"), patch.object(
            monitor, "run", return_value=completed
        ):
            result = monitor.try_import_captions(video, allow_browser_fallback=False)

        self.assertEqual("caption_acquisition_pending", result["status"])
        self.assertEqual("no_captions_found", result["attempt_status"])

    def test_explicit_no_slides_transcript_retires_only_standard_slide_artifacts(self):
        video = monitor.VideoEntry(
            "eBUyTS7SzV4",
            "Closing Keynote: Garry Tan",
            "2026-07-17T00:00:00+00:00",
            "2026-07-17T00:00:00+00:00",
            "https://www.youtube.com/watch?v=eBUyTS7SzV4",
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            raw = root / "raw" / "sources"
            wiki = root / "wiki"
            transcript = raw / "youtube-transcripts" / f"{video.video_id}.txt"
            transcript.parent.mkdir(parents=True)
            transcript.write_text(
                "Welcome to the closing keynote. Sorry, there's no slides. I have no slides. "
                "The talk continues with transcript-backed content.",
                encoding="utf-8",
            )
            slide_page = wiki / "slides" / f"youtube-{video.video_id}-slides.md"
            slide_page.parent.mkdir(parents=True)
            slide_page.write_text("# Extracted Slides\n", encoding="utf-8")
            dense_page = wiki / "slides" / f"youtube-{video.video_id}-dense-slides.md"
            dense_page.write_text("# Independently managed dense slides\n", encoding="utf-8")
            slide_image = wiki / "assets" / "slides" / video.video_id / "slide-001.jpg"
            slide_image.parent.mkdir(parents=True)
            slide_image.write_bytes(b"frame")
            slide_ocr = raw / "slide-ocr" / video.video_id / "slide-001.txt"
            slide_ocr.parent.mkdir(parents=True)
            slide_ocr.write_text("stage sponsor wall", encoding="utf-8")
            talk_page = wiki / "talks" / "closing-keynote.md"
            talk_page.parent.mkdir(parents=True)
            talk_page.write_text(
                "# Closing Keynote\n\n"
                "## Supporting Slides\n"
                f"- [[youtube-{video.video_id}-slides]] — extracted slides.\n\n"
                "## Media Evidence\n"
                f"- Source video: `youtube-{video.video_id}`\n"
                f"- Slide deck: [[youtube-{video.video_id}-slides]]\n"
                f"![[assets/slides/{video.video_id}/slide-001.jpg]]\n"
                f"- Slide-derived themes for `youtube-{video.video_id}`: sponsor, wall.\n\n"
                f"- [[youtube-{video.video_id}-transcript]] — transcript evidence.\n",
                encoding="utf-8",
            )
            with patch.object(monitor, "ROOT", root), patch.object(
                monitor, "RAW", raw
            ), patch.object(monitor, "WIKI", wiki), patch.object(
                monitor, "run"
            ) as run:
                self.assertTrue(
                    monitor.no_slides_reconciliation_needed(video.video_id, set())
                )
                result = monitor.try_extract_slides(video, [], enabled=True)
                self.assertFalse(
                    monitor.no_slides_reconciliation_needed(
                        video.video_id, {video.video_id}
                    )
                )
                self.assertTrue(
                    monitor.write_resource_page(
                        video,
                        [],
                        "already_cached",
                        str(result["status"]),
                        association_evidence="official_wf26_playlist_membership",
                    )
                )

            resource = (wiki / "resources" / f"youtube-{video.video_id}.md").read_text(
                encoding="utf-8"
            )
            slide_page_exists = slide_page.exists()
            slide_asset_dir_exists = slide_image.parent.exists()
            slide_ocr_dir_exists = slide_ocr.parent.exists()
            dense_page_exists = dense_page.exists()
            talk = talk_page.read_text(encoding="utf-8")
        self.assertEqual(monitor.NO_SLIDES_STATUS, result["status"])
        self.assertEqual("explicit_transcript_statement", result["reason"])
        self.assertIn("no slides", str(result["evidence"]).lower())
        self.assertEqual(3, len(result["removed_artifacts"]))
        self.assertFalse(slide_page_exists)
        self.assertFalse(slide_asset_dir_exists)
        self.assertFalse(slide_ocr_dir_exists)
        self.assertTrue(dense_page_exists)
        self.assertIn("No slide deck was used", resource)
        self.assertNotIn(f"[[youtube-{video.video_id}-slides]]", resource)
        self.assertNotIn(f"youtube-{video.video_id}-slides", talk)
        self.assertNotIn(f"assets/slides/{video.video_id}/", talk)
        self.assertNotIn(f"Slide-derived themes for `youtube-{video.video_id}`", talk)
        self.assertIn(f"[[youtube-{video.video_id}-transcript]]", talk)
        run.assert_not_called()

    def test_no_slides_gate_does_not_match_hypothetical_slide_wording(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            raw = root / "raw" / "sources"
            transcript = raw / "youtube-transcripts" / "video-1.txt"
            transcript.parent.mkdir(parents=True)
            transcript.write_text(
                "If there are no slides in a presentation, the audience may ask questions.",
                encoding="utf-8",
            )
            with patch.object(monitor, "ROOT", root), patch.object(
                monitor, "RAW", raw
            ):
                self.assertEqual("", monitor.explicit_no_slides_evidence("video-1"))

    def test_playlist_only_bypasses_cutoff_defaults_no_push_and_calls_maker_once(self):
        old = monitor.VideoEntry(
            "iCj_ATyThvc",
            "Old but official playlist recording",
            "2026-01-01T00:00:00+00:00",
            "2026-01-01T00:00:00+00:00",
            "https://www.youtube.com/watch?v=iCj_ATyThvc",
            channel_id=monitor.CHANNEL_ID,
        )
        private = monitor.PlaylistEntry(
            "Z3fP-eMEx-8", 28, "", "private", None
        )
        visible = monitor.PlaylistEntry(
            old.video_id, 1, old.title, "public", old
        )
        with tempfile.TemporaryDirectory() as directory, ExitStack() as stack:
            missing_resource = Path(directory) / "missing.md"
            call_order: list[str] = []
            stack.enter_context(
                patch.dict(monitor.os.environ, {"AIE_WF2026_MONITOR_AUTO_PUSH": "1"})
            )
            stack.enter_context(patch.object(monitor, "read_talk_pages", return_value=[]))
            stack.enter_context(
                patch.object(
                    monitor,
                    "fetch_official_playlist",
                    return_value=([visible, private], {"status": "fixture"}),
                )
            )
            fetch_rss = stack.enter_context(patch.object(monitor, "fetch_rss"))
            stack.enter_context(patch.object(monitor, "scheduled_manifest_video_ids", return_value=set()))
            stack.enter_context(patch.object(monitor, "pending_manifest_video_ids", return_value=set()))
            stack.enter_context(patch.object(monitor, "update_official_video_manifest", return_value=True))
            manifest_refresh = stack.enter_context(
                patch.object(
                    monitor,
                    "refresh_manifest_artifact_statuses",
                    side_effect=lambda *_args, **_kwargs: call_order.append("refresh")
                    or False,
                )
            )
            stack.enter_context(patch.object(monitor, "resource_path", return_value=missing_resource))
            captions = stack.enter_context(
                patch.object(
                    monitor,
                    "try_import_captions",
                    return_value={"status": "caption_acquisition_pending"},
                )
            )
            stack.enter_context(
                patch.object(monitor, "try_extract_slides", return_value={"status": "skipped_by_configuration"})
            )
            stack.enter_context(patch.object(monitor, "write_resource_page", return_value=True))
            stack.enter_context(patch.object(monitor, "write_unavailable_resource_page", return_value=True))
            stack.enter_context(patch.object(monitor, "update_talk_pages", return_value=0))
            maker = stack.enter_context(
                patch.object(
                    monitor,
                    "run_enrichment",
                    side_effect=lambda *_args, **_kwargs: call_order.append("maker")
                    or [],
                )
            )
            publish = stack.enter_context(
                patch.object(monitor, "maybe_commit_and_push", return_value={"enabled": False})
            )
            stack.enter_context(patch.object(monitor, "write_status"))

            self.assertEqual(
                0,
                monitor.main(["--playlist-only", "--no-slides", "--no-auto-push"]),
            )

        fetch_rss.assert_not_called()
        captions.assert_called_once_with(old, allow_browser_fallback=False)
        manifest_refresh.assert_called_once()
        maker.assert_called_once()
        self.assertEqual(["refresh", "maker"], call_order)
        publish.assert_called_once()
        self.assertFalse(publish.call_args.args[0])

    def test_upcoming_only_change_skips_private_refresh_and_public_synthesis(self):
        upcoming = monitor.VideoEntry(
            "uIiA6DquRiE",
            "Upcoming playlist premiere",
            "2026-07-16T00:00:00+00:00",
            "2026-07-16T00:00:00+00:00",
            "https://www.youtube.com/watch?v=uIiA6DquRiE",
            live_status="is_upcoming",
            release_date="2026-07-18",
            channel_id=monitor.CHANNEL_ID,
        )
        playlist_item = monitor.PlaylistEntry(
            upcoming.video_id, 14, upcoming.title, "public", upcoming
        )
        with tempfile.TemporaryDirectory() as directory, ExitStack() as stack:
            root = Path(directory)
            missing_resource = root / "missing.md"
            stack.enter_context(patch.dict(monitor.os.environ, {"AIE_WF2026_MONITOR_AUTO_PUSH": "0"}))
            stack.enter_context(patch.object(monitor, "OFFICIAL_VIDEO_MANIFEST", root / "manifest.json"))
            stack.enter_context(patch.object(monitor, "read_talk_pages", return_value=[]))
            stack.enter_context(
                patch.object(
                    monitor,
                    "fetch_official_playlist",
                    return_value=([playlist_item], {"status": "fixture"}),
                )
            )
            stack.enter_context(patch.object(monitor, "scheduled_manifest_video_ids", return_value=set()))
            stack.enter_context(patch.object(monitor, "pending_manifest_video_ids", return_value=set()))
            stack.enter_context(patch.object(monitor, "update_official_video_manifest", return_value=True))
            stack.enter_context(
                patch.object(monitor, "refresh_manifest_artifact_statuses", return_value=False)
            )
            stack.enter_context(patch.object(monitor, "resource_path", return_value=missing_resource))
            stack.enter_context(
                patch.object(
                    monitor,
                    "try_import_captions",
                    return_value={"status": "pending_premiere"},
                )
            )
            stack.enter_context(
                patch.object(
                    monitor,
                    "try_extract_slides",
                    return_value={"status": "pending_premiere"},
                )
            )
            stack.enter_context(patch.object(monitor, "write_resource_page", return_value=True))
            stack.enter_context(patch.object(monitor, "update_talk_pages", return_value=0))
            maker = stack.enter_context(patch.object(monitor, "run_enrichment"))
            stack.enter_context(
                patch.object(monitor, "maybe_commit_and_push", return_value={"enabled": False})
            )
            write_status = stack.enter_context(patch.object(monitor, "write_status"))

            self.assertEqual(
                0,
                monitor.main(["--playlist-only", "--no-slides", "--no-auto-push"]),
            )
            report = write_status.call_args.args[0]

        maker.assert_not_called()
        self.assertFalse(report["playable_evidence_changed"])
        self.assertEqual("not_needed", report["private_credibility_v2"]["status"])

    def test_unified_maker_dag_failure_blocks_publish(self):
        playable = monitor.VideoEntry(
            "iCj_ATyThvc",
            "Playable playlist recording",
            "2026-07-16T00:00:00+00:00",
            "2026-07-16T00:00:00+00:00",
            "https://www.youtube.com/watch?v=iCj_ATyThvc",
            channel_id=monitor.CHANNEL_ID,
        )
        playlist_item = monitor.PlaylistEntry(
            playable.video_id, 1, playable.title, "public", playable
        )
        with tempfile.TemporaryDirectory() as directory, ExitStack() as stack:
            root = Path(directory)
            missing_resource = root / "missing.md"
            stack.enter_context(patch.dict(monitor.os.environ, {"AIE_WF2026_MONITOR_AUTO_PUSH": "0"}))
            stack.enter_context(patch.object(monitor, "OFFICIAL_VIDEO_MANIFEST", root / "manifest.json"))
            stack.enter_context(patch.object(monitor, "read_talk_pages", return_value=[]))
            stack.enter_context(
                patch.object(
                    monitor,
                    "fetch_official_playlist",
                    return_value=([playlist_item], {"status": "fixture"}),
                )
            )
            stack.enter_context(patch.object(monitor, "scheduled_manifest_video_ids", return_value=set()))
            stack.enter_context(patch.object(monitor, "pending_manifest_video_ids", return_value=set()))
            stack.enter_context(patch.object(monitor, "update_official_video_manifest", return_value=True))
            stack.enter_context(
                patch.object(monitor, "refresh_manifest_artifact_statuses", return_value=False)
            )
            stack.enter_context(patch.object(monitor, "resource_path", return_value=missing_resource))
            stack.enter_context(
                patch.object(
                    monitor,
                    "try_import_captions",
                    return_value={"status": "already_cached"},
                )
            )
            stack.enter_context(
                patch.object(
                    monitor,
                    "try_extract_slides",
                    return_value={"status": "already_extracted"},
                )
            )
            stack.enter_context(patch.object(monitor, "write_resource_page", return_value=True))
            stack.enter_context(patch.object(monitor, "update_talk_pages", return_value=0))
            maker = stack.enter_context(
                patch.object(
                    monitor,
                    "run_enrichment",
                    return_value=[{"returncode": 1, "error": "credibility policy failed"}],
                )
            )
            publish = stack.enter_context(patch.object(monitor, "maybe_commit_and_push"))
            write_status = stack.enter_context(patch.object(monitor, "write_status"))

            self.assertEqual(
                1,
                monitor.main(["--playlist-only", "--no-slides", "--no-auto-push"]),
            )
            report = write_status.call_args.args[0]

        maker.assert_called_once()
        publish.assert_not_called()
        self.assertEqual("degraded", report["state"])
        self.assertTrue(report["playable_evidence_changed"])
        self.assertEqual(
            "delegated_to_unified_maker_dag",
            report["private_credibility_v2"]["status"],
        )
        self.assertIn("enrichment command failed", report["message"])

    def test_auto_push_preflight_rejects_non_main_and_dirty_worktree(self):
        clean = Mock(returncode=0, stdout="", stderr="")
        feature = Mock(returncode=0, stdout="feature\n", stderr="")
        with patch.object(monitor.subprocess, "run", side_effect=[clean, feature]):
            result = monitor.auto_push_preflight()
        self.assertFalse(result["ok"])
        self.assertIn("main branch", result["reason"])

        dirty = Mock(returncode=0, stdout=" M wiki/index.md\n", stderr="")
        main = Mock(returncode=0, stdout="main\n", stderr="")
        with patch.object(monitor.subprocess, "run", side_effect=[dirty, main]):
            result = monitor.auto_push_preflight()
        self.assertFalse(result["ok"])
        self.assertIn("clean", result["reason"])

    def test_rejected_auto_push_preflight_does_not_write_status_or_fetch_playlist(self):
        stdout = io.StringIO()
        with patch.object(
            monitor,
            "auto_push_preflight",
            return_value={"ok": False, "reason": "auto-push requires a clean pre-run worktree"},
        ), patch.object(monitor, "write_status") as write_status, patch.object(
            monitor, "fetch_official_playlist"
        ) as fetch_playlist, redirect_stdout(stdout):
            self.assertEqual(2, monitor.main(["--playlist-only", "--auto-push"]))

        write_status.assert_not_called()
        fetch_playlist.assert_not_called()
        report = json.loads(stdout.getvalue())
        self.assertEqual("blocked", report["state"])
        self.assertIn("no files were changed", report["message"])

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

    def test_monitor_dry_run_does_not_write_status_or_open_browser(self):
        published = datetime.now(timezone.utc).isoformat()
        entry = monitor.VideoEntry("video-1", "World's Fair 2026 Test", published, published, "https://example.test/video")
        with tempfile.TemporaryDirectory() as directory:
            missing_resource = Path(directory) / "missing.md"
            patches = (
                patch.object(monitor, "fetch_rss", return_value=[entry]),
                patch.object(monitor, "read_talk_pages", return_value=[]),
                patch.object(
                    monitor,
                    "fetch_official_playlist",
                    return_value=([], {"status": "fixture"}),
                ),
                patch.object(monitor, "event_entries", return_value=[(entry, [])]),
                patch.object(monitor, "discover_recent_channel_event_rows", return_value=([], {"status": "fixture"})),
                patch.object(monitor, "scheduled_manifest_video_ids", return_value=set()),
                patch.object(monitor, "pending_manifest_video_ids", return_value=set()),
                patch.object(monitor, "resource_path", return_value=missing_resource),
                patch.object(monitor, "write_status"),
                patch.object(monitor, "open_status_page"),
            )
            with (
                patches[0],
                patches[1],
                patches[2],
                patches[3],
                patches[4],
                patches[5],
                patches[6],
                patches[7],
                patches[8] as write_status,
                patches[9] as open_status,
            ):
                with redirect_stdout(io.StringIO()):
                    self.assertEqual(0, monitor.main(["--dry-run", "--open-status"]))

            write_status.assert_not_called()
            open_status.assert_not_called()
            self.assertFalse(missing_resource.exists())

    def test_rss_only_event_row_is_reconciled_into_manifest(self):
        published = "2026-07-01T12:00:00+00:00"
        entry = monitor.VideoEntry(
            "rss-only-video",
            "World's Fair 2026 RSS-only recording",
            published,
            published,
            "https://www.youtube.com/watch?v=rss-only-video",
        )
        matched = [{"id": "rss-talk", "title": "RSS Talk"}]

        report, manifest_update = self._run_dry_monitor_rows(
            [(entry, matched)],
            [],
        )

        reconciled_rows = manifest_update.call_args.args[0]
        self.assertEqual(["rss-only-video"], [video.video_id for video, _ in reconciled_rows])
        self.assertEqual(matched, reconciled_rows[0][1])
        self.assertEqual(["rss-only-video"], [item["id"] for item in report["processed"]])

    def test_recurring_union_includes_opaque_scheduled_and_unavailable_playlist_items(self):
        opaque = monitor.VideoEntry(
            "opaque00001",
            "A title with no event keywords",
            "2025-01-01T12:00:00+00:00",
            "2025-01-01T12:00:00+00:00",
            "https://www.youtube.com/watch?v=opaque00001",
            live_status="is_upcoming",
            release_date="2026-07-20",
            channel_id=monitor.CHANNEL_ID,
        )
        scheduled = monitor.PlaylistEntry(
            opaque.video_id,
            30,
            opaque.title,
            "public",
            opaque,
        )
        unavailable = monitor.PlaylistEntry(
            "private0001",
            31,
            "Private video",
            "private",
            None,
        )

        report, manifest_update = self._run_dry_monitor_rows(
            [],
            [],
            playlist_entries=[scheduled, unavailable],
        )

        reconciled_rows = manifest_update.call_args.args[0]
        self.assertEqual([opaque.video_id], [video.video_id for video, _ in reconciled_rows])
        self.assertEqual(
            [scheduled, unavailable],
            manifest_update.call_args.kwargs["playlist_entries"],
        )
        self.assertEqual(
            [opaque.video_id, unavailable.video_id],
            [item["id"] for item in report["processed"]],
        )
        self.assertEqual("scheduled_monitor", report["mode"])

    def test_duplicate_rss_channel_and_playlist_rows_are_reconciled_once(self):
        published = "2026-07-01T12:00:00+00:00"
        rss_entry = monitor.VideoEntry(
            "duplicate-video",
            "RSS title",
            published,
            published,
            "https://www.youtube.com/watch?v=duplicate-video",
        )
        channel_entry = monitor.VideoEntry(
            "duplicate-video",
            "Detailed channel title",
            published,
            published,
            "https://www.youtube.com/watch?v=duplicate-video",
            channel_id=monitor.CHANNEL_ID,
            has_english_captions=True,
        )
        channel_match = [{"id": "channel-talk", "title": "Channel Talk"}]
        playlist_entry = monitor.VideoEntry(
            "duplicate-video",
            "Owner-validated playlist metadata",
            published,
            published,
            "https://www.youtube.com/watch?v=duplicate-video",
            channel_id=monitor.CHANNEL_ID,
            has_english_captions=True,
        )
        playlist_item = monitor.PlaylistEntry(
            playlist_entry.video_id,
            7,
            playlist_entry.title,
            "public",
            playlist_entry,
            matched_talks=({"id": "playlist-talk", "title": "Playlist Talk"},),
        )

        report, manifest_update = self._run_dry_monitor_rows(
            [(rss_entry, [{"id": "rss-talk", "title": "RSS Talk"}])],
            [(channel_entry, channel_match)],
            playlist_entries=[playlist_item],
        )

        reconciled_rows = manifest_update.call_args.args[0]
        self.assertEqual(1, len(reconciled_rows))
        self.assertIs(playlist_entry, reconciled_rows[0][0])
        self.assertEqual(
            ["rss-talk", "channel-talk", "playlist-talk"],
            [talk["id"] for talk in reconciled_rows[0][1]],
        )
        self.assertEqual(
            [playlist_item], manifest_update.call_args.kwargs["playlist_entries"]
        )
        self.assertEqual(["duplicate-video"], [item["id"] for item in report["processed"]])

    def test_recurring_playlist_owner_failure_fails_closed_before_other_discovery(self):
        stdout = io.StringIO()
        with (
            patch.object(monitor, "read_talk_pages", return_value=[]),
            patch.object(
                monitor,
                "fetch_official_playlist",
                side_effect=RuntimeError("official WF26 playlist owner channel mismatch"),
            ),
            patch.object(monitor, "fetch_rss") as fetch_rss,
            patch.object(monitor, "discover_recent_channel_event_rows") as channel_scan,
            patch.object(monitor, "update_official_video_manifest") as manifest_update,
            patch.object(monitor, "write_status") as write_status,
            redirect_stdout(stdout),
            redirect_stderr(io.StringIO()),
        ):
            self.assertEqual(
                1,
                monitor.run_entrypoint(["--dry-run", "--no-auto-push"]),
            )

        report = json.loads(stdout.getvalue())
        self.assertEqual("degraded", report["state"])
        self.assertIn("owner channel mismatch", report["error"]["message"])
        fetch_rss.assert_not_called()
        channel_scan.assert_not_called()
        manifest_update.assert_not_called()
        write_status.assert_not_called()

    def test_empty_discovery_keeps_durable_reconciliation_active(self):
        report, manifest_update = self._run_dry_monitor_rows([], [])

        manifest_update.assert_called_once()
        self.assertEqual([], manifest_update.call_args.args[0])
        self.assertEqual("active", report["state"])
        self.assertIsNone(report["active_cutoff_date"])
        self.assertFalse(report["reconciliation_policy"]["auto_expiry"])
        self.assertIsNone(report["reconciliation_policy"]["date_cutoff"])
        self.assertIn("remains eligible for late releases", report["message"])

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
        self.assertEqual("rolled_back", report["mutation_rollback"]["status"])
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

    def test_remote_publish_with_pending_local_sync_is_truthful_and_not_rolled_back(self):
        returncode, report, _enrichment, _publish = self._run_monitor_item(
            {"status": "captions_imported"},
            {"status": "already_extracted"},
            publish_result={
                "enabled": True,
                "changed": True,
                "commit_returncode": 0,
                "push_returncode": 0,
                "local_sync": {
                    "status": "local_sync_pending",
                    "candidateCommit": "a" * 40,
                },
            },
        )

        self.assertEqual(1, returncode)
        self.assertEqual("degraded", report["state"])
        self.assertEqual("degraded", report["status"])
        self.assertIn("published", report["message"])
        self.assertNotIn("mutation_rollback", report)

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

    def test_mutation_transaction_restores_layered_roots_and_direct_writes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "project"
            state = root / ".ops/state/youtube-monitor"
            wiki = root / "wiki"
            existing = wiki / "topics/existing.md"
            existing.parent.mkdir(parents=True)
            existing.write_text("user baseline\n", encoding="utf-8")
            transaction = monitor.MonitorMutationTransaction(root, state)
            with patch.object(monitor, "_ACTIVE_TRANSACTION", transaction):
                monitor.write_text(existing, "monitor direct change\n")
                transaction.backup_canonical_root(wiki)
                existing.write_text("external maker change\n", encoding="utf-8")
                generated = wiki / "topics/generated.md"
                generated.write_text("external generated page\n", encoding="utf-8")
                durable_status = state / "status.json"
                monitor.write_text(durable_status, '{"state":"degraded"}\n')
                result = transaction.rollback()

            self.assertEqual("rolled_back", result["status"])
            self.assertEqual("user baseline\n", existing.read_text(encoding="utf-8"))
            self.assertFalse(generated.exists())
            self.assertEqual(
                '{"state":"degraded"}\n', durable_status.read_text(encoding="utf-8")
            )
            self.assertFalse(transaction.journal_path.exists())
            self.assertFalse(transaction.backup_root.exists())

    def test_root_rollback_wins_over_path_snapshot_taken_after_adapter_mutation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "project"
            state = root / ".ops/state/youtube-monitor"
            wiki = root / "wiki"
            page = wiki / "talks/example.md"
            page.parent.mkdir(parents=True)
            page.write_text("clean baseline\n", encoding="utf-8")
            transaction = monitor.MonitorMutationTransaction(root, state)

            transaction.backup_canonical_root(wiki)
            page.write_text("external adapter mutation\n", encoding="utf-8")
            with patch.object(monitor, "_ACTIVE_TRANSACTION", transaction):
                monitor.write_text(page, "later monitor mutation\n")
                result = transaction.rollback()

            self.assertEqual("rolled_back", result["status"])
            self.assertEqual("clean baseline\n", page.read_text(encoding="utf-8"))
            self.assertFalse(transaction.journal_path.exists())
            self.assertFalse(transaction.backup_root.exists())

    def test_successful_transaction_keeps_changes_and_clears_private_journal(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "project"
            state = root / ".ops/state/youtube-monitor"
            page = root / "wiki/index.md"
            page.parent.mkdir(parents=True)
            page.write_text("before\n", encoding="utf-8")
            transaction = monitor.MonitorMutationTransaction(root, state)
            with patch.object(monitor, "_ACTIVE_TRANSACTION", transaction):
                monitor.write_text(page, "after\n")
                transaction.commit()

            self.assertEqual("after\n", page.read_text(encoding="utf-8"))
            self.assertFalse(transaction.journal_path.exists())
            self.assertFalse(transaction.backup_root.exists())

    def test_enrichment_failure_restores_wiki_static_and_agent_outputs(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "project"
            state = root / ".ops/state/youtube-monitor"
            wiki_page = root / "wiki/index.md"
            static_page = root / "dist/index.html"
            agent_index = root / "agent-index.json"
            for path, value in (
                (wiki_page, "wiki before\n"),
                (static_page, "static before\n"),
                (agent_index, '{"before":true}\n'),
            ):
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(value, encoding="utf-8")
            transaction = monitor.MonitorMutationTransaction(root, state)

            def fail_enrichment(_cmd, **_kwargs):
                wiki_page.write_text("wiki after\n", encoding="utf-8")
                static_page.write_text("static after\n", encoding="utf-8")
                agent_index.write_text('{"after":true}\n', encoding="utf-8")
                (root / "wiki/generated.md").write_text("generated\n", encoding="utf-8")
                return Mock(returncode=1, stdout="", stderr="failed")

            with patch.object(monitor, "ROOT", root), patch.object(
                monitor, "WIKI", root / "wiki"
            ), patch.object(
                monitor, "RAW", root / "raw" / "sources"
            ), patch.object(monitor, "STATE_DIR", state), patch.object(
                monitor, "_ACTIVE_TRANSACTION", transaction
            ), patch.object(
                monitor, "wiki_maker_executable", return_value="wiki-from-topic-maker"
            ), patch.object(
                monitor, "update_source_paths", return_value=[]
            ), patch.object(
                monitor, "run", side_effect=fail_enrichment
            ):
                result = monitor.run_enrichment(0, [])
                report: dict[str, object] = {"message": "enrichment failed"}
                monitor.rollback_failed_monitor_run(report, transaction)

            self.assertEqual(1, result[0]["returncode"])
            self.assertEqual("wiki before\n", wiki_page.read_text(encoding="utf-8"))
            self.assertEqual("static before\n", static_page.read_text(encoding="utf-8"))
            self.assertEqual(
                '{"before":true}\n', agent_index.read_text(encoding="utf-8")
            )
            self.assertFalse((root / "wiki/generated.md").exists())
            self.assertEqual("rolled_back", report["mutation_rollback"]["status"])

    def test_uncaught_monitor_exception_rolls_back_before_durable_status(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "project"
            state = root / ".ops/state/youtube-monitor"
            page = root / "wiki/index.md"
            page.parent.mkdir(parents=True)
            page.write_text("before\n", encoding="utf-8")
            transaction = monitor.MonitorMutationTransaction(root, state)
            transaction.track_path(page)
            page.write_text("interrupted\n", encoding="utf-8")

            with patch.object(monitor, "_ACTIVE_TRANSACTION", transaction), patch.object(
                monitor, "STATUS_JSON", state / "status.json"
            ), patch.object(
                monitor, "STATUS_HTML", state / "status.html"
            ), patch.object(
                monitor, "main", side_effect=RuntimeError("synthetic crash")
            ), redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                self.assertEqual(1, monitor.run_entrypoint([]))

            report = json.loads((state / "status.json").read_text(encoding="utf-8"))
            self.assertEqual("before\n", page.read_text(encoding="utf-8"))
            self.assertEqual("rolled_back", report["mutation_rollback"]["status"])
            self.assertFalse(transaction.journal_path.exists())

    def test_uncertain_publish_exception_defers_rollback_to_startup_recovery(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "project"
            state = root / ".ops/state/youtube-monitor"
            page = root / "wiki/index.md"
            page.parent.mkdir(parents=True)
            page.write_text("before\n", encoding="utf-8")
            transaction = monitor.MonitorMutationTransaction(root, state)
            transaction.track_path(page)
            page.write_text("candidate\n", encoding="utf-8")
            (state / "publish-sync.json").write_text(
                json.dumps(
                    {
                        "schemaVersion": 1,
                        "phase": "candidate_prepared",
                        "baseCommit": "a" * 40,
                        "candidateCommit": "b" * 40,
                    }
                ),
                encoding="utf-8",
            )

            with patch.object(monitor, "ROOT", root), patch.object(
                monitor, "STATE_DIR", state
            ), patch.object(monitor, "_ACTIVE_TRANSACTION", transaction), patch.object(
                monitor, "STATUS_JSON", state / "status.json"
            ), patch.object(
                monitor, "STATUS_HTML", state / "status.html"
            ), patch.object(
                monitor, "main", side_effect=RuntimeError("post-push uncertainty")
            ), redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                self.assertEqual(1, monitor.run_entrypoint([]))

            report = json.loads((state / "status.json").read_text(encoding="utf-8"))
            self.assertEqual("candidate\n", page.read_text(encoding="utf-8"))
            self.assertEqual(
                "deferred_to_publish_recovery",
                report["mutation_rollback"]["status"],
            )
            self.assertTrue(transaction.journal_path.exists())

    def test_startup_recovers_interrupted_transaction_before_clean_preflight(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "project"
            state = root / ".ops/state/youtube-monitor"
            page = root / "wiki/index.md"
            page.parent.mkdir(parents=True)
            page.write_text("before\n", encoding="utf-8")
            transaction = monitor.MonitorMutationTransaction(root, state)
            transaction.track_path(page)
            page.write_text("interrupted mutation\n", encoding="utf-8")
            observed: list[str] = []

            def preflight():
                observed.append(page.read_text(encoding="utf-8"))
                self.assertFalse(transaction.journal_path.exists())
                return {"ok": False, "reason": "fixture stop after recovery"}

            with patch.object(monitor, "ROOT", root), patch.object(
                monitor, "STATE_DIR", state
            ), patch.object(
                monitor, "auto_push_preflight", side_effect=preflight
            ), redirect_stdout(io.StringIO()):
                self.assertEqual(2, monitor.main(["--auto-push"]))

            self.assertEqual(["before\n"], observed)
            self.assertEqual("before\n", page.read_text(encoding="utf-8"))

    def test_verified_remote_publish_commits_surviving_mutation_journal(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "project"
            state = root / ".ops/state/youtube-monitor"
            page = root / "wiki/index.md"
            page.parent.mkdir(parents=True)
            page.write_text("before publish\n", encoding="utf-8")
            transaction = monitor.MonitorMutationTransaction(root, state)
            transaction.track_path(page)
            page.write_text("published candidate\n", encoding="utf-8")
            sync = state / "publish-sync.json"
            sync.write_text(
                json.dumps(
                    {
                        "schemaVersion": 1,
                        "phase": "remote_published",
                        "baseCommit": "a" * 40,
                        "candidateCommit": "b" * 40,
                    }
                ),
                encoding="utf-8",
            )
            observed: list[str] = []

            def recover_publish():
                sync.unlink()
                return {"status": "synchronized", "candidateCommit": "b" * 40}

            def preflight():
                observed.append(page.read_text(encoding="utf-8"))
                self.assertFalse(transaction.journal_path.exists())
                return {"ok": False, "reason": "fixture stop after recovery"}

            with patch.object(monitor, "ROOT", root), patch.object(
                monitor, "STATE_DIR", state
            ), patch.object(
                monitor, "recover_monitor_publish_sync", side_effect=recover_publish
            ), patch.object(
                monitor, "auto_push_preflight", side_effect=preflight
            ), redirect_stdout(io.StringIO()):
                self.assertEqual(2, monitor.main(["--auto-push"]))

            self.assertEqual(["published candidate\n"], observed)
            self.assertEqual(
                "published candidate\n", page.read_text(encoding="utf-8")
            )
            self.assertFalse(transaction.backup_root.exists())

    def test_publish_failure_rolls_back_manifest_and_generated_resource(self):
        published = "2026-07-17T12:00:00+00:00"
        entry = monitor.VideoEntry(
            "video-rollback",
            "World's Fair 2026 Transaction Test",
            published,
            published,
            "https://www.youtube.com/watch?v=video-rollback",
        )
        with tempfile.TemporaryDirectory() as directory, ExitStack() as stack:
            root = Path(directory) / "project"
            raw = root / "raw/sources"
            wiki = root / "wiki"
            state = root / ".ops/state/youtube-monitor"
            manifest = raw / "official-wf26-video-manifest.json"
            manifest.parent.mkdir(parents=True)
            baseline = {"schemaVersion": 1, "videos": []}
            manifest.write_text(json.dumps(baseline) + "\n", encoding="utf-8")
            (wiki / "talks").mkdir(parents=True)
            resource = wiki / "resources/youtube-video-rollback.md"

            stack.enter_context(patch.object(monitor, "ROOT", root))
            stack.enter_context(patch.object(monitor, "RAW", raw))
            stack.enter_context(patch.object(monitor, "WIKI", wiki))
            stack.enter_context(patch.object(monitor, "STATE_DIR", state))
            stack.enter_context(
                patch.object(monitor, "STATUS_JSON", state / "status.json")
            )
            stack.enter_context(
                patch.object(monitor, "STATUS_HTML", state / "status.html")
            )
            stack.enter_context(
                patch.object(monitor, "RSS_SNAPSHOT", raw / "rss.json")
            )
            stack.enter_context(
                patch.object(monitor, "OFFICIAL_VIDEO_MANIFEST", manifest)
            )
            stack.enter_context(
                patch.dict(monitor.os.environ, {"AIE_WF2026_MONITOR_AUTO_PUSH": "0"})
            )
            stack.enter_context(
                patch.object(
                    monitor,
                    "fetch_official_playlist",
                    return_value=([], {"status": "fixture"}),
                )
            )
            stack.enter_context(patch.object(monitor, "fetch_rss", return_value=[entry]))
            stack.enter_context(
                patch.object(monitor, "update_channel_snapshot", return_value=False)
            )
            stack.enter_context(patch.object(monitor, "read_talk_pages", return_value=[]))
            stack.enter_context(
                patch.object(monitor, "event_entries", return_value=[(entry, [])])
            )
            stack.enter_context(
                patch.object(
                    monitor,
                    "discover_recent_channel_event_rows",
                    return_value=([], {"status": "fixture"}),
                )
            )
            stack.enter_context(
                patch.object(monitor, "scheduled_manifest_video_ids", return_value=set())
            )
            stack.enter_context(
                patch.object(monitor, "pending_manifest_video_ids", return_value=set())
            )
            stack.enter_context(
                patch.object(monitor, "no_slides_manifest_video_ids", return_value=set())
            )

            def update_manifest(*_args, **_kwargs):
                monitor.write_json(
                    manifest,
                    {
                        "schemaVersion": 1,
                        "videos": [
                            {
                                "id": entry.video_id,
                                "mediaType": "talk_recording",
                                "associationEvidence": "official_channel_explicit_wf26_title",
                            }
                        ],
                    },
                )
                return True

            def write_resource(*_args, **_kwargs):
                monitor.write_text(resource, "generated resource\n")
                return True

            stack.enter_context(
                patch.object(
                    monitor, "update_official_video_manifest", side_effect=update_manifest
                )
            )
            stack.enter_context(
                patch.object(
                    monitor,
                    "try_import_captions",
                    return_value={"status": "already_cached"},
                )
            )
            stack.enter_context(
                patch.object(
                    monitor,
                    "try_extract_slides",
                    return_value={"status": "already_extracted"},
                )
            )
            stack.enter_context(
                patch.object(monitor, "write_resource_page", side_effect=write_resource)
            )
            stack.enter_context(patch.object(monitor, "update_talk_pages", return_value=0))
            stack.enter_context(
                patch.object(
                    monitor, "refresh_manifest_artifact_statuses", return_value=False
                )
            )
            stack.enter_context(patch.object(monitor, "run_enrichment", return_value=[]))
            stack.enter_context(
                patch.object(
                    monitor,
                    "maybe_commit_and_push",
                    return_value={
                        "enabled": True,
                        "changed": True,
                        "commit_returncode": 0,
                        "push_returncode": 1,
                    },
                )
            )

            self.assertEqual(1, monitor.main(["--no-auto-push"]))
            report = json.loads((state / "status.json").read_text(encoding="utf-8"))

            self.assertEqual(baseline, json.loads(manifest.read_text(encoding="utf-8")))
            self.assertFalse(resource.exists())
            self.assertEqual("rolled_back", report["mutation_rollback"]["status"])
            self.assertFalse((state / monitor.TRANSACTION_JOURNAL.name).exists())

    def test_publish_candidate_advances_local_main_only_after_successful_push(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "project"
            remote = Path(directory) / "remote.git"
            root.mkdir()
            subprocess.run(["git", "init", "-b", "main"], cwd=root, check=True, capture_output=True)
            subprocess.run(
                ["git", "config", "user.email", "monitor@example.test"],
                cwd=root,
                check=True,
            )
            subprocess.run(
                ["git", "config", "user.name", "Monitor Test"], cwd=root, check=True
            )
            for path, value in (
                (root / "wiki/index.md", "before\n"),
                (root / "raw/input.json", "{}\n"),
                (root / "scripts/keep.py", "# fixture\n"),
                (root / "package.json", "{}\n"),
                (root / "agent-index.json", '{"version":1}\n'),
                (root / "agent-index.md", "# Agent index v1\n"),
            ):
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(value, encoding="utf-8")
            subprocess.run(["git", "add", "."], cwd=root, check=True)
            subprocess.run(["git", "commit", "-m", "baseline"], cwd=root, check=True, capture_output=True)
            subprocess.run(["git", "init", "--bare", str(remote)], check=True, capture_output=True)
            subprocess.run(["git", "remote", "add", "origin", str(remote)], cwd=root, check=True)
            subprocess.run(["git", "push", "-u", "origin", "main"], cwd=root, check=True, capture_output=True)
            baseline_head = subprocess.run(
                ["git", "rev-parse", "HEAD"], cwd=root, check=True, text=True, capture_output=True
            ).stdout.strip()
            (root / "wiki/index.md").write_text("published\n", encoding="utf-8")
            (root / "agent-index.json").write_text(
                '{"version":2}\n', encoding="utf-8"
            )
            (root / "agent-index.md").write_text(
                "# Agent index v2\n", encoding="utf-8"
            )
            with patch.object(monitor, "ROOT", root), patch.object(
                monitor, "STATE_DIR", root / ".ops/state/youtube-monitor"
            ), redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                published = monitor.maybe_commit_and_push(True, "published candidate")

            published_head = subprocess.run(
                ["git", "rev-parse", "HEAD"], cwd=root, check=True, text=True, capture_output=True
            ).stdout.strip()
            remote_head = subprocess.run(
                ["git", "--git-dir", str(remote), "rev-parse", "refs/heads/main"],
                check=True,
                text=True,
                capture_output=True,
            ).stdout.strip()
            self.assertEqual(0, published["push_returncode"])
            self.assertNotEqual(baseline_head, published_head)
            self.assertEqual(published_head, remote_head)
            self.assertEqual(
                '{"version":2}\n',
                subprocess.run(
                    ["git", "--git-dir", str(remote), "show", "main:agent-index.json"],
                    check=True,
                    text=True,
                    capture_output=True,
                ).stdout,
            )
            self.assertEqual(
                "",
                subprocess.run(
                    ["git", "status", "--porcelain"],
                    cwd=root,
                    check=True,
                    text=True,
                    capture_output=True,
                ).stdout,
            )

            (root / "wiki/index.md").write_text(
                "published but local sync pending\n", encoding="utf-8"
            )
            real_run = monitor.run

            def fail_local_ref(command, **kwargs):
                if command[:2] == ["git", "update-ref"]:
                    return Mock(returncode=1, stdout="", stderr="locked")
                return real_run(command, **kwargs)

            with patch.object(monitor, "ROOT", root), patch.object(
                monitor, "STATE_DIR", root / ".ops/state/youtube-monitor"
            ), patch.object(monitor, "run", side_effect=fail_local_ref), patch.object(
                monitor.time, "sleep"
            ), redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                pending = monitor.maybe_commit_and_push(True, "pending local sync")

            self.assertEqual("local_sync_pending", pending["local_sync"]["status"])
            self.assertEqual(
                published_head,
                subprocess.run(
                    ["git", "rev-parse", "HEAD"],
                    cwd=root,
                    check=True,
                    text=True,
                    capture_output=True,
                ).stdout.strip(),
            )
            self.assertTrue(
                (root / ".ops/state/youtube-monitor/publish-sync.json").is_file()
            )
            with patch.object(monitor, "ROOT", root), patch.object(
                monitor, "STATE_DIR", root / ".ops/state/youtube-monitor"
            ), redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                recovered = monitor.recover_monitor_publish_sync()
            self.assertEqual("synchronized", recovered["status"])
            published_head = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                cwd=root,
                check=True,
                text=True,
                capture_output=True,
            ).stdout.strip()
            self.assertEqual(pending["commit"], published_head)
            self.assertFalse(
                (root / ".ops/state/youtube-monitor/publish-sync.json").exists()
            )
            self.assertEqual(
                "",
                subprocess.run(
                    ["git", "status", "--porcelain"],
                    cwd=root,
                    check=True,
                    text=True,
                    capture_output=True,
                ).stdout,
            )

            (root / "wiki/index.md").write_text("after\n", encoding="utf-8")
            subprocess.run(
                ["git", "remote", "set-url", "origin", str(root / "missing-remote")],
                cwd=root,
                check=True,
            )

            with patch.object(monitor, "ROOT", root), patch.object(
                monitor, "STATE_DIR", root / ".ops/state/youtube-monitor"
            ), redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                result = monitor.maybe_commit_and_push(True, "candidate")

            current_head = subprocess.run(
                ["git", "rev-parse", "HEAD"], cwd=root, check=True, text=True, capture_output=True
            ).stdout.strip()
            self.assertNotEqual(0, result["push_returncode"])
            self.assertEqual(published_head, current_head)
            self.assertEqual("after\n", (root / "wiki/index.md").read_text(encoding="utf-8"))

    def _run_monitor_item(
        self, transcript_result, slide_result, *, publish_result=None
    ):
        published = datetime.now(timezone.utc).isoformat()
        entry = monitor.VideoEntry("video-1", "World's Fair 2026 Test", published, published, "https://example.test/video")
        with tempfile.TemporaryDirectory() as directory, ExitStack() as stack:
            missing_resource = Path(directory) / "missing.md"
            stack.enter_context(patch.dict(monitor.os.environ, {"AIE_WF2026_MONITOR_AUTO_PUSH": "0"}))
            stack.enter_context(
                patch.object(
                    monitor,
                    "fetch_official_playlist",
                    return_value=([], {"status": "fixture"}),
                )
            )
            stack.enter_context(patch.object(monitor, "fetch_rss", return_value=[entry]))
            stack.enter_context(patch.object(monitor, "update_channel_snapshot", return_value=False))
            stack.enter_context(patch.object(monitor, "read_talk_pages", return_value=[]))
            stack.enter_context(patch.object(monitor, "event_entries", return_value=[(entry, [])]))
            stack.enter_context(patch.object(monitor, "discover_recent_channel_event_rows", return_value=([], {"status": "fixture"})))
            stack.enter_context(patch.object(monitor, "scheduled_manifest_video_ids", return_value=set()))
            stack.enter_context(patch.object(monitor, "pending_manifest_video_ids", return_value=set()))
            stack.enter_context(patch.object(monitor, "update_official_video_manifest", return_value=False))
            stack.enter_context(
                patch.object(monitor, "refresh_manifest_artifact_statuses", return_value=False)
            )
            stack.enter_context(patch.object(monitor, "resource_path", return_value=missing_resource))
            stack.enter_context(patch.object(monitor, "try_import_captions", return_value=transcript_result))
            stack.enter_context(patch.object(monitor, "try_extract_slides", return_value=slide_result))
            stack.enter_context(patch.object(monitor, "write_resource_page", return_value=False))
            stack.enter_context(patch.object(monitor, "update_talk_pages", return_value=0))
            enrichment = stack.enter_context(patch.object(monitor, "run_enrichment", return_value=[]))
            publish = stack.enter_context(
                patch.object(
                    monitor,
                    "maybe_commit_and_push",
                    return_value=publish_result or {"enabled": False},
                )
            )
            write_status = stack.enter_context(patch.object(monitor, "write_status"))
            returncode = monitor.main([])
            report = write_status.call_args.args[0]
        return returncode, report, enrichment, publish

    def _run_dry_monitor_rows(self, rss_rows, channel_rows, *, playlist_entries=None):
        with tempfile.TemporaryDirectory() as directory, ExitStack() as stack:
            root = Path(directory)
            missing_resource = root / "missing.md"
            stack.enter_context(
                patch.dict(monitor.os.environ, {"AIE_WF2026_MONITOR_AUTO_PUSH": "0"})
            )
            stack.enter_context(
                patch.object(monitor, "OFFICIAL_VIDEO_MANIFEST", root / "manifest.json")
            )
            stack.enter_context(
                patch.object(
                    monitor,
                    "fetch_official_playlist",
                    return_value=(list(playlist_entries or []), {"status": "fixture"}),
                )
            )
            stack.enter_context(
                patch.object(
                    monitor,
                    "fetch_rss",
                    return_value=[entry for entry, _matched in rss_rows],
                )
            )
            stack.enter_context(patch.object(monitor, "read_talk_pages", return_value=[]))
            stack.enter_context(patch.object(monitor, "event_entries", return_value=rss_rows))
            stack.enter_context(
                patch.object(
                    monitor,
                    "discover_recent_channel_event_rows",
                    return_value=(channel_rows, {"status": "fixture"}),
                )
            )
            stack.enter_context(
                patch.object(monitor, "scheduled_manifest_video_ids", return_value=set())
            )
            stack.enter_context(
                patch.object(monitor, "pending_manifest_video_ids", return_value=set())
            )
            stack.enter_context(
                patch.object(monitor, "no_slides_manifest_video_ids", return_value=set())
            )
            manifest_update = stack.enter_context(
                patch.object(monitor, "update_official_video_manifest", return_value=False)
            )
            stack.enter_context(patch.object(monitor, "resource_path", return_value=missing_resource))
            stdout = io.StringIO()
            with redirect_stdout(stdout):
                self.assertEqual(0, monitor.main(["--dry-run", "--no-auto-push"]))
            report = json.loads(stdout.getvalue())
        return report, manifest_update


if __name__ == "__main__":
    unittest.main()
