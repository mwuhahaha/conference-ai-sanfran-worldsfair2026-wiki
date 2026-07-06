---
title: "Autoresearch for Dense Retrieval: Test-Time Compute with Frozen Embedding Models"
category: "talks"
date: "2026-06-30"
time: "11:10am-11:30am"
track: "Autoresearch"
room: "Main Stage"
speakers: ["Han Xiao"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
---

# Autoresearch for Dense Retrieval: Test-Time Compute with Frozen Embedding Models

## Official Schedule Context
- Date/time: 2026-06-30 · 11:10am-11:30am
- Track/room: Autoresearch · Main Stage
- Speaker(s): Han Xiao
- Session type/status: session · confirmed

## Official Description
Test-time compute is widely believed to benefit only large reasoning models. We show it also helps

small embedding models. Since modern embedding models are distilled from LLM backbones, a frozen

encoder should benefit from extra inference compute without retraining. Using an agentic program-

search loop spanning 144 generations, we explore 144 candidate programs over a frozen encoder API.

The search produces twelve Pareto-optimal programs spanning cost ratios of c=1.2 to 14.7 over the

single-pass baseline. The programs are structurally diverse: the search independently rediscovers

Rocchio pseudo-relevance feedback, ColBERT-style MaxSim at sentence granularity, reciprocal rank

fusion, and the Fisher linear discriminant, all without trainable parameters or external models.

Every frontier program improves nDCG@10 over the frozen baseline across all 14 MMTEB retrieval tasks

spanning legal, financial, long-document, and general domains.

## Related YouTube Video
No related AI Engineer channel video found yet.

## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## People
- [[han-xiao]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.
