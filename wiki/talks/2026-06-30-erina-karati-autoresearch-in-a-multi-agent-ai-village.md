---
title: "Autoresearch in a Multi-Agent AI Village"
category: "talks"
date: "2026-06-30"
time: "3:45pm-4:05pm"
track: "Autoresearch"
room: "Main Stage"
speakers: ["Erina Karati", "Arunachalam Manikandan"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
---

# Autoresearch in a Multi-Agent AI Village

## Official Schedule Context
- Date/time: 2026-06-30 · 3:45pm-4:05pm
- Track/room: Autoresearch · Main Stage
- Speaker(s): Erina Karati, Arunachalam Manikandan
- Session type/status: session · confirmed

## Official Description
Project Paradox is an existing multi-agent framework built at Supercell's first AI Innovation Lab,

which has a 3D Unity village with local LLM powered agents. The characters remember conversations,

update emotional state, track trust, plan actions, move through rooms, transfer items, and talk to

each other through a FastAPI backend. The new work is an autoresearch layer around that village. We

built a backend loop that runs controlled social scenarios, scores the resulting NPC behavior,

proposes protocol or policy changes, reruns the suite, and keeps changes that improve the agents.

The goal is to move beyond one good chat response and measure whether an NPC society can preserve

source attribution, verify claims, spread important information, coordinate goals, and replan after

new information arrives. The talk walks through the system architecture and the lessons from

building it. We show the backend simulation harness that executes Unity style actions without

opening Unity, the scenario suites that test information diffusion and memory provenance, and the

ratchet loop that edits protocol text or planner policy with rollback. One accepted run improved

information diffusion by teaching agents to broadcast important sourced evidence while preserving

who said it. The practical takeaway is a reusable pattern for AI engineers building agents with

messy state. Freeze the harness, expose a small editable policy surface, score real behavior instead

of vibes, and let an agent search for improvements under rollback. The same pattern applies to game

agents, coding agents, support agents, personal agents, and other systems where long horizon

behavior matters more than a single response.

## Related YouTube Video
No related AI Engineer channel video found yet.

## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## People
- [[erina-karati]]
- [[arunachalam-manikandan]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.
