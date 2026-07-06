---
title: "Dense Slides: Evals 101 — Doug Guthrie, Braintrust"
category: "slides"
video_id: "bk0TmxoZlUY"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Evals 101 — Doug Guthrie, Braintrust

## Source Video
[Evals 101 — Doug Guthrie, Braintrust](https://www.youtube.com/watch?v=bk0TmxoZlUY)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/bk0TmxoZlUY/slide-001.jpg]]

- Source scene image: `frame-00047.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.18`
- Slide-only rule: `visual-bright-slide`
