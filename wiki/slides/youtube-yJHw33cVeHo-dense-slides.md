---
title: "Dense Slides: From Text to Vision to Voice Exploring Multimodality with Open AI: Romain Huet"
category: "slides"
video_id: "yJHw33cVeHo"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: From Text to Vision to Voice Exploring Multimodality with Open AI: Romain Huet

## Source Video
[From Text to Vision to Voice Exploring Multimodality with Open AI: Romain Huet](https://www.youtube.com/watch?v=yJHw33cVeHo)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/yJHw33cVeHo/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/yJHw33cVeHo/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.89`
- Text source: agent_vision.

Slide text:

> Hello GPT-4o

### Hidden Non-Slide Evidence
- [`slide-002.jpg`](/assets/dense-slides/yJHw33cVeHo/slide-002.jpg) — `demo_video` confidence `0.16`; Embedded speaker video dominates the frame; no clearly readable presentation slide content.
- [`slide-003.jpg`](/assets/dense-slides/yJHw33cVeHo/slide-003.jpg) — `demo_video` confidence `0.14`; Stage/demo footage with embedded video and sponsor branding; not a readable slide.

Classification audit: `raw/sources/slide-ai-classification/dense/yJHw33cVeHo/audit.json`
