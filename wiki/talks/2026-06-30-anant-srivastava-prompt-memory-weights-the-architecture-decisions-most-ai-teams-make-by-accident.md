---
title: "Prompt, Memory, Weights: The Architecture Decisions Most AI Teams Make by Accident"
category: "talks"
date: "2026-06-30"
time: "12:05pm-12:25pm"
track: "Context Engineering"
room: "Expo Stage 4 SE"
speakers: ["Anant Srivastava"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Context Engineering"
scheduleRoom: "Expo Stage 4 SE"
scheduleLabels: ["Context Engineering", "Expo Stage 4 SE", "session", "confirmed"]
---
# Prompt, Memory, Weights: The Architecture Decisions Most AI Teams Make by Accident

## Conference Context
- Date/time: 2026-06-30 · 12:05pm-12:25pm
- Track/room: Context Engineering · Expo Stage 4 SE
- Speaker(s): Anant Srivastava
- Session type/status: session · confirmed

- Track: Context Engineering
- Room: Expo Stage 4 SE
- Session type: session
- Status: confirmed

## Session Description
The interesting engineering in production AI isn't in the model. Your knowledge lives in files, databases, and APIs: docs, runbooks, conversations, code. The model just reads tokens. So the real architectural question is which path that knowledge takes to inference: into the prompt directly, into memory for retrieval on demand, or into the weights through fine-tuning. Most teams treat these as a ladder. Start with prompts, escalate to RAG, eventually fine-tune, as if each step is a more advanced version of the last. The field is converging on a different answer: they solve different problems. The prompt shapes behavior and constraints. Memory grounds the model in current, citable knowledge. Weights harden specialized reasoning and format. They're not substitutes you graduate between; they're complementary, and the failures come from using one to do another's job. Fine-tuning to teach the model facts it should have retrieved is the classic trap: you bake in knowledge that's stale the day it ships, and you still can't cite it. This is an opinionated take on all three: when each is the right call, when each is a trap, and the part most teams never build, the circulation between them. Memory that captures what the agent does becomes the dataset you fine-tune on; fine-tuning changes what's worth retrieving; the loop compounds. Get the three paths right and they stop being a pipeline you climb and start being an architecture that learns.

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
- [[anant-srivastava]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.

## Synthesis
### Synthesized Breakdown
# Prompt, Memory, Weights: The Architecture Decisions Most AI Teams Make by Accident ## Conference Context - Date/time: 2026-06-30 · 12:05pm-12:25pm - Track/room: Context Engineering · Expo Stage 4 SE - Speaker(s): Anant Srivastava - Session type/status: session · confirmed - Track: Context Engineering - Room: Expo Stage 4 SE - Session type: session - Status: confirmed ## Session Description The interesting engineering in production AI isn't in the model. Your knowledge lives in files, databases, and APIs: docs, runbooks, conversations, code. The model just reads tokens. So the real architectural question is which path that knowledge takes to inference: into the prompt directly, into memory for retrieval on demand, or into the weights through fine-tuning.

### Speaker And Company Context
- [[anant-srivastava|Anant Srivastava]] — Principal Technologist - Data and AI Platforms at [[oracle|Oracle]].

### Topics Covered
- [[agentic-search]]
- [[agentic-web]]
- [[coding-agents]]

### Derived Links And Source Material

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis is based on the official schedule and linked source pages. It should be revisited when exact session recordings or transcript-backed secondary sources are available.
