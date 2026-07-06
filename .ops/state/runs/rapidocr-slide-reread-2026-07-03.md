---
type: run-receipt
scope: project-local
status: complete
created: 2026-07-03T15:25:00+00:00
---

# RapidOCR Slide Reread

## Purpose
Improve weak OCR in extracted slide decks where Tesseract missed projected slide text, especially washed-out or partial stage captures.

## Local OCR Engine
- Installed `rapidocr-onnxruntime` locally with ONNX Runtime and OpenCV.
- No hosted vision API was used because `OPENAI_API_KEY` was not configured.

## Inputs
- Existing slide images: `wiki/assets/slides/*/*.jpg`
- Existing Tesseract OCR: `raw/sources/slide-ocr/*/*.txt`

## Outputs
- RapidOCR candidate text: `raw/sources/slide-ocr-rapidocr/`
- RapidOCR audit: `raw/sources/slide-ocr-rapidocr-audit.json`
- Fast Tesseract reread helper/audit path: `scripts/reread_slide_ocr.py`, `raw/sources/slide-ocr-quality-audit.json`
- Refreshed visible slide markdown OCR blocks via `scripts/refresh_slide_pages_from_ocr.py`

## Counts
- Total slide images: 1842
- Weak slide candidates processed by RapidOCR: 675
- Canonical OCR replacements applied: 291
- Weak frames classified as unreadable/non-slide: 115
- Non-empty canonical OCR files after pass: 1826
- Slide deck markdown pages refreshed: 107
- Reconstructed crop companion decks validated: 107
- Reconstructed slide crop images: 1729

## Logic Updates
- `scripts/extract_video_slides.py` now uses optional RapidOCR fallback when Tesseract output is weak.
- `/garage/obsidian/scripts/native_youtube_slide_scan.py` now uses optional RapidOCR fallback for future native YouTube slide scans.
- `scripts/reconstruct_video_slides.py` now uses unique temporary OCR images during crop reconstruction.
