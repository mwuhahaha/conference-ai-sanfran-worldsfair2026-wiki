---
title: "CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens"
category: "talks"
date: "2026-07-01"
time: "10:45am-11:05am"
track: "Graphs"
room: "Track 5"
speakers: ["Stephen Chin"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Graphs"
scheduleRoom: "Track 5"
scheduleLabels: ["Graphs", "Track 5", "sponsor", "confirmed"]
---
# CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens

## Conference Context
- Date/time: 2026-07-01 · 10:45am-11:05am
- Track/room: Graphs · Track 5
- Speaker(s): Stephen Chin
- Session type/status: sponsor · confirmed

- Track: Graphs
- Room: Track 5
- Session type: sponsor
- Status: confirmed

## Session Description
Autonomous assistants are easy to demo and hard to make reliable. The problem is usually not tool access. It is memory. Most assistant architectures still treat memory as a chat log plus vector retrieval. That is fine for document question answering, but it breaks down when the assistant must connect conversations, people, tools, and decisions across multiple tool iterations. For an AI engineer, a single request can depend on a Slack thread, a GitHub PR, a failed CI run, a calendar event, and prior operating preferences or constraints. These are not isolated pieces of context. They form a connected state that changes as work progresses and context grows. In this talk, I’ll show why knowledge graphs, context graphs, and GraphRAG provide a better foundation for OpenClaw-style assistants. Knowledge graphs capture durable entities and relationships. Context graphs capture the operational layer assistants usually lose, including actions, decision traces, provenance, and recency. GraphRAG turns that structure into task-time context by combining graph traversal, semantic retrieval, and tool use. Attendees will leave with practical patterns for schema design, retrieval routing, and evaluation, plus a concrete blueprint for assistants that remember more than the last prompt and retrieve more than the nearest chunk.

## Media Evidence
[Connecting the Dots with Context Graphs — Stephen Chin, Neo4j](https://www.youtube.com/watch?v=eW_vxrjvERk) (speaker-match related prior/adjacent AI Engineer video; captions: English auto-captions).

- Source video: `youtube-eW_vxrjvERk`
- Slide deck: [[youtube-eW_vxrjvERk-dense-slides|Dense Slides: Connecting the Dots with Context Graphs — Stephen Chin, Neo4j]] — 1 visible slide image(s); 1 HTML recreation(s).
![[assets/dense-slides/eW_vxrjvERk/slide-001.jpg]]
- Additional slide evidence: [[youtube-eW_vxrjvERk-slides|Slides: Connecting the Dots with Context Graphs — Stephen Chin, Neo4j]], [[youtube-eW_vxrjvERk-reconstructed-slides|Reconstructed Slides: Connecting the Dots with Context Graphs — Stephen Chin, Neo4j]]
- Slide-derived themes for `youtube-eW_vxrjvERk`: enter, conversations, github, memory, podcast, press, send, shit.

## Evidence Graph
This evidence graph is generated from currently linked source material: official schedule text, related video pages, cached transcripts, visible slide text, dense/reconstructed slide pages, and AI slide-classification audits.

### Media Signals
- `youtube-eW_vxrjvERk` — 3 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-eW_vxrjvERk`: enter, conversations, github, memory, podcast, press, send, shit.
- Evidence links for `youtube-eW_vxrjvERk` (supporting context only): [[youtube-eW_vxrjvERk]], [[youtube-eW_vxrjvERk-slides]], [[youtube-eW_vxrjvERk-dense-slides]], [[youtube-eW_vxrjvERk-reconstructed-slides]]

### Agent Reading Notes
Use these signals to refine the synopsis, topic links, people/company context, and method notes. If a source is a related external video rather than an exact official recording, keep it framed as supporting evidence.

## Transcript Status
Related video transcript availability: English auto-captions. Treat this as supporting context, not a recording of this exact scheduled session unless later confirmed. Not fetched yet.

## People
- [[stephen-chin]]

## Supporting Slides
- [[youtube-eW_vxrjvERk-slides]] — extracted from the related public AI Engineer video.

## Slide Evidence
- Slide-only cropped deck: [[youtube-eW_vxrjvERk-dense-slides]] (1 viable slide images).
- Related slide/OCR pages:
- [[youtube-eW_vxrjvERk-dense-slides]]
- [[youtube-eW_vxrjvERk-reconstructed-slides]]
- [[youtube-eW_vxrjvERk-slides]]
- Slide-derived terms: `graph`, `context`, `engineer`, `memory`, `europe`, `engineering`, `future`, `reasoning`, `entities`, `knowledge`, `relationships`, `enhance`, `relevance`, `domain`, `care`, `plans`, `associated`, `andrea`

## Synthesis
### Synthesized Breakdown
# CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens ## Conference Context - Date/time: 2026-07-01 · 10:45am-11:05am - Track/room: Graphs · Track 5 - Speaker(s): Stephen Chin - Session type/status: sponsor · confirmed - Track: Graphs - Room: Track 5 - Session type: sponsor - Status: confirmed ## Session Description Autonomous assistants are easy to demo and hard to make reliable. The problem is usually not tool access. It is memory. Most assistant architectures still treat memory as a chat log plus vector retrieval.

### Speaker And Company Context
- [[stephen-chin|Stephen Chin]] — VP of Developer Relations at [[neo4j|Neo4j]].

### Topics Covered
- [[agentic-search]]
- [[coding-agents]]

### Derived Links And Source Material
- [[youtube-eW_vxrjvERk]] — related YouTube source page.
- [[youtube-eW_vxrjvERk-slides]] — slide evidence.
- [[youtube-eW_vxrjvERk-reconstructed-slides]] — slide evidence.
- [[youtube-eW_vxrjvERk-dense-slides]] — slide evidence.

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis is based on the official schedule and linked source pages. It should be revisited when exact session recordings or transcript-backed secondary sources are available.
