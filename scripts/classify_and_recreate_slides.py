#!/usr/bin/env python3
"""Classify slide frames with low-cost vision and create text/layout recreations."""

from __future__ import annotations

import argparse
import base64
import hashlib
import html
import importlib.util
import json
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

try:
    from markdown_blocks import blockquote
except ModuleNotFoundError:  # Imported as scripts.classify_and_recreate_slides.
    from scripts.markdown_blocks import blockquote

try:
    from slide_codex_safety import CODEX_NO_TOOL_ARGS, UNTRUSTED_MEDIA_PREAMBLE
except ModuleNotFoundError:  # Imported as scripts.classify_and_recreate_slides.
    from scripts.slide_codex_safety import CODEX_NO_TOOL_ARGS, UNTRUSTED_MEDIA_PREAMBLE


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
SLIDE_PAGES = WIKI / "slides"
CLASSIFICATION_ROOT = ROOT / "raw" / "sources" / "slide-ai-classification"
RECREATION_ASSETS = WIKI / "assets" / "slide-recreations"
DEFAULT_CODEX_MODEL = os.environ.get("CODEX_SLIDE_CLASSIFIER_MODEL", "gpt-5.4-mini")
POLICY_VERSION = "agent-triage-ocr-reconcile-v5"
CACHE_SCHEMA_VERSION = 2
PUBLICATION_SCHEMA_VERSION = 1
MIN_CLASSIFICATION_CONFIDENCE = 0.72
PUBLICATION_PENDING_MARKER = "<!-- slide-ai-classifier-publication-pending -->"

JSON_RE = re.compile(r"\{.*\}", re.S)

PROMPT = UNTRUSTED_MEDIA_PREAMBLE + """Inspect the attached conference video frame.

Return only compact JSON with this shape:
{
  "is_content_slide": true,
  "confidence": 0.0,
  "frame_type": "content_slide|title_card|sponsor_logo|speaker_stage|demo_video|blank|other",
  "reject_reason": "",
  "text": "only simple directly readable slide text, or empty string",
  "text_status": "meaningful|none|illegible|decorative|non_slide",
  "ocr_ready": false,
  "ocr_reason": "",
  "direct_read_ready": false,
  "text_density": "none|low|medium|high",
  "layout": {
    "background": "short CSS color or gradient description",
    "style": "minimal|dark|light|code|diagram|product",
    "blocks": [
      {"role":"title|subtitle|body|code|caption|logo|diagram_label","text":"exact visible text","x":8,"y":8,"w":84,"h":12}
    ]
  }
}

Keep only frames that are clearly actual presentation slides with meaningful content:
- Keep text-heavy slides, diagrams, code slides, architecture slides, tables, and product/UI screenshots when they are being used as slide content.
- Reject people standing on stage, sponsor/logo walls, "starting soon", speaker intro cards, blank frames, camera shots of an audience, and demo/video footage that is not a readable slide.
- This is a triage pass first. Do not spend effort transcribing dense slides.
- Do not invent text and do not translate text. Preserve exact visible language only.
- Set direct_read_ready true only for simple slides where the title/main bullets are large and easy to read visually.
- If direct_read_ready is true, extract only the visible title and main bullets into text.
- Set ocr_ready true when the frame is a content slide with dense, small, tabular, code, multi-column, or otherwise OCR-suitable text that a local OCR engine is likely to read more accurately or more cheaply than vision transcription.
- Set ocr_ready false for title cards, decorative/logo-only frames, speaker/stage shots, low-text diagram slides, illegible/cropped frames, screenshots where text is not the main evidence, or any non-slide frame.
- If ocr_ready is true, leave text as "" unless there is a very short obvious title. Do not transcribe the dense body text in this pass.
- If the frame has no meaningful slide text, set text to "" and text_status to "none", "decorative", "illegible", or "non_slide".
- For a diagram with little text, preserve visible labels exactly. Describe visual structure only in layout block text when it is needed to recreate the slide, not as transcript/OCR text.
- Coordinates are percentages from 0 to 100 and should approximate the recreated slide layout.
"""

BATCH_PROMPT = UNTRUSTED_MEDIA_PREAMBLE + """Inspect the attached conference video frames.

Return only compact JSON with this shape:
{
  "slides": [
    {
      "image_index": 1,
      "filename": "slide-001.jpg",
      "is_content_slide": true,
      "confidence": 0.0,
      "frame_type": "content_slide|title_card|sponsor_logo|speaker_stage|demo_video|blank|other",
      "reject_reason": "",
      "text": "only simple directly readable slide text, or empty string",
      "text_status": "meaningful|none|illegible|decorative|non_slide",
      "ocr_ready": false,
      "ocr_reason": "",
      "direct_read_ready": false,
      "text_density": "none|low|medium|high",
      "layout": {
        "background": "short CSS color or gradient description",
        "style": "minimal|dark|light|code|diagram|product",
        "blocks": [
          {"role":"title|subtitle|body|code|caption|logo|diagram_label","text":"exact visible text","x":8,"y":8,"w":84,"h":12}
        ]
      }
    }
  ]
}

Classify every attached frame exactly once. The image order is listed below.

Keep only frames that are clearly actual presentation slides with meaningful content:
- Keep text-heavy slides, diagrams, code slides, architecture slides, tables, and product/UI screenshots when they are being used as slide content.
- Reject people standing on stage, sponsor/logo walls, "starting soon", speaker intro cards, blank frames, camera shots of an audience, and demo/video footage that is not a readable slide.
- This is a triage pass first. Do not spend effort transcribing dense slides.
- Do not invent text and do not translate text. Preserve exact visible language only.
- Set direct_read_ready true only for simple slides where the title/main bullets are large and easy to read visually.
- If direct_read_ready is true, extract only the visible title and main bullets into text.
- Set ocr_ready true when the frame is a content slide with dense, small, tabular, code, multi-column, or otherwise OCR-suitable text that a local OCR engine is likely to read more accurately or more cheaply than vision transcription.
- Set ocr_ready false for title cards, decorative/logo-only frames, speaker/stage shots, low-text diagram slides, illegible/cropped frames, screenshots where text is not the main evidence, or any non-slide frame.
- If ocr_ready is true, leave text as "" unless there is a very short obvious title. Do not transcribe the dense body text in this pass.
- If the frame has no meaningful slide text, set text to "" and text_status to "none", "decorative", "illegible", or "non_slide".
- For a diagram with little text, preserve visible labels exactly. Describe visual structure only in layout block text when it is needed to recreate the slide, not as transcript/OCR text.
- Coordinates are percentages from 0 to 100 and should approximate the recreated slide layout.

Image order:
"""

