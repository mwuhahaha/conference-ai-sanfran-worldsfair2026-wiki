#!/usr/bin/env python3
"""Reconstruct cleaner slide decks by cropping slide regions from captured video frames."""

from __future__ import annotations

import argparse
import json
import re
import tempfile
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

from markdown_blocks import blockquote

try:
    from rapidocr_onnxruntime import RapidOCR
except Exception:  # pragma: no cover - optional local dependency
    RapidOCR = None


ROOT = Path(__file__).resolve().parents[1]
STAGE_SLIDES = ROOT / "wiki" / "assets" / "slides"
RECON_ASSETS = ROOT / "wiki" / "assets" / "reconstructed-slides"
RECON_OCR = ROOT / "raw" / "sources" / "reconstructed-slide-ocr"
SLIDE_PAGES = ROOT / "wiki" / "slides"
AUDIT_PATH = ROOT / "raw" / "sources" / "reconstructed-slide-audit.json"


WORD_RE = re.compile(r"[A-Za-z][A-Za-z0-9'._/-]{2,}")


def load_json(path: Path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text())


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n")


def normalize_text(text: str) -> str:
    lines = []
    for line in str(text or "").replace("\r", "\n").splitlines():
        clean = re.sub(r"[ \t]+", " ", line).strip()
        if clean:
            lines.append(clean)
    return "\n".join(lines).strip()


def frontmatter(fields: dict) -> str:
    lines = ["---"]
    for key, value in fields.items():
        if isinstance(value, list):
            lines.append(f"{key}: [{', '.join(json.dumps(str(v), ensure_ascii=False) for v in value)}]")
        elif value is not None:
            lines.append(f"{key}: {json.dumps(str(value), ensure_ascii=False)}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def md_label(value: str) -> str:
    return str(value or "").replace("[", "(").replace("]", ")").replace("|", "/")


def words(text: str) -> list[str]:
    return WORD_RE.findall(text or "")


def average_hash(image: Image.Image, size: int = 8) -> int:
    gray = image.convert("L").resize((size, size))
    pixels = list(gray.getdata())
    avg = sum(pixels) / len(pixels)
    bits = 0
    for pixel in pixels:
        bits = (bits << 1) | int(pixel > avg)
    return bits


def hamming(left: int, right: int) -> int:
    return (left ^ right).bit_count()


def video_metadata_by_id() -> dict[str, dict]:
    videos: dict[str, dict] = {}
    rows = load_json(ROOT / "raw" / "sources" / "speaker-video-map.json", [])
    for row in rows:
        video = row.get("related_video") or {}
        video_id = video.get("video_id")
        if video_id:
            videos.setdefault(video_id, video)
    for source_path in [
        ROOT / "raw" / "sources" / "aidotengineer-channel-streams-latest.json",
        ROOT / "raw" / "sources" / "aidotengineer-channel-videos-latest.json",
    ]:
        payload = load_json(source_path, {})
        for entry in payload.get("entries", []):
            video_id = entry.get("id")
            if video_id:
                videos.setdefault(
                    video_id,
                    {
                        "video_id": video_id,
                        "youtube_title": entry.get("title") or video_id,
                        "youtube_url": entry.get("url") or f"https://www.youtube.com/watch?v={video_id}",
                    },
                )
    return videos


def frame_paths_for_video(video_id: str) -> list[Path]:
    source_dir = STAGE_SLIDES / video_id
    return sorted(source_dir.glob("*.jpg"))


def rectangularity_score(gray: np.ndarray, box: tuple[int, int, int, int]) -> float:
    x, y, w, h = box
    if w <= 0 or h <= 0:
        return 0.0
    area_ratio = (w * h) / float(gray.shape[0] * gray.shape[1])
    aspect = w / float(h)
    if area_ratio < 0.12 or aspect < 1.05 or aspect > 2.6:
        return 0.0
    crop = gray[y : y + h, x : x + w]
    if crop.size == 0:
        return 0.0
    edges = cv2.Canny(crop, 50, 150)
    edge_density = float(np.count_nonzero(edges)) / float(edges.size)
    contrast = float(np.std(crop))
    brightness = float(np.mean(crop))
    aspect_bonus = 1.0 - min(abs(aspect - 16 / 9), abs(aspect - 4 / 3), 1.0)
    return area_ratio * 120 + edge_density * 35 + min(contrast / 60, 1.0) * 20 + aspect_bonus * 25 + (10 if brightness > 80 else 0)


def candidate_boxes(image_bgr: np.ndarray) -> list[tuple[str, tuple[int, int, int, int], float]]:
    h, w = image_bgr.shape[:2]
    gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 40, 140)
    edges = cv2.dilate(edges, np.ones((5, 5), np.uint8), iterations=2)
    contours, _hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    boxes: list[tuple[str, tuple[int, int, int, int], float]] = []
    for contour in contours:
        x, y, bw, bh = cv2.boundingRect(contour)
        score = rectangularity_score(gray, (x, y, bw, bh))
        if score > 25:
            boxes.append(("contour", (x, y, bw, bh), score))

    # Fallback layout guesses for stage shots where screen borders are weak.
    fallbacks = [
        ("full", (0, 0, w, h)),
        ("left-55-top85", (0, 0, int(w * 0.55), int(h * 0.85))),
        ("left-65-top85", (0, 0, int(w * 0.65), int(h * 0.85))),
        ("left-72", (0, 0, int(w * 0.72), h)),
        ("right-55-top85", (int(w * 0.45), 0, int(w * 0.55), int(h * 0.85))),
        ("right-65-top85", (int(w * 0.35), 0, int(w * 0.65), int(h * 0.85))),
        ("right-72", (int(w * 0.28), 0, int(w * 0.72), h)),
        ("top-82", (0, 0, w, int(h * 0.82))),
    ]
    for name, box in fallbacks:
        boxes.append((name, box, rectangularity_score(gray, box)))
    return sorted(boxes, key=lambda item: item[2], reverse=True)


