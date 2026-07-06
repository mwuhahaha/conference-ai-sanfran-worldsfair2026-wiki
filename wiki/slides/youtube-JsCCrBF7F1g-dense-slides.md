---
title: "Dense Slides: LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize"
category: "slides"
video_id: "JsCCrBF7F1g"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize

## Source Video
[LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize](https://www.youtube.com/watch?v=JsCCrBF7F1g)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/JsCCrBF7F1g/slide-001.jpg]]

- Source scene image: `frame-00005.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.87`
- Slide-only rule: `visual-bright-slide`
