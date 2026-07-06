---
title: "Dense Slides: Fun stories from building OpenRouter and where all this is going - Alex Atallah, OpenRouter"
category: "slides"
video_id: "84Vtz2IL1Ug"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Fun stories from building OpenRouter and where all this is going - Alex Atallah, OpenRouter

## Source Video
[Fun stories from building OpenRouter and where all this is going - Alex Atallah, OpenRouter](https://www.youtube.com/watch?v=84Vtz2IL1Ug)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/84Vtz2IL1Ug/slide-001.jpg]]

- Source scene image: `frame-00009.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `177.35`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/84Vtz2IL1Ug/slide-002.jpg]]

- Source scene image: `frame-00012.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.64`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/84Vtz2IL1Ug/slide-003.jpg]]

- Source scene image: `frame-00014.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.71`
- Slide-only rule: `visual-bright-slide`
