---
title: "Dense Slides: AI Red Teaming Agent: Azure AI Foundry — Nagkumar Arkalgud & Keiji Kanazawa, Microsoft"
category: "slides"
video_id: "JhJKgRAmfIU"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: AI Red Teaming Agent: Azure AI Foundry — Nagkumar Arkalgud & Keiji Kanazawa, Microsoft

## Source Video
[AI Red Teaming Agent: Azure AI Foundry — Nagkumar Arkalgud & Keiji Kanazawa, Microsoft](https://www.youtube.com/watch?v=JhJKgRAmfIU)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/JhJKgRAmfIU/slide-001.jpg]]

- Source scene image: `frame-00003.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.62`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/JhJKgRAmfIU/slide-002.jpg]]

- Source scene image: `frame-00006.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `175.9`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/JhJKgRAmfIU/slide-003.jpg]]

- Source scene image: `frame-00009.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.24`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/JhJKgRAmfIU/slide-004.jpg]]

- Source scene image: `frame-00015.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.42`
- Slide-only rule: `visual-bright-slide`
