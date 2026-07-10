---
title: "Vector Isn't Enough: Hybrid Search & Retrieval for AI Engineers"
category: "talks"
date: "2026-06-29"
time: "2:20pm-4:20pm"
track: "Track 7"
room: "Track 7"
speakers: ["Jeff Vestal"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Track 7"
scheduleRoom: "Track 7"
scheduleLabels: ["Track 7", "Track 7", "sponsor", "confirmed"]
---
# Vector Isn't Enough: Hybrid Search & Retrieval for AI Engineers

## Conference Context
- Date/time: 2026-06-29 · 2:20pm-4:20pm
- Track/room: Track 7 · Track 7
- Speaker(s): Jeff Vestal
- Session type/status: sponsor · confirmed

- Track: Track 7
- Room: Track 7
- Session type: sponsor
- Status: confirmed

## Session Description
If you build RAG, you reached for vector search first. This lab is about everything that happens after you realize embeddings alone don't cut it in production. You'll write real queries — semantic, lexical, and hybrid — feel exactly where each one fails, and walk out with a production-grade retrieval pipeline and the judgment to know which technique to reach for when. What you'll actually do: 1. Dense vector search, and the mechanism behind it. Run semantic queries over a semantic_text field backed by Jina v5 embeddings — generated server-side, at query time, by the Elastic Inference Service (EIS). No embedding service to stand up, no client-side inference code. We open the hood on how query-time embedding actually works. 2. Break it. Throw adversarial queries at pure vector — exact error codes, version numbers (8.18 vs 9.0), precise config keys — and watch semantic similarity blur the exact match you needed. Then bring in BM25 lexical search to rescue it… and find the queries where keyword search whiffs. Each method is strongest exactly where the other is weakest. 3. Hybrid, properly. Fuse lexical + semantic with Elasticsearch retrievers. Learn the two fusion strategies that matter — Reciprocal Rank Fusion (RRF) and linear combination with score normalization — when to use each, and how to tune them. Optional: cross-encoder reranking with Jina Reranker v2. 4. Why this is the whole game for agents. Wire the hybrid retriever into a RAG flow and prove that retrieval quality, not the model, determines answer quality. Only synthesis truly needs the LLM - retrieve, rank, filter, and document-level security are database work done in milliseconds for a fraction of the cost. The contrarian takeaway: most of your RAG pipeline shouldn't be LLM calls at all.

## Media Evidence
No related AI Engineer channel video found yet.

## Evidence Graph
This evidence graph is generated from currently linked source material: official schedule text, related video pages, cached transcripts, visible slide text, dense/reconstructed slide pages, and AI slide-classification audits.

### Media Signals
No linked video, transcript, or slide source has been attached yet.

### Agent Reading Notes
Use these signals to refine the synopsis, topic links, people/company context, and method notes. If a source is a related external video rather than an exact official recording, keep it framed as supporting evidence.

## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## People
- [[jeff-vestal]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.

## Synthesis
### Synthesized Breakdown
# Vector Isn't Enough: Hybrid Search & Retrieval for AI Engineers ## Conference Context - Date/time: 2026-06-29 · 2:20pm-4:20pm - Track/room: Track 7 · Track 7 - Speaker(s): Jeff Vestal - Session type/status: sponsor · confirmed - Track: Track 7 - Room: Track 7 - Session type: sponsor - Status: confirmed ## Session Description If you build RAG, you reached for vector search first. This lab is about everything that happens after you realize embeddings alone don't cut it in production. You'll write real queries — semantic, lexical, and hybrid — feel exactly where each one fails, and walk out with a production-grade retrieval pipeline and the judgment to know which technique to reach for when. What you'll actually do: 1.

### Speaker And Company Context
- [[jeff-vestal|Jeff Vestal]] — Senior Principal AI Architect at [[elastic|Elastic]].

### Topics Covered
- [[agentic-search]]
- [[coding-agents]]

### Derived Links And Source Material

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis is based on the official schedule and linked source pages. It should be revisited when exact session recordings or transcript-backed secondary sources are available.
