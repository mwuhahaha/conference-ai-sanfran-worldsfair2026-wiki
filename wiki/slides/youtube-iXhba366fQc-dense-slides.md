---
title: "Dense Slides: Building voice agents with OpenAI — Dominik Kundel, OpenAI"
category: "slides"
video_id: "iXhba366fQc"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Building voice agents with OpenAI — Dominik Kundel, OpenAI

## Source Video
[Building voice agents with OpenAI — Dominik Kundel, OpenAI](https://www.youtube.com/watch?v=iXhba366fQc)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/iXhba366fQc/slide-001.jpg]]

- Source scene image: `frame-00002.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.14`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/iXhba366fQc/slide-002.jpg]]

- Source scene image: `frame-00009.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.43`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/iXhba366fQc/slide-003.jpg]]

- Source scene image: `frame-00031.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `175.92`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/iXhba366fQc/slide-004.jpg]]

- Source scene image: `frame-00092.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `175.95`
- Slide-only rule: `visual-bright-slide`
