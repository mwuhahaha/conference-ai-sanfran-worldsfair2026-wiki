import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import extract_video_slides as slides
from scripts import slide_session_projection as projection


class ExtractVideoSlidesTests(unittest.TestCase):
    def test_merge_bullet_section_preserves_existing_items(self):
        with tempfile.TemporaryDirectory() as directory:
            page = Path(directory) / "topic.md"
            page.write_text("# Topic\n\n## Supporting Decks\n- [[existing]]\n", encoding="utf-8")

            slides.merge_bullet_section(page, "Supporting Decks", ["- [[new]]"])

            text = page.read_text(encoding="utf-8")
            self.assertIn("- [[existing]]", text)
            self.assertIn("- [[new]]", text)

    def test_manifest_sessions_replace_heuristic_matches_including_empty(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            sources = root / "raw" / "sources"
            talks = root / "wiki" / "talks"
            sources.mkdir(parents=True)
            talks.mkdir(parents=True)
            heuristic_rows = [
                {
                    "id": talk_id,
                    "title": title,
                    "related_video": {"video_id": video_id},
                }
                for video_id, talk_id, title in [
                    ("part-video", "part-1", "Part 1"),
                    ("part-video", "part-2", "Part 2"),
                    ("part-video", "part-3", "Part 3"),
                    ("empty-video", "part-2", "Part 2"),
                ]
            ]
            (sources / "speaker-video-map.json").write_text(
                json.dumps(heuristic_rows), encoding="utf-8"
            )
            (sources / "official-wf26-video-manifest.json").write_text(
                json.dumps(
                    {
                        "videos": [
                            {"id": "part-video", "matchedTalks": ["part-1"]},
                            {"id": "empty-video", "matchedTalks": []},
                        ]
                    }
                ),
                encoding="utf-8",
            )
            (talks / "registry.json").write_text(
                json.dumps(
                    [
                        {"id": "part-1", "title": "Part 1"},
                        {"id": "part-2", "title": "Part 2"},
                        {"id": "part-3", "title": "Part 3"},
                    ]
                ),
                encoding="utf-8",
            )

            with patch.object(slides, "ROOT", root):
                result = slides.related_sessions_by_video()

            self.assertEqual(["part-1"], [row["id"] for row in result["part-video"]])
            self.assertEqual([], result["empty-video"])

    def test_manifest_unknown_talk_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            sources = root / "raw" / "sources"
            talks = root / "wiki" / "talks"
            sources.mkdir(parents=True)
            talks.mkdir(parents=True)
            (sources / "speaker-video-map.json").write_text("[]", encoding="utf-8")
            (sources / "official-wf26-video-manifest.json").write_text(
                json.dumps(
                    {"videos": [{"id": "part-video", "matchedTalks": ["missing"]}]}
                ),
                encoding="utf-8",
            )
            (talks / "registry.json").write_text("[]", encoding="utf-8")

            with patch.object(slides, "ROOT", root), self.assertRaisesRegex(
                ValueError, "references missing talk"
            ):
                slides.related_sessions_by_video()

    def test_topic_session_reconciliation_uses_all_decks_and_preserves_manual_links(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            slide_dir = root / "wiki" / "slides"
            topic_dir = root / "wiki" / "topics"
            slide_dir.mkdir(parents=True)
            topic_dir.mkdir(parents=True)
            talks = [
                {"id": "part-1", "title": "Part 1"},
                {"id": "part-2", "title": "Part 2"},
                {"id": "part-3", "title": "Part 3"},
                {"id": "other-talk", "title": "Independent Deck Talk"},
            ]
            (slide_dir / "youtube-partvideo01-slides.md").write_text(
                "# Part deck\n\n"
                "## Related Scheduled Sessions\n"
                "- [[part-1]] — Part 1\n\n"
                "## Extracted Slides\npart OCR bytes\n",
                encoding="utf-8",
            )
            (slide_dir / "youtube-othervideo1-slides.md").write_text(
                "# Other deck\n\n"
                "## Related Scheduled Sessions\n"
                "- [[other-talk]] — Independent Deck Talk\n\n"
                "## Extracted Slides\nother OCR bytes\n",
                encoding="utf-8",
            )
            topic = topic_dir / "topic.md"
            manual = (
                "## Connections\n"
                "- [[part-2]] — independently sourced manual relationship\n"
                "- [[manual-only]] — unrelated manual relationship\n"
            )
            topic.write_text(
                "# Topic\n\n"
                "## Slide-Derived Scheduled Session Signals\n"
                "- [[part-1]] — Part 1\n"
                "- [[part-2]] — stale Part 2\n"
                "- [[part-3]] — stale Part 3\n"
                "\n"
                "## Slide-Derived Supporting Decks\n"
                "- [[youtube-partvideo01-slides]] — part deck\n"
                "- [[youtube-othervideo1-slides]] — other deck\n\n"
                + manual,
                encoding="utf-8",
            )

            changed = slides.reconcile_topic_slide_session_signals(
                talks,
                slides_dir=slide_dir,
                topics_dir=topic_dir,
                write=True,
            )
            first = topic.read_bytes()
            text = first.decode()
            owned = projection.markdown_section(
                text, "Slide-Derived Scheduled Session Signals"
            )

            self.assertEqual([topic], changed)
            self.assertIn("[[part-1]]", owned)
            self.assertIn("[[other-talk]]", owned)
            self.assertNotIn("[[part-2]]", owned)
            self.assertNotIn("[[part-3]]", owned)
            self.assertIn(manual, text)
            self.assertEqual(
                [],
                slides.reconcile_topic_slide_session_signals(
                    talks,
                    slides_dir=slide_dir,
                    topics_dir=topic_dir,
                    write=True,
                ),
            )
            self.assertEqual(first, topic.read_bytes())


if __name__ == "__main__":
    unittest.main()
