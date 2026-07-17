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

## Conference Context
- Date/time: 2026-06-29 · 1:55pm-2:15pm
- Track/room: Security · Track 5
- Speaker(s): Ethan (Jung Min) Cha
- Session type/status: sponsor · confirmed

- Track: Security
- Room: Track 5
- Session type: sponsor
- Status: confirmed

## Session Description
Every enterprise AI talk right now is about capability. Almost none are about containment. That's the gap this talk fills, because it's where regulated deployments actually die. The Deterministic Harness is the set of rigid rails around a model: schemas, data contracts, tool boundaries, and audit paths. These rails are what turn a probabilistic model into a deployable enterprise asset. The idea isn't new. Aviation wraps pilots in envelope protection. Nuclear wraps reactors in passive safety. Banking wraps algorithmic trading in transaction limits. Every regulated industry figured out the same thing eventually: high-variance systems only become deployable when wrapped in low-variance containment. Enterprise AI is catching up, not inventing. I'll walk through the single governed MCP and API server we built at Carlyle, and the architectural decisions behind it. You'll leave with four things: 1. A phased rollout model where each phase earns the next. Moving from locked-down reads to trusted writes isn't risk mitigation. It's trust compounding. Each phase generates the observability that underwrites the autonomy granted in the next one. Skip a phase and you don't save time. You destroy the evidence base that would have justified the next step. 2. One contract, two surfaces. A single data layer that serves both the human UI and the agent. The institution then has exactly one answer to any question either might ask. When the agent and the UI disagree, users lose trust in both. 3. An intent based feedback loop that captures what LLM providers structurally cannot. The gap between what users tried to accomplish and what the system actually delivered is invisible to Anthropic, OpenAI, and Google. Only the harness owner sees it. We close that loop back into the governed server, and it compounds into differentiation that model providers cannot replicate from where they sit. 4. The failure modes we hit and what we'd redesign. A pre mortem folks will inherit for free, from two regulated industries where a wrong answer has a named owner.

## Synthesis
### Synthesized Breakdown
Every enterprise AI talk right now is about capability. Almost none are about containment. That's the gap this talk fills, because it's where regulated deployments actually die. The Deterministic Harness is the set of rigid rails around a model: schemas, data contracts, tool boundaries, and audit paths.

### Speaker And Company Context
- [[ethan-jung-min-cha|Ethan (Jung Min) Cha]] — AI Development Lead at [[the-carlyle-group|The Carlyle Group]].

### Topics Covered
- [[agent-security]]
- [[mcp]]

### Derived Links And Source Material

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis is based on the official schedule and linked source pages. It should be revisited when exact session recordings or transcript-backed secondary sources are available.
## People
- [[ethan-jung-min-cha]]

## Media Evidence
No exact recording or transcript evidence is attached yet; the official schedule remains the source for this session.
## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
No linked video, transcript, or slide source has been attached yet.

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.
