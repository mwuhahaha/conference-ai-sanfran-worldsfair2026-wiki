---
title: "AI : Learned Execution Graphs for Real-Time Anomaly Detection & Drift Classification in APIs"
category: "talks"
date: "2026-07-01"
time: "1:30pm-1:50pm"
track: "Graphs"
room: "Track 5"
speakers: ["Ritvik Pandya"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
---

# AI : Learned Execution Graphs for Real-Time Anomaly Detection & Drift Classification in APIs

## Official Schedule Context
- Date/time: 2026-07-01 · 1:30pm-1:50pm
- Track/room: Graphs · Track 5
- Speaker(s): Ritvik Pandya
- Session type/status: sponsor · confirmed

## Official Description
API ingress controllers process requests through ordered sequences of middleware steps —

authentication, authorization, validation, rate limiting, routing, service invocation, caching. We

model this pipeline as a directed acyclic graph (DAG) learned from structured telemetry events, then

apply graph-based anomaly detection and drift classification in real time at 1,600+ TPS. The system

emits one structured event per processing step, constructs per-endpoint execution graphs using

sequence mining with statistical confidence thresholds, and learns per-node baselines (latency,

dependency, execution frequency). Three graph intelligence capabilities emerge: (1) Graph-based

anomaly attribution — compute per-node deviation ratios against learned baselines to identify the

exact bottleneck node and its dependency. In production, this pinpointed a 41x deviation at a single

graph node that was invisible to service-level monitoring, reducing root cause identification from

2-3 hours to under 30 seconds. (2) Graph structural drift detection — compare observed node

sequences against the learned graph topology to detect missing nodes (mandatory processing step

silently skipped), reordered nodes (middleware misconfiguration), and unexpected new nodes

(unauthorized middleware injection). Traditional monitoring reported "system healthy" when a

mandatory node was removed — latency dropped, errors at zero — only the learned graph comparison

detected the structural change. (3) Per-client graph fingerprinting — learn client-specific

execution graph profiles using exponential moving averages. Detect when a client's graph traversal

pattern changes, classify the cause (client behavior change vs. configuration drift vs.

infrastructure failover) using KL divergence on node-visit distributions, and apply graph-aware

adaptive control scoped to specific nodes rather than entire endpoints. The execution graph model

also enables a novel approach to retry storm detection: analyzing idempotency key entropy at graph

nodes to classify traffic as legitimate growth vs. retry amplification, and returning cached

responses at the specific graph node rather than rejecting requests — breaking the retry

amplification loop. Production system processing high TPS. Attendees will learn the graph

construction methodology, the anomaly attribution algorithm, and concrete patterns for adding

learned graph intelligence to any middleware pipeline.

## Related YouTube Video
No related AI Engineer channel video found yet.

## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## People
- [[ritvik-pandya]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.
