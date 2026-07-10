---
title: "Modality Misalignment and Originality Attribution in Short-Form Video: A Multi-Agent Approach at Platform Scale"
category: "talks"
date: "2026-06-29"
time: "12:05pm-12:25pm"
track: "Vision & OCR"
room: "Track 2"
speakers: ["Aditya Gautam"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Vision & OCR"
scheduleRoom: "Track 2"
scheduleLabels: ["Vision & OCR", "Track 2", "sponsor", "confirmed"]
---
# Modality Misalignment and Originality Attribution in Short-Form Video: A Multi-Agent Approach at Platform Scale

## Conference Context
- Date/time: 2026-06-29 · 12:05pm-12:25pm
- Track/room: Vision & OCR · Track 2
- Speaker(s): Aditya Gautam
- Session type/status: sponsor · confirmed

- Track: Vision & OCR
- Room: Track 2
- Session type: sponsor
- Status: confirmed

## Session Description
Short-form video presents a class of content understanding problems that are qualitatively different from text or single-modality media. Audio, visual, and text signals within the same piece of content frequently diverge, sometimes incidentally and sometimes deliberately, creating a modality misalignment that defeats systems designed around any single signal. At the same time, the resharing dynamics of short-form video platforms create originality attribution chains that degrade quickly and are poorly captured by metadata alone. Addressing both problems at platform scale, reliably and under real latency and cost constraints, is the challenge this talk is built around. The core of the talk is the multi-agent architecture developed to address this, published at ACM WSDM 2025, and the reasoning behind its design. Each agent in the system is specialized for a distinct aspect of the problem: understanding what a piece of content is actually communicating across modalities, identifying where those modalities diverge meaningfully, and tracing originality through the resharing graph to surface attribution that platform metadata misses. We will cover the design principles behind this decomposition, the tradeoffs between specialization and complexity, the evaluation framework built to measure performance in a setting where ground truth is genuinely ambiguous, and the practical optimizations that made the system viable at scale. We will also be honest about the limitations: where the multi-agent approach added overhead that simpler baselines handled adequately, and what the boundaries of the system's reliability actually look like in production conditions. The broader takeaway is a set of principles for approaching multimodal content understanding problems where the signals are misaligned by nature rather than by exception. Attendees will leave with a framework for thinking about agent decomposition across a complex multimodal problem, a grounded understanding of how originality attribution degrades at scale and what it takes to recover it, and practical lessons about building evaluation and optimization pipelines for systems where the problem itself resists clean benchmarking.

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
- [[aditya-gautam]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.
