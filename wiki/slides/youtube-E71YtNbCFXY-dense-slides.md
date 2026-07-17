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

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/E71YtNbCFXY/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.

Slide text:

> 500 milliseconds is a typical voice-to-voice latency during a human conversation

Classification audit: `raw/sources/slide-ai-classification/dense/E71YtNbCFXY/audit.json`
