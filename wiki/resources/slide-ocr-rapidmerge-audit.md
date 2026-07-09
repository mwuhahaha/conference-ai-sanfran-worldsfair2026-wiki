---
title: "Slide OCR RapidMerge Audit"
category: "resources"
sourceLabels: ["Local slide OCR", "RapidOCR", "OCR audit"]
---

# Slide OCR RapidMerge Audit

## What Changed
Weak or suspicious slide OCR is reread with local OCR engines, image crops, and high-contrast variants, then merged against prior OCR sources. Canonical slide OCR is replaced only when the best candidate clears the score-gain threshold.

## Latest Run
- Slide images seen: 2,870
- Slide OCR records processed: 1,789
- Slides skipped as already clean: 1,020
- Canonical OCR files updated: 601
- Manual review queue entries: 163
- Slide markdown pages refreshed from canonical OCR: 199
- Mode: all
- Elapsed seconds: 2.28
- Audit artifact: `raw/sources/slide-ocr-rapidmerge-audit.json`
- Merge output directory: `raw/sources/slide-ocr-rapidmerge/`
- Canonical backups: `raw/sources/slide-ocr-before-rapidmerge/`

## Best Source Distribution
- canonical: 1144
- ai-vision: 619
- rapidocr-prior: 21
- operator-verified: 4
- reconstructed: 1

## Canonical Updates By Source
- ai-vision: 601

## Engine Status
- Live OCR disabled or no engines selected.

## Tooling Notes
- `scripts/improve_slide_ocr_rapidmerge.py` performs weak-slide detection, crop/variant generation, RapidOCR rereads, source scoring, canonical replacement, and audit writing.
- `scripts/run_slide_ocr_pipeline.py` runs the improvement pass, refreshes slide markdown, regenerates tool/topic surfaces that depend on slide text, and rebuilds the static site.
- Optional heavier OCR engines such as PaddleOCR, EasyOCR, docTR, and Surya are treated as local candidate engines when installed and enabled.

## Source Rationale
- PaddleOCR and Surya are stronger candidates for future layout-aware OCR, but they are heavier dependencies than the current local environment provides.
- Tesseract documentation emphasizes that OCR quality depends heavily on preprocessing, cropping, border handling, and skew/segmentation quality; this pass therefore improves frame preparation instead of only swapping recognizers.
- RapidOCR remains useful for scene text from video frames, while the merge scorer avoids blindly replacing cleaner Tesseract text with denser but glued text.
