#!/usr/bin/env python3
"""Improve weak slide OCR by merging existing OCR with RapidOCR rereads."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageChops, ImageEnhance, ImageFilter, ImageOps, ImageStat
from rapidocr_onnxruntime import RapidOCR


ROOT = Path(__file__).resolve().parents[1]
SLIDE_ASSETS = ROOT / "wiki" / "assets" / "slides"
CANONICAL_OCR = ROOT / "raw" / "sources" / "slide-ocr"
MERGED_OCR = ROOT / "raw" / "sources" / "slide-ocr-rapidmerge"
AUDIT_PATH = ROOT / "raw" / "sources" / "slide-ocr-rapidmerge-audit.json"
AUDIT_PAGE = ROOT / "wiki" / "resources" / "slide-ocr-rapidmerge-audit.md"
SOURCE_DIRS = [
    ("canonical", CANONICAL_OCR),
    ("tesseract-improved", ROOT / "raw" / "sources" / "slide-ocr-improved"),
    ("rapidocr-prior", ROOT / "raw" / "sources" / "slide-ocr-rapidocr"),
    ("reconstructed", ROOT / "raw" / "sources" / "reconstructed-slide-ocr"),
    ("dense", ROOT / "raw" / "sources" / "dense-slide-ocr"),
]

WORD_RE = re.compile(r"[A-Za-z][A-Za-z0-9'._/-]{2,}")
GLUED_RE = re.compile(r"[A-Za-z]{22,}")
NOISE_RE = re.compile(r"^[\\W_0-9]+$")
SPACELESS_RE = re.compile(r"[A-Za-z]{14,}[A-Z][a-z]")


@dataclass
class Candidate:
    source: str
    text: str

    @property
    def words(self) -> list[str]:
        return WORD_RE.findall(self.text)

    @property
    def score(self) -> float:
        words = self.words
        alpha = sum(ch.isalpha() for ch in self.text)
        lines = [line for line in self.text.splitlines() if line.strip()]
        unique = len({word.lower() for word in words})
        score = len(words) * 7 + unique * 4 + min(alpha, 1200) * 0.12 + min(len(lines), 30) * 3
        glued = sum(1 for word in words if GLUED_RE.search(word))
        score -= glued * 18
        score -= len(SPACELESS_RE.findall(self.text)) * 22
        score -= sum(1 for line in lines if NOISE_RE.match(line.strip())) * 10
        if lines:
            avg_line = sum(len(line) for line in lines) / len(lines)
            if avg_line > 95:
                score -= min(80, (avg_line - 95) * 1.4)
        if len(words) < 4:
            score *= 0.35
        if len(words) >= 12 and " " in self.text:
            score += 30
        if self.source.startswith("rapidocr-live") and len(words) >= 8:
            score += 8
        return score


def normalize_text(text: str) -> str:
    lines = []
    for line in text.replace("\r", "\n").splitlines():
        clean = re.sub(r"[ \t]+", " ", line).strip()
        clean = re.sub(r"\s+([,.;:!?])", r"\1", clean)
        if clean:
            lines.append(clean)
    return "\n".join(lines).strip()


def is_weak(text: str) -> bool:
    words = WORD_RE.findall(text)
    alpha = sum(ch.isalpha() for ch in text)
    if not text.strip():
        return True
    if len(words) < 8:
        return True
    if len(text) < 80 and len(words) < 12:
        return True
    if alpha < 35 and len(words) < 10:
        return True
    if Candidate("current", text).score < 95:
        return True
    if len(GLUED_RE.findall(text)) >= 2 or len(SPACELESS_RE.findall(text)) >= 1:
        return True
    return False


def text_path(base: Path, slide: Path) -> Path:
    return base / slide.parent.name / f"{slide.stem}.txt"


def read_candidate(source: str, base: Path, slide: Path) -> Candidate | None:
    path = text_path(base, slide)
    if not path.exists():
        return None
    text = normalize_text(path.read_text(encoding="utf-8", errors="ignore"))
    if not text:
        return None
    return Candidate(source, text)


def rapid_lines(result: list | None) -> str:
    if not result:
        return ""
    rows = []
    for item in result:
        if len(item) < 3:
            continue
        box, text, conf = item[0], str(item[1]).strip(), float(item[2] or 0)
        if not text or conf < 0.35:
            continue
        xs = [point[0] for point in box]
        ys = [point[1] for point in box]
        rows.append({"x": min(xs), "y": min(ys), "h": max(ys) - min(ys), "text": text, "conf": conf})
    rows.sort(key=lambda row: (row["y"], row["x"]))
    grouped: list[list[dict]] = []
    for row in rows:
        if not grouped:
            grouped.append([row])
            continue
        prev = grouped[-1][-1]
        tolerance = max(10, (prev["h"] + row["h"]) * 0.6)
        if abs(row["y"] - prev["y"]) <= tolerance:
            grouped[-1].append(row)
        else:
            grouped.append([row])
    lines = []
    for group in grouped:
        group.sort(key=lambda row: row["x"])
        lines.append(" ".join(row["text"] for row in group))
    return normalize_text("\n".join(lines))


def crop_dark_border(image: Image.Image) -> tuple[int, int, int, int]:
    gray = image.convert("L")
    bg = Image.new("L", gray.size, 0)
    diff = ImageChops.difference(gray, bg)
    diff = diff.point(lambda p: 255 if p > 10 else 0)
    bbox = diff.getbbox()
    if not bbox:
        return (0, 0, image.width, image.height)
    left, top, right, bottom = bbox
    if (right - left) < image.width * 0.45 or (bottom - top) < image.height * 0.35:
        return (0, 0, image.width, image.height)
    return (left, top, right, bottom)


def bright_region_box(image: Image.Image) -> tuple[int, int, int, int] | None:
    gray = ImageOps.autocontrast(image.convert("L"))
    small = gray.resize((240, max(1, round(240 * image.height / image.width))))
    mask = small.point(lambda p: 255 if p > 150 else 0)
    bbox = mask.getbbox()
    if not bbox:
        return None
    sx = image.width / small.width
    sy = image.height / small.height
    left, top, right, bottom = [int(v * (sx if i % 2 == 0 else sy)) for i, v in enumerate(bbox)]
    pad_x = int(image.width * 0.035)
    pad_y = int(image.height * 0.045)
    left = max(0, left - pad_x)
    top = max(0, top - pad_y)
    right = min(image.width, right + pad_x)
    bottom = min(image.height, bottom + pad_y)
    if (right - left) < image.width * 0.22 or (bottom - top) < image.height * 0.18:
        return None
    return (left, top, right, bottom)


def candidate_images(slide: Path, *, deep: bool) -> list[tuple[str, Image.Image]]:
    image = Image.open(slide).convert("RGB")
    crops: list[tuple[str, Image.Image]] = []
    border = crop_dark_border(image)
    if border != (0, 0, image.width, image.height):
        crops.append(("border-trim", image.crop(border)))
    bright = bright_region_box(image)
    if bright:
        crops.append(("bright-screen", image.crop(bright)))
    width, height = image.size
    layout_crops = [
        ("left-72", (0, 0, int(width * 0.72), height)),
        ("right-72", (int(width * 0.28), 0, width, height)),
        ("center-82", (int(width * 0.09), int(height * 0.04), int(width * 0.91), int(height * 0.96))),
    ]
    scored_layouts = []
    for name, box in layout_crops:
        crop = image.crop(box).convert("L").resize((128, 72))
        stat = ImageStat.Stat(ImageOps.autocontrast(crop))
        histogram = crop.histogram()
        bright_pixels = sum(histogram[151:])
        scored_layouts.append((bright_pixels * max(stat.stddev[0], 1), name, box))
    for _score, name, box in sorted(scored_layouts, reverse=True)[: (2 if deep else 1)]:
        crops.append((name, image.crop(box)))

    variants: list[tuple[str, Image.Image]] = []
    seen_sizes = set()
    for crop_name, crop in crops:
        if crop.width < 120 or crop.height < 80:
            continue
        key = (crop_name, crop.size)
        if key in seen_sizes:
            continue
        seen_sizes.add(key)
        gray = crop.convert("L")
        scale = min(3 if not deep else 4, max(2, 1400 // max(gray.width, gray.height)))
        enlarged = gray.resize((gray.width * scale, gray.height * scale), Image.Resampling.LANCZOS)
        contrast = ImageEnhance.Contrast(ImageOps.autocontrast(enlarged)).enhance(1.7).filter(ImageFilter.SHARPEN)
        variants.append((f"{crop_name}/contrast", contrast.convert("RGB")))
        if deep:
            threshold = contrast.point(lambda p: 255 if p > 165 else 0)
            variants.append((f"{crop_name}/threshold", threshold.convert("RGB")))
    return variants


def rapid_candidates(ocr: RapidOCR, slide: Path, *, variants: bool, deep: bool = False) -> tuple[list[Candidate], str]:
    candidates: list[Candidate] = []
    errors: list[str] = []
    jobs: list[tuple[str, str | Path]] = [("rapidocr-live/full", slide)]
    temp_paths: list[Path] = []
    temp_dir: tempfile.TemporaryDirectory | None = None
    if variants:
        temp_dir = tempfile.TemporaryDirectory(prefix="worldsfair-slide-ocr-")
        tmp = Path(temp_dir.name)
        for name, image in candidate_images(slide, deep=deep):
            path = tmp / f"{re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')}.png"
            image.save(path)
            temp_paths.append(path)
            jobs.append((f"rapidocr-live/{name}", path))
    try:
        for source, image_path in jobs:
            try:
                result, _elapsed = ocr(str(image_path))
                text = rapid_lines(result)
            except Exception as exc:  # keep the batch moving on odd frames
                errors.append(f"{source}: {exc!r}")
                continue
            if text:
                candidates.append(Candidate(source, text))
    finally:
        if temp_dir is not None:
            temp_dir.cleanup()
    return candidates, "; ".join(errors)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def write_audit_page(audit: dict, refreshed_pages: int | None = None) -> None:
    records = audit.get("records", [])
    source_counts: dict[str, int] = {}
    update_counts: dict[str, int] = {}
    for row in records:
        source = row.get("bestSource") or "unknown"
        source_counts[source] = source_counts.get(source, 0) + 1
        if row.get("updatedCanonical"):
            update_counts[source] = update_counts.get(source, 0) + 1
    source_lines = [f"- {source}: {count}" for source, count in sorted(source_counts.items(), key=lambda item: (-item[1], item[0]))[:12]]
    update_lines = [f"- {source}: {count}" for source, count in sorted(update_counts.items(), key=lambda item: (-item[1], item[0]))[:12]]
    lines = [
        "---",
        'title: "Slide OCR RapidMerge Audit"',
        'category: "resources"',
        'sourceLabels: ["Local slide OCR", "RapidOCR", "OCR audit"]',
        "---",
        "",
        "# Slide OCR RapidMerge Audit",
        "",
        "## What Changed",
        "Weak or suspicious slide OCR is reread with local OCR engines, image crops, and high-contrast variants, then merged against prior OCR sources. Canonical slide OCR is replaced only when the best candidate clears the score-gain threshold.",
        "",
        "## Latest Run",
        f"- Slide images seen: {audit.get('slidesSeen', 0):,}",
        f"- Slide OCR records processed: {audit.get('slidesProcessed', 0):,}",
        f"- Canonical OCR files updated: {audit.get('canonicalUpdated', 0):,}",
        f"- Slide markdown pages refreshed from canonical OCR: {refreshed_pages if refreshed_pages is not None else 'run refresh script after this pass'}",
        f"- Mode: {audit.get('mode', 'unknown')}",
        f"- Elapsed seconds: {audit.get('elapsedSeconds', 'unknown')}",
        "- Audit artifact: `raw/sources/slide-ocr-rapidmerge-audit.json`",
        "- Merge output directory: `raw/sources/slide-ocr-rapidmerge/`",
        "- Canonical backups: `raw/sources/slide-ocr-before-rapidmerge/`",
        "",
        "## Best Source Distribution",
        *(source_lines or ["- No records processed."]),
        "",
        "## Canonical Updates By Source",
        *(update_lines or ["- No canonical replacements in the latest run."]),
        "",
        "## Tooling Notes",
        "- `scripts/improve_slide_ocr_rapidmerge.py` performs weak-slide detection, crop/variant generation, RapidOCR rereads, source scoring, canonical replacement, and audit writing.",
        "- `scripts/run_slide_ocr_pipeline.py` runs the improvement pass, refreshes slide markdown, regenerates tool/topic surfaces that depend on slide text, and rebuilds the static site.",
        "- Optional heavier OCR engines such as PaddleOCR or Surya should be added as additional candidate sources when installed; this repository keeps RapidOCR as the default local path because it is already available and runs offline.",
        "",
        "## Source Rationale",
        "- PaddleOCR and Surya are stronger candidates for future layout-aware OCR, but they are heavier dependencies than the current local environment provides.",
        "- Tesseract documentation emphasizes that OCR quality depends heavily on preprocessing, cropping, border handling, and skew/segmentation quality; this pass therefore improves frame preparation instead of only swapping recognizers.",
        "- RapidOCR remains useful for scene text from video frames, while the merge scorer avoids blindly replacing cleaner Tesseract text with denser but glued text.",
    ]
    write_text(AUDIT_PAGE, "\n".join(lines))


def improve(args: argparse.Namespace) -> int:
    slides = sorted(SLIDE_ASSETS.glob("*/*.jpg"))
    if args.limit:
        slides = slides[: args.limit]
    ocr = RapidOCR() if not args.no_rapidocr else None
    audit = {
        "generatedBy": "scripts/improve_slide_ocr_rapidmerge.py",
        "startedAtEpoch": time.time(),
        "mode": "all" if args.all else "weak-only",
        "slidesSeen": len(slides),
        "slidesProcessed": 0,
        "canonicalUpdated": 0,
        "records": [],
    }
    for index, slide in enumerate(slides, 1):
        current = read_candidate("canonical", CANONICAL_OCR, slide) or Candidate("canonical", "")
        should_process = args.all or is_weak(current.text)
        if not should_process:
            continue
        old_score = current.score
        candidates = [candidate for name, base in SOURCE_DIRS if (candidate := read_candidate(name, base, slide))]
        rapid_error = ""
        if ocr is not None:
            use_variants = (not args.no_variants) and (args.deep_variants or old_score <= args.variant_max_old_score)
            rapid_items, rapid_error = rapid_candidates(ocr, slide, variants=use_variants, deep=args.deep_variants)
            candidates.extend(rapid_items)
        if not candidates:
            continue
        best = max(candidates, key=lambda item: item.score)
        merged_path = text_path(MERGED_OCR, slide)
        write_text(merged_path, best.text)
        updated = best.score > old_score + args.min_gain
        if updated and best.text.strip():
            canonical_path = text_path(CANONICAL_OCR, slide)
            if args.backup and canonical_path.exists():
                backup = ROOT / "raw" / "sources" / "slide-ocr-before-rapidmerge" / slide.parent.name / f"{slide.stem}.txt"
                backup.parent.mkdir(parents=True, exist_ok=True)
                if not backup.exists():
                    shutil.copy2(canonical_path, backup)
            write_text(canonical_path, best.text)
            audit["canonicalUpdated"] += 1
        audit["slidesProcessed"] += 1
        audit["records"].append(
            {
                "videoId": slide.parent.name,
                "slide": slide.name,
                "image": str(slide.relative_to(ROOT)),
                "oldSource": current.source,
                "oldWords": len(current.words),
                "oldScore": round(old_score, 2),
                "variantReread": use_variants if ocr is not None else False,
                "bestSource": best.source,
                "bestWords": len(best.words),
                "bestScore": round(best.score, 2),
                "updatedCanonical": updated,
                "rapidError": rapid_error if ocr is not None else "",
                "preview": best.text[:260],
            }
        )
        if args.progress and audit["slidesProcessed"] % args.progress == 0:
            print(json.dumps({"processed": audit["slidesProcessed"], "updated": audit["canonicalUpdated"], "at": str(slide.relative_to(ROOT))}))
    audit["finishedAtEpoch"] = time.time()
    audit["elapsedSeconds"] = round(audit["finishedAtEpoch"] - audit["startedAtEpoch"], 2)
    AUDIT_PATH.write_text(json.dumps(audit, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_audit_page(audit)
    print(json.dumps({k: audit[k] for k in ["slidesSeen", "slidesProcessed", "canonicalUpdated", "elapsedSeconds"]}, sort_keys=True))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true", help="Process all slide images instead of weak canonical OCR only.")
    parser.add_argument("--limit", type=int, default=0, help="Debug limit over sorted slide images.")
    parser.add_argument("--min-gain", type=float, default=35.0, help="Minimum score gain required before replacing canonical OCR.")
    parser.add_argument("--no-rapidocr", action="store_true", help="Only merge existing OCR directories; do not run RapidOCR.")
    parser.add_argument("--no-variants", action="store_true", help="Disable crop/high-contrast RapidOCR variants.")
    parser.add_argument("--variant-max-old-score", type=float, default=50.0, help="Only run crop/high-contrast variants when the old OCR score is at or below this threshold.")
    parser.add_argument("--deep-variants", action="store_true", help="Try extra crop and threshold variants. Slower but useful for manual rescue passes.")
    parser.add_argument("--no-backup", dest="backup", action="store_false", help="Do not preserve replaced canonical OCR text.")
    parser.add_argument("--progress", type=int, default=25)
    parser.set_defaults(backup=True)
    return improve(parser.parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
