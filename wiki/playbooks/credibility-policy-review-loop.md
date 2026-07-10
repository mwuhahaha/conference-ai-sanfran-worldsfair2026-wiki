---
title: "Credibility Policy Review Loop"
category: "playbooks"
status: "seeded"
sourceLabels: ["Policy evals", "Source rules", "Topic synthesis"]
---
# Credibility Policy Review Loop

## Overview
A maintenance workflow for changing topic-specific credibility scoring without losing how previous scores were made.

## Evidence
- [[credibility-policy-evals]] - Policy evals
- [[agent-evaluations]] - Topic synthesis
- [[source-boundary]] - Source rules

## Evidence Boundary
This playbook is a post-conference action layer. It should cite sources for motivation while keeping implementation advice separate from observed event evidence.

## When To Use
Use this whenever a score feels wrong, a new topic needs a different algorithm, or public attention should be weighted differently.

## Steps
- Change exactly one policy file under `raw/sources/credibility-policies/`.
- Add or adjust at least one eval fixture that names a person who should score high or low for that topic.
- Run `python3 scripts/generate_synthesis_layers.py` and inspect the policy eval report.
- If the eval contradicts domain intuition, tune the policy weights rather than hand-editing the score.
- Commit or review policy changes one policy at a time so future readers know how each score was made.
