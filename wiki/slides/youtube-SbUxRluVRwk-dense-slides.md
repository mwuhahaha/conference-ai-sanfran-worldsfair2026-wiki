---
title: "Dense Slides: Structuring a modern AI team — Denys Linkov, Wisedocs"
category: "slides"
video_id: "SbUxRluVRwk"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Structuring a modern AI team — Denys Linkov, Wisedocs

## Source Video
[Structuring a modern AI team — Denys Linkov, Wisedocs](https://www.youtube.com/watch?v=SbUxRluVRwk)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/SbUxRluVRwk/slide-001.jpg]]

- Source scene image: `frame-00004.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `175.92`
- Slide-only rule: `visual-bright-slide`
