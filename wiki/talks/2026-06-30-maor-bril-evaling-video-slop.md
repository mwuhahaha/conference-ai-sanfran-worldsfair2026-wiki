---
title: "Evaling Video Slop"
category: "talks"
date: "2026-06-30"
time: "1:55pm-2:15pm"
track: "Evals"
room: "Track 5"
speakers: ["Maor Bril"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Evals"
scheduleRoom: "Track 5"
scheduleLabels: ["Evals", "Track 5", "sponsor", "confirmed"]
---
# Evaling Video Slop

## Conference Context
- Date/time: 2026-06-30 · 1:55pm-2:15pm
- Track/room: Evals · Track 5
- Speaker(s): Maor Bril
- Session type/status: sponsor · confirmed

- Track: Evals
- Room: Track 5
- Session type: sponsor
- Status: confirmed

## Session Description
Everyone is shipping video models. Almost no one is evaling them honestly. CLIP score doesn't catch temporal incoherence. Vibes-based human review doesn't scale. And every "AI judge" you wire up will quietly drift away from human preference unless you measure the drift. This is a tactical talk on building real multimodal eval, using JudgeJudy (open-sourced at Character.ai) as the working example. You'll leave with: Why video is different from text. Temporal consistency, shot continuity, narrative coherence, and the metrics that actually capture each (clip_temporal, temporal_consistency, and friends). AI judges, the real version. Custom rubrics, when they work, when they hallucinate, when they collapse to a single dimension and pretend they didn't. The calibration loop. Pearson/Spearman correlation against human scores, automated rubric improvement, detecting systematic judge bias before it costs you a release. Pairwise preference models for video. Training a Qwen3-VL backbone with Bradley-Terry loss to score "is this slop?" before it ships. Regression gates in CI. How every AgentX release at Character.ai passes through an eval wall before it reaches users. Closing the loop with JudgeJudy. Correlating eval scores against real telemetry (Amplitude, Statsig) and feeding validated gates back into the runtime. If you're shipping any multimodal output and your eval strategy is still "the team watches some clips on Friday," this is the upgrade. github.com/character-ai/judgejudy

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
- [[maor-bril]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.
