---
title: "Can LLMs write fast multi-GPU kernels? We built a benchmark to find out."
category: "talks"
date: "2026-06-29"
time: "12:05pm-12:25pm"
track: "Expo Stage 3 SW"
room: "Expo Stage 3 SW"
speakers: ["Simran Arora"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
---

# Can LLMs write fast multi-GPU kernels? We built a benchmark to find out.

## Official Schedule Context
- Date/time: 2026-06-29 · 12:05pm-12:25pm
- Track/room: track TBD · Expo Stage 3 SW
- Speaker(s): Simran Arora
- Session type/status: session · confirmed

## Official Description
LLMs have gotten surprisingly good at writing GPU kernels, but almost all the benchmarks measuring

that progress are single-GPU. In production, communication is the bottleneck: all-reduce alone

accounts for over 20% of inference latency on Llama-3.3-70B, and that gap keeps widening as compute

scales faster than interconnect bandwidth. ParallelKernelBench (PKB) offers a benchmark and

evaluation framework for multi-GPU kernel generation and includes 87 problems from real codebases

where the task is replacing PyTorch + NCCL with a CUDA kernel that moves data directly over NVLink.

We tested GPT-5.5, Gemini 3 Pro, Opus 4.7, and other frontier coding models. Under a third of

problems solved were correctly, and fewer than a quarter of those beat the naive baseline. We'll

cover why they fail, what the patterns look like, and a few cases where models produced kernels

faster than anything publicly available, including one for NVIDIA NeMo-RL's GRPO training loop,

which has no prior optimized public reference. The benchmark is open source and we want to see what

you can do!

## Related YouTube Video
No related AI Engineer channel video found yet.

## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## People
- [[simran-arora]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.
