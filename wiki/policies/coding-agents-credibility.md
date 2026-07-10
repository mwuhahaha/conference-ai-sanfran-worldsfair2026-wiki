---
title: "Coding Agents Credibility"
category: "policies"
topic: "coding-agents"
version: "2026-07-10.1"
status: "active"
sourceLabels: ["Credibility policy", "Evaluation-backed scoring"]
---

# Coding Agents Credibility

## Use Case
Rank people or sources for practical coding-agent workflow guidance.

## View Signal Role
Minor. Views can indicate broad adoption, but code/review practice and shipped artifacts matter more.

## Scoring Weights
| Signal | Weight |
| --- | ---: |
| `topic_fit` | 20 |
| `practitioner_depth` | 25 |
| `shipped_artifacts` | 20 |
| `official_or_primary_source` | 15 |
| `peer_recognition` | 10 |
| `production_scale` | 5 |
| `public_attention` | 5 |

## Evaluation Fixtures
| Name | Score | Expected Min | Result |
| --- | ---: | ---: | --- |
| Kent C. Dodds | 88.75 | 82 | pass |
| Jason Liu | 89.25 | 82 | pass |

## Policy Boundary
This policy scores credibility for one topic and use case. Do not reuse it for unrelated topics where public fame, domain credentials, implementation depth, or primary-source evidence should be weighted differently.

## Change Rule
Change one policy file at a time, rerun `python3 scripts/generate_synthesis_layers.py`, and inspect [[credibility-policy-evals]] before applying new scores.
