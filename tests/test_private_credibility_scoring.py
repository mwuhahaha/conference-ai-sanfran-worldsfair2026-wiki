from __future__ import annotations

import importlib.util
import json
import sys
from dataclasses import replace
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from wiki_from_topic_maker.credibility_v2 import (
    ClaimRecord,
    CredibilityStore,
    DimensionName,
    DimensionStatus,
    EndorsementStatus,
    EventAssociationStatus,
    EvidenceCertainty,
    EvidenceDirectness,
    EvidenceObservation,
    IdentityStatus,
    ObservationStance,
    PublicationDisposition,
    ReasonCode,
)
from wiki_from_topic_maker.credibility_v2.scoring import (
    DimensionCap,
    EvidenceKind,
    FactorChoice,
    RationalFactor,
    ScoreRule,
    ScoreRuleset,
    SourceRole,
)


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/build_private_credibility_v2.py"
SPEC = importlib.util.spec_from_file_location("private_credibility_scoring_test", SCRIPT)
POLICY = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
sys.modules[SPEC.name] = POLICY
SPEC.loader.exec_module(POLICY)

NOW = datetime(2026, 7, 17, 12, 0, tzinfo=timezone.utc)


def _factor_choices(source_authority: str) -> tuple[FactorChoice, ...]:
    values = (
        ("claim_relevance", "exact"),
        ("method_quality", "moderate"),
        ("method_quality", "strong"),
        ("method_quality", "weak"),
        ("source_authority", source_authority),
    )
    return tuple(
        FactorChoice(
            factor_id=factor_id,
            choice_id=choice_id,
            factor=RationalFactor(1, 1),
            reason_code=f"test_{factor_id}_{choice_id}",
        )
        for factor_id, choice_id in values
    )


def _ruleset() -> ScoreRuleset:
    return ScoreRuleset.create(
        ruleset_version="synthetic-test-v1",
        policy_name="Synthetic test-only auditable scoring policy",
        policy_sources=("https://example.test/scoring-methodology",),
        rules=(
            ScoreRule(
                rule_id="test-adverse-l1",
                rule_version="synthetic-test-v1",
                evidence_kind=EvidenceKind.ADVERSE_L1,
                dimension=DimensionName.CLAIM_SUPPORT,
                base_points=-6,
                description="Synthetic unresolved adverse evidence.",
                allowed_source_roles=(SourceRole.INDEPENDENT_SECONDARY,),
                factor_choices=_factor_choices("independent_documented"),
            ),
            ScoreRule(
                rule_id="test-direct-primary",
                rule_version="synthetic-test-v1",
                evidence_kind=EvidenceKind.DIRECT_PRIMARY_RECORD,
                dimension=DimensionName.CLAIM_SUPPORT,
                base_points=10,
                description="Synthetic direct primary evidence.",
                allowed_source_roles=(SourceRole.OFFICIAL_PRIMARY,),
                factor_choices=_factor_choices("official_original"),
            ),
            ScoreRule(
                rule_id="test-owner-assertion",
                rule_version="synthetic-test-v1",
                evidence_kind=EvidenceKind.OWNER_ASSERTION,
                dimension=DimensionName.CLAIM_SUPPORT,
                base_points=3,
                description="Synthetic attributed owner evidence.",
                allowed_source_roles=(SourceRole.FIRST_PARTY,),
                factor_choices=_factor_choices("first_party_or_indirect"),
            ),
        ),
        dimension_caps=(
            DimensionCap(DimensionName.CLAIM_SUPPORT, -100, 100),
        ),
    )


def _write_ruleset(root: Path, ruleset: ScoreRuleset | None = None) -> Path:
    path = (
        root
        / ".ops/state/cache/wiki-maker/credibility-v2/scoring-policies/active.json"
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps((ruleset or _ruleset()).as_dict(), sort_keys=True),
        encoding="utf-8",
    )
    return path


