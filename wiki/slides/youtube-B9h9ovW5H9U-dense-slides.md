---
title: "Dense Slides: Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j"
category: "slides"
video_id: "B9h9ovW5H9U"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j

## Source Video
[Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j](https://www.youtube.com/watch?v=B9h9ovW5H9U)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/B9h9ovW5H9U/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/B9h9ovW5H9U/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: agent_vision.
- OCR decision: ready — Dense small UI text and diagram labels make this suitable for OCR; only the main title is directly readable.

Slide text:

> Engineering the future of AI

Classification audit: `raw/sources/slide-ai-classification/dense/B9h9ovW5H9U/audit.json`
