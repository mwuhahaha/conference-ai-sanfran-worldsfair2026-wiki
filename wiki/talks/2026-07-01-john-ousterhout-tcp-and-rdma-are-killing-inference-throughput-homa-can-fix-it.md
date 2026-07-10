---
title: "TCP and RDMA are Killing Inference Throughput; Homa can Fix It"
category: "talks"
date: "2026-07-01"
time: "9:20am-9:40am"
track: "Software Factories"
room: "Main Stage"
speakers: ["John Ousterhout"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Software Factories"
scheduleRoom: "Main Stage"
scheduleLabels: ["Software Factories", "Main Stage", "keynote", "confirmed"]
---
# TCP and RDMA are Killing Inference Throughput; Homa can Fix It

## Conference Context
- Date/time: 2026-07-01 · 9:20am-9:40am
- Track/room: Software Factories · Main Stage
- Speaker(s): John Ousterhout
- Session type/status: keynote · confirmed

- Track: Software Factories
- Room: Main Stage
- Session type: keynote
- Status: confirmed

## Session Description
Modern AI inferencing is shifting from monolithic requests to complex agentic workflows and disaggregated KV stores. As a result, AI network traffic is no longer just very large transfers; tiny metadata requests are becoming more and more common, and their latency has a critical impact on throughput. Unfortunately, legacy transport protocols such as TCP and RDMA perform poorly on these workloads due to poor congestion control and head-of-line blocking. This talk will discuss the problems with TCP and RDMA and provide a brief introduction to the Homa transport protocol. Homa uses receiver-driven flow control and capitalizes on priority queues in network switches to reduce short-message latency by 10x for workloads like those in AI datacenters.

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
- [[john-ousterhout]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.
