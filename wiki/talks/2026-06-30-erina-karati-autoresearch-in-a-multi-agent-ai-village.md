---
title: "Autoresearch in a Multi-Agent AI Village"
category: "talks"
date: "2026-06-30"
time: "3:45pm-4:05pm"
track: "Autoresearch"
room: "Main Stage"
speakers: ["Erina Karati", "Arunachalam Manikandan"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Autoresearch"
scheduleRoom: "Main Stage"
scheduleLabels: ["Autoresearch", "Main Stage", "session", "confirmed"]
---
# Autoresearch in a Multi-Agent AI Village

## Conference Context
- Date/time: 2026-06-30 · 3:45pm-4:05pm
- Track/room: Autoresearch · Main Stage
- Speaker(s): Erina Karati, Arunachalam Manikandan
- Session type/status: session · confirmed

- Track: Autoresearch
- Room: Main Stage
- Session type: session
- Status: confirmed

## Session Description
Project Paradox is an existing multi-agent framework built at Supercell's first AI Innovation Lab, which has a 3D Unity village with local LLM powered agents. The characters remember conversations, update emotional state, track trust, plan actions, move through rooms, transfer items, and talk to each other through a FastAPI backend. The new work is an autoresearch layer around that village. We built a backend loop that runs controlled social scenarios, scores the resulting NPC behavior, proposes protocol or policy changes, reruns the suite, and keeps changes that improve the agents. The goal is to move beyond one good chat response and measure whether an NPC society can preserve source attribution, verify claims, spread important information, coordinate goals, and replan after new information arrives. The talk walks through the system architecture and the lessons from building it. We show the backend simulation harness that executes Unity style actions without opening Unity, the scenario suites that test information diffusion and memory provenance, and the ratchet loop that edits protocol text or planner policy with rollback. One accepted run improved information diffusion by teaching agents to broadcast important sourced evidence while preserving who said it. The practical takeaway is a reusable pattern for AI engineers building agents with messy state. Freeze the harness, expose a small editable policy surface, score real behavior instead of vibes, and let an agent search for improvements under rollback. The same pattern applies to game agents, coding agents, support agents, personal agents, and other systems where long horizon behavior matters more than a single response.

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
- [[erina-karati]]
- [[arunachalam-manikandan]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.

## Synthesis
### Synthesized Breakdown
# Autoresearch in a Multi-Agent AI Village ## Conference Context - Date/time: 2026-06-30 · 3:45pm-4:05pm - Track/room: Autoresearch · Main Stage - Speaker(s): Erina Karati, Arunachalam Manikandan - Session type/status: session · confirmed - Track: Autoresearch - Room: Main Stage - Session type: session - Status: confirmed ## Session Description Project Paradox is an existing multi-agent framework built at Supercell's first AI Innovation Lab, which has a 3D Unity village with local LLM powered agents. The characters remember conversations, update emotional state, track trust, plan actions, move through rooms, transfer items, and talk to each other through a FastAPI backend. The new work is an autoresearch layer around that village. We built a backend loop that runs controlled social scenarios, scores the resulting NPC behavior, proposes protocol or policy changes, reruns the suite, and keeps changes that improve the agents.

### Speaker And Company Context
- [[erina-karati|Erina Karati]] — Former Microsoft at [[supercell|Supercell]].
- [[arunachalam-manikandan|Arunachalam Manikandan]] — AI Engineer, Co-Founder at [[university-of-minnesota|University of Minnesota]].

### Topics Covered
- [[agent-security]]
- [[agentic-search]]
- [[coding-agents]]

### Derived Links And Source Material

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis is based on the official schedule and linked source pages. It should be revisited when exact session recordings or transcript-backed secondary sources are available.
