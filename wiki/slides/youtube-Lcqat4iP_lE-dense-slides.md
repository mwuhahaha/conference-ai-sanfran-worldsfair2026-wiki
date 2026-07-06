---
title: "Dense Slides: The State of MCP observability: Observable.tools — Alex Volkov and Benjamin Eckel, W&B and Dylibso"
category: "slides"
video_id: "Lcqat4iP_lE"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: The State of MCP observability: Observable.tools — Alex Volkov and Benjamin Eckel, W&B and Dylibso

## Source Video
[The State of MCP observability: Observable.tools — Alex Volkov and Benjamin Eckel, W&B and Dylibso](https://www.youtube.com/watch?v=Lcqat4iP_lE)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/Lcqat4iP_lE/slide-001.jpg]]

- Source scene image: `frame-00010.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.92`
- Slide-only rule: `visual-bright-slide`
