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

## Synthesis
### Synthesized Breakdown
Production LLM apps need more than a fast model: they need an inference routing layer that can choose where each request should run as engines, capacity, latency, and geography cost change. This talk shares a generalized Inference Load Balancer (ILB) proxy/controller architecture. A low-latency proxy applies routing weights and request-path signals, while a controller computes source-cluster-to-engine weights from demand, capacity/performance profiles, replica state, and geography cost. We will cover the practical debugging patterns AI engineers need: reading engine signals, explaining why a request went to one backend instead of another, handling retries and load shedding, and keeping routing behavior observable without exposing OpenAI-specific internals or non-public metrics.

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
## People
- [[qianru-lao]]
- [[lu-zhang]]

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
