---
title: "Slide OCR RapidMerge Audit"
category: "resources"
sourceLabels: ["Local slide OCR", "RapidOCR", "OCR audit"]
---

# Slide OCR RapidMerge Audit

## What Changed
Weak or suspicious slide OCR is reread with local OCR engines, image crops, and high-contrast variants, then merged against prior OCR sources. Canonical slide OCR is replaced only when the best candidate clears the score-gain threshold.

## Latest Run
- Slide images seen: 2,823
- Slide OCR records processed: 708
- Canonical OCR files updated: 30
- Slide markdown pages refreshed from canonical OCR: 199
- Mode: weak-only
- Elapsed seconds: 1626.27
- Audit artifact: `raw/sources/slide-ocr-rapidmerge-audit.json`
- Merge output directory: `raw/sources/slide-ocr-rapidmerge/`
- Canonical backups: `raw/sources/slide-ocr-before-rapidmerge/`

## Best Source Distribution
- canonical: 500
- rapidocr-live/full: 91
- rapidocr-prior: 64
- rapidocr-live/bright-screen/contrast: 30
- rapidocr-live/right-72/contrast: 10
- rapidocr-live/left-72/contrast: 5
- rapidocr-live/center-82/contrast: 4
- rapidocr-live/border-trim/contrast: 3
- reconstructed: 1

## Canonical Updates By Source
- rapidocr-live/bright-screen/contrast: 14
- rapidocr-live/full: 6
- rapidocr-live/right-72/contrast: 4
- rapidocr-live/border-trim/contrast: 3
- rapidocr-live/left-72/contrast: 3

## Tooling Notes
- `scripts/improve_slide_ocr_rapidmerge.py` performs weak-slide detection, crop/variant generation, RapidOCR rereads, source scoring, canonical replacement, and audit writing.
- `scripts/run_slide_ocr_pipeline.py` runs the improvement pass, refreshes slide markdown, regenerates tool/topic surfaces that depend on slide text, and rebuilds the static site.
- Optional heavier OCR engines such as PaddleOCR or Surya should be added as additional candidate sources when installed; this repository keeps RapidOCR as the default local path because it is already available and runs offline.

## Source Rationale
- PaddleOCR and Surya are stronger candidates for future layout-aware OCR, but they are heavier dependencies than the current local environment provides.
- Tesseract documentation emphasizes that OCR quality depends heavily on preprocessing, cropping, border handling, and skew/segmentation quality; this pass therefore improves frame preparation instead of only swapping recognizers.
- RapidOCR remains useful for scene text from video frames, while the merge scorer avoids blindly replacing cleaner Tesseract text with denser but glued text.
