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

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/Bc6Ojl2XS1w/slide-001.html)
- AI slide classifier: `demo_video` confidence `0.94`
- Text source: agent_vision.
- OCR decision: ready — Dense UI screenshot with small transcript text and multiple readable headings; OCR is better suited than manual vision transcription for the body copy.

Slide text:

> Engineering the future of AI


Classification audit: `raw/sources/slide-ai-classification/dense/Bc6Ojl2XS1w/audit.json`
