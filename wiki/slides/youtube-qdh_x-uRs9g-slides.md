---
title: "Slides: The Small Model Infrastructure Nobody Built (So We Did) — Filip Makraduli, Superlinked"
category: "slides"
video_id: "qdh_x-uRs9g"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: The Small Model Infrastructure Nobody Built (So We Did) — Filip Makraduli, Superlinked

## Source Video
[The Small Model Infrastructure Nobody Built (So We Did) — Filip Makraduli, Superlinked](https://www.youtube.com/watch?v=qdh_x-uRs9g)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/qdh_x-uRs9g/slide-001.jpg]]

OCR text:

> PLATINUM SPONSORS
> Braintrust WorkOS OpenAI

![[assets/slides/qdh_x-uRs9g/slide-002.jpg]]

OCR text:

> TheSmall-Model
> Infrastructure
> Nobody Built
> (sowe did）
> FilipMakraduli·Superlinked
> AlEngineer
> EUROPE

![[assets/slides/qdh_x-uRs9g/slide-003.jpg]]

OCR text:

> A WRITER'S DIARY ON AI
> What Actually Makes Embedding
> Model Inference Fast?
> From Flash Attention to Quantization, where is the inference bottleneck? Is it the architecture, the maths, or will writing everything in Rust solve all my problems? (Hint: It's Not Rust)
> FILIP MAKRADULI
> JAN 22, 2026
> Not quite.
> Google DeepMind

![[assets/slides/qdh_x-uRs9g/slide-004.jpg]]

OCR text:

> I realised... I had to learn
> AI Engineer
> EUROPE

![[assets/slides/qdh_x-uRs9g/slide-005.jpg]]

OCR text:

> Traming & re tening area pose DCMT RL stenet a gern
> va Eva‘vation & bencnmark:ng GPU uti! zat on & schedu .ng
> 
> * *
> * ~ Appied Al researc Rosting & autosca’ ng
> # . Bem rae feat ien Crployment & oprrat ons
> bod *
> 
> ad os *
> 
> Best way to learn?
> Join the team building it.
> : | Al Engineer |
> 
> eS) EUROPE
> 
> =

![[assets/slides/qdh_x-uRs9g/slide-006.jpg]]

OCR text:

> .
> Superlinked ©) github.com/superlinked/sie
> rane
> * *
> Ps * VC - backed Al infrastructure company building the model stack for Al search and document
> re x processing
> * ve *
> Works with your favorite taols neers
> ey Pa Pree’ os Pera te} coy paren ae
> Cree nears oes ee ere vena Sone Un Tn eee earns
> eer et Beene eee es prereset an
> Cate iat tne ie Ld Cha Se Ct we aac d oe eon a ee Lael pee OE i rec
> teat eer eaed ene Learns] coe ae ar ar Ree eee Tre el
> eee te Cm Me eerie seer ie at et ere de he Pe A ae ee
> Fo ett loses Pe oes re
> l | Al Engineer |
> = aUelaa
> re = oF

![[assets/slides/qdh_x-uRs9g/slide-007.jpg]]

OCR text:

> PU emulate uh
> Performance degrades as contest fille up
> lel Ret CECE LOE CDC
> aa _ / vere Tee ah ee Mae Lis
> Oa a TM, . 2a,
> * a N atl eeelre)
> rs N
> 4 : N\
> : \- . Es
> : . “iy . "Why not just Opus 4.62"
> . = Ty, se!
> : | Al Engineer |
> eS See) aa
> a hati

![[assets/slides/qdh_x-uRs9g/slide-008.jpg]]

OCR text:

> Context management
> Taxonomy classification
> 1OK categories Shopify product catalogue text + images
> Pan 3
> Pu *
> aCe
> Sg a Tool calling
> ars Product
> bauer sO) a ae
> Switching model type = changing one parameter, not
> rebuilding infra
> ] Engineering the future of Al

![[assets/slides/qdh_x-uRs9g/slide-009.jpg]]

OCR text:

> Model Performance V5 Size
> we _ ‘ :
> te ey °
> Y
> one ”
> Pane d
> * * ne nom &
> a
> * ad ‘ e °
> a in .
> 2
> .
> Pole Muitel See titan Paraet ona)
> | Al Engineer |
> Eng EUROPE
> aoe

![[assets/slides/qdh_x-uRs9g/slide-010.jpg]]

OCR text:

> SO, LET'S SUPPORT 85+ MODELS WITH 35+ RUNTIMES AND INFERENCE BACKENDS
> Every architecture is different under the hood
> bert_flash
> Fixed position IDs (0,1,2,...)
> Each token knows its absolute slot
> qwen2_flash
> RoPE: rotates Q/K vectors by position
> GQA: fewer KV heads = less memory
> modernbert_flash
> Fused QKV: one matrix, not three
> Pre-normalize before attention
> colbert_*
> Keeps every token's vector (not pooled)
> Late interaction: match token-by-token
> cross_encoder
> Takes a pair (query + doc) as input
> Outputs a score, not a vector
> clip_siglip_florence2
> Image encoder + text encoder
> Shared embedding space
> splade_flash
> Sparse 250K-dim vocabulary vector
> Learned term weights, not dense floats
> sglang
> 48-88 embedding models
> KV cache = paged memory
> No universal engine
> BERT + Qwen2 + ModernBERT.
> Each needs its own inference path.
> An agentic workflow
> We wrote each adapter using AI agents
> until we had coverage across 90 models.
> Re-implementation
> Not wrappers. We re-implement
> the forward pass and pooling for each arch.
> 15 of 35 adopters use Flash Attention 2 with variable-length sequence packing

![[assets/slides/qdh_x-uRs9g/slide-011.jpg]]

OCR text:

> cee Qwen2 ore a1 as
> Norm Pre-norm RMSNorm
> é Ca i‘ Q/KIV Rate Separate (GQA)
> na ae
> * rar i Lexth ated) Coa
> Attention GGA (fewer KV)
> Output
> Allon packed sequences with = zero padding waste
> Engineering the future of Al
> ES) >

![[assets/slides/qdh_x-uRs9g/slide-012.jpg]]

OCR text:

> We open sourced both the yin (model inference) and the
> 4, a
> nn Superlinked [m] ar art « [m]
> ® re
> * a . SIE — Superlinked Inference Engine is allan "
> i s i
> tro :
> ©) github.com/superlinked/sie 7
> ] Google DeepMind
> ES i a

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
