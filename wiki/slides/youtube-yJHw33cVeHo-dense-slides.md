---
title: "Dense Slides: From Text to Vision to Voice Exploring Multimodality with Open AI: Romain Huet"
category: "slides"
video_id: "yJHw33cVeHo"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: From Text to Vision to Voice Exploring Multimodality with Open AI: Romain Huet

## Source Video
[From Text to Vision to Voice Exploring Multimodality with Open AI: Romain Huet](https://www.youtube.com/watch?v=yJHw33cVeHo)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/yJHw33cVeHo/slide-001.jpg]]

- Source scene image: `frame-00017.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `175.92`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/yJHw33cVeHo/slide-002.jpg]]

- Source scene image: `frame-00023.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `175.89`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/yJHw33cVeHo/slide-003.jpg]]

- Source scene image: `frame-00024.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.13`
- Slide-only rule: `visual-bright-slide`
