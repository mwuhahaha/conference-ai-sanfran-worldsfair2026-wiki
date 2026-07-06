#!/usr/bin/env python3
"""Reread weak slide OCR with crop/enhancement variants and confidence scoring."""

from __future__ import annotations

import argparse
import csv
import io
import json
import os
import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

from PIL import Image, ImageChops, ImageEnhance, ImageFilter, ImageOps, ImageStat


ROOT = Path(__file__).resolve().parents[1]
SLIDE_ASSETS = ROOT / "wiki" / "assets" / "slides"
SLIDE_OCR = ROOT / "raw" / "sources" / "slide-ocr"
IMPROVED_OCR = ROOT / "raw" / "sources" / "slide-ocr-improved"
AUDIT_PATH = ROOT / "raw" / "sources" / "slide-ocr-quality-audit.json"


WORD_RE = re.compile(r"[A-Za-z][A-Za-z0-9'._/-]{2,}")


@dataclass
class OcrResult:
    text: str
    mean_conf: float
    word_count: int
    char_count: int
    variant: str
    crop_box: tuple[int, int, int, int] | None

    @property
    def score(self) -> float:
        # Balance text volume with OCR confidence. Tiny one-word results should
        # not beat a more complete moderate-confidence reading.
        return (self.mean_conf * min(self.word_count, 80)) + min(self.char_count, 1200) * 0.12


def run_ocr(cmd: list[str], *, timeout: int = 8) -> subprocess.CompletedProcess:
    env = os.environ.copy()
    local_root = ROOT / ".local" / "ocr" / "root"
    if (local_root / "usr" / "bin" / "tesseract").exists():
        lib_path = str(local_root / "usr" / "lib" / "x86_64-linux-gnu")
        env["LD_LIBRARY_PATH"] = lib_path + (":" + env["LD_LIBRARY_PATH"] if env.get("LD_LIBRARY_PATH") else "")
        env["TESSDATA_PREFIX"] = str(local_root / "usr" / "share" / "tesseract-ocr" / "4.00" / "tessdata")
    return subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, timeout=timeout, env=env)


def resolve_tesseract() -> str:
    local = ROOT / ".local" / "ocr" / "root" / "usr" / "bin" / "tesseract"
    if local.exists():
        return str(local)
    found = shutil.which("tesseract")
    if not found:
        raise SystemExit("tesseract not found")
    return found


def words(text: str) -> list[str]:
    return WORD_RE.findall(text)


def normalize_text(text: str) -> str:
    lines = []
    for line in text.replace("\r", "\n").splitlines():
        clean = re.sub(r"[ \t]+", " ", line).strip()
        if clean:
            lines.append(clean)
    return "\n".join(lines).strip()


def current_text_for(slide: Path) -> str:
    path = SLIDE_OCR / slide.parent.name / f"{slide.stem}.txt"
    if not path.exists():
        return ""
    return normalize_text(path.read_text(errors="ignore"))


def is_weak(text: str) -> bool:
    found = words(text)
    alpha = sum(ch.isalpha() for ch in text)
    if not text.strip():
        return True
    if len(found) < 8:
        return True
    if len(text) < 80 and len(found) < 12:
        return True
    if alpha < 35 and len(found) < 10:
        return True
    return False


def edge_trim_box(image: Image.Image) -> tuple[int, int, int, int]:
    # Remove black letterbox/pillarbox borders while preserving full-stage frames.
    gray = image.convert("L")
    bg = Image.new("L", gray.size, 0)
    diff = ImageChops.difference(gray, bg)
    diff = diff.point(lambda p: 255 if p > 12 else 0)
    bbox = diff.getbbox()
    if not bbox:
        return (0, 0, image.width, image.height)
    left, top, right, bottom = bbox
    if (right - left) < image.width * 0.5 or (bottom - top) < image.height * 0.5:
        return (0, 0, image.width, image.height)
    return (left, top, right, bottom)


