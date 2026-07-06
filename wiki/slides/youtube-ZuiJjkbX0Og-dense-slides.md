---
title: "Dense Slides: How LLMs work for Web Devs: GPT in 600 lines of Vanilla JS - Ishan Anand"
category: "slides"
video_id: "ZuiJjkbX0Og"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: How LLMs work for Web Devs: GPT in 600 lines of Vanilla JS - Ishan Anand

## Source Video
[How LLMs work for Web Devs: GPT in 600 lines of Vanilla JS - Ishan Anand](https://www.youtube.com/watch?v=ZuiJjkbX0Og)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/ZuiJjkbX0Og/slide-001.jpg]]

- Source scene image: `frame-00002.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.63`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/ZuiJjkbX0Og/slide-002.jpg]]

- Source scene image: `frame-00078.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.96`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/ZuiJjkbX0Og/slide-003.jpg]]

- Source scene image: `frame-00228.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.79`
- Slide-only rule: `visual-bright-slide`
