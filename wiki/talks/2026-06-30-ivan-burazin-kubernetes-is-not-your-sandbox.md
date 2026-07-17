---
title: "Kubernetes Is Not Your Sandbox"
category: "talks"
date: "2026-06-30"
time: "11:40am-12:00pm"
track: "Sandbox & Platform Engineering"
room: "Track 1"
speakers: ["Ivan Burazin"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Sandbox & Platform Engineering"
scheduleRoom: "Track 1"
scheduleLabels: ["Sandbox & Platform Engineering", "Track 1", "session", "confirmed"]
---
# Kubernetes Is Not Your Sandbox

## Conference Context
- Date/time: 2026-06-30 · 11:40am-12:00pm
- Track/room: Sandbox & Platform Engineering · Track 1
- Speaker(s): Ivan Burazin
- Session type/status: session · confirmed

- Track: Sandbox & Platform Engineering
- Room: Track 1
- Session type: session
- Status: confirmed

## Session Description
Teams are reaching for Kubernetes to run agent sandboxes, and it's the wrong tool. Kubernetes is built to keep things alive and hold them in a steady state. A sandbox is born, forked, and killed before any of that machinery catches up. The mismatch compounds because the sandbox keeps gaining requirements without shedding any. In eighteen months it went from a fast code-snippet runner, to a stateful box for long-running agents, to ten thousand ephemeral environments that fork for RL rollouts and die in under a second. It has to be all of those at once, a contradiction set no orchestrator was designed to hold. The cost shows up the moment you measure it. We ran the same 50-action bug-fix trajectory across five stacks and got a 12x spread: 12.9s on the fastest, 161.5s on the slowest. The gap isn't compute, it's lifecycle overhead per action. We name every stack and explain the mechanism behind each number. wdyt?

## Synthesis
### Synthesized Breakdown
Teams are reaching for Kubernetes to run agent sandboxes, and it's the wrong tool. Kubernetes is built to keep things alive and hold them in a steady state. A sandbox is born, forked, and killed before any of that machinery catches up. The mismatch compounds because the sandbox keeps gaining requirements without shedding any.

### Speaker And Company Context
- [[ivan-burazin|Ivan Burazin]] — CEO at [[daytona|Daytona]].

### Topics Covered
- [[ai-sandboxes]]
- [[coding-agents]]

### Derived Links And Source Material
- [[youtube-e9sLVMN76qU]] — related YouTube source page.
- [[youtube-e9sLVMN76qU-slides]] — slide evidence.
- [[youtube-e9sLVMN76qU-reconstructed-slides]] — slide evidence.

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis is based on the official schedule and linked source pages. It should be revisited when exact session recordings or transcript-backed secondary sources are available.
## People
- [[ivan-burazin]]

## Media Evidence
No exact recording or transcript evidence is attached yet; the official schedule remains the source for this session.
## Transcript Status
Related video transcript availability: English auto-captions. Treat this as supporting context, not a recording of this exact scheduled session unless later confirmed. Not fetched yet.

## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
No linked video, transcript, or slide source has been attached yet.

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
