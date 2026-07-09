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

## Official Schedule Context
- Date/time: 2026-07-01 · 2:25pm-2:45pm
- Track/room: track TBD · Expo Stage 3 SW
- Speaker(s): Melanie Warrick
- Session type/status: session · confirmed

## Schedule Labels
- Track: track TBD
- Room: Expo Stage 3 SW
- Session type: session
- Status: confirmed

## Official Description
Production agent systems need humans in the loop. So why do they keep getting modeled as synchronous tool calls? The agent ecosystem is focused on autonomy, but in reality, especially for high-stakes or regulated workflows, humans are a critical feature, not an afterthought. This demo-driven talk shows how to stop bolting on humans and start treating them as async-by-default endpoints with proper durability, retry, and escalation semantics. We will walk through two live, multi-agent patterns built with LangGraph and Google ADK, on Temporal for durable execution: The Agent Calls the Human. A fleet dispatch system escalates a disruption to an approver. We will intentionally kill the worker process mid-wait. Hours later, the human responds. State survives, and the agent resumes. The Human Calls the Agent. An operator interrupts a long-running task mid-flight to redirect it. The agent halts gracefully, surfaces state, accepts the override, and continues. Harness engineering has heavily focused on model autonomy. This talk is about the other half of the puzzle: the human. You will leave with two production-ready architectural designs you can apply this week: agent-initiated approval gates with timeout and escalation semantics, and human-initiated interrupts with graceful agent halt and resumption. Not every agent needs a human in the loop. But if you are building systems where the cost of being wrong exceeds the cost of being slow, this talk is for you.

## Related YouTube Video
No related AI Engineer channel video found yet.

## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## People
- [[melanie-warrick]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.

## Source-Derived Enrichment
This section is generated from all currently linked source material for the article: official schedule text, related video pages, cached transcripts, visible slide text, dense/reconstructed slide pages, and AI slide-classification audits.

### Source Signals
No linked video, transcript, or slide source has been attached yet.

### Article Use
Use these source signals to refine the synopsis, topic links, people/company context, and method notes. If a source is a related external video rather than an exact official recording, keep it framed as supporting evidence.
