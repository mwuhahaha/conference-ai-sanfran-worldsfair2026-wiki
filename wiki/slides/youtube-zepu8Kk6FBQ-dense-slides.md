---
title: "Dense Slides: Agents for Everything Else — swyx"
category: "slides"
video_id: "zepu8Kk6FBQ"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Agents for Everything Else — swyx

## Source Video
[Agents for Everything Else — swyx](https://www.youtube.com/watch?v=zepu8Kk6FBQ)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/zepu8Kk6FBQ/slide-001.jpg]]

- Source scene image: `frame-00005.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `178.2`
- Slide-only rule: `visual-bright-slide`
