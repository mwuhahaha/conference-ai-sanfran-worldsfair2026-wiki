---
title: "Slides: Road to 5 Million Tokens: Breaking Barriers in Long Context Training — Max Ryabinin, Together AI"
category: "slides"
video_id: "TUnPNY4E2fw"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: Road to 5 Million Tokens: Breaking Barriers in Long Context Training — Max Ryabinin, Together AI

## Source Video
[Road to 5 Million Tokens: Breaking Barriers in Long Context Training — Max Ryabinin, Together AI](https://www.youtube.com/watch?v=TUnPNY4E2fw)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/TUnPNY4E2fw/slide-001.jpg]]

OCR text:

> together.ai
> The AI Native Cloud
> Road to 5M
> Sequence Length
> Breaking Memory Barriers in
> Context Parallelism
> Max Ryabinin
> VPRSD,Model Shaping
> AlEngineer
> EUROPE

![[assets/slides/TUnPNY4E2fw/slide-002.jpg]]

OCR text:

> Al Native Cloud
> bd *
> “1. cursor 2 Runware LM aiclol ee COMU Lore A417
> i e ty
> _ ’ Engineering the future of Al

![[assets/slides/TUnPNY4E2fw/slide-003.jpg]]

OCR text:

> Why do we want to long-context training?
> ra ae ne es CY i}
> . * Cee Mey yy)
> — =
> | AlEngineer |
> , 4 a EUROPE

![[assets/slides/TUnPNY4E2fw/slide-004.jpg]]

OCR text:

> What's stopping us?
> Long Context
> . * O(NA2) O(N)
> ra é Computation Memory
> a ad
> | AlEngineer |
> i . : EUROPE

![[assets/slides/TUnPNY4E2fw/slide-005.jpg]]

OCR text:

> What's stopping us?
> Long Context
> aaa a ae
> Ps _- oe
> ‘B88 BES === _ll
> _ 4— : Engineering the future of Al

![[assets/slides/TUnPNY4E2fw/slide-006.jpg]]

OCR text:

> LONE aker- A No 4 1
> 80
> a Model Gi
> . * a a. Attn act. Hi
> * bd 3% Other ==:
> * * QC
> a zo
> 320
> 0” Default
> Llama 3-8B, 3M tokens, 8xH1O0
> a ; |
> ye Engineering the future of Al

![[assets/slides/TUnPNY4E2fw/slide-007.jpg]]

OCR text:

> DeepSpeed Ulysses
> |
> Pein be 7 — 7 0
> aoe “ | a
> ** 7 a  - Full Flash Attention : kt
> What if we divide by num_heads dim?
> _ a Engineering the future of Al

![[assets/slides/TUnPNY4E2fw/slide-008.jpg]]

OCR text:

> With Ulysses context parallelism
> 4 ° Model Gl
> Pe * * PY 2 gq Attn act =
> a [ave] " o” Other ==
> we = oot
> ae E40 i
> 320
> aU
> 0° ‘Default FSDP FSDP
> + Ulysses
> Llama 3-88, 3M tokens, 8xHI1OO
> , ww Engineering the future of Al

![[assets/slides/TUnPNY4E2fw/slide-009.jpg]]

OCR text:

> What if the activations are still too big?
> |. Inputs to each Transformer block can't be recomputed quickly
> he 2. Still, we can offload to CPU
> * *
> Ps * Prefetch before we reach the layer. similar to weights for FSOP
> a " Ps x first implemented in
> * >
> Unsloth Gradient
> Checkpointing - 4x longer
> context windows
> - | AlEngineer |
> ; EUROPE

![[assets/slides/TUnPNY4E2fw/slide-010.jpg]]

OCR text:

> Untied Ulysses
> @ = Intermediate butfers are toa large! (all OK, x2 because of all-to-all)
> 4 e Let's leverage the multi: head aspect of attention
> o— Rages: |§- EB EB SE 3 -s208
> 8-388 —|2- Eh Gap 88— 3 |-asee-
> |
> (RC 7 (a)
> 2100 loome 0 Com
> rv ai Engineering the future of Al

![[assets/slides/TUnPNY4E2fw/slide-011.jpg]]

OCR text:

> Chunk size ablations
> a 20: | 840-
> * - 15; f a0.
> 5g * 9 3
> * E10: $820:
> 5° = 810:
> Ons 16 3200 FON 'g 16 32,
> Chunk size Chunk size
> , = Engineering the future of Al

![[assets/slides/TUnPNY4E2fw/slide-012.jpg]]

OCR text:

> AIEngineer
> EUROPE
> HTTPS://AI.ENGINEER

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
