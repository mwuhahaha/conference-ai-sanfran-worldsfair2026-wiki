import importlib.util
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from wiki_from_topic_maker.credibility_v2 import DimensionName
from wiki_from_topic_maker.credibility_v2.scoring import (
    DimensionCap,
    EvidenceKind,
    ScoreRule,
    ScoreRuleset,
    SourceRole,
)


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build_private_credibility_v2.py"
SPEC = importlib.util.spec_from_file_location("build_private_credibility_v2_test", SCRIPT)
POLICY = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
sys.modules[SPEC.name] = POLICY
SPEC.loader.exec_module(POLICY)


def _write_test_scoring_policy(root: Path) -> Path:
    ruleset = ScoreRuleset.create(
        ruleset_version="test-v1",
        policy_name="Synthetic test-only WF26 scoring policy",
        policy_sources=("https://example.test/scoring-methodology",),
        rules=(
            ScoreRule(
                rule_id="test-direct-primary",
                rule_version="test-v1",
                evidence_kind=EvidenceKind.DIRECT_PRIMARY_RECORD,
                dimension=DimensionName.CLAIM_SUPPORT,
                base_points=10,
                description="Synthetic positive primary-record evidence.",
                allowed_source_roles=(SourceRole.OFFICIAL_PRIMARY,),
            ),
            ScoreRule(
                rule_id="test-owner-assertion",
                rule_version="test-v1",
                evidence_kind=EvidenceKind.OWNER_ASSERTION,
                dimension=DimensionName.CLAIM_SUPPORT,
                base_points=3,
                description="Synthetic attributed owner evidence.",
                allowed_source_roles=(SourceRole.FIRST_PARTY,),
            ),
        ),
        dimension_caps=(
            DimensionCap(DimensionName.CLAIM_SUPPORT, -100, 100),
        ),
    )
    path = (
        root
        / ".ops/state/cache/wiki-maker/credibility-v2/scoring-policies/active.json"
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(ruleset.as_dict(), sort_keys=True), encoding="utf-8")
    return path


def _fixture(tmp_path: Path) -> Path:
    root = tmp_path / "project"
    raw = root / "raw" / "sources"
    transcripts = raw / "youtube-transcripts"
    resources = root / "wiki" / "resources"
    transcripts.mkdir(parents=True)
    resources.mkdir(parents=True)
    (raw / "official-wf26-video-manifest.json").write_text(
        json.dumps(
            {
                "schemaVersion": 1,
                "checkedAt": "2026-07-16T20:00:00Z",
                "videos": [
                    {
                        "id": "aaaaaaaaaaa",
                        "title": "Agent evaluation quality gates",
                        "mediaType": "talk_recording",
                        "associationEvidence": "official_wf26_playlist_membership",
                        "uploadDate": "2026-07-16",
                    },
                    {
                        "id": "bbbbbbbbbbb",
                        "title": "Evals for production agents",
                        "mediaType": "talk_recording",
                        "associationEvidence": "official_wf26_playlist_membership",
                        "uploadDate": "2026-07-16",
                    },
                    {
                        "id": "ccccccccccc",
                        "mediaType": "unavailable_playlist_item",
                        "associationEvidence": "official_wf26_playlist_membership",
                    },
                ],
            }
        ),
        encoding="utf-8",
    )
    (raw / "official-speakers.json").write_text(
        json.dumps(
            {
                "speakers": [
                    {
                        "name": "Example Person",
                        "role": "Clinical Documentation Engineer",
                        "company": "Example Co",
                        "website": "https://example.com/team/example-person",
                    },
                    {
                        "name": "Other Person",
                        "role": "Agent Evaluation Engineer",
                        "company": "Other Labs",
                    },
                ]
            }
        ),
        encoding="utf-8",
    )
    (raw / "official-sessions.json").write_text(
        json.dumps(
            {
                "website": "https://ai.engineer/worldsfair",
                "scheduleVersion": 1,
                "sessions": [],
            }
        ),
        encoding="utf-8",
    )
    (raw / "company-profiles.json").write_text(
        json.dumps(
            {
                "example-co": {
                    "website": "https://example.com/",
                    "fetchStatus": "fetched",
                    "fetchedMetadata": {
                        "title": "Example Co",
                        "description": "Clinical documentation systems for care teams.",
                        "site_name": "Example Co",
                        "h1": "Clinical documentation",
                    },
                    "sourceLabels": ["Public company site"],
                },
                "other-labs": {
                    "website": "https://other.example/",
                    "fetchStatus": "fetched",
                    "fetchedMetadata": {
                        "title": "Other Specialties",
                        "description": "Industrial instrumentation and process gas analytics services.",
                        "site_name": "Other Specialties",
                        "h1": "Process controls",
                    },
                    "sourceLabels": ["Public company site"],
                },
                "insecure-co": {
                    "website": "http://insecure.example/",
                    "fetchStatus": "fetched",
                    "fetchedMetadata": {
                        "title": "Insecure Co",
                        "description": "A candidate that lacks an HTTPS source.",
                        "site_name": "Insecure Co",
                        "h1": "Insecure Co",
                    },
                    "sourceLabels": ["Unverified company site"],
                },
            }
        ),
        encoding="utf-8",
    )
    for video_id in ("aaaaaaaaaaa", "bbbbbbbbbbb"):
        (transcripts / f"{video_id}.txt").write_text(
            "The speaker describes agent evaluations, evals, and a quality gate.",
            encoding="utf-8",
        )
    _write_test_scoring_policy(root)
    return root


