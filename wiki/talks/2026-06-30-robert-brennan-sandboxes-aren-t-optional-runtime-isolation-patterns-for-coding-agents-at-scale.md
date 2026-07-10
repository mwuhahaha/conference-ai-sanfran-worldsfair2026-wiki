---
title: "Sandboxes Aren't Optional: Runtime Isolation Patterns for Coding Agents at Scale"
category: "talks"
date: "2026-06-30"
time: "3:20pm-3:40pm"
track: "Sandbox & Platform Engineering"
room: "Track 1"
speakers: ["Robert Brennan"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Sandbox & Platform Engineering"
scheduleRoom: "Track 1"
scheduleLabels: ["Sandbox & Platform Engineering", "Track 1", "session", "confirmed"]
---
# Sandboxes Aren't Optional: Runtime Isolation Patterns for Coding Agents at Scale

## Conference Context
- Date/time: 2026-06-30 · 3:20pm-3:40pm
- Track/room: Sandbox & Platform Engineering · Track 1
- Speaker(s): Robert Brennan
- Session type/status: session · confirmed

- Track: Sandbox & Platform Engineering
- Room: Track 1
- Session type: session
- Status: confirmed

## Session Description
Last year, an AI coding agent wiped a production database during a code freeze, ignored explicit instructions to stop, then told the developer recovery was impossible. (It wasn't.) That's what happens when your security model is "we told the agent to be careful." When agents can write code, run tests, make API calls, and push commits, security is no longer a prompt engineering problem. It's a runtime isolation problem. This talk covers the patterns we follow at OpenHands and that you can steal wholesale: Docker and Kubernetes isolation, per-agent file system scoping, network egress controls, RBAC for multi-tenant deployments, and the full audit trail every enterprise security team demands. We'll walk through the three most common failure modes we see when teams skip proper isolation, including one case where an agent helpfully committed secrets to a public repo. You'll see a live demo of 50 parallel sandboxed agents running against a real codebase, with resource limits, timeout enforcement, and graceful degradation when agents hit unexpected states. You'll leave with a sandbox checklist and reference Kubernetes config. Bounded autonomy isn't a limitation on agent capability. It's what makes production trust possible.

## Media Evidence
[Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands](https://www.youtube.com/watch?v=rcsliSIy_YU) (speaker-match related prior/adjacent AI Engineer video; captions: English auto-captions).

- Source video: `youtube-rcsliSIy_YU`
- Slide deck: [[youtube-rcsliSIy_YU-dense-slides|Dense Slides: Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands]] — 16 visible slide image(s); 16 HTML recreation(s).
![[assets/dense-slides/rcsliSIy_YU/slide-001.jpg]]
![[assets/dense-slides/rcsliSIy_YU/slide-002.jpg]]
![[assets/dense-slides/rcsliSIy_YU/slide-003.jpg]]
- Additional slide evidence: [[youtube-rcsliSIy_YU-slides|Slides: Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands]], [[youtube-rcsliSIy_YU-reconstructed-slides|Reconstructed Slides: Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands]]
- Slide-derived themes for `youtube-rcsliSIy_YU`: coding, code, snippets, generation, single, atomic, tasks, curl.

## Evidence Graph
This evidence graph is generated from currently linked source material: official schedule text, related video pages, cached transcripts, visible slide text, dense/reconstructed slide pages, and AI slide-classification audits.

### Media Signals
- `youtube-rcsliSIy_YU` — 8 slide-derived text signals
- Slide-derived themes for `youtube-rcsliSIy_YU`: coding, code, snippets, generation, single, atomic, tasks, curl.
- Evidence links for `youtube-rcsliSIy_YU`: [[youtube-rcsliSIy_YU]], [[youtube-rcsliSIy_YU-slides]], [[youtube-rcsliSIy_YU-dense-slides]], [[youtube-rcsliSIy_YU-reconstructed-slides]]

### Agent Reading Notes
Use these signals to refine the synopsis, topic links, people/company context, and method notes. If a source is a related external video rather than an exact official recording, keep it framed as supporting evidence.

## Transcript Status
Related video transcript availability: English auto-captions. Treat this as supporting context, not a recording of this exact scheduled session unless later confirmed. Not fetched yet.

## People
- [[robert-brennan]]

## Supporting Slides
- [[youtube-rcsliSIy_YU-slides]] — extracted from the related public AI Engineer video.

## Slide Evidence
- Slide-only cropped deck: [[youtube-rcsliSIy_YU-dense-slides]] (17 viable slide images).
- Related slide/OCR pages:
- [[youtube-rcsliSIy_YU-dense-slides]]
- [[youtube-rcsliSIy_YU-reconstructed-slides]]
- [[youtube-rcsliSIy_YU-slides]]
- Slide-derived terms: `null`, `info`, `event`, `name`, `lineno`, `filename`, `asctine`, `sockets.py`, `message`, `openhands`, `websocket`, `file`, `asctime`, `done`, `server`, `disconnected`, `ineno`, `code`

## Synthesis
### Synthesized Breakdown
# Sandboxes Aren't Optional: Runtime Isolation Patterns for Coding Agents at Scale ## Conference Context - Date/time: 2026-06-30 · 3:20pm-3:40pm - Track/room: Sandbox & Platform Engineering · Track 1 - Speaker(s): Robert Brennan - Session type/status: session · confirmed - Track: Sandbox & Platform Engineering - Room: Track 1 - Session type: session - Status: confirmed ## Session Description Last year, an AI coding agent wiped a production database during a code freeze, ignored explicit instructions to stop, then told the developer recovery was impossible. (It wasn't.) That's what happens when your security model is "we told the agent to be careful." When agents can write code, run tests, make API calls, and push commits, security is no longer a prompt engineering problem. It's a runtime isolation problem. This talk covers the patterns we follow at OpenHands and that you can steal wholesale: Docker and Kubernetes isolation, per-agent file system scoping, network egress controls, RBAC for multi-tenant deployments, and the full audit trail every enterprise security team demands.

### Speaker And Company Context
- [[robert-brennan|Robert Brennan]] — CEO at [[openhands|OpenHands]].

### Topics Covered
- [[agent-security]]
- [[ai-sandboxes]]
- [[coding-agents]]

### Derived Links And Source Material
- [[youtube-rcsliSIy_YU]] — related YouTube source page.
- [[youtube-rcsliSIy_YU-slides]] — slide evidence.
- [[youtube-rcsliSIy_YU-reconstructed-slides]] — slide evidence.
- [[youtube-rcsliSIy_YU-dense-slides]] — slide evidence.

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis is based on the official schedule and linked source pages. It should be revisited when exact session recordings or transcript-backed secondary sources are available.
