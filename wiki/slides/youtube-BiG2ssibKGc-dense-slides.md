---
title: "Dense Slides: Stop babysitting your agents... — Brandon Waselnuk, Unblocked"
category: "slides"
video_id: "BiG2ssibKGc"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Stop babysitting your agents... — Brandon Waselnuk, Unblocked

## Source Video
[Stop babysitting your agents... — Brandon Waselnuk, Unblocked](https://www.youtube.com/watch?v=BiG2ssibKGc)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/BiG2ssibKGc/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/BiG2ssibKGc/slide-001.html)
- AI slide classifier: `title_card` confidence `0.94`
- Text source: agent_vision.

Slide text:

> CONTEXT ENGINEERING
> Stop babysitting your agents: building a context engine for mergeable code
> Brandon Waselnuk
> Unblocked | getunblocked.com
> AIE Europe 2026

Classification audit: `raw/sources/slide-ai-classification/dense/BiG2ssibKGc/audit.json`
