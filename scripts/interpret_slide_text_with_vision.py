#!/usr/bin/env python3
"""Use a vision model to rescue slide text when OCR confidence is low."""

from __future__ import annotations

import argparse
import base64
import concurrent.futures
import hashlib
import json
import math
import os
import re
import shutil
import subprocess
import time
from pathlib import Path

import requests

try:
    from slide_codex_safety import CODEX_NO_TOOL_ARGS
except ModuleNotFoundError:  # Imported as scripts.interpret_slide_text_with_vision.
    from scripts.slide_codex_safety import CODEX_NO_TOOL_ARGS

from improve_slide_ocr_rapidmerge import (
    AUDIT_PATH,
    PROVENANCE_REPAIR_SUMMARY,
    is_weak,
    text_path,
    write_text,
)
try:
    from slide_vision_cache_contract import (
        CACHE_SCHEMA_VERSION,
        CODEX_PROMPT_PREFIX,
        MIN_ACCEPTED_CONFIDENCE,
        PROMPT_CONTRACT_SHA256,
        PROMPT_CONTRACT_VERSION,
        VISION_PROMPT as PROMPT,
    )
except ModuleNotFoundError:  # Imported as scripts.interpret_slide_text_with_vision.
    from scripts.slide_vision_cache_contract import (
        CACHE_SCHEMA_VERSION,
        CODEX_PROMPT_PREFIX,
        MIN_ACCEPTED_CONFIDENCE,
        PROMPT_CONTRACT_SHA256,
        PROMPT_CONTRACT_VERSION,
        VISION_PROMPT as PROMPT,
    )


ROOT = Path(__file__).resolve().parents[1]
SLIDE_ASSETS = ROOT / "wiki" / "assets" / "slides"
CANONICAL_OCR = ROOT / "raw" / "sources" / "slide-ocr"
AI_VISION_OCR = ROOT / "raw" / "sources" / "slide-ocr-ai-vision"
AI_VISION_AUDIT = ROOT / "raw" / "sources" / "slide-ocr-ai-vision-audit.json"
AI_VISION_PAGE = ROOT / "wiki" / "resources" / "slide-ocr-ai-vision-audit.md"

JSON_RE = re.compile(r"\{.*\}", re.S)
DEFAULT_CODEX_VISION_MODEL = "gpt-5.4-mini"
MAX_JOBS = 8


def encode_image(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("utf-8")


def parse_json(text: str) -> dict:
    match = JSON_RE.search(text or "")
    payload = match.group(0) if match else text
    try:
        data = json.loads(payload)
    except (json.JSONDecodeError, TypeError) as exc:
        raise ValueError(f"model returned malformed JSON: {text[:180]}") from exc
    if not isinstance(data, dict):
        raise ValueError("model returned malformed JSON: expected an object")
    confidence_value = data.get("confidence")
    if type(confidence_value) not in {int, float}:
        raise ValueError("model returned a non-numeric confidence")
    try:
        confidence = float(confidence_value)
    except (TypeError, ValueError) as exc:
        raise ValueError("model returned a non-numeric confidence") from exc
    if not math.isfinite(confidence) or not 0 <= confidence <= 1:
        raise ValueError("model returned confidence outside 0..1")
    return {
        "text": str(data.get("text") or "").strip(),
        "confidence": confidence,
        "notes": str(data.get("notes") or "").strip(),
    }


def openai_responses(image: Path, ocr_text: str, model: str, timeout: int) -> dict:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set")
    body = {
        "model": model,
        "input": [
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": PROMPT + (ocr_text or "(none)")},
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{encode_image(image)}",
                    },
                ],
            }
        ],
        "max_output_tokens": 400,
    }
    response = requests.post(
        "https://api.openai.com/v1/responses",
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        json=body,
        timeout=timeout,
    )
    response.raise_for_status()
    data = response.json()
    return parse_json(data.get("output_text") or json.dumps(data))


