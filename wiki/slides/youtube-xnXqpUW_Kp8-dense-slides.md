---
title: "Dense Slides: Building a Smarter AI Agent with Neural RAG - Will Bryk, Exa.ai"
category: "slides"
video_id: "xnXqpUW_Kp8"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Building a Smarter AI Agent with Neural RAG - Will Bryk, Exa.ai

## Source Video
[Building a Smarter AI Agent with Neural RAG - Will Bryk, Exa.ai](https://www.youtube.com/watch?v=xnXqpUW_Kp8)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/xnXqpUW_Kp8/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/xnXqpUW_Kp8/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: agent_vision.

Slide text:

> One API to get any information from the web

![[assets/dense-slides/xnXqpUW_Kp8/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/xnXqpUW_Kp8/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.96`
- Text source: agent_vision.

Slide text:

> Traditional search engines were built for humans
> Humans want to type simple keywords to click a couple links
> Google built a keyword based algorithm for humans

![[assets/dense-slides/xnXqpUW_Kp8/slide-003.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/xnXqpUW_Kp8/slide-003.html)
- AI slide classifier: `content_slide` confidence `0.94`
- Text source: agent_vision.

Slide text:

> Keyword
> "stripe pricing"
> Semantic
> "People in SF who know assembly"
> Queries no one has thought to
> Pure LLM
> "Explain this concept to me"
> super-complex
> "Find me every article that argues X and not Y from an author like Z"

![[assets/dense-slides/xnXqpUW_Kp8/slide-004.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/xnXqpUW_Kp8/slide-004.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/full`.
- OCR decision: ready — Dense multi-pane product UI and code/JSON text is better handled by OCR than manual transcription.

Slide text:

> Search italley
> frosea_PY rtEa
> a·aa_ey-3614
> AIE D Perult category ech7yoe resltea.seerch_an_cetents( algpt t A" text -Tous
> ng
> fiers
> IncNde texd
> Exclude terl "dsta':（
> Crawling "teprogttringhlogsntovtx". ]
> "teAthtfctle "url"："hstaa//asbatrs/2aca/astficiat-kstallio-zldlon-l.ha pub11ahedDeta12015-01-22714:21:52.0002", "suthar*:*TixUchan, "04*:4.379075484701233, fy fertng
> "fe:tt/.2.s.cboteth/tL
> Ask ExaBet
> "title':
> Microsoft smol

Classification audit: `raw/sources/slide-ai-classification/dense/xnXqpUW_Kp8/audit.json`
