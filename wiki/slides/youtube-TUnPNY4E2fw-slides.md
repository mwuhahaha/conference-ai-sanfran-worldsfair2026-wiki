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
![[assets/slides/TUnPNY4E2fw/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/TUnPNY4E2fw/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.

Slide text:

> AI Native Cloud
> GPU Clusters
> Model Shaping
> Inference
> Engineering the future of AI

![[assets/slides/TUnPNY4E2fw/slide-003.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/TUnPNY4E2fw/slide-003.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast`.
- OCR decision: ready — dense small screenshot text inside the slide

Slide text:

> Why do we want to long-context training?
> Did the car actuoliy do
> /context
> AIE ContextUsage claude-s0nnet-4-5-20250929.163k/200ktoker
> Autocompact buffer:45.oktokens（22.5%) ONessages: 5.4k tokons (2.7x) 9Systen prompt:2.6k tokons (1.3s) 9Systen too1s:16.2k tokens(7.6%) 9Custon agents:758 tokens (o,4%) )Frec space:37k （18.4%) 9 NCP t001s:94.2kt0kens（47.1%)
> AI Engineer
> EUROPE

![[assets/slides/TUnPNY4E2fw/slide-004.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/TUnPNY4E2fw/slide-004.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.

Slide text:

> What's stopping us?
> Long Context
> O(N^2) Computation
> O(N) Memory

![[assets/slides/TUnPNY4E2fw/slide-005.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/TUnPNY4E2fw/slide-005.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/full`.
- OCR decision: ready — small chart labels and legend are better suited to OCR

Slide text:

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

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/TUnPNY4E2fw/slide-006.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/full`.
- OCR decision: ready — small chart labels and legend are better suited to OCR

Slide text:

> How far can we get?
> AIE Peakmemory(GiB) 80 60 Attn act. Model Other
> 40 OOM (119)
> 20
> Default
> Llama3-8B,3Mtokens,8xH100
> Engineering the future of Al

![[assets/slides/TUnPNY4E2fw/slide-007.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/TUnPNY4E2fw/slide-007.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/full`.
- OCR decision: ready — Diagram slide with many small labels and a citation line; OCR should be more efficient than manual transcription.

Slide text:

> DeepSpeedUlysses
> qo. ko 00
> AIE AII2AII Full FlashAttention AII2AIl 02 01
> q3. k3 03
> Whatifwedividebynum_headsdim?
> DeepSpeed Ulysses:System Optimizations for Enabling Tra sformer Models.Jacobsea.,2023
> Engineering the future of Al

![[assets/slides/TUnPNY4E2fw/slide-008.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/TUnPNY4E2fw/slide-008.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/border-trim/contrast`.
- OCR decision: ready — Chart slide with axis labels, legend, and numeric annotations that are better captured by OCR.

Slide text:

> With Ulysses context parallelism
> 80 Model
> AIE Peak memory (GiB) 60 40 OOM (610) (7684) NOO 00M (964) Attnact. Other
> 20
> 15.0 15.0
> 0 Default FSDP + Ulysses
> Llama 3-8B, 3M tokens, 8xH100
> Engineering the future of Al

![[assets/slides/TUnPNY4E2fw/slide-009.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/TUnPNY4E2fw/slide-009.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: agent_vision.

Slide text:

> What if the activations are still too big?
> 1. Inputs to each Transformer block can't be recomputed quickly
> 2. Still, we can offload to CPU

![[assets/slides/TUnPNY4E2fw/slide-010.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/TUnPNY4E2fw/slide-010.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/center-82/contrast`.
- OCR decision: ready — Diagram-heavy slide with compact labels and small source text; OCR will recover the structure more reliably.

Slide text:

> Untied Ulysses
> Intermediate buffers are too large! (all Q.K.V, x2 because of all-to-all)
> Let's leverage the multi-head aspect of attention:
> AIE Inp-All-to-All Attention H H1 Out-All-to-All
> Attention
> inint QKV All-to-ALl Outo
> (a) Outi
> Unbed Uysses:Memory-EmdontConteatPanllism Va Headwise Chunking.Ghada e al,2026
> Engineering the future of Al

![[assets/slides/TUnPNY4E2fw/slide-011.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/TUnPNY4E2fw/slide-011.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: advanced OCR `rapidocr-live/center-82/contrast`.
- OCR decision: ready — Chart slide with small axes, tick labels, and multiple plotted panels that are OCR-suitable.

Slide text:

> Chunk size ablations
> AIE Memory (GiB) 20 15 Throughput (TpS) 840 830
> 10 820
> 810
> 4 Chunksize 8 16 32 800 4 Chunksiz.e 8 16 32
> UntiedUysses:Memory-Emdont ConteatParallelismva Headwise ChunkingGhadia etal,2026
> Engineering the future of Al

### Hidden Non-Slide Evidence
- [`slide-001.jpg`](/assets/slides/TUnPNY4E2fw/slide-001.jpg) — `speaker_stage` confidence `0.98`; speaker at podium with projected slide; not a clean slide frame
- [`slide-012.jpg`](/assets/slides/TUnPNY4E2fw/slide-012.jpg) — `sponsor_logo` confidence `0.99`; Closing sponsor/logo card; no presentation content to retain.

Classification audit: `raw/sources/slide-ai-classification/slides/TUnPNY4E2fw/audit.json`

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
