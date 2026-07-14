import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from third_party_connection_policy import assess_connection, normalize_url
from audit_third_party_connections import metadata_corroborates_company
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