def _write_provider_index(
    root: Path,
    results: list[dict],
    receipts: list[dict],
) -> None:
    private = root / ".ops/state/cache/wiki-maker/credibility-v2"
    receipt_root = private / "receipts/provider-fetch"
    receipt_root.mkdir(parents=True)
    (private / "provider-checks.json").write_text(
        json.dumps(
            {
                "schemaVersion": 1,
                "visibility": "internal-only",
                "results": results,
            }
        ),
        encoding="utf-8",
    )
    for receipt in receipts:
        request_id = receipt["requestId"].removeprefix("provider-request:")
        (receipt_root / f"{request_id}.json").write_text(
            json.dumps(receipt),
            encoding="utf-8",
        )


def test_builds_claim_scoped_decisions_for_people_companies_media_and_topics(
    tmp_path: Path,
) -> None:
    root = _fixture(tmp_path)

    policy = POLICY.build_private_policy(root)

    assert set(policy["videoWritingDecisions"]) == {
        "aaaaaaaaaaa",
        "bbbbbbbbbbb",
        "ccccccccccc",
    }
    assert "example-person" in policy["peopleWritingDecisions"]
    assert "example-co" in policy["companyWritingDecisions"]
    assert (
        policy["companyProfileWritingDecisions"]["example-co"][
            "writingDisposition"
        ]
        == "attribute_to_source"
    )
    assert (
        policy["companyProfileWritingDecisions"]["other-labs"][
            "writingDisposition"
        ]
        == "omit"
    )
    assert (
        policy["companyProfileGateStates"]["other-labs"]["status"] == "held"
    )
    assert policy["companyProfileGateStates"]["insecure-co"]["status"] == "held"
    assert (
        policy["companyProfileWritingDecisions"]["insecure-co"][
            "writingDisposition"
        ]
        == "omit"
    )
    assert (
        policy["companyProfileWritingDecisions"]["insecure-co"][
            "publicSourceIds"
        ]
        == []
    )
    assert (
        policy["topicWritingDecisions"]["agent-evaluations"]["writingDisposition"]
        == "assert_with_citations"
    )
    assert set(policy["topicVideoWritingDecisions"]["agent-evaluations"]) == {
        "aaaaaaaaaaa",
        "bbbbbbbbbbb",
    }
    assert (root / ".ops/state/cache/wiki-maker/credibility-v2/credibility-v2.sqlite").is_file()


