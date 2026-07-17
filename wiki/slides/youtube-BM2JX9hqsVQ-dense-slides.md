---
title: "Dense Slides: What if the network was the sandbox? — Remy Guercio, Tailscale"
category: "slides"
video_id: "BM2JX9hqsVQ"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: What if the network was the sandbox? — Remy Guercio, Tailscale

## Source Video
[What if the network was the sandbox? — Remy Guercio, Tailscale](https://www.youtube.com/watch?v=BM2JX9hqsVQ)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/BM2JX9hqsVQ/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/BM2JX9hqsVQ/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: agent_vision.
- OCR decision: ready — Contains a readable title plus a dense product UI screenshot with many small labels that OCR should handle better than manual transcription.

Slide text:

> Engineering the future of AI

Classification audit: `raw/sources/slide-ai-classification/dense/BM2JX9hqsVQ/audit.json`
