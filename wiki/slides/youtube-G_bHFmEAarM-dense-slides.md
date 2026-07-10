---
title: "Dense Slides: Build & deploy AI-powered apps — Paige Bailey, Google DeepMind"
category: "slides"
video_id: "G_bHFmEAarM"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Build & deploy AI-powered apps — Paige Bailey, Google DeepMind

## Source Video
[Build & deploy AI-powered apps — Paige Bailey, Google DeepMind](https://www.youtube.com/watch?v=G_bHFmEAarM)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/G_bHFmEAarM/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/G_bHFmEAarM/slide-001.html)
- AI slide classifier: `title_card` confidence `0.99`
- Text source: agent_vision.

Slide text:

> Google’s latest releases
> Gemini 3.1 Flash Live
> Gemini 3.1 Pro and Flash-Lite
> NanoBanana 2
> Embeddings 2.0
> Lyria 3
> Genie 3
> AI Studio FSR
> Gemma 4
> Veo 3.1 Lite

![[assets/dense-slides/G_bHFmEAarM/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/G_bHFmEAarM/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.9`
- Text source: agent_vision.
- OCR decision: ready — browser/article screenshot with smaller page text and metadata

Slide text:

> Gemma 4: Byte for byte, the most capable open models

![[assets/dense-slides/G_bHFmEAarM/slide-003.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/G_bHFmEAarM/slide-003.html)
- AI slide classifier: `content_slide` confidence `0.9`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast` reconciled by agent.
- OCR decision: ready — Small screenshot-like slide with embedded UI chrome and compact labels that OCR can read more reliably than manual transcription in this pass.

Slide text:

> GEMINI CAN
> Understand
> text, images,
> audio and more
> 
> Text
> Image
> Audio
> Video
> Coding

![[assets/dense-slides/G_bHFmEAarM/slide-004.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/G_bHFmEAarM/slide-004.html)
- AI slide classifier: `content_slide` confidence `0.89`
- Text source: none.
- OCR decision: ready — Dense code/editor content and small interface labels are better handled by OCR than by manual transcription here.
- Slide text: not surfaced (`none` by AI classifier).
![[assets/dense-slides/G_bHFmEAarM/slide-005.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/G_bHFmEAarM/slide-005.html)
- AI slide classifier: `content_slide` confidence `0.95`
- Text source: agent_vision.

Slide text:

> Create your sound
> Synthesis of professional music from narrative engineering.


Classification audit: `raw/sources/slide-ai-classification/dense/G_bHFmEAarM/audit.json`
