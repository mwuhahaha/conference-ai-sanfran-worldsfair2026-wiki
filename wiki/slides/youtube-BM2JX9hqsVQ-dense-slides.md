---
title: "Dense Slides: What if the network was the sandbox? — Remy Guercio, Tailscale"
category: "slides"
video_id: "BM2JX9hqsVQ"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: What if the network was the sandbox? — Remy Guercio, Tailscale

## Source Video
[What if the network was the sandbox? — Remy Guercio, Tailscale](https://www.youtube.com/watch?v=BM2JX9hqsVQ)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/BM2JX9hqsVQ/slide-001.jpg]]

- Source scene image: `frame-00019.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.15`
- Slide-only rule: `visual-bright-slide`
