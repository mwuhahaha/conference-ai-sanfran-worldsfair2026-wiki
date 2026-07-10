---
title: "Dense Slides: Jack Morris: Stuffing Context is not Memory, Updating Weights is"
category: "slides"
video_id: "Jty4s9-Jb78"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Jack Morris: Stuffing Context is not Memory, Updating Weights is

## Source Video
[Jack Morris: Stuffing Context is not Memory, Updating Weights is](https://www.youtube.com/watch?v=Jty4s9-Jb78)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/Jty4s9-Jb78/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/Jty4s9-Jb78/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.
- OCR decision: ready — Product-style screenshot with dense small on-slide text; OCR will be more reliable than manual transcription for the embedded UI content.

Slide text:

> LLMs have fixed capacity
> but probably know too much

![[assets/dense-slides/Jty4s9-Jb78/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/Jty4s9-Jb78/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: none.
- OCR decision: ready — Dense multi-column academic-paper comparison slide with small body text and citations; OCR is the right extraction path.
![[assets/dense-slides/Jty4s9-Jb78/slide-003.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/Jty4s9-Jb78/slide-003.html)
- AI slide classifier: `content_slide` confidence `0.95`
- Text source: agent_vision.

Slide text:

> ICL
> RAG
> Full Finetune
> LoRA
> Cartridges
> Memory Layers


Classification audit: `raw/sources/slide-ai-classification/dense/Jty4s9-Jb78/audit.json`
