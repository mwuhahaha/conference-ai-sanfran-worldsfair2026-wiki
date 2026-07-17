---
title: "Self-Improvement of Context, Harness, and Model Weights through Reflective Optimization"
category: "talks"
date: "2026-06-30"
time: "2:25pm-2:45pm"
track: "Autoresearch"
room: "Main Stage"
speakers: ["Lakshya Agrawal"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Autoresearch"
scheduleRoom: "Main Stage"
scheduleLabels: ["Autoresearch", "Main Stage", "session", "confirmed"]
---
# Self-Improvement of Context, Harness, and Model Weights through Reflective Optimization

## Conference Context
- Date/time: 2026-06-30 · 2:25pm-2:45pm
- Track/room: Autoresearch · Main Stage
- Speaker(s): Lakshya Agrawal
- Session type/status: session · confirmed

- Track: Autoresearch
- Room: Main Stage
- Session type: session
- Status: confirmed

## Session Description
Large language models are increasingly adapted to downstream tasks via reinforcement learning methods like GRPO, which often require thousands of rollouts to learn new tasks. We argue that language provides a much richer learning medium: an LLM can reflect on full trajectories (including reasoning, tool calls and errors) to diagnose failures and propose targeted improvements. We introduce [GEPA](gepa-ai.github.io/gepa/), a reflective prompt optimizer that incorporates this principle outperforming GRPO by up to 20% while using up to 35x fewer rollouts across tasks spanning 5+ domains and also works with black-box models. Building on this, we then introduce [optimize_anything](gepa-ai.github.io/gepa/blog/2026/02/18/introducing-optimize-anything/), a unified API that generalizes reflective optimization to arbitrary text parameters. This single system achieves state-of-the-art results across eight fundamentally different areas, including nearly tripling ARC-AGI accuracy via agent architecture discovery, generating CUDA kernels that beat PyTorch and cutting cloud scheduling costs by 40% through policy discovery, establishing LLM-based reflective search as a general-purpose problem-solving paradigm. Finally, I present [Fast-Slow Training](arxiv.org/abs/2605.12484) (FST), which brings reflective optimization into LLM post-training. FST jointly optimizes model parameters ("slow weights") via RL and textual contexts ("fast weights") via GEPA. Because the fast channel quickly absorbs task-specific nuances, the slow parametric updates are freed to consolidate general reasoning rather than memorizing task details. This yields up to 3x better sample efficiency, a higher performance asymptote with a significantly lower drift from the base model. This reduced drift preserves plasticity for continual learning, allowing FST to adapt sequentially where parameter-only RL stalls. Broadly, our work advocates a fundamental shift in AI adaptation: replacing task-specific algorithms with diagnostic evaluation, and evolving from parameter-only post-training to the joint optimization of prompts, agent architectures, and model weights.

## Synthesis
### Synthesized Breakdown
Large language models are increasingly adapted to downstream tasks via reinforcement learning methods like GRPO, which often require thousands of rollouts to learn new tasks. We argue that language provides a much richer learning medium: an LLM can reflect on full trajectories (including reasoning, tool calls and errors) to diagnose failures and propose targeted improvements. We introduce [GEPA](gepa-ai.github.io/gepa/), a reflective prompt optimizer that incorporates this principle outperforming GRPO by up to 20% while using up to 35x fewer rollouts across tasks spanning 5+ domains and also works with black-box models. Building on this, we then introduce [optimize_anything](gepa-ai.github.io/gepa/blog/2026/02/18/introducing-optimize-anything/), a unified API that generalizes reflective optimization to arbitrary text parameters.

### Speaker And Company Context
- [[lakshya-agrawal|Lakshya Agrawal]] — Creator and maintainer of GEPA at GEPA.

### Topics Covered
- [[agentic-search]]

### Derived Links And Source Material

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis is based on the official schedule and linked source pages. It should be revisited when exact session recordings or transcript-backed secondary sources are available.
## People
- [[lakshya-agrawal]]

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
