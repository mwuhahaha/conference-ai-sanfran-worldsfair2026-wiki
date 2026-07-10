---
title: "Dense Slides: Building an Agentic Platform — Ben Kus, CTO Box"
category: "slides"
video_id: "12v5S1n1eOY"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Building an Agentic Platform — Ben Kus, CTO Box

## Source Video
[Building an Agentic Platform — Ben Kus, CTO Box](https://www.youtube.com/watch?v=12v5S1n1eOY)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/12v5S1n1eOY/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/12v5S1n1eOY/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.94`
- Text source: agent_vision.

Slide text:

> 67%
> Fortune 500
> 115K
> Total customers

![[assets/dense-slides/12v5S1n1eOY/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/12v5S1n1eOY/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.

Slide text:

> Box has fully integrated generative AI starting in 2023
> Q&A across documents
> Data extraction
> AI-powered workflows


Classification audit: `raw/sources/slide-ai-classification/dense/12v5S1n1eOY/audit.json`
