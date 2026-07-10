---
title: "Dense Slides: How fast are LLM inference engines anyway? — Charles Frye, Modal"
category: "slides"
video_id: "DeFF3J8T5Pk"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: How fast are LLM inference engines anyway? — Charles Frye, Modal

## Source Video
[How fast are LLM inference engines anyway? — Charles Frye, Modal](https://www.youtube.com/watch?v=DeFF3J8T5Pk)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/DeFF3J8T5Pk/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/DeFF3J8T5Pk/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: none.
- OCR decision: ready — Dense product/UI screenshot with chart, small labels, and configuration text; OCR is better than manual transcription.
- Slide text: not surfaced (`illegible` by AI classifier).
![[assets/dense-slides/DeFF3J8T5Pk/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/DeFF3J8T5Pk/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.
- OCR decision: ready — Dense product/UI screenshot with chart, controls, and small configuration text; OCR is better than manual transcription.

Slide text:

> LLM Engine Advisor


Classification audit: `raw/sources/slide-ai-classification/dense/DeFF3J8T5Pk/audit.json`
