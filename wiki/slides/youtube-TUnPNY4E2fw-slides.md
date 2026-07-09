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

> AI Native Cloud
> Model Builders AppDevelopers
> AIE GPUClusters Model Shaping Inference 紫
> GPUs asa service with accelerated training stack yourtasks Tailloredcustomizationfor The fastest waytolaunch Almodels
> Storage services B200+GB20OLeader Accelerate modeltraining Observability RL(private beta) Fine-tuning+distillation Complete ownership 200+leadingmodels Advancedoptimizations ServerlessandDedicated
> Trusted by: CURSOR Runware hedra Decagon KREA
> Engineering the future of Al

![[assets/slides/TUnPNY4E2fw/slide-003.jpg]]

OCR text:

> Why do we want to long-context training?
> thsr
> /context
> AIE 0990099900 0008000000 0000000000 00000008器 9900000900 Context Usage 06800 00000 Systen tools:15.2k tokens（7.6%） MCP t0o1s:94.2ktokens （47.1%） Custonagents:758 tokens （o.4%） Messages:5.4k tokens （2.7%) Free space:37k（18.4%） Autocompact buffer:45.oktokens （22.5%) claude-s0nnet-4-5-20250929-163k/20ek toke Systen prompt:2.6k tokens （1.3%)
> AIEngineer
> EUROPE

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
> LongContext
> AIE Computation (VN)0) Memory O(N)
> Memory Usage for SBModel
> 160 DP-8 DP=8 Zero-1 OP=8 Zero-2 DP=8Zero-3
> 140 120
> 00
> Seqvence Length Seduence Length Stqvence Length Sequtnce Length 924 16.354
> Engineering the future of Al

![[assets/slides/TUnPNY4E2fw/slide-006.jpg]]

OCR text:

> How far can we get?
> AIE Peakmemory(GiB) 80 60 Attn act. Model Other
> 40 OOM (119)
> 20
> Default
> Llama3-8B,3Mtokens,8xH100
> Engineering the future of Al

![[assets/slides/TUnPNY4E2fw/slide-007.jpg]]

OCR text:

> DeepSpeedUlysses
> qo. ko 00
> AIE AII2AII Full FlashAttention AII2AIl 02 01
> q3. k3 03
> Whatifwedividebynum_headsdim?
> DeepSpeed Ulysses:System Optimizations for Enabling Tra sformer Models.Jacobsea.,2023
> Engineering the future of Al

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

> Chunksizeablations
> AIE Memory(GiB) 15 20 Throughput(TPS) 840 830
> 10 820
> 5 810
> Chunksize 8 16 32 800 Chunk size 8 16 32
> Untied Ulysses:Memory-Eficient Chunking.Ghadia etal.,2026
> Engineering the future of Al

![[assets/slides/TUnPNY4E2fw/slide-012.jpg]]

OCR text:

> AIEngineer
> EUROPE
> HTTPS://AI.ENGINEER

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
