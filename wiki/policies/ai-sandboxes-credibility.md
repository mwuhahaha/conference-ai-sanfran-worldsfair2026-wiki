---
title: "AI Sandboxes Credibility"
category: "policies"
topic: "ai-sandboxes"
version: "2026-07-10.1"
status: "active"
sourceLabels: ["Credibility policy", "Evaluation-backed scoring"]
---

# AI Sandboxes Credibility

## Use Case
Rank people or sources for agent runtime isolation, tool permissions, code execution, and sandbox safety.

## View Signal Role
Very low. Isolation credibility should follow production security and runtime evidence, not popularity.

## Scoring Weights
| Signal | Weight |
| --- | ---: |
| `topic_fit` | 20 |
| `security_infra_practice` | 30 |
| `production_isolation` | 25 |
| `evidence_source` | 15 |
| `peer_recognition` | 5 |
| `public_attention` | 5 |

## Evaluation Fixtures
| Name | Score | Expected Min | Result |
| --- | ---: | ---: | --- |
| Solomon Hykes | 89.00 | 82 | pass |
| Samuel Colvin | 86.50 | 80 | pass |

## Policy Boundary
This policy scores credibility for one topic and use case. Do not reuse it for unrelated topics where public fame, domain credentials, implementation depth, or primary-source evidence should be weighted differently.

## Change Rule
Change one policy file at a time, rerun `python3 scripts/generate_synthesis_layers.py`, and inspect [[credibility-policy-evals]] before applying new scores.
