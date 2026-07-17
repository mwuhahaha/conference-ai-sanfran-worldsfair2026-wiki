---
title: "The Human Is an Async API"
category: "talks"
date: "2026-07-01"
time: "2:25pm-2:45pm"
track: "Expo Stage 3 SW"
room: "Expo Stage 3 SW"
speakers: ["Melanie Warrick"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: ""
scheduleRoom: "Expo Stage 3 SW"
scheduleLabels: ["Expo Stage 3 SW", "session", "confirmed"]
---
# The Human Is an Async API

## Conference Context
- Date/time: 2026-07-01 · 2:25pm-2:45pm
- Track/room: track TBD · Expo Stage 3 SW
- Speaker(s): Melanie Warrick
- Session type/status: session · confirmed

- Track: track TBD
- Room: Expo Stage 3 SW
- Session type: session
- Status: confirmed

## Session Description
Production agent systems need humans in the loop. So why do they keep getting modeled as synchronous tool calls? The agent ecosystem is focused on autonomy, but in reality, especially for high-stakes or regulated workflows, humans are a critical feature, not an afterthought. This demo-driven talk shows how to stop bolting on humans and start treating them as async-by-default endpoints with proper durability, retry, and escalation semantics. We will walk through two live, multi-agent patterns built with LangGraph and Google ADK, on Temporal for durable execution: The Agent Calls the Human. A fleet dispatch system escalates a disruption to an approver. We will intentionally kill the worker process mid-wait. Hours later, the human responds. State survives, and the agent resumes. The Human Calls the Agent. An operator interrupts a long-running task mid-flight to redirect it. The agent halts gracefully, surfaces state, accepts the override, and continues. Harness engineering has heavily focused on model autonomy. This talk is about the other half of the puzzle: the human. You will leave with two production-ready architectural designs you can apply this week: agent-initiated approval gates with timeout and escalation semantics, and human-initiated interrupts with graceful agent halt and resumption. Not every agent needs a human in the loop. But if you are building systems where the cost of being wrong exceeds the cost of being slow, this talk is for you.

## Synthesis
### Synthesized Breakdown
Production agent systems need humans in the loop. So why do they keep getting modeled as synchronous tool calls? The agent ecosystem is focused on autonomy, but in reality, especially for high-stakes or regulated workflows, humans are a critical feature, not an afterthought. This demo-driven talk shows how to stop bolting on humans and start treating them as async-by-default endpoints with proper durability, retry, and escalation semantics.

### Speaker And Company Context
- [[melanie-warrick|Melanie Warrick]] — Developer Relations Engineering at [[temporal-technologies|Temporal Technologies]].

### Topics Covered
- Topic links are pending transcript-backed classification.

### Derived Links And Source Material

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis is based on the official schedule and linked source pages. It should be revisited when exact session recordings or transcript-backed secondary sources are available.
## People
- [[melanie-warrick]]

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