def crop_from_box(image_bgr: np.ndarray, box: tuple[int, int, int, int], frame_size: tuple[int, int]) -> Image.Image:
    frame_w, frame_h = frame_size
    x, y, bw, bh = box
    pad_x = int(frame_w * 0.01)
    pad_y = int(frame_h * 0.01)
    x = max(0, x - pad_x)
    y = max(0, y - pad_y)
    bw = min(frame_w - x, bw + 2 * pad_x)
    bh = min(frame_h - y, bh + 2 * pad_y)
    crop_bgr = image_bgr[y : y + bh, x : x + bw]
    crop_rgb = cv2.cvtColor(crop_bgr, cv2.COLOR_BGR2RGB)
    return Image.fromarray(crop_rgb)


def ocr_selection_candidates(
    candidates: list[tuple[str, tuple[int, int, int, int], float]],
    *,
    max_candidates: int,
) -> list[tuple[str, tuple[int, int, int, int], float]]:
    selected: list[tuple[str, tuple[int, int, int, int], float]] = []
    seen = set()
    preferred_names = {"left-55-top85", "left-65-top85", "right-55-top85", "right-65-top85", "full"}
    for item in candidates[:1] + [item for item in candidates if item[0] in preferred_names]:
        key = tuple(item[1])
        if key in seen:
            continue
        seen.add(key)
        selected.append(item)
        if len(selected) >= max_candidates:
            break
    return selected


