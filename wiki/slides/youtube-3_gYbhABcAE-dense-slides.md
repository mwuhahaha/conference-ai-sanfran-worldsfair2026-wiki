---
title: "Dense Slides: Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind"
category: "slides"
video_id: "3_gYbhABcAE"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind

## Source Video
[Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind](https://www.youtube.com/watch?v=3_gYbhABcAE)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/3_gYbhABcAE/slide-001.jpg]]

- Source scene image: `frame-00002.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.36`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/3_gYbhABcAE/slide-002.jpg]]

- Source scene image: `frame-00006.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.4`
- Slide-only rule: `visual-bright-slide`
