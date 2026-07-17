import json
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path
from unittest.mock import patch


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import audit_third_party_connections as connection_audit
from third_party_connection_policy import assess_connection, normalize_url
from audit_third_party_connections import (
    audit_public_ranking_artifacts,
    forbidden_json_key_paths,
    metadata_corroborates_company,
    official_tool_maintainer_evidence,
    package_project_names,
    public_ranking_markers,
    scan_publishable_artifacts,
)
from discover_external_event_videos import public_report
import enrich_from_youtube_transcripts as youtube_enrichment
import build_worldsfair_wiki as worldsfair_builder
import fetch_company_profiles as company_profile_fetch
from build_worldsfair_wiki import public_speaker_video_map
from fetch_company_profiles import Candidate, validate_company_candidate
from generate_livestream_talk_segments import public_match


class ThirdPartyConnectionPolicyTests(unittest.TestCase):
    def test_company_profile_fetch_defaults_to_private_candidate_state(self):
        self.assertEqual(
            company_profile_fetch.PROFILES,
            company_profile_fetch.ROOT
            / ".ops/state/cache/wiki-maker/credibility-v2/company-profile-candidates.json",
        )
        self.assertEqual(
            company_profile_fetch.resolve_profiles_path(
                Path("raw/sources/company-profiles.json")
            ),
            company_profile_fetch.ROOT / "raw/sources/company-profiles.json",
        )

    def test_private_profile_state_bootstraps_legacy_without_rewriting_public_source(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            private = (
                root
                / ".ops/state/cache/wiki-maker/credibility-v2/company-profile-candidates.json"
            )
            legacy = root / "raw/sources/company-profiles.json"
            legacy.parent.mkdir(parents=True)
            legacy.write_text(
                json.dumps({"example": {"website": "https://example.com/"}}),
                encoding="utf-8",
            )
            before = legacy.read_bytes()

            with (
                patch.object(company_profile_fetch, "ROOT", root),
                patch.object(company_profile_fetch, "PROFILES", private),
            ):
                profiles, bootstrapped = company_profile_fetch.load_profiles_for_run(
                    private
                )

            self.assertTrue(bootstrapped)
            self.assertIn("example", profiles)
            self.assertEqual(legacy.read_bytes(), before)
            self.assertFalse(private.exists())

    def test_livestream_public_match_omits_internal_ranking_mechanics(self):
        result = public_match(
            {
                "talk_slug": "example-talk",
                "confidence": "high",
                "confidence_score": 141,
                "matched_speakers": ["Example Speaker"],
                "matched_title_terms": ["example"],
                "match_basis": "speaker and title",
                "evidence_excerpt": "Transcript evidence.",
            }
        )

        self.assertEqual(
            result,
            {
                "talk_slug": "example-talk",
                "confidence": "high",
                "evidence_excerpt": "Transcript evidence.",
            },
        )

    def test_public_speaker_video_map_omits_candidate_ranking_inputs(self):
        result = public_speaker_video_map(
            [
                {
                    "title": "Example Talk",
                    "related_video": {
                        "score": 105,
                        "speaker_hit": ["Example Speaker"],
                        "topic_overlap": 5,
                        "video_id": "abc123",
                        "relationship": "supporting context",
                    },
                }
            ]
        )

        self.assertEqual(
            result,
            [
                {
                    "title": "Example Talk",
                    "related_video": {
                        "video_id": "abc123",
                        "relationship": "supporting context",
                    },
                }
            ],
        )

    def test_speaker_video_map_writer_keeps_diagnostics_only_in_private_state(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "input.json"
            rows = [
                {
                    "title": "Example Talk",
                    "related_video": {
                        "score": 105,
                        "speaker_hit": ["Example Speaker"],
                        "topic_overlap": 5,
                        "video_id": "abc123",
                    },
                }
            ]
            source.write_text(json.dumps(rows), encoding="utf-8")
            with patch.object(worldsfair_builder, "ROOT", root):
                worldsfair_builder.write_speaker_video_maps(source)

            private_rows = json.loads(
                (
                    root
                    / ".ops/state/cache/source-matching/speaker-video-map.json"
                ).read_text(encoding="utf-8")
            )
            public_rows = json.loads(
                (root / "raw/sources/speaker-video-map.json").read_text(
                    encoding="utf-8"
                )
            )

        self.assertEqual(rows, private_rows)
        self.assertEqual(
            [{"title": "Example Talk", "related_video": {"video_id": "abc123"}}],
            public_rows,
        )

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

    def test_curator_publication_approval_does_not_imply_endorsement(self):
        result = assess_connection(
            {"official_exact_source": True, "curator_approved": True},
            identity_required=True,
        )
        self.assertEqual(result["endorsement_status"], "not_endorsed")
        self.assertEqual(result["disposition"], "approved_connection")

    def test_explicit_endorsement_is_separate_from_publication(self):
        result = assess_connection(
            {"official_exact_source": True, "explicit_endorsement": True},
            identity_required=True,
        )
        self.assertEqual(result["endorsement_status"], "endorsed")
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

    def test_v2_company_audit_separates_candidate_risk_from_public_enforcement(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            wiki_page = root / "wiki/companies/apify.md"
            wiki_page.parent.mkdir(parents=True)
            wiki_page.write_text(
                "---\ntitle: Apify\n---\n# Apify\n\nOfficial roster context only.\n",
                encoding="utf-8",
            )
            profiles_path = (
                root
                / ".ops/state/cache/wiki-maker/credibility-v2/company-profile-candidates.json"
            )
            profiles_path.parent.mkdir(parents=True)
            profiles_path.write_text(
                json.dumps(
                    {
                        "apify": {
                            "website": "https://apify.ai/",
                            "summary": "Apify.ai provides unrelated WhatsApp automation.",
                            "fetchStatus": "fetched",
                            "origin": "Discovered by domain-guess.",
                            "fetchedMetadata": {
                                "title": "Apify.ai",
                                "description": "Apify.ai provides WhatsApp automation.",
                            },
                            "sourceLinks": [
                                {"url": "https://apify.ai/", "label": "Apify.ai"}
                            ],
                        }
                    }
                ),
                encoding="utf-8",
            )
            policy_path = profiles_path.parent / "writing-policy.json"
            policy_path.write_text(
                json.dumps(
                    {
                        "companyProfileGateStates": {
                            "apify": {"status": "held"}
                        },
                        "companyProfileWritingDecisions": {
                            "apify": {"writingDisposition": "omit"}
                        },
                    }
                ),
                encoding="utf-8",
            )
            findings = []
            counters = Counter()

            connection_audit.audit_company_profiles(
                findings,
                counters,
                root,
            )

            self.assertIn(
                "same_name_company_candidate_held_by_v2_identity_gate",
                {row["kind"] for row in findings},
            )
            self.assertNotIn(
                "held_company_profile_reached_public_artifact",
                {row["kind"] for row in findings},
            )
            self.assertEqual(
                counters["held_company_profiles_absent_from_public_artifacts"],
                1,
            )
            self.assertNotIn(
                "unvalidated_company_candidates_in_public_source",
                {row["kind"] for row in findings},
            )

            wiki_page.write_text(
                "---\ntitle: Apify\n---\n# Apify\n\nhttps://apify.ai/\n",
                encoding="utf-8",
            )
            findings = []
            counters = Counter()
            connection_audit.audit_company_profiles(findings, counters, root)

            self.assertIn(
                "held_company_profile_reached_public_artifact",
                {row["kind"] for row in findings},
            )
            self.assertEqual(
                counters["held_company_profile_public_enforcement_failures"],
                1,
            )

    def test_company_audit_flags_legacy_public_candidate_source(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            raw = root / "raw/sources"
            raw.mkdir(parents=True)
            (raw / "company-profiles.json").write_text(
                json.dumps(
                    {
                        "example": {
                            "website": "https://example.invalid/",
                            "fetchStatus": "unknown",
                        }
                    }
                ),
                encoding="utf-8",
            )
            findings = []
            counters = Counter()

            connection_audit.audit_company_profiles(findings, counters, root)

            self.assertIn(
                "unvalidated_company_candidates_in_public_source",
                {row["kind"] for row in findings},
            )

    def test_company_audit_accepts_explicit_candidate_path_outside_project(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory)
            root = workspace / "project"
            (root / "wiki/companies").mkdir(parents=True)
            profile_path = workspace / "company-profile-candidates.json"
            profile_path.write_text(
                json.dumps(
                    {
                        "example": {
                            "website": "https://example.invalid/",
                            "fetchStatus": "unknown",
                        }
                    }
                ),
                encoding="utf-8",
            )
            policy_path = workspace / "writing-policy.json"
            policy_path.write_text("{}", encoding="utf-8")
            findings = []
            counters = Counter()

            connection_audit.audit_company_profiles(
                findings,
                counters,
                root,
                profile_path=profile_path,
                policy_path=policy_path,
            )

            self.assertIn(
                str(profile_path.resolve()),
                findings[0]["evidence"],
            )

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

    def test_publishable_tree_scan_finds_structural_markdown_json_and_html_leaks(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "wiki").mkdir()
            (root / "dist").mkdir()
            (root / "wiki" / "page.md").write_text(
                "---\ntitle: Unsafe\ninternal_score: 0.91\n---\n\nCandidate (match score 92).\n"
            )
            (root / "dist" / "agent.json").write_text(
                json.dumps({"id": "unsafe", "rankingWeight": 0.7})
            )
            (root / "dist" / "index.html").write_text(
                '<html><body><div data-candidate-rank="2">Candidate</div></body></html>'
            )

            scan = scan_publishable_artifacts(root)
            findings = []
            counters = Counter()
            leak_count = audit_public_ranking_artifacts(findings, counters, root)

            self.assertFalse(scan.ok)
            self.assertEqual({issue.artifact_format for issue in scan.issues}, {"markdown", "json", "html"})
            self.assertEqual(leak_count, len(scan.issues))
            self.assertEqual(counters["publishable_artifact_files_scanned"], 3)
            self.assertEqual({finding["page"] for finding in findings}, {"wiki/page.md", "dist/agent.json", "dist/index.html"})

    def test_publishable_tree_scan_keeps_source_backed_score_discussion(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "wiki").mkdir()
            (root / "dist").mkdir()
            prose = (
                "According to the linked conference transcript, the evaluation scores rose from "
                "71 to 84, while benchmark rankings still required task-specific context."
            )
            (root / "wiki" / "evaluation.md").write_text(
                "---\nsourceLabels: [Conference transcript]\n---\n\n" + prose + "\n"
            )
            (root / "dist" / "evaluation.json").write_text(
                json.dumps({"content": prose, "confidence": "high", "sourceLabels": ["Conference transcript"]})
            )
            (root / "dist" / "evaluation.html").write_text(f"<p>{prose}</p>")

            scan = scan_publishable_artifacts(root)

            self.assertTrue(scan.ok)
            self.assertEqual(len(scan.checked_files), 3)

    def test_raw_source_scan_separates_internal_match_metadata_from_measurements(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            raw = root / "raw" / "sources"
            raw.mkdir(parents=True)
            (raw / "livestream-match.json").write_text(
                json.dumps(
                    {
                        "confidence": "high",
                        "confidence_score": 141,
                        "matched_speakers": ["Example Speaker"],
                        "matched_title_terms": ["example"],
                        "match_basis": "speaker and title",
                    }
                )
            )
            (raw / "technical-measurements.json").write_text(
                json.dumps(
                    {
                        "score": 4,
                        "bestScore": 177.4,
                        "benchmark_score": 0.83,
                        "rank": 2,
                        "weight": 0.7,
                        "ocr_confidence": 0.91,
                        "calibration": {"pixels_per_meter": 18.2},
                        "numeric_ranking_is_internal_only": True,
                    }
                )
            )
            findings = []
            counters = Counter()

            shared = scan_publishable_artifacts(root)
            with patch.object(connection_audit, "_shared_scan_public_artifacts", None):
                standalone = connection_audit.scan_publishable_artifacts(root)
            leak_count = audit_public_ranking_artifacts(findings, counters, root)

            self.assertEqual(
                [
                    (issue.path.name, issue.artifact_format, issue.code, issue.marker)
                    for issue in shared.issues
                ],
                [
                    (issue.path.name, issue.artifact_format, issue.code, issue.marker)
                    for issue in standalone.issues
                ],
            )
            self.assertEqual(leak_count, 4)
            self.assertEqual(counters["raw_source_artifact_files_scanned"], 2)
            self.assertEqual(counters["raw_source_artifact_files_without_internal_ranking"], 1)
            self.assertEqual(counters["raw_source_internal_ranking_findings"], 4)
            self.assertEqual(
                {finding["kind"] for finding in findings},
                {"raw_source_internal_ranking_json"},
            )
            self.assertTrue(all(finding["page"] == "raw/sources/livestream-match.json" for finding in findings))

    def test_speaker_video_map_score_uses_parent_and_sibling_matching_context(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            raw = root / "raw" / "sources"
            raw.mkdir(parents=True)
            (raw / "speaker-video-map.json").write_text(
                json.dumps(
                    [
                        {
                            "title": "From Vibes to Production",
                            "speakers": ["Laurie Voss"],
                            "related_video": {
                                "score": 105,
                                "speaker_hit": ["Laurie Voss"],
                                "topic_overlap": 5,
                                "video_id": "Xfl50508LZM",
                                "relationship": (
                                    "speaker-match related prior/adjacent AI Engineer video"
                                ),
                            },
                        }
                    ]
                )
            )

            shared = scan_publishable_artifacts(root)
            with patch.object(connection_audit, "_shared_scan_public_artifacts", None):
                standalone = connection_audit.scan_publishable_artifacts(root)

            shared_signature = [
                (issue.artifact_format, issue.code, issue.location, issue.marker)
                for issue in shared.issues
            ]
            standalone_signature = [
                (issue.artifact_format, issue.code, issue.location, issue.marker)
                for issue in standalone.issues
            ]
            self.assertEqual(shared_signature, standalone_signature)
            self.assertEqual(
                shared_signature,
                [
                    (
                        "json",
                        "internal_metadata_key",
                        "$[0].related_video.score",
                        "score",
                    )
                ],
            )

    def test_publishable_tree_scan_has_standalone_fail_closed_fallback(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "wiki").mkdir()
            (root / "dist").mkdir()
            (root / "wiki" / "unsafe.md").write_text("---\ncandidate_rank: 2\n---\n")
            (root / "dist" / "safe.html").write_text(
                "<p>The conference source compared benchmark scores across tasks.</p>"
            )

            with patch.object(connection_audit, "_shared_scan_public_artifacts", None):
                scan = connection_audit.scan_publishable_artifacts(root)

            self.assertFalse(scan.ok)
            self.assertEqual(len(scan.issues), 1)
            self.assertEqual(scan.issues[0].code, "internal_frontmatter_key")

    def test_shared_and_standalone_scans_align_for_embedded_html_json(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "dist").mkdir()
            for name, script_type in (
                ("json", "application/json"),
                ("json-ld", "application/ld+json"),
            ):
                (root / "dist" / f"{name}.html").write_text(
                    f'<script type="{script_type}">'
                    '{"name":"Candidate","rankingWeight":0.7}'
                    "</script>"
                )

            shared = scan_publishable_artifacts(root)
            with patch.object(connection_audit, "_shared_scan_public_artifacts", None):
                standalone = connection_audit.scan_publishable_artifacts(root)

            shared_signature = [
                (issue.path.name, issue.artifact_format, issue.code, issue.marker)
                for issue in shared.issues
            ]
            standalone_signature = [
                (issue.path.name, issue.artifact_format, issue.code, issue.marker)
                for issue in standalone.issues
            ]
            self.assertEqual(shared_signature, standalone_signature)
            self.assertEqual(len(shared_signature), 2)

    def test_shared_and_standalone_html_scans_align_for_meta_and_blockquotes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "dist").mkdir()
            (root / "dist" / "meta-name.html").write_text(
                '<meta name="rankingWeight" content="0.7">'
            )
            (root / "dist" / "meta-property.html").write_text(
                '<meta property="candidateRank" content="2">'
            )
            (root / "dist" / "quoted-source.html").write_text(
                "<blockquote><p>Related candidate (match score 92).</p></blockquote>"
                "<p>Source-backed discussion outside the quote.</p>"
            )

            shared = scan_publishable_artifacts(root)
            with patch.object(connection_audit, "_shared_scan_public_artifacts", None):
                standalone = connection_audit.scan_publishable_artifacts(root)

            shared_signature = [
                (issue.path.name, issue.artifact_format, issue.code, issue.marker)
                for issue in shared.issues
            ]
            standalone_signature = [
                (issue.path.name, issue.artifact_format, issue.code, issue.marker)
                for issue in standalone.issues
            ]
            self.assertEqual(shared_signature, standalone_signature)
            self.assertEqual(
                shared_signature,
                [
                    ("meta-name.html", "html", "internal_html_metadata", "rankingWeight"),
                    ("meta-property.html", "html", "internal_html_metadata", "candidateRank"),
                ],
            )

    def test_resource_generator_keeps_match_score_internal(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            wiki = root / "wiki"
            resources = wiki / "resources"
            talks = wiki / "talks"
            talks.mkdir(parents=True)
            (talks / "registry.json").write_text("[]\n")
            video = {
                "youtube_title": "Example Talk - Example Speaker, Example Co",
                "youtube_url": "https://www.youtube.com/watch?v=example",
                "source_kind": "channel_video",
            }
            session = {"title": "Example Talk", "speakers": ["Example Speaker"]}

            with patch.object(youtube_enrichment, "WIKI", wiki), patch.object(
                youtube_enrichment, "RESOURCES", resources
            ):
                youtube_enrichment.write_resource(
                    "example",
                    video,
                    "A representative conference transcript with useful engineering details.",
                    [],
                    [(92, session)],
                    is_event_video=True,
                )

            generated = resources / "youtube-example.md"
            text = generated.read_text()
            self.assertIn("[[example-talk]]", text)
            self.assertNotIn("match score", text.lower())
            self.assertTrue(scan_publishable_artifacts(root).ok)

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
