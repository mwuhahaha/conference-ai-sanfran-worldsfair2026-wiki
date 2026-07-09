---
title: What If Your Chip Design Team Moved Like a Single Body?
category: talks
date: '2026-07-01'
time: '11:40am-12:00pm'
track: 'AI Architects: AI Factories'
room: Leadership 2
speakers:
  - Khaled Alashmouny
  - Abduallah Mohamed
sourceLabels:
  - Official conference schedule
  - Public YouTube metadata
last_auto_summarized: '2026-07-06T16:57:41.135Z'
scheduleTrack: "AI Architects: AI Factories"
scheduleRoom: "Leadership 2"
scheduleLabels: ["AI Architects: AI Factories", "Leadership 2", "session", "confirmed"]
---
# What If Your Chip Design Team Moved Like a Single Body?

## Summary
This AI Architects session frames chip design as a coordination problem that exposes the limits of single-user, single-session agent demos. Khaled Alashmouny, founder and CEO of AIDAChip, and Abduallah Mohamed, AIDAChip's VP of AI/ML, use semiconductor IP development to argue for Multiplayer AI: many specialized agents coordinating across disciplines while staying attached to one shared project intent, spec hierarchy, and milestone plan. The schedule description makes the expensive failure mode explicit: not slow individual engineers, but silent divergence between teams as specifications drift, assumptions fork, and handoffs become brittle. In this domain, a missed alignment point can become a $10-50M mistake, and the talk treats that pressure as a forcing function for agent-system architecture.

The proposed architecture has three concrete alignment layers. First is a living spec graph, described as a System of Intent, that propagates changes and detects conflicts in real time. Second is a Memory layer that carries methodology and tribal knowledge across projects so engineering practice compounds rather than resetting at every handoff. Third is milestone-aware execution that can drive EDA tools with the full design context available to the relevant agents. The session also emphasizes typed structured tool calls, API-enforced spec-hierarchy boundaries, and audit logs for cross-agent invocations, making the coordination substrate as important as the agent capabilities themselves.

The connected people pages sharpen the roles behind the talk. Alashmouny brings AIDAChip's founder/operator perspective: the company is explicitly building multiplayer AI systems for semiconductor engineering teams rather than a generic copilot. Mohamed brings the AI platform and production ML perspective at the intersection of agentic systems and chip engineering. Together, they position chip design as an unusually demanding test bed for AI agents because it combines long project arcs, many specialized disciplines, strict design boundaries, expensive validation cycles, and a need for traceable decisions across time.

The current evidence layer is still schedule-grounded. No official matched AI Engineer YouTube recording or transcript is linked yet, and the transcript map notes that exact session-recording matches were not found by normalized title during this run. This page should therefore keep its claims tied to the official description and connected index context: a July 1 AI Architects session in the Leadership 2 room, part of the dense multi-track World's Fair program, centered on AIDAChip's Anthropic Agent SDK-based multiplayer AI, practitioner interviews across semiconductor and EDA companies, and the practical lesson that AI engineering teams need alignment infrastructure as much as capable agents.

## Official Schedule Context
- Date/time: 2026-07-01 · 11:40am-12:00pm
- Track/room: AI Architects: AI Factories · Leadership 2
- Speaker(s): Khaled Alashmouny, Abduallah Mohamed
- Session type/status: session · confirmed

## Schedule Labels
- Track: AI Architects: AI Factories
- Room: Leadership 2
- Session type: session
- Status: confirmed

## Official Description
Most agentic demos you've seen has a hidden assumption: one user, one session, one task. But what happens when the agent needs to coordinate with 30 other agents, across 10 disciplines, on a project that takes 12 months — where a single miscommunication costs $10-50M? Chip design is that problem. Only 14% of chips succeed on first silicon. The bottleneck isn't individual engineer speed — it's silent divergence between disciplines working from specs that drift without noticing. We built a multiplayer AI on the Anthropic Agent SDK, connected through three alignment layers: a living spec graph (System of Intent) that propagates changes and detects conflicts in real time, a tribal knowledge layer (Memory) that compounds methodology across projects, and milestone-aware execution that drives EDA tools with full design context. Each agent operates within strict spec-hierarchy boundaries enforced at the API level. Cross-agent invocations use structured tool calls with typed parameters, logged for full auditability. We talked with 15 practitioners across 8 major semiconductor and EDA companies. The universal finding: teams need alignment infrastructure, not faster copilots. We'll also share what broke — because coordination tax applies to AI agents too, and the failure modes are surprisingly instructive. This talk covers the multi-agent architecture, evaluation methodology, and lessons from deploying agentic AI in one of engineering's most complex coordination domains.

## Related YouTube Video
No related AI Engineer channel video found yet.

## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## People
- [[khaled-alashmouny]]
- [[abduallah-mohamed]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.

## Source-Derived Enrichment
This section is generated from all currently linked source material for the article: official schedule text, related video pages, cached transcripts, visible slide text, dense/reconstructed slide pages, and AI slide-classification audits.

### Source Signals
No linked video, transcript, or slide source has been attached yet.

### Article Use
Use these source signals to refine the synopsis, topic links, people/company context, and method notes. If a source is a related external video rather than an exact official recording, keep it framed as supporting evidence.
