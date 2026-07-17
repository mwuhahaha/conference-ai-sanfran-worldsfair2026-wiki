from __future__ import annotations

import importlib.util
import json
import sys
from hashlib import sha256
from pathlib import Path

import pytest
import yaml

from wiki_from_topic_maker.credibility_v2 import DimensionName
from wiki_from_topic_maker.credibility_v2.scoring import (
    DimensionCap,
    EvidenceKind,
    ScoreRule,
    ScoreRuleset,
    SourceRole,
)


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/apply_page_assessments.py"
SPEC = importlib.util.spec_from_file_location("apply_page_assessments_test", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def _ruleset() -> ScoreRuleset:
    return ScoreRuleset.create(
        ruleset_version="page-assessment-test-v1",
        policy_name="Synthetic page evidence coverage policy",
        policy_sources=("https://example.test/evidence-policy",),
        rules=(
            ScoreRule(
                rule_id="test-direct-primary",
                rule_version="page-assessment-test-v1",
                evidence_kind=EvidenceKind.DIRECT_PRIMARY_RECORD,
                dimension=DimensionName.CLAIM_SUPPORT,
                base_points=10,
                description="Synthetic official event record.",
                allowed_source_roles=(SourceRole.OFFICIAL_PRIMARY,),
            ),
            ScoreRule(
                rule_id="test-contradiction",
                rule_version="page-assessment-test-v1",
                evidence_kind=EvidenceKind.HIGH_QUALITY_CONTRADICTION,
                dimension=DimensionName.CLAIM_SUPPORT,
                base_points=-8,
                description="Synthetic independent contradiction.",
                allowed_source_roles=(SourceRole.INDEPENDENT_SECONDARY,),
            ),
            ScoreRule(
                rule_id="test-independent-report",
                rule_version="page-assessment-test-v1",
                evidence_kind=EvidenceKind.INDEPENDENT_DOCUMENTED_REPORT,
                dimension=DimensionName.CLAIM_SUPPORT,
                base_points=6,
                description="Synthetic independent report.",
                allowed_source_roles=(SourceRole.INDEPENDENT_SECONDARY,),
            ),
            ScoreRule(
                rule_id="test-owner-assertion",
                rule_version="page-assessment-test-v1",
                evidence_kind=EvidenceKind.OWNER_ASSERTION,
                dimension=DimensionName.CLAIM_SUPPORT,
                base_points=2,
                description="Synthetic owner assertion.",
                allowed_source_roles=(SourceRole.FIRST_PARTY,),
            ),
            ScoreRule(
                rule_id="test-repository",
                rule_version="page-assessment-test-v1",
                evidence_kind=EvidenceKind.REPRODUCIBLE_ARTIFACT,
                dimension=DimensionName.REPRODUCIBILITY,
                base_points=4,
                description="Synthetic inspectable repository.",
                allowed_source_roles=(SourceRole.FIRST_PARTY,),
            ),
        ),
        dimension_caps=(
            DimensionCap(DimensionName.CLAIM_SUPPORT, -100, 100),
            DimensionCap(DimensionName.REPRODUCIBILITY, -100, 100),
        ),
    )


def _page(title: str, category: str, header: str, body: str) -> str:
    return f"---\ntitle: {title}\ncategory: {category}\n{header}---\n# {title}\n\n{body}\n"


def _fixture(tmp_path: Path) -> Path:
    root = tmp_path / "project"
    for category in MODULE.TARGET_CATEGORIES:
        (root / "wiki" / category).mkdir(parents=True, exist_ok=True)
    (root / "raw/sources").mkdir(parents=True)
    (root / "raw/sources/official-wf26-video-manifest.json").write_text(
        json.dumps(
            {
                "checkedAt": "2026-07-17T12:00:00Z",
                "videos": [
                    {
                        "id": "abcdefghijk",
                        "associationEvidence": "official_wf26_playlist_membership",
                        "mediaType": "talk_recording",
                        "videoAvailability": "unlisted",
                    }
                ],
            }
        )
    )
    (root / "raw/sources/official-speakers.json").write_text(
        json.dumps(
            {
                "speakers": [
                    {"name": "Example Person", "company": "Example Org"}
                ]
            }
        )
    )
    (root / "raw/sources/official-sessions.json").write_text(
        json.dumps({"sessions": []})
    )
    policy = root / MODULE.ACTIVE_RULESET
    policy.parent.mkdir(parents=True)
    policy.write_text(json.dumps(_ruleset().as_dict(), sort_keys=True))
    provider_body = b"verified example company owner page"
    provider_cache = (
        root
        / MODULE.PRIVATE_ROOT
        / "fetch-cache/owner_web/example.body"
    )
    provider_cache.parent.mkdir(parents=True)
    provider_cache.write_bytes(provider_body)
    provider_receipt = (
        root
        / MODULE.PRIVATE_ROOT
        / "receipts/provider-fetch/example.json"
    )
    provider_receipt.parent.mkdir(parents=True)
    provider_receipt.write_text(
        json.dumps(
            {
                "cachePath": provider_cache.relative_to(root).as_posix(),
                "finalUrl": "https://example.com/",
                "outcome": "success",
                "providerId": "owner_web",
                "responseSha256": sha256(provider_body).hexdigest(),
                "retrievedAt": "2026-07-17T13:00:00Z",
                "subjectId": "company:example-co",
            }
        )
    )

    (root / "wiki/people/example-person.md").write_text(
        _page(
            "Example Person",
            "people",
            'sourceLabels: ["Official speaker roster", "Synthesis"]\n',
            "Officially listed event participant.",
        )
    )
    (root / "wiki/companies/example-co.md").write_text(
        _page(
            "Example Co",
            "companies",
            'website: "https://example.com/"\n'
            'sourceLabels: ["Public company site", "Y Combinator profile"]\n',
            "## Sources\n- [Company website](https://example.com/)\n"
            "- [Y Combinator profile](https://www.ycombinator.com/companies/example)",
        )
    )
    (root / "wiki/topics/derived-topic.md").write_text(
        _page(
            "Derived Topic",
            "topics",
            'sourceLabels: ["Slide/video-derived supporting context"]\n',
            "Derived comparison material linked to [[youtube-abcdefghijk-transcript]].",
        )
    )
    (root / "wiki/tools/contested-tool.md").write_text(
        _page(
            "Contested Tool",
            "tools",
            'sourceLabels: ["Official conference schedule"]\n'
            'contradictingSources: ["https://report.example.test/dispute"]\n',
            "Official event fact with a cited contradiction.",
        )
    )
    (root / "wiki/tools/index.md").write_text(
        _page(
            "Tools",
            "tools",
            "sourceAssessment:\n  state: limited\n",
            "Tool category inventory.",
        )
    )
    (root / "wiki/tools/tools.md").write_text(
        _page(
            "Tools",
            "tools",
            "sourceAssessment:\n  state: limited\n",
            "Duplicate tool category inventory.",
        )
    )
    return root


def _frontmatter(path: Path) -> dict:
    raw = path.read_text()
    end = raw.find("\n---\n", 4)
    return yaml.safe_load(raw[4:end])


def test_assesses_every_entity_page_and_keeps_private_receipts_auditable(
    tmp_path: Path,
) -> None:
    root = _fixture(tmp_path)

    first = MODULE.apply_page_assessments(root, minimum_pages=4)

    assert first["pageCount"] == 4
    assert first["coverageRecordCount"] == 10
    assert first["excludedNonEntityPageCount"] == 2
    assert first["assessmentCoverageStatuses"] == {
        "assessed": 3,
        "no_admitted_evidence": 1,
    }
    assert first["states"] == {
        "strong": 0,
        "limited": 3,
        "contested": 0,
        "pending": 1,
    }
    expected = {
        "people/example-person.md": ("limited", "official_primary_canonical"),
        "companies/example-co.md": ("limited", "source_attributed"),
        "topics/derived-topic.md": ("limited", "official_primary_canonical"),
        "tools/contested-tool.md": ("pending", "no_admitted_evidence"),
    }
    for relative, (state, basis) in expected.items():
        page = root / "wiki" / relative
        frontmatter = _frontmatter(page)
        capsule = frontmatter["sourceAssessment"]
        assert "evidenceAssessment" not in frontmatter
        assert capsule["state"] == state
        assert capsule["basis"] == basis
        raw = page.read_text()
        _metadata, body, _end = MODULE._frontmatter_and_body(raw)
        assert frontmatter["sourceAssessmentBodySha256"] == (
            "sha256:" + sha256(body.strip().encode("utf-8")).hexdigest()
        )
        serialized = json.dumps(capsule, sort_keys=True)
        for private_key in ("totalPoints", "receiptId", "rulesetId", "lineItems"):
            assert private_key not in serialized

    private = root / MODULE.PAGE_ASSESSMENT_ROOT
    inventory = json.loads((private / "inventory.json").read_text())
    coverage = json.loads((private / "coverage-bindings.json").read_text())
    ignored = json.loads((private / "ignored-evidence.json").read_text())
    assert inventory["pageCount"] == 4
    assert inventory["asOf"] == "2026-07-17T13:00:00Z"
    assert inventory["pages"][0]["claim"]["predicate"] == (
        "has verified source associations for material page evidence"
    )
    assert inventory["pages"][0]["assessmentSnapshotId"].startswith(
        "assessment-snapshot:"
    )
    assert len(coverage["records"]) == 10
    assert {
        (item["target_id"], item["status"])
        for item in coverage["records"]
        if item["status"] != "assessed"
    } == {
        ("tool:contested-tool", "no_admitted_evidence"),
        ("page:tools/contested-tool", "no_admitted_evidence"),
        ("page:tools/index", "not_applicable"),
        ("page:tools/tools", "not_applicable"),
    }
    assert any(
        item["value"] == "https://report.example.test/dispute"
        and item["reason"] == "source_content_not_observed"
        for item in ignored["items"]
    )
    receipts = sorted((root / MODULE.PRIVATE_ROOT / "receipts/scoring").glob("*.json"))
    markdown_receipts = sorted((root / MODULE.PRIVATE_ROOT / "receipts/scoring").glob("*.md"))
    assert len(receipts) == len(markdown_receipts) == 4
    assert all("Internal only" in path.read_text() for path in markdown_receipts)
    assert "sourceAssessment" not in _frontmatter(root / "wiki/tools/index.md")
    assert "sourceAssessment" not in _frontmatter(root / "wiki/tools/tools.md")
    assert inventory["excludedNonEntityPages"] == [
        "tools/index.md",
        "tools/tools.md",
    ]

    before = {
        path.relative_to(root).as_posix(): path.read_bytes()
        for path in [
            *receipts,
            *markdown_receipts,
            private / "inventory.json",
            private / "coverage-bindings.json",
            private / "ignored-evidence.json",
        ]
    }
    second = MODULE.apply_page_assessments(root, minimum_pages=4)
    after = {
        path.relative_to(root).as_posix(): path.read_bytes()
        for path in [
            *receipts,
            *markdown_receipts,
            private / "inventory.json",
            private / "coverage-bindings.json",
            private / "ignored-evidence.json",
        ]
    }
    assert second == first
    assert after == before


def test_inventory_floor_fails_before_partial_assessment(tmp_path: Path) -> None:
    root = _fixture(tmp_path)

    with pytest.raises(ValueError, match="inventory shrank"):
        MODULE.apply_page_assessments(root, minimum_pages=5)

    assert not (root / MODULE.PAGE_ASSESSMENT_ROOT / "inventory.json").exists()


def test_failed_assessment_does_not_partially_project_public_pages(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = _fixture(tmp_path)
    before = {
        path.relative_to(root).as_posix(): path.read_bytes()
        for path in sorted((root / "wiki").rglob("*.md"))
    }
    real_evaluate = MODULE.evaluate_score
    calls = 0

    def fail_second(*args, **kwargs):
        nonlocal calls
        calls += 1
        if calls == 2:
            raise RuntimeError("synthetic assessment failure")
        return real_evaluate(*args, **kwargs)

    monkeypatch.setattr(MODULE, "evaluate_score", fail_second)
    with pytest.raises(RuntimeError, match="synthetic assessment failure"):
        MODULE.apply_page_assessments(root, minimum_pages=4)

    after = {
        path.relative_to(root).as_posix(): path.read_bytes()
        for path in sorted((root / "wiki").rglob("*.md"))
    }
    assert after == before


def test_assessment_timestamp_ignores_future_premiere_release_date(
    tmp_path: Path,
) -> None:
    root = tmp_path / "project"
    manifest = root / "raw/sources/official-wf26-video-manifest.json"
    manifest.parent.mkdir(parents=True)
    manifest.write_text(
        json.dumps(
            {
                "videos": [
                    {
                        "mediaType": "scheduled_premiere",
                        "uploadDate": "2026-07-16",
                        "releaseDate": "2099-01-01",
                    }
                ]
            }
        )
    )

    assert MODULE.assessment_as_of(root).isoformat() == "2026-07-16T00:00:00+00:00"