def codex_cli(image: Path, ocr_text: str, model: str, timeout: int) -> dict:
    command = shutil.which("codex")
    if not command:
        raise RuntimeError("codex CLI is not available on PATH")
    out_dir = ROOT / ".ops" / "state" / "cache" / "codex-vision-samples"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"{image.parent.name}-{image.stem}-{int(time.time() * 1000)}.json"
    prompt = CODEX_PROMPT_PREFIX + (ocr_text or "(none)")
    cmd = [
        command,
        "exec",
        "--ephemeral",
        "--ignore-user-config",
        "--ignore-rules",
        "--skip-git-repo-check",
        *CODEX_NO_TOOL_ARGS,
        "-s",
        "read-only",
        "-C",
        str(out_dir),
        "-i",
        str(image),
        "-o",
        str(out_file),
    ]
    if model:
        cmd.extend(["-m", model])
    cmd.append(prompt)
    env = os.environ.copy()
    env.pop("OPENAI_API_KEY", None)
    cp = subprocess.run(
        cmd,
        cwd=out_dir,
        input="",
        text=True,
        capture_output=True,
        timeout=timeout,
        env=env,
    )
    if cp.returncode != 0:
        raise RuntimeError((cp.stderr or cp.stdout)[-1000:])
    if not out_file.exists():
        raise RuntimeError("codex CLI did not write an output message")
    return parse_json(out_file.read_text(encoding="utf-8", errors="ignore"))


def ollama_generate(image: Path, ocr_text: str, model: str, timeout: int) -> dict:
    endpoint = os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434").rstrip("/")
    body = {
        "model": model,
        "prompt": PROMPT + (ocr_text or "(none)"),
        "images": [encode_image(image)],
        "stream": False,
        "format": "json",
        "options": {"temperature": 0},
    }
    response = requests.post(f"{endpoint}/api/generate", json=body, timeout=timeout)
    response.raise_for_status()
    return parse_json(response.json().get("response", ""))


def provider_available(provider: str) -> bool:
    if provider == "openai":
        return bool(os.environ.get("OPENAI_API_KEY"))
    if provider == "codex-cli":
        return shutil.which("codex") is not None
    if provider == "ollama":
        endpoint = os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434").rstrip("/")
        try:
            return requests.get(f"{endpoint}/api/tags", timeout=2).ok
        except Exception:
            return False
    return False


def choose_provider(provider: str) -> str | None:
    if provider != "auto":
        return provider if provider_available(provider) else None
    if provider_available("ollama"):
        return "ollama"
    if provider_available("codex-cli"):
        return "codex-cli"
    if provider_available("openai"):
        return "openai"
    return None


def current_ocr(slide: Path) -> str:
    path = text_path(CANONICAL_OCR, slide)
    return path.read_text(encoding="utf-8", errors="ignore").strip() if path.exists() else ""


def existing_vision_text(slide: Path) -> str:
    path = text_path(AI_VISION_OCR, slide)
    return path.read_text(encoding="utf-8", errors="ignore").strip() if path.exists() else ""


def cache_receipt_path(slide: Path) -> Path:
    return text_path(AI_VISION_OCR, slide).with_suffix(".receipt.json")


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _model_for_provider(provider: str, args: argparse.Namespace) -> str:
    return str(
        {
            "ollama": args.ollama_model,
            "codex-cli": args.codex_model,
            "openai": args.openai_model,
        }.get(provider, "")
    )


def _cache_identity(
    provider: str, slide: Path, ocr_text: str, args: argparse.Namespace
) -> dict[str, object]:
    return {
        "schemaVersion": CACHE_SCHEMA_VERSION,
        "status": "accepted",
        "imageSha256": _sha256_bytes(slide.read_bytes()),
        "ocrSha256": _sha256_bytes(ocr_text.encode("utf-8")),
        "provider": provider,
        "model": _model_for_provider(provider, args),
        "promptContractVersion": PROMPT_CONTRACT_VERSION,
        "promptContractSha256": PROMPT_CONTRACT_SHA256,
        "minimumAcceptedConfidence": float(args.min_confidence),
    }


def _load_valid_cache(
    provider: str, slide: Path, ocr_text: str, args: argparse.Namespace
) -> tuple[str, dict[str, object]] | None:
    output = text_path(AI_VISION_OCR, slide)
    receipt_path = cache_receipt_path(slide)
    if not output.is_file() or not receipt_path.is_file():
        return None
    try:
        text = output.read_text(encoding="utf-8").strip()
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        confidence = float(receipt.get("confidence"))
    except (OSError, TypeError, ValueError, json.JSONDecodeError):
        return None
    expected = _cache_identity(provider, slide, ocr_text, args)
    if not text or any(receipt.get(key) != value for key, value in expected.items()):
        return None
    if not 0 <= confidence <= 1 or confidence < args.min_confidence:
        return None
    if receipt.get("textSha256") != _sha256_bytes(text.encode("utf-8")):
        return None
    return text, receipt


