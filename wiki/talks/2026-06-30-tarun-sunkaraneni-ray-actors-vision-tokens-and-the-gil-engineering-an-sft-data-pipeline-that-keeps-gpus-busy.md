---
title: "Ray Actors, Vision Tokens, and the GIL: Engineering an SFT Data Pipeline That Keeps GPUs Busy"
category: "talks"
date: "2026-06-30"
time: "3:45pm-4:05pm"
track: "Expo Stage 4 SE"
room: "Expo Stage 4 SE"
speakers: ["Tarun Sunkaraneni"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: ""
scheduleRoom: "Expo Stage 4 SE"
scheduleLabels: ["Expo Stage 4 SE", "session", "confirmed"]
---
# Ray Actors, Vision Tokens, and the GIL: Engineering an SFT Data Pipeline That Keeps GPUs Busy

## Official Schedule Context
- Date/time: 2026-06-30 · 3:45pm-4:05pm
- Track/room: track TBD · Expo Stage 4 SE
- Speaker(s): Tarun Sunkaraneni
- Session type/status: session · confirmed

## Schedule Labels
- Track: track TBD
- Room: Expo Stage 4 SE
- Session type: session
- Status: confirmed

## Official Description
Perception agents only learn as fast as we can feed them. Multimodal SFT is deceptively expensive on

the data side, and at million-sample scale, naive pipelines leave a fleet of GPUs waiting on Python

and data preprocessing.This talk walks through the SFT data pipeline we built to train vision-

language models for perception agents. We rebuilt the data path so that image fetching, vision

preprocessing, tokenization, and loss-mask generation all happen off the trainer's critical path,

and only the artifacts the trainer actually consumes ever cross the boundary into the training loop.

We pair this with a blended multi-dataset sampler designed for resumable streaming over very large

mixes, and an I/O layer tuned for the realities of fetching multimodal data from object storage.The

result: on large-scale VLM SFT runs, the trainer went from spending most of each step blocked on

data to spending most of it training, a major improvement in useful GPU time. We'll share the

architecture at a conceptual level, the gotchas at million-datapoint scale, and a mental model

engineers can take home for the data side of any perception-agent stack.

## Related YouTube Video
No related AI Engineer channel video found yet.

## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## People
- [[tarun-sunkaraneni]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.

## Source-Derived Enrichment
This section is generated from all currently linked source material for the article: official schedule text, related video pages, cached transcripts, visible slide text, dense/reconstructed slide pages, and AI slide-classification audits.

### Source Signals
No linked video, transcript, or slide source has been attached yet.

### Article Use
Use these source signals to refine the synopsis, topic links, people/company context, and method notes. If a source is a related external video rather than an exact official recording, keep it framed as supporting evidence.
