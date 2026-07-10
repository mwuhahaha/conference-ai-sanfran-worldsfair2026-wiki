---
title: "Dense Slides: How LLMs work for Web Devs: GPT in 600 lines of Vanilla JS - Ishan Anand"
category: "slides"
video_id: "ZuiJjkbX0Og"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: How LLMs work for Web Devs: GPT in 600 lines of Vanilla JS - Ishan Anand

## Source Video
[How LLMs work for Web Devs: GPT in 600 lines of Vanilla JS - Ishan Anand](https://www.youtube.com/watch?v=ZuiJjkbX0Og)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/ZuiJjkbX0Og/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/ZuiJjkbX0Og/slide-001.html)
- AI slide classifier: `title_card` confidence `0.98`
- Text source: agent_vision.

Slide text:

> HOW LLMS WORK FOR WEB DEVS
> GPT in 600 lines of Vanilla JavaScript
> Ishan Anand
> Spreadsheets-are-all-you-need.ai

![[assets/dense-slides/ZuiJjkbX0Og/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/ZuiJjkbX0Og/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: none.
- OCR decision: ready — dense paper screenshot, small diagram labels, and multi-column technical text are better handled by OCR
![[assets/dense-slides/ZuiJjkbX0Og/slide-003.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/ZuiJjkbX0Og/slide-003.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.

Slide text:

> Spread the word on spreadsheets-are-all-you-need
> Visit Spreadsheets-are-all-you-need.ai
> • Mailing list & YouTube
> • Members/Patrons
>   • Discount on full class, office hours, etc.
> Available for AI consulting
> • Training, Strategy & Implementation


Classification audit: `raw/sources/slide-ai-classification/dense/ZuiJjkbX0Og/audit.json`
