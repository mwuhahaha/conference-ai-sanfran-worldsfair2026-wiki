---
title: "Dense Slides: From 46% to 90%: Fine-Tuning Tiny LLMs for On-Device Agents — Cormac Brick, Google"
category: "slides"
video_id: "-TiET_K-E_g"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: From 46% to 90%: Fine-Tuning Tiny LLMs for On-Device Agents — Cormac Brick, Google

## Source Video
[From 46% to 90%: Fine-Tuning Tiny LLMs for On-Device Agents — Cormac Brick, Google](https://www.youtube.com/watch?v=-TiET_K-E_g)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/-TiET_K-E_g/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/-TiET_K-E_g/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/border-trim/contrast` reconciled by agent.
- OCR decision: ready — Dense small text in four cards; OCR is likely more accurate than manual triage.

Slide text:

> Running AI on the Edge has many benefits
> 
> Latency / UX
> Faster, no network involved
> 
> Privacy
> Sensitive data not sent off device
> 
> Offline use
> Works without requiring cellular
> 
> Savings
> Lower or no data-center costs
> 
> AI Engineer EUROPE

Classification audit: `raw/sources/slide-ai-classification/dense/-TiET_K-E_g/audit.json`
