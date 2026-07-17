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

> THE ASSUMPTION
> EveryAl coding tool we tried had the same assumption:
> sendasmuchcontextaspossible.
> WHAT AGENTS SEND 45,000 WHAT'SACTUALLYUSEFUL ~5,000
> tokensperquery tokensperquery
> We didn't notice until we saw the cost and latency impact.
> elara-labs/code-context-engine

![[assets/slides/dRmWYHuIJxM/slide-003.jpg]]

OCR text:

> We optimized the model. We should have optimized the
> eet a> 4
> @ A retrieval layer between codebase and agent 4»
> t

![[assets/slides/dRmWYHuIJxM/slide-004.jpg]]

OCR text:

> WHYINPUT MATTERS
> Where your tokens actually go
> Output compression
> Saves75%ofoutput tokens
> %06 =~8%off totalbill
> jnduis! Inputretrieval Saves94%of input tokens
> ~61%off totalbill
> Input tokens(filereads,search,context) spend. Both help.But if you're only doing one,do the one that tar
> Output tokens(agentreplies,code)
> 4elara-labs/code-context-engine

![[assets/slides/dRmWYHuIJxM/slide-005.jpg]]

OCR text:

> ARCHITECTURE
> A localretrieval layerbetweencodebaseand agent
> Tree-sitter Chunking Retrieval Hybrid Compression Chunk Graph Code Confidence Scoring
> AST-aware splits 10langs Vector 94% T+BM25+RRF Signatures 89% docs CALLS related IMPORTS Threshold gate filter
> Everythingruns locally.No cloud,noAPIcalls.sqlite-vec+FTS5+graph in threeSQLite files.
> elara-labs/code-context-engine

![[assets/slides/dRmWYHuIJxM/slide-006.jpg]]

OCR text:

> Why not just vector search?
> Ss re a
> Vector Search FTS5 (BM25) RRF Fusion
> res cree,
> Neither retriever is good enough alone. Together they cover each other's blind spots. a

![[assets/slides/dRmWYHuIJxM/slide-007.jpg]]

OCR text:

> THE HARD PART
> The hardestproblem wasn'tretrieval.Itwasknowingwhen retrievalwaswrong.
> LLM-based scoring Confidencescoringblend
> and costperquery. Similarity 50%
> Fixed thresholds Keywords 30%
> alike. cosine>0.7=relevant.Broke on short queriesand longqueries Recency 20%
> Simpleheuristicwon
> noAPI calls. 50%similarity+30%keyword+20%recency.Adaptive.0.4ms, Lesson:don't reach foran LLMwhena weighted avera
> 4elara-labs/code-context-engine

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
> Whatwe'rehonestabout
> 94%isagainstfull-filereads Monorepos diluterecall
> savingsvsnormal behavior are lower.Full-file is ourreproducible baseline. Claude Code alreadyuses grep andpartial reads.Real-world OnGo'sfiber(396files),recall dropped to0.07@10.One- feature-per-filereposhit R=1.00.Focused filesretrieve best.
> Embeddingmodel matters Whatactuallyworked
> cache. bge-small-en-v1.5(384d)is fast,notSOTA.Biggermodels lift recall but add latency.We chose speed;<1sre-indexat96% overpure vector.Local-first.The boring choices com Simple heuristics overML.SQLite over specialized DB
> elara-labs/code-context-engine

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

> KEYTAKEAWAY
> The biggest optimization in Al coding isn't the model. It's the context.
> $uvx--from"code-context-engine[local]"cceinit
> 94% local MIT
> fewerinputtokens nodataleavesyourmachine free,open source
> Tryitnow
> yourself. Scan to open the repo.Starit,forkit,run the benchmark
> github.com/elara-labs/code-context-engine
> Thank you.Rajkumar Sakthivel

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
