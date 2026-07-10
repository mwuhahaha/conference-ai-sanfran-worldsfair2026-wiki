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
- [[sebastian-fox]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.
