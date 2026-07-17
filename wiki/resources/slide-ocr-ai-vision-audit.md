---
title: "Slide AI Vision Rescue Audit"
category: "resources"
sourceLabels: ["AI vision", "Slide OCR", "OCR audit"]
---

# Slide AI Vision Rescue Audit

## Current Trust Status
The AI-vision cache and audit below are from a superseded historical run and are not trusted current evidence. That run recorded no current cache receipts, so the current RapidMerge policy accepts 0 of its AI-vision results.

- Historical unreceipted canonical updates affected: 601
- Canonical files restored from byte-exact pre-merge backups: 599
- Files already matching their pre-merge backups: 2
- Current provenance receipts recorded by the historical run: 0
- Historical AI-vision results accepted by current RapidMerge policy: 0

The cached text remains only as historical review material. It must not be reused or merged unless a new image-, prompt-, model-, policy-, and output-bound receipt passes the current validator.

## Historical AI Vision Run (Superseded)
- Provider: codex-cli
- Model: gpt-5.4-mini
- Slides queued: 781
- Slides attempted: 515
- Existing AI vision files reused: 266
- AI vision text files written: 385
- AI vision text files available: 651
- Output directory: `raw/sources/slide-ocr-ai-vision/`

## Notes
- The historical counts above are retained for auditability; they do not represent accepted current OCR evidence.
- Vision interpretation remains downstream of OCR: OCR identifies weak frames, and vision reads the actual image only for low-confidence cases.
- Current AI-vision text is eligible for comparison only when its cache receipt validates against the exact image bytes, OCR input, prompt, model, policy, and output. Unreceipted files are rejected.
- A newly validated AI-vision candidate may be considered by `scripts/improve_slide_ocr_rapidmerge.py`; the superseded cache documented here is not eligible.
