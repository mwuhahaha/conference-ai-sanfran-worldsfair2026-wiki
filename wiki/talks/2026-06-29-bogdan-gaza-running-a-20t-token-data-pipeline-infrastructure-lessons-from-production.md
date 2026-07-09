---
title: "Running a 20T-Token Data Pipeline: Infrastructure Lessons from Production"
category: "talks"
date: "2026-06-29"
time: "3:20pm-3:40pm"
track: "Expo Stage 3 SW"
room: "Expo Stage 3 SW"
speakers: ["Bogdan Gaza"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: ""
scheduleRoom: "Expo Stage 3 SW"
scheduleLabels: ["Expo Stage 3 SW", "session", "confirmed"]
---
# Running a 20T-Token Data Pipeline: Infrastructure Lessons from Production

## Official Schedule Context
- Date/time: 2026-06-29 · 3:20pm-3:40pm
- Track/room: track TBD · Expo Stage 3 SW
- Speaker(s): Bogdan Gaza
- Session type/status: session · confirmed

## Schedule Labels
- Track: track TBD
- Room: Expo Stage 3 SW
- Session type: session
- Status: confirmed

## Official Description
The problem. Curation algorithms tend to get the spotlight: model-based quality filtering,

embedding-based deduplication, synthetic generation at scale, target distribution matching. The

engineering behind them, the systems that actually run those algorithms reliably on petabytes of

data and thousands of GPUs, usually gets overlooked. This session is about the engineering. What we

built. The infrastructure behind two production data curation pipelines, on two very different

shapes of workload: Arcee Trinity-Large-Thinking three model generations in nine months, with the

curated corpus scaling from 8T to 10T to 20T tokens. Trinity-Large's 20T-token corpus included 8T+

synthetic tokens generated on clusters peaking at 2,048 H100 GPUs. Each generation incorporated

deeper curation and broader domain coverage; the pipeline ran end-to-end multiple times, not once.

Thomson Reuters legal 100B tokens of mid-training output, generated from TR's proprietary legal

corpus, delivered as a deployment artifact and plugged into their existing SFT and DPO post-

training. Different operational profile entirely: smaller scale, sensitive data, customer-

environment integration. What you'll learn about. The metadata bottleneck. At trillion-token scale,

fetching metadata from object storage across millions of files becomes the dominant source of idle

time. We offload metadata management to Spark and use a lightweight file-level distribution scheme

to drive idle time to near zero. Fault tolerance at multi-week scale. Long-running GPU inference

jobs fail. We use one-to-one partition mapping between Spark and Ray jobs to get idempotent,

resumable execution. A node failure no longer means reprocessing the dataset. Heterogeneous workload

scheduling. Curation pipelines mix CPU-heavy preprocessing (Spark) with GPU-heavy inference (Ray +

vLLM). An in-house scheduler routes each job type to isolated node pools, preventing resource

fragmentation and ensuring critical training jobs aren't blocked by upstream CPU work. Inference

tuning across models. vLLM defaults aren't right for every model. Tuning batch size, speculative

decoding, and n-gram sampling per-model yields up to 40% throughput improvement, without over-

engineering. Pipeline reproducibility. Treating a curated training corpus as a versioned deployment

artifact rather than a one-off output. What that enables when a customer wants to run mid-training

against a pre-trained base. For engineers building or operating large-scale data pipelines for ML

training

## Related YouTube Video
No related AI Engineer channel video found yet.

## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## People
- [[bogdan-gaza]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.

## Source-Derived Enrichment
This section is generated from all currently linked source material for the article: official schedule text, related video pages, cached transcripts, visible slide text, dense/reconstructed slide pages, and AI slide-classification audits.

### Source Signals
No linked video, transcript, or slide source has been attached yet.

### Article Use
Use these source signals to refine the synopsis, topic links, people/company context, and method notes. If a source is a related external video rather than an exact official recording, keep it framed as supporting evidence.
