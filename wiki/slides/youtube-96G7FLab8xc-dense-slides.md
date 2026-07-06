---
title: "Dense Slides: Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect"
category: "slides"
video_id: "96G7FLab8xc"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect

## Source Video
[Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect](https://www.youtube.com/watch?v=96G7FLab8xc)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/96G7FLab8xc/slide-001.jpg]]

- Source scene image: `frame-00090.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.83`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/96G7FLab8xc/slide-002.jpg]]

- Source scene image: `frame-00094.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.64`
- Slide-only rule: `visual-bright-slide`
