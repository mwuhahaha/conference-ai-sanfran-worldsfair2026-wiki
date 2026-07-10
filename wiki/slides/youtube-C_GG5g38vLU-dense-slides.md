---
title: "Dense Slides: Harnesses in AI: A Deep Dive — Tejas Kumar, IBM"
category: "slides"
video_id: "C_GG5g38vLU"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Harnesses in AI: A Deep Dive — Tejas Kumar, IBM

## Source Video
[Harnesses in AI: A Deep Dive — Tejas Kumar, IBM](https://www.youtube.com/watch?v=C_GG5g38vLU)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
No slide-like frames are visible after AI slide classification. Rejected frames remain stored as evidence and are listed below.

### Hidden Non-Slide Evidence
- [`slide-001.jpg`](/assets/dense-slides/C_GG5g38vLU/slide-001.jpg) — `speaker_stage` confidence `0.93`; Stage photo with speaker and auditorium view; the projected screen is visible but this is not a clean slide frame.

Classification audit: `raw/sources/slide-ai-classification/dense/C_GG5g38vLU/audit.json`
