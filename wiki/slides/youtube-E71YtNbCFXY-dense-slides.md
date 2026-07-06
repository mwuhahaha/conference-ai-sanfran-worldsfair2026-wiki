---
title: "Dense Slides: Your realtime AI is ngmi — Sean DuBois (OpenAI), Kwindla Kramer (Daily)"
category: "slides"
video_id: "E71YtNbCFXY"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Your realtime AI is ngmi — Sean DuBois (OpenAI), Kwindla Kramer (Daily)

## Source Video
[Your realtime AI is ngmi — Sean DuBois (OpenAI), Kwindla Kramer (Daily)](https://www.youtube.com/watch?v=E71YtNbCFXY)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/E71YtNbCFXY/slide-001.jpg]]

- Source scene image: `frame-00005.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.42`
- Slide-only rule: `visual-bright-slide`
