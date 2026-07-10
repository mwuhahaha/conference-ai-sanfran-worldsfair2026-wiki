---
title: "Dense Slides: LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize"
category: "slides"
video_id: "JsCCrBF7F1g"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize

## Source Video
[LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize](https://www.youtube.com/watch?v=JsCCrBF7F1g)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/JsCCrBF7F1g/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/JsCCrBF7F1g/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast` reconciled by agent.
- OCR decision: ready — Diagram slide with multiple boxed text regions and smaller body copy that is better suited for OCR than manual transcription.

Slide text:

> Observability
> What is happening in my application? Can I root cause down into the problem?
> 
> Evaluation
> How well is the AI product that I've built, actually performing according my criteria?
> 
> Experimentation & Improvement
> The ultimate goal of observability and evaluation is to know where to iterate
> and know where to improve the system


Classification audit: `raw/sources/slide-ai-classification/dense/JsCCrBF7F1g/audit.json`
