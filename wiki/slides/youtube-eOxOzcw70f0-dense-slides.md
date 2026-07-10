---
title: "Dense Slides: Real World Development with GitHub Copilot and VS Code — Harald Kirschner, Christopher Harrison"
category: "slides"
video_id: "eOxOzcw70f0"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Real World Development with GitHub Copilot and VS Code — Harald Kirschner, Christopher Harrison

## Source Video
[Real World Development with GitHub Copilot and VS Code — Harald Kirschner, Christopher Harrison](https://www.youtube.com/watch?v=eOxOzcw70f0)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
No slide-like frames are visible after AI slide classification. Rejected frames remain stored as evidence and are listed below.

### Hidden Non-Slide Evidence
- [`slide-001.jpg`](/assets/dense-slides/eOxOzcw70f0/slide-001.jpg) — `demo_video` confidence `0.97`; Projected computer demo with presenter on stage; not a readable presentation slide.

Classification audit: `raw/sources/slide-ai-classification/dense/eOxOzcw70f0/audit.json`
