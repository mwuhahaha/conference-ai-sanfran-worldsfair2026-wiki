---
title: "Dense Slides: The Bitter Layout or: How I Learned to Love the Model Picker — Maximillian Piras, Yutori"
category: "slides"
video_id: "BZtD0yYAgCQ"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: The Bitter Layout or: How I Learned to Love the Model Picker — Maximillian Piras, Yutori

## Source Video
[The Bitter Layout or: How I Learned to Love the Model Picker — Maximillian Piras, Yutori](https://www.youtube.com/watch?v=BZtD0yYAgCQ)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/BZtD0yYAgCQ/slide-001.jpg]]

- Source scene image: `frame-00002.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `175.95`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/BZtD0yYAgCQ/slide-002.jpg]]

- Source scene image: `frame-00034.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `178.14`
- Slide-only rule: `visual-bright-slide`
