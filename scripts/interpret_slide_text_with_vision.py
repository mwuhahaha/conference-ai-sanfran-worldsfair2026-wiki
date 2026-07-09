#!/usr/bin/env python3
"""Use a vision model to rescue slide text when OCR confidence is low."""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import shutil
import subprocess
import time
from pathlib import Path

import requests

from improve_slide_ocr_rapidmerge import AUDIT_PATH, Candidate, is_weak, text_path, write_text


ROOT = Path(__file__).resolve().parents[1]
SLIDE_ASSETS = ROOT / "wiki" / "assets" / "slides"
CANONICAL_OCR = ROOT / "raw" / "sources" / "slide-ocr"
AI_VISION_OCR = ROOT / "raw" / "sources" / "slide-ocr-ai-vision"
AI_VISION_AUDIT = ROOT / "raw" / "sources" / "slide-ocr-ai-vision-audit.json"
AI_VISION_PAGE = ROOT / "wiki" / "resources" / "slide-ocr-ai-vision-audit.md"

JSON_RE = re.compile(r"\{.*\}", re.S)


PROMPT = """Read the visible text on this conference slide or video frame.

Return only JSON with this shape:
{"text":"line 1\\nline 2","confidence":0.0,"notes":"brief reason"}

Rules:
- Preserve exact visible wording, capitalization, punctuation, product names, and dates.
- Put each distinct visual line on its own newline.
- Do not infer hidden text.
- If the frame is mostly a person/stage/photo with no useful slide text, return an empty text string and low confidence.
- If existing OCR is close but has obvious character errors, correct it from the image.

Existing OCR to compare:
"""


def encode_image(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("utf-8")


def parse_json(text: str) -> dict:
    match = JSON_RE.search(text or "")
    payload = match.group(0) if match else text
    try:
        data = json.loads(payload)
    except Exception:
        return {"text": "", "confidence": 0.0, "notes": f"unparseable response: {text[:180]}"}
    return {
        "text": str(data.get("text") or "").strip(),
        "confidence": float(data.get("confidence") or 0),
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
    prompt = (
        "Inspect only the attached image. Return only compact JSON with keys text, confidence, notes. "
        "text must be the exact visible slide/frame text with line breaks. Prefer meaningful slide text "
        "over background sponsor-wall fragments. If no useful visible text, use empty string. Do not use tools.\n\n"
        "Existing OCR to compare:\n"
        + (ocr_text or "(none)")
    )
    cmd = [
        command,
        "exec",
        "--ephemeral",
        "-s",
        "read-only",
        "-C",
        str(ROOT),
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
        cwd=ROOT,
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


def write_audit_page(audit: dict) -> None:
    lines = [
        "---",
        'title: "Slide AI Vision Rescue Audit"',
        'category: "resources"',
        'sourceLabels: ["AI vision", "Slide OCR", "OCR audit"]',
        "---",
        "",
        "# Slide AI Vision Rescue Audit",
        "",
        "## Latest Run",
        f"- Provider: {audit.get('provider') or 'none available'}",
        f"- Slides queued: {audit.get('slidesQueued', 0):,}",
        f"- Slides attempted: {audit.get('slidesAttempted', 0):,}",
        f"- AI vision text files written: {audit.get('visionFilesWritten', 0):,}",
        f"- Minimum confidence: {audit.get('minConfidence')}",
        "- Output directory: `raw/sources/slide-ocr-ai-vision/`",
        "",
        "## Notes",
        "- This step is intentionally after OCR. OCR creates candidates and identifies weak frames; vision interpretation reads the actual image only for low-confidence cases.",
        "- Free local vision is preferred through Ollama when available. Codex CLI can be used through its existing login without reading `OPENAI_API_KEY`. OpenAI Responses API is used only when `OPENAI_API_KEY` is set and the provider is selected or auto-detected.",
        "- Generated text is merged by `scripts/improve_slide_ocr_rapidmerge.py` as `ai-vision`, below operator-verified text but above raw OCR.",
    ]
    write_text(AI_VISION_PAGE, "\n".join(lines))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--provider", choices=["auto", "ollama", "codex-cli", "openai"], default="auto")
    parser.add_argument("--ollama-model", default=os.environ.get("OLLAMA_VISION_MODEL", "llava:latest"))
    parser.add_argument("--codex-model", default=os.environ.get("CODEX_VISION_MODEL", ""))
    parser.add_argument("--openai-model", default=os.environ.get("OPENAI_VISION_MODEL", "gpt-5.5"))
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--min-confidence", type=float, default=0.72)
    parser.add_argument("--video-id", action="append", default=[])
    parser.add_argument("--slide", action="append", default=[], help="Slide image filename such as slide-001.jpg. Repeatable.")
    parser.add_argument("--ignore-rapidmerge-audit", action="store_true")
    parser.add_argument("--timeout", type=int, default=90)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    provider = choose_provider(args.provider)
    slides = candidate_slides(args)
    if args.limit:
        slides = slides[: args.limit]
    audit = {
        "generatedBy": "scripts/interpret_slide_text_with_vision.py",
        "startedAtEpoch": time.time(),
        "provider": provider,
        "requestedProvider": args.provider,
        "slidesQueued": len(slides),
        "slidesAttempted": 0,
        "visionFilesWritten": 0,
        "minConfidence": args.min_confidence,
        "records": [],
    }
    if not provider or args.dry_run:
        audit["providerStatus"] = "dry-run" if args.dry_run else "unavailable"
        AI_VISION_AUDIT.write_text(json.dumps(audit, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        write_audit_page(audit)
        print(json.dumps({k: audit[k] for k in ["provider", "slidesQueued", "slidesAttempted", "visionFilesWritten"]}, sort_keys=True))
        return 0

    for slide in slides:
        ocr_text = current_ocr(slide)
        record = {"image": str(slide.relative_to(ROOT)), "oldPreview": ocr_text[:220]}
        try:
            result = interpret(provider, slide, ocr_text, args)
        except Exception as exc:
            record["error"] = repr(exc)
            audit["records"].append(record)
            continue
        audit["slidesAttempted"] += 1
        record.update(result)
        if result["text"] and result["confidence"] >= args.min_confidence:
            out = text_path(AI_VISION_OCR, slide)
            write_text(out, result["text"])
            record["written"] = str(out.relative_to(ROOT))
            audit["visionFilesWritten"] += 1
        audit["records"].append(record)

    audit["finishedAtEpoch"] = time.time()
    audit["elapsedSeconds"] = round(audit["finishedAtEpoch"] - audit["startedAtEpoch"], 2)
    AI_VISION_AUDIT.write_text(json.dumps(audit, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_audit_page(audit)
    print(json.dumps({k: audit[k] for k in ["provider", "slidesQueued", "slidesAttempted", "visionFilesWritten"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
