---
title: "Dense Slides: Building Cursor Composer – Lee Robinson, Cursor"
category: "slides"
video_id: "fL1iJHtl51Q"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Building Cursor Composer – Lee Robinson, Cursor

## Source Video
[Building Cursor Composer – Lee Robinson, Cursor](https://www.youtube.com/watch?v=fL1iJHtl51Q)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/fL1iJHtl51Q/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/fL1iJHtl51Q/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast`.
- OCR decision: ready — Dense benchmark chart with small axis labels and multiple text regions; OCR will read this more reliably than direct transcription.

Slide text:

> best-in-class speed Composer combines coding intelligence with
> Best Open
> Fast Frontier
> Frontier7/2025
> Composer
> Best Frontier
> 0 20 40 60 0 100 200
> Composer Intelligence (CursorBench score) Speed (Tokens per Second)
> AIE /CODE BUILDING A FAST FRONTIER MODEL WITH RL
> Google DeepMind PRESENTED8Y LEE ROBINSON /VP, Developer Education CURSOR

![[assets/dense-slides/fL1iJHtl51Q/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/fL1iJHtl51Q/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.

Slide text:

> Why Build Composer? Inspired by Cursor Tab Our aim was a fast, interactive model that is delightful to use. Experiments with Cheetah Prototype fast model in Cursor, quickly became popular.


Classification audit: `raw/sources/slide-ai-classification/dense/fL1iJHtl51Q/audit.json`
