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

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/84Vtz2IL1Ug/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.
- OCR decision: ready — Dense paper screenshot with small multi-column text; OCR will capture details more reliably than manual transcription.

Slide text:

> LLaMA: Open and Efficient Foundation Language Models

![[assets/dense-slides/84Vtz2IL1Ug/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/84Vtz2IL1Ug/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: agent_vision.
- OCR decision: ready — Dense paper-style slide with small body text and embedded screenshot/logo elements; OCR is appropriate.

Slide text:

> Alpaca: A Strong, Replicable Instruction-Following Model

### Hidden Non-Slide Evidence
- [`slide-003.jpg`](/assets/dense-slides/84Vtz2IL1Ug/slide-003.jpg) — `speaker_stage` confidence `0.99`; Stage photo with speaker and projected slide; not a standalone readable slide.

Classification audit: `raw/sources/slide-ai-classification/dense/84Vtz2IL1Ug/audit.json`
