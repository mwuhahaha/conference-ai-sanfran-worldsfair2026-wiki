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
![[assets/dense-slides/C_GG5g38vLU/slide-001.jpg]]

- Source scene image: `frame-00018.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.74`
- Slide-only rule: `visual-bright-slide`
