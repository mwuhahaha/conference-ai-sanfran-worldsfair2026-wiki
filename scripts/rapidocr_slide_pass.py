#!/usr/bin/env python3
"""Use local RapidOCR to improve weak slide OCR results."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from rapidocr_onnxruntime import RapidOCR


ROOT = Path(__file__).resolve().parents[1]
SLIDE_ASSETS = ROOT / "wiki" / "assets" / "slides"
SLIDE_OCR = ROOT / "raw" / "sources" / "slide-ocr"
RAPID_OCR = ROOT / "raw" / "sources" / "slide-ocr-rapidocr"
AUDIT_PATH = ROOT / "raw" / "sources" / "slide-ocr-rapidocr-audit.json"

WORD_RE = re.compile(r"[A-Za-z][A-Za-z0-9'._/-]{2,}")


def words(text: str) -> list[str]:
    return WORD_RE.findall(text or "")


def normalize_text(text: str) -> str:
    lines = []
    for line in text.replace("\r", "\n").splitlines():
        clean = re.sub(r"[ \t]+", " ", line).strip()
        if clean:
            lines.append(clean)
    return "\n".join(lines).strip()


def is_weak(text: str) -> bool:
    found = words(text)
    alpha = sum(ch.isalpha() for ch in text)
    return not text.strip() or len(found) < 8 or (len(text) < 80 and len(found) < 12) or (alpha < 35 and len(found) < 10)


def current_text_for(slide: Path) -> str:
    path = SLIDE_OCR / slide.parent.name / f"{slide.stem}.txt"
    if not path.exists():
        return ""
    return normalize_text(path.read_text(errors="ignore"))


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + ("\n" if text.strip() else ""))


def rapid_text(ocr: RapidOCR, slide: Path) -> tuple[str, float, list[dict]]:
    result, _elapsed = ocr(str(slide))
    if not result:
        return "", 0.0, []
    lines = []
    kept = []
    confs = []
    for item in result:
        text = normalize_text(str(item[1] or ""))
        try:
            conf = float(item[2])
        except Exception:
            conf = 0.0
        # Drop non-English hallucinations from audience/stage shots.
        if not any("A" <= ch <= "Z" or "a" <= ch <= "z" for ch in text):
            continue
        if conf < 0.45:
            continue
        lines.append(text)
        confs.append(conf)
        kept.append({"text": text, "confidence": round(conf, 4)})
    return normalize_text("\n".join(lines)), (sum(confs) / len(confs) if confs else 0.0), kept


def materially_better(original: str, candidate: str, confidence: float) -> bool:
    original_words = len(words(original))
    candidate_words = len(words(candidate))
    if confidence < 0.5 and candidate_words < 12:
        return False
    if original_words < 3 and candidate_words >= 3:
        return True
    if candidate_words >= original_words + 4:
        return True
    if len(candidate) >= len(original) + 60 and candidate_words >= original_words + 2:
        return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    slides = sorted(SLIDE_ASSETS.glob("*/*.jpg"))
    candidates = []
    rows = []
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

    ocr = RapidOCR()
    improved = 0
    unreadable = 0
    processed = 0
    for slide, original, row in candidates:
        processed += 1
        text, confidence, kept = rapid_text(ocr, slide)
        write_text(RAPID_OCR / slide.parent.name / f"{slide.stem}.txt", text)
        row.update(
            {
                "rapid_chars": len(text),
                "rapid_words": len(words(text)),
                "rapid_confidence": round(confidence, 4),
                "rapid_text_preview": text[:300],
                "rapid_items": kept[:30],
            }
        )
        if not text or len(words(text)) < 2:
            row["classification"] = "unreadable-or-non-slide"
            unreadable += 1
        elif materially_better(original, text, confidence):
            row["classification"] = "improved"
            improved += 1
            if args.apply:
                write_text(SLIDE_OCR / slide.parent.name / f"{slide.stem}.txt", text)
        else:
            row["classification"] = "no-material-gain"
        if processed % 25 == 0:
            print(f"processed {processed}/{len(candidates)}; improved={improved}; unreadable={unreadable}", flush=True)

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
    print(
        json.dumps(
            {
                "slides": len(slides),
                "candidates": len(candidates),
                "processed": processed,
                "improved": improved,
                "unreadable": unreadable,
                "audit": str(AUDIT_PATH),
                "applied": args.apply,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
