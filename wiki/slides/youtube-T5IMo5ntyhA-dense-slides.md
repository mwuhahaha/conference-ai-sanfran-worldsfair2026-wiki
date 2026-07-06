---
title: "Dense Slides: Stop Using RAG as Memory — Daniel Chalef, Zep"
category: "slides"
video_id: "T5IMo5ntyhA"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Stop Using RAG as Memory — Daniel Chalef, Zep

## Source Video
[Stop Using RAG as Memory — Daniel Chalef, Zep](https://www.youtube.com/watch?v=T5IMo5ntyhA)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/T5IMo5ntyhA/slide-001.jpg]]

- Source scene image: `frame-00004.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.55`
- Slide-only rule: `visual-bright-slide`
