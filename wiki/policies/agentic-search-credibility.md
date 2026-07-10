---
title: "Agentic Search Credibility"
category: "policies"
topic: "agentic-search"
version: "2026-07-10.1"
status: "active"
sourceLabels: ["Credibility policy", "Evaluation-backed scoring"]
---

# Agentic Search Credibility

## Use Case
Rank people or sources for retrieval, search infrastructure, source triage, and research-agent discovery.

## View Signal Role
Contextual. Views matter when the goal is public influence or consumer search behavior; primary retrieval expertise matters more for correctness.

## Scoring Weights
| Signal | Weight |
| --- | ---: |
| `topic_fit` | 20 |
| `retrieval_expertise` | 25 |
| `primary_research_or_product` | 20 |
| `source_quality` | 15 |
| `deployment_signal` | 10 |
| `public_attention` | 10 |

## Evaluation Fixtures
| Name | Score | Expected Min | Result |
| --- | ---: | ---: | --- |
| Jo Kristian Bergum | 88.25 | 82 | pass |
| Han Xiao | 88.50 | 82 | pass |

## Policy Boundary
This policy scores credibility for one topic and use case. Do not reuse it for unrelated topics where public fame, domain credentials, implementation depth, or primary-source evidence should be weighted differently.

## Change Rule
Change one policy file at a time, rerun `python3 scripts/generate_synthesis_layers.py`, and inspect [[credibility-policy-evals]] before applying new scores.