def bright_content_box(image: Image.Image) -> tuple[int, int, int, int] | None:
    # Many captures include a bright projected slide surrounded by dark stage.
    # Find the dominant bright text/screen region and pad it for OCR.
    small = ImageOps.autocontrast(image.convert("L")).resize((240, 135))
    threshold = small.point(lambda p: 255 if p > 155 else 0)
    bbox = threshold.getbbox()
    if not bbox:
        return None
    sx = image.width / small.width
    sy = image.height / small.height
    left, top, right, bottom = [int(v * (sx if i % 2 == 0 else sy)) for i, v in enumerate(bbox)]
    pad_x = int(image.width * 0.025)
    pad_y = int(image.height * 0.035)
    left = max(0, left - pad_x)
    top = max(0, top - pad_y)
    right = min(image.width, right + pad_x)
    bottom = min(image.height, bottom + pad_y)
    if (right - left) < image.width * 0.25 or (bottom - top) < image.height * 0.2:
        return None
    return (left, top, right, bottom)


def candidate_crops(image: Image.Image) -> list[tuple[str, Image.Image, tuple[int, int, int, int] | None]]:
    bright = bright_content_box(image)
    if bright:
        return [("bright-region", image.crop(bright), bright)]
    # Common stage layout: projected slides on one side, speaker on the other.
    w, h = image.size
    left = (0, 0, int(w * 0.72), h)
    right = (int(w * 0.28), 0, w, h)
    candidates = [("left-70", left), ("right-70", right), ("full", (0, 0, w, h))]
    scored = []
    for name, box in candidates:
        crop = image.crop(box).convert("L").resize((120, 68))
        autocontrast = ImageOps.autocontrast(crop)
        bright_pixels = sum(1 for p in autocontrast.getdata() if p > 165)
        stat = ImageStat.Stat(autocontrast)
        scored.append((bright_pixels * max(stat.stddev[0], 1), name, box))
    _score, name, box = max(scored)
    return [(name, image.crop(box), None if name == "full" else box)]


