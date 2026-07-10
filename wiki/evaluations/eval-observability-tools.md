---
title: "Eval And Observability Tools"
category: "evaluations"
status: "tentative"
confidence: "medium"
sourceLabels: ["Harness", "Official schedule", "Tool inventory", "Topic synthesis"]
---

# Eval And Observability Tools

## Decision Question
Compare eval and observability tooling by whether it connects user outcomes, traces, policy checks, and regression tests into one improvement loop.

## Criteria
- Custom eval authoring and versioning
- Trace and span quality for agent workflows
- Dataset management and failure clustering
- Human review ergonomics
- Production feedback loop support

## Source Evidence
- [[agent-evaluations]] - Topic synthesis
- [[arize]] - Tool inventory
- [[braintrust]] - Tool inventory
- [[langfuse]] - Tool inventory
- [[agent-eval-gate]] - Harness
- [[2026-06-30-soumya-gupta-building-closed-loop-evals-for-a-multimodal-agent-at-uber-scale]] - Official schedule

## Tentative Recommendation
Tentative: require a trial that reproduces one production-like failure and shows how the tool would prevent or detect it next time.

## Confidence
medium. No recommendation should be treated as final without a hands-on trial or source-backed comparison for the concrete use case.

## Open Questions
- Which current project workflow is the evaluation being applied to?
- Which failure mode would make the recommendation wrong?
- Which source or trial result would change the score?
