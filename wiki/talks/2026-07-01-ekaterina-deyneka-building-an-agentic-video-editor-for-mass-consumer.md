---
title: "Building an Agentic Video Editor for Mass Consumer"
category: "talks"
date: "2026-07-01"
time: "11:40am-12:00pm"
track: "Generative Media"
room: "Track 1"
speakers: ["Ekaterina Deyneka"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Generative Media"
scheduleRoom: "Track 1"
scheduleLabels: ["Generative Media", "Track 1", "session", "confirmed"]
---
# Building an Agentic Video Editor for Mass Consumer

## Official Schedule Context
- Date/time: 2026-07-01 · 11:40am-12:00pm
- Track/room: Generative Media · Track 1
- Speaker(s): Ekaterina Deyneka
- Session type/status: session · confirmed

## Schedule Labels
- Track: Generative Media
- Room: Track 1
- Session type: session
- Status: confirmed

## Official Description
Most agentic systems today are built for developers — people comfortable setting up environment,

configs, and debugging agent loops. But what happens when your user has never heard the word "agent"

and just wants a video ready to post? Reelful is an agentic video editor that lives right in the

user's phone. It turns raw photos and videos from your camera roll into polished, short videos. No

setup. No sophisticated prompting. No empty timeline. Under the hood, the agent orchestrates

multiple models and composes a video together. In this talk, I'll walk through: * The agentic

pipeline architecture: how we chain models across modalities (vision → language → speech → video),

handle context passing between steps, and manage state across a multi-minute generation job * The UX

inversion: how we designed the agent to require minimal effort from user — the system infers intent

from the media itself, making complex orchestration invisible This talk is for anyone building

agents that need to work for non-technical users, or anyone curious about multimodal agentic

pipelines beyond text and code.

## Related YouTube Video
No related AI Engineer channel video found yet.

## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## People
- [[ekaterina-deyneka]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.

## External Secondary Source Candidates
These videos were discovered outside the official AI Engineer channel and matched by the external-video discovery tool. Treat them as secondary sources only until manually verified against the official event recording.

- [AI Engineer World's Fair: Building Reelful - Agentic Video Editor](https://www.youtube.com/watch?v=AheG9p_JXVw)
  - Uploader: Kate | AI Founder · Building Reelful
  - Confidence: high (0.74)
  - Match evidence: event marker in title/metadata; ordered title phrase match 0.50; company match: Reelful; talk/session-shaped title; plausible talk/workshop duration
  - Transcript status: captions_imported `raw/sources/external-youtube-transcripts/AheG9p_JXVw.txt`

## Transcript Markdown
- [[youtube-AheG9p_JXVw-transcript]] — full cached transcript markdown for the related YouTube source.

## Synthesis
### Synthesized Breakdown
Ekaterina Deyneka frames Reelful as an agentic video editor for non-technical mobile users. The workflow starts with a user's photos, clips, and lightweight direction, then uses an agent to understand media, transcribe speech, select the best moments, assemble a composition, and generate supporting assets such as captions, music, voiceover, B-roll, and animated photos.

The technical comparison is to an agentic app builder: both use a prompt, a working artifact, a sandboxed execution environment, agent tools or skills, and a rendered preview. The difference is that Reelful edits real footage rather than generating from a blank canvas, so the agent must handle messy source material, infer user intent, preserve useful moments, and verify that the final Remotion-based composition renders cleanly.

The product lesson is that complex agent workflows should disappear behind simple UX for mass consumers. Reelful uses a mobile-first interface, directional templates, and an optional built-in editor so users can start with an agent-generated cut and make small familiar adjustments afterward.

### Speaker And Company Context
- [[ekaterina-deyneka|Ekaterina Deyneka]] — Founder & CEO at [[reelful|Reelful]].

### Topics Covered
- [[ai-sandboxes]]
- [[coding-agents]]
- [[voice-agents]]

### Derived Links And Source Material
- [[youtube-AheG9p_JXVw-transcript]] — transcript markdown; source cache `raw/sources/external-youtube-transcripts/AheG9p_JXVw.txt` (1,340 words).
- [[youtube-AheG9p_JXVw-slides]] — slide evidence.

### Novel Concepts / Clever Methods
- Treating an agentic video editor as the media equivalent of an agentic app builder: a sandboxed agent writes and verifies a video composition rather than a code app.
- Using Remotion-style video-as-code as the agent's editable/renderable artifact, with a verification layer that catches composition problems and lets the agent iterate.
- Hiding a multimodal agent pipeline behind consumer UX primitives: mobile capture, directional templates, and manual editor escape hatches.

### Evidence Boundary
This synthesis uses the official schedule plus cached related-video transcripts. Related videos remain supporting context unless explicitly verified as exact session recordings.
