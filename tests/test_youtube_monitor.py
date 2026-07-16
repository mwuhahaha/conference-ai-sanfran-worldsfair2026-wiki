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
