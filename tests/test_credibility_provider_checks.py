import json
from pathlib import Path

import scripts.run_credibility_provider_checks as checks


def _fixture(tmp_path: Path) -> Path:
    root = tmp_path / "project"
    (root / "raw/sources").mkdir(parents=True)
    (root / "wiki/tools").mkdir(parents=True)
    (root / "wiki/topics").mkdir(parents=True)
    (root / "raw/sources/official-speakers.json").write_text(
        json.dumps(
            [
                {
                    "name": "Owner Person",
                    "website": "https://owner.example/about",
                }
            ]
        )
    )
    (root / "wiki/tools/external.md").write_text(
        "---\n"
        "title: External\n"
        "category: tools\n"
        "accidentalResources: [\"https://github.com/example/collision\"]\n"
        "---\n"
        "# External\n\n"
        "https://github.com/example/collision\n"
        "https://pypi.org/project/example-package/\n"
    )
    (root / "wiki/topics/agent-memory.md").write_text(
        "---\ntitle: Agent Memory\ncategory: topics\n---\n# Agent Memory\n"
    )
    return root


def test_discovery_uses_only_explicit_identifiers_and_boundaries(tmp_path) -> None:
    root = _fixture(tmp_path)

    planned = checks.discover_planned_checks(root)
    rows = {
        (item.plan.request.subject_id, tuple(step.provider_id for step in item.plan.steps)):
        item
        for item in planned
    }

    assert ("person:owner-person", ("owner_web",)) in rows
    assert (
        "person:owner-person",
        ("google_dns_doh", "rdap_registry"),
    ) in rows
    github = rows[("tool:external", ("github_rest",))]
    assert github.source_boundary == "accidental_third_party"
    assert rows[("tool:external", ("pypi",))].source_boundary == (
        "curated_wiki_context"
    )
    topic = rows[("concept:agent-memory", ("wikimedia",))]
    assert topic.plan.steps[0].discovery_only is True


def test_selection_is_thin_per_provider_and_skips_existing_receipts(tmp_path) -> None:
    root = _fixture(tmp_path)
    planned = checks.discover_planned_checks(root)

    selected = checks.select_unqueried_checks(root, planned, per_provider=1)

    providers = [
        provider
        for item in selected
        for provider in {request.provider_id for request in checks.build_provider_requests(item.plan)}
    ]
    assert len(providers) == len(set(providers))
    first_request = checks.build_provider_requests(selected[0].plan)[0]
    private = checks.CredibilityPrivatePaths.for_project(root)
    receipt = (
        private.receipts
        / "provider-fetch"
        / f"{first_request.request_id.removeprefix('provider-request:')}.json"
    )
    receipt.parent.mkdir(parents=True, exist_ok=True)
    receipt.write_text("{}")

    repeated = checks.select_unqueried_checks(root, planned, per_provider=1)

    assert selected[0] not in repeated


def test_dry_run_does_not_write_private_state(tmp_path) -> None:
    root = _fixture(tmp_path)

    result = checks.run_checks(root, per_provider=1, dry_run=True)

    assert result["dryRun"] is True
    assert result["selectedPlans"] >= 1
    assert not (root / ".ops").exists()
