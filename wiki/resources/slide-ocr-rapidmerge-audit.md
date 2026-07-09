---
title: "Slide OCR RapidMerge Audit"
category: "resources"
sourceLabels: ["Local slide OCR", "RapidOCR", "OCR audit"]
---

# Slide OCR RapidMerge Audit

## What Changed
Weak slide OCR was reread with local RapidOCR/ONNX Runtime and merged against prior OCR sources. The merge tool compares canonical Tesseract output, prior RapidOCR output, reconstructed-slide OCR, dense-slide OCR, and live RapidOCR rereads. Canonical slide OCR is replaced only when the best candidate clears the score-gain threshold.

## Latest Run
- Slide images seen: 2,823
- Weak slide OCR records processed: 646
- Canonical OCR files updated: 121
- Slide markdown pages refreshed from canonical OCR: 199
- Audit artifact: `raw/sources/slide-ocr-rapidmerge-audit.json`
- Merge output directory: `raw/sources/slide-ocr-rapidmerge/`
- Canonical backups: `raw/sources/slide-ocr-before-rapidmerge/`

## Tooling Notes
- `scripts/improve_slide_ocr_rapidmerge.py` performs weak-slide detection, RapidOCR rereads, source scoring, canonical replacement, and audit writing.
- `scripts/refresh_slide_pages_from_ocr.py` republishes canonical OCR text into `wiki/slides/*-slides.md`.

## Source Rationale
- RapidOCR was already available locally through `rapidocr_onnxruntime`, so this pass avoided a heavier PaddlePaddle install while still using a modern OCR family suited to scene text.
- Tesseract remains useful where it already produced better spaced text; the merge scorer does not blindly replace good existing OCR with denser but glued OCR.
