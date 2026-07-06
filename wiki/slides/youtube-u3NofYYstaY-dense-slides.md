---
title: "Dense Slides: Cohere for VPs of AI: Vivek Muppalla"
category: "slides"
video_id: "u3NofYYstaY"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Cohere for VPs of AI: Vivek Muppalla

## Source Video
[Cohere for VPs of AI: Vivek Muppalla](https://www.youtube.com/watch?v=u3NofYYstaY)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/u3NofYYstaY/slide-001.jpg]]

- Source scene image: `frame-00002.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.74`
- Slide-only rule: `visual-bright-slide`
