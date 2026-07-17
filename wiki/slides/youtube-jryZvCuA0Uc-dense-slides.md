---
title: "Dense Slides: How to look at your data — Jeff Huber (Chroma) + Jason Liu (567)"
category: "slides"
video_id: "jryZvCuA0Uc"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: How to look at your data — Jeff Huber (Chroma) + Jason Liu (567)

## Source Video
[How to look at your data — Jeff Huber (Chroma) + Jason Liu (567)](https://www.youtube.com/watch?v=jryZvCuA0Uc)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/jryZvCuA0Uc/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/jryZvCuA0Uc/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.95`
- Text source: agent_vision.

Slide text:

> Read the full report
> research.trychroma.com

### Hidden Non-Slide Evidence
- [`slide-001.jpg`](/assets/dense-slides/jryZvCuA0Uc/slide-001.jpg) — `title_card` confidence `0.98`; title card

Classification audit: `raw/sources/slide-ai-classification/dense/jryZvCuA0Uc/audit.json`
