---
title: "Why Agentic Systems Need Ontologies"
category: "talks"
date: "2026-07-01"
time: "1:55pm-2:15pm"
track: "Graphs"
room: "Track 5"
speakers: ["Frank Coyle"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
---

# Why Agentic Systems Need Ontologies

## Official Schedule Context
- Date/time: 2026-07-01 · 1:55pm-2:15pm
- Track/room: Graphs · Track 5
- Speaker(s): Frank Coyle
- Session type/status: sponsor · confirmed

## Official Description
Agentic systems fail in predictable ways: context degradation, brittle tool descriptions, fragile

multi-agent handoffs, stop-reason confusion, and the ever-present temptation to fix reliability

problems with more natural-language instructions. These anti-patterns aren't bugs to be patched turn

by turn — they're symptoms of a missing architectural layer. LLMs reason probabilistically over

domains they only partially understand, and no amount of prompt engineering fully closes that gap.

This talk argues that the missing layer is an explicit ontology: a formal, shared map of the

domain's concepts, relationships, and constraints. The pattern is not new — ontologies have driven

commercial success in defense and intelligence systems for over a decade, where probabilistic models

must operate over high-stakes enterprise data without drifting into nonsense. Graph databases like

Neo4j and Amazon Neptune have made the underlying primitives widely accessible. We'll show how

lightweight ontology constructs can surround an agentic system with enforceable logical constraints:

typed entities and relationships that tools must respect, cardinality and domain restrictions that

catch malformed tool calls before they execute, and a shared vocabulary that keeps coordinators and

subagents talking about the same things. The session walks through several agentic applications — a

multi-agent research workflow, a tool-heavy customer support agent, a coordinator-subagent

delegation pattern — and shows in each case how an ontology layer addresses the kinds of anti-

patterns catalogued in Anthropic's Claude Certified Architect exam. The result is a hybrid

neurosymbolic architecture: probabilistic reasoning inside, logical guardrails outside. Who should

attend: engineers building production agentic systems, architects evaluating reliability strategies

beyond prompt engineering, and technical leads who suspect their agents need more structure than

another system prompt can provide.

## Related YouTube Video
No related AI Engineer channel video found yet.

## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## People
- [[frank-coyle]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.
