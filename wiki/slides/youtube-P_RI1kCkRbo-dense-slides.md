---
title: "Dense Slides: Voice AI: when is the \"Her\" moment? — Neil Zeghidour, CEO, Gradium AI"
category: "slides"
video_id: "P_RI1kCkRbo"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Voice AI: when is the "Her" moment? — Neil Zeghidour, CEO, Gradium AI

## Source Video
[Voice AI: when is the "Her" moment? — Neil Zeghidour, CEO, Gradium AI](https://www.youtube.com/watch?v=P_RI1kCkRbo)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/P_RI1kCkRbo/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/P_RI1kCkRbo/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.94`
- Text source: agent_vision.
- OCR decision: ready — Product UI screenshot with dense small interface text; OCR will read the sidebar and page controls better than manual transcription.

Slide text:

> Gradient Booking

### Hidden Non-Slide Evidence
- [`slide-002.jpg`](/assets/dense-slides/P_RI1kCkRbo/slide-002.jpg) — `demo_video` confidence `0.93`; Demo screen with speaker camera inset and no readable presentation slide content.

Classification audit: `raw/sources/slide-ai-classification/dense/P_RI1kCkRbo/audit.json`
