---
title: "Guardrails First: Engineering Member-Facing Health AI"
category: "talks"
date: "2026-07-01"
time: "11:10am-11:30am"
track: "AI in Healthcare"
room: "Track 7"
speakers: ["Rashi Agrawal"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "AI in Healthcare"
scheduleRoom: "Track 7"
scheduleLabels: ["AI in Healthcare", "Track 7", "session", "confirmed"]
---
# Guardrails First: Engineering Member-Facing Health AI

## Official Schedule Context
- Date/time: 2026-07-01 · 11:10am-11:30am
- Track/room: AI in Healthcare · Track 7
- Speaker(s): Rashi Agrawal
- Session type/status: session · confirmed

## Schedule Labels
- Track: AI in Healthcare
- Room: Track 7
- Session type: session
- Status: confirmed

## Official Description
Everywhere else in the company, an AI pilot can reach production in weeks. For our member-facing

clinical assistant, it can't, and that single constraint redesigned our entire architecture. This is

a field report on building conversational AI in a regulated digital health setting, where "move fast

and break things" isn't a culture choice. It's a liability. We'll get concrete about what changes

when every output has to be clinically safe, auditable, and compliant: PHI is protected by

architecture, not policy. Production and non-production are hard-isolated, dashboards are sanitized,

and engineers outside the US never touch protected health information. Must-not-fail behavior never

lives in a prompt. Emergency escalation and intent routing run as deterministic rules at the top of

every conversation turn, before the model is consulted. If you can't afford to get something wrong,

you don't leave it to a probabilistic system. Clinical safety is a continuous eval layer. ~30 LLM-

as-judge evaluators score clinical accuracy, clinical safety, escalation routing, and recommendation

relevance, continuously, not once. Every output is auditable. Each turn, tool call, and reasoning

step is traced so outputs can be reviewed and meet regulated reporting obligations. The throughline:

in regulated healthcare, compliance constraints aren't a tax you pay around the architecture. They

become the architecture. We'll talk about why guardrails-first is the only way to ship member-facing

health AI, and why "painfully slow" is sometimes exactly right. (This is non-diagnostic, member-

facing AI. The talk is about engineering discipline under regulation, not medical claims.) Key

takeaways - In regulated health AI, "move fast" is the wrong default. Design for deliberate, careful

launches. - Must-not-fail behaviors belong in deterministic rules at the top of every turn, never in

the prompt. - Protect PHI through architecture: isolate prod from non-prod, sanitize dashboards,

restrict access by role and geography. - Make every output auditable. Trace each turn, tool call,

and reasoning step so safety is reviewable, not assumed. - Treat clinical safety as a continuous

LLM-as-judge layer, not a one-time gate.

## Related YouTube Video
No related AI Engineer channel video found yet.

## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## People
- [[rashi-agrawal]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.

## Source-Derived Enrichment
This section is generated from all currently linked source material for the article: official schedule text, related video pages, cached transcripts, visible slide text, dense/reconstructed slide pages, and AI slide-classification audits.

### Source Signals
No linked video, transcript, or slide source has been attached yet.

### Article Use
Use these source signals to refine the synopsis, topic links, people/company context, and method notes. If a source is a related external video rather than an exact official recording, keep it framed as supporting evidence.
