---
title: "Dense Slides: Building Agents at Cloud Scale — Antje Barth, AWS"
category: "slides"
video_id: "WJjInLeaJjo"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Building Agents at Cloud Scale — Antje Barth, AWS

## Source Video
[Building Agents at Cloud Scale — Antje Barth, AWS](https://www.youtube.com/watch?v=WJjInLeaJjo)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/WJjInLeaJjo/slide-001.jpg]]

- Source scene image: `frame-00031.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.91`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/WJjInLeaJjo/slide-002.jpg]]

- Source scene image: `frame-00043.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `177.77`
- Slide-only rule: `visual-bright-slide`
