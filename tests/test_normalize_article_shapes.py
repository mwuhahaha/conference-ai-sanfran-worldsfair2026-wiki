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
    def test_generator_headings_resolve_to_category_contracts(self):
        cases = {
            "talks": ("Transcript Markdown",),
            "companies": (
                "What It Is",
                "Why It Matters At World's Fair",
                "Related People",
                "Related Scheduled Sessions",
                "Public Sources",
            ),
            "harnesses": (
                "Purpose",
                "Observed At AIE",
                "Recommended Implementation Steps",
                "Source Evidence",
            ),
            "playbooks": ("Purpose", "Source Evidence"),
            "evaluations": ("Source Evidence",),
        }

        for category, headings in cases.items():
            selected = NORMALIZER.WF26_ARTICLE_CONTRACTS.resolve(category)
            self.assertIsNotNone(selected)
            for heading in headings:
                with self.subTest(category=category, heading=heading):
                    self.assertIsNotNone(selected.section_for_heading(heading))

    def test_topic_sections_reorder_without_rewriting_bodies_or_code(self):
        applied_body = (
            "This workflow turns linked source evidence into a bounded implementation plan.\n\n"
            "- Keep provenance labels visible in public output.\n\n"
        )
        code_block = (
            "```bash\n"
            "# This is code, not a Markdown section.\n"
            "wiki-from-topic-maker update ./event-wiki --change-type media\n"
            "```"
        )

        with tempfile.TemporaryDirectory() as directory:
            page = Path(directory) / "wiki" / "topics" / "agent-evaluations.md"
            page.parent.mkdir(parents=True)
            page.write_text(
                "# Agent Evaluations\n\n"
                "## Evidence Graph\n"
                f"{code_block}\n\n"
                "## Significance\n"
                "This theme turns evaluation into an operational gate.\n\n"
                "## Applied Use\n"
                f"{applied_body}",
                encoding="utf-8",
            )

            self.assertTrue(NORMALIZER.normalize_page(page, "topics"))
            normalized = page.read_text(encoding="utf-8")

            self.assertLess(
                normalized.index("## Significance"),
                normalized.index("## Applied Use"),
            )
            self.assertLess(
                normalized.index("## Applied Use"),
                normalized.index("## Evidence Graph"),
            )
            self.assertIn(applied_body.rstrip(), normalized)
            self.assertIn(code_block, normalized)
            self.assertEqual(1, normalized.count("## Applied Use"))
            self.assertFalse(NORMALIZER.normalize_page(page, "topics"))

    def test_playbook_contract_puts_evidence_boundary_last(self):
        with tempfile.TemporaryDirectory() as directory:
            page = Path(directory) / "wiki" / "playbooks" / "trial.md"
            page.parent.mkdir(parents=True)
            page.write_text(
                "# Trial\n\n"
                "## Evidence\nEvidence body.\n\n"
                "## Evidence Boundary\nBoundary body.\n\n"
                "## When To Use\nWhen body.\n\n"
                "## Overview\nOverview body.\n\n"
                "## Steps\nSteps body.\n",
                encoding="utf-8",
            )

            self.assertTrue(NORMALIZER.normalize_page(page, "playbooks"))
            normalized = page.read_text(encoding="utf-8")
            headings = [
                line
                for line in normalized.splitlines()
                if line.startswith("## ")
            ]
            self.assertEqual(
                headings,
                [
                    "## Overview",
                    "## When To Use",
                    "## Steps",
                    "## Evidence",
                    "## Evidence Boundary",
                ],
            )
            self.assertFalse(NORMALIZER.normalize_page(page, "playbooks"))

    def test_talk_keeps_secondary_interview_distinct_and_merges_slide_evidence(self):
        with tempfile.TemporaryDirectory() as directory:
            page = Path(directory) / "wiki" / "talks" / "trial.md"
            page.parent.mkdir(parents=True)
            page.write_text(
                "# Trial\n\n"
                "## Conference Context\nOfficial schedule identity.\n\n"
                "## Session Description\nOfficial description.\n\n"
                "## Media Evidence\nOfficial recording evidence.\n\n"
                "## Slides\nSecondary slide evidence.\n\n"
                "## Secondary Interview Context\nLabeled third-party context.\n\n"
                "## Evidence Graph\nLinked evidence.\n",
                encoding="utf-8",
            )

            self.assertTrue(NORMALIZER.normalize_page(page, "talks"))
            normalized = page.read_text(encoding="utf-8")
            self.assertEqual(1, normalized.count("## Media Evidence"))
            self.assertNotIn("## Supporting Slides", normalized)
            self.assertNotIn("## Slides", normalized)
            self.assertEqual(1, normalized.count("## Secondary Interview Context"))
            self.assertIn("Official recording evidence.", normalized)
            self.assertIn("Secondary slide evidence.", normalized)
            self.assertIn("Labeled third-party context.", normalized)
            self.assertLess(
                normalized.index("## Secondary Interview Context"),
                normalized.index("## Media Evidence"),
            )
            self.assertFalse(NORMALIZER.normalize_page(page, "talks"))

    def test_normalizer_preserves_livestream_projection_sections(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "wiki"
            talk = root / "talks" / "trial.md"
            person = root / "people" / "alice.md"
            talk.parent.mkdir(parents=True)
            person.parent.mkdir(parents=True)
            segment = (
                "- [Watch in livestream at 03:14:28]"
                "(https://www.youtube.com/watch?v=stream00001&t=11668s) — Day 3.\n"
                "- Evidence: transcript-aligned segment.\n"
                "- Confidence: high."
            )
            appearance = (
                "- [[trial|Trial]] — [watch at 03:14:28]"
                "(https://www.youtube.com/watch?v=stream00001&t=11668s) in Day 3."
            )
            talk.write_text(
                "# Trial\n\n"
                "## Evidence Graph\nGraph.\n\n"
                f"## Livestream Segment\n{segment}\n\n"
                "## Conference Context\nContext.\n\n"
                "## Session Description\nDescription.\n\n"
                "## Media Evidence\nMedia.\n",
                encoding="utf-8",
            )
            person.write_text(
                "# Alice\n\n"
                "## Evidence Graph\nGraph.\n\n"
                f"## Livestream Appearances\n{appearance}\n\n"
                "## Profile\nProfile.\n",
                encoding="utf-8",
            )

            self.assertTrue(NORMALIZER.normalize_page(talk, "talks"))
            self.assertTrue(NORMALIZER.normalize_page(person, "people"))
            self.assertIn(f"## Livestream Segment\n{segment}", talk.read_text())
            self.assertIn(
                f"## Livestream Appearances\n{appearance}", person.read_text()
            )
            self.assertFalse(NORMALIZER.normalize_page(talk, "talks"))
            self.assertFalse(NORMALIZER.normalize_page(person, "people"))


if __name__ == "__main__":
    unittest.main()