def crop_slide_region(frame_path: Path, ocr=None, *, ocr_select: bool = True, ocr_select_candidates: int = 4) -> tuple[Image.Image, dict, str, float]:
    image_bgr = cv2.imread(str(frame_path))
    if image_bgr is None:
        raise RuntimeError(f"Could not read image: {frame_path}")
    h, w = image_bgr.shape[:2]
    candidates = candidate_boxes(image_bgr)
    ranked = ocr_selection_candidates(candidates, max_candidates=ocr_select_candidates)
    best = None
    if ocr is not None and ocr_select:
        for kind, box, score in ranked:
            crop = crop_from_box(image_bgr, box, (w, h))
            text, confidence = rapid_ocr_image(ocr, crop)
            word_count = len(words(text))
            ocr_score = word_count * max(confidence, 0.2) * 12 + min(len(text), 500) * 0.25
            # Penalize full-frame crops when a smaller crop has comparable OCR;
            # the smaller crop is usually closer to the actual projected slide.
            area = box[2] * box[3]
            area_ratio = area / float(w * h)
            compact_bonus = max(0.0, 1.0 - area_ratio) * 18
            total = ocr_score + compact_bonus + score * 0.2
            if best is None or total > best[0]:
                best = (total, kind, box, score, crop, text, confidence)
    if best is None:
        kind, box, score = candidates[0]
        crop = crop_from_box(image_bgr, box, (w, h))
        text, confidence = "", 0.0
    else:
        _total, kind, box, score, crop, text, confidence = best
    x, y, bw, bh = box
    return crop, {"source": frame_path.name, "kind": kind, "box": [x, y, bw, bh], "score": round(float(score), 2)}, text, confidence


def rapid_ocr_image(ocr, image: Image.Image) -> tuple[str, float]:
    if ocr is None:
        return "", 0.0
    with tempfile.TemporaryDirectory(prefix="reconstruct-ocr-") as tmp_dir:
        tmp = Path(tmp_dir) / "crop.png"
        image.save(tmp)
        result, _elapsed = ocr(str(tmp))
    if not result:
        return "", 0.0
    lines = []
    confs = []
    for item in result:
        text = normalize_text(item[1])
        try:
            conf = float(item[2])
        except Exception:
            conf = 0.0
        if conf >= 0.45 and any(ch.isalpha() for ch in text):
            lines.append(text)
            confs.append(conf)
    return normalize_text("\n".join(lines)), (sum(confs) / len(confs) if confs else 0.0)


def reconstruct_video(video_id: str, *, max_slides: int, use_ocr: bool, ocr_select: bool, ocr_select_candidates: int) -> dict:
    frames = frame_paths_for_video(video_id)
    out_dir = RECON_ASSETS / video_id
    ocr_dir = RECON_OCR / video_id
    out_dir.mkdir(parents=True, exist_ok=True)
    ocr_dir.mkdir(parents=True, exist_ok=True)
    for old in out_dir.glob("*.jpg"):
        old.unlink()
    for old in ocr_dir.glob("*.txt"):
        old.unlink()

    ocr = RapidOCR() if use_ocr and RapidOCR is not None else None
    selected: list[dict] = []
    hashes: list[int] = []
    for frame in frames:
        crop, meta, text, confidence = crop_slide_region(
            frame,
            ocr=ocr,
            ocr_select=ocr_select,
            ocr_select_candidates=ocr_select_candidates,
        )
        # Normalize output dimensions while preserving enough text detail.
        width, height = crop.size
        if max(width, height) < 1200:
            scale = 1200 / max(width, height)
            crop = crop.resize((int(width * scale), int(height * scale)), Image.Resampling.LANCZOS)
        ahash = average_hash(crop)
        if any(hamming(ahash, previous) <= 6 for previous in hashes[-16:]):
            continue
        if use_ocr and not text:
            text, confidence = rapid_ocr_image(ocr, crop)
        if len(selected) > 0 and text and selected[-1].get("ocr_text"):
            prev_words = set(words(selected[-1]["ocr_text"].lower()))
            now_words = set(words(text.lower()))
            if prev_words and now_words and len(prev_words & now_words) / max(len(prev_words | now_words), 1) > 0.86:
                continue
        output = out_dir / f"slide-{len(selected) + 1:03d}.jpg"
        crop.save(output, "JPEG", quality=90, optimize=True)
        if text:
            write(ocr_dir / f"{output.stem}.txt", text)
        hashes.append(ahash)
        selected.append({**meta, "output": output.name, "ocr_text": text, "ocr_confidence": round(confidence, 4)})
        if len(selected) >= max_slides:
            break
    return {"video_id": video_id, "frames": len(frames), "slides": selected}


