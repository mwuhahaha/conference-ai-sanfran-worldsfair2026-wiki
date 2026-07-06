---
title: "Dense Slides: Building AI Agents that actually automate Knowledge Work - Jerry Liu, LlamaIndex"
category: "slides"
video_id: "jVGCulhBRZI"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Building AI Agents that actually automate Knowledge Work - Jerry Liu, LlamaIndex

## Source Video
[Building AI Agents that actually automate Knowledge Work - Jerry Liu, LlamaIndex](https://www.youtube.com/watch?v=jVGCulhBRZI)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/jVGCulhBRZI/slide-001.jpg]]

- Source scene image: `frame-00002.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.6`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/jVGCulhBRZI/slide-002.jpg]]

- Source scene image: `frame-00003.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.32`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/jVGCulhBRZI/slide-003.jpg]]

- Source scene image: `frame-00022.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.6`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/jVGCulhBRZI/slide-004.jpg]]

- Source scene image: `frame-00034.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.17`
- Slide-only rule: `visual-bright-slide`
