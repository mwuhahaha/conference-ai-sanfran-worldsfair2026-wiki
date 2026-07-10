---
title: "Dense Slides: Your Agent Failed in Prod. Good Luck Reproducing It. - Tisha Chawla & Susheem Koul, Microsoft"
category: "slides"
video_id: "Lc8zRh9muoY"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Your Agent Failed in Prod. Good Luck Reproducing It. - Tisha Chawla & Susheem Koul, Microsoft

## Source Video
[Your Agent Failed in Prod. Good Luck Reproducing It. - Tisha Chawla & Susheem Koul, Microsoft](https://www.youtube.com/watch?v=Lc8zRh9muoY)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/Lc8zRh9muoY/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/Lc8zRh9muoY/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/center-82/opencv-adaptive`.
- OCR decision: ready — Dense multi-line instructional slide with small text and equations; OCR will be more reliable than manual transcription.

Slide text:

> sampling determinism. ≠ system determinism
> cemp O fixes the rule (argmax), not the logits.you argmax over.
> reorder a reduction - a logit's last bits move - argmax flips.. (0.1 + 1e20) - 1e20 = 0 float addition is Nor associative: I'o = (ozar - ozar) + r'o
> same matmul, same GPU, 1oo0x → bitwise identical. Orod batches you with strangers; the kernel depends on batch shape. the culprit is batch invariance
> MoE routing jitter: expert capacity ceiling, route depends on the batch..
> same token? no. we need the SYSTEM to run the
> STATE TRANSITION.

![[assets/dense-slides/Lc8zRh9muoY/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/Lc8zRh9muoY/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Two-column comparison slide with small body text and multiple lines; OCR is appropriate.

Slide text:

> X Wrong question: can we make the model deterministic.
> right question: can we debug & test a run we can't reproduce.
> determinism was never the goal. record the run, replay the recording.
> ='controllability bitwise determinism ='observability replayability.
> : same input - Identical output.: randomness makes the model good.: you won't get it from a hosted APl, and you don't want it: that. reconstruct a run that happened, need determinism, you need. the run recorded.. well enough to debug. you don't

![[assets/dense-slides/Lc8zRh9muoY/slide-003.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/Lc8zRh9muoY/slide-003.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Text-heavy comparison slide with small footer text and multiple boxes; OCR is better for accurate capture.

Slide text:

> record above the wire, not on it.
> X. at the network layer. I at the boundary
> the network: local retrieval,: in-process tools, memory. half your agent never touches: and what leaves it, every I/0, capture what enters each node network or not..
> : the socket can't record what isn't on it. not the packets. the meaning of each step.
> Openlnference Arize Phoenix · LangGraph checkpointers · framework-agnostic tracing records it. replay re-runs it offline: stub the model, O calls..

![[assets/dense-slides/Lc8zRh9muoY/slide-005.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/Lc8zRh9muoY/slide-005.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Comparison slide with small body copy in two columns; OCR is appropriate.

Slide text:

> two kinds of check.
> deterministic behavioural:
> control flow · guardralls prompt / wording'changes
> : a fixture. Let the tool be called with qty 1000 never calls the model. rerunnable & free. again, but this time assert on the tool output: freeze the recorded context as did it stay grounded? did it: score it: assert fields / LiM-judge. replay the scenario, score' MEANING not bytes:: refuse the destructive call?

![[assets/dense-slides/Lc8zRh9muoY/slide-006.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/Lc8zRh9muoY/slide-006.html)
- AI slide classifier: `title_card` confidence `0.96`
- Text source: agent_vision.

Slide text:

> code + writeup


### Hidden Non-Slide Evidence
- [`slide-004.jpg`](/assets/dense-slides/Lc8zRh9muoY/slide-004.jpg) — `demo_video` confidence `0.97`; Screen recording of a slide editor with presenter webcam; not a readable presentation slide.

Classification audit: `raw/sources/slide-ai-classification/dense/Lc8zRh9muoY/audit.json`
