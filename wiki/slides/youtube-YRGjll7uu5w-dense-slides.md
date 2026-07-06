---
title: "Dense Slides: The Web Browser Is All You Need - Paul Klein IV, Browserbase"
category: "slides"
video_id: "YRGjll7uu5w"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: The Web Browser Is All You Need - Paul Klein IV, Browserbase

## Source Video
[The Web Browser Is All You Need - Paul Klein IV, Browserbase](https://www.youtube.com/watch?v=YRGjll7uu5w)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/YRGjll7uu5w/slide-001.jpg]]

- Source scene image: `frame-00002.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `175.89`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/YRGjll7uu5w/slide-002.jpg]]

- Source scene image: `frame-00004.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.63`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/YRGjll7uu5w/slide-003.jpg]]

- Source scene image: `frame-00021.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `175.97`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/YRGjll7uu5w/slide-004.jpg]]

- Source scene image: `frame-00033.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.29`
- Slide-only rule: `visual-bright-slide`
