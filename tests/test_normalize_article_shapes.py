import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "normalize_article_shapes.py"
SPEC = importlib.util.spec_from_file_location("normalize_article_shapes_prose_test", SCRIPT)
NORMALIZER = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(NORMALIZER)


class NormalizeArticleShapesTest(unittest.TestCase):
    def test_repeated_applied_use_prose_is_deduplicated_without_losing_structure(self):
        paragraphs = [
            "This workflow turns linked source evidence into a bounded implementation plan.",
            "Operators should preserve source roles before promoting any derived recommendation.",
            "Agents can then verify the change against explicit acceptance criteria.",
        ]
        repeated_prose = "\n\n".join(paragraphs * 6)
        list_block = (
            "- Run targeted checks before changing a gate.\n"
            "- Keep provenance labels visible in public output."
        )
        code_block = (
            "```bash\n"
            "wiki-from-topic-maker update ./event-wiki --change-type media\n"
            "```"
        )

        with tempfile.TemporaryDirectory() as directory:
            page = Path(directory) / "wiki" / "topics" / "agent-evaluations.md"
            page.parent.mkdir(parents=True)
            page.write_text(
                "# Agent Evaluations\n\n"
                "## Applied Use\n"
                f"{repeated_prose}\n\n{list_block}\n\n{code_block}\n",
                encoding="utf-8",
            )

            self.assertTrue(NORMALIZER.normalize_page(page, "topics"))
            normalized = page.read_text(encoding="utf-8")

            for paragraph in paragraphs:
                self.assertEqual(1, normalized.count(paragraph))
            self.assertIn(list_block, normalized)
            self.assertIn(code_block, normalized)
            self.assertEqual(1, normalized.count("## Applied Use"))
            self.assertFalse(NORMALIZER.normalize_page(page, "topics"))


if __name__ == "__main__":
    unittest.main()
