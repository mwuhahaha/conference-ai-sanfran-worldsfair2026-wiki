---
title: "Dense Slides: Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind"
category: "slides"
video_id: "3_gYbhABcAE"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind

## Source Video
[Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind](https://www.youtube.com/watch?v=3_gYbhABcAE)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/3_gYbhABcAE/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/3_gYbhABcAE/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: none.
- OCR decision: ready — Diagram slide with multiple small labels and compact text blocks.
![[assets/dense-slides/3_gYbhABcAE/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/3_gYbhABcAE/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.
- OCR decision: ready — Text-heavy slide with bullets and embedded code screenshots.

Slide text:

> Text is the New State
> - The Trap: Treating the real world as enums and booleans because it feels safe.
> - The Collision: Forcing natural language intent into discrete booleans lobotomizes the context.
> - The Fix: Preserve semantic meaning through raw strings so the agent can adapt intelligently downstream.

Classification audit: `raw/sources/slide-ai-classification/dense/3_gYbhABcAE/audit.json`
