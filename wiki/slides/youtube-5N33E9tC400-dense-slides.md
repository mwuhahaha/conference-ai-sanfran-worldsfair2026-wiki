---
title: "Dense Slides: Why Agent Engineering — swyx"
category: "slides"
video_id: "5N33E9tC400"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Why Agent Engineering — swyx

## Source Video
[Why Agent Engineering — swyx](https://www.youtube.com/watch?v=5N33E9tC400)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/5N33E9tC400/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/5N33E9tC400/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: none.
- OCR decision: ready — Dense transcript screenshot with small body text is better handled by OCR than manual transcription.
![[assets/dense-slides/5N33E9tC400/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/5N33E9tC400/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.94`
- Text source: agent_vision.
- OCR decision: ready — The slide combines screenshots, charts, and small labels that OCR should capture more reliably than a quick visual pass.

Slide text:

> Agent PMF — ChatGPT.com


Classification audit: `raw/sources/slide-ai-classification/dense/5N33E9tC400/audit.json`
