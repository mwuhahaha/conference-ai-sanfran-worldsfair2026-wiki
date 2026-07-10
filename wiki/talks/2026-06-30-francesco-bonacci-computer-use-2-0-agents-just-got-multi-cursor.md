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

## Evidence Graph
This evidence graph is generated from currently linked source material: official schedule text, related video pages, cached transcripts, visible slide text, dense/reconstructed slide pages, and AI slide-classification audits.

### Media Signals
No linked video, transcript, or slide source has been attached yet.

### Agent Reading Notes
Use these signals to refine the synopsis, topic links, people/company context, and method notes. If a source is a related external video rather than an exact official recording, keep it framed as supporting evidence.

## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## People
- [[francesco-bonacci]]
- [[dillon-dupont]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.

## Synthesis
### Synthesized Breakdown
# Computer-Use 2.0: Agents Just Got Multi-Cursor ## Conference Context - Date/time: 2026-06-30 · 2:25pm-2:45pm - Track/room: Computer Use · Track 7 - Speaker(s): Francesco Bonacci, Dillon DuPont - Session type/status: session · confirmed - Track: Computer Use - Room: Track 7 - Session type: session - Status: confirmed ## Session Description Computer-use agents still inherit a basic desktop limitation: one machine has one foreground app, one hardware cursor, and one active actor. Once you try to run more than one agent per desktop, they start stealing focus from the user and from each other. We built cua-driver around a different model: multiple agents operating real desktop applications in parallel, each with its own synthetic pointer, while the user's cursor and keyboard stay undisturbed. The key move is to stop treating hardware mouse and keyboard events as the primary automation layer.

### Speaker And Company Context
- [[francesco-bonacci|Francesco Bonacci]] — Co-founder & CEO at [[cua|Cua]].
- [[dillon-dupont|Dillon DuPont]] — CTO at [[cua|Cua]].

### Topics Covered
- Topic links are pending transcript-backed classification.

### Derived Links And Source Material

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis is based on the official schedule and linked source pages. It should be revisited when exact session recordings or transcript-backed secondary sources are available.
