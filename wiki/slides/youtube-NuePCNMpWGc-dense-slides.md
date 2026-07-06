---
title: "Dense Slides: Can LLMs generate Enterprise Quality Code? — Prasenjit Sarkar, Sonar"
category: "slides"
video_id: "NuePCNMpWGc"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Can LLMs generate Enterprise Quality Code? — Prasenjit Sarkar, Sonar

## Source Video
[Can LLMs generate Enterprise Quality Code? — Prasenjit Sarkar, Sonar](https://www.youtube.com/watch?v=NuePCNMpWGc)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/NuePCNMpWGc/slide-001.jpg]]

- Source scene image: `frame-00002.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `177.11`
- Slide-only rule: `visual-bright-slide`
