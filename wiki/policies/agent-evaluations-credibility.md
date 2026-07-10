---
title: "Agent Evaluations Credibility"
category: "policies"
topic: "agent-evaluations"
version: "2026-07-10.1"
status: "active"
sourceLabels: ["Credibility policy", "Evaluation-backed scoring"]
---

# Agent Evaluations Credibility

## Use Case
Rank people or sources for eval design, observability, review loops, and production agent quality.

## View Signal Role
Low. Eval credibility comes from repeatable artifacts, production failure coverage, and trace evidence.

## Scoring Weights
| Signal | Weight |
| --- | ---: |
| `topic_fit` | 15 |
| `domain_practice` | 25 |
| `evaluation_artifacts` | 25 |
| `production_scale` | 15 |
| `source_depth` | 15 |
| `public_attention` | 5 |

## Evaluation Fixtures
| Name | Score | Expected Min | Result |
| --- | ---: | ---: | --- |
| Aparna Dhinakaran | 91.75 | 84 | pass |
| Laurie Voss | 87.25 | 82 | pass |

## Policy Boundary
This policy scores credibility for one topic and use case. Do not reuse it for unrelated topics where public fame, domain credentials, implementation depth, or primary-source evidence should be weighted differently.

## Change Rule
Change one policy file at a time, rerun `python3 scripts/generate_synthesis_layers.py`, and inspect [[credibility-policy-evals]] before applying new scores.
