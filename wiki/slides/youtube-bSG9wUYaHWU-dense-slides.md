---
title: "Dense Slides: Context Is the New Code — Patrick Debois, Tessl"
category: "slides"
video_id: "bSG9wUYaHWU"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Context Is the New Code — Patrick Debois, Tessl

## Source Video
[Context Is the New Code — Patrick Debois, Tessl](https://www.youtube.com/watch?v=bSG9wUYaHWU)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/bSG9wUYaHWU/slide-001.jpg]]

- Source scene image: `frame-00009.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.39`
- Slide-only rule: `visual-bright-slide`