RECONCILE_PROMPT = UNTRUSTED_MEDIA_PREAMBLE + """Inspect the attached slide image and the OCR candidate below.

Return only compact JSON with this shape:
{
  "text": "corrected meaningful slide text with line breaks, or empty string",
  "text_status": "meaningful|none|illegible|decorative|non_slide",
  "corrections": "short note about whether OCR was accepted or corrected"
}

Use the image as authority. Correct obvious OCR errors only when the image clearly supports the correction. Do not invent missing text and do not translate.

OCR candidate:
"""

PROMPT_CONTRACT_SHA256 = hashlib.sha256(
    f"{POLICY_VERSION}\n{PROMPT}\n{BATCH_PROMPT}\n{RECONCILE_PROMPT}".encode("utf-8")
).hexdigest()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore").strip() if path.exists() else ""


def _text_bytes(text: str) -> bytes:
    return (text.rstrip() + "\n").encode("utf-8")


def _fsync_directory(path: Path) -> None:
    try:
        descriptor = os.open(path, os.O_RDONLY)
    except OSError:
        return
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _stage_bytes(path: Path, data: bytes) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
    )
    temporary_path = Path(temporary)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
    except BaseException:
        temporary_path.unlink(missing_ok=True)
        raise
    return temporary_path


def atomic_write_bytes(path: Path, data: bytes) -> None:
    temporary_path = _stage_bytes(path, data)
    try:
        os.replace(temporary_path, path)
        _fsync_directory(path.parent)
    finally:
        temporary_path.unlink(missing_ok=True)


def write_text(path: Path, text: str) -> None:
    atomic_write_bytes(path, _text_bytes(text))


def encode_image(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("utf-8")


def parse_json(text: str) -> dict:
    match = JSON_RE.search(text or "")
    payload = match.group(0) if match else text
    try:
        data = json.loads(payload)
    except Exception as exc:
        raise ValueError(f"slide classifier returned malformed JSON: {(text or '')[:180]}") from exc
    if not isinstance(data, dict):
        raise ValueError("slide classifier returned malformed JSON: expected an object")
    layout = data.get("layout") if isinstance(data.get("layout"), dict) else {}
    blocks = layout.get("blocks") if isinstance(layout.get("blocks"), list) else []
    normalized_blocks = []
    for block in blocks[:24]:
        if not isinstance(block, dict):
            continue
        normalized_blocks.append(
            {
                "role": str(block.get("role") or "body")[:40],
                "text": str(block.get("text") or "").strip(),
                "x": clamp_number(block.get("x"), 0, 100, 8),
                "y": clamp_number(block.get("y"), 0, 100, 8),
                "w": clamp_number(block.get("w"), 1, 100, 84),
                "h": clamp_number(block.get("h"), 1, 100, 12),
            }
        )
    confidence = parse_probability(data.get("confidence"))
    return {
        "is_content_slide": parse_boolean(data.get("is_content_slide"), "is_content_slide"),
        "confidence": confidence,
        "frame_type": str(data.get("frame_type") or "other"),
        "reject_reason": str(data.get("reject_reason") or "").strip(),
        "text": str(data.get("text") or "").strip(),
        "text_status": str(data.get("text_status") or ("meaningful" if data.get("text") else "none"))[:40],
        "ocr_ready": parse_boolean(data.get("ocr_ready"), "ocr_ready"),
        "ocr_reason": str(data.get("ocr_reason") or "").strip()[:240],
        "direct_read_ready": parse_boolean(
            data.get("direct_read_ready"), "direct_read_ready"
        ),
        "text_density": str(data.get("text_density") or "none")[:40],
        "layout": {
            "background": str(layout.get("background") or "#ffffff")[:160],
            "style": str(layout.get("style") or "light")[:40],
            "blocks": normalized_blocks,
        },
    }


def parse_batch_json(text: str) -> list[dict]:
    match = JSON_RE.search(text or "")
    payload = match.group(0) if match else text
    try:
        data = json.loads(payload)
    except Exception as exc:
        raise ValueError("slide batch classifier returned malformed JSON") from exc
    slides = data.get("slides") if isinstance(data, dict) else data
    if not isinstance(slides, list):
        raise ValueError("slide batch classifier returned no slides array")
    return [parse_json(json.dumps(item, ensure_ascii=False)) | {
        "image_index": item.get("image_index") if isinstance(item, dict) else None,
        "filename": str(item.get("filename") or "").strip() if isinstance(item, dict) else "",
    } for item in slides if isinstance(item, dict)]


def clamp_number(value, lower: float, upper: float, fallback: float) -> float:
    try:
        number = float(value)
    except Exception:
        return fallback
    if not math.isfinite(number):
        return fallback
    return max(lower, min(upper, number))


def parse_boolean(value, name: str) -> bool:
    if type(value) is not bool:
        raise ValueError(f"slide classifier returned non-boolean {name}")
    return value


def parse_probability(value) -> float:
    if type(value) not in {int, float}:
        raise ValueError("slide classifier returned non-numeric confidence")
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError("slide classifier returned non-numeric confidence") from exc
    if not math.isfinite(number) or not 0 <= number <= 1:
        raise ValueError("slide classifier returned confidence outside 0..1")
    return number


def validate_min_confidence(value: float) -> float:
    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not math.isfinite(float(value))
        or not MIN_CLASSIFICATION_CONFIDENCE <= float(value) <= 1
    ):
        raise ValueError(
            f"min confidence must be between {MIN_CLASSIFICATION_CONFIDENCE} and 1"
        )
    return float(value)


