---
title: "Dense Slides: Can LLMs generate Enterprise Quality Code? — Prasenjit Sarkar, Sonar"
category: "slides"
video_id: "NuePCNMpWGc"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Can LLMs generate Enterprise Quality Code? — Prasenjit Sarkar, Sonar

## Source Video
[Can LLMs generate Enterprise Quality Code? — Prasenjit Sarkar, Sonar](https://www.youtube.com/watch?v=NuePCNMpWGc)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/NuePCNMpWGc/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/NuePCNMpWGc/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Readable content slide with dense quote text and small footer text that OCR should capture better than manual transcription.

Slide text:

> Software engineering has changed for good
> ★ ★ AIE ★ 0 and managing and reviewing their work in 2 months... You're not typing computer code into an editor... that era is over. You're spinning parallel." Co-fouhdur af Optrll, Feurder of turtls Labs up Alagents, giving them tasks *in English* programming has changed due to Alin the last "It's hard to communicate how much I ndr ey Kaetpa thy.
> c2oze, Sararsource Sart
> GoogeDeepMind


Classification audit: `raw/sources/slide-ai-classification/dense/NuePCNMpWGc/audit.json`
