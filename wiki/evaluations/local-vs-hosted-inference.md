---
title: "Local Vs Hosted Inference"
category: "evaluations"
status: "tentative"
confidence: "medium"
sourceLabels: ["Official schedule", "Question layer", "Tool inventory", "Topic synthesis"]
---
# Local Vs Hosted Inference

## Evidence
- [[inference-engineering]] - Topic synthesis
- [[what-latency-and-cost-budget-is-right-for-agent-systems]] - Question layer
- [[vllm]] - Tool inventory
- [[openrouter]] - Tool inventory
- [[modal]] - Tool inventory
- [[2026-07-01-qianru-lao-routing-llm-inference-in-production-from-engine-signals-to-policy]] - Official schedule

## Decision Question
Compare local and hosted inference by workload, latency budget, privacy boundary, operational ownership, and model-routing needs.

## Criteria
- Latency and throughput under realistic agent loops
- Data privacy and deployment environment
- Model availability and routing flexibility
- Operational burden and GPU utilization
- Cost attribution per user-visible task

## Tentative Recommendation
Tentative: use hosted inference for fast iteration and broad model access, then move bounded workloads local or dedicated only when privacy, latency, or utilization evidence justifies it.

## Confidence
medium. No recommendation should be treated as final without a hands-on trial or source-backed comparison for the concrete use case.

## Open Questions
- Which current project workflow is the evaluation being applied to?
- Which failure mode would make the recommendation wrong?
- Which source or trial result would change the score?