def codex_cli(image: Path, model: str, timeout: int) -> dict:
    command = shutil.which("codex")
    if not command:
        raise RuntimeError("codex CLI is not available on PATH")
    out_dir = ROOT / ".ops" / "state" / "cache" / "codex-slide-classifier"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"{image.parent.name}-{image.stem}-{int(time.time() * 1000)}.json"
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
        "-m",
        model,
        PROMPT,
    ]
    env = os.environ.copy()
    env.pop("OPENAI_API_KEY", None)
    cp = subprocess.run(cmd, cwd=out_dir, text=True, capture_output=True, timeout=timeout, env=env)
    if cp.returncode != 0:
        raise RuntimeError((cp.stderr or cp.stdout)[-1200:])
    if not out_file.exists():
        raise RuntimeError("codex CLI did not write output")
    return parse_json(read_text(out_file))


def codex_cli_reconcile(image: Path, ocr_text: str, model: str, timeout: int) -> dict:
    command = shutil.which("codex")
    if not command:
        raise RuntimeError("codex CLI is not available on PATH")
    out_dir = ROOT / ".ops" / "state" / "cache" / "codex-slide-classifier"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"reconcile-{image.parent.name}-{image.stem}-{int(time.time() * 1000)}.json"
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
        "-m",
        model,
        RECONCILE_PROMPT + (ocr_text or "(none)"),
    ]
    env = os.environ.copy()
    env.pop("OPENAI_API_KEY", None)
    cp = subprocess.run(cmd, cwd=out_dir, text=True, capture_output=True, timeout=timeout, env=env)
    if cp.returncode != 0:
        raise RuntimeError((cp.stderr or cp.stdout)[-1200:])
    if not out_file.exists():
        raise RuntimeError("codex CLI did not write output")
    try:
        data = json.loads(JSON_RE.search(read_text(out_file)).group(0))
    except Exception:
        return {"text": ocr_text, "text_status": "meaningful" if ocr_text else "illegible", "corrections": "reconcile response unparseable; used OCR candidate"}
    return {
        "text": str(data.get("text") or "").strip(),
        "text_status": str(data.get("text_status") or ("meaningful" if data.get("text") else "illegible"))[:40],
        "corrections": str(data.get("corrections") or "").strip()[:500],
    }


def codex_cli_batch(images: list[Path], model: str, timeout: int) -> list[dict]:
    command = shutil.which("codex")
    if not command:
        raise RuntimeError("codex CLI is not available on PATH")
    out_dir = ROOT / ".ops" / "state" / "cache" / "codex-slide-classifier"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"batch-{images[0].parent.name}-{images[0].stem}-{int(time.time() * 1000)}.json"
    image_args = []
    for image in images:
        image_args.extend(["-i", str(image)])
    hints = []
    for index, image in enumerate(images, 1):
        hints.append(f"{index}. {image.name}")
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
        *image_args,
        "-o",
        str(out_file),
        "-m",
        model,
        BATCH_PROMPT + "\n\n".join(hints),
    ]
    env = os.environ.copy()
    env.pop("OPENAI_API_KEY", None)
    cp = subprocess.run(cmd, cwd=out_dir, text=True, capture_output=True, timeout=timeout, env=env)
    if cp.returncode != 0:
        raise RuntimeError((cp.stderr or cp.stdout)[-1200:])
    if not out_file.exists():
        raise RuntimeError("codex CLI did not write output")
    return parse_batch_json(read_text(out_file))


def load_advanced_ocr_module():
    path = ROOT / "scripts" / "improve_slide_ocr_rapidmerge.py"
    spec = importlib.util.spec_from_file_location("slide_rapidmerge", path)
    if spec is None or spec.loader is None:
        return None
    module = importlib.util.module_from_spec(spec)
    try:
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
    except Exception:
        return None
    return module


def advanced_ocr_text(slide: Path, args: argparse.Namespace) -> tuple[str, str, dict]:
    if args.no_advanced_ocr:
        return "", "", {"status": "disabled"}
    module = load_advanced_ocr_module()
    if module is None:
        return "", "", {"status": "unavailable"}
    engines = module.requested_engines(args.ocr_engine or ["rapidocr"])
    ready = []
    status: dict[str, str] = {}
    for engine in engines:
        if not engine.available():
            status[engine.name] = "unavailable"
            continue
        try:
            status[engine.name] = engine.init()
            ready.append(engine)
        except Exception as exc:
            status[engine.name] = f"init-error: {exc!r}"
    if not ready:
        return "", "", {"status": status}
    candidates, errors = module.engine_candidates(
        ready,
        slide,
        variants=not args.no_ocr_variants,
        deep=args.deep_ocr,
    )
    if not candidates:
        return "", "", {"status": status, "errors": errors}
    best = max(candidates, key=lambda candidate: candidate.score)
    min_score = args.ocr_min_score
    weak = False
    try:
        weak = bool(module.is_weak(best.text))
    except Exception:
        weak = False
    alpha = sum(ch.isalpha() for ch in best.text)
    suspicious = sum(1 for ch in best.text if not (ch.isalnum() or ch.isspace() or ch in ".,;:!?()[]{}<>/\\-_'\"@#$%&+=*|"))
    suspicious_ratio = suspicious / max(len(best.text), 1)
    if weak or suspicious_ratio > args.ocr_max_suspicious_ratio or (len(best.text) > 240 and alpha / max(len(best.text), 1) < 0.45):
        return "", "", {
            "status": status,
            "errors": errors,
            "best_source": best.source,
            "best_score": round(best.score, 2),
            "rejected_as_weak": True,
            "suspicious_ratio": round(suspicious_ratio, 4),
        }
    if best.score < min_score:
        return "", "", {"status": status, "errors": errors, "best_source": best.source, "best_score": round(best.score, 2)}
    return best.text, best.source, {"status": status, "errors": errors, "best_score": round(best.score, 2)}


