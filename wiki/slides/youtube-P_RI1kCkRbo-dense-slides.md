---
title: "Dense Slides: Voice AI: when is the \"Her\" moment? — Neil Zeghidour, CEO, Gradium AI"
category: "slides"
video_id: "P_RI1kCkRbo"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Voice AI: when is the "Her" moment? — Neil Zeghidour, CEO, Gradium AI

## Source Video
[Voice AI: when is the "Her" moment? — Neil Zeghidour, CEO, Gradium AI](https://www.youtube.com/watch?v=P_RI1kCkRbo)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/P_RI1kCkRbo/slide-001.jpg]]

- Source scene image: `frame-00020.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `177.22`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/P_RI1kCkRbo/slide-002.jpg]]

- Source scene image: `frame-00027.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `175.95`
- Slide-only rule: `visual-bright-slide`
