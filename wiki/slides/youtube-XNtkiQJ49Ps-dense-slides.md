---
title: "Dense Slides: Agents need more than a chat - Jacob Lauritzen, CTO Legora"
category: "slides"
video_id: "XNtkiQJ49Ps"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Agents need more than a chat - Jacob Lauritzen, CTO Legora

## Source Video
[Agents need more than a chat - Jacob Lauritzen, CTO Legora](https://www.youtube.com/watch?v=XNtkiQJ49Ps)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/XNtkiQJ49Ps/slide-001.jpg]]

- Source scene image: `frame-00002.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `175.98`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/XNtkiQJ49Ps/slide-002.jpg]]

- Source scene image: `frame-00005.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.3`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/XNtkiQJ49Ps/slide-003.jpg]]

- Source scene image: `frame-00007.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.06`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/XNtkiQJ49Ps/slide-004.jpg]]

- Source scene image: `frame-00013.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.19`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/XNtkiQJ49Ps/slide-005.jpg]]

- Source scene image: `frame-00014.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.37`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/XNtkiQJ49Ps/slide-006.jpg]]

- Source scene image: `frame-00019.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.24`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/XNtkiQJ49Ps/slide-007.jpg]]

- Source scene image: `frame-00021.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.44`
- Slide-only rule: `visual-bright-slide`