DECKS = {
    "slides": {
        "asset_dir": WIKI / "assets" / "slides",
        "ocr_dir": ROOT / "raw" / "sources" / "slide-ocr",
        "page_suffix": "slides",
        "visible_heading": "Extracted Slides",
    },
    "dense": {
        "asset_dir": WIKI / "assets" / "dense-slides",
        "ocr_dir": ROOT / "raw" / "sources" / "dense-slide-ocr",
        "page_suffix": "dense-slides",
        "visible_heading": "Cropped Visible Slides",
    },
    "reconstructed": {
        "asset_dir": WIKI / "assets" / "reconstructed-slides",
        "ocr_dir": ROOT / "raw" / "sources" / "reconstructed-slide-ocr",
        "page_suffix": "reconstructed-slides",
        "visible_heading": "Reconstructed Slides",
    },
}


def deck_config(args: argparse.Namespace) -> dict:
    return DECKS[args.deck_kind]


def slide_images(video_id: str, args: argparse.Namespace) -> list[Path]:
    assets = deck_config(args)["asset_dir"]
    if args.slide:
        found: list[Path] = []
        for name in args.slide:
            path = assets / video_id / name
            if path.exists():
                found.append(path)
        return found[: args.limit or None]
    slides = sorted((assets / video_id).glob("*.jpg"))
    return slides[: args.limit or None]


def ocr_path(video_id: str, slide: Path, args: argparse.Namespace) -> Path:
    return deck_config(args)["ocr_dir"] / video_id / f"{slide.stem}.txt"


def classification_path(video_id: str, slide: Path, args: argparse.Namespace) -> Path:
    return CLASSIFICATION_ROOT / args.deck_kind / video_id / f"{slide.stem}.json"


def recreation_path(video_id: str, slide: Path, args: argparse.Namespace) -> Path:
    return RECREATION_ASSETS / args.deck_kind / video_id / f"{slide.stem}.html"


def css_background(value: str) -> str:
    value = value.strip() or "#fff"
    if re.match(r"^#[0-9a-fA-F]{3,8}$", value):
        return value
    if value.lower() in {"white", "black", "transparent"}:
        return value.lower()
    if "dark" in value.lower():
        return "#10141f"
    return "#ffffff"


