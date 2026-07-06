---
title: "Your Agent Didn’t Fail. Your Harness Did."
category: "talks"
date: "2026-06-29"
time: "11:10am-11:30am"
track: "Claws & Personal Agents"
room: "Track 1"
speakers: ["Vinoth Govindarajan"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
---

# Your Agent Didn’t Fail. Your Harness Did.

## Official Schedule Context
- Date/time: 2026-06-29 · 11:10am-11:30am
- Track/room: Claws & Personal Agents · Track 1
- Speaker(s): Vinoth Govindarajan
- Session type/status: session · confirmed

## Official Description
AI agents do not fail only because the model is wrong. Many production failures happen in the

harness around the model: state is not persisted, two runs mutate the same session, a tool call

never returns, an approval loses scope, or an internal success never becomes user-visible proof.

This talk uses OpenClaw as a public case study to examine real harness failure modes and extract a

reusable production model for AI engineers. We will look at how events enter an agent system, how

session state is rehydrated, why single-writer lanes and throttles matter, and why tool execution

needs scoped approvals and auditable receipts. The core idea is simple: a model proposes, the

harness commits, and the receipt proves it. Attendees will leave with a practical 'run receipt'

audit they can apply to their own agents: what woke it up, which state did it inherit, what

authority did it use, what executed, and what evidence survived.

## Related YouTube Video
No related AI Engineer channel video found yet.

## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## People
- [[vinoth-govindarajan]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.
