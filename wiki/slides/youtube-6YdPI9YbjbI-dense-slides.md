---
title: "Dense Slides: How to build world-class AI products — Sarah Sachs (AI lead @ Notion) &  Carlos Esteban (Braintrust)"
category: "slides"
video_id: "6YdPI9YbjbI"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: How to build world-class AI products — Sarah Sachs (AI lead @ Notion) &  Carlos Esteban (Braintrust)

## Source Video
[How to build world-class AI products — Sarah Sachs (AI lead @ Notion) &  Carlos Esteban (Braintrust)](https://www.youtube.com/watch?v=6YdPI9YbjbI)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/6YdPI9YbjbI/slide-001.jpg]]

- Source scene image: `frame-00103.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `177.03`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/6YdPI9YbjbI/slide-002.jpg]]

- Source scene image: `frame-00106.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.55`
- Slide-only rule: `visual-bright-slide`
