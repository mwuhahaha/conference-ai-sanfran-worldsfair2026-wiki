#!/usr/bin/env python3
"""Improve weak slide OCR by merging existing OCR with RapidOCR rereads."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import time
from dataclasses import dataclass
from pathlib import Path

from rapidocr_onnxruntime import RapidOCR


ROOT = Path(__file__).resolve().parents[1]
SLIDE_ASSETS = ROOT / "wiki" / "assets" / "slides"
CANONICAL_OCR = ROOT / "raw" / "sources" / "slide-ocr"
MERGED_OCR = ROOT / "raw" / "sources" / "slide-ocr-rapidmerge"
AUDIT_PATH = ROOT / "raw" / "sources" / "slide-ocr-rapidmerge-audit.json"
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
        score -= sum(1 for line in lines if NOISE_RE.match(line.strip())) * 10
        if len(words) < 4:
            score *= 0.35
        if len(words) >= 12 and " " in self.text:
            score += 30
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


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


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
        candidates = [candidate for name, base in SOURCE_DIRS if (candidate := read_candidate(name, base, slide))]
        rapid_text = ""
        if ocr is not None:
            try:
                result, _elapsed = ocr(str(slide))
                rapid_text = rapid_lines(result)
            except Exception as exc:  # keep the batch moving on odd frames
                rapid_text = ""
                rapid_error = repr(exc)
            else:
                rapid_error = ""
            if rapid_text:
                candidates.append(Candidate("rapidocr-live", rapid_text))
        if not candidates:
            continue
        best = max(candidates, key=lambda item: item.score)
        merged_path = text_path(MERGED_OCR, slide)
        write_text(merged_path, best.text)
        old_score = current.score
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
    print(json.dumps({k: audit[k] for k in ["slidesSeen", "slidesProcessed", "canonicalUpdated", "elapsedSeconds"]}, sort_keys=True))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true", help="Process all slide images instead of weak canonical OCR only.")
    parser.add_argument("--limit", type=int, default=0, help="Debug limit over sorted slide images.")
    parser.add_argument("--min-gain", type=float, default=35.0, help="Minimum score gain required before replacing canonical OCR.")
    parser.add_argument("--no-rapidocr", action="store_true", help="Only merge existing OCR directories; do not run RapidOCR.")
    parser.add_argument("--no-backup", dest="backup", action="store_false", help="Do not preserve replaced canonical OCR text.")
    parser.add_argument("--progress", type=int, default=25)
    parser.set_defaults(backup=True)
    return improve(parser.parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
