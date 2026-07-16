#!/usr/bin/env python3
"""Run AI slide classification across the video slide corpus.

The corpus often has three deck variants for the same video. For whole-video
coverage, use the highest-signal deck available: dense crops first,
reconstructed crops second, full-frame standard slides last.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
RUNS = ROOT / ".ops" / "state" / "runs"
POLICY_VERSION = "agent-triage-ocr-reconcile-v2"
MAX_WORKERS = 8

DECKS = {
    "dense": WIKI / "assets" / "dense-slides",
    "reconstructed": WIKI / "assets" / "reconstructed-slides",
    "slides": WIKI / "assets" / "slides",
}
PREFERENCE = ["dense", "reconstructed", "slides"]


def video_ids_for(kind: str) -> set[str]:
    base = DECKS[kind]
    if not base.exists():
        return set()
    return {
        path.name
        for path in base.iterdir()
        if path.is_dir() and list(path.glob("*.jpg")) and not path.name.startswith("google-photos-")
    }


def selected_work() -> list[dict]:
    remaining: set[str] = set()
    by_kind = {kind: video_ids_for(kind) for kind in PREFERENCE}
    for ids in by_kind.values():
        remaining |= ids

    work = []
    for video_id in sorted(remaining):
        for kind in PREFERENCE:
            if video_id in by_kind[kind]:
                images = sorted((DECKS[kind] / video_id).glob("*.jpg"))
                work.append({"video_id": video_id, "deck_kind": kind, "images": len(images)})
                break
    return work


def audit_path(video_id: str, kind: str) -> Path:
    return ROOT / "raw" / "sources" / "slide-ai-classification" / kind / video_id / "audit.json"


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def completed(video_id: str, kind: str, image_count: int, model: str) -> bool:
    audit = load_json(audit_path(video_id, kind))
    if not audit:
        return False
    if audit.get("model") != model:
        return False
    if audit.get("policy_version") != POLICY_VERSION:
        return False
    return int(audit.get("accepted_count", 0)) + int(audit.get("rejected_count", 0)) >= image_count


def run_one(item: dict, args: argparse.Namespace) -> dict:
    cmd = [
        "python3",
        "scripts/classify_and_recreate_slides.py",
        f"--video-id={item['video_id']}",
        "--deck-kind",
        item["deck_kind"],
        "--model",
        args.model,
        "--min-confidence",
        str(args.min_confidence),
        "--timeout",
        str(args.timeout),
        "--batch-size",
        str(args.batch_size),
        "--reconcile-timeout",
        str(args.reconcile_timeout),
        "--ocr-max-suspicious-ratio",
        str(args.ocr_max_suspicious_ratio),
        "--reuse",
    ]
    if args.no_ocr_reconcile:
        cmd.append("--no-ocr-reconcile")
    if args.no_advanced_ocr:
        cmd.append("--no-advanced-ocr")
    started = time.time()
    cp = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, timeout=args.job_timeout)
    elapsed = round(time.time() - started, 3)
    record = {
        **item,
        "elapsed_seconds": elapsed,
        "returncode": cp.returncode,
        "stdout": cp.stdout.strip()[-2000:],
        "stderr": cp.stderr.strip()[-2000:],
    }
    if cp.returncode == 0:
        audit = load_json(audit_path(item["video_id"], item["deck_kind"]))
        record.update(
            {
                "accepted_count": audit.get("accepted_count", 0),
                "rejected_count": audit.get("rejected_count", 0),
            }
        )
    return record


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--model", default="gpt-5.4-mini")
    parser.add_argument("--min-confidence", type=float, default=0.72)
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--reconcile-timeout", type=int, default=90)
    parser.add_argument("--ocr-max-suspicious-ratio", type=float, default=0.08)
    parser.add_argument("--no-ocr-reconcile", action="store_true")
    parser.add_argument("--no-advanced-ocr", action="store_true")
    parser.add_argument("--job-timeout", type=int, default=7200)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--shard-count", type=int, default=1)
    parser.add_argument("--shard-index", type=int, default=0)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    work = selected_work()
    if args.shard_count < 1:
        raise SystemExit("--shard-count must be >= 1")
    if args.shard_index < 0 or args.shard_index >= args.shard_count:
        raise SystemExit("--shard-index must be between 0 and shard-count - 1")
    if args.workers < 1 or args.workers > MAX_WORKERS:
        raise SystemExit(f"--workers must be between 1 and {MAX_WORKERS}")
    if args.shard_count > 1:
        work = [item for index, item in enumerate(work) if index % args.shard_count == args.shard_index]

    pending = [
        item
        for item in work
        if args.force or not completed(item["video_id"], item["deck_kind"], item["images"], args.model)
    ]
    if args.limit:
        pending = pending[: args.limit]

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    report_path = RUNS / f"{stamp}-slide-ai-corpus-s{args.shard_index}-of-{args.shard_count}.json"
    report = {
        "model": args.model,
        "min_confidence": args.min_confidence,
        "total_videos": len(work),
        "pending_videos": len(pending),
        "total_images_selected": sum(item["images"] for item in work),
        "pending_images_selected": sum(item["images"] for item in pending),
        "shard_count": args.shard_count,
        "shard_index": args.shard_index,
        "dry_run": args.dry_run,
        "no_advanced_ocr": args.no_advanced_ocr,
        "workers": args.workers,
        "status": "planned" if args.dry_run else "running",
        "items": [],
    }

    if args.dry_run:
        report["items"] = pending
        print(json.dumps({k: report[k] for k in report if k != "items"}, sort_keys=True))
        return 0

    RUNS.mkdir(parents=True, exist_ok=True)
    failures = 0
    workers = max(1, args.workers)
    if workers == 1:
        for index, item in enumerate(pending, 1):
            print(
                json.dumps(
                    {
                        "index": index,
                        "pending": len(pending),
                        "video_id": item["video_id"],
                        "deck_kind": item["deck_kind"],
                        "images": item["images"],
                    },
                    sort_keys=True,
                ),
                flush=True,
            )
            try:
                result = run_one(item, args)
            except Exception as exc:
                result = {
                    **item,
                    "elapsed_seconds": None,
                    "returncode": 1,
                    "stdout": "",
                    "stderr": repr(exc),
                    "status": "failed",
                }
            else:
                result["status"] = "succeeded" if result["returncode"] == 0 else "failed"
            report["items"].append(result)
            if result["returncode"] != 0:
                failures += 1
            report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    else:
        with ThreadPoolExecutor(max_workers=workers) as pool:
            future_to_item = {}
            for index, item in enumerate(pending, 1):
                print(
                    json.dumps(
                        {
                            "index": index,
                            "pending": len(pending),
                            "video_id": item["video_id"],
                            "deck_kind": item["deck_kind"],
                            "images": item["images"],
                            "workers": workers,
                        },
                        sort_keys=True,
                    ),
                    flush=True,
                )
                future_to_item[pool.submit(run_one, item, args)] = item
            for future in as_completed(future_to_item):
                item = future_to_item[future]
                try:
                    result = future.result()
                except Exception as exc:
                    result = {
                        **item,
                        "elapsed_seconds": None,
                        "returncode": 1,
                        "stdout": "",
                        "stderr": repr(exc),
                        "status": "failed",
                    }
                else:
                    result["status"] = "succeeded" if result["returncode"] == 0 else "failed"
                report["items"].append(result)
                if result["returncode"] != 0:
                    failures += 1
                print(
                    json.dumps(
                        {
                            "completed": len(report["items"]),
                            "finished": len(report["items"]),
                            "pending": len(pending),
                            "video_id": result["video_id"],
                            "status": result["status"],
                            "returncode": result["returncode"],
                            "elapsed_seconds": result["elapsed_seconds"],
                            "accepted_count": result.get("accepted_count"),
                            "rejected_count": result.get("rejected_count"),
                        },
                        sort_keys=True,
                    ),
                    flush=True,
                )
                report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    report["failures"] = failures
    report["status"] = "degraded" if failures else "succeeded"
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({"status": report["status"], "processed": len(pending), "failures": failures, "report": str(report_path)}, sort_keys=True))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
