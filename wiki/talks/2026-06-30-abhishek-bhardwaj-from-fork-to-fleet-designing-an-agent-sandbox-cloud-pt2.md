---
title: 'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt2'
category: talks
date: '2026-06-30'
time: '1:55pm-2:15pm'
track: Sandbox & Platform Engineering
room: Track 1
speakers:
  - Abhishek Bhardwaj
sourceLabels:
  - Official conference schedule
  - Public YouTube metadata
last_auto_summarized: '2026-07-18T01:27:43.295Z'
scheduleTrack: Sandbox & Platform Engineering
scheduleRoom: Track 1
scheduleLabels:
  - Sandbox & Platform Engineering
  - Track 1
  - session
  - confirmed
---
# From fork() to Fleet: Designing an Agent Sandbox Cloud Pt2

## Conference Context
- Date/time: 2026-06-30 · 1:55pm-2:15pm
- Track/room: Sandbox & Platform Engineering · Track 1
- Speaker(s): Abhishek Bhardwaj
- Session type/status: session · confirmed

- Track: Sandbox & Platform Engineering
- Room: Track 1
- Session type: session
- Status: confirmed

## Session Description
Sandboxes unleash agents by giving them secure, fully functional computers where they can tackle diverse tasks with minimal setup. This talk explores the architectural challenges of building an agent sandbox cloud. We compare runtime isolation technologies and their trade-offs, examine persistence and storage as the next major unlock for agent capabilities, and discuss the key decisions involved in orchestrating and scaling sandboxes.

## Summary
Abhishek Bhardwaj’s session examines the transition from creating one isolated execution environment with fork-like primitives to operating a secure, persistent fleet of computers for AI agents. The exact session now has a dedicated official recording, a 7,738-word transcript, and 15 visible slide images, making it the primary evidence for the talk rather than relying on the earlier Arrakis presentation. Bhardwaj’s role building RL and agent infrastructure at [[openai|OpenAI]] places the discussion where agent training, tool use, and production execution meet: [[coding-agents]] and other tool-using systems need enough freedom to write and run code, install dependencies, inspect files, and retain artifacts, while the platform must prevent those workloads from escaping into the host or interfering with one another.

The architectural problem spans several connected layers. Runtime isolation determines the boundary between host and guest behavior, including the use of processes, Linux namespaces, containers, syscalls, and kernel-level protection. Persistence introduces mounts, filesystem snapshots, and durable storage so an agent can continue a long-running task instead of losing its environment after each execution, but retained state also expands the security and lifecycle responsibilities of the platform. Fleet orchestration then has to turn those individual sandboxes into a dependable service that can create, schedule, monitor, recover, and scale many environments without weakening isolation. In that sense, [[ai-sandboxes]] are not merely code runners: they are a platform control plane whose capability model, storage design, and attack surface directly shape [[agent-security]].

The linked Arrakis recording and reconstructed slide sets remain valuable supporting context because they expose the implementation vocabulary behind the same design space—process cloning, namespaces, mounts, snapshots, userspace behavior, syscalls, kernel boundaries, and attack surfaces—but they are not evidence for the precise contents of this scheduled session. Taken together, the official World’s Fair recording and the related systems material frame the sandbox cloud as foundational agent infrastructure: a way to provide reproducible computers with durable working state while preserving strong boundaries and fleet-level reliability for production agent workflows, training, and [[agent-evaluations]].

## Synthesis
### Synthesized Breakdown
Welcome everyone. Can you guys hear me okay? I've been standing here for 15 minutes without saying anything, so we can start now. My name is Abhishek.

### Speaker And Company Context
- No speaker profile is attached in the official schedule data.

### Topics Covered
- [[agent-security]]
- [[agentic-search]]
- [[ai-sandboxes]]
- [[coding-agents]]

