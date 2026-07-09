---
title: "From Scratch to SOTA: Training a 3B State-Space Vision Model for 1.4 Billion People"
category: "talks"
date: "2026-06-29"
time: "3:20pm-3:40pm"
track: "Vision & OCR"
room: "Track 2"
speakers: ["Krishna Prasad Srinivasan"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Vision & OCR"
scheduleRoom: "Track 2"
scheduleLabels: ["Vision & OCR", "Track 2", "sponsor", "confirmed"]
---
# From Scratch to SOTA: Training a 3B State-Space Vision Model for 1.4 Billion People

## Official Schedule Context
- Date/time: 2026-06-29 · 3:20pm-3:40pm
- Track/room: Vision & OCR · Track 2
- Speaker(s): Krishna Prasad Srinivasan
- Session type/status: sponsor · confirmed

## Schedule Labels
- Track: Vision & OCR
- Room: Track 2
- Session type: sponsor
- Status: confirmed

## Official Description
India has 22 official languages. Across those languages live over a billion people whose knowledge

is locked inside scanned images in scripts that most frontier models perform poorly. The problem is

dire - until now, there wasn't even a comprehensive benchmark to measure Indic OCR performance, let

alone training data at scale. When Sarvam AI set out to solve this, we had to build the

infrastructure before the model, creating the first ground-truth benchmark for Indic document

intelligence. In this talk, Krishna Srinivasan, who led the Vision Models team to build India's

first sovereign VLM from scratch, will walk through the end-to-end engineering lifecycle. We will

cover: (a) Architecture: Why we chose a 3B-parameter state-space architecture over transformer

baselines to handle high-resolution visual inputs with minimal memory overhead and faster inference.

(b) Training Pipeline: The exact recipe we used: starting with text-only pre-training, moving to

continual pre-training with text and images, followed by SFT. Finally, we'll cover the advances we

made in implementing large-scale RL with Verifiable Rewards for visual tasks in just 3 days using

deterministic character-level reward signals. (c) Compute Efficiency: How we trained a frontier-

competitive multimodal model with extreme capital efficiency, optimizing distributed training and

GPU cluster management to punch far above our compute class. (d) Agentic Workflows: How this model

powers Sarvam Akshar, a first-of-its-kind agentic document intelligence workbench featuring visual

grounding and automated proofreading loops. The results speak for themselves: Sarvam Vision achieves

best-in-class global scores (84.3% on olmOCR-Bench, 93.28% on OmniDocBench) and dominates Indic OCR.

Attendees will learn the blueprint for compute-efficient multimodal training, and deploying state-

space VLMs for population-scale enterprise workloads.

## Related YouTube Video
No related AI Engineer channel video found yet.

## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## People
- [[krishna-prasad-srinivasan]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.

## Source-Derived Enrichment
This section is generated from all currently linked source material for the article: official schedule text, related video pages, cached transcripts, visible slide text, dense/reconstructed slide pages, and AI slide-classification audits.

### Source Signals
No linked video, transcript, or slide source has been attached yet.

### Article Use
Use these source signals to refine the synopsis, topic links, people/company context, and method notes. If a source is a related external video rather than an exact official recording, keep it framed as supporting evidence.
