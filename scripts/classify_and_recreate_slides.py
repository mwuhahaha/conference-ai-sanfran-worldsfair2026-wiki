#!/usr/bin/env python3
"""Classify slide frames with low-cost vision and create text/layout recreations."""

from __future__ import annotations

import argparse
import base64
import html
import json
import os
import re
import shutil
import subprocess
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
SLIDE_PAGES = WIKI / "slides"
CLASSIFICATION_ROOT = ROOT / "raw" / "sources" / "slide-ai-classification"
RECREATION_ASSETS = WIKI / "assets" / "slide-recreations"
DEFAULT_CODEX_MODEL = os.environ.get("CODEX_SLIDE_CLASSIFIER_MODEL", "gpt-5.4-mini")

JSON_RE = re.compile(r"\{.*\}", re.S)

PROMPT = """Inspect the attached conference video frame.

Return only compact JSON with this shape:
{
  "is_content_slide": true,
  "confidence": 0.0,
  "frame_type": "content_slide|title_card|sponsor_logo|speaker_stage|demo_video|blank|other",
  "reject_reason": "",
  "text": "visible slide text with line breaks",
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
- Do not invent text. Use only visible text. For a diagram with little text, preserve visible labels and describe the visual structure briefly in block text.
- Coordinates are percentages from 0 to 100 and should approximate the recreated slide layout.

Existing OCR:
"""


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore").strip() if path.exists() else ""


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def encode_image(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("utf-8")


def parse_json(text: str) -> dict:
    match = JSON_RE.search(text or "")
    payload = match.group(0) if match else text
    try:
        data = json.loads(payload)
    except Exception:
        return {
            "is_content_slide": False,
            "confidence": 0.0,
            "frame_type": "other",
            "reject_reason": f"unparseable response: {(text or '')[:180]}",
            "text": "",
            "layout": {"background": "#ffffff", "style": "light", "blocks": []},
        }
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
    return {
        "is_content_slide": bool(data.get("is_content_slide")),
        "confidence": float(data.get("confidence") or 0),
        "frame_type": str(data.get("frame_type") or "other"),
        "reject_reason": str(data.get("reject_reason") or "").strip(),
        "text": str(data.get("text") or "").strip(),
        "layout": {
            "background": str(layout.get("background") or "#ffffff")[:160],
            "style": str(layout.get("style") or "light")[:40],
            "blocks": normalized_blocks,
        },
    }


def clamp_number(value, lower: float, upper: float, fallback: float) -> float:
    try:
        number = float(value)
    except Exception:
        return fallback
    return max(lower, min(upper, number))


def codex_cli(image: Path, ocr_text: str, model: str, timeout: int) -> dict:
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
        "-s",
        "read-only",
        "-C",
        str(ROOT),
        "-i",
        str(image),
        "-o",
        str(out_file),
        "-m",
        model,
        PROMPT + (ocr_text or "(none)"),
    ]
    env = os.environ.copy()
    env.pop("OPENAI_API_KEY", None)
    cp = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, timeout=timeout, env=env)
    if cp.returncode != 0:
        raise RuntimeError((cp.stderr or cp.stdout)[-1200:])
    if not out_file.exists():
        raise RuntimeError("codex CLI did not write output")
    return parse_json(read_text(out_file))


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


def upsert_section(path: Path, heading: str, body: str) -> None:
    text = path.read_text(encoding="utf-8")
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
    write_text(path, text)


def refresh_page(video_id: str, accepted: list[dict], rejected: list[dict], args: argparse.Namespace) -> None:
    suffix = deck_config(args)["page_suffix"]
    page = SLIDE_PAGES / f"youtube-{video_id}-{suffix}.md"
    if not page.exists():
        return
    lines = []
    if not accepted:
        lines.append("No slide-like frames are visible after AI slide classification. Rejected frames remain stored as evidence and are listed below.")
    for item in accepted:
        slide = Path(item["image"])
        rel = slide.relative_to(WIKI)
        lines.append(f"![[{rel.as_posix()}]]")
        lines.append("")
        recreate_rel = Path(item["recreation"]).relative_to(WIKI).as_posix()
        lines.append(f"- Recreated text/layout view: [open HTML recreation](/{recreate_rel})")
        lines.append(f"- AI slide classifier: `{item['frame_type']}` confidence `{item['confidence']}`")
        text = item.get("text") or read_text(ocr_path(video_id, slide, args))
        if text:
            lines.extend(["", "Slide text:", "", "> " + text.strip().replace("\n", "\n> "), ""])
    if rejected:
        lines.extend(["", "### Hidden Non-Slide Evidence"])
        for item in rejected:
            slide = Path(item["image"])
            rel = slide.relative_to(WIKI).as_posix()
            lines.append(
                f"- [`{slide.name}`](/{rel}) — `{item['frame_type']}` confidence `{item['confidence']}`; "
                f"{item.get('reject_reason') or 'not a content slide'}"
            )
    lines.extend(["", f"Classification audit: `raw/sources/slide-ai-classification/{args.deck_kind}/{video_id}/audit.json`"])
    upsert_section(page, deck_config(args)["visible_heading"], "\n".join(lines))


def classify_video(video_id: str, args: argparse.Namespace) -> dict:
    accepted: list[dict] = []
    rejected: list[dict] = []
    for slide in slide_images(video_id, args):
        cached = classification_path(video_id, slide, args)
        if args.reuse and cached.exists():
            result = json.loads(read_text(cached))
        else:
            result = codex_cli(slide, read_text(ocr_path(video_id, slide, args)), args.model, args.timeout)
            result["image"] = str(slide.relative_to(ROOT))
            result["deck_kind"] = args.deck_kind
            result["model"] = args.model
            result["classified_at_epoch"] = time.time()
            write_text(cached, json.dumps(result, indent=2, ensure_ascii=False))
        keep = bool(result.get("is_content_slide")) and float(result.get("confidence") or 0) >= args.min_confidence
        record = {
            **result,
            "image": str(slide),
            "confidence": round(float(result.get("confidence") or 0), 4),
            "frame_type": result.get("frame_type") or "other",
        }
        if keep:
            recreation = recreation_path(video_id, slide, args)
            write_text(recreation, render_recreation(video_id, slide, result, args))
            record["recreation"] = str(recreation)
            accepted.append(record)
        else:
            rejected.append(record)
    if not args.no_refresh_page:
        refresh_page(video_id, accepted, rejected, args)
    audit = {
        "video_id": video_id,
        "deck_kind": args.deck_kind,
        "model": args.model,
        "min_confidence": args.min_confidence,
        "hide_rejected": args.hide_rejected,
        "evidence_retained": True,
        "accepted_count": len(accepted),
        "rejected_count": len(rejected),
        "accepted": accepted,
        "rejected": rejected,
    }
    write_text(CLASSIFICATION_ROOT / args.deck_kind / video_id / "audit.json", json.dumps(audit, indent=2, ensure_ascii=False))
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
    parser.add_argument("--reuse", action="store_true", help="Reuse existing classification JSON.")
    parser.add_argument("--no-refresh-page", action="store_true", help="Write audit/recreations without changing the wiki deck page.")
    parser.add_argument("--refresh-partial-page", action="store_true", help="Allow --limit/--slide runs to rewrite the visible wiki page.")
    parser.add_argument("--hide-rejected", action="store_true", help="Hide rejected frames from the visible wiki slide sequence while retaining evidence files.")
    parser.add_argument("--remove-rejected", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args()
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
