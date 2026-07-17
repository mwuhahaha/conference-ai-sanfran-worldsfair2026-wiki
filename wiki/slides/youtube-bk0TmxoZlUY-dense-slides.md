---
title: "Dense Slides: Evals 101 — Doug Guthrie, Braintrust"
category: "slides"
video_id: "bk0TmxoZlUY"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Evals 101 — Doug Guthrie, Braintrust

## Source Video
[Evals 101 — Doug Guthrie, Braintrust](https://www.youtube.com/watch?v=bk0TmxoZlUY)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/bk0TmxoZlUY/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/bk0TmxoZlUY/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.95`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast`.
- OCR decision: ready — Dense product UI screenshot with many small labels, table columns, and sidebar items.

Slide text:

> Frojecta
> San ach 。
> Generte (hargeog 1 generte·Oa OenerteaCh DougCut
> Uareiawd·Al
> AIE Overview
> G Qatatett
> Fronges
> 1(x0%
> oren
> Ageets
> ?
> PpaTeut
> 010
> braintrust
> g 1
> aws

Classification audit: `raw/sources/slide-ai-classification/dense/bk0TmxoZlUY/audit.json`
