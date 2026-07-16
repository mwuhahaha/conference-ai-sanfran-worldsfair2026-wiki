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
last_auto_summarized: '2026-07-06T07:16:20.383Z'
scheduleTrack: "Sandbox & Platform Engineering"
scheduleRoom: "Track 1"
scheduleLabels: ["Sandbox & Platform Engineering", "Track 1", "session", "confirmed"]
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

## Media Evidence
[Arrakis: How To Build An AI Sandbox From Scratch - Abhishek Bhardwaj, OpenAI](https://www.youtube.com/watch?v=wsFd22SL1s8) (speaker-match related prior/adjacent AI Engineer video; captions: English auto-captions).

- Source video: `youtube-wsFd22SL1s8`
- Slide deck: [[youtube-wsFd22SL1s8-dense-slides|Dense Slides: Arrakis: How To Build An AI Sandbox From Scratch - Abhishek Bhardwaj, OpenAI]] — 42 visible slide image(s); 42 HTML recreation(s).
![[assets/dense-slides/wsFd22SL1s8/slide-001.jpg]]
![[assets/dense-slides/wsFd22SL1s8/slide-002.jpg]]
![[assets/dense-slides/wsFd22SL1s8/slide-003.jpg]]
- Additional slide evidence: [[youtube-wsFd22SL1s8-slides|Slides: Arrakis: How To Build An AI Sandbox From Scratch - Abhishek Bhardwaj, OpenAI]], [[youtube-wsFd22SL1s8-reconstructed-slides|Reconstructed Slides: Arrakis: How To Build An AI Sandbox From Scratch - Abhishek Bhardwaj, OpenAI]]
- Slide-derived themes for `youtube-wsFd22SL1s8`: systems, chrome, code, sandboxes, operating, distributed, windows, subsystem.

## Evidence Graph
This evidence graph is generated from currently linked source material: official schedule text, related video pages, cached transcripts, visible slide text, dense/reconstructed slide pages, and AI slide-classification audits.

### Media Signals
- `youtube-OqM67QG_Ikk` — source page linked; role: primary event evidence.
- Evidence links for `youtube-OqM67QG_Ikk` (primary event evidence): [[youtube-OqM67QG_Ikk]]
- `youtube-wsFd22SL1s8` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-wsFd22SL1s8`: systems, chrome, code, sandboxes, operating, distributed, windows, subsystem.
- Evidence links for `youtube-wsFd22SL1s8` (supporting context only): [[youtube-wsFd22SL1s8]], [[youtube-wsFd22SL1s8-slides]], [[youtube-wsFd22SL1s8-dense-slides]], [[youtube-wsFd22SL1s8-reconstructed-slides]]

### Agent Reading Notes
Use these signals to refine the synopsis, topic links, people/company context, and method notes. If a source is a related external video rather than an exact official recording, keep it framed as supporting evidence.

## Summary
Abhishek Bhardwaj's World's Fair session is a Sandbox & Platform Engineering talk about the infrastructure layer that lets agents operate inside secure, real computing environments rather than toy execution sandboxes. The official session description frames the problem at cloud scale: compare runtime isolation technologies, decide how much kernel and process boundary protection is needed, make persistence and storage usable for longer-running agents, and orchestrate many sandbox instances as a production fleet. The connected speaker page adds useful context: Bhardwaj works on RL and agent infrastructure at OpenAI, so the session should be read as coming from the layer where agent training, tool use, and execution environments meet. The linked Arrakis video and slide pages are supporting evidence from a related public AI Engineer talk by the same speaker, not a confirmed recording of this exact World's Fair session, but they make the technical vocabulary concrete: Linux namespaces, containers, process cloning, mounts, filesystem snapshots, userspace behavior, syscalls, kernel boundaries, and attack surfaces. Together, the schedule and Arrakis materials point to a systems design talk about moving from a single sandbox runtime toward a fleet-scale agent sandbox cloud: how to isolate untrusted or semi-trusted agent work, how to preserve state without weakening security, and how to make sandbox orchestration reliable enough for production AI engineering workflows.

## Transcript Status
Related video transcript availability: English auto-captions. Treat this as supporting context, not a recording of this exact scheduled session unless later confirmed. Not fetched yet.

## People
- [[abhishek-bhardwaj]]

## Supporting Slides
- [[youtube-wsFd22SL1s8-slides]] — extracted from the related public AI Engineer video.

## Slide Evidence
- Slide-only cropped deck: [[youtube-wsFd22SL1s8-dense-slides]] (42 viable slide images).
- Related slide/OCR pages:
- [[youtube-wsFd22SL1s8-dense-slides]]
- [[youtube-wsFd22SL1s8-reconstructed-slides]]
- [[youtube-wsFd22SL1s8-slides]]
- Slide-derived terms: `namespace`, `arrakis`, `process`, `containers`, `kernel`, `container`, `linux`, `code`, `chatgpt`, `clone`, `mount`, `attack`, `snapshot`, `server`, `python`, `userspace`, `version`, `syscall`

## Official YouTube Recording
- [[youtube-OqM67QG_Ikk]] — official AI Engineer YouTube channel recording published 2026-07-08.
- Evidence status: transcript/slide enrichment pending.
- Boundary: use this recording as media evidence; keep date/time/room facts tied to the official schedule.

## Synthesis
### Synthesized Breakdown
# From fork() to Fleet: Designing an Agent Sandbox Cloud Pt2 ## Conference Context - Date/time: 2026-06-30 · 1:55pm-2:15pm - Track/room: Sandbox & Platform Engineering · Track 1 - Speaker(s): Abhishek Bhardwaj - Session type/status: session · confirmed - Track: Sandbox & Platform Engineering - Room: Track 1 - Session type: session - Status: confirmed ## Session Description Sandboxes unleash agents by giving them secure, fully functional computers where they can tackle diverse tasks with minimal setup. This talk explores the architectural challenges of building an agent sandbox cloud. We compare runtime isolation technologies and their trade-offs, examine persistence and storage as the next major unlock for agent capabilities, and discuss the key decisions involved in orchestrating and scaling sandboxes. ## Media Evidence [Arrakis: How To Build An AI Sandbox From Scratch - Abhishek Bhardwaj, OpenAI](https://www.youtube.com/watch?v=wsFd22SL1s8) (speaker-match related prior/adjacent AI Engineer video; captions: English auto-captions).

### Speaker And Company Context
- No speaker profile is attached in the official schedule data.

### Topics Covered
- [[agent-security]]
- [[ai-sandboxes]]
- [[coding-agents]]

### Derived Links And Source Material
- [[youtube-OqM67QG_Ikk]] — related YouTube source page.
- [[youtube-wsFd22SL1s8]] — related YouTube source page.
- [[youtube-wsFd22SL1s8-slides]] — slide evidence.
- [[youtube-wsFd22SL1s8-reconstructed-slides]] — slide evidence.
- [[youtube-wsFd22SL1s8-dense-slides]] — slide evidence.

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis is based on the official schedule and linked source pages. It should be revisited when exact session recordings or transcript-backed secondary sources are available.
