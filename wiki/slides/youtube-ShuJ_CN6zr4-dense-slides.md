---
title: "Dense Slides: Making Codebases Agent Ready – Eno Reyes, Factory AI"
category: "slides"
video_id: "ShuJ_CN6zr4"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Making Codebases Agent Ready – Eno Reyes, Factory AI

## Source Video
[Making Codebases Agent Ready – Eno Reyes, Factory AI](https://www.youtube.com/watch?v=ShuJ_CN6zr4)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/ShuJ_CN6zr4/slide-001.jpg]]

- Source scene image: `frame-00002.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.22`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/ShuJ_CN6zr4/slide-002.jpg]]

- Source scene image: `frame-00003.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.55`
- Slide-only rule: `visual-bright-slide`
