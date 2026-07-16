import importlib.util
import io
import json
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "enrich_evolution_context.py"
SPEC = importlib.util.spec_from_file_location("enrich_evolution_context", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)

NORMALIZER_SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "normalize_article_shapes.py"
NORMALIZER_SPEC = importlib.util.spec_from_file_location("normalize_article_shapes_contract_test", NORMALIZER_SCRIPT)
NORMALIZER = importlib.util.module_from_spec(NORMALIZER_SPEC)
assert NORMALIZER_SPEC.loader
NORMALIZER_SPEC.loader.exec_module(NORMALIZER)


class EvolutionContextTest(unittest.TestCase):
    def setUp(self):
        self.profile = {
            "schemaVersion": 1,
            "comparisonSource": "delta",
            "comparisonBoundary": "Comparison only.",
            "stages": [{"id": "past", "label": "Past", "evidenceRole": "fixture"}],
            "themes": [{
                "id": "theme",
                "match": {"categories": ["topics"], "slugs": ["agents"]},
                "evidenceGate": {"minimumMatches": 2, "requiredAny": ["source-a", "source-b", "source-c"]},
                "evolution": {"past": "The earlier framing."},
                "whyNow": "It matters now.",
                "practicalLesson": "Test the whole loop.",
                "confidence": "medium",
            }],
        }

    def test_evidence_gate_requires_configured_local_links(self):
        path = Path("wiki/topics/agents.md")
        self.assertIsNone(MODULE.matching_theme(path, "# Agents\n\n[[source-a]]\n", self.profile))
        theme = MODULE.matching_theme(path, "# Agents\n\n[[source-a]] [[source-b|B]]\n", self.profile)
        self.assertEqual("theme", theme["id"])

    def test_enrichment_is_idempotent_and_labels_boundary(self):
        original = "# Agents\n\n[[source-a]] [[source-b]]\n"
        theme = {**self.profile["themes"][0], "matchedEvidence": ["source-a", "source-b"]}
        enriched = MODULE.enrich(original, theme, self.profile)
        self.assertEqual(enriched, MODULE.enrich(enriched, theme, self.profile))
        for heading in MODULE.SECTION_NAMES:
            self.assertEqual(1, enriched.count(f"## {heading}"))
        self.assertIn("Comparison only.", enriched)
        self.assertIn("Confidence:", enriched)
        self.assertIn("[[delta]]", enriched)
        self.assertNotIn("[[source-c]]", enriched)

    def test_profile_rejects_unknown_stage(self):
        self.profile["themes"][0]["evolution"] = {"missing": "No source."}
        with self.assertRaisesRegex(ValueError, "unknown stages"):
            MODULE.validate_profile(self.profile)

    def test_check_and_dry_run_leave_eligible_page_byte_identical(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            page = root / "wiki" / "topics" / "agents.md"
            page.parent.mkdir(parents=True)
            page.write_text("# Agents\n\n[[source-a]] [[source-b]]\n", encoding="utf-8")
            profile_path = root / "profile.json"
            profile_path.write_text(json.dumps(self.profile), encoding="utf-8")
            before = page.read_bytes()

            with patch.object(MODULE, "ROOT", root), patch.object(MODULE, "WIKI", root / "wiki"):
                with redirect_stdout(io.StringIO()):
                    self.assertEqual(
                        0,
                        MODULE.main(["--profile", str(profile_path), "--path", "wiki/topics/agents.md", "--dry-run"]),
                    )
                    self.assertEqual(
                        1,
                        MODULE.main(["--profile", str(profile_path), "--path", "wiki/topics/agents.md", "--check"]),
                    )

            self.assertEqual(before, page.read_bytes())

    def test_normalizer_check_reports_drift_without_rewriting_whole_page(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            page = root / "wiki" / "topics" / "agents.md"
            page.parent.mkdir(parents=True)
            page.write_text(
                "# Agents\n\n## Why It Matters\nImportant.\n\n## Overview\nSummary.\n",
                encoding="utf-8",
            )
            before = page.read_bytes()

            with patch.object(NORMALIZER, "ROOT", root), patch.object(NORMALIZER, "WIKI", root / "wiki"):
                with redirect_stdout(io.StringIO()):
                    self.assertEqual(1, NORMALIZER.main(["--kind", "topics", "--check"]))

            self.assertEqual(before, page.read_bytes())
            self.assertEqual("whole_page", NORMALIZER.WRITER_CONTRACT["scope"])
            self.assertFalse(NORMALIZER.WRITER_CONTRACT["incremental_safe"])

    def test_normalizer_deduplicates_slide_alias_content_across_repeated_runs(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            page = root / "wiki" / "talks" / "example.md"
            page.parent.mkdir(parents=True)
            page.write_text(
                "# Example\n\n"
                "## Media Evidence\n"
                "- Source video: `youtube-AAAAAAAAAAA`\n"
                "![[assets/slides/AAAAAAAAAAA/slide-001.jpg]]\n\n"
                "## Slides\n"
                "- Source video: `youtube-AAAAAAAAAAA`\n"
                "![[assets/slides/AAAAAAAAAAA/slide-001.jpg]]\n",
                encoding="utf-8",
            )

            self.assertTrue(NORMALIZER.normalize_page(page, "talks"))
            normalized = page.read_text(encoding="utf-8")
            self.assertEqual(1, normalized.count("## Media Evidence"))
            self.assertNotIn("## Slides", normalized)
            self.assertEqual(1, normalized.count("- Source video: `youtube-AAAAAAAAAAA`"))
            self.assertEqual(
                1,
                normalized.count("![[assets/slides/AAAAAAAAAAA/slide-001.jpg]]"),
            )
            self.assertFalse(NORMALIZER.normalize_page(page, "talks"))

    def test_normalizer_rejects_help_and_unknown_arguments_before_generation(self):
        for argv in (["--help"], ["--unknown"], ["--chec"]):
            with self.subTest(argv=argv), patch.object(NORMALIZER, "normalize_page") as generator:
                with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                    NORMALIZER.main(argv)
                generator.assert_not_called()


if __name__ == "__main__":
    unittest.main()