def test_policy_is_deterministic_and_contains_no_numeric_ranking_fields(
    tmp_path: Path,
) -> None:
    root = _fixture(tmp_path)

    first = POLICY.build_private_policy(root)
    second = POLICY.build_private_policy(root)

    assert first == second
    rendered = json.dumps(first, sort_keys=True)
    assert '"score"' not in rendered
    assert '"weight"' not in rendered
    assert '"rank"' not in rendered
    assert first["policy"]["publicationImpliesEndorsement"] is False


def test_source_as_of_does_not_time_travel_to_a_pending_release() -> None:
    manifest = {
        "checkedAt": "2026-07-16T20:00:00Z",
        "videos": [
            {
                "mediaType": "talk_recording",
                "uploadDate": "2026-07-16",
                "releaseDate": "2026-07-16",
            },
            {
                "mediaType": "scheduled_premiere",
                "uploadDate": "2026-07-10",
                "releaseDate": "2026-07-20",
            },
        ],
    }

    provider_index = {"checkedAt": "2026-07-17T04:55:52Z"}

    assert POLICY.source_as_of(manifest, provider_index) == datetime(
        2026, 7, 17, 4, 55, 52, tzinfo=timezone.utc
    )


def test_pending_premiere_cached_transcript_cannot_drive_topic_writing(
    tmp_path: Path,
) -> None:
    root = _fixture(tmp_path)
    manifest_path = root / "raw/sources/official-wf26-video-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["videos"].append(
        {
            "id": "premiere001",
            "title": "Pending MCP premiere",
            "mediaType": "scheduled_premiere",
            "associationEvidence": "official_wf26_playlist_membership",
            "uploadDate": "2026-07-10",
            "releaseDate": "2026-07-20",
        }
    )
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    (root / "raw/sources/youtube-transcripts/premiere001.txt").write_text(
        "MCP tools and an MCP server appear in this stale early transcript cache.",
        encoding="utf-8",
    )

    policy = POLICY.build_private_policy(root)

    assert "premiere001" in policy["videoWritingDecisions"]
    assert "mcp" not in policy["topicWritingDecisions"]
    assert all(
        "premiere001" not in rows
        for rows in policy["topicVideoWritingDecisions"].values()
    )
    assert "youtube-premiere001" not in json.dumps(
        {
            "topics": policy["topicWritingDecisions"],
            "topicVideos": policy["topicVideoWritingDecisions"],
        },
        sort_keys=True,
    )


def test_same_name_domain_and_topical_metadata_do_not_prove_company_identity() -> None:
    accepted, reasons, _metadata, signals = POLICY.company_profile_gate(
        "Apify",
        {
            "website": "https://apify.ai/",
            "fetchedMetadata": {
                "title": "Apify.ai - AI automation",
                "description": (
                    "Apify.ai provides business automation, AI chatbots, and "
                    "real-time management dashboards."
                ),
                "site_name": "Apify.ai",
                "h1": "Business automation",
            },
        },
        "Apify builds a marketplace of web data tools for AI agents.",
        official_identity_hosts=("apify.com",),
    )

    assert accepted is False
    assert POLICY.ReasonCode.ID_NAME_ONLY in reasons
    assert signals["identityHostMatch"] is False
    assert signals["metadataIdentityMatch"] is True


def test_exact_event_published_owner_host_allows_attributed_owner_context() -> None:
    accepted, reasons, _metadata, signals = POLICY.company_profile_gate(
        "Abridge",
        {
            "website": "https://www.abridge.com/",
            "fetchedMetadata": {
                "title": "Abridge",
                "description": "Clinical documentation support for care teams.",
                "site_name": "Abridge",
                "h1": "For every moment of care",
            },
        },
        "Abridge is represented in the official program.",
        official_identity_hosts=("abridge.com",),
    )

    assert accepted is True
    assert POLICY.ReasonCode.ID_OWNER_EXACT in reasons
    assert signals["identityHostMatch"] is True


