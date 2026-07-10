---
title: "Seeing the Plumbing: Profiling vLLM Speculative Decoding on NVIDIA Blackwell"
category: "talks"
date: "2026-07-01"
time: "11:40am-12:00pm"
track: "Expo Stage 2 NW"
room: "Expo Stage 2 NW"
speakers: ["Sheilah Kirui"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: ""
scheduleRoom: "Expo Stage 2 NW"
scheduleLabels: ["Expo Stage 2 NW", "session", "confirmed"]
---
# Seeing the Plumbing: Profiling vLLM Speculative Decoding on NVIDIA Blackwell

## Conference Context
- Date/time: 2026-07-01 · 11:40am-12:00pm
- Track/room: track TBD · Expo Stage 2 NW
- Speaker(s): Sheilah Kirui
- Session type/status: session · confirmed

- Track: track TBD
- Room: Expo Stage 2 NW
- Session type: session
- Status: confirmed

## Session Description
Speculative decoding promises dramatic LLM speedups by using a tiny draft model to guess tokens ahead of a large target model. However, dual-model serving fundamentally rewrites your memory dynamics and introduces a rigid engineering trade-off: guess right, and you bypass the memory-bandwidth bottleneck; guess wrong, and you waste compute. This session is a live-demo routing identical workloads through baseline and speculative configurations in vLLM on a single NVIDIA RTX 6000 Blackwell GPU. Splitting the screen between a Streamlit app and a live Grafana dashboard, we will profile the inference engine across three vectors: Time per Output Token (TPOT): The real-time, user-facing latency delta. KV Cache & Memory Footprint: The exact VRAM tax of tracking parallel token states within a 96GB budget. Draft Acceptance Rate: Visualizing the tipping point where dropping acceptance rates cause speculative decoding to fall below baseline efficiency. Supporting Materials Project Repository: https://github.com/akamai-developers/speculative-decoding-example-vllm-blackwell# (Work In Progress / Active Development)

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
- [[sheilah-kirui]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.

## Synthesis
### Synthesized Breakdown
# Seeing the Plumbing: Profiling vLLM Speculative Decoding on NVIDIA Blackwell ## Conference Context - Date/time: 2026-07-01 · 11:40am-12:00pm - Track/room: track TBD · Expo Stage 2 NW - Speaker(s): Sheilah Kirui - Session type/status: session · confirmed - Track: track TBD - Room: Expo Stage 2 NW - Session type: session - Status: confirmed ## Session Description Speculative decoding promises dramatic LLM speedups by using a tiny draft model to guess tokens ahead of a large target model. However, dual-model serving fundamentally rewrites your memory dynamics and introduces a rigid engineering trade-off: guess right, and you bypass the memory-bandwidth bottleneck; guess wrong, and you waste compute. This session is a live-demo routing identical workloads through baseline and speculative configurations in vLLM on a single NVIDIA RTX 6000 Blackwell GPU. Splitting the screen between a Streamlit app and a live Grafana dashboard, we will profile the inference engine across three vectors: Time per Output Token (TPOT): The real-time, user-facing latency delta.

### Speaker And Company Context
- [[sheilah-kirui|Sheilah Kirui]] — role not listed at [[nvidia|NVIDIA]].

### Topics Covered
- [[coding-agents]]

### Derived Links And Source Material

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis is based on the official schedule and linked source pages. It should be revisited when exact session recordings or transcript-backed secondary sources are available.
