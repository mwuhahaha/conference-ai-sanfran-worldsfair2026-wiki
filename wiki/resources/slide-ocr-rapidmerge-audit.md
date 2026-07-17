---
title: "Slide OCR RapidMerge Audit"
category: "resources"
sourceLabels: ["Local slide OCR", "RapidOCR", "OCR audit"]
---

# Slide OCR RapidMerge Audit

## What Changed
Weak or suspicious slide OCR is reread with local OCR engines, image crops, and high-contrast variants, then merged against prior OCR sources. Canonical slide OCR is replaced only when the best candidate clears the score-gain threshold.

## Provenance Repair
A historical RapidMerge run affected 601 canonical OCR files using AI-vision output that had no valid cache receipts. The repair restored 599 files from their byte-exact pre-merge backups. The other 2 files already matched their pre-merge backups byte-for-byte, so no content restoration was needed for them. The post-repair check found 0 remaining exact unreceipted copies and 0 ambiguous records.

The old AI-vision cache and both historical audit distributions below are superseded and untrusted. They are retained for auditability, but the current RapidMerge policy accepts 0 results from that run because it recorded 0 current provenance receipts.

## Historical RapidMerge Run (Superseded)
- Slide images seen: 2,870
- Slide OCR records processed: 1,789
- Slides skipped as already clean: 1,020
- Canonical OCR files updated: 601
- Manual review queue entries: 163
- Slide markdown pages refreshed from canonical OCR: 221
- Mode: all
- Elapsed seconds: 2.28
- Audit artifact: `raw/sources/slide-ocr-rapidmerge-audit.json`
- Merge output directory: `raw/sources/slide-ocr-rapidmerge/`
- Canonical backups: `raw/sources/slide-ocr-before-rapidmerge/`

## Best Source Distribution
These are historical selections from the superseded run, not currently accepted sources.

- canonical: 1144
- ai-vision: 619
- rapidocr-prior: 21
- operator-verified: 4
- reconstructed: 1

## Canonical Updates By Source
This is the superseded run's historical update count. The provenance repair described above has removed its unreceipted AI-vision content from canonical OCR.

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