### Derived Links And Source Material
- [[youtube-OqM67QG_Ikk-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/OqM67QG_Ikk.txt` (7,738 words).
- [[youtube-OqM67QG_Ikk]] — related YouTube source page.
- [[youtube-OqM67QG_Ikk-slides]] — slide evidence.
- [[youtube-wsFd22SL1s8]] — related YouTube source page.
- [[youtube-wsFd22SL1s8-slides]] — slide evidence.
- [[youtube-wsFd22SL1s8-reconstructed-slides]] — slide evidence.
- [[youtube-wsFd22SL1s8-dense-slides]] — slide evidence.

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis uses the official schedule and only a dedicated manifest-matched recording transcript for session-level claims and topic extraction. Related official-channel, external, and broad livestream sources remain supporting context and do not stand in for the scheduled session.
## People
- [[abhishek-bhardwaj]]

## Slide Evidence
- Slide-only cropped deck: [[youtube-wsFd22SL1s8-dense-slides]] (42 viable slide images).
- Related slide/OCR pages:
- [[youtube-wsFd22SL1s8-dense-slides]]
- [[youtube-wsFd22SL1s8-reconstructed-slides]]
- [[youtube-wsFd22SL1s8-slides]]
- Slide-derived terms: `namespace`, `arrakis`, `process`, `containers`, `kernel`, `container`, `linux`, `code`, `chatgpt`, `clone`, `mount`, `attack`, `snapshot`, `server`, `python`, `userspace`, `version`, `syscall`

## Official YouTube Recording
- [[youtube-OqM67QG_Ikk|From fork() to Fleet: Designing an Agent Sandbox Cloud — Abhishek Bhardwaj, OpenAI]] — official AI Engineer YouTube recording published 2026-07-13.
- Evidence status: [[youtube-OqM67QG_Ikk-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-OqM67QG_Ikk]] - dedicated official event recording.
- [[youtube-OqM67QG_Ikk-transcript]] - dedicated official recording transcript.
- [[youtube-wsFd22SL1s8]] - supporting context; not the exact session recording.

- Source video: `youtube-OqM67QG_Ikk`
- Slide deck: [[youtube-OqM67QG_Ikk-slides|Slides: From fork() to Fleet: Designing an Agent Sandbox Cloud — Abhishek Bhardwaj, OpenAI]] — 15 visible slide image(s).
![[assets/slides/OqM67QG_Ikk/slide-001.jpg]]
![[assets/slides/OqM67QG_Ikk/slide-002.jpg]]
![[assets/slides/OqM67QG_Ikk/slide-003.jpg]]
- Slide-derived themes for `youtube-OqM67QG_Ikk`: engineering, sandbox, platform, track, july, security, fork, fleet.
- Source video: `youtube-wsFd22SL1s8`
- Slide deck: [[youtube-wsFd22SL1s8-dense-slides|Dense Slides: Arrakis: How To Build An AI Sandbox From Scratch - Abhishek Bhardwaj, OpenAI]] — slide evidence page.
- Additional slide evidence: [[youtube-wsFd22SL1s8-slides|Slides: Arrakis: How To Build An AI Sandbox From Scratch - Abhishek Bhardwaj, OpenAI]], [[youtube-wsFd22SL1s8-reconstructed-slides|Reconstructed Slides: Arrakis: How To Build An AI Sandbox From Scratch - Abhishek Bhardwaj, OpenAI]]
- Slide-derived themes for `youtube-wsFd22SL1s8`: clone, flask, project, code, create, scratch, systems, chat.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/OqM67QG_Ikk.txt` (7,738 words).

## Transcript Markdown
- [[youtube-OqM67QG_Ikk-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/OqM67QG_Ikk.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-OqM67QG_Ikk` — 7,738 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-OqM67QG_Ikk`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-OqM67QG_Ikk`: kernel, many, system, code, host, guest, block, running.
- Slide-derived themes for `youtube-OqM67QG_Ikk`: engineering, sandbox, platform, track, july, security, fork, fleet.
- Evidence links for `youtube-OqM67QG_Ikk` (primary event evidence): [[youtube-OqM67QG_Ikk]], [[youtube-OqM67QG_Ikk-transcript]], [[youtube-OqM67QG_Ikk-slides]]
- `youtube-wsFd22SL1s8` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-wsFd22SL1s8`: clone, flask, project, code, create, scratch, systems, chat.
- Evidence links for `youtube-wsFd22SL1s8` (supporting context only): [[youtube-wsFd22SL1s8]], [[youtube-wsFd22SL1s8-slides]], [[youtube-wsFd22SL1s8-dense-slides]], [[youtube-wsFd22SL1s8-reconstructed-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
