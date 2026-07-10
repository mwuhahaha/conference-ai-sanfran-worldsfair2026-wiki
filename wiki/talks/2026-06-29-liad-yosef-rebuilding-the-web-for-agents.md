---
title: "Rebuilding the web for agents"
category: "talks"
date: "2026-06-29"
time: "12:05pm-12:25pm"
track: "Search & Retrieval"
room: "Track 3"
speakers: ["Liad Yosef"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Search & Retrieval"
scheduleRoom: "Track 3"
scheduleLabels: ["Search & Retrieval", "Track 3", "session", "confirmed"]
---
# Rebuilding the web for agents

## Conference Context
- Date/time: 2026-06-29 · 12:05pm-12:25pm
- Track/room: Search & Retrieval · Track 3
- Speaker(s): Liad Yosef
- Session type/status: session · confirmed

- Track: Search & Retrieval
- Room: Track 3
- Session type: session
- Status: confirmed

## Session Description
AI apps are the new browsers. And the web is not ready. For thirty years we built the web for human eyes, benchmarked by tools like Lighthouse: humans measuring human behavior. That era is ending. Bot traffic has overtaken human traffic, and we can't hand-write a benchmark for what comes next - every best practice goes stale the moment models improve. Your next customer isn't a human with a credit card - it's an agent with a protocol, and it would rather not see your interface at all. That shift moves the UX question from how a human experiences your product to how an agent does, and how a human experiences that agent. Already, some services report their MCP traffic outpacing their web UI. The agent is rapidly becoming the main surface, and it always takes the path of least friction. Claude Code might consistently prefer PostHog over Mixpanel simply because PostHog *has the better agentic surface* - and Mixpanel loses customers without a human ever weighing in. Meanwhile the agentic web protocol stack keeps multiplying, a new one seemingly every week. The harder problem isn't discovery - it's operability: whether the web can actually be run once an agent arrives, and what is the ideal stack for that. Should we lean into headless protocols, or ones like WebMCP that treat the UI as the source of truth? Does a site need to implement every new spec just to support every kind of agent? So we stopped guessing and watched real agents work the whole journey: finding, understanding, authenticating, acting, handing back to a human. The findings go against the last year of agent-readiness advice. Agents ignore the files we built for them, reaching for docs and homepages instead - and whatever they reach, they trust and act on. But when those files are linked properly, their usage jumps 4x. The format isn't the key for the agentic web. Reachability is. The web will never be completely headless. Some moments still demand a human: choosing a seat, comparing options, casually exploring. And agents aren't uniform - some want full headless access, others spin up a browser to fill the gaps, but that's a friction point, not a free fallback. So the web is going nearly headless, always with a human eye at the end. This talk maps the entire agent web landscape based on findings from real agent journeys research:

- Which protocols earn their place and which are noise.
- Why "agent-ready" and "accessible" are the same engineering problem.
- How MCP Apps close the last mile - and when headful protocols like WebMCP step in.
- How to build for agent-readiness that survives the next model - not a checklist that's stale in a month. The gap between ready and not is about to separate the relevant from the invisible.

## Media Evidence
[MCP UI: Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps](https://www.youtube.com/watch?v=o-zkvb0iFDQ) (speaker-match related prior/adjacent AI Engineer video; captions: English auto-captions).

- [[youtube-o-zkvb0iFDQ-transcript]] — full cached transcript markdown for the related YouTube source.

These are phone-photo slide captures from the Google Photos `AIE Slides` album. They are supporting slide evidence and do not override official schedule fields.
- [[google-photos-aie-slides-9gWZzS1EpXM1C5eK6-rebuilding-the-web-for-agents-slides]] - Google Photos Slides: Rebuilding the Web for Agents (confidence: high).

- Source video: `youtube-o-zkvb0iFDQ`
- Slide deck: [[youtube-o-zkvb0iFDQ-dense-slides|Dense Slides: MCP UI: Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps]] — 1 visible slide image(s); 1 HTML recreation(s).
![[assets/dense-slides/o-zkvb0iFDQ/slide-001.jpg]]
- Additional slide evidence: [[youtube-o-zkvb0iFDQ-slides|Slides: MCP UI: Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps]], [[youtube-o-zkvb0iFDQ-reconstructed-slides|Reconstructed Slides: MCP UI: Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps]]
- Slide-derived themes for `youtube-o-zkvb0iFDQ`: engineering, future.

## Evidence Graph
This evidence graph is generated from currently linked source material: official schedule text, related video pages, cached transcripts, visible slide text, dense/reconstructed slide pages, and AI slide-classification audits.

### Media Signals
- `youtube-o-zkvb0iFDQ` — 3,969 transcript words; 1 slide-derived text signals
- Transcript signals for `youtube-o-zkvb0iFDQ`: apps, host, claude, back, chatgpt, look, mcpui, chat.
- Slide-derived themes for `youtube-o-zkvb0iFDQ`: engineering, future.
- Evidence links for `youtube-o-zkvb0iFDQ`: [[youtube-o-zkvb0iFDQ]], [[youtube-o-zkvb0iFDQ-transcript]], [[youtube-o-zkvb0iFDQ-slides]], [[youtube-o-zkvb0iFDQ-dense-slides]], [[youtube-o-zkvb0iFDQ-reconstructed-slides]]

### Agent Reading Notes
Use these signals to refine the synopsis, topic links, people/company context, and method notes. If a source is a related external video rather than an exact official recording, keep it framed as supporting evidence.

## Transcript Status
Related video transcript availability: English auto-captions. The transcript has been fetched and converted to [[youtube-o-zkvb0iFDQ-transcript]]. Treat this as supporting context, not a recording of this exact scheduled session unless later confirmed.

## People
- [[liad-yosef]]

## Notes
- This page now includes source-backed synthesis from the official schedule and the related Liad/Ido MCP UI transcript. Revisit if a confirmed exact recording of this scheduled session is published.

## Supporting Slides
- [[youtube-o-zkvb0iFDQ-slides]] — extracted from the related public AI Engineer video.

## Slide Evidence
- Slide-only cropped deck: [[youtube-o-zkvb0iFDQ-dense-slides]] (1 viable slide images).
- Related slide/OCR pages:
- [[youtube-o-zkvb0iFDQ-dense-slides]]
- [[youtube-o-zkvb0iFDQ-reconstructed-slides]]
- [[youtube-o-zkvb0iFDQ-slides]]
- Slide-derived terms: `future`, `engineering`, `apps`, `alengineer`, `europe`, `engineer`, `aiengineer`, `mcp-ui`, `host`, `braintrust`, `workos`, `openal`, `rene`, `morrow`, `server`, `claude`, `architecture`, `sandbox`

## Synthesis
### Synthesized Breakdown
This talk argues that AI apps are becoming the new browsers, so the web has to be designed for agents as operators, not only for human readers. It breaks agentic-web readiness into the whole journey of discovery, understanding, authentication, action, and human handoff. The key finding is reachability over format: agent-facing files and specs only help when agents can actually find them from trusted surfaces such as docs and homepages. The resulting design frame is a nearly headless web, where agents handle most execution while human-visible checkpoints remain available for judgment, comparison, and consent.

### Speaker And Company Context
- [[liad-yosef|Liad Yosef]] — Co-creator at [[mcp-apps|MCP Apps]].

### Topics Covered
- [[agent-security]]
- [[agentic-search]]
- [[agentic-web]]
- [[ai-sandboxes]]
- [[coding-agents]]
- [[mcp]]
- [[mcp-apps]]

### Derived Links And Source Material
- [[youtube-o-zkvb0iFDQ-transcript]] — transcript markdown; source cache `raw/sources/youtube-transcripts/o-zkvb0iFDQ.txt` (3,969 words).
- [[youtube-o-zkvb0iFDQ]] — related YouTube source page.
- [[youtube-o-zkvb0iFDQ-slides]] — slide evidence.
- [[youtube-o-zkvb0iFDQ-reconstructed-slides]] — slide evidence.
- [[youtube-o-zkvb0iFDQ-dense-slides]] — slide evidence.

### Novel Concepts / Clever Methods
- [[reachability-over-format|Reachability Over Format]] — Agent-facing files and specs matter less than whether agents can actually find and reach them from the surfaces they use.
- [[nearly-headless-web|Nearly Headless Web]] — The web moves toward machine-operable surfaces while preserving human-visible moments for choice, review, and judgment.
- [[agent-ready-accessibility|Agent-Ready Accessibility]] — Designing for agents and designing for accessibility converge around explicit structure, reachable controls, and understandable state.
- [[mcp-app-runtime|MCP Apps As Agentic App Runtime]] — MCP Apps treats interactive UI returned from MCP servers as a runtime layer for agent-facing software.

### Evidence Boundary
This synthesis uses the official schedule plus cached related-video transcripts. Related videos remain supporting context unless explicitly verified as exact session recordings.
