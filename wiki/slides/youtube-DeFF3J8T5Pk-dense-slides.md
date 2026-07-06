---
title: "Dense Slides: How fast are LLM inference engines anyway? — Charles Frye, Modal"
category: "slides"
video_id: "DeFF3J8T5Pk"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: How fast are LLM inference engines anyway? — Charles Frye, Modal

## Source Video
[How fast are LLM inference engines anyway? — Charles Frye, Modal](https://www.youtube.com/watch?v=DeFF3J8T5Pk)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/DeFF3J8T5Pk/slide-001.jpg]]

- Source scene image: `frame-00013.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.22`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/DeFF3J8T5Pk/slide-002.jpg]]

- Source scene image: `frame-00017.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.55`
- Slide-only rule: `visual-bright-slide`
