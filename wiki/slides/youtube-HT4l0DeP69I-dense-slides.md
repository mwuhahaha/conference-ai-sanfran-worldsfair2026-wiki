---
title: "Dense Slides: Ship it! Building Production Ready Agents — Mike Chambers, AWS"
category: "slides"
video_id: "HT4l0DeP69I"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Ship it! Building Production Ready Agents — Mike Chambers, AWS

## Source Video
[Ship it! Building Production Ready Agents — Mike Chambers, AWS](https://www.youtube.com/watch?v=HT4l0DeP69I)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/HT4l0DeP69I/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/HT4l0DeP69I/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.96`
- Text source: none.
- OCR decision: ready — Dense product UI screenshot with many small labels, tabs, and list items; OCR is better than manual transcription in this triage pass.
- Slide text: not surfaced (`illegible` by AI classifier).
![[assets/dense-slides/HT4l0DeP69I/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/HT4l0DeP69I/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.95`
- Text source: none.
- OCR decision: ready — Dense AWS console screenshot with multiple panels, controls, and small labels; OCR is the efficient read path.
- Slide text: not surfaced (`illegible` by AI classifier).

Classification audit: `raw/sources/slide-ai-classification/dense/HT4l0DeP69I/audit.json`
