---
title: "Spin at the Gate Until Green: The Engineering Primitives Behind Self-Driving Codebases"
category: "talks"
date: "2026-06-29"
time: "1:30pm-1:50pm"
track: "Software Factories"
room: "Leadership 1"
speakers: ["Andrew Orobator"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Software Factories"
scheduleRoom: "Leadership 1"
scheduleLabels: ["Software Factories", "Leadership 1", "session", "confirmed"]
---
# Spin at the Gate Until Green: The Engineering Primitives Behind Self-Driving Codebases

## Official Schedule Context
- Date/time: 2026-06-29 · 1:30pm-1:50pm
- Track/room: Software Factories · Leadership 1
- Speaker(s): Andrew Orobator
- Session type/status: session · confirmed

## Schedule Labels
- Track: Software Factories
- Room: Leadership 1
- Session type: session
- Status: confirmed

## Official Description
Most AI-assisted development fails the same way: the AI produces plausible output, the human can't

tell if it's right, so they check manually, find the problem, re-prompt, and repeat. This loop

doesn't scale. There's a different approach. If you can express correctness as a binary — does it

compile, do the tests pass, does the lint check clear — you can remove the human from that loop

entirely. The AI submits. The gate checks. If red, it adjusts and resubmits. Spin at the gate until

green. This talk covers the engineering primitives that make this possible: personas (consistent

behavior at the agent level), skills (composable, reusable prompt modules), worklogs (accountability

across sessions), postmortems (turning failures into constraints), and spec-driven development

(making the target explicit enough for a machine to hit it). The culmination is a flag lifecycle

agent — triggered by a cron job, cleaning up stale feature flags, verified by compile + test + lint,

no human in the loop. Not hypothetical. Working prototype, proven in practice. I co-authored a ten-

part series on this methodology with Claude. The series was built using the workflow described in

this talk. If you don't trust the theory, the fact that this talk exists is the proof.

## Related YouTube Video
No related AI Engineer channel video found yet.

## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## People
- [[andrew-orobator]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.

## Source-Derived Enrichment
This section is generated from all currently linked source material for the article: official schedule text, related video pages, cached transcripts, visible slide text, dense/reconstructed slide pages, and AI slide-classification audits.

### Source Signals
No linked video, transcript, or slide source has been attached yet.

### Article Use
Use these source signals to refine the synopsis, topic links, people/company context, and method notes. If a source is a related external video rather than an exact official recording, keep it framed as supporting evidence.
