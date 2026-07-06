---
title: "Dense Slides: New York Times' Connections: A Case Study on NLP in Word Games — Shafik Quoraishee, NYT Games"
category: "slides"
video_id: "P_uhFGH4J9Y"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: New York Times' Connections: A Case Study on NLP in Word Games — Shafik Quoraishee, NYT Games

## Source Video
[New York Times' Connections: A Case Study on NLP in Word Games — Shafik Quoraishee, NYT Games](https://www.youtube.com/watch?v=P_uhFGH4J9Y)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/P_uhFGH4J9Y/slide-001.jpg]]

- Source scene image: `frame-00002.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.55`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/P_uhFGH4J9Y/slide-002.jpg]]

- Source scene image: `frame-00003.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.16`
- Slide-only rule: `visual-bright-slide`
