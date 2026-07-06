---
title: "Dense Slides: Why Can't Anyone Answer Questions About the Business? — Garrett Galow, WorkOS"
category: "slides"
video_id: "iUWwcG-C8OU"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Why Can't Anyone Answer Questions About the Business? — Garrett Galow, WorkOS

## Source Video
[Why Can't Anyone Answer Questions About the Business? — Garrett Galow, WorkOS](https://www.youtube.com/watch?v=iUWwcG-C8OU)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/iUWwcG-C8OU/slide-001.jpg]]

- Source scene image: `frame-00002.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.45`
- Slide-only rule: `visual-bright-slide`
