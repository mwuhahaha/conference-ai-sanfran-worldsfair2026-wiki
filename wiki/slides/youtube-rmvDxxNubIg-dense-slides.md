---
title: "Dense Slides: No Vibes Allowed: Solving Hard Problems in Complex Codebases – Dex Horthy, HumanLayer"
category: "slides"
video_id: "rmvDxxNubIg"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: No Vibes Allowed: Solving Hard Problems in Complex Codebases – Dex Horthy, HumanLayer

## Source Video
[No Vibes Allowed: Solving Hard Problems in Complex Codebases – Dex Horthy, HumanLayer](https://www.youtube.com/watch?v=rmvDxxNubIg)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/rmvDxxNubIg/slide-001.jpg]]

- Source scene image: `frame-00004.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `177.23`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/rmvDxxNubIg/slide-002.jpg]]

- Source scene image: `frame-00010.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `178.32`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/rmvDxxNubIg/slide-003.jpg]]

- Source scene image: `frame-00021.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `177.38`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/rmvDxxNubIg/slide-004.jpg]]

- Source scene image: `frame-00022.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `177.47`
- Slide-only rule: `visual-bright-slide`
