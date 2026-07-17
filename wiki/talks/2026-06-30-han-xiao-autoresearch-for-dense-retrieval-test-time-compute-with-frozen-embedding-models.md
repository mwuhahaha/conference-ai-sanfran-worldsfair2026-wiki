---
title: "Autoresearch for Dense Retrieval: Test-Time Compute with Frozen Embedding Models"
category: "talks"
date: "2026-06-30"
time: "11:10am-11:30am"
track: "Autoresearch"
room: "Main Stage"
speakers: ["Han Xiao"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Autoresearch"
scheduleRoom: "Main Stage"
scheduleLabels: ["Autoresearch", "Main Stage", "session", "confirmed"]
---
# Autoresearch for Dense Retrieval: Test-Time Compute with Frozen Embedding Models

## Conference Context
- Date/time: 2026-06-30 · 11:10am-11:30am
- Track/room: Autoresearch · Main Stage
- Speaker(s): Han Xiao
- Session type/status: session · confirmed

- Track: Autoresearch
- Room: Main Stage
- Session type: session
- Status: confirmed

## Session Description
Test-time compute is widely believed to benefit only large reasoning models. We show it also helps small embedding models. Since modern embedding models are distilled from LLM backbones, a frozen encoder should benefit from extra inference compute without retraining. Using an agentic program-search loop spanning 144 generations, we explore 144 candidate programs over a frozen encoder API. The search produces twelve Pareto-optimal programs spanning cost ratios of c=1.2 to 14.7 over the single-pass baseline. The programs are structurally diverse: the search independently rediscovers Rocchio pseudo-relevance feedback, ColBERT-style MaxSim at sentence granularity, reciprocal rank fusion, and the Fisher linear discriminant, all without trainable parameters or external models. Every frontier program improves nDCG@10 over the frozen baseline across all 14 MMTEB retrieval tasks spanning legal, financial, long-document, and general domains.

## Synthesis
### Synthesized Breakdown
Test-time compute is widely believed to benefit only large reasoning models. We show it also helps small embedding models. Since modern embedding models are distilled from LLM backbones, a frozen encoder should benefit from extra inference compute without retraining. Using an agentic program-search loop spanning 144 generations, we explore 144 candidate programs over a frozen encoder API.

### Speaker And Company Context
- [[han-xiao|Han Xiao]] — VP, AI at [[elastic|Elastic]].

### Topics Covered
- [[agentic-search]]
- [[coding-agents]]

### Derived Links And Source Material

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis is based on the official schedule and linked source pages. It should be revisited when exact session recordings or transcript-backed secondary sources are available.
## People
- [[han-xiao]]

## Media Evidence
No exact recording or transcript evidence is attached yet; the official schedule remains the source for this session.
## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
No linked video, transcript, or slide source has been attached yet.

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.
