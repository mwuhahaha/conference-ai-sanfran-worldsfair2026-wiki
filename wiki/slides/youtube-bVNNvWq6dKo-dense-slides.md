---
title: "Dense Slides: How Windsurf writes 90% of your code with an Agentic IDE - Kevin Hou, Windsurf"
category: "slides"
video_id: "bVNNvWq6dKo"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: How Windsurf writes 90% of your code with an Agentic IDE - Kevin Hou, Windsurf

## Source Video
[How Windsurf writes 90% of your code with an Agentic IDE - Kevin Hou, Windsurf](https://www.youtube.com/watch?v=bVNNvWq6dKo)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/bVNNvWq6dKo/slide-001.jpg]]

- Source scene image: `frame-00018.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.26`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/bVNNvWq6dKo/slide-002.jpg]]

- Source scene image: `frame-00025.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.1`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/bVNNvWq6dKo/slide-003.jpg]]

- Source scene image: `frame-00042.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `177.15`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/bVNNvWq6dKo/slide-004.jpg]]

- Source scene image: `frame-00046.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `166.41`
- Slide-only rule: `visual-bright-slide`
