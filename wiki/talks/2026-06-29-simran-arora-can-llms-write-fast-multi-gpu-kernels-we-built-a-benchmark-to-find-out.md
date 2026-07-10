---
title: "Can LLMs write fast multi-GPU kernels? We built a benchmark to find out."
category: "talks"
date: "2026-06-29"
time: "12:05pm-12:25pm"
track: "Expo Stage 3 SW"
room: "Expo Stage 3 SW"
speakers: ["Simran Arora"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: ""
scheduleRoom: "Expo Stage 3 SW"
scheduleLabels: ["Expo Stage 3 SW", "session", "confirmed"]
---
# Can LLMs write fast multi-GPU kernels? We built a benchmark to find out.

## Conference Context
- Date/time: 2026-06-29 · 12:05pm-12:25pm
- Track/room: track TBD · Expo Stage 3 SW
- Speaker(s): Simran Arora
- Session type/status: session · confirmed

- Track: track TBD
- Room: Expo Stage 3 SW
- Session type: session
- Status: confirmed

## Session Description
LLMs have gotten surprisingly good at writing GPU kernels, but almost all the benchmarks measuring that progress are single-GPU. In production, communication is the bottleneck: all-reduce alone accounts for over 20% of inference latency on Llama-3.3-70B, and that gap keeps widening as compute scales faster than interconnect bandwidth. ParallelKernelBench (PKB) offers a benchmark and evaluation framework for multi-GPU kernel generation and includes 87 problems from real codebases where the task is replacing PyTorch + NCCL with a CUDA kernel that moves data directly over NVLink. We tested GPT-5.5, Gemini 3 Pro, Opus 4.7, and other frontier coding models. Under a third of problems solved were correctly, and fewer than a quarter of those beat the naive baseline. We'll cover why they fail, what the patterns look like, and a few cases where models produced kernels faster than anything publicly available, including one for NVIDIA NeMo-RL's GRPO training loop, which has no prior optimized public reference. The benchmark is open source and we want to see what you can do!

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
- [[simran-arora]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.

## Synthesis
### Synthesized Breakdown
# Can LLMs write fast multi-GPU kernels? We built a benchmark to find out. ## Conference Context - Date/time: 2026-06-29 · 12:05pm-12:25pm - Track/room: track TBD · Expo Stage 3 SW - Speaker(s): Simran Arora - Session type/status: session · confirmed - Track: track TBD - Room: Expo Stage 3 SW - Session type: session - Status: confirmed ## Session Description LLMs have gotten surprisingly good at writing GPU kernels, but almost all the benchmarks measuring that progress are single-GPU. In production, communication is the bottleneck: all-reduce alone accounts for over 20% of inference latency on Llama-3.3-70B, and that gap keeps widening as compute scales faster than interconnect bandwidth.

### Speaker And Company Context
- [[simran-arora|Simran Arora]] — Computer Science PhD Student at [[stanford-university|Stanford University]].

### Topics Covered
- [[coding-agents]]

### Derived Links And Source Material

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis is based on the official schedule and linked source pages. It should be revisited when exact session recordings or transcript-backed secondary sources are available.
