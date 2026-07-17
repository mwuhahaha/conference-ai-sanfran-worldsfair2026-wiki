---
title: "Slide AI Classifier Status"
category: "resources"
status: "quarantined"
sourceLabels: ["Historical AI classifier audits", "Current provenance contract"]
---

# Slide AI Classifier Status

AI-classified slide selections, extracted text, confidence labels, and HTML recreations are public derived artifacts. They are published only when their audit binds the current classifier policy and prompt to the exact source-image bytes and cache configuration.

## Current Validation

- Current classifier publication contract enforcement: active.
- Exact gate configuration and validation receipts: retained in private operator state.
- Historical audits retained: 200.
- Audits satisfying the current contract: 0.
- Historical audits not satisfying the current contract: 200.
- Slide pages with classifier-derived sections withheld: 108.
- Historical accepted-record recreations not published: 1466.
- HTML recreation artifacts removed by quarantine: 1498.

The historical JSON audits remain under `raw/sources/slide-ai-classification/` for provenance and later reprocessing. They are not treated as current evidence, and the original captured slide/frame images remain available on their source layers. Restoring a classifier-derived public section requires a successful rerun under the current contract; changing a version label alone is insufficient.

## Source Boundary

This quarantine does not invalidate official event recordings, captured source images, transcript evidence, or separately labeled OCR. It suppresses only stale AI classifier decisions and the HTML views derived from them.

This page is maintained by `scripts/quarantine_stale_slide_ai.py`.
