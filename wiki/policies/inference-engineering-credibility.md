---
title: "Inference Engineering Credibility"
category: "policies"
topic: "inference-engineering"
version: "2026-07-10.1"
status: "active"
sourceLabels: ["Credibility policy", "Evaluation-backed scoring"]
---

# Inference Engineering Credibility

## Use Case
Rank people or sources for inference engines, routing, latency, GPU utilization, and model-serving operations.

## View Signal Role
Low unless evaluating public education reach. Systems evidence, benchmarks, and operating scale dominate.

## Scoring Weights
| Signal | Weight |
| --- | ---: |
| `topic_fit` | 20 |
| `systems_expertise` | 30 |
| `production_scale` | 20 |
| `benchmark_or_paper` | 15 |
| `operational_signal` | 10 |
| `public_attention` | 5 |

## Evaluation Fixtures
| Name | Score | Expected Min | Result |
| --- | ---: | ---: | --- |
| Charles Frye | 86.00 | 82 | pass |
| Ion Stoica | 92.65 | 84 | pass |

## Policy Boundary
This policy scores credibility for one topic and use case. Do not reuse it for unrelated topics where public fame, domain credentials, implementation depth, or primary-source evidence should be weighted differently.

## Change Rule
Change one policy file at a time, rerun `python3 scripts/generate_synthesis_layers.py`, and inspect [[credibility-policy-evals]] before applying new scores.
