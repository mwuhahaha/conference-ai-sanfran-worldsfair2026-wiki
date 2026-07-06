---
title: "Dense Slides: Build & deploy AI-powered apps — Paige Bailey, Google DeepMind"
category: "slides"
video_id: "G_bHFmEAarM"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Build & deploy AI-powered apps — Paige Bailey, Google DeepMind

## Source Video
[Build & deploy AI-powered apps — Paige Bailey, Google DeepMind](https://www.youtube.com/watch?v=G_bHFmEAarM)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/G_bHFmEAarM/slide-001.jpg]]

- Source scene image: `frame-00006.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.17`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/G_bHFmEAarM/slide-002.jpg]]

- Source scene image: `frame-00041.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.29`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/G_bHFmEAarM/slide-003.jpg]]

- Source scene image: `frame-00071.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.81`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/G_bHFmEAarM/slide-004.jpg]]

- Source scene image: `frame-00108.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.73`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/G_bHFmEAarM/slide-005.jpg]]

- Source scene image: `frame-00131.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.27`
- Slide-only rule: `visual-bright-slide`
