---
title: "Dense Slides: Why Agent Engineering — swyx"
category: "slides"
video_id: "5N33E9tC400"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Why Agent Engineering — swyx

## Source Video
[Why Agent Engineering — swyx](https://www.youtube.com/watch?v=5N33E9tC400)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/5N33E9tC400/slide-001.jpg]]

- Source scene image: `frame-00013.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `177.27`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/5N33E9tC400/slide-002.jpg]]

- Source scene image: `frame-00025.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.85`
- Slide-only rule: `visual-bright-slide`
