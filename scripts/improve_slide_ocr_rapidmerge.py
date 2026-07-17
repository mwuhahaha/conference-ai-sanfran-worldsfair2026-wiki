#!/usr/bin/env python3
"""Improve slide OCR by merging existing OCR with optional local OCR engines."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import os
import re
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageChops, ImageEnhance, ImageFilter, ImageOps, ImageStat
from rapidocr_onnxruntime import RapidOCR

try:
    from slide_vision_cache_contract import (
        CACHE_SCHEMA_VERSION as AI_VISION_CACHE_SCHEMA_VERSION,
        MIN_ACCEPTED_CONFIDENCE as AI_VISION_MIN_ACCEPTED_CONFIDENCE,
        PROMPT_CONTRACT_SHA256 as AI_VISION_PROMPT_CONTRACT_SHA256,
        PROMPT_CONTRACT_VERSION as AI_VISION_PROMPT_CONTRACT_VERSION,
    )
except ModuleNotFoundError:  # Imported as scripts.improve_slide_ocr_rapidmerge.
    from scripts.slide_vision_cache_contract import (
        CACHE_SCHEMA_VERSION as AI_VISION_CACHE_SCHEMA_VERSION,
        MIN_ACCEPTED_CONFIDENCE as AI_VISION_MIN_ACCEPTED_CONFIDENCE,
        PROMPT_CONTRACT_SHA256 as AI_VISION_PROMPT_CONTRACT_SHA256,
        PROMPT_CONTRACT_VERSION as AI_VISION_PROMPT_CONTRACT_VERSION,
    )

try:
    import cv2
    import numpy as np
except Exception:  # OpenCV preprocessing is optional.
    cv2 = None
    np = None


ROOT = Path(__file__).resolve().parents[1]
SLIDE_ASSETS = ROOT / "wiki" / "assets" / "slides"
CANONICAL_OCR = ROOT / "raw" / "sources" / "slide-ocr"
MERGED_OCR = ROOT / "raw" / "sources" / "slide-ocr-rapidmerge"
AUDIT_PATH = ROOT / "raw" / "sources" / "slide-ocr-rapidmerge-audit.json"
AUDIT_PAGE = ROOT / "wiki" / "resources" / "slide-ocr-rapidmerge-audit.md"
PROVENANCE_REPAIR_SUMMARY = (
    ROOT / "raw" / "sources" / "slide-ocr-provenance-repair-summary.json"
)
SOURCE_DIRS = [
    ("operator-verified", ROOT / "raw" / "sources" / "slide-ocr-operator-verified"),
    ("ai-vision", ROOT / "raw" / "sources" / "slide-ocr-ai-vision"),
    ("canonical", CANONICAL_OCR),
    ("tesseract-improved", ROOT / "raw" / "sources" / "slide-ocr-improved"),
    ("rapidocr-prior", ROOT / "raw" / "sources" / "slide-ocr-rapidocr"),
    ("reconstructed", ROOT / "raw" / "sources" / "reconstructed-slide-ocr"),
    ("dense", ROOT / "raw" / "sources" / "dense-slide-ocr"),
]
INTERNAL_LOG_DIR = ROOT / ".ops" / "state" / "cache" / "slide-ocr-evals"
RECOVERY_ROOT = (
    ROOT / ".ops" / "state" / "cache" / "slide-ocr-rapidmerge-recovery"
)
PUBLICATION_SCHEMA_VERSION = 1
RECEIPT_SCHEMA_VERSION = 1
SELECTION_POLICY_VERSION = "operator-verified-absolute-v1"

WORD_RE = re.compile(r"[A-Za-z][A-Za-z0-9'._/-]{2,}")
GLUED_RE = re.compile(r"[A-Za-z]{22,}")
NOISE_RE = re.compile(r"^[\\W_0-9]+$")
SPACELESS_RE = re.compile(r"[A-Za-z]{14,}[A-Z][a-z]")


@dataclass
class Candidate:
    source: str
    text: str
    provenance: dict[str, object] | None = None

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
        if self.source == "operator-verified":
            score += 100
        if self.source == "ai-vision":
            score += 80
        return score


def normalize_text(text: str) -> str:
    lines = []
    for line in text.replace("\r", "\n").splitlines():
        clean = re.sub(r"[ \t]+", " ", line).strip()
        clean = re.sub(r"\s+([,.;:!?])", r"\1", clean)
        if clean:
            lines.append(clean)
    return "\n".join(lines).strip()


def available_module(name: str) -> bool:
    return importlib.util.find_spec(name) is not None


def is_perfect_enough(text: str) -> bool:
    """Heuristic for not rereading an already clean slide OCR block."""
    candidate = Candidate("current", text)
    words = candidate.words
    if is_weak(text):
        return False
    if candidate.score < 220:
        return False
    if len(words) < 24:
        return False
    if len(GLUED_RE.findall(text)) or len(SPACELESS_RE.findall(text)):
        return False
    lines = [line for line in text.splitlines() if line.strip()]
    if lines and max(len(line) for line in lines) > 120:
        return False
    return True


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


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _display_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def _validated_ai_vision_candidate(base: Path, slide: Path) -> Candidate | None:
    """Accept AI vision text only with a current producer receipt.

    The receipt is an integrity contract, not a signature. It prevents stale,
    partial, failed, or accidentally unreceipted cache text from receiving the
    AI-vision priority bonus and being promoted into canonical OCR.
    """

    path = text_path(base, slide)
    receipt_path = path.with_suffix(".receipt.json")
    if not path.is_file() or not receipt_path.is_file() or not slide.is_file():
        return None
    try:
        receipt_bytes = receipt_path.read_bytes()
        raw_text = path.read_text(encoding="utf-8").strip()
        receipt = json.loads(receipt_bytes)
        image_sha256 = _sha256_bytes(slide.read_bytes())
        canonical_path = text_path(CANONICAL_OCR, slide)
        canonical_text = (
            canonical_path.read_text(encoding="utf-8", errors="ignore").strip()
            if canonical_path.is_file()
            else ""
        )
    except (OSError, json.JSONDecodeError):
        return None
    required = {
        "schemaVersion": AI_VISION_CACHE_SCHEMA_VERSION,
        "status": "accepted",
        "imageSha256": image_sha256,
        "ocrSha256": _sha256_bytes(canonical_text.encode("utf-8")),
        "promptContractVersion": AI_VISION_PROMPT_CONTRACT_VERSION,
        "promptContractSha256": AI_VISION_PROMPT_CONTRACT_SHA256,
        "textSha256": _sha256_bytes(raw_text.encode("utf-8")),
    }
    if not raw_text or not isinstance(receipt, dict):
        return None
    if any(receipt.get(key) != value for key, value in required.items()):
        return None
    provider = receipt.get("provider")
    model = receipt.get("model")
    if (
        not isinstance(provider, str)
        or not provider.strip()
        or len(provider) > 200
    ):
        return None
    if not isinstance(model, str) or not model.strip() or len(model) > 200:
        return None
    try:
        confidence = float(receipt.get("confidence"))
        minimum_confidence = float(receipt.get("minimumAcceptedConfidence"))
        written_at = float(receipt.get("writtenAtEpoch"))
    except (TypeError, ValueError):
        return None
    if (
        isinstance(receipt.get("confidence"), bool)
        or isinstance(receipt.get("minimumAcceptedConfidence"), bool)
        or isinstance(receipt.get("writtenAtEpoch"), bool)
        or not math.isfinite(confidence)
        or not math.isfinite(minimum_confidence)
        or not math.isfinite(written_at)
        or not AI_VISION_MIN_ACCEPTED_CONFIDENCE <= minimum_confidence <= 1
        or not minimum_confidence <= confidence <= 1
        or written_at < 0
    ):
        return None
    text = normalize_text(raw_text)
    if not text:
        return None
    provenance = {
        "cacheTextPath": _display_path(path),
        "receiptPath": _display_path(receipt_path),
        "receiptSha256": _sha256_bytes(receipt_bytes),
        "schemaVersion": receipt["schemaVersion"],
        "status": receipt["status"],
        "imageSha256": receipt["imageSha256"],
        "inputOcrSha256": receipt["ocrSha256"],
        "provider": provider,
        "model": model,
        "promptContractVersion": receipt["promptContractVersion"],
        "promptContractSha256": receipt["promptContractSha256"],
        "minimumAcceptedConfidence": minimum_confidence,
        "confidence": confidence,
        "outputTextSha256": receipt["textSha256"],
        "writtenAtEpoch": written_at,
    }
    return Candidate("ai-vision", text, provenance)


def _validated_ai_vision_text(base: Path, slide: Path) -> str | None:
    candidate = _validated_ai_vision_candidate(base, slide)
    return candidate.text if candidate is not None else None


def read_candidate(source: str, base: Path, slide: Path) -> Candidate | None:
    path = text_path(base, slide)
    if source == "ai-vision":
        return _validated_ai_vision_candidate(base, slide)
    if not path.exists():
        return None
    text = normalize_text(path.read_text(encoding="utf-8", errors="ignore"))
    if not text:
        return None
    return Candidate(source, text)


def select_best_candidate(candidates: list[Candidate]) -> Candidate:
    """Select operator-verified text whenever it exists, independent of score."""

    operator = [
        candidate for candidate in candidates if candidate.source == "operator-verified"
    ]
    return max(operator or candidates, key=lambda candidate: candidate.score)


def decision_input_sha256(payload: dict[str, object]) -> str:
    return _sha256_bytes(
        json.dumps(payload, separators=(",", ":"), sort_keys=True).encode("utf-8")
    )


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


def generic_rows_to_text(rows: list[dict]) -> str:
    rows = [row for row in rows if row.get("text")]
    rows.sort(key=lambda row: (row.get("y", 0), row.get("x", 0)))
    grouped: list[list[dict]] = []
    for row in rows:
        if not grouped:
            grouped.append([row])
            continue
        prev = grouped[-1][-1]
        tolerance = max(10, (prev.get("h", 12) + row.get("h", 12)) * 0.65)
        if abs(row.get("y", 0) - prev.get("y", 0)) <= tolerance:
            grouped[-1].append(row)
        else:
            grouped.append([row])
    lines = []
    for group in grouped:
        group.sort(key=lambda row: row.get("x", 0))
        lines.append(" ".join(str(row["text"]) for row in group if row.get("text")))
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
        if cv2 is not None and np is not None:
            arr = np.array(contrast)
            adaptive = cv2.adaptiveThreshold(arr, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 9)
            kernel = np.ones((2, 2), np.uint8)
            morph = cv2.morphologyEx(adaptive, cv2.MORPH_OPEN, kernel)
            variants.append((f"{crop_name}/opencv-adaptive", Image.fromarray(morph).convert("RGB")))
        if deep:
            threshold = contrast.point(lambda p: 255 if p > 165 else 0)
            variants.append((f"{crop_name}/threshold", threshold.convert("RGB")))
    return variants


class OcrEngine:
    name = "base"

    def available(self) -> bool:
        return False

    def init(self) -> str:
        return "not implemented"

    def read(self, image_path: Path) -> str:
        return ""


class RapidOcrEngine(OcrEngine):
    name = "rapidocr"

    def __init__(self) -> None:
        self.engine = None

    def available(self) -> bool:
        return available_module("rapidocr_onnxruntime")

    def init(self) -> str:
        self.engine = RapidOCR()
        return "ready"

    def read(self, image_path: Path) -> str:
        result, _elapsed = self.engine(str(image_path))
        return rapid_lines(result)


class PaddleOcrEngine(OcrEngine):
    name = "paddleocr"

    def __init__(self) -> None:
        self.engine = None

    def available(self) -> bool:
        return available_module("paddleocr") and available_module("paddle")

    def init(self) -> str:
        # The default oneDNN path can fail on some local CPU installs with
        # Paddle 3.x/PaddleOCR 3.x PIR attributes. Disable it before import.
        os.environ.setdefault("FLAGS_use_mkldnn", "0")
        import paddle
        from paddleocr import PaddleOCR

        try:
            paddle.set_flags({"FLAGS_use_mkldnn": False})
        except Exception:
            pass
        try:
            self.engine = PaddleOCR(lang="en", use_textline_orientation=True)
        except TypeError:
            self.engine = PaddleOCR(lang="en", use_angle_cls=True)
        return "ready"

    def read(self, image_path: Path) -> str:
        try:
            result = self.engine.ocr(str(image_path))
        except AttributeError:
            result = self.engine.predict(str(image_path))
        rows: list[dict] = []
        for page in result or []:
            if isinstance(page, dict):
                texts = page.get("rec_texts") or page.get("text") or []
                boxes = page.get("rec_boxes") or page.get("dt_polys") or []
                if isinstance(texts, str):
                    texts = [texts]
                for index, text in enumerate(texts):
                    box = boxes[index] if index < len(boxes) else None
                    if box is not None and len(box) >= 4 and not isinstance(box[0], (list, tuple)):
                        x1, y1, x2, y2 = [float(v) for v in box[:4]]
                    elif box is not None:
                        xs = [float(point[0]) for point in box]
                        ys = [float(point[1]) for point in box]
                        x1, y1, y2 = min(xs), min(ys), max(ys)
                    else:
                        x1 = y1 = y2 = 0
                    rows.append({"x": x1, "y": y1, "h": y2 - y1, "text": str(text).strip()})
            elif isinstance(page, list):
                for item in page:
                    if not item or len(item) < 2:
                        continue
                    box = item[0]
                    text_part = item[1]
                    text = text_part[0] if isinstance(text_part, (list, tuple)) else text_part
                    xs = [float(point[0]) for point in box]
                    ys = [float(point[1]) for point in box]
                    rows.append({"x": min(xs), "y": min(ys), "h": max(ys) - min(ys), "text": str(text).strip()})
        return generic_rows_to_text(rows)


class EasyOcrEngine(OcrEngine):
    name = "easyocr"

    def __init__(self) -> None:
        self.engine = None

    def available(self) -> bool:
        return available_module("easyocr")

    def init(self) -> str:
        import easyocr

        self.engine = easyocr.Reader(["en"], gpu=False, verbose=False)
        return "ready"

    def read(self, image_path: Path) -> str:
        result = self.engine.readtext(str(image_path), detail=1, paragraph=False)
        rows = []
        for box, text, conf in result:
            if conf < 0.25:
                continue
            xs = [float(point[0]) for point in box]
            ys = [float(point[1]) for point in box]
            rows.append({"x": min(xs), "y": min(ys), "h": max(ys) - min(ys), "text": str(text).strip()})
        return generic_rows_to_text(rows)


class DoctrEngine(OcrEngine):
    name = "doctr"

    def __init__(self) -> None:
        self.engine = None

    def available(self) -> bool:
        return available_module("doctr") and (available_module("torch") or available_module("tensorflow"))

    def init(self) -> str:
        from doctr.models import ocr_predictor

        self.engine = ocr_predictor(pretrained=True)
        return "ready"

    def read(self, image_path: Path) -> str:
        import numpy as local_np

        image = local_np.array(Image.open(image_path).convert("RGB"))
        doc = self.engine([image])
        exported = doc.export()
        lines = []
        for page in exported.get("pages", []):
            for block in page.get("blocks", []):
                for line in block.get("lines", []):
                    words = [word.get("value", "") for word in line.get("words", []) if word.get("value")]
                    if words:
                        lines.append(" ".join(words))
        return normalize_text("\n".join(lines))


class SuryaEngine(OcrEngine):
    name = "surya"

    def available(self) -> bool:
        return available_module("surya")

    def init(self) -> str:
        return "available-but-disabled-license-check-required"

    def read(self, image_path: Path) -> str:
        return ""


def requested_engines(names: list[str]) -> list[OcrEngine]:
    all_engines: dict[str, OcrEngine] = {
        "rapidocr": RapidOcrEngine(),
        "paddleocr": PaddleOcrEngine(),
        "easyocr": EasyOcrEngine(),
        "doctr": DoctrEngine(),
        "surya": SuryaEngine(),
    }
    selected = names or ["rapidocr", "paddleocr", "easyocr", "doctr"]
    return [all_engines[name] for name in selected if name in all_engines]


def engine_candidates(
    engines: list[OcrEngine],
    slide: Path,
    *,
    variants: bool,
    deep: bool,
) -> tuple[list[Candidate], dict[str, str]]:
    candidates: list[Candidate] = []
    errors: dict[str, str] = {}
    jobs: list[tuple[str, Path]] = [("full", slide)]
    temp_dir: tempfile.TemporaryDirectory | None = None
    if variants:
        temp_dir = tempfile.TemporaryDirectory(prefix="worldsfair-slide-ocr-")
        tmp = Path(temp_dir.name)
        for name, image in candidate_images(slide, deep=deep):
            path = tmp / f"{re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')}.png"
            image.save(path)
            jobs.append((name, path))
    try:
        for engine in engines:
            for variant_name, image_path in jobs:
                source = f"{engine.name}-live/{variant_name}"
                try:
                    text = engine.read(image_path)
                except Exception as exc:
                    errors[source] = repr(exc)
                    continue
                text = normalize_text(text)
                if text:
                    candidates.append(Candidate(source, text))
    finally:
        if temp_dir is not None:
            temp_dir.cleanup()
    return candidates, errors


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


def atomic_write_bytes(path: Path, data: bytes) -> None:
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
        os.replace(temporary_path, path)
        _fsync_directory(path.parent)
    finally:
        temporary_path.unlink(missing_ok=True)


def write_text(path: Path, text: str) -> None:
    atomic_write_bytes(path, _text_bytes(text))


def decision_receipt_path(slide: Path) -> Path:
    return text_path(MERGED_OCR, slide).with_suffix(".receipt.json")


def recovery_backup_path(run_id: str, slide: Path) -> Path:
    return RECOVERY_ROOT / run_id / slide.parent.name / f"{slide.stem}.txt"


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
    engine_lines = [
        f"- {engine}: {status}"
        for engine, status in sorted((audit.get("engineStatus") or {}).items())
    ]
    repair = {}
    if PROVENANCE_REPAIR_SUMMARY.is_file():
        try:
            candidate = json.loads(PROVENANCE_REPAIR_SUMMARY.read_text(encoding="utf-8"))
            audit_digest = hashlib.sha256(AUDIT_PATH.read_bytes()).hexdigest()
            if (
                isinstance(candidate, dict)
                and candidate.get("historicalAuditSuperseded") is True
                and candidate.get("sourceAuditSha256") == audit_digest
            ):
                repair = candidate
        except (OSError, json.JSONDecodeError):
            repair = {}
    run_heading = (
        "## Historical RapidMerge Run (Superseded)" if repair else "## Latest Run"
    )
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
    ]
    if repair:
        historical_affected = int(
            repair.get(
                "historicalUnreceiptedAiVisionUpdates",
                audit.get("canonicalUpdated", 0),
            )
        )
        restored = int(repair.get("restoredCanonicalFiles", 0))
        already_matched = int(repair.get("alreadyMatchedBackupFiles", 0))
        accepted = int(
            repair.get("historicalAiVisionUpdatesAcceptedByCurrentPolicy", 0)
        )
        lines.extend(
            [
                "## Provenance Repair",
                f"A historical RapidMerge run affected {historical_affected:,} canonical OCR files using AI-vision output that had no valid cache receipts. The repair restored {restored:,} canonical OCR files from their byte-exact pre-merge backups. The other {already_matched:,} files already matched their pre-merge backups byte-for-byte, so no content restoration was needed for them. The post-repair check found {int(repair.get('remainingExactUnreceiptedCopies', 0)):,} remaining exact unreceipted copies and {int(repair.get('ambiguousRecords', 0)):,} ambiguous records.",
                "",
                f"The old AI-vision cache and both historical audit distributions below are superseded and untrusted; they are not current trusted evidence. They are retained for auditability, but the current RapidMerge policy accepts {accepted:,} results from that run because it recorded {int(repair.get('historicalAiVisionAuditRecordedReceipts', 0)):,} current provenance receipts.",
                "",
            ]
        )
    lines.extend(
        [
        run_heading,
        f"- Slide images seen: {audit.get('slidesSeen', 0):,}",
        f"- Slide OCR records processed: {audit.get('slidesProcessed', 0):,}",
        f"- Slides skipped as already clean: {audit.get('slidesSkippedPerfect', 0):,}",
        f"- Canonical OCR files updated: {audit.get('canonicalUpdated', 0):,}",
        f"- Manual review queue entries: {audit.get('manualReviewNeeded', 0):,}",
        f"- Slide markdown pages refreshed from canonical OCR: {refreshed_pages if refreshed_pages is not None else 'run refresh script after this pass'}",
        f"- Mode: {audit.get('mode', 'unknown')}",
        f"- Elapsed seconds: {audit.get('elapsedSeconds', 'unknown')}",
        "- Audit artifact: `raw/sources/slide-ocr-rapidmerge-audit.json`",
        "- Merge output directory: `raw/sources/slide-ocr-rapidmerge/`",
        "- Canonical backups: `raw/sources/slide-ocr-before-rapidmerge/`",
        "",
        "## Best Source Distribution",
        *(
            ["These are historical selections from the superseded run, not currently accepted sources.", ""]
            if repair
            else []
        ),
        *(source_lines or ["- No records processed."]),
        "",
        "## Canonical Updates By Source",
        *(
            ["This is the superseded run's historical update count. The provenance repair described above has removed its unreceipted AI-vision content from canonical OCR.", ""]
            if repair
            else []
        ),
        *(update_lines or ["- No canonical replacements in the latest run."]),
        "",
        "## Engine Status",
        *(engine_lines or ["- Live OCR disabled or no engines selected."]),
        "",
        "## Tooling Notes",
        "- `scripts/improve_slide_ocr_rapidmerge.py` performs weak-slide detection, crop/variant generation, RapidOCR rereads, source scoring, canonical replacement, and audit writing.",
        "- `scripts/run_slide_ocr_pipeline.py` runs the improvement pass, refreshes slide markdown, regenerates tool/topic surfaces that depend on slide text, and rebuilds the static site.",
        "- Optional heavier OCR engines such as PaddleOCR, EasyOCR, docTR, and Surya are treated as local candidate engines when installed and enabled.",
        "",
        "## Source Rationale",
        "- PaddleOCR and Surya are stronger candidates for future layout-aware OCR, but they are heavier dependencies than the current local environment provides.",
        "- Tesseract documentation emphasizes that OCR quality depends heavily on preprocessing, cropping, border handling, and skew/segmentation quality; this pass therefore improves frame preparation instead of only swapping recognizers.",
        "- RapidOCR remains useful for scene text from video frames, while the merge scorer avoids blindly replacing cleaner Tesseract text with denser but glued text.",
        ]
    )
    write_text(AUDIT_PAGE, "\n".join(lines))


def _json_bytes(payload: dict[str, object]) -> bytes:
    return _text_bytes(
        json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True)
    )


def _valid_sha256(value: object) -> bool:
    return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value) is not None


def _record_paths(record: dict[str, object], run_id: str) -> tuple[Path, Path, Path]:
    video_id = record.get("videoId")
    slide_name = record.get("slide")
    if (
        not isinstance(video_id, str)
        or not video_id
        or Path(video_id).name != video_id
        or not isinstance(slide_name, str)
        or Path(slide_name).name != slide_name
        or not slide_name.endswith(".jpg")
    ):
        raise RuntimeError("RapidMerge recovery record has an unsafe path")
    slide = SLIDE_ASSETS / video_id / slide_name
    return (
        text_path(CANONICAL_OCR, slide),
        decision_receipt_path(slide),
        recovery_backup_path(run_id, slide),
    )


def recover_incomplete_publication() -> dict[str, object] | None:
    """Roll back canonical files from an interrupted publication audit."""

    if not AUDIT_PATH.is_file():
        return None
    try:
        audit = json.loads(AUDIT_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    if (
        not isinstance(audit, dict)
        or audit.get("publicationSchemaVersion") != PUBLICATION_SCHEMA_VERSION
        or audit.get("status") not in {"publishing", "failed"}
    ):
        return None
    run_id = audit.get("runId")
    records = audit.get("records")
    if (
        not isinstance(run_id, str)
        or re.fullmatch(r"[A-Za-z0-9._-]{1,100}", run_id) is None
        or not isinstance(records, list)
    ):
        raise RuntimeError("RapidMerge incomplete audit is not safely recoverable")

    actions: list[tuple[dict[str, object], Path, Path, Path, bytes | None]] = []
    for raw_record in records:
        if not isinstance(raw_record, dict) or not raw_record.get(
            "updatedCanonicalPlanned"
        ):
            continue
        canonical, receipt_path, backup = _record_paths(raw_record, run_id)
        previous = raw_record.get("previousCanonicalSha256")
        replacement = raw_record.get("replacementCanonicalSha256")
        existed = raw_record.get("previousCanonicalExisted")
        if (
            not isinstance(existed, bool)
            or (existed and not _valid_sha256(previous))
            or not _valid_sha256(replacement)
        ):
            raise RuntimeError("RapidMerge recovery hashes are incomplete")
        current_bytes = canonical.read_bytes() if canonical.is_file() else None
        current_digest = _sha256_bytes(current_bytes) if current_bytes is not None else None
        if existed:
            if not backup.is_file():
                raise RuntimeError(f"RapidMerge recovery backup is missing: {backup}")
            backup_bytes = backup.read_bytes()
            if _sha256_bytes(backup_bytes) != previous:
                raise RuntimeError(f"RapidMerge recovery backup digest mismatch: {backup}")
            if current_digest not in {previous, replacement}:
                raise RuntimeError(
                    f"RapidMerge canonical file diverged during recovery: {canonical}"
                )
        else:
            backup_bytes = None
            if current_digest not in {None, replacement}:
                raise RuntimeError(
                    f"RapidMerge new canonical file diverged during recovery: {canonical}"
                )
        actions.append((raw_record, canonical, receipt_path, backup, backup_bytes))

    restored = 0
    for record, canonical, receipt_path, _backup, backup_bytes in actions:
        replacement = record["replacementCanonicalSha256"]
        current_bytes = canonical.read_bytes() if canonical.is_file() else None
        if current_bytes is not None and _sha256_bytes(current_bytes) == replacement:
            if backup_bytes is None:
                canonical.unlink(missing_ok=True)
                _fsync_directory(canonical.parent)
            else:
                atomic_write_bytes(canonical, backup_bytes)
            restored += 1
        if receipt_path.is_file():
            try:
                receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                receipt = {}
            if isinstance(receipt, dict) and receipt.get("runId") == run_id:
                receipt["status"] = "rolled_back"
                receipt["rolledBackAtEpoch"] = time.time()
                atomic_write_bytes(receipt_path, _json_bytes(receipt))
        record["canonicalPublicationStatus"] = "rolled_back"
        record["updatedCanonical"] = False

    audit["status"] = "rolled_back"
    audit["canonicalUpdated"] = 0
    audit["recovery"] = {
        "restoredCanonicalFiles": restored,
        "completedAtEpoch": time.time(),
    }
    atomic_write_bytes(AUDIT_PATH, _json_bytes(audit))
    return audit


def _decision_receipt(
    audit: dict[str, object], record: dict[str, object], *, status: str
) -> dict[str, object]:
    receipt = {
        "schemaVersion": RECEIPT_SCHEMA_VERSION,
        "status": status,
        "runId": audit["runId"],
        "publicationPlanSha256": audit["publicationPlanSha256"],
        "selectionPolicyVersion": SELECTION_POLICY_VERSION,
        "image": record["image"],
        "imageSha256": record["imageSha256"],
        "decisionInputSha256": record["decisionInputSha256"],
        "selectedSource": record["bestSource"],
        "selectedTextSha256": record["selectedTextSha256"],
        "mergedPath": record["mergedPath"],
        "mergedSha256": record["selectedTextSha256"],
        "canonicalPath": record["canonicalPath"],
        "previousCanonicalExisted": record["previousCanonicalExisted"],
        "previousCanonicalSha256": record["previousCanonicalSha256"],
        "replacementCanonicalSha256": record["replacementCanonicalSha256"],
        "updatedCanonicalPlanned": record["updatedCanonicalPlanned"],
        "recoveryBackupPath": record["recoveryBackupPath"],
        "recoveryBackupSha256": record["recoveryBackupSha256"],
    }
    if record.get("aiVisionProvenance"):
        receipt["aiVisionProvenance"] = record["aiVisionProvenance"]
    return receipt


def _validate_decision_sources(decisions: list[dict[str, object]]) -> None:
    sources = dict(SOURCE_DIRS)
    operator_base = sources.get("operator-verified")
    ai_base = sources.get("ai-vision")
    for decision in decisions:
        record = decision["record"]
        slide = decision["slide"]
        if _sha256_bytes(slide.read_bytes()) != record["imageSha256"]:
            raise RuntimeError(f"RapidMerge image changed before publication: {slide}")
        if record["bestSource"] == "operator-verified":
            if operator_base is None:
                raise RuntimeError("RapidMerge operator source directory is unavailable")
            operator = read_candidate("operator-verified", operator_base, slide)
            if (
                operator is None
                or _sha256_bytes(operator.text.encode("utf-8"))
                != record["selectedTextSha256"]
            ):
                raise RuntimeError(
                    f"RapidMerge operator text changed before publication: {slide}"
                )
        if record["bestSource"] == "ai-vision":
            if ai_base is None:
                raise RuntimeError("RapidMerge AI source directory is unavailable")
            candidate = _validated_ai_vision_candidate(ai_base, slide)
            if (
                candidate is None
                or candidate.provenance != record.get("aiVisionProvenance")
                or _sha256_bytes(candidate.text.encode("utf-8"))
                != record["selectedTextSha256"]
            ):
                raise RuntimeError(
                    f"RapidMerge AI receipt changed before publication: {slide}"
                )


def publish_rapidmerge(
    audit: dict[str, object],
    decisions: list[dict[str, object]],
    args: argparse.Namespace,
) -> None:
    """Publish receipts before canonical replacements and finalize the audit last."""

    _validate_decision_sources(decisions)
    for decision in decisions:
        record = decision["record"]
        old_bytes = decision["old_bytes"]
        canonical = decision["canonical_path"]
        current = canonical.read_bytes() if canonical.is_file() else None
        if current != old_bytes:
            raise RuntimeError(f"RapidMerge canonical input changed before publication: {canonical}")
        recovery = decision["recovery_path"]
        if old_bytes is not None:
            atomic_write_bytes(recovery, old_bytes)
            if args.backup:
                legacy_backup = (
                    ROOT
                    / "raw"
                    / "sources"
                    / "slide-ocr-before-rapidmerge"
                    / decision["slide"].parent.name
                    / f"{decision['slide'].stem}.txt"
                )
                if not legacy_backup.exists():
                    atomic_write_bytes(legacy_backup, old_bytes)
        record["recoveryBackupPath"] = _display_path(recovery)
        record["recoveryBackupSha256"] = (
            _sha256_bytes(old_bytes) if old_bytes is not None else None
        )

    plan_manifest = [
        {
            "image": decision["record"]["image"],
            "decisionInputSha256": decision["record"]["decisionInputSha256"],
            "updatedCanonicalPlanned": decision["record"]["updatedCanonicalPlanned"],
            "previousCanonicalSha256": decision["record"]["previousCanonicalSha256"],
            "replacementCanonicalSha256": decision["record"]["replacementCanonicalSha256"],
            "recoveryBackupSha256": decision["record"]["recoveryBackupSha256"],
        }
        for decision in decisions
    ]
    audit["publicationPlanSha256"] = decision_input_sha256(
        {
            "runId": audit["runId"],
            "selectionPolicyVersion": SELECTION_POLICY_VERSION,
            "records": plan_manifest,
        }
    )
    audit["status"] = "publishing"
    atomic_write_bytes(AUDIT_PATH, _json_bytes(audit))

    try:
        receipt_manifest: list[dict[str, str]] = []
        canonical_manifest: list[dict[str, str]] = []
        for decision in decisions:
            record = decision["record"]
            merged_path = decision["merged_path"]
            receipt_path = decision["receipt_path"]
            prepared = _decision_receipt(audit, record, status="prepared")
            atomic_write_bytes(receipt_path, _json_bytes(prepared))
            write_text(merged_path, decision["best_text"])
            if decision["updated"]:
                canonical = decision["canonical_path"]
                current = canonical.read_bytes() if canonical.is_file() else None
                if current != decision["old_bytes"]:
                    raise RuntimeError(
                        f"RapidMerge canonical changed during publication: {canonical}"
                    )
                atomic_write_bytes(canonical, decision["new_bytes"])
            committed_receipt = _decision_receipt(audit, record, status="committed")
            committed_receipt["committedAtEpoch"] = time.time()
            receipt_bytes = _json_bytes(committed_receipt)
            atomic_write_bytes(receipt_path, receipt_bytes)
            record["canonicalPublicationStatus"] = "committed"
            record["updatedCanonical"] = bool(decision["updated"])
            record["decisionReceiptSha256"] = _sha256_bytes(receipt_bytes)
            receipt_manifest.append(
                {
                    "path": _display_path(receipt_path),
                    "sha256": record["decisionReceiptSha256"],
                }
            )
            if decision["updated"]:
                canonical_manifest.append(
                    {
                        "path": record["canonicalPath"],
                        "sha256": record["replacementCanonicalSha256"],
                    }
                )

        for decision in decisions:
            record = decision["record"]
            merged_bytes = decision["merged_path"].read_bytes()
            if _sha256_bytes(merged_bytes.rstrip(b"\n")) != record["selectedTextSha256"]:
                raise RuntimeError(
                    f"RapidMerge merged output digest mismatch: {decision['merged_path']}"
                )
            receipt_bytes = decision["receipt_path"].read_bytes()
            if _sha256_bytes(receipt_bytes) != record["decisionReceiptSha256"]:
                raise RuntimeError(
                    f"RapidMerge receipt digest mismatch: {decision['receipt_path']}"
                )
            if decision["updated"] and _sha256_bytes(
                decision["canonical_path"].read_bytes()
            ) != record["replacementCanonicalSha256"]:
                raise RuntimeError(
                    f"RapidMerge canonical output digest mismatch: {decision['canonical_path']}"
                )

        audit["decisionReceiptManifest"] = sorted(
            receipt_manifest, key=lambda item: item["path"]
        )
        audit["decisionReceiptManifestSha256"] = decision_input_sha256(
            {"receipts": audit["decisionReceiptManifest"]}
        )
        audit["canonicalManifest"] = sorted(
            canonical_manifest, key=lambda item: item["path"]
        )
        audit["canonicalManifestSha256"] = decision_input_sha256(
            {"canonical": audit["canonicalManifest"]}
        )
        audit["canonicalUpdated"] = len(canonical_manifest)
        audit["finishedAtEpoch"] = time.time()
        audit["elapsedSeconds"] = round(
            audit["finishedAtEpoch"] - audit["startedAtEpoch"], 2
        )
        audit["status"] = "succeeded"
        atomic_write_bytes(AUDIT_PATH, _json_bytes(audit))
    except BaseException:
        try:
            recover_incomplete_publication()
        except Exception as recovery_error:
            raise RuntimeError(
                "RapidMerge publication failed and automatic recovery is blocked"
            ) from recovery_error
        raise


def improve(args: argparse.Namespace) -> int:
    recovered = recover_incomplete_publication()
    slides = sorted(SLIDE_ASSETS.glob("*/*.jpg"))
    if args.limit:
        slides = slides[: args.limit]
    engines = []
    engine_status = {}
    if not args.no_live_ocr:
        for engine in requested_engines(args.engine):
            if engine.name == "surya" and not args.enable_surya:
                engine_status[engine.name] = "disabled-license-check-required"
                continue
            if not engine.available():
                engine_status[engine.name] = "unavailable"
                continue
            try:
                engine_status[engine.name] = engine.init()
                if engine_status[engine.name] == "ready":
                    engines.append(engine)
            except Exception as exc:
                engine_status[engine.name] = f"init_failed: {exc!r}"
    audit = {
        "generatedBy": "scripts/improve_slide_ocr_rapidmerge.py",
        "publicationSchemaVersion": PUBLICATION_SCHEMA_VERSION,
        "selectionPolicyVersion": SELECTION_POLICY_VERSION,
        "status": "planning",
        "runId": f"rapidmerge-{int(time.time() * 1000)}-{os.getpid()}",
        "startedAtEpoch": time.time(),
        "mode": "all" if args.all else "weak-only",
        "skipPerfect": args.skip_perfect,
        "engineStatus": engine_status,
        "slidesSeen": len(slides),
        "slidesProcessed": 0,
        "slidesSkippedPerfect": 0,
        "canonicalUpdated": 0,
        "manualReviewNeeded": 0,
        "records": [],
    }
    if recovered is not None:
        audit["recoveredPriorRunId"] = recovered.get("runId")
    decisions: list[dict[str, object]] = []
    source_directories = dict(SOURCE_DIRS)
    for index, slide in enumerate(slides, 1):
        current = read_candidate("canonical", CANONICAL_OCR, slide) or Candidate("canonical", "")
        operator_base = source_directories.get("operator-verified")
        operator = (
            read_candidate("operator-verified", operator_base, slide)
            if operator_base is not None
            else None
        )
        perfect = is_perfect_enough(current.text)
        should_process = args.all or is_weak(current.text) or operator is not None
        if args.skip_perfect and perfect and operator is None:
            audit["slidesSkippedPerfect"] += 1
            continue
        if not should_process:
            continue
        old_score = current.score
        candidates = [
            candidate
            for name, base in SOURCE_DIRS
            if (
                candidate := (
                    operator
                    if name == "operator-verified"
                    else read_candidate(name, base, slide)
                )
            )
        ]
        engine_errors = {}
        if engines:
            use_variants = (not args.no_variants) and (args.deep_variants or old_score <= args.variant_max_old_score)
            live_items, engine_errors = engine_candidates(engines, slide, variants=use_variants, deep=args.deep_variants)
            candidates.extend(live_items)
        else:
            use_variants = False
        if not candidates:
            continue
        best = select_best_candidate(candidates)
        merged_path = text_path(MERGED_OCR, slide)
        text_changed = best.text.strip() != current.text.strip()
        updated = text_changed and (
            best.source == "operator-verified"
            or best.score > old_score + args.min_gain
        )
        manual_needed = (
            args.log_manual_queue
            and best.source != "operator-verified"
            and best.source != "ai-vision"
            and (best.score < args.manual_score_threshold or is_weak(best.text))
        )
        if manual_needed:
            audit["manualReviewNeeded"] += 1
        canonical_path = text_path(CANONICAL_OCR, slide)
        old_bytes = canonical_path.read_bytes() if canonical_path.is_file() else None
        new_bytes = _text_bytes(best.text)
        image_sha256 = _sha256_bytes(slide.read_bytes())
        selected_text_sha256 = _sha256_bytes(best.text.encode("utf-8"))
        ai_provenance = best.provenance if best.source == "ai-vision" else None
        decision_inputs = {
            "selectionPolicyVersion": SELECTION_POLICY_VERSION,
            "imageSha256": image_sha256,
            "previousCanonicalSha256": (
                _sha256_bytes(old_bytes) if old_bytes is not None else None
            ),
            "selectedSource": best.source,
            "selectedTextSha256": selected_text_sha256,
            "minimumScoreGain": float(args.min_gain),
            "aiVisionReceiptSha256": (
                ai_provenance.get("receiptSha256") if ai_provenance else None
            ),
            "aiVisionInputOcrSha256": (
                ai_provenance.get("inputOcrSha256") if ai_provenance else None
            ),
        }
        receipt_path = decision_receipt_path(slide)
        recovery_path = recovery_backup_path(audit["runId"], slide)
        record = {
            "videoId": slide.parent.name,
            "slide": slide.name,
            "image": str(slide.relative_to(ROOT)),
            "imageSha256": image_sha256,
            "oldSource": current.source,
            "oldWords": len(current.words),
            "oldScore": round(old_score, 2),
            "previousCanonicalExisted": old_bytes is not None,
            "previousCanonicalSha256": (
                _sha256_bytes(old_bytes) if old_bytes is not None else None
            ),
            "perfectBefore": perfect,
            "variantReread": use_variants,
            "bestSource": best.source,
            "bestWords": len(best.words),
            "bestScore": round(best.score, 2),
            "selectedTextSha256": selected_text_sha256,
            "replacementCanonicalSha256": _sha256_bytes(new_bytes),
            "decisionInputs": decision_inputs,
            "decisionInputSha256": decision_input_sha256(decision_inputs),
            "aiVisionProvenance": ai_provenance,
            "updatedCanonicalPlanned": updated,
            "updatedCanonical": False,
            "canonicalPublicationStatus": "planned" if updated else "not_required",
            "canonicalPath": _display_path(canonical_path),
            "mergedPath": _display_path(merged_path),
            "decisionReceiptPath": _display_path(receipt_path),
            "recoveryBackupPath": _display_path(recovery_path),
            "recoveryBackupSha256": (
                _sha256_bytes(old_bytes) if old_bytes is not None else None
            ),
            "manualReviewNeeded": manual_needed,
            "engineErrors": engine_errors,
            "preview": best.text[:260],
        }
        audit["slidesProcessed"] += 1
        audit["records"].append(record)
        decisions.append(
            {
                "record": record,
                "slide": slide,
                "best_text": best.text,
                "merged_path": merged_path,
                "receipt_path": receipt_path,
                "canonical_path": canonical_path,
                "recovery_path": recovery_path,
                "old_bytes": old_bytes,
                "new_bytes": new_bytes,
                "updated": updated,
            }
        )
        if args.progress and audit["slidesProcessed"] % args.progress == 0:
            print(
                json.dumps(
                    {
                        "processed": audit["slidesProcessed"],
                        "planned_updates": sum(
                            bool(item["updated"]) for item in decisions
                        ),
                        "at": str(slide.relative_to(ROOT)),
                    }
                )
            )
    if args.internal_eval_log:
        INTERNAL_LOG_DIR.mkdir(parents=True, exist_ok=True)
        internal = {
            "note": "Internal, uncommitted operator/tool comparison log. Manual review entries are a queue for human correction, not public wiki evidence.",
            "generatedAtEpoch": time.time(),
            "toolRun": {
                key: audit[key]
                for key in [
                    "slidesSeen",
                    "slidesProcessed",
                    "slidesSkippedPerfect",
                    "manualReviewNeeded",
                    "engineStatus",
                ]
            },
            "manualQueue": [
                row
                for row in audit["records"]
                if row.get("manualReviewNeeded")
            ][: args.internal_eval_limit],
        }
        path = INTERNAL_LOG_DIR / f"slide-ocr-eval-{int(time.time())}.json"
        atomic_write_bytes(path, _json_bytes(internal))
        audit["internalEvalLog"] = str(path.relative_to(ROOT))
    publish_rapidmerge(audit, decisions, args)
    write_audit_page(audit)
    print(json.dumps({k: audit[k] for k in ["slidesSeen", "slidesProcessed", "canonicalUpdated", "elapsedSeconds"]}, sort_keys=True))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true", help="Process all slide images instead of weak canonical OCR only.")
    parser.add_argument("--limit", type=int, default=0, help="Debug limit over sorted slide images.")
    parser.add_argument("--min-gain", type=float, default=35.0, help="Minimum score gain required before replacing canonical OCR.")
    parser.add_argument("--engine", action="append", default=[], help="OCR engine to use. Repeatable: rapidocr, paddleocr, easyocr, doctr, surya.")
    parser.add_argument("--no-live-ocr", action="store_true", help="Only merge existing OCR directories; do not run live OCR engines.")
    parser.add_argument("--no-rapidocr", dest="no_live_ocr", action="store_true", help="Deprecated alias for --no-live-ocr.")
    parser.add_argument("--enable-surya", action="store_true", help="Enable Surya only after confirming model-weight license terms fit this use.")
    parser.add_argument("--no-variants", action="store_true", help="Disable crop/high-contrast RapidOCR variants.")
    parser.add_argument("--variant-max-old-score", type=float, default=50.0, help="Only run crop/high-contrast variants when the old OCR score is at or below this threshold.")
    parser.add_argument("--deep-variants", action="store_true", help="Try extra crop and threshold variants. Slower but useful for manual rescue passes.")
    parser.add_argument("--skip-perfect", action="store_true", help="When processing all slides, skip OCR blocks that already pass the high-confidence clean-text heuristic.")
    parser.add_argument("--log-manual-queue", action="store_true", help="Mark slides whose best tool output still needs operator/manual review.")
    parser.add_argument("--manual-score-threshold", type=float, default=95.0)
    parser.add_argument("--internal-eval-log", action="store_true", help="Write an ignored internal operator/tool comparison log under .ops/state/cache.")
    parser.add_argument("--internal-eval-limit", type=int, default=200)
    parser.add_argument("--no-backup", dest="backup", action="store_false", help="Do not preserve replaced canonical OCR text.")
    parser.add_argument("--progress", type=int, default=25)
    parser.set_defaults(backup=True)
    return improve(parser.parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
