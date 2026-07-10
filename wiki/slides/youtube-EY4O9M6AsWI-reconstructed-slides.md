---
title: "Reconstructed Slides: Dream Machine: Scaling to 1m users in 4 days — Keegan McCallum, Luma AI"
category: "slides"
video_id: "EY4O9M6AsWI"
sourceLabels: ["Cropped public YouTube video frames", "Local OpenCV slide-region detection", "Local RapidOCR"]
---

# Reconstructed Slides: Dream Machine: Scaling to 1m users in 4 days — Keegan McCallum, Luma AI

## Source Video
[Dream Machine: Scaling to 1m users in 4 days — Keegan McCallum, Luma AI](https://www.youtube.com/watch?v=EY4O9M6AsWI)

## Method
This deck is reconstructed from the existing video frame captures by detecting likely slide regions with OpenCV, cropping/upscaling those regions, deduplicating similar crops, and OCRing the cropped slide images locally. It is a cleaner companion to the full-stage frame deck.

## Reconstructed Slides
![[assets/reconstructed-slides/EY4O9M6AsWI/slide-003.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/reconstructed/EY4O9M6AsWI/slide-003.html)
- AI slide classifier: `content_slide` confidence `0.94`
- Text source: agent_vision.

Slide text:

> AIE
> Luma
> Microsoft
> smol.ai

![[assets/reconstructed-slides/EY4O9M6AsWI/slide-004.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/reconstructed/EY4O9M6AsWI/slide-004.html)
- AI slide classifier: `content_slide` confidence `0.93`
- Text source: none.
- OCR decision: ready — dense embedded social post screenshot with small text
![[assets/reconstructed-slides/EY4O9M6AsWI/slide-005.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/reconstructed/EY4O9M6AsWI/slide-005.html)
- AI slide classifier: `content_slide` confidence `0.94`
- Text source: none.
- OCR decision: ready — dense chat screenshot collage with small text
![[assets/reconstructed-slides/EY4O9M6AsWI/slide-006.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/reconstructed/EY4O9M6AsWI/slide-006.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.

Slide text:

> Luma's mission is to build multimodal general intelligence that can generate, understand, and operate in the physical world

![[assets/reconstructed-slides/EY4O9M6AsWI/slide-009.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/reconstructed/EY4O9M6AsWI/slide-009.html)
- AI slide classifier: `title_card` confidence `0.98`
- Text source: agent_vision.

Slide text:

> Public API
> Check it out at:
> https://lumalabs.ai/api/pricing

![[assets/reconstructed-slides/EY4O9M6AsWI/slide-010.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/reconstructed/EY4O9M6AsWI/slide-010.html)
- AI slide classifier: `content_slide` confidence `0.92`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast` reconciled by agent.
- OCR decision: ready — Dense repeated diagram labels are better handled by OCR than direct transcription.

Slide text:

> AIE
> CPU Worker
> triton-inference-server
> CPU Worker
> triton-inference-server
> CPU Worker
> triton-inference-server
> CPU Worker
> triton-inference-server
> CPU Worker
> triton-inference-server
> CPU Worker
> triton-inference-server
> Luma
> Microsoft
> smol ai

![[assets/reconstructed-slides/EY4O9M6AsWI/slide-011.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/reconstructed/EY4O9M6AsWI/slide-011.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast` reconciled by agent.
- OCR decision: ready — Body bullets are small and dense enough that OCR is the safer extraction path.

Slide text:

> Challenges
> - Brittle, need to coordinate between both CPU and Triton being up at the same time
> - Triton not built for multi-gpu/multi-node
> - Push model not ideal for multi-node (which node has rank 0?)
> - No/limited support for non-nvidia chipsets with Triton
> - Very difficult to develop against
> - Need to have every piece everywhere, hard to bring in disparate compute (i.e. from our training cluster :kekw:)

![[assets/reconstructed-slides/EY4O9M6AsWI/slide-012.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/reconstructed/EY4O9M6AsWI/slide-012.html)
- AI slide classifier: `content_slide` confidence `0.91`
- Text source: advanced OCR `rapidocr-live/border-trim/contrast` reconciled by agent.
- OCR decision: ready — Dense architecture diagram labels and connectors are better suited to OCR than direct transcription.

Slide text:

> API
> Redis (standby)
> Redis
> Redis (standby)
> GPU Workers
> CPU Workers
> Seaweedfs

![[assets/reconstructed-slides/EY4O9M6AsWI/slide-013.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/reconstructed/EY4O9M6AsWI/slide-013.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.

Slide text:

> Challenges
> - Backpressure
> - Priorities/fair scheduling
> - Handling many different models
> - Handling Bursts

![[assets/reconstructed-slides/EY4O9M6AsWI/slide-014.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/reconstructed/EY4O9M6AsWI/slide-014.html)
- AI slide classifier: `title_card` confidence `0.96`
- Text source: agent_vision.

Slide text:

> Queues, Queues, Queues

![[assets/reconstructed-slides/EY4O9M6AsWI/slide-015.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/reconstructed/EY4O9M6AsWI/slide-015.html)
- AI slide classifier: `title_card` confidence `0.98`
- Text source: agent_vision.

Slide text:

> Model Management

![[assets/reconstructed-slides/EY4O9M6AsWI/slide-016.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/reconstructed/EY4O9M6AsWI/slide-016.html)
- AI slide classifier: `title_card` confidence `0.97`
- Text source: agent_vision.

Slide text:

> THANK YOU


### Hidden Non-Slide Evidence
- [`slide-001.jpg`](/assets/reconstructed-slides/EY4O9M6AsWI/slide-001.jpg) — `sponsor_logo` confidence `0.99`; sponsor logo wall, no presentation content
- [`slide-002.jpg`](/assets/reconstructed-slides/EY4O9M6AsWI/slide-002.jpg) — `speaker_stage` confidence `0.98`; speaker on stage, not a slide
- [`slide-007.jpg`](/assets/reconstructed-slides/EY4O9M6AsWI/slide-007.jpg) — `demo_video` confidence `0.99`; embedded video footage, not a presentation slide
- [`slide-008.jpg`](/assets/reconstructed-slides/EY4O9M6AsWI/slide-008.jpg) — `demo_video` confidence `0.99`; embedded video footage, not a presentation slide
- [`slide-017.jpg`](/assets/reconstructed-slides/EY4O9M6AsWI/slide-017.jpg) — `speaker_stage` confidence `0.99`; Camera shot of speaker, audience, and projected screen; not a presentation slide.

Classification audit: `raw/sources/slide-ai-classification/reconstructed/EY4O9M6AsWI/audit.json`
