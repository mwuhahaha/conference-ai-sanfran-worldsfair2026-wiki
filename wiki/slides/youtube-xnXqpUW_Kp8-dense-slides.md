---
title: "Dense Slides: Building a Smarter AI Agent with Neural RAG - Will Bryk, Exa.ai"
category: "slides"
video_id: "xnXqpUW_Kp8"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Building a Smarter AI Agent with Neural RAG - Will Bryk, Exa.ai

## Source Video
[Building a Smarter AI Agent with Neural RAG - Will Bryk, Exa.ai](https://www.youtube.com/watch?v=xnXqpUW_Kp8)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/xnXqpUW_Kp8/slide-001.jpg]]

- Source scene image: `frame-00002.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.0`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/xnXqpUW_Kp8/slide-002.jpg]]

- Source scene image: `frame-00019.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.41`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/xnXqpUW_Kp8/slide-003.jpg]]

- Source scene image: `frame-00029.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.45`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/xnXqpUW_Kp8/slide-004.jpg]]

- Source scene image: `frame-00037.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.93`
- Slide-only rule: `visual-bright-slide`
