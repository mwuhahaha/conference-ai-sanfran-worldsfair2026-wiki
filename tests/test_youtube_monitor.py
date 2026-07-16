import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from scripts import monitor_official_youtube as monitor


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


if __name__ == "__main__":
    unittest.main()
