---
title: "Computer-Use 2.0: Agents Just Got Multi-Cursor"
category: "talks"
date: "2026-06-30"
time: "2:25pm-2:45pm"
track: "Computer Use"
room: "Track 7"
speakers: ["Francesco Bonacci", "Dillon DuPont"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Computer Use"
scheduleRoom: "Track 7"
scheduleLabels: ["Computer Use", "Track 7", "session", "confirmed"]
---
# Computer-Use 2.0: Agents Just Got Multi-Cursor

## Conference Context
- Date/time: 2026-06-30 · 2:25pm-2:45pm
- Track/room: Computer Use · Track 7
- Speaker(s): Francesco Bonacci, Dillon DuPont
- Session type/status: session · confirmed

- Track: Computer Use
- Room: Track 7
- Session type: session
- Status: confirmed

## Session Description
Computer-use agents still inherit a basic desktop limitation: one machine has one foreground app, one hardware cursor, and one active actor. Once you try to run more than one agent per desktop, they start stealing focus from the user and from each other. We built cua-driver around a different model: multiple agents operating real desktop applications in parallel, each with its own synthetic pointer, while the user's cursor and keyboard stay undisturbed. The key move is to stop treating hardware mouse and keyboard events as the primary automation layer. cua-driver goes one layer lower, into the OS plumbing behind accessibility: UI Automation on Windows, AT-SPI on Linux, and AX on macOS. Those APIs address applications and elements directly, so the OS does not require the target window to be frontmost. A click can land on a background window. A keystroke can reach a hidden one. Multiple agents can act at once because none of them is competing for the singleton hardware mouse. I'll walk through the architecture, the API shape, and the platform-specific traps we hit while making it work across Windows, macOS, and Linux. The live demo is three agents operating on one desktop while the user keeps typing uninterrupted. The goal is to make Computer-Use 2.0 feel concrete: what changes in the stack, what becomes possible, and where the approach still leaks, including Wayland, Chromium DOM surfaces, native canvas apps, and fallback input paths.

## Media Evidence
No related AI Engineer channel video found yet.

- [[youtube-ZSQb5fzRFPw-transcript]] — full cached transcript markdown for the related YouTube source.

- Source video: `youtube-ZSQb5fzRFPw`
- Slide deck: [[youtube-ZSQb5fzRFPw-slides|Slides: ZSQb5fzRFPw]] — 17 visible slide image(s).
![[assets/slides/ZSQb5fzRFPw/slide-001.jpg]]
![[assets/slides/ZSQb5fzRFPw/slide-002.jpg]]
![[assets/slides/ZSQb5fzRFPw/slide-003.jpg]]
- Slide-derived themes for `youtube-ZSQb5fzRFPw`: track, july, fair, computer, operator, loop, wired, model.

## Evidence Graph
This evidence graph is generated from currently linked source material: official schedule text, related video pages, cached transcripts, visible slide text, dense/reconstructed slide pages, and AI slide-classification audits.

### Media Signals
- `youtube-ZSQb5fzRFPw` — 2,617 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Transcript signals for `youtube-ZSQb5fzRFPw`: computer, take, over, driver, background, task, might, sandbox.
- Slide-derived themes for `youtube-ZSQb5fzRFPw`: track, july, fair, computer, operator, loop, wired, model.
- Evidence links for `youtube-ZSQb5fzRFPw` (primary event evidence): [[youtube-ZSQb5fzRFPw]], [[youtube-ZSQb5fzRFPw-transcript]], [[youtube-ZSQb5fzRFPw-slides]]

### Agent Reading Notes
Use these signals to refine the synopsis, topic links, people/company context, and method notes. If a source is a related external video rather than an exact official recording, keep it framed as supporting evidence.

## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## People
- [[francesco-bonacci]]
- [[dillon-dupont]]

## Synthesis
### Synthesized Breakdown
Thank you for taking the time for coming over here. Um I'm Franchesco. I'm the CEO of the company. Uh alongside me, a couple of other folks.

### Speaker And Company Context
- [[francesco-bonacci|Francesco Bonacci]] — Co-founder & CEO at [[cua|Cua]].
- [[dillon-dupont|Dillon DuPont]] — CTO at [[cua|Cua]].

### Topics Covered
- [[agent-security]]
- [[agentic-search]]
- [[ai-sandboxes]]
- [[coding-agents]]

### Derived Links And Source Material
- [[youtube-ZSQb5fzRFPw-transcript]] — transcript markdown; source cache `raw/sources/youtube-transcripts/ZSQb5fzRFPw.txt` (2,617 words).
- [[youtube-ZSQb5fzRFPw]] — related YouTube source page.
- [[youtube-ZSQb5fzRFPw-slides]] — slide evidence.

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis uses the official schedule plus cached video transcripts. Official AI Engineer World's Fair San Francisco 2026 livestreams and cut videos are primary event video sources for transcript/slide evidence; external, historical, or speaker-matched videos remain supporting context unless manually verified as exact official event recordings.

## Official YouTube Recording
- [[youtube-ZSQb5fzRFPw]] — official AI Engineer YouTube channel recording published 2026-07-15.
- Evidence status: [[youtube-ZSQb5fzRFPw-transcript]]; [[youtube-ZSQb5fzRFPw-slides]].
- Boundary: use this recording as media evidence; keep date/time/room facts tied to the official schedule.