def _minimal_project(tmp_path: Path, *, with_ruleset: bool = True) -> Path:
    root = tmp_path / "project"
    raw = root / "raw/sources"
    (root / "wiki/resources").mkdir(parents=True)
    raw.mkdir(parents=True)
    (raw / "official-wf26-video-manifest.json").write_text(
        json.dumps(
            {
                "checkedAt": "2026-07-17T12:00:00Z",
                "videos": [
                    {
                        "id": "aaaaaaaaaaa",
                        "title": "A verified event recording",
                        "mediaType": "talk_recording",
                        "associationEvidence": "official_wf26_playlist_membership",
                        "uploadDate": "2026-07-16",
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    (raw / "official-speakers.json").write_text(
        json.dumps({"speakers": []}), encoding="utf-8"
    )
    (raw / "official-sessions.json").write_text(
        json.dumps({"website": "https://ai.engineer/worldsfair", "sessions": []}),
        encoding="utf-8",
    )
    if with_ruleset:
        _write_ruleset(root)
    return root


def test_missing_private_ruleset_fails_closed(tmp_path: Path) -> None:
    root = _minimal_project(tmp_path, with_ruleset=False)

    with pytest.raises(FileNotFoundError, match="private scoring ruleset is required"):
        POLICY.build_private_policy(root)


def test_policy_build_persists_deterministic_private_receipts_without_leaks(
    tmp_path: Path,
) -> None:
    root = _minimal_project(tmp_path)

    first = POLICY.build_private_policy(root)
    receipt_root = (
        root / ".ops/state/cache/wiki-maker/credibility-v2/receipts/scoring"
    )
    first_files = tuple(sorted(receipt_root.glob("*.json")))
    first_payloads = tuple(path.read_text(encoding="utf-8") for path in first_files)
    ruleset_files = tuple(
        path
        for path in sorted(
            (
                root
                / ".ops/state/cache/wiki-maker/credibility-v2/scoring-policies"
            ).glob("*.json")
        )
        if path.name != "active.json"
    )
    second = POLICY.build_private_policy(root)

    assert first == second
    assert len(first_files) == 1
    receipt_payload = json.loads(first_payloads[0])
    assert receipt_payload["line_items"][0]["evidence"]["evidence_at"] == (
        "2026-07-16T00:00:00.000000Z"
    )
    assert len(ruleset_files) == 1
    assert json.loads(ruleset_files[0].read_text(encoding="utf-8")) == (
        _ruleset().as_dict()
    )
    assert tuple(sorted(receipt_root.glob("*.json"))) == first_files
    assert tuple(path.read_text(encoding="utf-8") for path in first_files) == first_payloads
    public_policy_shape = json.dumps(first, sort_keys=True)
    for private_key in (
        "receiptId",
        "rulesetId",
        "rulesetDigest",
        "lineItems",
        "basePoints",
        "signedPoints",
        "totalPoints",
    ):
        assert private_key not in public_policy_shape
    assert first["videoWritingDecisions"]["aaaaaaaaaaa"][
        "writingDisposition"
    ] == "attribute_to_source"


def test_media_publication_dates_never_time_travel_to_pending_release() -> None:
    as_of = datetime(2026, 7, 17, 12, 0, tzinfo=timezone.utc)

    assert POLICY.media_published_at(
        {
            "mediaType": "talk_recording",
            "uploadDate": "2026-07-15",
            "releaseDate": "2026-07-16T08:30:00-04:00",
        },
        as_of=as_of,
    ) == datetime(2026, 7, 16, 12, 30, tzinfo=timezone.utc)
    assert POLICY.media_published_at(
        {
            "mediaType": "scheduled_premiere",
            "uploadDate": "2026-07-15",
            "releaseDate": "2026-07-20T10:00:00Z",
        },
        as_of=as_of,
    ) == datetime(2026, 7, 15, tzinfo=timezone.utc)
    assert POLICY.media_published_at(
        {
            "mediaType": "talk_recording",
            "uploadDate": "not-a-date",
            "releaseDate": "2026-07-20T10:00:00Z",
        },
        as_of=as_of,
    ) is None


def test_scoring_uses_first_append_only_observation_when_source_is_rediscovered(
    tmp_path: Path,
) -> None:
    root = tmp_path / "project"
    root.mkdir()
    store = CredibilityStore.for_project(root)
    claim = ClaimRecord.create(
        subject_id="video:example",
        predicate="is official event media",
        object_value=True,
    )
    store.append_claim(claim)
    source = POLICY.append_source(
        store,
        source_id="official-video:example",
        canonical_url="https://www.youtube.com/watch?v=example",
        value={"title": "Example"},
        as_of=NOW,
        published_at=NOW - timedelta(days=2),
    )
    first = POLICY.append_observation(
        store,
        claim=claim,
        source=source,
        span_id="manifest-video:example",
        cluster_id="official-event-media",
        as_of=NOW - timedelta(days=1),
    )
    rediscovered = replace(first, observed_at=NOW)

    assert rediscovered.observation_id == first.observation_id
    assert store.append_observation(rediscovered) is False
    scored = POLICY.build_score_evidence(store, _ruleset(), rediscovered)

    assert scored is not None
    assert scored.observation_id == first.observation_id
    assert scored.observed_at == first.observed_at


def test_signed_line_items_are_replayable_and_correlated_adverse_copy_is_zero(
    tmp_path: Path,
) -> None:
    root = tmp_path / "project"
    root.mkdir()
    store = CredibilityStore.for_project(root)
    runtime = POLICY.PrivateScoringRuntime(store=store, ruleset=_ruleset())
    claim = ClaimRecord.create(
        subject_id="person:example",
        predicate="has evidence relevant to an AI engineering claim",
        object_value=True,
    )
    store.append_claim(claim)
    primary = POLICY.append_source(
        store,
        source_id="official-primary:example",
        canonical_url="https://example.test/official-record",
        value={"finding": "supported"},
        as_of=NOW,
        published_at=NOW - timedelta(days=2),
        corrected_at=NOW - timedelta(days=1),
    )
    adverse_one = POLICY.append_source(
        store,
        source_id="independent-report:example-one",
        canonical_url="https://example.test/report-one",
        value={"allegation": "unresolved"},
        as_of=NOW,
    )
    adverse_copy = POLICY.append_source(
        store,
        source_id="independent-report:example-copy",
        canonical_url="https://example.test/report-copy",
        value={"allegation": "republished unresolved claim"},
        as_of=NOW,
    )
    positive = POLICY.append_observation(
        store,
        claim=claim,
        source=primary,
        span_id="official-finding",
        cluster_id="official-record",
        as_of=NOW,
    )

    def adverse_observation(source, span_id: str) -> EvidenceObservation:
        observation = EvidenceObservation.create(
            claim_id=claim.claim_id,
            subject_id=claim.subject_id,
            source_version_id=source.source_version_id,
            evidence_span_id=span_id,
            stance=ObservationStance.REFUTES,
            directness=EvidenceDirectness.REPORTED,
            extraction_certainty=EvidenceCertainty.MEDIUM,
            independence_cluster_id="syndicated-adverse-report",
            observed_at=NOW,
            reason_codes=(
                ReasonCode.ADVERSE_EVIDENCE_L1,
                ReasonCode.DOCUMENTED_INDEPENDENT_REPORT,
            ),
            extractor_version=POLICY.SOURCE_ADAPTER_VERSION,
        )
        store.append_observation(observation)
        return observation

    negative = adverse_observation(adverse_one, "unresolved-allegation")
    duplicate = adverse_observation(adverse_copy, "republished-allegation")
    snapshot = POLICY.append_assessment(
        store,
        scoring=runtime,
        claim=claim,
        observations=[positive, negative, duplicate],
        as_of=NOW,
        identity_status=IdentityStatus.VERIFIED,
        identity_required=True,
        event_status=EventAssociationStatus.NOT_CLAIMED,
        event_claimed=False,
        publication=PublicationDisposition.APPROVED,
        independent=True,
    )
    receipt = store.score_receipt_as_of(claim.claim_id, NOW)

    assert receipt is not None
    assert sorted(item.signed_points for item in receipt.line_items) == [-6, 0, 10]
    suppressed = next(item for item in receipt.line_items if item.signed_points == 0)
    assert suppressed.factor_applications[-1].reason_code == (
        "dependent_cluster_suppressed"
    )
    assert receipt.unresolved_conflict is True
    assert receipt.human_review_required is True
    assert snapshot.dimension(DimensionName.CLAIM_SUPPORT).status is (
        DimensionStatus.CONTESTED
    )
    assert store.verify_score_receipt(receipt.receipt_id) == receipt
    assert all(
        item.evidence.evidence_sha256.startswith("sha256:")
        and item.evidence.evidence_locator
        for item in receipt.line_items
    )
    primary_line = next(
        item
        for item in receipt.line_items
        if item.evidence.source_id == primary.source_id
    )
    assert primary_line.evidence.evidence_at == NOW - timedelta(days=1)
    assert snapshot.identity_status is IdentityStatus.VERIFIED
    assert snapshot.event_status is EventAssociationStatus.NOT_CLAIMED
    assert snapshot.publication_disposition is PublicationDisposition.APPROVED
    assert snapshot.endorsement_status is EndorsementStatus.NOT_ENDORSED
    selected_factors = {
        item.evidence.source_role: dict(item.evidence.factor_selections)
        for item in receipt.line_items
        if item.signed_points
    }
    assert selected_factors[SourceRole.OFFICIAL_PRIMARY] == {
        "claim_relevance": "exact",
        "method_quality": "strong",
        "source_authority": "official_original",
    }
    assert selected_factors[SourceRole.INDEPENDENT_SECONDARY] == {
        "claim_relevance": "exact",
        "method_quality": "weak",
        "source_authority": "independent_documented",
    }

    replayed = runtime.evaluate(
        claim=claim,
        snapshot=snapshot,
        observations=[positive, negative, duplicate],
    )
    assert replayed == receipt
    decision = POLICY.project_writing_decision(snapshot).as_dict()
    assert set(decision) == {
        "schemaVersion",
        "claimId",
        "subjectId",
        "writingDisposition",
        "attribution",
        "asOf",
        "publicSourceIds",
    }
    assert decision["writingDisposition"] == "present_disagreement"
