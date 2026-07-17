---
title: "Dense Slides: The Bitter Layout or: How I Learned to Love the Model Picker — Maximillian Piras, Yutori"
category: "slides"
video_id: "BZtD0yYAgCQ"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: The Bitter Layout or: How I Learned to Love the Model Picker — Maximillian Piras, Yutori

## Source Video
[The Bitter Layout or: How I Learned to Love the Model Picker — Maximillian Piras, Yutori](https://www.youtube.com/watch?v=BZtD0yYAgCQ)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/BZtD0yYAgCQ/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/BZtD0yYAgCQ/slide-001.html)
- AI slide classifier: `other` confidence `0.93`
- Text source: none.
- OCR decision: ready — Dense product UI screenshots and small headings are better handled by OCR than manual transcription in this triage pass.
- Slide text: not surfaced (`illegible` by AI classifier).
![[assets/dense-slides/BZtD0yYAgCQ/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/BZtD0yYAgCQ/slide-002.html)
- AI slide classifier: `other` confidence `0.97`
- Text source: agent_vision.

Slide text:

> “…generative AI systems are grown more than they are built—their internal mechanisms are “emergent” rather than directly designed.”
> Dario Amodei

Classification audit: `raw/sources/slide-ai-classification/dense/BZtD0yYAgCQ/audit.json`
