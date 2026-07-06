---
title: "Dense Slides: MCP UI: Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps"
category: "slides"
video_id: "o-zkvb0iFDQ"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: MCP UI: Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps

## Source Video
[MCP UI: Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps](https://www.youtube.com/watch?v=o-zkvb0iFDQ)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/o-zkvb0iFDQ/slide-001.jpg]]

- Source scene image: `frame-00018.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.47`
- Slide-only rule: `visual-bright-slide`
