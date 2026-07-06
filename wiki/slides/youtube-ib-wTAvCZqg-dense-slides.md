---
title: "Dense Slides: Architecting and Testing Controllable Agents: Lance Martin"
category: "slides"
video_id: "ib-wTAvCZqg"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Architecting and Testing Controllable Agents: Lance Martin

## Source Video
[Architecting and Testing Controllable Agents: Lance Martin](https://www.youtube.com/watch?v=ib-wTAvCZqg)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/ib-wTAvCZqg/slide-001.jpg]]

- Source scene image: `frame-00008.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.01`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/ib-wTAvCZqg/slide-002.jpg]]

- Source scene image: `frame-00063.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.42`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/ib-wTAvCZqg/slide-003.jpg]]

- Source scene image: `frame-00143.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `177.06`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/ib-wTAvCZqg/slide-004.jpg]]

- Source scene image: `frame-00213.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.51`
- Slide-only rule: `visual-bright-slide`
