---
title: "Agent Eval Gate"
category: "harnesses"
status: "seeded"
sourceLabels: ["Official schedule", "Question layer", "Slide/OCR evidence", "Topic synthesis"]
---
# Agent Eval Gate

## Overview
A release gate for coding or tool-using agents that checks task success, policy adherence, regression risk, and human-review handoff before broader rollout.

## Conference Context
- The Evals track treats evaluation as operating infrastructure, not a post-demo report.
- Coding-agent talks repeatedly connect automated work to review, quality gates, traces, and production rollout decisions.
- Slide and transcript evidence warns that static benchmarks are insufficient for agents that keep changing behavior.

## Implementation Pattern
- Define the exact action boundary the agent is allowed to cross.
- Collect golden tasks, adversarial tasks, and regression tasks for that boundary.
- Score task completion separately from policy adherence, latency/cost budget, and reviewability.
- Require evidence artifacts: trace, diff, test output, source citations, and final human decision.
- Version the gate policy and attach each run to the agent/model/tooling version that produced it.

## Evidence
- [[agent-evaluations]] - Topic synthesis
- [[how-should-coding-agents-be-evaluated-before-production-use]] - Question layer
- [[2026-06-29-laurie-voss-from-vibes-to-production-evaluating-and-shipping-ai-agents-that-work-101]] - Official schedule
- [[2026-06-30-philipp-schmid-don-t-ship-skills-without-evals]] - Official schedule
- [[2026-06-29-nnenna-ndukwe-how-to-build-quality-gates-into-agentic-coding-workflows]] - Official schedule
- [[youtube-Xfl50508LZM-slides]] - Slide/OCR evidence

## Evidence Boundary
This is a reusable workflow synthesized from the linked conference evidence. Treat it as a recommended implementation pattern, not as a direct quote from any single talk.