def enhance_variants(image: Image.Image) -> list[tuple[str, Image.Image]]:
    gray = image.convert("L")
    scale = max(2, 1800 // max(1, max(gray.size)))
    if scale > 4:
        scale = 4
    enlarged = gray.resize((gray.width * scale, gray.height * scale), Image.Resampling.LANCZOS)
    autocontrast = ImageOps.autocontrast(enlarged)
    contrast = ImageEnhance.Contrast(autocontrast).enhance(1.8).filter(ImageFilter.SHARPEN)
    threshold_light = contrast.point(lambda p: 255 if p > 165 else 0)
    return [
        ("contrast-sharpen", contrast),
    ]


def parse_tsv(tsv_text: str) -> tuple[str, float]:
    reader = csv.DictReader(io.StringIO(tsv_text), delimiter="\t")
    rows = []
    confs = []
    for row in reader:
        token = (row.get("text") or "").strip()
        if not token:
            continue
        rows.append(row)
        try:
            conf = float(row.get("conf") or -1)
        except ValueError:
            conf = -1
        if conf >= 0:
            confs.append(conf)
    by_line: dict[tuple[str, str, str], list[str]] = {}
    for row in rows:
        key = (row.get("block_num") or "", row.get("par_num") or "", row.get("line_num") or "")
        by_line.setdefault(key, []).append(row.get("text") or "")
    text = "\n".join(" ".join(tokens).strip() for tokens in by_line.values() if any(tokens))
    mean_conf = sum(confs) / len(confs) if confs else 0.0
    return normalize_text(text), mean_conf


def tesseract_text(tesseract: str, image: Image.Image, name: str, psm: int) -> OcrResult:
    with tempfile.TemporaryDirectory(prefix="slide-ocr-reread-") as tmp:
        path = Path(tmp) / f"{name}.png"
        image.save(path)
        try:
            cp = run_ocr([tesseract, str(path), "stdout", "-l", "eng", "--psm", str(psm)])
        except subprocess.TimeoutExpired:
            return OcrResult(text="", mean_conf=0, word_count=0, char_count=0, variant=f"{name}/psm{psm}/timeout", crop_box=None)
    text = normalize_text(cp.stdout or "")
    mean_conf = 50.0 if len(words(text)) >= 8 else 20.0 if text else 0.0
    return OcrResult(text=text, mean_conf=mean_conf, word_count=len(words(text)), char_count=len(text), variant=f"{name}/psm{psm}", crop_box=None)


def reread_slide(tesseract: str, slide: Path) -> OcrResult:
    image = Image.open(slide).convert("RGB")
    best = OcrResult(text="", mean_conf=0, word_count=0, char_count=0, variant="none", crop_box=None)
    for crop_name, crop, crop_box in candidate_crops(image):
        stat = ImageStat.Stat(crop.convert("L").resize((96, 54)))
        if stat.stddev[0] < 3:
            continue
        for variant_name, enhanced in enhance_variants(crop):
            for psm in (6,):
                result = tesseract_text(tesseract, enhanced, f"{crop_name}-{variant_name}", psm)
                result.crop_box = crop_box
                if result.score > best.score:
                    best = result
    return best


def process_candidate(payload: tuple[str, str]) -> dict:
    tesseract, slide_raw = payload
    slide = Path(slide_raw)
    original = current_text_for(slide)
    result = reread_slide(tesseract, slide)
    original_words = len(words(original))
    material_gain = result.word_count >= max(8, original_words + 5) or len(result.text) >= len(original) + 80
    confident_enough = result.mean_conf >= 25 or result.word_count >= 15
    if result.word_count < 3 and len(result.text) < 20:
        classification = "unreadable-or-non-slide"
    elif material_gain and confident_enough:
        classification = "improved"
    else:
        classification = "no-material-gain"
    improved_path = IMPROVED_OCR / slide.parent.name / f"{slide.stem}.txt"
    write_text(improved_path, result.text)
    return {
        "video_id": slide.parent.name,
        "slide": slide.name,
        "image": str(slide),
        "original_chars": len(original),
        "original_words": original_words,
        "weak_original": is_weak(original),
        "reread_chars": result.char_count,
        "reread_words": result.word_count,
        "reread_confidence": round(result.mean_conf, 2),
        "reread_variant": result.variant,
        "reread_crop_box": result.crop_box,
        "reread_text_preview": result.text[:240],
        "classification": classification,
    }


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + ("\n" if text.strip() else ""))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--all", action="store_true", help="Reread every slide, not just weak existing OCR.")
    parser.add_argument("--apply", action="store_true", help="Replace raw slide OCR when the reread is materially better.")
    parser.add_argument("--min-score-delta", type=float, default=60.0)
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()

    tesseract = resolve_tesseract()
    slides = sorted(SLIDE_ASSETS.glob("*/*.jpg"))
    rows = []
    candidates = []
    for slide in slides:
        original = current_text_for(slide)
        weak = is_weak(original)
        row = {
            "video_id": slide.parent.name,
            "slide": slide.name,
            "image": str(slide),
            "original_chars": len(original),
            "original_words": len(words(original)),
            "weak_original": weak,
        }
        rows.append(row)
        if args.all or weak:
            candidates.append((slide, original, row))
    if args.limit:
        candidates = candidates[: args.limit]

    improved = 0
    unreadable = 0
    processed = 0
    row_by_image = {row["image"]: row for row in rows}
    work = [(tesseract, str(slide)) for slide, _original, _row in candidates]
    with ProcessPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = [executor.submit(process_candidate, item) for item in work]
        for future in as_completed(futures):
            processed += 1
            result_row = future.result()
            row_by_image[result_row["image"]].update(result_row)
            if result_row["classification"] == "improved":
                improved += 1
                if args.apply:
                    improved_text_path = IMPROVED_OCR / result_row["video_id"] / result_row["slide"].replace(".jpg", ".txt")
                    write_text(SLIDE_OCR / result_row["video_id"] / result_row["slide"].replace(".jpg", ".txt"), improved_text_path.read_text(errors="ignore"))
            elif result_row["classification"] == "unreadable-or-non-slide":
                unreadable += 1
            if processed % 25 == 0:
                print(f"processed {processed}/{len(candidates)}; improved={improved}; unreadable={unreadable}", flush=True)

    AUDIT_PATH.parent.mkdir(parents=True, exist_ok=True)
    AUDIT_PATH.write_text(
        json.dumps(
            {
                "slideCount": len(slides),
                "candidateCount": len(candidates),
                "processedCount": processed,
                "improvedCount": improved,
                "unreadableOrNonSlideCount": unreadable,
                "applied": args.apply,
                "rows": rows,
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n"
    )
    print(json.dumps({"slides": len(slides), "candidates": len(candidates), "processed": processed, "improved": improved, "unreadable": unreadable, "audit": str(AUDIT_PATH)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
