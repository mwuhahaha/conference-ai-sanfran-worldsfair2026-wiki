---
title: "Dense Slides: Ship it! Building Production Ready Agents — Mike Chambers, AWS"
category: "slides"
video_id: "HT4l0DeP69I"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Ship it! Building Production Ready Agents — Mike Chambers, AWS

## Source Video
[Ship it! Building Production Ready Agents — Mike Chambers, AWS](https://www.youtube.com/watch?v=HT4l0DeP69I)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/HT4l0DeP69I/slide-001.jpg]]

- Source scene image: `frame-00030.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.75`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/HT4l0DeP69I/slide-002.jpg]]

- Source scene image: `frame-00031.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.99`
- Slide-only rule: `visual-bright-slide`
