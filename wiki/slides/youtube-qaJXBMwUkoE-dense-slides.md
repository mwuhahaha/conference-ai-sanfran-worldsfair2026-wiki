---
title: "Dense Slides: The 1,000x AI Engineer: Swyx"
category: "slides"
video_id: "qaJXBMwUkoE"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: The 1,000x AI Engineer: Swyx

## Source Video
[The 1,000x AI Engineer: Swyx](https://www.youtube.com/watch?v=qaJXBMwUkoE)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/qaJXBMwUkoE/slide-001.jpg]]

- Source scene image: `frame-00021.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.53`
- Slide-only rule: `visual-bright-slide`
