#!/usr/bin/env python3
"""Run the full slide OCR improvement and wiki refresh pipeline."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

try:
    from improve_slide_ocr_rapidmerge import AUDIT_PATH, write_audit_page
except ModuleNotFoundError:  # Imported as scripts.run_slide_ocr_pipeline.
    from scripts.improve_slide_ocr_rapidmerge import AUDIT_PATH, write_audit_page


ROOT = Path(__file__).resolve().parents[1]


def run(cmd: list[str]) -> subprocess.CompletedProcess:
    print("+ " + " ".join(cmd), flush=True)
    cp = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
    if cp.stdout:
        print(cp.stdout, end="" if cp.stdout.endswith("\n") else "\n")
    if cp.stderr:
        print(cp.stderr, file=sys.stderr, end="" if cp.stderr.endswith("\n") else "\n")
    if cp.returncode != 0:
        raise SystemExit(cp.returncode)
    return cp


def refreshed_count(output: str) -> int | None:
    match = re.search(r"refreshed\s+(\d+)\s+slide pages", output)
    return int(match.group(1)) if match else None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true", help="Process all slide images instead of suspicious/weak OCR only.")
    parser.add_argument("--skip-perfect", action="store_true", help="Skip slides whose current OCR already passes the high-confidence clean-text heuristic.")
    parser.add_argument("--limit", type=int, default=0, help="Debug limit passed to the OCR improvement tool.")
    parser.add_argument("--min-gain", type=float, default=35.0)
    parser.add_argument("--deep-variants", action="store_true", help="Use slower extra crop/threshold OCR variants.")
    parser.add_argument("--variant-max-old-score", type=float, default=50.0, help="Only use crop/high-contrast variants below this old OCR score.")
    parser.add_argument("--engine", action="append", default=[], help="OCR engine to use. Repeatable: rapidocr, paddleocr, easyocr, doctr, surya.")
    parser.add_argument("--no-live-ocr", action="store_true", help="Merge existing OCR/operator sources without running live OCR engines.")
    parser.add_argument("--enable-surya", action="store_true", help="Enable Surya only after confirming model-weight license terms fit this use.")
    parser.add_argument("--vision-rescue", action="store_true", help="Run AI vision interpretation for low-confidence/manual-queue slides after OCR.")
    parser.add_argument("--vision-provider", choices=["auto", "ollama", "codex-cli", "openai"], default="auto")
    parser.add_argument("--vision-codex-model", default="", help="Codex CLI model for vision rescue; defaults to the rescue tool default.")
    parser.add_argument("--vision-limit", type=int, default=0)
    parser.add_argument("--vision-jobs", type=int, default=1, help="Parallel vision rescue reads. Keep low for Codex CLI provider.")
    parser.add_argument("--classify-video-id", action="append", default=[], help="Run low-cost vision slide/non-slide classification for a specific video deck.")
    parser.add_argument("--classify-deck-kind", choices=["slides", "dense", "reconstructed"], default="slides")
    parser.add_argument("--classify-model", default="gpt-5.4-mini")
    parser.add_argument("--remove-non-slides", action="store_true", help="Compatibility alias: hide rejected non-slide frames from visible wiki slide decks while keeping evidence files.")
    parser.add_argument("--internal-eval-log", action="store_true", help="Write ignored internal operator/tool comparison log.")
    parser.add_argument("--no-build", action="store_true", help="Skip npm static export.")
    parser.add_argument("--no-dependent-indexes", action="store_true", help="Skip topic/tool/word-cloud refreshes.")
    args = parser.parse_args()

    improve_cmd = [sys.executable, "scripts/improve_slide_ocr_rapidmerge.py", "--min-gain", str(args.min_gain)]
    if args.all:
        improve_cmd.append("--all")
    if args.skip_perfect:
        improve_cmd.append("--skip-perfect")
    if args.limit:
        improve_cmd.extend(["--limit", str(args.limit)])
    if args.deep_variants:
        improve_cmd.append("--deep-variants")
    for engine in args.engine:
        improve_cmd.extend(["--engine", engine])
    if args.no_live_ocr:
        improve_cmd.append("--no-live-ocr")
    if args.enable_surya:
        improve_cmd.append("--enable-surya")
    if args.internal_eval_log:
        improve_cmd.extend(["--log-manual-queue", "--internal-eval-log"])
    improve_cmd.extend(["--variant-max-old-score", str(args.variant_max_old_score)])
    run(improve_cmd)

    if args.vision_rescue:
        vision_cmd = [
            sys.executable,
            "scripts/interpret_slide_text_with_vision.py",
            "--provider",
            args.vision_provider,
        ]
        if args.vision_limit:
            vision_cmd.extend(["--limit", str(args.vision_limit)])
        if args.vision_codex_model:
            vision_cmd.extend(["--codex-model", args.vision_codex_model])
        if args.vision_jobs:
            vision_cmd.extend(["--jobs", str(args.vision_jobs)])
        run(vision_cmd)
        merge_ai_cmd = [
            sys.executable,
            "scripts/improve_slide_ocr_rapidmerge.py",
            "--all" if args.all else "--log-manual-queue",
            "--skip-perfect",
            "--no-live-ocr",
            "--min-gain",
            str(args.min_gain),
            "--variant-max-old-score",
            str(args.variant_max_old_score),
        ]
        if args.all:
            merge_ai_cmd.append("--log-manual-queue")
        if args.internal_eval_log:
            merge_ai_cmd.append("--internal-eval-log")
        run(merge_ai_cmd)

    refresh = run([sys.executable, "scripts/refresh_slide_pages_from_ocr.py"])
    count = refreshed_count(refresh.stdout or "")
    if AUDIT_PATH.exists():
        write_audit_page(json.loads(AUDIT_PATH.read_text()), refreshed_pages=count)

    for video_id in args.classify_video_id:
        classify_cmd = [
            sys.executable,
            "scripts/classify_and_recreate_slides.py",
            "--video-id",
            video_id,
            "--deck-kind",
            args.classify_deck_kind,
            "--model",
            args.classify_model,
        ]
        if args.remove_non_slides:
            classify_cmd.append("--hide-rejected")
        run(classify_cmd)

    run([sys.executable, "scripts/quarantine_stale_slide_ai.py"])

    if not args.no_dependent_indexes:
        run([sys.executable, "scripts/generate_tool_inventory.py"])
        run([sys.executable, "scripts/generate_agentic_web_topic.py"])
        run([sys.executable, "scripts/generate_phrase_word_cloud.py"])
        run([sys.executable, "scripts/generate_agent_source_index.py"])

    if not args.no_build:
        run(["npm", "run", "build"])

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
