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

## Synthesis
### Synthesized Breakdown
My name's Steven Chin. I run the developer relations team here at Neo Forj. And I'm excited to talk to you about something we've all come to love, our our crustaceian friends. So, we have um um openclaw mascot.

### Speaker And Company Context
- [[stephen-chin|Stephen Chin]] — VP of Developer Relations at [[neo4j|Neo4j]].

### Topics Covered
- [[agent-security]]
- [[agentic-search]]
- [[coding-agents]]
- [[mcp]]

### Derived Links And Source Material
- [[youtube-Q0VkgCyNVUg-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/Q0VkgCyNVUg.txt` (3,266 words).
- [[youtube-Q0VkgCyNVUg]] — related YouTube source page.
- [[youtube-Q0VkgCyNVUg-slides]] — slide evidence.
- [[youtube-eW_vxrjvERk]] — related YouTube source page.
- [[youtube-eW_vxrjvERk-slides]] — slide evidence.
- [[youtube-eW_vxrjvERk-reconstructed-slides]] — slide evidence.
- [[youtube-eW_vxrjvERk-dense-slides]] — slide evidence.

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis uses the official schedule and only a dedicated manifest-matched recording transcript for session-level claims and topic extraction. Related official-channel, external, and broad livestream sources remain supporting context and do not stand in for the scheduled session.
## People
- [[stephen-chin]]

## Slide Evidence
- Slide-only cropped deck: [[youtube-eW_vxrjvERk-dense-slides]] (1 viable slide images).
- Related slide/OCR pages:
- [[youtube-eW_vxrjvERk-dense-slides]]
- [[youtube-eW_vxrjvERk-reconstructed-slides]]
- [[youtube-eW_vxrjvERk-slides]]
- Slide-derived terms: `graph`, `context`, `engineer`, `memory`, `europe`, `engineering`, `future`, `reasoning`, `entities`, `knowledge`, `relationships`, `enhance`, `relevance`, `domain`, `care`, `plans`, `associated`, `andrea`

## Official YouTube Recording
- [[youtube-Q0VkgCyNVUg|CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens — Stephen Chin, Neo4j]] — official AI Engineer YouTube recording published 2026-07-22.
- Evidence status: [[youtube-Q0VkgCyNVUg-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-Q0VkgCyNVUg]] - dedicated official event recording.
- [[youtube-Q0VkgCyNVUg-transcript]] - dedicated official recording transcript.
- [[youtube-eW_vxrjvERk]] - supporting context; not the exact session recording.

- [[youtube-Q0VkgCyNVUg-slides]] — extracted from the related public AI Engineer video.

- Source video: `youtube-Q0VkgCyNVUg`
- Slide deck: [[youtube-Q0VkgCyNVUg-slides|Slides: CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens — Stephen Chin, Neo4j]] — 22 visible slide image(s).
![[assets/slides/Q0VkgCyNVUg/slide-001.jpg]]
![[assets/slides/Q0VkgCyNVUg/slide-002.jpg]]
![[assets/slides/Q0VkgCyNVUg/slide-003.jpg]]
- Slide-derived themes for `youtube-Q0VkgCyNVUg`: shell, track, july, skills, meat, engineering, future, wakes.
- Source video: `youtube-eW_vxrjvERk`
- Slide deck: [[youtube-eW_vxrjvERk-dense-slides|Dense Slides: Connecting the Dots with Context Graphs — Stephen Chin, Neo4j]] — slide evidence page.
- Additional slide evidence: [[youtube-eW_vxrjvERk-slides|Slides: Connecting the Dots with Context Graphs — Stephen Chin, Neo4j]], [[youtube-eW_vxrjvERk-reconstructed-slides|Reconstructed Slides: Connecting the Dots with Context Graphs — Stephen Chin, Neo4j]]
- Slide-derived themes for `youtube-eW_vxrjvERk`: context, slack, knowledge, enhance, relevance, domain, alternatives, considered.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/Q0VkgCyNVUg.txt` (3,266 words).

## Transcript Markdown
- [[youtube-Q0VkgCyNVUg-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/Q0VkgCyNVUg.txt`.

## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-Q0VkgCyNVUg` — 3,266 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-Q0VkgCyNVUg`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-Q0VkgCyNVUg`: graph, memory, vector, files, demo, information, great, store.
- Slide-derived themes for `youtube-Q0VkgCyNVUg`: shell, track, july, skills, meat, engineering, future, wakes.
- Evidence links for `youtube-Q0VkgCyNVUg` (primary event evidence): [[youtube-Q0VkgCyNVUg]], [[youtube-Q0VkgCyNVUg-transcript]], [[youtube-Q0VkgCyNVUg-slides]]
- `youtube-eW_vxrjvERk` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-eW_vxrjvERk`: context, slack, knowledge, enhance, relevance, domain, alternatives, considered.
- Evidence links for `youtube-eW_vxrjvERk` (supporting context only): [[youtube-eW_vxrjvERk]], [[youtube-eW_vxrjvERk-slides]], [[youtube-eW_vxrjvERk-dense-slides]], [[youtube-eW_vxrjvERk-reconstructed-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
