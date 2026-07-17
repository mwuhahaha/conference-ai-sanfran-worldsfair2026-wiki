---
title: "Give the Agent a Budget, Not a Token"
category: "talks"
date: "2026-07-01"
time: "3:20pm-3:40pm"
track: "AI Architects: AI Factories"
room: "Leadership 2"
speakers: ["Sachin Malhotra"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "AI Architects: AI Factories"
scheduleRoom: "Leadership 2"
scheduleLabels: ["AI Architects: AI Factories", "Leadership 2", "session", "confirmed"]
---
# Give the Agent a Budget, Not a Token

## Conference Context
- Date/time: 2026-07-01 · 3:20pm-3:40pm
- Track/room: AI Architects: AI Factories · Leadership 2
- Speaker(s): Sachin Malhotra
- Session type/status: session · confirmed

- Track: AI Architects: AI Factories
- Room: Leadership 2
- Session type: session
- Status: confirmed

## Session Description
Every agent demo runs with a god-token. Then it ships, and someone has to explain why the helpful AI just rm -rf'd the staging database "to clean up." I run platform infrastructure at a frontier lab, and for the last year my job has partly been: let coding agents do real work against real systems, without ever having to write the postmortem. This talk is the permission model that fell out of that - not RBAC-with-extra-steps, but primitives designed for an actor that's smart, fast, tireless, and occasionally *confidently wrong*. **The four primitives:** - **Asymmetric verbs** - the agent can `quarantine` but not `delete`, `retry` but not `approve`, `propose` but not `merge`. The verb list *is* the security boundary. Stop thinking in resources, start thinking in reversible vs. irreversible actions. - **Regenerating budgets** - every agent identity gets N disruptive actions per window. Burn the budget, you're benched until it refills. No human-in-the-loop until the budget's gone — which means 95% autonomy with a hard ceiling on blast radius. - **The undo test** - if the agent can't undo it, the agent can't do it without a second key. One line, surprisingly load-bearing. - **Tripwires over allow-lists** - let the agent roam, but instrument the three actions that would actually hurt. Cheaper than enumerating everything safe. I'll show the ~200-line policy layer that implements all four, the failure modes each one exists to catch, and the one design I shipped that turned out to be security theater. Tool-agnostic - works whether your agent is touching CI, a database, a cloud account, or your users' files. If you're shipping an agent that does anything more than read, you'll leave with a threat model and a starting policy you can paste into your repo on the flight home.

## Synthesis
### Synthesized Breakdown
Every agent demo runs with a god-token. Then it ships, and someone has to explain why the helpful AI just rm -rf'd the staging database "to clean up." I run platform infrastructure at a frontier lab, and for the last year my job has partly been: let coding agents do real work against real systems, without ever having to write the postmortem. This talk is the permission model that fell out of that - not RBAC-with-extra-steps, but primitives designed for an actor that's smart, fast, tireless, and occasionally *confidently wrong*. **The four primitives:** - **Asymmetric verbs** - the agent can `quarantine` but not `delete`, `retry` but not `approve`, `propose` but not `merge`.

### Speaker And Company Context
- [[sachin-malhotra|Sachin Malhotra]] — Member of Technical Staff at [[anthropic|Anthropic]].

### Topics Covered
- [[agent-security]]
- [[coding-agents]]

### Derived Links And Source Material

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis is based on the official schedule and linked source pages. It should be revisited when exact session recordings or transcript-backed secondary sources are available.
## People
- [[sachin-malhotra]]

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
