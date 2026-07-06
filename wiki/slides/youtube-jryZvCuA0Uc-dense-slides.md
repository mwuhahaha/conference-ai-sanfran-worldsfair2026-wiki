---
title: "Dense Slides: How to look at your data — Jeff Huber (Chroma) + Jason Liu (567)"
category: "slides"
video_id: "jryZvCuA0Uc"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: How to look at your data — Jeff Huber (Chroma) + Jason Liu (567)

## Source Video
[How to look at your data — Jeff Huber (Chroma) + Jason Liu (567)](https://www.youtube.com/watch?v=jryZvCuA0Uc)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/jryZvCuA0Uc/slide-001.jpg]]

- Source scene image: `frame-00002.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.33`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/jryZvCuA0Uc/slide-002.jpg]]

- Source scene image: `frame-00017.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.83`
- Slide-only rule: `visual-bright-slide`
