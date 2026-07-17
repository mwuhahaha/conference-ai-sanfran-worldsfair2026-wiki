---
title: "Your agent needs a sandbox, not a desert"
category: "talks"
date: "2026-06-30"
time: "12:05pm-12:25pm"
track: "Sandbox & Platform Engineering"
room: "Track 1"
speakers: ["Samuel Colvin"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Sandbox & Platform Engineering"
scheduleRoom: "Track 1"
scheduleLabels: ["Sandbox & Platform Engineering", "Track 1", "session", "confirmed"]
---
# Your agent needs a sandbox, not a desert

## Conference Context
- Date/time: 2026-06-30 · 12:05pm-12:25pm
- Track/room: Sandbox & Platform Engineering · Track 1
- Speaker(s): Samuel Colvin
- Session type/status: session · confirmed

- Track: Sandbox & Platform Engineering
- Room: Track 1
- Session type: session
- Status: confirmed

## Session Description
Everyone agrees agents need code execution. That agreement lasts right up until you ask how to do it. The default answer is usually something like "My agent needs a full Linux VM to succeed". That's a very convenient answer for sandbox providers, but I think it's often incorrect. In many real-world agent workflows, the model does not need a whole computer. It does not need arbitrary packages, shell access, CPython, node, let alone `awk` `sed` and `gcc`. It needs a small amount of safe, expressive compute: enough to write code, call tools, and keep intermediate state out of the context window. That is the idea behind Monty: a minimal Python interpreter, written in Rust, designed specifically for running code written by agents. In this talk, I'll argue that for a surprisingly large class of agent systems, a curated set of tools in a custom runtime is better than a full sandbox. Not because full sandboxes are bad, but because they solve a much larger problem than most embedded agents actually have. And you pay for that mismatch in complexity, cost, operational pain, and 100,000X higher latency. Sandboxes are great, but there's such a thing as too much sand - in many scenarios the constraints and limitations of a custom built, minimal sandbox are a feature, not a bug.

## Synthesis
### Synthesized Breakdown
Everyone agrees agents need code execution. That agreement lasts right up until you ask how to do it. The default answer is usually something like "My agent needs a full Linux VM to succeed". That's a very convenient answer for sandbox providers, but I think it's often incorrect.

### Speaker And Company Context
- [[samuel-colvin|Samuel Colvin]] — Founder & CEO at [[pydantic|Pydantic]].

### Topics Covered
- [[agent-security]]
- [[ai-sandboxes]]
- [[coding-agents]]

### Derived Links And Source Material
- [[youtube-bmWZk9vTze0]] — related YouTube source page.
- [[youtube-bmWZk9vTze0-slides]] — slide evidence.
- [[youtube-bmWZk9vTze0-reconstructed-slides]] — slide evidence.
- [[youtube-bmWZk9vTze0-dense-slides]] — slide evidence.

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis is based on the official schedule and linked source pages. It should be revisited when exact session recordings or transcript-backed secondary sources are available.
## People
- [[samuel-colvin]]

## Slide Evidence
- Slide-only cropped deck: [[youtube-bmWZk9vTze0-dense-slides]] (1 viable slide images).
- Related slide/OCR pages:
- [[youtube-bmWZk9vTze0-dense-slides]]
- [[youtube-bmWZk9vTze0-reconstructed-slides]]
- [[youtube-bmWZk9vTze0-slides]]
- Slide-derived terms: `request`, `world`, `tool`, `response`, `call`, `sfair`, `microsoft`, `server`, `pydantic`, `smol`, `sampling`, `client`, `been`, `chat`, `toolcall`, `text`, `return`, `async`

## Media Evidence
- [[youtube-bmWZk9vTze0]] - supporting context; not the exact session recording.

- Source video: `youtube-bmWZk9vTze0`
- Slide deck: [[youtube-bmWZk9vTze0-dense-slides|Dense Slides: MCP is all you need — Samuel Colvin, Pydantic]] — slide evidence page.
- Additional slide evidence: [[youtube-bmWZk9vTze0-slides|Slides: MCP is all you need — Samuel Colvin, Pydantic]], [[youtube-bmWZk9vTze0-reconstructed-slides|Reconstructed Slides: MCP is all you need — Samuel Colvin, Pydantic]]
- Slide-derived themes for `youtube-bmWZk9vTze0`: query, client, info, table, tool, call, response, await.

## Transcript Status
Related video transcript availability: English auto-captions. Treat this as supporting context, not a recording of this exact scheduled session unless later confirmed. Not fetched yet.

## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-bmWZk9vTze0` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-bmWZk9vTze0`: query, client, info, table, tool, call, response, await.
- Evidence links for `youtube-bmWZk9vTze0` (supporting context only): [[youtube-bmWZk9vTze0]], [[youtube-bmWZk9vTze0-slides]], [[youtube-bmWZk9vTze0-dense-slides]], [[youtube-bmWZk9vTze0-reconstructed-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
