---
title: "Wearing the Agent: Engineering a Family-and-Friends Personal Agent, from Group Chats to Glasses"
category: "talks"
date: "2026-07-01"
time: "3:45pm-4:05pm"
track: "AI in Finance"
room: "Track 3"
speakers: ["Sai Krishna Rallabandi"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "AI in Finance"
scheduleRoom: "Track 3"
scheduleLabels: ["AI in Finance", "Track 3", "session", "confirmed"]
---
# Wearing the Agent: Engineering a Family-and-Friends Personal Agent, from Group Chats to Glasses

## Conference Context
- Date/time: 2026-07-01 · 3:45pm-4:05pm
- Track/room: AI in Finance · Track 3
- Speaker(s): Sai Krishna Rallabandi
- Session type/status: session · confirmed

- Track: AI in Finance
- Room: Track 3
- Session type: session
- Status: confirmed

## Session Description
Judith is a personal AI agent that has run in daily production for a year, used by more than a dozen of my family and friends across three WhatsApp group chats, Telegram, and Discord. This talk walks through how it's built, in two parts. The first part is the engineering that makes one agent safe for many people to share: a multi-tenant permission model (read-only for my mom, exec for me), a memory stack — FAISS + Neo4j + curated long-term notes — that stays useful over a year instead of bloating into noise, cron-scheduled subagents that scout and act on their own, and the guardrails it enforces on every message — redact personal info before posting to a group, never reply to the wrong person, and screen attacker-controllable text for prompt injection before acting on it. The second part takes the agent off the screen and onto a $50 pair of smart glasses. It captures what I see, describes and stores it as a running visual memory, sets destination path on maps before I get onto car, finds and tells me which aisle in the store to go to first, etc. I cover the latency budget that keeps it conversational — on-device Whisper for speech, cloud reasoning, sub-one-second round trips — and the custom neural voice it speaks in rather than stock TTS, drawn from my speech-synthesis background. Both parts are shown live, including a candid look at the pieces that don't work yet. Audience takeaways: A multi-tenant architecture for a personal agent multiple people actually share A memory design that survives real long-term use (not just a vector store) A defensive checklist for any agent that ingests untrusted text A blueprint for an ambient, vision-aware wearable interface on commodity hardware, with a real latency budget

## Synthesis
### Synthesized Breakdown
Judith is a personal AI agent that has run in daily production for a year, used by more than a dozen of my family and friends across three WhatsApp group chats, Telegram, and Discord. This talk walks through how it's built, in two parts. The first part is the engineering that makes one agent safe for many people to share: a multi-tenant permission model (read-only for my mom, exec for me), a memory stack — FAISS + Neo4j + curated long-term notes — that stays useful over a year instead of bloating into noise, cron-scheduled subagents that scout and act on their own, and the guardrails it enforces on every message — redact personal info before posting to a group, never reply to the wrong person, and screen attacker-controllable text for prompt injection before acting on it. The second part takes the agent off the screen and onto a $50 pair of smart glasses.

### Speaker And Company Context
- [[sai-krishna-rallabandi|Sai Krishna Rallabandi]] — Director, Data Science at [[fidelity-investments|Fidelity Investments]].

### Topics Covered
- [[agent-security]]

### Derived Links And Source Material

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis is based on the official schedule and linked source pages. It should be revisited when exact session recordings or transcript-backed secondary sources are available.
## People
- [[sai-krishna-rallabandi]]

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
