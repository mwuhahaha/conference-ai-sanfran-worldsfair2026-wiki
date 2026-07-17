---
title: "Why your company needs a context graph, and how to build it"
category: "talks"
date: "2026-06-30"
time: "1:55pm-2:15pm"
track: "Expo Stage 3"
room: "Expo Stage 2 NW"
speakers: ["Gil Feig"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Expo Stage 3"
scheduleRoom: "Expo Stage 2 NW"
scheduleLabels: ["Expo Stage 3", "Expo Stage 2 NW", "session", "confirmed"]
---
# Why your company needs a context graph, and how to build it

## Conference Context
- Date/time: 2026-06-30 · 1:55pm-2:15pm
- Track/room: Expo Stage 3 · Expo Stage 2 NW
- Speaker(s): Gil Feig
- Session type/status: session · confirmed

- Track: Expo Stage 3
- Room: Expo Stage 2 NW
- Session type: session
- Status: confirmed

## Session Description
Everyone building AI products eventually draws the same diagram: boxes representing data sources, arrows pointing at the model, and a label that says "context." What that diagram doesn't show is the system that has to run underneath it deciding, for each request: which sources to consult, whether to fetch live or use cached data, if the user is actually allowed to view that data, how to stitch it all together before the latency budget runs out. And it hides the counterintuitive part: fetching more context usually makes your answers worse, not better. At Merge, we reframed context graphs as control planes, helping companies scale context graphs to hundreds of thousands of users with sub-300 ms latency. This talk walks engineers through the system design at scale: how to tier data freshness, why provenance isn't optional once third-party systems are in the loop, and how to decide when fetching less context is the right call. Attendees will leave with a mental model for context system design that separates the orchestration decisions from the retrieval layer.

## Synthesis
### Synthesized Breakdown
Everyone building AI products eventually draws the same diagram: boxes representing data sources, arrows pointing at the model, and a label that says "context." What that diagram doesn't show is the system that has to run underneath it deciding, for each request: which sources to consult, whether to fetch live or use cached data, if the user is actually allowed to view that data, how to stitch it all together before the latency budget runs out. And it hides the counterintuitive part: fetching more context usually makes your answers worse, not better. At Merge, we reframed context graphs as control planes, helping companies scale context graphs to hundreds of thousands of users with sub-300 ms latency. This talk walks engineers through the system design at scale: how to tier data freshness, why provenance isn't optional once third-party systems are in the loop, and how to decide when fetching less context is the right call.

### Speaker And Company Context
- [[gil-feig|Gil Feig]] — CTO and Co-Founder at [[merge|Merge]].

### Topics Covered
- [[agent-security]]
- [[agentic-search]]

### Derived Links And Source Material

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis is based on the official schedule and linked source pages. It should be revisited when exact session recordings or transcript-backed secondary sources are available.
## People
- [[gil-feig]]

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
