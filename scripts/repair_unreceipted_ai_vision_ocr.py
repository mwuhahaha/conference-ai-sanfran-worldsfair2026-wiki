#!/usr/bin/env python3
"""Audit or restore canonical OCR copied from unreceipted AI-vision caches."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / "raw" / "sources" / "slide-ocr-rapidmerge-audit.json"
CANONICAL_OCR = ROOT / "raw" / "sources" / "slide-ocr"
AI_VISION_OCR = ROOT / "raw" / "sources" / "slide-ocr-ai-vision"
PRE_MERGE_OCR = ROOT / "raw" / "sources" / "slide-ocr-before-rapidmerge"
RUNS = ROOT / ".ops" / "state" / "runs"
PUBLIC_SUMMARY = (
    ROOT / "raw" / "sources" / "slide-ocr-provenance-repair-summary.json"
)


def normalize_text(text: str) -> str:
    lines = []
    for line in text.replace("\r", "\n").splitlines():
        clean = re.sub(r"[ \t]+", " ", line).strip()
        clean = re.sub(r"\s+([,.;:!?])", r"\1", clean)
        if clean:
            lines.append(clean)
    return "\n".join(lines).strip()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def source_rows() -> list[dict]:
    payload = json.loads(AUDIT_PATH.read_text(encoding="utf-8"))
    return [
        row
        for row in payload.get("records", [])
        if row.get("bestSource") == "ai-vision" and row.get("updatedCanonical")
    ]


def inspect_row(row: dict) -> dict:
    image = ROOT / row["image"]
    video_id = image.parent.name
    name = f"{image.stem}.txt"
    canonical = CANONICAL_OCR / video_id / name
    ai_vision = AI_VISION_OCR / video_id / name
    receipt = ai_vision.with_suffix(".receipt.json")
    backup = PRE_MERGE_OCR / video_id / name
    result = {
        "videoId": video_id,
        "slide": image.name,
        "canonicalPath": str(canonical.relative_to(ROOT)),
        "aiVisionPath": str(ai_vision.relative_to(ROOT)),
        "backupPath": str(backup.relative_to(ROOT)),
    }
    if receipt.is_file():
        result["status"] = "receipted_requires_manual_review"
        return result
    if not canonical.is_file() or not ai_vision.is_file():
        result["status"] = "missing_required_artifact"
        return result
    canonical_bytes = canonical.read_bytes()
    ai_bytes = ai_vision.read_bytes()
    canonical_text = normalize_text(canonical_bytes.decode("utf-8", errors="ignore"))
    ai_text = normalize_text(ai_bytes.decode("utf-8", errors="ignore"))
    result.update(
        {
            "canonicalBeforeSha256": sha256_text(canonical_text),
            "aiVisionSha256": sha256_text(ai_text),
            "canonicalBytesSha256": hashlib.sha256(canonical_bytes).hexdigest(),
            "aiVisionBytesSha256": hashlib.sha256(ai_bytes).hexdigest(),
        }
    )
    if not backup.is_file():
        result["status"] = (
            "canonical_already_diverged"
            if canonical_text != ai_text
            else "missing_pre_merge_backup"
        )
        return result
    backup_bytes = backup.read_bytes()
    backup_text = normalize_text(backup_bytes.decode("utf-8", errors="ignore"))
    result["backupSha256"] = sha256_text(backup_text)
    result["backupBytesSha256"] = hashlib.sha256(backup_bytes).hexdigest()
    if canonical_bytes == backup_bytes:
        result["status"] = (
            "already_matches_pre_merge_backup"
            if canonical_bytes == ai_bytes
            else "restored_from_pre_merge_backup"
        )
    elif canonical_text != ai_text:
        result["status"] = (
            "normalized_restore_needs_exact_backup"
            if canonical_text == backup_text
            else "canonical_already_diverged"
        )
    else:
        result["status"] = "repairable_unreceipted_copy"
    return result


def write_public_summary(*, now: datetime, postcheck: list[dict]) -> None:
    source_audit_sha256 = hashlib.sha256(AUDIT_PATH.read_bytes()).hexdigest()
    restored = sum(
        row["status"] == "restored_from_pre_merge_backup" for row in postcheck
    )
    already_matched = sum(
        row["status"] == "already_matches_pre_merge_backup" for row in postcheck
    )
    summary = {
        "schemaVersion": 2,
        "generatedAt": now.isoformat(),
        "sourceAudit": str(AUDIT_PATH.relative_to(ROOT)),
        "sourceAuditSha256": source_audit_sha256,
        "historicalUnreceiptedAiVisionUpdates": len(postcheck),
        # Keep the legacy key for the RapidMerge page generator, but report only
        # files whose restored bytes differ from the superseded AI cache.
        "restoredCanonicalFiles": restored,
        "restoredFromBackupFiles": restored,
        "alreadyMatchedBackupFiles": already_matched,
        "remainingExactUnreceiptedCopies": sum(
            row["status"]
            in {
                "repairable_unreceipted_copy",
                "normalized_restore_needs_exact_backup",
            }
            for row in postcheck
        ),
        "ambiguousRecords": sum(
            row["status"]
            not in {
                "repairable_unreceipted_copy",
                "normalized_restore_needs_exact_backup",
                "canonical_already_diverged",
                "restored_from_pre_merge_backup",
                "already_matches_pre_merge_backup",
            }
            for row in postcheck
        ),
        "repairMethod": "restored_from_pre_merge_canonical_backup",
        "historicalAuditSuperseded": True,
        "historicalAiVisionAuditStatus": "superseded_untrusted",
        "historicalAiVisionAuditRecordedReceipts": 0,
        "historicalAiVisionUpdatesAcceptedByCurrentPolicy": 0,
    }
    PUBLIC_SUMMARY.parent.mkdir(parents=True, exist_ok=True)
    PUBLIC_SUMMARY.write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def atomic_restore(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        Path(temporary).replace(path)
    finally:
        Path(temporary).unlink(missing_ok=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args(argv)

    inspected = [inspect_row(row) for row in source_rows()]
    repairable = [
        row
        for row in inspected
        if row["status"]
        in {
            "repairable_unreceipted_copy",
            "normalized_restore_needs_exact_backup",
        }
    ]
    ambiguous = [
        row
        for row in inspected
        if row["status"]
        not in {
            "repairable_unreceipted_copy",
            "normalized_restore_needs_exact_backup",
            "canonical_already_diverged",
            "restored_from_pre_merge_backup",
            "already_matches_pre_merge_backup",
        }
    ]
    if args.apply and ambiguous:
        raise SystemExit(
            f"refusing repair with {len(ambiguous)} ambiguous provenance records"
        )

    repaired = []
    if args.apply:
        for row in repairable:
            backup = ROOT / row["backupPath"]
            canonical = ROOT / row["canonicalPath"]
            restored = backup.read_bytes()
            atomic_restore(canonical, restored)
            repaired.append(
                {
                    **row,
                    "status": "restored_from_pre_merge_backup",
                    "canonicalAfterSha256": hashlib.sha256(restored).hexdigest(),
                }
            )

    postcheck = [inspect_row(row) for row in source_rows()] if args.apply else inspected

    now = datetime.now(timezone.utc)
    receipt_path = args.receipt
    if receipt_path is None:
        receipt_path = RUNS / (
            now.strftime("%Y%m%dT%H%M%SZ")
            + "-unreceipted-ai-vision-ocr-repair.json"
        )
    payload = {
        "schemaVersion": 1,
        "generatedAt": now.isoformat(),
        "applied": args.apply,
        "sourceAudit": str(AUDIT_PATH.relative_to(ROOT)),
        "counts": {
            "historicalAiVisionUpdates": len(inspected),
            "repairable": len(repairable),
            "ambiguous": len(ambiguous),
            "repaired": len(repaired),
        },
        "records": repaired if args.apply else inspected,
    }
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    if args.apply and not ambiguous:
        write_public_summary(now=now, postcheck=postcheck)
    print(json.dumps({**payload["counts"], "receipt": str(receipt_path)}, sort_keys=True))
    return 1 if ambiguous else 0


if __name__ == "__main__":
    raise SystemExit(main())
