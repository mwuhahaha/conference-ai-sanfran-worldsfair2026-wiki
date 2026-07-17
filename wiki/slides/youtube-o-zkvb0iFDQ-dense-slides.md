---
title: "Dense Slides: MCP UI: Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps"
category: "slides"
video_id: "o-zkvb0iFDQ"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: MCP UI: Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps

## Source Video
[MCP UI: Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps](https://www.youtube.com/watch?v=o-zkvb0iFDQ)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/o-zkvb0iFDQ/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/o-zkvb0iFDQ/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.91`
- Text source: agent_vision.
- OCR decision: ready — Dense small text in the projected screenshot plus multiple UI elements; OCR is likely better than manual transcription for the body content.

Slide text:

> Engineering the future of AI

Classification audit: `raw/sources/slide-ai-classification/dense/o-zkvb0iFDQ/audit.json`
