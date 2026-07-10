---
title: "Dense Slides: Structuring a modern AI team — Denys Linkov, Wisedocs"
category: "slides"
video_id: "SbUxRluVRwk"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Structuring a modern AI team — Denys Linkov, Wisedocs

## Source Video
[Structuring a modern AI team — Denys Linkov, Wisedocs](https://www.youtube.com/watch?v=SbUxRluVRwk)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/SbUxRluVRwk/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/SbUxRluVRwk/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/border-trim/contrast`.
- OCR decision: ready — Diagram slide with multiple small labels and footer text; OCR is a better fit than manual transcription.

Slide text:

> A spectrum of companies
> AIE Technology Company Verticalized Solution or Services Enabled Tech
> Big Tech, Startup Pa'antir,Wisedocs Big Bank,Large Retaier,SMBs
> AnatomyofanAl Team Evolutionofa Generalist A Question of hiring
> WerdsFar aws


Classification audit: `raw/sources/slide-ai-classification/dense/SbUxRluVRwk/audit.json`
