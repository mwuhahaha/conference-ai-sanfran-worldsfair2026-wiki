---
title: "Slides: We Cut 94% of AI Coding Tokens With a Local Code Index - Rajkumar Sakthivel, Tesco"
category: "slides"
video_id: "dRmWYHuIJxM"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: We Cut 94% of AI Coding Tokens With a Local Code Index - Rajkumar Sakthivel, Tesco

## Source Video
[We Cut 94% of AI Coding Tokens With a Local Code Index - Rajkumar Sakthivel, Tesco](https://www.youtube.com/watch?v=dRmWYHuIJxM)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/dRmWYHuIJxM/slide-001.jpg]]

OCR text:

> AIENGINEERWORLD'SFAIR
> June30-July2,2026-SanFrancisco
> SEARCH&RETRIEVAL TRACK
> We Cut 94% of Our Al Coding Tokens
> With a Local Code Index
> Here's the architecture.
> 0.4ms
> Token Reduction
> Search Latency
> Recall@10
> RajkumarSakthivel
> RS
> github.com/elara-labs/code-
> context-engine

![[assets/slides/dRmWYHuIJxM/slide-002.jpg]]

OCR text:

> Every Al coding tool we tried had the same assumption:
> send as much context as possible.
> sw \2)2)
> | i“

![[assets/slides/dRmWYHuIJxM/slide-003.jpg]]

OCR text:

> We optimized the model. We should have optimized the
> eet a> 4
> @ A retrieval layer between codebase and agent 4»
> t

![[assets/slides/dRmWYHuIJxM/slide-004.jpg]]

OCR text:

> Where your tokens actually go
> < | Output compression
> XO,
> = ~8% off total bill
> Input retrieval
> = ~61% off total bill
> @ 1 .

![[assets/slides/dRmWYHuIJxM/slide-005.jpg]]

OCR text:

> A local retrieval layer between codebase and agent
> Bic ibeCitg Hybrid Poin g Code Confidence
> Chunking Retrieval Compression Graph TorLitils]
> 10 langs 94% a Tica

![[assets/slides/dRmWYHuIJxM/slide-006.jpg]]

OCR text:

> Why not just vector search?
> Ss re a
> Vector Search FTS5 (BM25) RRF Fusion
> res cree,
> Neither retriever is good enough alone. Together they cover each other's blind spots. a

![[assets/slides/dRmWYHuIJxM/slide-007.jpg]]

OCR text:

> The hardest problem wasn't retrieval. It was knowing when
> retrieval was -
> Confidence scoring blend
> @ Simple heuristic won

![[assets/slides/dRmWYHuIJxM/slide-008.jpg]]

OCR text:

> BENCHMARK
> FastAPI
> FastAPl:53files,20realquestions,reproducible
> Full file baseline
> 83,681 tok/q
> Afterretrieval
> 4,927tok/q
> retrieval savings
> After compression
> 523tok/q
> No cherry-picking.No synthetic queries.
> 20questionsadeveloperwouldactuallyask
> Recall@10
> $pythonbenchmarks/run_benchmark.py
> --repo fastapi/fastapi--source-dirfa
> elara-labs/code-context-engine

![[assets/slides/dRmWYHuIJxM/slide-009.jpg]]

OCR text:

> TRADE-OFFS
> i
> What we're honest about
> 94% is against full-file reads Monorepos dilute recall
> Embedding model matters What actually worked
> : )

![[assets/slides/dRmWYHuIJxM/slide-010.jpg]]

OCR text:

> KEY TAKEAWAY
> MEASURABLE
> Everytokentracked.Everydollarcounted.
> my-project.247queries.Last query5mago
> 90088xtokensaved
> Input savings
> 12.4M
> tokens
> Output savings
> 48.2k
> tokens
> Total saved
> 12.4M
> tokens
> Breakdown:
> retrieval
> 10.4H $156.00
> chunk conpression
> 421.5k
> 48.2k
> nates.Actual tokens served vs full
> LDo
> costs from live modelpricing
> Thank you·Rajkumar Sakthivel

![[assets/slides/dRmWYHuIJxM/slide-011.jpg]]

OCR text:

> The biggest optimization in Al coding
> isn't the model. [t's the context.
> SA local a
> Bese) Try it now
> ae
> >

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
