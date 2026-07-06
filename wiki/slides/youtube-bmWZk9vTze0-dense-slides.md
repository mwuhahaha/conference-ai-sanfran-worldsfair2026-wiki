---
title: "Dense Slides: MCP is all you need — Samuel Colvin, Pydantic"
category: "slides"
video_id: "bmWZk9vTze0"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: MCP is all you need — Samuel Colvin, Pydantic

## Source Video
[MCP is all you need — Samuel Colvin, Pydantic](https://www.youtube.com/watch?v=bmWZk9vTze0)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/bmWZk9vTze0/slide-001.jpg]]

- Source scene image: `frame-00033.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `177.44`
- Slide-only rule: `visual-bright-slide`
