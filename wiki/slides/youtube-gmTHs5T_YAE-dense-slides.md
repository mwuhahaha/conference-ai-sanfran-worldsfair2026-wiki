---
title: "Dense Slides: Optimizing inference for voice models in production - Philip Kiely, Baseten"
category: "slides"
video_id: "gmTHs5T_YAE"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Optimizing inference for voice models in production - Philip Kiely, Baseten

## Source Video
[Optimizing inference for voice models in production - Philip Kiely, Baseten](https://www.youtube.com/watch?v=gmTHs5T_YAE)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/gmTHs5T_YAE/slide-001.jpg]]

- Source scene image: `frame-00002.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `177.21`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/gmTHs5T_YAE/slide-002.jpg]]

- Source scene image: `frame-00003.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.35`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/gmTHs5T_YAE/slide-003.jpg]]

- Source scene image: `frame-00007.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `177.28`
- Slide-only rule: `visual-bright-slide`
