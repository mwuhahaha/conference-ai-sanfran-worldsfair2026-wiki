import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "enrich_evolution_context.py"
SPEC = importlib.util.spec_from_file_location("enrich_evolution_context", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


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


if __name__ == "__main__":
    unittest.main()
