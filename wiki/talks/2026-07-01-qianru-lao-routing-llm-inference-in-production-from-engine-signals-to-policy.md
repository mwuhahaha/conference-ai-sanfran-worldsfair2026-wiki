---
title: "Routing LLM Inference in Production: From Engine Signals to Policy"
category: "talks"
date: "2026-07-01"
time: "11:10am-11:30am"
track: "Inference"
room: "Track 9"
speakers: ["Qianru Lao", "Lu Zhang"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Inference"
scheduleRoom: "Track 9"
scheduleLabels: ["Inference", "Track 9", "session", "confirmed"]
---
# Routing LLM Inference in Production: From Engine Signals to Policy

## Conference Context
- Date/time: 2026-07-01 · 11:10am-11:30am
- Track/room: Inference · Track 9
- Speaker(s): Qianru Lao, Lu Zhang
- Session type/status: session · confirmed

- Track: Inference
- Room: Track 9
- Session type: session
- Status: confirmed

## Session Description
Production LLM apps need more than a fast model: they need an inference routing layer that can choose where each request should run as engines, capacity, latency, and geography cost change. This talk shares a generalized Inference Load Balancer (ILB) proxy/controller architecture. A low-latency proxy applies routing weights and request-path signals, while a controller computes source-cluster-to-engine weights from demand, capacity/performance profiles, replica state, and geography cost. We will cover the practical debugging patterns AI engineers need: reading engine signals, explaining why a request went to one backend instead of another, handling retries and load shedding, and keeping routing behavior observable without exposing OpenAI-specific internals or non-public metrics.

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
- [[qianru-lao]]
- [[lu-zhang]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.

## Synthesis
### Synthesized Breakdown
# Routing LLM Inference in Production: From Engine Signals to Policy ## Conference Context - Date/time: 2026-07-01 · 11:10am-11:30am - Track/room: Inference · Track 9 - Speaker(s): Qianru Lao, Lu Zhang - Session type/status: session · confirmed - Track: Inference - Room: Track 9 - Session type: session - Status: confirmed ## Session Description Production LLM apps need more than a fast model: they need an inference routing layer that can choose where each request should run as engines, capacity, latency, and geography cost change. This talk shares a generalized Inference Load Balancer (ILB) proxy/controller architecture. A low-latency proxy applies routing weights and request-path signals, while a controller computes source-cluster-to-engine weights from demand, capacity/performance profiles, replica state, and geography cost. We will cover the practical debugging patterns AI engineers need: reading engine signals, explaining why a request went to one backend instead of another, handling retries and load shedding, and keeping routing behavior observable without exposing OpenAI-specific internals or non-public metrics.

### Speaker And Company Context
- [[qianru-lao|Qianru Lao]] — Member of Technical Staff at [[openai|OpenAI]].
- [[lu-zhang|Lu Zhang]] — Member of Technical Staff at [[openai|OpenAI]].

### Topics Covered
- [[agent-security]]

### Derived Links And Source Material

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis is based on the official schedule and linked source pages. It should be revisited when exact session recordings or transcript-backed secondary sources are available.
