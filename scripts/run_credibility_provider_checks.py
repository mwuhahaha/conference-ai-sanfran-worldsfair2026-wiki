#!/usr/bin/env python3
"""Run a thin, private slice of provider checks for explicitly bound WF26 entities."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote, urlsplit

from wiki_from_topic_maker.credibility_v2 import (
    EntityIdentifier,
    OwnerSource,
    ProviderPlan,
    ProviderPlanningRequest,
    ScopedProviderQuery,
    build_provider_requests,
    execute_provider_plan,
    plan_evidence_providers,
)
from wiki_from_topic_maker.credibility_v2.private_paths import CredibilityPrivatePaths


ROOT = Path(__file__).resolve().parents[1]
SPEAKERS_PATH = ROOT / "raw" / "sources" / "official-speakers.json"
WIKI_ROOT = ROOT / "wiki"
RUN_RECEIPT_RELATIVE = Path(
    ".ops/state/cache/wiki-maker/credibility-v2/provider-checks.json"
)
GITHUB_RE = re.compile(r"https://github\.com/([^\s)\]<>\"`?#]+)", re.I)
PYPI_RE = re.compile(r"https://pypi\.org/project/([^\s)\]<>\"`?#/]+)", re.I)
PRIORITY_SUBJECTS = (
    "company:ora",
    "person:liad-yosef",
    "tool:chrome-agent",
    "tool:sderosiaux-chrome-agent",
    "concept:agent-memory",
)


@dataclass(frozen=True)
class PlannedCheck:
    plan: ProviderPlan
    source_boundary: str
    source_path: str


def discover_planned_checks(root: Path = ROOT) -> tuple[PlannedCheck, ...]:
    checks = [*_official_owner_checks(root), *_wiki_identifier_checks(root)]
    return tuple(
        sorted(
            checks,
            key=lambda item: (
                _priority(item.plan.request.subject_id),
                item.plan.request.subject_id,
                item.plan.plan_id,
            ),
        )
    )


def select_unqueried_checks(
    root: Path,
    checks: Iterable[PlannedCheck],
    *,
    per_provider: int,
) -> tuple[PlannedCheck, ...]:
    if per_provider < 1 or per_provider > 5:
        raise ValueError("per_provider must be between 1 and 5")
    paths = CredibilityPrivatePaths.for_project(root)
    selected: list[PlannedCheck] = []
    counts: dict[str, int] = {}
    for check in checks:
        requests = build_provider_requests(check.plan)
        provider_ids = {request.provider_id for request in requests}
        if not provider_ids or any(counts.get(provider_id, 0) >= per_provider for provider_id in provider_ids):
            continue
        if all(_receipt_exists(paths, request.request_id) for request in requests):
            continue
        selected.append(check)
        for provider_id in provider_ids:
            counts[provider_id] = counts.get(provider_id, 0) + 1
    return tuple(selected)


def run_checks(
    root: Path = ROOT,
    *,
    per_provider: int = 1,
    dry_run: bool = False,
    index_only: bool = False,
) -> dict[str, object]:
    discovered = discover_planned_checks(root)
    selected = (
        ()
        if index_only
        else select_unqueried_checks(root, discovered, per_provider=per_provider)
    )
    executed_plan_ids: list[str] = []
    for check in selected:
        requests = build_provider_requests(check.plan)
        if dry_run:
            continue
        else:
            execute_provider_plan(
                root,
                check.plan,
                max_requests=max(1, len(requests)),
            )
            executed_plan_ids.append(check.plan.plan_id)
    results = (
        [
            {
                "subjectId": check.plan.request.subject_id,
                "planId": check.plan.plan_id,
                "sourceBoundary": check.source_boundary,
                "sourcePath": check.source_path,
                "providers": sorted(
                    {
                        request.provider_id
                        for request in build_provider_requests(check.plan)
                    }
                ),
                "requestCount": len(build_provider_requests(check.plan)),
                "evidence": [],
            }
            for check in selected
        ]
        if dry_run
        else _completed_results(root, discovered)
    )
    run_receipt = root / RUN_RECEIPT_RELATIVE
    previous_payload = _load_json(run_receipt, {})
    previous = previous_payload if isinstance(previous_payload, dict) else {}
    checked_at = (
        str(previous.get("checkedAt"))
        if index_only and previous.get("checkedAt")
        else datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    )
    payload = {
        "schemaVersion": 1,
        "visibility": "internal-only",
        "checkedAt": checked_at,
        "dryRun": dry_run,
        "indexOnly": index_only,
        "discoveredPlans": len(discovered),
        "selectedPlans": len(selected),
        "completedPlans": len(results) if not dry_run else 0,
        "executedPlanIds": sorted(executed_plan_ids),
        "providerCoverage": sorted(
            {
                provider
                for result in results
                for provider in result["providers"]
                if isinstance(provider, str)
            }
        ),
        "results": results,
        "interpretationBoundary": (
            "Provider success confirms only the provider-scoped metadata. Owner and "
            "host records do not establish independent endorsement, event association, "
            "or a global reputation judgment. Discovery-only results remain candidates."
        ),
    }
    if not dry_run and (results or run_receipt.is_file()):
        _write_if_changed(run_receipt, payload)
    return payload


def _completed_results(
    root: Path, checks: Iterable[PlannedCheck]
) -> list[dict[str, object]]:
    paths = CredibilityPrivatePaths.for_project(root)
    results: list[dict[str, object]] = []
    for check in checks:
        requests = build_provider_requests(check.plan)
        evidence: list[dict[str, object]] = []
        for request in requests:
            receipt_path = _receipt_path(paths, request.request_id)
            if not receipt_path.is_file():
                continue
            receipt_payload = _load_json(receipt_path, {})
            if not isinstance(receipt_payload, dict):
                continue
            receipt = receipt_payload
            claim_scopes = sorted(
                {
                    scope
                    for step in check.plan.steps
                    if step.provider_id == request.provider_id
                    for scope in step.claim_scopes
                }
            )
            evidence.append(
                {
                    "providerId": request.provider_id,
                    "requestId": request.request_id,
                    "outcome": receipt.get("outcome"),
                    "claimScopes": claim_scopes,
                    "semanticResult": _semantic_result(root, request.provider_id, receipt),
                }
            )
        if not evidence:
            continue
        results.append(
            {
                "subjectId": check.plan.request.subject_id,
                "planId": check.plan.plan_id,
                "sourceBoundary": check.source_boundary,
                "sourcePath": check.source_path,
                "providers": sorted({row["providerId"] for row in evidence}),
                "requestCount": len(requests),
                "evidence": sorted(evidence, key=lambda item: str(item["requestId"])),
            }
        )
    return sorted(results, key=lambda item: (str(item["subjectId"]), str(item["planId"])))


def _semantic_result(
    root: Path, provider_id: str, receipt: dict[str, object]
) -> dict[str, object]:
    cache_path = receipt.get("cachePath")
    if receipt.get("outcome") != "success" or not isinstance(cache_path, str):
        return {"state": "unavailable"}
    body_path = root / cache_path
    if not body_path.is_file():
        return {"state": "cache_missing"}
    if provider_id == "owner_web":
        return {
            "state": "owner_content_available",
            "responseBytes": int(receipt.get("responseBytes") or 0),
        }
    try:
        body = json.loads(body_path.read_text(encoding="utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        return {"state": "non_json_metadata_available"}
    if provider_id == "google_dns_doh":
        answers = body.get("Answer") if isinstance(body, dict) else []
        return {
            "state": "dns_observed",
            "rcode": body.get("Status") if isinstance(body, dict) else None,
            "answerCount": len(answers) if isinstance(answers, list) else 0,
        }
    if provider_id == "rdap_registry":
        return {
            "state": "registration_metadata_available",
            "domain": body.get("ldhName") if isinstance(body, dict) else None,
        }
    if provider_id == "github_rest":
        return {
            "state": "repository_metadata_available",
            "repository": body.get("full_name") if isinstance(body, dict) else None,
            "archived": body.get("archived") if isinstance(body, dict) else None,
            "disabled": body.get("disabled") if isinstance(body, dict) else None,
        }
    if provider_id == "pypi":
        info = body.get("info") if isinstance(body, dict) else {}
        return {
            "state": "package_metadata_available",
            "package": info.get("name") if isinstance(info, dict) else None,
            "version": info.get("version") if isinstance(info, dict) else None,
        }
    if provider_id == "wikimedia":
        rows = body.get("search") if isinstance(body, dict) else []
        return {
            "state": "discovery_candidates",
            "resultCount": len(rows) if isinstance(rows, list) else 0,
            "candidateIds": [
                str(row["id"])
                for row in rows[:5]
                if isinstance(row, dict) and row.get("id")
            ]
            if isinstance(rows, list)
            else [],
        }
    return {"state": "provider_metadata_available"}


def _official_owner_checks(root: Path) -> list[PlannedCheck]:
    payload = json.loads((root / SPEAKERS_PATH.relative_to(ROOT)).read_text(encoding="utf-8"))
    rows = payload if isinstance(payload, list) else payload.get("speakers") or payload.get("data") or []
    checks: list[PlannedCheck] = []
    seen: set[tuple[str, str]] = set()
    for row in rows:
        if not isinstance(row, dict) or not row.get("name") or not row.get("website"):
            continue
        url = str(row["website"]).strip()
        parts = urlsplit(url)
        if (
            parts.scheme != "https"
            or not parts.hostname
            or any(character.isspace() for character in url)
        ):
            continue
        subject_id = f"person:{_slug(str(row['name']))}"
        owner_key = (subject_id, url)
        if owner_key not in seen:
            seen.add(owner_key)
            checks.append(
                PlannedCheck(
                    plan=plan_evidence_providers(
                        ProviderPlanningRequest.create(
                            subject_id=subject_id,
                            entity_type="person",
                            claim_scopes=("self_statement",),
                            owner_sources=(OwnerSource(url),),
                        )
                    ),
                    source_boundary="official_roster_owner_url",
                    source_path="raw/sources/official-speakers.json",
                )
            )
        domain = parts.hostname.casefold().removeprefix("www.")
        checks.append(
            PlannedCheck(
                plan=plan_evidence_providers(
                    ProviderPlanningRequest.create(
                        subject_id=subject_id,
                        entity_type="person",
                        claim_scopes=(
                            "dns_record_observation",
                            "domain_registration_metadata",
                        ),
                        identifiers=(EntityIdentifier("domain_name", domain),),
                    )
                ),
                source_boundary="official_roster_host_metadata",
                source_path="raw/sources/official-speakers.json",
            )
        )
    return checks


def _wiki_identifier_checks(root: Path) -> list[PlannedCheck]:
    checks: list[PlannedCheck] = []
    for page in sorted((root / "wiki").rglob("*.md")):
        relative = page.relative_to(root)
        if len(relative.parts) < 3 or page.name == "index.md":
            continue
        category = relative.parts[1]
        entity_type = {
            "companies": "company",
            "people": "person",
            "topics": "concept",
            "tools": "tool",
        }.get(category)
        if entity_type is None:
            continue
        subject_id = f"{entity_type}:{page.stem}"
        text = page.read_text(encoding="utf-8")
        accidental = _accidental_urls(text)
        for value in sorted(set(GITHUB_RE.findall(text))):
            repository = unquote(value).strip("/")
            if len(repository.split("/")) < 2:
                continue
            url = f"https://github.com/{repository}"
            checks.append(
                PlannedCheck(
                    plan=plan_evidence_providers(
                        ProviderPlanningRequest.create(
                            subject_id=subject_id,
                            entity_type=entity_type,
                            claim_scopes=("repository_metadata",),
                            identifiers=(
                                EntityIdentifier("github_repository", repository),
                            ),
                        )
                    ),
                    source_boundary=(
                        "accidental_third_party"
                        if url in accidental
                        else "curated_wiki_context"
                    ),
                    source_path=str(relative),
                )
            )
        for project in sorted(set(PYPI_RE.findall(text))):
            checks.append(
                PlannedCheck(
                    plan=plan_evidence_providers(
                        ProviderPlanningRequest.create(
                            subject_id=subject_id,
                            entity_type=entity_type,
                            claim_scopes=("python_package_metadata",),
                            identifiers=(EntityIdentifier("pypi_project", project),),
                        )
                    ),
                    source_boundary="curated_wiki_context",
                    source_path=str(relative),
                )
            )
        if category == "topics":
            title = _frontmatter_title(text) or page.stem.replace("-", " ")
            checks.append(
                PlannedCheck(
                    plan=plan_evidence_providers(
                        ProviderPlanningRequest.create(
                            subject_id=subject_id,
                            entity_type="concept",
                            claim_scopes=("encyclopedic_context",),
                            scoped_queries=(
                                ScopedProviderQuery.create(
                                    "wikimedia",
                                    {
                                        "context": "AI engineering conference topic",
                                        "entity_name": title,
                                        "entity_type": "concept",
                                    },
                                ),
                            ),
                        )
                    ),
                    source_boundary="discovery_only_topic_context",
                    source_path=str(relative),
                )
            )
    return checks


def _accidental_urls(text: str) -> set[str]:
    match = re.search(r"(?m)^accidentalResources:\s*\[(.*?)\]\s*$", text)
    if not match:
        return set()
    return {
        value.strip().strip("'\"")
        for value in match.group(1).split(",")
        if value.strip()
    }


def _frontmatter_title(text: str) -> str | None:
    match = re.search(r'(?m)^title:\s*["\']?(.+?)["\']?\s*$', text)
    return match.group(1) if match else None


def _slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")


def _priority(subject_id: str) -> int:
    try:
        return PRIORITY_SUBJECTS.index(subject_id)
    except ValueError:
        return len(PRIORITY_SUBJECTS)


def _receipt_exists(paths: CredibilityPrivatePaths, request_id: str) -> bool:
    return _receipt_path(paths, request_id).is_file()


def _receipt_path(paths: CredibilityPrivatePaths, request_id: str) -> Path:
    name = request_id.removeprefix("provider-request:") + ".json"
    return paths.receipts / "provider-fetch" / name


def _load_json(path: Path, default: object) -> object:
    if not path.is_file():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default


def _write_if_changed(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    rendered = json.dumps(payload, indent=2, ensure_ascii=True, sort_keys=True) + "\n"
    if path.is_file() and path.read_text(encoding="utf-8") == rendered:
        return
    path.write_text(rendered, encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--per-provider", type=int, default=1)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--index-only", action="store_true")
    args = parser.parse_args(argv)
    payload = run_checks(
        per_provider=args.per_provider,
        dry_run=args.dry_run,
        index_only=args.index_only,
    )
    print(json.dumps(payload, indent=2, ensure_ascii=True, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
