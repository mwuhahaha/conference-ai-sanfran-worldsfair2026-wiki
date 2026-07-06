---
title: "Dense Slides: From 46% to 90%: Fine-Tuning Tiny LLMs for On-Device Agents — Cormac Brick, Google"
category: "slides"
video_id: "-TiET_K-E_g"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: From 46% to 90%: Fine-Tuning Tiny LLMs for On-Device Agents — Cormac Brick, Google

## Source Video
[From 46% to 90%: Fine-Tuning Tiny LLMs for On-Device Agents — Cormac Brick, Google](https://www.youtube.com/watch?v=-TiET_K-E_g)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/-TiET_K-E_g/slide-001.jpg]]

- Source scene image: `frame-00004.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.56`
- Slide-only rule: `visual-bright-slide`
