---
title: "Dense Slides: Building Cursor Composer – Lee Robinson, Cursor"
category: "slides"
video_id: "fL1iJHtl51Q"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Building Cursor Composer – Lee Robinson, Cursor

## Source Video
[Building Cursor Composer – Lee Robinson, Cursor](https://www.youtube.com/watch?v=fL1iJHtl51Q)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/fL1iJHtl51Q/slide-001.jpg]]

- Source scene image: `frame-00003.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.93`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/fL1iJHtl51Q/slide-002.jpg]]

- Source scene image: `frame-00004.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.61`
- Slide-only rule: `visual-bright-slide`