def test_placeholder_owner_metadata_is_not_usable_public_context() -> None:
    accepted, reasons, _metadata, signals = POLICY.company_profile_gate(
        "Emulated",
        {
            "website": "https://emulated.so/",
            "fetchedMetadata": {
                "title": "Emulated",
                "description": "Your company description goes here.",
                "site_name": "Emulated",
                "h1": "Emulated",
            },
        },
        "Emulated is represented in the official program.",
        official_identity_hosts=("emulated.so",),
    )

    assert accepted is False
    assert POLICY.ReasonCode.MISSING_EVIDENCE in reasons
    assert signals["identityHostMatch"] is True


def test_official_roster_record_binds_ora_owner_host_to_explicit_bio() -> None:
    speakers = [
        {
            "name": "Liad Yosef",
            "role": "Co-creator",
            "company": "MCP Apps",
            "bio": "Liad is currently the co-founder and CTO at ORA.",
            "website": "https://ora.ai",
        }
    ]

    hosts, contexts = POLICY.official_roster_company_context("ORA", speakers)
    accepted, _reasons, _metadata, signals = POLICY.company_profile_gate(
        "ORA",
        {
            "website": "https://ora.ai/",
            "fetchedMetadata": {
                "title": "ORA",
                "description": (
                    "ORA researches and builds agent-ready interfaces for the web."
                ),
                "site_name": "ORA",
                "h1": "The agent-ready web",
            },
        },
        " ".join(contexts),
        official_identity_hosts=hosts,
    )

    assert hosts == ("ora.ai",)
    assert accepted is True
    assert signals["identityHostMatch"] is True


def test_private_policy_admits_ora_as_attributed_owner_context(tmp_path: Path) -> None:
    root = _fixture(tmp_path)
    raw = root / "raw/sources"
    speakers = json.loads((raw / "official-speakers.json").read_text())
    speakers["speakers"].append(
        {
            "name": "Liad Yosef",
            "role": "Co-creator",
            "company": "MCP Apps",
            "bio": "Liad is currently the co-founder and CTO at ORA.",
            "website": "https://ora.ai",
        }
    )
    (raw / "official-speakers.json").write_text(json.dumps(speakers))
    profiles = json.loads((raw / "company-profiles.json").read_text())
    profiles["ora"] = {
        "website": "https://ora.ai/",
        "fetchStatus": "fetched",
        "fetchedMetadata": {
            "title": "ORA",
            "description": "ORA builds agent-ready interfaces for the public web.",
            "site_name": "ORA",
            "h1": "The agent-ready web",
        },
    }
    (raw / "company-profiles.json").write_text(json.dumps(profiles))
    plan_id = "provider-plan:ora-host"
    provider_rows = [
        (
            "owner_web",
            "provider-request:owner",
            ["self_statement"],
            {"state": "owner_content_available", "responseBytes": 100},
            "https://ora.ai/",
            "https://ora.ai/",
        ),
        (
            "google_dns_doh",
            "provider-request:dns",
            ["dns_record_observation"],
            {"state": "dns_observed", "rcode": 0, "answerCount": 2},
            "https://dns.google/resolve?name=ora.ai&type=A",
            "https://dns.google/resolve?name=ora.ai&type=A",
        ),
        (
            "rdap_registry",
            "provider-request:rdap",
            ["domain_registration_metadata"],
            {"state": "registration_metadata_available", "domain": "ora.ai"},
            "https://rdap.org/domain/ora.ai",
            "https://rdap.example/domain/ora.ai",
        ),
    ]
    _write_provider_index(
        root,
        [
            {
                "subjectId": "person:liad-yosef",
                "planId": plan_id,
                "sourceBoundary": "official_roster_host_metadata",
                "sourcePath": "raw/sources/official-speakers.json",
                "evidence": [
                    {
                        "providerId": provider_id,
                        "requestId": request_id,
                        "outcome": "success",
                        "claimScopes": claim_scopes,
                        "semanticResult": semantic_result,
                    }
                    for (
                        provider_id,
                        request_id,
                        claim_scopes,
                        semantic_result,
                        _request_url,
                        _final_url,
                    ) in provider_rows
                ],
            }
        ],
        [
            {
                "requestId": request_id,
                "planId": plan_id,
                "subjectId": "person:liad-yosef",
                "providerId": provider_id,
                "outcome": "success",
                "requestUrl": request_url,
                "finalUrl": final_url,
                "retrievedAt": "2026-07-17T00:00:00Z",
            }
            for (
                provider_id,
                request_id,
                _claim_scopes,
                _semantic_result,
                request_url,
                final_url,
            ) in provider_rows
        ],
    )

    policy = POLICY.build_private_policy(root)

    assert policy["companyProfileGateStates"]["ora"]["status"] == (
        "accepted_as_attributed_owner_context"
    )
    assert policy["companyProfileWritingDecisions"]["ora"][
        "writingDisposition"
    ] == "attribute_to_source"
    provider_evidence = policy["companyProfileGateStates"]["ora"][
        "providerEvidence"
    ]
    assert {row["providerId"] for row in provider_evidence} == {
        "owner_web",
        "google_dns_doh",
        "rdap_registry",
    }
    assert all(row["hostAvailabilityCorroborated"] for row in provider_evidence)
    assert policy["companyProfileGateStates"]["ora"]["signals"][
        "providerHostAvailabilityCorroborated"
    ] is True


