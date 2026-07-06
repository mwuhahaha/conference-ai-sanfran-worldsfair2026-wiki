---
title: "Why We Killed Our Multi-Agent Pipeline: Lessons From Pharma Commercial Intelligence"
category: "talks"
date: "2026-07-01"
time: "3:45pm-4:05pm"
track: "Graphs"
room: "Track 5"
speakers: ["Subbiah Sethuraman", "Abhilash Asokan"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
---

# Why We Killed Our Multi-Agent Pipeline: Lessons From Pharma Commercial Intelligence

## Official Schedule Context
- Date/time: 2026-07-01 · 3:45pm-4:05pm
- Track/room: Graphs · Track 5
- Speaker(s): Subbiah Sethuraman, Abhilash Asokan
- Session type/status: sponsor · confirmed

## Official Description
Key takeaways: A practical design principle for agentic systems in regulated, high-stakes domains:

derive the architecture from agent behavior, don't impose it. Concrete patterns the audience can

apply this week — domain knowledge graphs as agent context, deterministic preprocessing as a

complement to agentic reasoning, reference-based context management. An honest case study from

production: what worked, what didn't, and the open architectural questions we're still working on.

Abstract : We lead the architecture and AI engineering org behind ZS Associates' commercial

intelligence platform for pharmaceutical brand teams. The product has two surfaces: a proactive

alert system that delivers signal-driven intelligence packets when a brand's KPIs move, and a

conversational analytics chat where business users ask ad-hoc questions. A year ago we built both

surfaces as separate V1 stacks. They broke in different ways. The diagnosis was the same: we had

decided on the structure before we knew what the agent actually needed. This talk is about the

design principle that came out of rebuilding both — and what it produced. The architecture is

derived, not designed. We stopped trying to predict what scaffolding the agent would need and

started designing the system around what the agent's behavior, on real production tasks, actually

demanded. Tools, context, structure, and guardrails get introduced at the points where the agent's

reasoning needs them — and nowhere else. What that produced is an architecture that's smaller than

V1, not bigger. A single agent owns each investigation end-to-end across both surfaces, launching

parallel sub-agents when the work needs them — not according to a pre-defined topology. A

pharmaceutical commercial knowledge graph — HCPs, accounts, payers, territories, brands, KPIs and

the relationships between them — gives the agent the domain context it needs without prompt-

engineering heroics. Statistical signal detection runs deterministically before the agent wakes up,

so the agent's job is to explain signals, not find them. Raw query results stay out of the context

window through a reference-pattern that lets the agent reason over data without drowning in it. Each

of those decisions came from watching an agent struggle on a real task and asking what does it need

here? — not from sketching the architecture in a doc and forcing the agent into it. The patterns

generalize. If you're shipping agents over messy enterprise data — finance, supply chain, claims,

operations — the failure modes and the fixes will look familiar. We'll close with the open questions

and the pieces we haven't solved yet.

## Related YouTube Video
No related AI Engineer channel video found yet.

## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## People
- [[subbiah-sethuraman]]
- [[abhilash-asokan]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.
