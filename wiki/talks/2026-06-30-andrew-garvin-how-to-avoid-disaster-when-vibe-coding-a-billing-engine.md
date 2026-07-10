---
title: "How to avoid disaster when vibe-coding a billing engine"
category: "talks"
date: "2026-06-30"
time: "11:10am-11:30am"
track: "AI-Native Enterprises"
room: "Leadership 1"
speakers: ["Andrew Garvin"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "AI-Native Enterprises"
scheduleRoom: "Leadership 1"
scheduleLabels: ["AI-Native Enterprises", "Leadership 1", "session", "confirmed"]
---
# How to avoid disaster when vibe-coding a billing engine

## Conference Context
- Date/time: 2026-06-30 · 11:10am-11:30am
- Track/room: AI-Native Enterprises · Leadership 1
- Speaker(s): Andrew Garvin
- Session type/status: session · confirmed

- Track: AI-Native Enterprises
- Room: Leadership 1
- Session type: session
- Status: confirmed

## Session Description
This talk covers what that infrastructure looks like in practice: which primitives matter, where the human checkpoints belong, and what changes when your billing system needs to be legible to machines instead of configured by humans clicking through a UI. When building AI products, billing and pricing should be directly tied to the products themselves. They're in the hot path. Every token, every agent action, every inference is a billable moment, and if your entitlement checks aren't keeping up, a single runaway agent can rack up thousands of dollars in seconds with no one to send the bill to. Get metering wrong and you're either eating costs or overcharging customers. Get ledger consistency wrong and your invoices don't add up. Get tax wrong across 47 jurisdictions and you find out from a regulator, not a user. Here's the thing, though — agents are legitimately good at billing strategy. They can pick pricing models, configure plans, run simulations, and iterate on packaging way faster than a human team could. You want them doing that work. But proration, multi-currency, revenue recognition, tax — this stuff took the industry years to get right, and it's unforgiving when you get it wrong. The question then becomes not whether agents should be making billing changes, it's what they should be operating on when they do. Agents need tight, composable building blocks where the correctness is already baked in, human-in-the-loop checkpoints before anything irreversible goes out the door, and sandbox environments where they can experiment freely without torching production. That's the architecture that lets you move fast on pricing without waking up to broken invoices. Target audience: Engineers and technical founders building AI products that charge for usage — whether that's per-token, per-action, or per-seat with consumption overages. If you've ever hard-coded a pricing tier, duct-taped metering onto an existing system, or wondered how your billing setup is going to survive your next pricing change, this talk is for you. Audience takeaways: - A clear understanding of why billing for AI products sits in the hot path — and what specifically goes wrong when metering, entitlements, or ledger consistency can't keep up. - A practical architecture for making billing agent-operable: composable primitives with correctness baked in, human-in-the-loop checkpoints on irreversible actions, and sandbox environments for safe experimentation. - A framework for deciding where agents should be empowered to move fast on billing strategy and where guardrails need to be non-negotiable.

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
- [[andrew-garvin]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.

## Synthesis
### Synthesized Breakdown
# How to avoid disaster when vibe-coding a billing engine ## Conference Context - Date/time: 2026-06-30 · 11:10am-11:30am - Track/room: AI-Native Enterprises · Leadership 1 - Speaker(s): Andrew Garvin - Session type/status: session · confirmed - Track: AI-Native Enterprises - Room: Leadership 1 - Session type: session - Status: confirmed ## Session Description This talk covers what that infrastructure looks like in practice: which primitives matter, where the human checkpoints belong, and what changes when your billing system needs to be legible to machines instead of configured by humans clicking through a UI. When building AI products, billing and pricing should be directly tied to the products themselves. They're in the hot path. Every token, every agent action, every inference is a billable moment, and if your entitlement checks aren't keeping up, a single runaway agent can rack up thousands of dollars in seconds with no one to send the bill to.

### Speaker And Company Context
- [[andrew-garvin|Andrew Garvin]] — Cofounder of Metronome at [[stripe|Stripe]].

### Topics Covered
- [[agent-security]]
- [[ai-sandboxes]]
- [[coding-agents]]

### Derived Links And Source Material

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis is based on the official schedule and linked source pages. It should be revisited when exact session recordings or transcript-backed secondary sources are available.
