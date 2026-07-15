import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from third_party_connection_policy import assess_connection, normalize_url
from audit_third_party_connections import (
    forbidden_json_key_paths,
    metadata_corroborates_company,
    official_tool_maintainer_evidence,
    package_project_names,
    public_ranking_markers,
)
from discover_external_event_videos import public_report
from fetch_company_profiles import Candidate, validate_company_candidate


class ThirdPartyConnectionPolicyTests(unittest.TestCase):
    def test_name_match_cannot_pass_identity_gate(self):
        result = assess_connection({"exact_name_only": True}, identity_required=True)
        self.assertEqual(result["identity_status"], "unverified")
        self.assertEqual(result["disposition"], "hold_for_review")

    def test_verified_identity_does_not_prove_event_connection(self):
        result = assess_connection({"primary_owner_metadata": True}, identity_required=True, event_claim=True)
        self.assertEqual(result["identity_status"], "verified")
        self.assertEqual(result["event_status"], "unverified")
        self.assertEqual(result["disposition"], "hold_for_review")

    def test_conflict_rejects_regardless_of_positive_signals(self):
        result = assess_connection(
            {"official_exact_source": True, "primary_owner_metadata": True, "identity_conflict": True},
            identity_required=True,
        )
        self.assertEqual(result["identity_status"], "conflict")
        self.assertEqual(result["disposition"], "reject")

    def test_publication_does_not_imply_endorsement(self):
        result = assess_connection({"official_exact_source": True}, identity_required=True)
        self.assertEqual(result["endorsement_status"], "not_endorsed")
        self.assertEqual(result["disposition"], "context_only")

    def test_url_normalization_ignores_www_scheme_and_trailing_slash(self):
        self.assertEqual(
            normalize_url("http://www.linkedin.com/in/example/"),
            "https://linkedin.com/in/example",
        )

    def test_company_brand_corroboration_keeps_ai_and_labs_tokens(self):
        self.assertTrue(metadata_corroborates_company("DatologyAI", "Datology AI | Data curation"))
        self.assertTrue(metadata_corroborates_company("TwelveLabs", "Twelve Labs video intelligence"))
        self.assertFalse(metadata_corroborates_company("Indeed", "Independent bookstore"))

    def test_public_video_report_hides_ranking_signals(self):
        report = {
            "checked_at": "2026-07-14T00:00:00Z",
            "limits": {"max_results": 20},
            "results": [{
                "video": {"id": "abc", "title": "Candidate"},
                "confidence": "high",
                "event_marker": True,
                "usefulness": 0.9,
                "best_match": {
                    "score": 0.91,
                    "title_overlap": 0.8,
                    "reasons": ["speaker exact"],
                    "speaker_hits": ["Example Person"],
                    "session": {"slug": "example-talk", "title": "Example Talk"},
                },
            }],
        }
        result = public_report(report)
        self.assertNotIn("limits", result)
        self.assertNotIn("event_marker", result["results"][0])
        self.assertNotIn("usefulness", result["results"][0])
        self.assertEqual(
            result["results"][0]["best_match"],
            {"session": {"slug": "example-talk", "title": "Example Talk"}},
        )
        self.assertEqual(
            forbidden_json_key_paths(
                result,
                {"score", "title_overlap", "reasons", "speaker_hits", "usefulness", "limits"},
            ),
            [],
        )

    def test_public_ranking_marker_check_ignores_ordinary_confidence_prose(self):
        text = "Confidence in the source is limited, and benchmark scores need context."
        self.assertEqual(public_ranking_markers(text), [])

    def test_public_ranking_marker_check_finds_generated_details(self):
        text = """## External Video Discovery
- Confidence: high (0.81)
- Match evidence: speaker exact
"""
        self.assertEqual(public_ranking_markers(text), ["numeric confidence", "match reasons"])

    def test_package_project_names_extracts_pypi_identity(self):
        text = "[Package](https://pypi.org/project/chrome-agent/)"
        self.assertEqual(package_project_names(text), {"chrome-agent"})

    def test_official_tool_maintainer_requires_roster_and_session_evidence(self):
        descriptions = "We introduce GEPA, a reflective prompt optimizer."
        self.assertTrue(official_tool_maintainer_evidence("GEPA", descriptions))
        self.assertFalse(official_tool_maintainer_evidence("GEPA", "Unrelated session"))
        self.assertFalse(official_tool_maintainer_evidence("Unknown Tool", descriptions))

    def test_company_collector_accepts_owner_metadata_with_spaced_brand_terms(self):
        result = validate_company_candidate(
            "DatologyAI",
            Candidate("https://datologyai.com/", "domain-guess", 20),
            {"url": "https://datologyai.com/", "title": "Datology AI", "description": "Data curation"},
        )
        self.assertEqual(result["identity_status"], "verified")
        self.assertEqual(result["disposition"], "context_only")


if __name__ == "__main__":
    unittest.main()
