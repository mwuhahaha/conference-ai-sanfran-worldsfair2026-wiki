---
title: "1,000 Agent Tasks in a Sandbox: What Breaks When LLMs Write and Run Code"
category: "talks"
date: "2026-06-30"
time: "2:25pm-2:45pm"
track: "Sandbox & Platform Engineering"
room: "Track 1"
speakers: ["Kevin Orellana"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Sandbox & Platform Engineering"
scheduleRoom: "Track 1"
scheduleLabels: ["Sandbox & Platform Engineering", "Track 1", "session", "confirmed"]
---
# 1,000 Agent Tasks in a Sandbox: What Breaks When LLMs Write and Run Code

## Conference Context
- Date/time: 2026-06-30 · 2:25pm-2:45pm
- Track/room: Sandbox & Platform Engineering · Track 1
- Speaker(s): Kevin Orellana
- Session type/status: session · confirmed

- Track: Sandbox & Platform Engineering
- Room: Track 1
- Session type: session
- Status: confirmed

## Session Description
We ran 1,000 automated tasks through a production code interpreter sandbox — file I/O, package installs, data analysis, ML training, binary downloads, multi-language execution — and tracked every failure. 88% passed. The other 12% revealed 18 distinct failure modes that no unit test would catch: binary encoding corruption in the transport layer, null bytes silently truncating file downloads, pip blocked by network isolation with no useful error, and path traversal inputs accepted without validation. This talk walks through the experiment design, the findings ranked by severity, and what we changed. If you are building or operating sandboxed execution for AI agents, these are the bugs waiting for your customers to find first.

## Synthesis
### Synthesized Breakdown
We ran 1,000 automated tasks through a production code interpreter sandbox — file I/O, package installs, data analysis, ML training, binary downloads, multi-language execution — and tracked every failure. 88% passed. The other 12% revealed 18 distinct failure modes that no unit test would catch: binary encoding corruption in the transport layer, null bytes silently truncating file downloads, pip blocked by network isolation with no useful error, and path traversal inputs accepted without validation. This talk walks through the experiment design, the findings ranked by severity, and what we changed.

### Speaker And Company Context
- [[kevin-orellana|Kevin Orellana]] — Software Engineer at [[amazon-web-services|Amazon Web Services]].

### Topics Covered
- [[agentic-search]]
- [[ai-sandboxes]]
- [[coding-agents]]

### Derived Links And Source Material

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis is based on the official schedule and linked source pages. It should be revisited when exact session recordings or transcript-backed secondary sources are available.
## People
- [[kevin-orellana]]

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