def test_roster_identity_does_not_join_name_and_website_across_records() -> None:
    hosts, contexts = POLICY.official_roster_company_context(
        "ORA",
        [
            {
                "name": "First Person",
                "role": "CTO at ORA",
                "bio": "Builds agent-ready interfaces.",
                "website": "https://first-person.example/",
            },
            {
                "name": "Second Person",
                "role": "Engineer",
                "bio": "Works on web protocols.",
                "website": "https://ora.ai/",
            },
        ],
    )

    assert hosts == ()
    assert contexts == ()
    assert (
        POLICY.official_roster_company_provider_bindings(
            "ORA",
            [
                {
                    "name": "First Person",
                    "role": "CTO at ORA",
                    "website": "https://first-person.example/",
                },
                {
                    "name": "Second Person",
                    "role": "Engineer",
                    "website": "https://ora.ai/",
                },
            ],
        )
        == ()
    )


def test_roster_name_field_and_lowercase_word_do_not_bind_short_brand() -> None:
    hosts, _contexts = POLICY.official_roster_company_context(
        "ORA",
        [
            {
                "name": "ORA",
                "role": "Engineer",
                "bio": "Researches ora in an unrelated context.",
                "website": "https://ora.ai/",
            }
        ],
    )

    assert hosts == ()


def test_company_profile_source_prefers_private_state_and_keeps_explicit_legacy(
    tmp_path: Path,
) -> None:
    root = tmp_path / "project"
    legacy = root / POLICY.LEGACY_COMPANY_PROFILES_RELATIVE
    private = root / POLICY.PRIVATE_COMPANY_PROFILES_RELATIVE
    legacy.parent.mkdir(parents=True)
    legacy.write_text("{}", encoding="utf-8")

    assert POLICY.company_profile_source_path(root) == legacy

    private.parent.mkdir(parents=True)
    private.write_text("{}", encoding="utf-8")

    assert POLICY.company_profile_source_path(root) == private
    assert (
        POLICY.company_profile_source_path(
            root,
            POLICY.LEGACY_COMPANY_PROFILES_RELATIVE,
        )
        == legacy
    )


