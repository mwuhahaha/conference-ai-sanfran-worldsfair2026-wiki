---
title: "Dense Slides: Stop babysitting your agents... — Brandon Waselnuk, Unblocked"
category: "slides"
video_id: "BiG2ssibKGc"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Stop babysitting your agents... — Brandon Waselnuk, Unblocked

## Source Video
[Stop babysitting your agents... — Brandon Waselnuk, Unblocked](https://www.youtube.com/watch?v=BiG2ssibKGc)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/BiG2ssibKGc/slide-001.jpg]]

- Source scene image: `frame-00002.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.28`
- Slide-only rule: `visual-bright-slide`
