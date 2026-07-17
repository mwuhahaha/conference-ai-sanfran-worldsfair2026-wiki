---
title: "Inside 847 Production Clinical AI Notes"
category: "talks"
date: "2026-07-01"
time: "2:50pm-3:10pm"
track: "AI Architects: AI Factories"
room: "Leadership 2"
speakers: ["Sebastian Fox"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "AI Architects: AI Factories"
scheduleRoom: "Leadership 2"
scheduleLabels: ["AI Architects: AI Factories", "Leadership 2", "session", "confirmed"]
---
# Inside 847 Production Clinical AI Notes

## Conference Context
- Date/time: 2026-07-01 · 2:50pm-3:10pm
- Track/room: AI Architects: AI Factories · Leadership 2
- Speaker(s): Sebastian Fox
- Session type/status: session · confirmed

- Track: AI Architects: AI Factories
- Room: Leadership 2
- Session type: session
- Status: confirmed

## Session Description
A Series B clinical AI company had an ambient scribe in production for six months. Internal evals passed every release. A clinical team spot-checked a sample weekly and saw nothing alarming. The system had healthy NPS, expanding deployments, and the company was preparing for European market expansion. We ran a structured audit on 847 production notes. Found 127 failures across six categories. 23 were severity-critical - the kind that could directly alter a clinical decision. The team's existing LLM-as-judge had reported zero failures across the same notes. This talk is the engineering forensics of that audit. The audit setup: which production traces we sampled, how the structured failure-mode coding worked, and the reviewer protocol. The results: three dominant failure clusters - decision-status corruption (19 cases), structured omissions (34 cases), and dosage substitution (12 cases) - and the underlying generation pattern behind each. For each cluster I will show: a real anonymised trace, the eval rule that should have caught it but did not, an explanation of why the eval missed it, and the criterion that does catch it. The pattern that emerged in the data is engineering-actionable. The team had built a 20-criterion content-faithfulness eval layer. The failures lived underneath it, in a missing intent layer. We replaced the broad content layer with a five-criterion intent layer (decision status, omission impact, dosage integrity, diagnostic chain, laterality consistency). Detection rate went from 0% to 96% on the failure set. Compute cost dropped because the intent layer is cheaper to run than the content layer it replaced. You will leave with a forensics protocol for auditing your own production AI, the five intent criteria that generalise to any high-stakes domain, and the architectural pattern: build a thin intent layer, not a thick content layer.

## Synthesis
### Synthesized Breakdown
A Series B clinical AI company had an ambient scribe in production for six months. Internal evals passed every release. A clinical team spot-checked a sample weekly and saw nothing alarming. The system had healthy NPS, expanding deployments, and the company was preparing for European market expansion.

### Speaker And Company Context
- [[sebastian-fox|Sebastian Fox]] — CEO at [[composo|Composo]].

### Topics Covered
- Topic links are pending transcript-backed classification.

### Derived Links And Source Material

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis is based on the official schedule and linked source pages. It should be revisited when exact session recordings or transcript-backed secondary sources are available.
## People
- [[sebastian-fox]]

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
