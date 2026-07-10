---
title: "KV Cache-Aware Routing and P/D Disaggregation on Kubernetes: The Parts Public Benchmarks Don't Show"
category: "talks"
date: "2026-07-01"
time: "2:50pm-3:10pm"
track: "Inference"
room: "Track 9"
speakers: ["Yuchen Fama", "Ashish Kamra"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Inference"
scheduleRoom: "Track 9"
scheduleLabels: ["Inference", "Track 9", "session", "confirmed"]
---
# KV Cache-Aware Routing and P/D Disaggregation on Kubernetes: The Parts Public Benchmarks Don't Show

## Conference Context
- Date/time: 2026-07-01 · 2:50pm-3:10pm
- Track/room: Inference · Track 9
- Speaker(s): Yuchen Fama, Ashish Kamra
- Session type/status: session · confirmed

- Track: Inference
- Room: Track 9
- Session type: session
- Status: confirmed

## Session Description
We're at the inflection point between classic LLM inference and agentic inference. When we look at the agentic workloads and trace replays, many core characteristics break classic LLM serving assumptions. The most consequential: the server no longer controls its own cache lifecycle. The client does, through prompt construction, multi-turn context that grows and changes each turn. This has downstream effects. Because context is client-determined, prefill strategy, eviction, and routing decisions move up to the scheduler layer. KV cache becomes volatile — frequent eviction and rewrite, driven from outside the engine. And latency becomes a first-class scheduling metric alongside throughput. This talk covers the open stack for LLM and agentic era inference serving: vLLM and llm-d. We begin with the core characteristics and challenges of agentic inference, then the economics: prefill dominates cost, and cache reuse is the primary lever. We explain why KV-aware routing through a fleet-wide scheduler is the first optimization to apply, ahead of adding capacity. Next, prefill/decode disaggregation. We separate compute-bound prefill from memory-bound decode, and examine what public benchmarks omit: the conditions under which P/D disaggregation shines, and the workload shapes that justify the added architectural complexity. We close with GLM-5.2 and show the equivalent stack assembled in the open: cache-aware routing, P/D disaggregation, tiered KV offload, and wide expert parallelism — implemented on vLLM and llm-d. Attendees leave with a tuning decision framework: which lever to apply first, how to read workload signals, and where additional GPUs do and don't help.

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
- [[yuchen-fama]]
- [[ashish-kamra]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.
