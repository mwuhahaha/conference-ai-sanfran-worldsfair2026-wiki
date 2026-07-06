---
title: "Dense Slides: Building an Agentic Platform — Ben Kus, CTO Box"
category: "slides"
video_id: "12v5S1n1eOY"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Building an Agentic Platform — Ben Kus, CTO Box

## Source Video
[Building an Agentic Platform — Ben Kus, CTO Box](https://www.youtube.com/watch?v=12v5S1n1eOY)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/12v5S1n1eOY/slide-001.jpg]]

- Source scene image: `frame-00002.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.35`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/12v5S1n1eOY/slide-002.jpg]]

- Source scene image: `frame-00005.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.75`
- Slide-only rule: `visual-bright-slide`