def test_empty_wikimedia_discovery_is_private_and_cannot_boost_topic(
    tmp_path: Path,
) -> None:
    root = _fixture(tmp_path)
    request_id = "provider-request:empty-wikimedia"
    plan_id = "provider-plan:empty-wikimedia"
    _write_provider_index(
        root,
        [
            {
                "subjectId": "concept:agent-memory",
                "planId": plan_id,
                "sourceBoundary": "discovery_only_topic_context",
                "sourcePath": "wiki/topics/agent-memory.md",
                "evidence": [
                    {
                        "providerId": "wikimedia",
                        "requestId": request_id,
                        "outcome": "success",
                        "claimScopes": ["encyclopedic_context"],
                        "semanticResult": {
                            "state": "discovery_candidates",
                            "resultCount": 0,
                            "candidateIds": [],
                        },
                    }
                ],
            }
        ],
        [
            {
                "requestId": request_id,
                "planId": plan_id,
                "subjectId": "concept:agent-memory",
                "providerId": "wikimedia",
                "outcome": "success",
                "requestUrl": "https://wikidata.example/search",
                "retrievedAt": "2026-07-17T00:00:00Z",
                "cachePath": (
                    ".ops/state/cache/wiki-maker/credibility-v2/fetch-cache/"
                    "wikimedia/private.body"
                ),
            }
        ],
    )
    cache_body = (
        root
        / ".ops/state/cache/wiki-maker/credibility-v2/fetch-cache/wikimedia/private.body"
    )
    cache_body.mkdir(parents=True)

    policy = POLICY.build_private_policy(root)

    gate = policy["providerEvidenceGateStates"]["concept:agent-memory"]
    assert gate["status"] == "empty_discovery_result"
    assert gate["automaticWritingImpact"] == "none"
    assert gate["globalReputationAssessment"] == "not_computed"
    assert gate["endorsementStatus"] == "not_endorsed"
    assert "agent-memory" not in policy["topicWritingDecisions"]


def test_repository_and_package_success_remain_metadata_only(tmp_path: Path) -> None:
    root = _fixture(tmp_path)
    plan_id = "provider-plan:tool-metadata"
    rows = [
        (
            "github_rest",
            "provider-request:github",
            "repository_metadata",
            {
                "state": "repository_metadata_available",
                "repository": "captivus/chrome-agent",
                "archived": False,
                "disabled": False,
            },
        ),
        (
            "pypi",
            "provider-request:pypi",
            "python_package_metadata",
            {
                "state": "package_metadata_available",
                "package": "chrome-agent",
                "version": "0.5.3",
            },
        ),
    ]
    _write_provider_index(
        root,
        [
            {
                "subjectId": "tool:chrome-agent",
                "planId": plan_id,
                "sourceBoundary": "curated_wiki_context",
                "sourcePath": "wiki/tools/chrome-agent.md",
                "evidence": [
                    {
                        "providerId": provider_id,
                        "requestId": request_id,
                        "outcome": "success",
                        "claimScopes": [scope],
                        "semanticResult": semantic,
                    }
                    for provider_id, request_id, scope, semantic in rows
                ],
            }
        ],
        [
            {
                "requestId": request_id,
                "planId": plan_id,
                "subjectId": "tool:chrome-agent",
                "providerId": provider_id,
                "outcome": "success",
                "requestUrl": "https://metadata.example/record",
                "retrievedAt": "2026-07-17T00:00:00Z",
            }
            for provider_id, request_id, _scope, _semantic in rows
        ],
    )

    policy = POLICY.build_private_policy(root)
    gate = policy["providerEvidenceGateStates"]["tool:chrome-agent"]

    assert gate["status"] == "claim_scoped_metadata_available"
    assert {
        tuple(item["claimScopes"])
        for item in gate["claimScopedEvidence"]
    } == {("repository_metadata",), ("python_package_metadata",)}
    assert gate["eventAssociationStatus"] == "not_claimed"
    assert gate["endorsementStatus"] == "not_endorsed"
    assert gate["automaticWritingImpact"] == "none"


def test_provider_host_evidence_requires_preexisting_official_identity_binding() -> None:
    evidence = {
        "person:example": [
            {
                "providerId": "owner_web",
                "outcome": "success",
                "claimScopes": ["self_statement"],
                "semanticResult": {"state": "owner_content_available"},
                "targetHost": "example.ai",
                "requestId": "provider-request:example",
            }
        ]
    }
    bindings = ({"subjectId": "person:example", "host": "example.ai"},)

    assert (
        POLICY.company_provider_host_evidence(
            evidence,
            bindings,
            identity_bound=False,
        )
        == ()
    )
