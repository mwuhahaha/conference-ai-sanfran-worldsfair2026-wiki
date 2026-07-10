---
title: "Dense Slides: How to Build Planning Agents without losing control - Yogendra Miraje, Factset"
category: "slides"
video_id: "sl3icG-IjHo"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: How to Build Planning Agents without losing control - Yogendra Miraje, Factset

## Source Video
[How to Build Planning Agents without losing control - Yogendra Miraje, Factset](https://www.youtube.com/watch?v=sl3icG-IjHo)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/sl3icG-IjHo/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/sl3icG-IjHo/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.

Slide text:

> Why don't Agents behave ?
> LLM messes up
> Unclear or Incomplete Instructions
> Lack of tools or Incorrect usage of tools
> Poorly written input/output contracts
> Missing the right Context
> Limited knowledge of enterprise-specific workflows

![[assets/dense-slides/sl3icG-IjHo/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/sl3icG-IjHo/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: agent_vision.

Slide text:

> Recommended Agentic Architectures
> 1 Plan-and-Solve
> Simple and Sequential multi-step tasks
> 2 ReWOO
> Context Aware, Sequential, Variable-dependent workflows
> 3 LLM Compiler
> Fast, Parallel and Multiple Dependencies


### Hidden Non-Slide Evidence
- [`slide-003.jpg`](/assets/dense-slides/sl3icG-IjHo/slide-003.jpg) — `title_card` confidence `0.99`; closing contact slide with QR codes and logos

Classification audit: `raw/sources/slide-ai-classification/dense/sl3icG-IjHo/audit.json`
