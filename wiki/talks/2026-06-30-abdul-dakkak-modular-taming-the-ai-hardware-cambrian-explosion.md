---
title: 'Modular: Taming the AI Hardware Cambrian Explosion'
category: talks
date: '2026-06-30'
time: '3:45pm-4:05pm'
track: Expo Stage 1 NE
room: Expo Stage 1 NE
speakers:
  - Abdul Dakkak
sourceLabels:
  - Official conference schedule
  - Public YouTube metadata
last_auto_summarized: '2026-07-06T09:33:55.904Z'
scheduleTrack: ""
scheduleRoom: "Expo Stage 1 NE"
scheduleLabels: ["Expo Stage 1 NE", "session", "confirmed"]
---
# Modular: Taming the AI Hardware Cambrian Explosion

## Summary
Abdul Dakkak's session frames Modular's core problem as the widening gap between fast-moving GenAI workloads and the limited, fragmented hardware teams can reliably use. As Modular's Chief Scientist, Dakkak is positioned to connect the company-level platform story to concrete inference-stack details: Mojo kernels, the MAX compiler and runtime, and Modular Cloud are presented as one path toward performance portability across NVIDIA, AMD, Apple Silicon, and CPU deployments. The official description makes this a hardware-diversity and production-inference talk rather than a general accelerator pitch, with specific attention to memory movement, batching, KV-cache layout, quantization, scheduling, and kernel specialization.

The talk's evidence layer is still schedule-only in this clean wiki: no exact AI Engineer YouTube recording match or official transcript has been found yet. That means the strongest grounded claims remain the official benchmark claims in the schedule description, including lower latency on image and video models such as FLUX2, higher throughput on MoE workloads such as Kimi K2.5, and the broader argument that AI teams need to extract more from existing hardware while avoiding vendor-by-vendor kernel rewrites.

## Official Schedule Context
- Date/time: 2026-06-30 · 3:45pm-4:05pm
- Track/room: track TBD · Expo Stage 1 NE
- Speaker(s): Abdul Dakkak
- Session type/status: session · confirmed

## Schedule Labels
- Track: track TBD
- Room: Expo Stage 1 NE
- Session type: session
- Status: confirmed

## Official Description
AI teams are hitting the same wall: the workloads they want to run require more hardware than they can reliably access. Buying more GPUs is not always possible, and rewriting kernels for every vendor is not sustainable. Meanwhile, models keep growing, SLAs keep tightening, workloads keep diversifying, and modalities keep multiplying. Modular has two answers: squeeze more performance out of the hardware you already have, and unlock far greater hardware diversity. We'll ground the talk in benchmark data and show how the Modular platform delivers 10x lower latency on image and video models like FLUX2 and 5.5x higher throughput on MoE models like Kimi K2.5, both over the state of the art. This talk explains how Modular is rebuilding the inference stack for performance portability. We'll demonstrate how Mojo kernels, the MAX compiler and runtime, and Modular Cloud work together to optimize GenAI workloads from model graph to hardware execution across NVIDIA, AMD, Apple Silicon, and CPU deployments. Along the way, we'll cover the bottlenecks that dominate production inference: memory movement, batching, KV-cache layout, quantization, scheduling, and kernel specialization. Using examples from LLM serving, we'll reveal which optimizations matter, where abstractions leak, and how to reason about performance portability in real deployments.

## Related YouTube Video
No related AI Engineer channel video found yet.

## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## People
- [[abdul-dakkak]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.

## Source-Derived Enrichment
This section is generated from all currently linked source material for the article: official schedule text, related video pages, cached transcripts, visible slide text, dense/reconstructed slide pages, and AI slide-classification audits.

### Source Signals
No linked video, transcript, or slide source has been attached yet.

### Article Use
Use these source signals to refine the synopsis, topic links, people/company context, and method notes. If a source is a related external video rather than an exact official recording, keep it framed as supporting evidence.
