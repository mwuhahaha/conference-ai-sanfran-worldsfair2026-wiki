#!/usr/bin/env python3
"""Fail closed on public slide-classifier artifacts without current receipts.

Raw classifier JSON remains historical source evidence.  Markdown classifier
sections and HTML recreations are public derived artifacts, so they are
surfaced only while their audit passes the current policy/input/cache contract.
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile

if __package__:
    from scripts import process_slide_corpus_ai as corpus
else:  # Executed directly from scripts/.
    import process_slide_corpus_ai as corpus


ROOT = Path(__file__).resolve().parents[1]
SLIDE_PAGES = ROOT / "wiki" / "slides"
RECREATION_ROOT = ROOT / "wiki" / "assets" / "slide-recreations"
CLASSIFICATION_ROOT = ROOT / "raw" / "sources" / "slide-ai-classification"
RESOURCE_NOTE = ROOT / "wiki" / "resources" / "slide-ai-classifier-status.md"
PRIVATE_REPORT_JSON = (
    ROOT
    / ".ops"
    / "state"
    / "cache"
    / "wiki-maker"
    / "slide-ai"
    / "classifier-scan.json"
)
RECREATION_PUBLICATION_SCHEMA_VERSION = 1
PRIVATE_REPORT_SCHEMA_VERSION = 1

AUDIT_REF_RE = re.compile(
    r"Classification audit:\s*`"
    r"(?P<path>raw/sources/slide-ai-classification/"
    r"(?P<kind>dense|reconstructed|slides)/(?P<video_id>[^/`]+)/audit\.json)`"
)
RECREATION_LINK_RE = re.compile(
    r"/assets/slide-recreations/"
    r"(?P<kind>dense|reconstructed|slides)/(?P<video_id>[^/)]+)/"
    r"(?P<filename>[^/)]+\.html)"
)
SECTION_RE = re.compile(
    r"(?ms)^## (?P<heading>[^\n]+)\n(?P<body>.*?)(?=^## |\Z)"
)
WITHHELD_MARKER = "<!-- slide-ai-classifier-output-withheld -->"
CLASSIFIER_MARKERS = (
    "Classification audit:",
    "/assets/slide-recreations/",
    "AI slide classifier:",
    "### Hidden Non-Slide Evidence",
)
PAGE_SUFFIX = {
    "dense": "dense-slides",
    "reconstructed": "reconstructed-slides",
    "slides": "slides",
}


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
    )
    temporary_path = Path(temporary)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(text.rstrip() + "\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_path, path)
    finally:
        temporary_path.unlink(missing_ok=True)


def contract_args(
    *, model: str = "gpt-5.4-mini", min_confidence: float = 0.72
) -> argparse.Namespace:
    return argparse.Namespace(
        model=model,
        min_confidence=min_confidence,
        ocr_max_suspicious_ratio=0.08,
        no_ocr_reconcile=False,
        no_advanced_ocr=False,
    )


def item_for(kind: str, video_id: str) -> dict[str, object]:
    images = list((corpus.DECKS[kind] / video_id).glob("*.jpg"))
    return {"video_id": video_id, "deck_kind": kind, "images": len(images)}


def _manifest_sha256(manifest: list[dict[str, object]]) -> str:
    return hashlib.sha256(
        json.dumps(manifest, separators=(",", ":"), sort_keys=True).encode("utf-8")
    ).hexdigest()


def recreation_contract_violations(kind: str, video_id: str) -> list[str]:
    violations: list[str] = []
    audit = corpus.load_json(corpus.audit_path(video_id, kind))
    if (
        audit.get("publication_schema_version")
        != RECREATION_PUBLICATION_SCHEMA_VERSION
        or audit.get("publication_status") != "succeeded"
    ):
        return ["recreation_publication_not_successfully_bound"]
    accepted = audit.get("accepted")
    rejected = audit.get("rejected")
    manifest = audit.get("recreation_manifest")
    if (
        not isinstance(accepted, list)
        or not isinstance(rejected, list)
        or not isinstance(manifest, list)
    ):
        return ["recreation_publication_records_invalid"]

    expected_manifest: list[dict[str, object]] = []
    expected_paths: set[Path] = set()
    for record in accepted:
        if not isinstance(record, dict):
            violations.append("recreation_record_invalid")
            continue
        image_name = Path(str(record.get("image") or "")).stem
        if not image_name:
            violations.append("recreation_record_image_invalid")
            continue
        expected_path = RECREATION_ROOT / kind / video_id / f"{image_name}.html"
        raw_path = Path(str(record.get("recreation") or ""))
        record_path = raw_path if raw_path.is_absolute() else ROOT / raw_path
        if record_path != expected_path:
            violations.append(f"recreation_record_path_mismatch:{image_name}.html")
            continue
        digest = record.get("recreation_sha256")
        size = record.get("recreation_size_bytes")
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            violations.append(f"recreation_record_digest_invalid:{image_name}.html")
            continue
        if isinstance(size, bool) or not isinstance(size, int) or size < 0:
            violations.append(f"recreation_record_size_invalid:{image_name}.html")
            continue
        try:
            relative = expected_path.relative_to(ROOT)
        except ValueError:
            violations.append("recreation_root_outside_project")
            continue
        expected_manifest.append(
            {"path": str(relative), "sha256": digest, "size_bytes": size}
        )
        expected_paths.add(expected_path)
        if not expected_path.is_file() or expected_path.is_symlink():
            violations.append(f"recreation_asset_missing:{image_name}.html")
            continue
        data = expected_path.read_bytes()
        if hashlib.sha256(data).hexdigest() != digest or len(data) != size:
            violations.append(f"recreation_asset_digest_mismatch:{image_name}.html")

    if any(isinstance(record, dict) and record.get("recreation") for record in rejected):
        violations.append("rejected_record_has_recreation")
    expected_manifest.sort(key=lambda item: str(item["path"]))
    if manifest != expected_manifest:
        violations.append("recreation_manifest_mismatch")
    if audit.get("recreation_manifest_sha256") != _manifest_sha256(manifest):
        violations.append("recreation_manifest_digest_mismatch")

    live_directory = RECREATION_ROOT / kind / video_id
    actual_paths = {
        path
        for path in live_directory.rglob("*")
        if path.is_file()
    } if live_directory.is_dir() else set()
    if actual_paths != expected_paths:
        violations.append("recreation_asset_set_mismatch")
    return sorted(set(violations))


def audit_violations(
    kind: str,
    video_id: str,
    args: argparse.Namespace,
    cache: dict[tuple[str, str], list[str]],
) -> list[str]:
    key = (kind, video_id)
    if key not in cache:
        cache[key] = sorted(
            set(
                corpus.audit_validation(item_for(kind, video_id), args)
                + recreation_contract_violations(kind, video_id)
            )
        )
    return cache[key]


def classifier_section(body: str) -> bool:
    return any(marker in body for marker in CLASSIFIER_MARKERS)


def expected_page_name(kind: str, video_id: str) -> str:
    return f"youtube-{video_id}-{PAGE_SUFFIX[kind]}.md"


def validate_classifier_section(
    page: Path,
    body: str,
    args: argparse.Namespace,
    cache: dict[tuple[str, str], list[str]],
) -> list[str]:
    violations: list[str] = []
    references = list(AUDIT_REF_RE.finditer(body))
    if len(references) != 1:
        return ["classification_audit_reference_missing_or_ambiguous"]

    reference = references[0]
    kind = reference.group("kind")
    video_id = reference.group("video_id")
    if page.name != expected_page_name(kind, video_id):
        violations.append("classification_audit_page_mismatch")
    violations.extend(audit_violations(kind, video_id, args, cache))

    recreation_links = {
        (match.group("kind"), match.group("video_id"), match.group("filename"))
        for match in RECREATION_LINK_RE.finditer(body)
    }
    if any(link[:2] != (kind, video_id) for link in recreation_links):
        violations.append("recreation_link_audit_mismatch")

    audit = corpus.load_json(corpus.audit_path(video_id, kind))
    expected_recreations = {
        (kind, video_id, Path(str(record.get("recreation") or "")).name)
        for record in audit.get("accepted", [])
        if isinstance(record, dict) and record.get("recreation")
    }
    if recreation_links != expected_recreations:
        violations.append("recreation_link_set_mismatch")
    for _, _, filename in recreation_links:
        if not (RECREATION_ROOT / kind / video_id / filename).is_file():
            violations.append(f"recreation_asset_missing:{filename}")
    return sorted(set(violations))


def scan_pages(
    args: argparse.Namespace,
    cache: dict[tuple[str, str], list[str]],
) -> dict[str, object]:
    stale_sections: list[dict[str, object]] = []
    current_sections = 0
    withheld_sections = 0
    for page in sorted(SLIDE_PAGES.glob("*.md")):
        text = page.read_text(encoding="utf-8")
        covered_spans: list[tuple[int, int]] = []
        for section in SECTION_RE.finditer(text):
            body = section.group("body")
            covered_spans.append(section.span())
            if WITHHELD_MARKER in body:
                withheld_sections += 1
                if classifier_section(body):
                    stale_sections.append(
                        {
                            "page": str(page.relative_to(ROOT)),
                            "heading": section.group("heading"),
                            "violations": ["withheld_section_still_surfaces_classifier_output"],
                        }
                    )
                continue
            if not classifier_section(body):
                continue
            violations = validate_classifier_section(page, body, args, cache)
            if violations:
                stale_sections.append(
                    {
                        "page": str(page.relative_to(ROOT)),
                        "heading": section.group("heading"),
                        "violations": violations,
                    }
                )
            else:
                current_sections += 1

        for marker in CLASSIFIER_MARKERS:
            for match in re.finditer(re.escape(marker), text):
                if not any(start <= match.start() < end for start, end in covered_spans):
                    stale_sections.append(
                        {
                            "page": str(page.relative_to(ROOT)),
                            "heading": None,
                            "violations": ["classifier_output_outside_section"],
                        }
                    )
    return {
        "current_sections": current_sections,
        "withheld_sections": withheld_sections,
        "stale_sections": stale_sections,
    }


def recreation_asset_violations(
    asset: Path,
    args: argparse.Namespace,
    cache: dict[tuple[str, str], list[str]],
) -> list[str]:
    try:
        kind, video_id, filename = asset.relative_to(RECREATION_ROOT).parts
    except ValueError:
        return ["recreation_path_invalid"]
    if kind not in PAGE_SUFFIX or not filename.endswith(".html"):
        return ["recreation_path_invalid"]
    violations = list(audit_violations(kind, video_id, args, cache))
    audit = corpus.load_json(corpus.audit_path(video_id, kind))
    accepted_names = {
        Path(str(record.get("recreation") or "")).name
        for record in audit.get("accepted", [])
        if isinstance(record, dict) and record.get("recreation")
    }
    if filename not in accepted_names:
        violations.append("recreation_not_in_accepted_audit_records")
    return sorted(set(violations))


def scan_recreations(
    args: argparse.Namespace,
    cache: dict[tuple[str, str], list[str]],
) -> dict[str, object]:
    stale_assets: list[dict[str, object]] = []
    current_assets = 0
    if not RECREATION_ROOT.exists():
        return {"current_assets": 0, "stale_assets": stale_assets}
    for asset in sorted(RECREATION_ROOT.rglob("*")):
        if not asset.is_file():
            continue
        violations = recreation_asset_violations(asset, args, cache)
        if violations:
            stale_assets.append(
                {
                    "path": str(asset.relative_to(ROOT)),
                    "violations": violations,
                }
            )
        else:
            current_assets += 1
    return {"current_assets": current_assets, "stale_assets": stale_assets}


def audit_summary(
    args: argparse.Namespace,
    cache: dict[tuple[str, str], list[str]],
) -> dict[str, object]:
    versions: Counter[str] = Counter()
    current = 0
    stale = 0
    stale_recreation_records = 0
    for path in sorted(CLASSIFICATION_ROOT.glob("*/*/audit.json")):
        kind = path.parent.parent.name
        video_id = path.parent.name
        data = corpus.load_json(path)
        versions[str(data.get("policy_version") or "missing")] += 1
        if kind not in PAGE_SUFFIX or audit_violations(
            kind, video_id, args, cache
        ):
            stale += 1
            stale_recreation_records += sum(
                1
                for record in data.get("accepted", [])
                if isinstance(record, dict) and record.get("recreation")
            )
        else:
            current += 1
    return {
        "total": current + stale,
        "current": current,
        "stale": stale,
        "policy_versions": dict(sorted(versions.items())),
        "stale_recreation_records": stale_recreation_records,
    }


def scan(args: argparse.Namespace) -> dict[str, object]:
    cache: dict[tuple[str, str], list[str]] = {}
    pages = scan_pages(args, cache)
    recreations = scan_recreations(args, cache)
    report = {
        "contract": {
            "policy_version": corpus.POLICY_VERSION,
            "cache_schema_version": corpus.CACHE_SCHEMA_VERSION,
            "prompt_contract_sha256": corpus.PROMPT_CONTRACT_SHA256,
            "model": args.model,
            "min_confidence": args.min_confidence,
        },
        "audits": audit_summary(args, cache),
        "pages": pages,
        "recreations": recreations,
    }
    report["status_page"] = {
        "violations": status_page_violations(report),
    }
    return report


def withheld_body() -> str:
    return (
        f"{WITHHELD_MARKER}\n"
        "> **Classifier-derived view withheld.** The previous AI slide "
        "classification does not satisfy the current policy, prompt, exact-input, "
        "and cache-provenance contract. Original captured slide/frame files remain "
        "the source evidence. See [[resources/slide-ai-classifier-status]].\n\n"
    )


def quarantine_pages(
    args: argparse.Namespace,
    cache: dict[tuple[str, str], list[str]],
) -> int:
    changed = 0
    for page in sorted(SLIDE_PAGES.glob("*.md")):
        text = page.read_text(encoding="utf-8")

        def replace(section: re.Match[str]) -> str:
            body = section.group("body")
            if WITHHELD_MARKER in body or not classifier_section(body):
                return section.group(0)
            if not validate_classifier_section(page, body, args, cache):
                return section.group(0)
            return f"## {section.group('heading')}\n{withheld_body()}"

        updated = SECTION_RE.sub(replace, text)
        if updated != text:
            atomic_write_text(page, updated)
            changed += 1
    return changed


def quarantine_recreations(
    args: argparse.Namespace,
    cache: dict[tuple[str, str], list[str]],
) -> int:
    removed = 0
    if not RECREATION_ROOT.exists():
        return removed
    for asset in sorted(RECREATION_ROOT.rglob("*")):
        if asset.is_file() and recreation_asset_violations(asset, args, cache):
            asset.unlink()
            removed += 1
    for directory in sorted(
        (path for path in RECREATION_ROOT.rglob("*") if path.is_dir()),
        key=lambda path: len(path.parts),
        reverse=True,
    ):
        try:
            directory.rmdir()
        except OSError:
            pass
    return removed


def previous_quarantined_asset_count() -> int:
    if not RESOURCE_NOTE.exists():
        return 0
    match = re.search(
        r"HTML recreation artifacts removed by quarantine: (\d+)",
        RESOURCE_NOTE.read_text(encoding="utf-8"),
    )
    return int(match.group(1)) if match else 0


def resource_note_text(
    report: dict[str, object], *, quarantined_assets: int = 0
) -> str:
    audits = report["audits"]
    pages = report["pages"]
    quarantined_assets = max(
        quarantined_assets, previous_quarantined_asset_count()
    )
    return f'''---
title: "Slide AI Classifier Status"
category: "resources"
status: "quarantined"
sourceLabels: ["Historical AI classifier audits", "Current provenance contract"]
---

# Slide AI Classifier Status

AI-classified slide selections, extracted text, confidence labels, and HTML recreations are public derived artifacts. They are published only when their audit binds the current classifier policy and prompt to the exact source-image bytes and cache configuration.

## Current Validation

- Current classifier publication contract enforcement: active.
- Exact gate configuration and validation receipts: retained in private operator state.
- Historical audits retained: {audits['total']}.
- Audits satisfying the current contract: {audits['current']}.
- Historical audits not satisfying the current contract: {audits['stale']}.
- Slide pages with classifier-derived sections withheld: {pages['withheld_sections']}.
- Historical accepted-record recreations not published: {audits['stale_recreation_records']}.
- HTML recreation artifacts removed by quarantine: {quarantined_assets}.

The historical JSON audits remain under `raw/sources/slide-ai-classification/` for provenance and later reprocessing. They are not treated as current evidence, and the original captured slide/frame images remain available on their source layers. Restoring a classifier-derived public section requires a successful rerun under the current contract; changing a version label alone is insufficient.

## Source Boundary

This quarantine does not invalidate official event recordings, captured source images, transcript evidence, or separately labeled OCR. It suppresses only stale AI classifier decisions and the HTML views derived from them.

This page is maintained by `scripts/quarantine_stale_slide_ai.py`.
'''


def status_page_violations(report: dict[str, object]) -> list[str]:
    if not RESOURCE_NOTE.is_file():
        return ["classifier_status_page_missing"]
    expected = resource_note_text(report)
    try:
        actual = RESOURCE_NOTE.read_text(encoding="utf-8")
    except OSError:
        return ["classifier_status_page_unreadable"]
    if actual != expected:
        return ["classifier_status_page_stale_or_unbound"]
    return []


def write_resource_note(
    report: dict[str, object], *, quarantined_assets: int = 0
) -> None:
    text = resource_note_text(report, quarantined_assets=quarantined_assets)
    RESOURCE_NOTE.parent.mkdir(parents=True, exist_ok=True)
    atomic_write_text(RESOURCE_NOTE, text)


def private_report_payload(report: dict[str, object]) -> dict[str, object]:
    canonical = json.dumps(
        report, separators=(",", ":"), sort_keys=True
    ).encode("utf-8")
    return {
        "schemaVersion": PRIVATE_REPORT_SCHEMA_VERSION,
        "generatedBy": "scripts/quarantine_stale_slide_ai.py",
        "reportSha256": hashlib.sha256(canonical).hexdigest(),
        "report": report,
    }


def private_report_path() -> Path:
    adapter_state = os.environ.get("WIKI_MAKER_ADAPTER_STATE_DIR")
    if adapter_state:
        return Path(adapter_state).resolve() / "classifier-scan.json"
    return PRIVATE_REPORT_JSON


def write_private_report(report: dict[str, object]) -> Path:
    path = private_report_path()
    atomic_write_text(
        path,
        json.dumps(
            private_report_payload(report),
            indent=2,
            ensure_ascii=False,
            sort_keys=True,
        ),
    )
    return path


def public_violation_count(report: dict[str, object]) -> int:
    return len(report["pages"]["stale_sections"]) + len(
        report["recreations"]["stale_assets"]
    ) + len(report["status_page"]["violations"])


def concise(report: dict[str, object]) -> dict[str, object]:
    return {
        "contract": {
            "enforcement": "active",
            "details": "private_operator_receipt",
        },
        "audits": {
            "total": report["audits"]["total"],
            "current": report["audits"]["current"],
            "stale": report["audits"]["stale"],
            "stale_recreation_records": report["audits"][
                "stale_recreation_records"
            ],
        },
        "pages": {
            "current_sections": report["pages"]["current_sections"],
            "withheld_sections": report["pages"]["withheld_sections"],
            "stale_sections": len(report["pages"]["stale_sections"]),
        },
        "recreations": {
            "current_assets": report["recreations"]["current_assets"],
            "stale_assets": len(report["recreations"]["stale_assets"]),
        },
        "status_page": {
            "current": not report["status_page"]["violations"],
            "violations": report["status_page"]["violations"],
        },
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--model", default="gpt-5.4-mini")
    parser.add_argument("--min-confidence", type=float, default=0.72)
    parser.add_argument("--details", action="store_true")
    options = parser.parse_args(argv)
    try:
        min_confidence = corpus.validate_min_confidence(options.min_confidence)
    except ValueError as exc:
        parser.error(str(exc))
    args = contract_args(model=options.model, min_confidence=min_confidence)

    before = scan(args)
    payload: dict[str, object] = {"before": concise(before)}
    if options.apply:
        cache: dict[tuple[str, str], list[str]] = {}
        pages_changed = quarantine_pages(args, cache)
        assets_removed = quarantine_recreations(args, cache)
        after = scan(args)
        write_resource_note(
            after,
            quarantined_assets=len(before["recreations"]["stale_assets"]),
        )
        after = scan(args)
        payload.update(
            {
                "actions": {
                    "pages_changed": pages_changed,
                    "assets_removed": assets_removed,
                    "resource_note": str(RESOURCE_NOTE.relative_to(ROOT)),
                },
                "after": concise(after),
            }
        )
        report = after
    else:
        report = before
    private_report = write_private_report(report)
    payload["private_report"] = str(private_report.relative_to(ROOT))
    if options.details:
        payload["violations"] = {
            "pages": report["pages"]["stale_sections"],
            "recreations": report["recreations"]["stale_assets"],
            "status_page": report["status_page"]["violations"],
        }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 1 if public_violation_count(report) else 0


if __name__ == "__main__":
    raise SystemExit(main())
