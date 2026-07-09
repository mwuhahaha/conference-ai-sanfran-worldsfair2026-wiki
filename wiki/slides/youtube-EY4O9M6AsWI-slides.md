---
title: "Slides: Dream Machine: Scaling to 1m users in 4 days — Keegan McCallum, Luma AI"
category: "slides"
video_id: "EY4O9M6AsWI"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: Dream Machine: Scaling to 1m users in 4 days — Keegan McCallum, Luma AI

## Source Video
[Dream Machine: Scaling to 1m users in 4 days — Keegan McCallum, Luma AI](https://www.youtube.com/watch?v=EY4O9M6AsWI)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/EY4O9M6AsWI/slide-001.jpg]]

OCR text:

> INNOVATIONPARTNER
> aws
> PLATINUMSPONSORS
> Graphite
> WWindsurf
> MongoDB
> daily
> augment code
> Workos

![[assets/slides/EY4O9M6AsWI/slide-002.jpg]]
![[assets/slides/EY4O9M6AsWI/slide-003.jpg]]

OCR text:

> AIE
> Luma
> Microsoft
> smol ai

![[assets/slides/EY4O9M6AsWI/slide-004.jpg]]

OCR text:

> amit10:42PM
> iamthecha0smonkeyhttps://x.com/LumaLabsAl/status/1801127491496730730
> XX(formerlyTwitter)
> LumaAl(@LumaLabsAl)onX
> Thankyou foryourpatiencewhilewescaled upDreamMachine.It's10xbiggernow！
> AIE
> Let'sgetbackto imagining...(135kB)
> ITIS
> RELEASEDAY
> MY DUDES.
> Luma
> Microsoft
> smolo

![[assets/slides/EY4O9M6AsWI/slide-005.jpg]]

OCR text:

> let'sseehowitgoes
> KeeganMcCallom 10517
> Thomas
> KeeganMcCallum 11:31PM
> KeeganMcCallm
> 1952PM
> 400 ahth ol
> AIE
> ustPINNING 5000 H100s aIldary
> dockerinstalledon1st16/18
> pullingimage
> Thomus
> 10S3PM
> keepingat aroumd 400muybe
> KeeganMeCallm10.5P
> Nope oh boy 500
> ahhhh this is white knuckling.Ihope these nodes are enough
> saanninomscanAi
> KeeganMcCallum 12:11AM
> YESlol
> 2500im2vidqueue
> banana barely made a dent
> Microsoft
> smol?

![[assets/slides/EY4O9M6AsWI/slide-006.jpg]]

OCR text:

> Luma's mission is to build multimodal general
> intelligence that can generate, understand, and
> operate in the physical world
> « Luma
> aws
> 7 |
> ae —"

![[assets/slides/EY4O9M6AsWI/slide-007.jpg]]

OCR text:

> AIE
> aws

![[assets/slides/EY4O9M6AsWI/slide-008.jpg]]

OCR text:

> AIE

![[assets/slides/EY4O9M6AsWI/slide-009.jpg]]

OCR text:

> Public API
> Check it out at:
> https://lumalabs.ai/api/pricing

![[assets/slides/EY4O9M6AsWI/slide-010.jpg]]

OCR text:

> CPU Worker FARR PACE ey CPU Worker a
> -
> CPU Worker CPU Worker
> - ug
> triton abe re et ne eee baeeeel COE e See 2 oe
> « Luma
> —_ 7
> si)
> a Microsoft §$ou
> ee —

![[assets/slides/EY4O9M6AsWI/slide-011.jpg]]

OCR text:

> Challenges
> • Brittle, need to coordinate between both CPU and Triton being up at the same
> time
> • Triton not built for multi-gpu/multi-node
> • Push model not ideal for multi-node (which node has rank 0?)
> • No/limited support for non-nvidia chipsets with Triton
> • Very difficult to develop against
> • Need to have every piece everywhere, hard to bring in disparate compute (i.e.
> from our training cluster:kekw:)

![[assets/slides/EY4O9M6AsWI/slide-012.jpg]]

OCR text:

> (hapuens)
> Redis
> API
> GpU werkers
> Redis
> AIE
> (stardbg)
> Redis
> Workers
> CPU
> Seaweedfs
> Luma
> aws

![[assets/slides/EY4O9M6AsWI/slide-013.jpg]]

OCR text:

> Challenges
> Backpressure
> AIE
> Priorities/fairscheduling
> Handlingmanydifferentmodels
> Handling Bursts
> Microsoft
> .loms

![[assets/slides/EY4O9M6AsWI/slide-014.jpg]]

OCR text:

> Queues, Queues, Queues
> AIE
> Luma
> Microsoft
> smol ai

![[assets/slides/EY4O9M6AsWI/slide-015.jpg]]

OCR text:

> Model Management
> AIE
> Luma
> Microsoft
> smol ai

![[assets/slides/EY4O9M6AsWI/slide-016.jpg]]

OCR text:

> THANK YOU
> Luma

![[assets/slides/EY4O9M6AsWI/slide-017.jpg]]

OCR text:

> THANK YOU
> Luma

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
