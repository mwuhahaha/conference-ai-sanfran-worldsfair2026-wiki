---
title: "Ray Actors, Vision Tokens, and the GIL: Engineering an SFT Data Pipeline That Keeps GPUs Busy"
category: "talks"
date: "2026-06-30"
time: "3:45pm-4:05pm"
track: "Expo Stage 4 SE"
room: "Expo Stage 4 SE"
speakers: ["Tarun Sunkaraneni"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
---

# Ray Actors, Vision Tokens, and the GIL: Engineering an SFT Data Pipeline That Keeps GPUs Busy

## Official Schedule Context
- Date/time: 2026-06-30 · 3:45pm-4:05pm
- Track/room: track TBD · Expo Stage 4 SE
- Speaker(s): Tarun Sunkaraneni
- Session type/status: session · confirmed

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
