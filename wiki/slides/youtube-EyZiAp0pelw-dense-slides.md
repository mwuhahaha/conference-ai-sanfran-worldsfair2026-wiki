---
title: "Dense Slides: Letting AI Interface with your App with MCP — Kent C Dodds"
category: "slides"
video_id: "EyZiAp0pelw"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Letting AI Interface with your App with MCP — Kent C Dodds

## Source Video
[Letting AI Interface with your App with MCP — Kent C Dodds](https://www.youtube.com/watch?v=EyZiAp0pelw)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/EyZiAp0pelw/slide-001.jpg]]

- Source scene image: `frame-00009.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.24`
- Slide-only rule: `visual-bright-slide`
