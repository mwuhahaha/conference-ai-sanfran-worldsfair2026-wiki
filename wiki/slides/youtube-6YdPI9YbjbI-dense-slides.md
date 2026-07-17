---
title: "Dense Slides: How to build world-class AI products — Sarah Sachs (AI lead @ Notion) &  Carlos Esteban (Braintrust)"
category: "slides"
video_id: "6YdPI9YbjbI"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: How to build world-class AI products — Sarah Sachs (AI lead @ Notion) &  Carlos Esteban (Braintrust)

## Source Video
[How to build world-class AI products — Sarah Sachs (AI lead @ Notion) &  Carlos Esteban (Braintrust)](https://www.youtube.com/watch?v=6YdPI9YbjbI)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/6YdPI9YbjbI/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/6YdPI9YbjbI/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.96`
- Text source: none.
- OCR decision: ready — Dense UI screenshot slide with multiple small text sections and logos; OCR should read the body more reliably than manual transcription in this triage pass.
![[assets/dense-slides/6YdPI9YbjbI/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/6YdPI9YbjbI/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.95`
- Text source: agent_vision.
- OCR decision: ready — Content slide with a clear title, body instruction, and an embedded product UI screenshot containing small readable text.

Slide text:

> Create a Braintrust project

Classification audit: `raw/sources/slide-ai-classification/dense/6YdPI9YbjbI/audit.json`
