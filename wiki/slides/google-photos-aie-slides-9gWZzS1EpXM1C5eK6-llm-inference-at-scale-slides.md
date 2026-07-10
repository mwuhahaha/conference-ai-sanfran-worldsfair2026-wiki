---
title: "Google Photos Slides: LLM Inference at Scale Workshop"
category: "slides"
import_id: "aie-slides-9gWZzS1EpXM1C5eK6"
author: "boxofchocolates"
sourceLabels: ["Google Photos share", "Phone photo slide evidence", "RapidOCR text"]
confidence: "high"
---

# Google Photos Slides: LLM Inference at Scale Workshop

## Source
- Author: boxofchocolates
- Source type: Google Photos album import supplied to the wiki builder.
- Imported source layer: `raw/sources/google-photos-slides/aie-slides-9gWZzS1EpXM1C5eK6/`
- OCR engine: RapidOCR over downloaded Google Photos images.

## Relationship To World's Fair 2026
These photos are matched to the following scheduled session(s):
- [[2026-06-29-harshul-jain-2-hr-deep-dive-on-llm-inference-at-scale-part-1-of-2]] - 2 hr deep dive on LLM Inference at Scale — Part 1 of 2
- [[2026-06-29-harshul-jain-2-hr-deep-dive-on-llm-inference-at-scale-part-2-of-2]] - 2 hr deep dive on LLM Inference at Scale — Part 2 of 2

## Match Confidence
- Confidence: high
- OCR includes tensor/data/pipeline/expert/context parallelism.
- OCR names NSight Systems, Torch profilers, CuPTI, vLLM resources, and Modal.
- Timestamp note: Photo timestamps are around the Day 1 LLM inference workshop transition; linked to both workshop parts.

## Photo Slides
### Photo 002
- Captured at UTC: 2026-06-29T19:00:37.791000+00:00
- Captured local clock: 2026-06-29T12:00:37.791000+00:00
- Raw OCR: `raw/sources/google-photos-slides/aie-slides-9gWZzS1EpXM1C5eK6/ocr/photo-002.txt`

![[assets/slides/google-photos-aie-slides-9gWZzS1EpXM1C5eK6/photo-002.jpg]]

OCR text:

> Parallelism techniques
> Tensor parallelism Split matmul across GPUs,good for GEMMs
> Data parallelism Split batch across GPus,good for attention
> Pipeline parallelism Split model forward pipeline steps across GPus Prefill/decode disaggregation is, IMO,a special case
> Expertparallelism Split MoE experts across GPUs,good for group GEMMs
> Context parallelism Split sequence across GPUs, stillnew (to Oss)
> Modal

### Photo 003
- Captured at UTC: 2026-06-29T19:05:01.974000+00:00
- Captured local clock: 2026-06-29T12:05:01.974000+00:00
- Raw OCR: `raw/sources/google-photos-slides/aie-slides-9gWZzS1EpXM1C5eK6/ocr/photo-003.txt`

![[assets/slides/google-photos-aie-slides-9gWZzS1EpXM1C5eK6/photo-003.jpg]]

OCR text:

> Using the NSight Systems/Torch Profilers (CuPTI)
> 13 1 37853734
> 16716 DP3L 100%
> CUDAHWDOC3 300020-X
> NCCI
> 00030-N
> NCCL
> NCOL Threads(187)
> CUDAHW(000250010-N
> AISTN
> NCCL
> 00010-N
> AR
> NCCL
> ..
> Modal Threds(91) 2ste Stra

### Photo 004
- Captured at UTC: 2026-06-29T19:05:25.093000+00:00
- Captured local clock: 2026-06-29T12:05:25.093000+00:00
- Raw OCR: `raw/sources/google-photos-slides/aie-slides-9gWZzS1EpXM1C5eK6/ocr/photo-004.txt`

![[assets/slides/google-photos-aie-slides-9gWZzS1EpXM1C5eK6/photo-004.jpg]]

OCR text:

> Helpful resources
> Good for humans,good for agents
> Aleksa Gordic's walkthrough of vllm,Modal Notebooks [1l,[2]
> DeepWiki from Cognition Organized,diagrams,queryable s
> Modal
