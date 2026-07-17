---
title: "Dense Slides: Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect"
category: "slides"
video_id: "96G7FLab8xc"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect

## Source Video
[Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect](https://www.youtube.com/watch?v=96G7FLab8xc)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/96G7FLab8xc/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/96G7FLab8xc/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.
- OCR decision: ready — Dense embedded article screenshots with small text; OCR will read these more reliably than a quick visual pass.

Slide text:

> Curate ruthlessly

![[assets/dense-slides/96G7FLab8xc/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/96G7FLab8xc/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: agent_vision.
- OCR decision: ready — Dense embedded screenshots and small webpage text are OCR-suitable; the slide title alone is not enough to capture the content.

Slide text:

> Yes, but...

Classification audit: `raw/sources/slide-ai-classification/dense/96G7FLab8xc/audit.json`
