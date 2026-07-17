---
title: "Dense Slides: Analyzing 10,000 Sales Calls With AI In 2 Weeks — Charlie Guo"
category: "slides"
video_id: "dvft0Gp9sEE"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Analyzing 10,000 Sales Calls With AI In 2 Weeks — Charlie Guo

## Source Video
[Analyzing 10,000 Sales Calls With AI In 2 Weeks — Charlie Guo](https://www.youtube.com/watch?v=dvft0Gp9sEE)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/dvft0Gp9sEE/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/dvft0Gp9sEE/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/left-72/opencv-adaptive`.
- OCR decision: ready — Dense table text with multiple rows and columns; OCR is better suited than direct transcription.

Slide text:

> Manual Analysis Keyword Analysl
> Quality High" Low.
> Scalability Low: High
> Context Rich: Missing
> Feasibility Impossible Limited

![[assets/dense-slides/dvft0Gp9sEE/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/dvft0Gp9sEE/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.96`
- Text source: agent_vision.

Slide text:

> Your Data Goldmine

Classification audit: `raw/sources/slide-ai-classification/dense/dvft0Gp9sEE/audit.json`