def render_recreation(video_id: str, slide: Path, result: dict, args: argparse.Namespace) -> str:
    layout = result.get("layout") or {}
    style = str(layout.get("style") or "light").lower()
    dark = style in {"dark", "code"} or "dark" in str(layout.get("background") or "").lower()
    bg = css_background(str(layout.get("background") or ""))
    fg = "#f8fafc" if dark else "#111827"
    muted = "#cbd5e1" if dark else "#475569"
    blocks_html = []
    for block in layout.get("blocks") or []:
        text = str(block.get("text") or "").strip()
        if not text:
            continue
        role = str(block.get("role") or "body")
        size = "clamp(20px, 3.4vw, 44px)" if role == "title" else "clamp(13px, 1.6vw, 22px)"
        weight = "800" if role in {"title", "subtitle"} else "520"
        family = "ui-monospace, SFMono-Regular, Menlo, monospace" if role == "code" else "Inter, ui-sans-serif, system-ui, sans-serif"
        blocks_html.append(
            '<div class="block" style="'
            f"left:{float(block.get('x', 8)):.2f}%;top:{float(block.get('y', 8)):.2f}%;"
            f"width:{float(block.get('w', 84)):.2f}%;min-height:{float(block.get('h', 12)):.2f}%;"
            f"font-size:{size};font-weight:{weight};font-family:{family};"
            f'">{html.escape(text).replace(chr(10), "<br>")}</div>'
        )
    if not blocks_html and result.get("text"):
        blocks_html.append(f'<div class="fallback">{html.escape(result["text"]).replace(chr(10), "<br>")}</div>')
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Slide recreation {html.escape(args.deck_kind)} {html.escape(video_id)} {html.escape(slide.stem)}</title>
  <style>
    html, body {{ margin: 0; background: #f1f5f9; }}
    .slide {{
      position: relative;
      width: min(100vw, 1200px);
      aspect-ratio: 16 / 9;
      margin: 0 auto;
      overflow: hidden;
      background: {html.escape(bg)};
      color: {fg};
      box-sizing: border-box;
      border: 1px solid rgba(15, 23, 42, 0.16);
    }}
    .block {{ position: absolute; box-sizing: border-box; line-height: 1.16; letter-spacing: 0; white-space: pre-wrap; }}
    .fallback {{ position: absolute; inset: 8%; color: {fg}; font: 600 clamp(16px, 2.5vw, 32px)/1.2 Inter, ui-sans-serif, system-ui, sans-serif; white-space: pre-wrap; }}
    .meta {{ position: absolute; left: 3%; bottom: 3%; color: {muted}; font: 500 12px/1.2 Inter, ui-sans-serif, system-ui, sans-serif; }}
  </style>
</head>
<body>
  <main class="slide">
    {''.join(blocks_html)}
    <div class="meta">AI text/layout recreation from video frame; verify against source image.</div>
  </main>
</body>
</html>
"""


def updated_section_text(text: str, heading: str, body: str) -> str:
    text = re.sub(r"\n## Removed Non-Slide Frames\n.*?(?=\n## |\Z)", "\n", text, flags=re.S)
    text = re.sub(r"\n## Hidden Non-Slide Evidence\n.*?(?=\n## |\Z)", "\n", text, flags=re.S)
    if heading != "Extracted Slides":
        text = re.sub(r"\n## Extracted Slides\n.*?(?=\n## |\Z)", "\n", text, flags=re.S)
    block = f"\n## {heading}\n{body.rstrip()}\n"
    pattern = re.compile(rf"\n## {re.escape(heading)}\n.*?(?=\n## |\Z)", re.S)
    if pattern.search(text):
        text = pattern.sub(lambda _m: block, text)
    else:
        text = text.rstrip() + block
    return text.rstrip() + "\n"


def upsert_section(path: Path, heading: str, body: str) -> None:
    write_text(
        path,
        updated_section_text(path.read_text(encoding="utf-8"), heading, body),
    )


def rendered_page(
    video_id: str,
    accepted: list[dict],
    rejected: list[dict],
    args: argparse.Namespace,
) -> tuple[Path, str] | None:
    suffix = deck_config(args)["page_suffix"]
    page = SLIDE_PAGES / f"youtube-{video_id}-{suffix}.md"
    if not page.exists():
        return None
    lines = []
    if not accepted:
        lines.append("No slide-like frames are visible after AI slide classification. Rejected frames remain stored as evidence and are listed below.")
    for item in accepted:
        slide = Path(item["image"])
        if not slide.is_absolute():
            slide = ROOT / slide
        rel = slide.relative_to(WIKI)
        lines.append(f"![[{rel.as_posix()}]]")
        lines.append("")
        recreation = Path(item["recreation"])
        if not recreation.is_absolute():
            recreation = ROOT / recreation
        recreate_rel = recreation.relative_to(WIKI).as_posix()
        lines.append(f"- Recreated text/layout view: [open HTML recreation](/{recreate_rel})")
        lines.append(f"- AI slide classifier: `{item['frame_type']}` confidence `{item['confidence']}`")
        if item.get("text_source"):
            source = item["text_source"]
            if source in {"advanced_ocr", "advanced_ocr_reconciled"}:
                source = f"advanced OCR `{item.get('ocr_source') or 'unknown'}`"
                if item.get("text_source") == "advanced_ocr_reconciled":
                    source += " reconciled by agent"
            lines.append(f"- Text source: {source}.")
        if item.get("ocr_ready"):
            reason = item.get("ocr_reason") or "agent marked this slide as OCR-ready"
            lines.append(f"- OCR decision: ready — {reason}")
        text = item.get("text") or ""
        text_status = item.get("text_status") or ("meaningful" if text else "none")
        if text and text_status == "meaningful":
            lines.extend(["", "Slide text:", "", blockquote(text), ""])
        elif text_status and text_status != "meaningful":
            lines.append(f"- Slide text: not surfaced (`{text_status}` by AI classifier).")
    if rejected:
        lines.extend(["", "### Hidden Non-Slide Evidence"])
        for item in rejected:
            slide = Path(item["image"])
            if not slide.is_absolute():
                slide = ROOT / slide
            rel = slide.relative_to(WIKI).as_posix()
            lines.append(
                f"- [`{slide.name}`](/{rel}) — `{item['frame_type']}` confidence `{item['confidence']}`; "
                f"{item.get('reject_reason') or 'not a content slide'}"
            )
    lines.extend(["", f"Classification audit: `raw/sources/slide-ai-classification/{args.deck_kind}/{video_id}/audit.json`"])
    return (
        page,
        updated_section_text(
            page.read_text(encoding="utf-8"),
            deck_config(args)["visible_heading"],
            "\n".join(lines),
        ),
    )


def refresh_page(video_id: str, accepted: list[dict], rejected: list[dict], args: argparse.Namespace) -> None:
    rendered = rendered_page(video_id, accepted, rejected, args)
    if rendered is not None:
        page, text = rendered
        write_text(page, text)


def pending_page_text(page: Path, args: argparse.Namespace) -> str | None:
    text = page.read_text(encoding="utf-8")
    markers = (
        "Classification audit:",
        "/assets/slide-recreations/",
        "AI slide classifier:",
    )
    if not any(marker in text for marker in markers):
        return None
    body = (
        f"{PUBLICATION_PENDING_MARKER}\n"
        "> **Classifier-derived view withheld.** A replacement publication is "
        "in progress or did not finish. Original captured slide/frame files "
        "remain the source evidence.\n"
    )
    return updated_section_text(text, deck_config(args)["visible_heading"], body)


def _manifest_sha256(manifest: list[dict[str, object]]) -> str:
    return hashlib.sha256(
        json.dumps(manifest, separators=(",", ":"), sort_keys=True).encode("utf-8")
    ).hexdigest()


def _project_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def bind_recreation_output(record: dict, path: Path, data: bytes) -> None:
    record.update(
        {
            "recreation": _project_path(path),
            "recreation_sha256": hashlib.sha256(data).hexdigest(),
            "recreation_size_bytes": len(data),
        }
    )


def recreation_manifest(accepted: list[dict]) -> list[dict[str, object]]:
    manifest = [
        {
            "path": str(
                Path(record["recreation"]).relative_to(ROOT)
                if Path(record["recreation"]).is_absolute()
                else Path(record["recreation"])
            ),
            "sha256": record["recreation_sha256"],
            "size_bytes": record["recreation_size_bytes"],
        }
        for record in accepted
    ]
    return sorted(manifest, key=lambda item: str(item["path"]))


def validate_recreation_publication(
    audit: dict,
    outputs: list[tuple[Path, bytes]],
    *,
    read_published: bool = False,
) -> None:
    if (
        audit.get("publication_schema_version") != PUBLICATION_SCHEMA_VERSION
        or audit.get("publication_status") != "succeeded"
    ):
        raise RuntimeError("classification publication envelope is incomplete")
    manifest = audit.get("recreation_manifest")
    if not isinstance(manifest, list) or audit.get(
        "recreation_manifest_sha256"
    ) != _manifest_sha256(manifest):
        raise RuntimeError("classification recreation manifest is not digest-bound")
    accepted = audit.get("accepted")
    if not isinstance(accepted, list) or recreation_manifest(accepted) != manifest:
        raise RuntimeError(
            "classification accepted records do not match recreation manifest"
        )
    output_by_path = {str(path.relative_to(ROOT)): data for path, data in outputs}
    if len(output_by_path) != len(outputs):
        raise RuntimeError("classification recreation output paths are not unique")
    expected = {
        str(item.get("path")): (
            item.get("sha256"),
            item.get("size_bytes"),
        )
        for item in manifest
        if isinstance(item, dict)
    }
    if set(expected) != set(output_by_path):
        raise RuntimeError("classification recreation output set does not match audit")
    for relative, data in output_by_path.items():
        path = ROOT / relative
        actual = path.read_bytes() if read_published else data
        digest, size = expected[relative]
        if hashlib.sha256(actual).hexdigest() != digest or len(actual) != size:
            raise RuntimeError(
                f"classification recreation output digest mismatch: {relative}"
            )


def publish_classification(
    video_id: str,
    audit: dict,
    outputs: list[tuple[Path, bytes]],
    args: argparse.Namespace,
    final_page: tuple[Path, str] | None,
) -> None:
    """Publish one classifier result with the page as the final visibility gate."""

    validate_recreation_publication(audit, outputs)
    live_directory = RECREATION_ASSETS / args.deck_kind / video_id
    live_parent = live_directory.parent
    live_parent.mkdir(parents=True, exist_ok=True)
    staged_directory = Path(
        tempfile.mkdtemp(prefix=f".{video_id}.publication-", dir=live_parent)
    )
    audit_path = CLASSIFICATION_ROOT / args.deck_kind / video_id / "audit.json"
    audit_bytes = _text_bytes(
        json.dumps(audit, indent=2, ensure_ascii=False, sort_keys=True)
    )
    audit_temporary: Path | None = None
    pending_temporary: Path | None = None
    final_page_temporary: Path | None = None
    backup_directory: Path | None = None
    old_audit = audit_path.read_bytes() if audit_path.is_file() else None
    page_path = final_page[0] if final_page else (
        SLIDE_PAGES / f"youtube-{video_id}-{deck_config(args)['page_suffix']}.md"
    )
    committed = False
    try:
        for output_path, data in outputs:
            if output_path.parent != live_directory:
                raise RuntimeError("classification recreation escaped publication directory")
            staged_path = staged_directory / output_path.name
            staged_path.write_bytes(data)
            with staged_path.open("rb") as handle:
                os.fsync(handle.fileno())
        _fsync_directory(staged_directory)
        validate_recreation_publication(audit, outputs)
        audit_temporary = _stage_bytes(audit_path, audit_bytes)
        if page_path.is_file():
            pending = pending_page_text(page_path, args)
            if pending is not None:
                pending_temporary = _stage_bytes(page_path, _text_bytes(pending))
        if final_page is not None:
            final_page_temporary = _stage_bytes(
                final_page[0], _text_bytes(final_page[1])
            )

        if pending_temporary is not None:
            os.replace(pending_temporary, page_path)
            pending_temporary = None
            _fsync_directory(page_path.parent)

        os.replace(audit_temporary, audit_path)
        audit_temporary = None
        _fsync_directory(audit_path.parent)

        if live_directory.exists():
            backup_directory = Path(
                tempfile.mkdtemp(prefix=f".{video_id}.previous-", dir=live_parent)
            )
            backup_directory.rmdir()
            os.replace(live_directory, backup_directory)
            _fsync_directory(live_parent)
        os.replace(staged_directory, live_directory)
        _fsync_directory(live_parent)

        published_audit = json.loads(audit_path.read_text(encoding="utf-8"))
        validate_recreation_publication(
            published_audit, outputs, read_published=True
        )
        if final_page_temporary is not None:
            os.replace(final_page_temporary, final_page[0])
            final_page_temporary = None
            _fsync_directory(final_page[0].parent)
        committed = True
    except BaseException:
        if not staged_directory.exists() and live_directory.exists():
            shutil.rmtree(live_directory, ignore_errors=True)
        if backup_directory is not None and backup_directory.exists():
            os.replace(backup_directory, live_directory)
            backup_directory = None
            _fsync_directory(live_parent)
        if old_audit is None:
            audit_path.unlink(missing_ok=True)
            _fsync_directory(audit_path.parent)
        else:
            atomic_write_bytes(audit_path, old_audit)
        raise
    finally:
        if not committed and staged_directory.exists():
            shutil.rmtree(staged_directory, ignore_errors=True)
        for temporary_path in (
            audit_temporary,
            pending_temporary,
            final_page_temporary,
        ):
            if temporary_path is not None:
                temporary_path.unlink(missing_ok=True)
    if backup_directory is not None:
        shutil.rmtree(backup_directory, ignore_errors=True)


def _cache_policy(args: argparse.Namespace) -> dict[str, object]:
    return {
        "model": str(args.model),
        "deck_kind": str(args.deck_kind),
        "advanced_ocr": not bool(getattr(args, "no_advanced_ocr", False)),
        "ocr_reconcile": not bool(getattr(args, "no_ocr_reconcile", False)),
        "ocr_engines": list(getattr(args, "ocr_engine", []) or ["rapidocr"]),
        "ocr_min_score": float(getattr(args, "ocr_min_score", 120.0)),
        "ocr_max_suspicious_ratio": float(
            getattr(args, "ocr_max_suspicious_ratio", 0.08)
        ),
        "ocr_variants": not bool(getattr(args, "no_ocr_variants", False)),
        "deep_ocr": bool(getattr(args, "deep_ocr", False)),
    }


def bind_cache_provenance(
    result: dict, slide: Path, args: argparse.Namespace
) -> dict:
    result.update(
        {
            "cache_schema_version": CACHE_SCHEMA_VERSION,
            "cache_status": "succeeded",
            "policy_version": POLICY_VERSION,
            "prompt_contract_sha256": PROMPT_CONTRACT_SHA256,
            "image_sha256": hashlib.sha256(slide.read_bytes()).hexdigest(),
            "cache_policy": _cache_policy(args),
            "model": str(args.model),
            "deck_kind": str(args.deck_kind),
        }
    )
    return result


def cached_result(
    path: Path, slide: Path, args: argparse.Namespace
) -> dict | None:
    if not path.exists():
        return None
    try:
        data = json.loads(read_text(path))
        confidence = float(data.get("confidence"))
    except (OSError, TypeError, ValueError, json.JSONDecodeError):
        return None
    if (
        data.get("cache_schema_version") != CACHE_SCHEMA_VERSION
        or data.get("cache_status") != "succeeded"
        or data.get("policy_version") != POLICY_VERSION
        or data.get("prompt_contract_sha256") != PROMPT_CONTRACT_SHA256
        or data.get("image_sha256") != hashlib.sha256(slide.read_bytes()).hexdigest()
        or data.get("cache_policy") != _cache_policy(args)
        or not isinstance(data.get("is_content_slide"), bool)
        or not math.isfinite(confidence)
        or not 0 <= confidence <= 1
    ):
        return None
    return data


def resolve_batch_results(
    slides: list[Path], results: list[dict]
) -> list[tuple[Path, dict]]:
    """Bind each batch response to exactly one requested image."""

    def result_index(result: dict) -> int | None:
        value = result.get("image_index")
        if isinstance(value, int) and not isinstance(value, bool):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
        return None

    unused = set(range(len(results)))
    resolved: list[tuple[Path, dict]] = []
    for expected_index, slide in enumerate(slides, 1):
        filename_matches = [
            index
            for index in unused
            if str(results[index].get("filename") or "") == slide.name
        ]
        index_matches = [
            index
            for index in unused
            if result_index(results[index]) == expected_index
        ]
        matches = filename_matches or index_matches
        if len(matches) != 1:
            raise RuntimeError(
                f"slide batch classifier did not uniquely identify {slide.name}"
            )
        selected_row = matches[0]
        result = results[selected_row]
        filename = str(result.get("filename") or "")
        image_index = result_index(result)
        if filename and filename != slide.name:
            raise RuntimeError(
                f"slide batch classifier filename mismatch for {slide.name}: {filename}"
            )
        if image_index is not None and image_index != expected_index:
            raise RuntimeError(
                f"slide batch classifier index mismatch for {slide.name}: {image_index}"
            )
        unused.remove(selected_row)
        resolved.append((slide, result))
    if unused:
        raise RuntimeError("slide batch classifier returned unbound extra results")
    return resolved


def apply_agent_first_ocr(slide: Path, result: dict, args: argparse.Namespace) -> dict:
    result["policy_version"] = POLICY_VERSION
    result.setdefault("text_source", "agent_vision" if result.get("text") else "none")
    result.setdefault("vision_text", result.get("text") or "")
    result.setdefault("advanced_ocr", {})
    if not result.get("is_content_slide") or not result.get("ocr_ready"):
        return result
    ocr_text, source, meta = advanced_ocr_text(slide, args)
    result["advanced_ocr"] = {"source": source, "text": ocr_text, **meta}
    if ocr_text:
        reconciled = codex_cli_reconcile(slide, ocr_text, args.model, args.reconcile_timeout) if not args.no_ocr_reconcile else {
            "text": ocr_text,
            "text_status": "meaningful",
            "corrections": "reconcile disabled",
        }
        result["vision_text"] = result.get("text") or ""
        result["text"] = reconciled.get("text") or ocr_text
        result["text_status"] = reconciled.get("text_status") or "meaningful"
        result["text_source"] = "advanced_ocr_reconciled" if not args.no_ocr_reconcile else "advanced_ocr"
        result["ocr_source"] = source
        result["ocr_reconcile"] = reconciled
    else:
        result["text_source"] = "agent_vision" if result.get("text") else "none"
    return result


def classify_video(video_id: str, args: argparse.Namespace) -> dict:
    accepted: list[dict] = []
    rejected: list[dict] = []
    recreation_outputs: list[tuple[Path, bytes]] = []
    slides = slide_images(video_id, args)
    if not slides:
        raise ValueError(
            f"no {args.deck_kind} images found for requested video {video_id}"
        )
    args.min_confidence = validate_min_confidence(args.min_confidence)
    missing = [
        slide
        for slide in slides
        if not (
            args.reuse
            and cached_result(
                classification_path(video_id, slide, args), slide, args
            )
        )
    ]
    if args.batch_size > 1:
        for start in range(0, len(missing), args.batch_size):
            chunk = missing[start : start + args.batch_size]
            if not chunk:
                continue
            results = codex_cli_batch(chunk, args.model, args.timeout)
            for slide, result in resolve_batch_results(chunk, results):
                result["image"] = str(slide.relative_to(ROOT))
                result["deck_kind"] = args.deck_kind
                result["model"] = args.model
                result["classified_at_epoch"] = time.time()
                result = apply_agent_first_ocr(slide, result, args)
                bind_cache_provenance(result, slide, args)
                write_text(classification_path(video_id, slide, args), json.dumps(result, indent=2, ensure_ascii=False))
    for slide in slides:
        cached = classification_path(video_id, slide, args)
        result = cached_result(cached, slide, args) if args.reuse else None
        if result is not None:
            pass
        else:
            result = codex_cli(slide, args.model, args.timeout)
            result["image"] = str(slide.relative_to(ROOT))
            result["deck_kind"] = args.deck_kind
            result["model"] = args.model
            result["classified_at_epoch"] = time.time()
            result = apply_agent_first_ocr(slide, result, args)
            bind_cache_provenance(result, slide, args)
            write_text(cached, json.dumps(result, indent=2, ensure_ascii=False))
        keep = bool(result.get("is_content_slide")) and float(result.get("confidence") or 0) >= args.min_confidence
        record = {
            **result,
            "image": _project_path(slide),
            "confidence": round(float(result.get("confidence") or 0), 4),
            "frame_type": result.get("frame_type") or "other",
        }
        if keep:
            recreation = recreation_path(video_id, slide, args)
            recreation_data = _text_bytes(
                render_recreation(video_id, slide, result, args)
            )
            bind_recreation_output(record, recreation, recreation_data)
            recreation_outputs.append((recreation, recreation_data))
            accepted.append(record)
        else:
            rejected.append(record)
    input_manifest = [
        {
            "filename": slide.name,
            "sha256": hashlib.sha256(slide.read_bytes()).hexdigest(),
        }
        for slide in slides
    ]
    input_manifest_sha256 = hashlib.sha256(
        json.dumps(
            input_manifest, separators=(",", ":"), sort_keys=True
        ).encode("utf-8")
    ).hexdigest()
    audit = {
        "status": "succeeded",
        "cache_schema_version": CACHE_SCHEMA_VERSION,
        "video_id": video_id,
        "deck_kind": args.deck_kind,
        "model": args.model,
        "policy_version": POLICY_VERSION,
        "prompt_contract_sha256": PROMPT_CONTRACT_SHA256,
        "cache_policy": _cache_policy(args),
        "input_manifest": input_manifest,
        "input_manifest_sha256": input_manifest_sha256,
        "min_confidence": args.min_confidence,
        "ocr_policy": {
            "agent_first": True,
            "advanced_ocr_only_when_agent_marks_ocr_ready": True,
            "agent_reconciles_advanced_ocr": not args.no_ocr_reconcile,
            "default_model": DEFAULT_CODEX_MODEL,
            "model": args.model,
            "ocr_engines": args.ocr_engine or ["rapidocr"],
            "ocr_min_score": args.ocr_min_score,
            "ocr_variants": not args.no_ocr_variants,
            "deep_ocr": args.deep_ocr,
        },
        "hide_rejected": args.hide_rejected,
        "evidence_retained": True,
        "accepted_count": len(accepted),
        "rejected_count": len(rejected),
        "accepted": accepted,
        "rejected": rejected,
    }
    audit["publication_schema_version"] = PUBLICATION_SCHEMA_VERSION
    audit["publication_status"] = "succeeded"
    audit["recreation_manifest"] = recreation_manifest(accepted)
    audit["recreation_manifest_sha256"] = _manifest_sha256(
        audit["recreation_manifest"]
    )
    final_page = (
        rendered_page(video_id, accepted, rejected, args)
        if not args.no_refresh_page
        else None
    )
    publish_classification(
        video_id,
        audit,
        recreation_outputs,
        args,
        final_page,
    )
    return audit


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--video-id", action="append", required=True)
    parser.add_argument("--deck-kind", choices=sorted(DECKS), default="slides")
    parser.add_argument("--slide", action="append", default=[], help="Specific slide filename such as slide-001.jpg. Repeatable.")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--model", default=DEFAULT_CODEX_MODEL)
    parser.add_argument("--min-confidence", type=float, default=0.72)
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--batch-size", type=int, default=8, help="Classify missing slides in multi-image batches. Use 1 for legacy per-slide calls.")
    parser.add_argument("--ocr-engine", action="append", default=[], help="Advanced OCR engine used only when the agent marks a slide OCR-ready. Repeatable: rapidocr, paddleocr, easyocr, doctr.")
    parser.add_argument("--ocr-min-score", type=float, default=120.0, help="Minimum advanced OCR candidate score before replacing agent vision text.")
    parser.add_argument("--ocr-max-suspicious-ratio", type=float, default=0.08, help="Reject advanced OCR when unusual character ratio is above this threshold.")
    parser.add_argument("--reconcile-timeout", type=int, default=90, help="Timeout for agent reconciliation of OCR output.")
    parser.add_argument("--no-advanced-ocr", action="store_true", help="Disable the OCR-ready second pass.")
    parser.add_argument("--no-ocr-reconcile", action="store_true", help="Do not ask the agent to reconcile advanced OCR output against the image.")
    parser.add_argument("--no-ocr-variants", action="store_true", help="Do not create crop/contrast variants for advanced OCR.")
    parser.add_argument("--deep-ocr", action="store_true", help="Use more aggressive OCR image variants when the agent marks a slide OCR-ready.")
    parser.add_argument("--reuse", action="store_true", help="Reuse existing classification JSON.")
    parser.add_argument("--no-refresh-page", action="store_true", help="Write audit/recreations without changing the wiki deck page.")
    parser.add_argument("--refresh-partial-page", action="store_true", help="Allow --limit/--slide runs to rewrite the visible wiki page.")
    parser.add_argument("--hide-rejected", action="store_true", help="Hide rejected frames from the visible wiki slide sequence while retaining evidence files.")
    parser.add_argument("--remove-rejected", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args()
    try:
        args.min_confidence = validate_min_confidence(args.min_confidence)
    except ValueError as exc:
        parser.error(str(exc))
    if args.remove_rejected:
        args.hide_rejected = True
    if (args.limit or args.slide) and not args.refresh_partial_page:
        args.no_refresh_page = True

    summaries = []
    for video_id in args.video_id:
        summaries.append(classify_video(video_id, args))
    print(
        json.dumps(
            {
                "videos": len(summaries),
                "accepted": sum(item["accepted_count"] for item in summaries),
                "rejected": sum(item["rejected_count"] for item in summaries),
                "model": args.model,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
