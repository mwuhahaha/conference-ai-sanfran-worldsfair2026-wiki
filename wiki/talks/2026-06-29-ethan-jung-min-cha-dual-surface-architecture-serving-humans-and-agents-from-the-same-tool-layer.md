---
title: "Dual-Surface Architecture: Serving Humans and Agents from the Same Tool Layer"
category: "talks"
date: "2026-06-29"
time: "1:55pm-2:15pm"
track: "Security"
room: "Track 5"
speakers: ["Ethan (Jung Min) Cha"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Security"
scheduleRoom: "Track 5"
scheduleLabels: ["Security", "Track 5", "sponsor", "confirmed"]
---
# Dual-Surface Architecture: Serving Humans and Agents from the Same Tool Layer

## Official Schedule Context
- Date/time: 2026-06-29 · 1:55pm-2:15pm
- Track/room: Security · Track 5
- Speaker(s): Ethan (Jung Min) Cha
- Session type/status: sponsor · confirmed

## Schedule Labels
- Track: Security
- Room: Track 5
- Session type: sponsor
- Status: confirmed

## Official Description
Every enterprise AI talk right now is about capability. Almost none are about containment. That's the gap this talk fills, because it's where regulated deployments actually die. The Deterministic Harness is the set of rigid rails around a model: schemas, data contracts, tool boundaries, and audit paths. These rails are what turn a probabilistic model into a deployable enterprise asset. The idea isn't new. Aviation wraps pilots in envelope protection. Nuclear wraps reactors in passive safety. Banking wraps algorithmic trading in transaction limits. Every regulated industry figured out the same thing eventually: high-variance systems only become deployable when wrapped in low-variance containment. Enterprise AI is catching up, not inventing. I'll walk through the single governed MCP and API server we built at Carlyle, and the architectural decisions behind it. You'll leave with four things: 1. A phased rollout model where each phase earns the next. Moving from locked-down reads to trusted writes isn't risk mitigation. It's trust compounding. Each phase generates the observability that underwrites the autonomy granted in the next one. Skip a phase and you don't save time. You destroy the evidence base that would have justified the next step. 2. One contract, two surfaces. A single data layer that serves both the human UI and the agent. The institution then has exactly one answer to any question either might ask. When the agent and the UI disagree, users lose trust in both. 3. An intent based feedback loop that captures what LLM providers structurally cannot. The gap between what users tried to accomplish and what the system actually delivered is invisible to Anthropic, OpenAI, and Google. Only the harness owner sees it. We close that loop back into the governed server, and it compounds into differentiation that model providers cannot replicate from where they sit. 4. The failure modes we hit and what we'd redesign. A pre mortem folks will inherit for free, from two regulated industries where a wrong answer has a named owner.

## Related YouTube Video
No related AI Engineer channel video found yet.

## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## People
- [[ethan-jung-min-cha]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.

## Source-Derived Enrichment
This section is generated from all currently linked source material for the article: official schedule text, related video pages, cached transcripts, visible slide text, dense/reconstructed slide pages, and AI slide-classification audits.

### Source Signals
No linked video, transcript, or slide source has been attached yet.

### Article Use
Use these source signals to refine the synopsis, topic links, people/company context, and method notes. If a source is a related external video rather than an exact official recording, keep it framed as supporting evidence.
