---
title: "Dense Slides: How to Build Planning Agents without losing control - Yogendra Miraje, Factset"
category: "slides"
video_id: "sl3icG-IjHo"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: How to Build Planning Agents without losing control - Yogendra Miraje, Factset

## Source Video
[How to Build Planning Agents without losing control - Yogendra Miraje, Factset](https://www.youtube.com/watch?v=sl3icG-IjHo)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/sl3icG-IjHo/slide-001.jpg]]

- Source scene image: `frame-00003.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `175.92`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/sl3icG-IjHo/slide-002.jpg]]

- Source scene image: `frame-00013.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.31`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/sl3icG-IjHo/slide-003.jpg]]

- Source scene image: `frame-00034.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.62`
- Slide-only rule: `visual-bright-slide`