def _clear_cache(slide: Path) -> None:
    text_path(AI_VISION_OCR, slide).unlink(missing_ok=True)
    cache_receipt_path(slide).unlink(missing_ok=True)


def _write_accepted_cache(
    provider: str,
    slide: Path,
    ocr_text: str,
    result: dict[str, object],
    args: argparse.Namespace,
) -> tuple[Path, Path]:
    output = text_path(AI_VISION_OCR, slide)
    receipt_path = cache_receipt_path(slide)
    text = str(result["text"]).strip()
    receipt = {
        **_cache_identity(provider, slide, ocr_text, args),
        "confidence": float(result["confidence"]),
        "textSha256": _sha256_bytes(text.encode("utf-8")),
        "writtenAtEpoch": time.time(),
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output_tmp = output.with_suffix(output.suffix + ".tmp")
    receipt_tmp = receipt_path.with_suffix(receipt_path.suffix + ".tmp")
    output_tmp.write_text(text + "\n", encoding="utf-8")
    receipt_tmp.write_text(
        json.dumps(receipt, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    output_tmp.replace(output)
    receipt_tmp.replace(receipt_path)
    return output, receipt_path


def candidate_slides(args: argparse.Namespace) -> list[Path]:
    if args.video_id or args.slide:
        slides = []
        video_ids = args.video_id or ["*"]
        slide_names = args.slide or ["*.jpg"]
        for video_id in video_ids:
            for slide_name in slide_names:
                slides.extend(sorted(SLIDE_ASSETS.glob(f"{video_id}/{slide_name}")))
        return slides
    if AUDIT_PATH.exists() and not args.ignore_rapidmerge_audit:
        audit = json.loads(AUDIT_PATH.read_text(encoding="utf-8"))
        rows = [row for row in audit.get("records", []) if row.get("manualReviewNeeded")]
        rows.sort(key=lambda row: row.get("bestScore", 0))
        return [ROOT / row["image"] for row in rows if (ROOT / row["image"]).exists()]
    slides = sorted(SLIDE_ASSETS.glob("*/*.jpg"))
    return [slide for slide in slides if is_weak(current_ocr(slide))]


def interpret(provider: str, image: Path, ocr_text: str, args: argparse.Namespace) -> dict:
    if provider == "openai":
        return openai_responses(image, ocr_text, args.openai_model, args.timeout)
    if provider == "codex-cli":
        return codex_cli(image, ocr_text, args.codex_model, args.timeout)
    if provider == "ollama":
        return ollama_generate(image, ocr_text, args.ollama_model, args.timeout)
    raise RuntimeError(f"Unsupported provider: {provider}")


def process_slide(provider: str, slide: Path, args: argparse.Namespace) -> dict:
    ocr_text = current_ocr(slide)
    record = {"image": str(slide.relative_to(ROOT)), "oldPreview": ocr_text[:220]}
    if args.skip_existing:
        cached = _load_valid_cache(provider, slide, ocr_text, args)
        if cached:
            existing, receipt = cached
            record.update(
                {
                    "text": existing,
                    "confidence": receipt["confidence"],
                    "notes": "validated AI vision cache reused",
                    "skippedExisting": True,
                    "written": str(text_path(AI_VISION_OCR, slide).relative_to(ROOT)),
                    "cacheReceipt": str(cache_receipt_path(slide).relative_to(ROOT)),
                }
            )
            return record
    _clear_cache(slide)
    record["attempted"] = True
    try:
        result = interpret(provider, slide, ocr_text, args)
    except Exception as exc:
        record["error"] = repr(exc)
        return record
    record.update(result)
    if result["text"] and result["confidence"] >= args.min_confidence:
        out, receipt_path = _write_accepted_cache(
            provider, slide, ocr_text, result, args
        )
        record["written"] = str(out.relative_to(ROOT))
        record["cacheReceipt"] = str(receipt_path.relative_to(ROOT))
        record["cacheStatus"] = "accepted"
    else:
        record["cacheStatus"] = "not_accepted"
    return record


def write_audit_page(audit: dict) -> None:
    repair = {}
    if PROVENANCE_REPAIR_SUMMARY.is_file() and AUDIT_PATH.is_file():
        try:
            candidate = json.loads(
                PROVENANCE_REPAIR_SUMMARY.read_text(encoding="utf-8")
            )
            if (
                isinstance(candidate, dict)
                and candidate.get("historicalAuditSuperseded") is True
                and candidate.get("sourceAuditSha256")
                == hashlib.sha256(AUDIT_PATH.read_bytes()).hexdigest()
            ):
                repair = candidate
        except (OSError, json.JSONDecodeError):
            repair = {}
    receipt_count = sum(
        bool(record.get("cacheReceipt"))
        for record in audit.get("records", [])
        if isinstance(record, dict)
    )
    historical_only = bool(repair) and receipt_count == 0
    lines = [
        "---",
        'title: "Slide AI Vision Rescue Audit"',
        'category: "resources"',
        'sourceLabels: ["AI vision", "Slide OCR", "OCR audit"]',
        "---",
        "",
        "# Slide AI Vision Rescue Audit",
        "",
    ]
    if historical_only:
        lines.extend(
            [
                "## Current Trust Status",
                "The AI-vision cache and audit below are from a superseded historical run and are not trusted current evidence. That run recorded no current cache receipts, so the current RapidMerge policy accepts 0 of its AI-vision results.",
                "",
                f"- Historical unreceipted canonical updates affected: {int(repair.get('historicalUnreceiptedAiVisionUpdates', 0)):,}",
                f"- Canonical files restored from byte-exact pre-merge backups: {int(repair.get('restoredCanonicalFiles', 0)):,}",
                f"- Files already matching their pre-merge backups: {int(repair.get('alreadyMatchedBackupFiles', 0)):,}",
                f"- Current provenance receipts recorded by the historical run: {int(repair.get('historicalAiVisionAuditRecordedReceipts', 0)):,}",
                f"- Historical AI-vision results accepted by current RapidMerge policy: {int(repair.get('historicalAiVisionUpdatesAcceptedByCurrentPolicy', 0)):,}",
                "",
                "The cached text remains only as historical review material. It must not be reused or merged unless a new image-, prompt-, model-, policy-, and output-bound receipt passes the current validator.",
                "",
                "## Historical AI Vision Run (Superseded)",
            ]
        )
    else:
        lines.extend(
            [
                "## Latest Run",
                f"- Current validated cache receipts: {receipt_count:,}",
            ]
        )
    lines.extend(
        [
        f"- Provider: {audit.get('provider') or 'none available'}",
        f"- Model: {audit.get('model') or 'default'}",
        f"- Slides queued: {audit.get('slidesQueued', 0):,}",
        f"- Slides attempted: {audit.get('slidesAttempted', 0):,}",
        f"- Existing AI vision files reused: {audit.get('slidesSkippedExisting', 0):,}",
        f"- AI vision text files written: {audit.get('visionFilesWritten', 0):,}",
        f"- AI vision text files available: {audit.get('visionFilesAvailable', audit.get('visionFilesWritten', 0)):,}",
        "- Output directory: `raw/sources/slide-ocr-ai-vision/`",
        "",
        "## Notes",
        "- The historical counts above are retained for auditability; they do not represent accepted current OCR evidence." if historical_only else "- This step is intentionally after OCR. OCR creates candidates and identifies weak frames; vision interpretation reads the actual image only for low-confidence cases.",
        "- Free local vision is preferred through Ollama when available. Codex CLI uses `gpt-5.4-mini` by default through its existing login without reading `OPENAI_API_KEY`. OpenAI Responses API is used only when `OPENAI_API_KEY` is set and the provider is selected or auto-detected.",
        "- Current AI-vision text is eligible for comparison only when its cache receipt validates against the exact image bytes, OCR input, prompt, model, policy, and output. Unreceipted files are rejected.",
        "- A newly validated AI-vision candidate may be considered by `scripts/improve_slide_ocr_rapidmerge.py`; superseded cache entries are not eligible.",
        ]
    )
    write_text(AI_VISION_PAGE, "\n".join(lines))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--provider", choices=["auto", "ollama", "codex-cli", "openai"], default="auto")
    parser.add_argument("--ollama-model", default=os.environ.get("OLLAMA_VISION_MODEL", "llava:latest"))
    parser.add_argument("--codex-model", default=os.environ.get("CODEX_VISION_MODEL", DEFAULT_CODEX_VISION_MODEL))
    parser.add_argument("--openai-model", default=os.environ.get("OPENAI_VISION_MODEL", "gpt-5.5"))
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--min-confidence", type=float, default=0.72)
    parser.add_argument("--jobs", type=int, default=int(os.environ.get("CODEX_VISION_JOBS", "1")), help="Parallel slide reads. Keep low for Codex CLI provider.")
    parser.add_argument("--no-skip-existing", dest="skip_existing", action="store_false", help="Reread slides even when AI vision text already exists.")
    parser.set_defaults(skip_existing=True)
    parser.add_argument("--video-id", action="append", default=[])
    parser.add_argument("--slide", action="append", default=[], help="Slide image filename such as slide-001.jpg. Repeatable.")
    parser.add_argument("--ignore-rapidmerge-audit", action="store_true")
    parser.add_argument("--timeout", type=int, default=90)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    if args.jobs < 1 or args.jobs > MAX_JOBS:
        raise SystemExit(f"--jobs must be between 1 and {MAX_JOBS}")
    if not MIN_ACCEPTED_CONFIDENCE <= args.min_confidence <= 1:
        raise SystemExit(
            f"--min-confidence must be between {MIN_ACCEPTED_CONFIDENCE} and 1"
        )

    provider = None if args.dry_run else choose_provider(args.provider)
    slides = candidate_slides(args)
    if args.limit:
        slides = slides[: args.limit]
    audit = {
        "generatedBy": "scripts/interpret_slide_text_with_vision.py",
        "startedAtEpoch": time.time(),
        "provider": provider,
        "requestedProvider": args.provider,
        "model": {
            "ollama": args.ollama_model,
            "codex-cli": args.codex_model,
            "openai": args.openai_model,
        }.get(provider or ""),
        "slidesQueued": len(slides),
        "slidesAttempted": 0,
        "slidesSkippedExisting": 0,
        "visionFilesWritten": 0,
        "visionFilesAvailable": 0,
        "minConfidence": args.min_confidence,
        "jobs": max(1, args.jobs),
        "skipExisting": args.skip_existing,
        "records": [],
    }
    if args.dry_run:
        audit["status"] = "planned"
        audit["providerStatus"] = "dry-run"
        print(json.dumps({k: audit[k] for k in ["status", "provider", "slidesQueued", "slidesAttempted", "visionFilesWritten"]}, sort_keys=True))
        return 0
    if not provider:
        audit["status"] = "blocked"
        audit["providerStatus"] = "unavailable"
        AI_VISION_AUDIT.write_text(json.dumps(audit, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        write_audit_page(audit)
        print(json.dumps({k: audit[k] for k in ["status", "provider", "slidesQueued", "slidesAttempted", "visionFilesWritten"]}, sort_keys=True))
        return 2

    if args.jobs <= 1:
        records = [process_slide(provider, slide, args) for slide in slides]
    else:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as executor:
            records = list(executor.map(lambda slide: process_slide(provider, slide, args), slides))

    for record in records:
        if record.get("attempted"):
            audit["slidesAttempted"] += 1
        if record.get("skippedExisting"):
            audit["slidesSkippedExisting"] += 1
        if record.get("written") and not record.get("skippedExisting"):
            audit["visionFilesWritten"] += 1
        if record.get("written"):
            audit["visionFilesAvailable"] += 1
        audit["records"].append(record)

    audit["finishedAtEpoch"] = time.time()
    audit["elapsedSeconds"] = round(audit["finishedAtEpoch"] - audit["startedAtEpoch"], 2)
    audit["failures"] = sum(1 for record in records if record.get("error"))
    audit["status"] = "degraded" if audit["failures"] else "succeeded"
    AI_VISION_AUDIT.write_text(json.dumps(audit, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_audit_page(audit)
    print(json.dumps({k: audit[k] for k in ["status", "provider", "slidesQueued", "slidesAttempted", "visionFilesWritten", "failures"]}, sort_keys=True))
    return 1 if audit["failures"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
