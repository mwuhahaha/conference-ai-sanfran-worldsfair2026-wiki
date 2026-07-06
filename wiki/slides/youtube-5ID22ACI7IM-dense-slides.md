---
title: "Dense Slides: Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked"
category: "slides"
video_id: "5ID22ACI7IM"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked

## Source Video
[Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked](https://www.youtube.com/watch?v=5ID22ACI7IM)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/5ID22ACI7IM/slide-001.jpg]]

- Source scene image: `frame-00024.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `174.46`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/5ID22ACI7IM/slide-002.jpg]]

- Source scene image: `frame-00037.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `175.97`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/5ID22ACI7IM/slide-003.jpg]]

- Source scene image: `frame-00054.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.83`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/5ID22ACI7IM/slide-004.jpg]]

- Source scene image: `frame-00102.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.33`
- Slide-only rule: `visual-bright-slide`
