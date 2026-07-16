import tempfile
import unittest
from pathlib import Path

from scripts import extract_video_slides as slides


class ExtractVideoSlidesTests(unittest.TestCase):
    def test_merge_bullet_section_preserves_existing_items(self):
        with tempfile.TemporaryDirectory() as directory:
            page = Path(directory) / "topic.md"
            page.write_text("# Topic\n\n## Supporting Decks\n- [[existing]]\n", encoding="utf-8")

            slides.merge_bullet_section(page, "Supporting Decks", ["- [[new]]"])

            text = page.read_text(encoding="utf-8")
            self.assertIn("- [[existing]]", text)
            self.assertIn("- [[new]]", text)


if __name__ == "__main__":
    unittest.main()
