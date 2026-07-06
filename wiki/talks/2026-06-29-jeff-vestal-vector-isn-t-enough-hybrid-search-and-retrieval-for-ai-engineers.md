---
title: "Vector Isn't Enough: Hybrid Search & Retrieval for AI Engineers"
category: "talks"
date: "2026-06-29"
time: "2:20pm-4:20pm"
track: "Track 7"
room: "Track 7"
speakers: ["Jeff Vestal"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
---

# Vector Isn't Enough: Hybrid Search & Retrieval for AI Engineers

## Official Schedule Context
- Date/time: 2026-06-29 · 2:20pm-4:20pm
- Track/room: Track 7 · Track 7
- Speaker(s): Jeff Vestal
- Session type/status: sponsor · confirmed

## Official Description
If you build RAG, you reached for vector search first. This lab is about everything that happens

after you realize embeddings alone don't cut it in production. You'll write real queries — semantic,

lexical, and hybrid — feel exactly where each one fails, and walk out with a production-grade

retrieval pipeline and the judgment to know which technique to reach for when.  What you'll actually

do: 1. Dense vector search, and the mechanism behind it. Run semantic queries over a  semantic_text 

field backed by Jina v5 embeddings — generated server-side, at query time, by the Elastic Inference

Service (EIS). No embedding service to stand up, no client-side inference code. We open the hood on

how query-time embedding actually works. 2. Break it. Throw adversarial queries at pure vector —

exact error codes, version numbers (8.18 vs 9.0), precise config keys — and watch semantic

similarity blur the exact match you needed. Then bring in BM25 lexical search to rescue it… and find

the queries where keyword search whiffs. Each method is strongest exactly where the other is

weakest. 3. Hybrid, properly. Fuse lexical + semantic with Elasticsearch retrievers. Learn the two

fusion strategies that matter — Reciprocal Rank Fusion (RRF) and linear combination with score

normalization — when to use each, and how to tune them. Optional: cross-encoder reranking with Jina

Reranker v2.  4. Why this is the whole game for agents. Wire the hybrid retriever into a RAG flow

and prove that retrieval quality, not the model, determines answer quality. Only synthesis truly

needs the LLM - retrieve, rank, filter, and document-level security are database work done in

milliseconds for a fraction of the cost. The contrarian takeaway: most of your RAG pipeline

shouldn't be LLM calls at all.

## Related YouTube Video
No related AI Engineer channel video found yet.

## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## People
- [[jeff-vestal]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.