def write_reconstructed_page(video_id: str, video: dict, result: dict) -> Path:
    page = SLIDE_PAGES / f"youtube-{video_id}-reconstructed-slides.md"
    title = f"Reconstructed Slides: {video.get('youtube_title') or video_id}"
    lines = [
        frontmatter(
            {
                "title": title,
                "category": "slides",
                "video_id": video_id,
                "sourceLabels": ["Cropped public YouTube video frames", "Local OpenCV slide-region detection", "Local RapidOCR"],
            }
        ),
        f"# {title}",
        "",
        "## Source Video",
        f"[{md_label(video.get('youtube_title') or video_id)}]({video.get('youtube_url') or f'https://www.youtube.com/watch?v={video_id}'})",
        "",
        "## Method",
        "This deck is reconstructed from the existing video frame captures by detecting likely slide regions with OpenCV, cropping/upscaling those regions, deduplicating similar crops, and OCRing the cropped slide images locally. It is a cleaner companion to the full-stage frame deck.",
        "",
        "## Reconstructed Slides",
    ]
    if not result["slides"]:
        lines.append("No reconstructed slide crops were selected.")
    for item in result["slides"]:
        image_path = f"assets/reconstructed-slides/{video_id}/{item['output']}"
        lines.append(f"![[{image_path}]]")
        lines.append("")
        lines.append(f"- Source frame: `{item['source']}`")
        lines.append(f"- Crop: `{item['kind']}` `{item['box']}` score `{item['score']}`")
        text = (item.get("ocr_text") or "").strip()
        if text:
            lines.extend(["", "OCR text:", "", blockquote(text), ""])
    write(page, "\n".join(lines))
    return page


def update_reconstructed_registry() -> None:
    rows = []
    for page in sorted(SLIDE_PAGES.glob("youtube-*-reconstructed-slides.md")):
        text = page.read_text()
        title_match = re.search(r'^title: "?(.*?)"?$', text, re.M)
        rows.append(
            {
                "id": page.stem,
                "title": title_match.group(1) if title_match else page.stem,
                "path": f"wiki/slides/{page.name}",
                "slide_count": len(re.findall(r"!\[\[assets/reconstructed-slides/", text)),
            }
        )
    write(SLIDE_PAGES / "reconstructed-registry.json", json.dumps(rows, indent=2, ensure_ascii=False))


def upsert_section(path: Path, heading: str, body: str) -> None:
    if not path.exists():
        return
    text = path.read_text()
    block = f"\n## {heading}\n{body.rstrip()}\n"
    pattern = re.compile(rf"\n## {re.escape(heading)}\n.*?(?=\n## |\Z)", re.S)
    if pattern.search(text):
        text = pattern.sub(block, text)
    else:
        text = text.rstrip() + block
    write(path, text)


def update_original_slide_page(video_id: str) -> None:
    original = SLIDE_PAGES / f"youtube-{video_id}-slides.md"
    upsert_section(original, "Reconstructed Slide Deck", f"- [[youtube-{video_id}-reconstructed-slides]]")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--video-id", action="append", default=[])
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--max-slides", type=int, default=80)
    parser.add_argument("--no-ocr", action="store_true")
    parser.add_argument("--no-ocr-select", action="store_true", help="Use geometric crop scoring only.")
    parser.add_argument("--ocr-select-candidates", type=int, default=4)
    args = parser.parse_args()

    videos = video_metadata_by_id()
    ids = args.video_id or sorted(path.name for path in STAGE_SLIDES.iterdir() if path.is_dir())
    if args.limit:
        ids = ids[: args.limit]

    audit = []
    for index, video_id in enumerate(ids, start=1):
        print(f"[{index}/{len(ids)}] reconstructing {video_id}", flush=True)
        result = reconstruct_video(
            video_id,
            max_slides=args.max_slides,
            use_ocr=not args.no_ocr,
            ocr_select=not args.no_ocr_select,
            ocr_select_candidates=args.ocr_select_candidates,
        )
        write_reconstructed_page(video_id, videos.get(video_id, {"video_id": video_id}), result)
        update_original_slide_page(video_id)
        audit.append(result)
        print(f"  selected {len(result['slides'])} reconstructed slides from {result['frames']} frames", flush=True)

    update_reconstructed_registry()
    write(AUDIT_PATH, json.dumps({"videoCount": len(audit), "videos": audit}, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
