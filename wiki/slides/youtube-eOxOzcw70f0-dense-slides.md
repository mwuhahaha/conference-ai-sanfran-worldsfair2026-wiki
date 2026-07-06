---
title: "Dense Slides: Real World Development with GitHub Copilot and VS Code — Harald Kirschner, Christopher Harrison"
category: "slides"
video_id: "eOxOzcw70f0"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Real World Development with GitHub Copilot and VS Code — Harald Kirschner, Christopher Harrison

## Source Video
[Real World Development with GitHub Copilot and VS Code — Harald Kirschner, Christopher Harrison](https://www.youtube.com/watch?v=eOxOzcw70f0)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/eOxOzcw70f0/slide-001.jpg]]

- Source scene image: `frame-00086.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `177.09`
- Slide-only rule: `visual-bright-slide`
