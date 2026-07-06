---
title: "Dense Slides: From Transcription to Live Music: Gemini's Audio Stack — Thor Schaeff, Google DeepMind"
category: "slides"
video_id: "Bc6Ojl2XS1w"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: From Transcription to Live Music: Gemini's Audio Stack — Thor Schaeff, Google DeepMind

## Source Video
[From Transcription to Live Music: Gemini's Audio Stack — Thor Schaeff, Google DeepMind](https://www.youtube.com/watch?v=Bc6Ojl2XS1w)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/Bc6Ojl2XS1w/slide-001.jpg]]

- Source scene image: `frame-00012.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.66`
- Slide-only rule: `visual-bright-slide`
