---
title: "Dense Slides: Run Frontier AI at Home — Alex Cheema, EXO Labs"
category: "slides"
video_id: "ESbWpPT_9-o"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Run Frontier AI at Home — Alex Cheema, EXO Labs

## Source Video
[Run Frontier AI at Home — Alex Cheema, EXO Labs](https://www.youtube.com/watch?v=ESbWpPT_9-o)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/ESbWpPT_9-o/slide-001.jpg]]

- Source scene image: `frame-00028.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.44`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/ESbWpPT_9-o/slide-002.jpg]]

- Source scene image: `frame-00038.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `177.78`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/ESbWpPT_9-o/slide-003.jpg]]

- Source scene image: `frame-00041.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.05`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/ESbWpPT_9-o/slide-004.jpg]]

- Source scene image: `frame-00137.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.6`
- Slide-only rule: `visual-bright-slide`
