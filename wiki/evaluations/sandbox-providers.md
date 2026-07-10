---
title: "Sandbox Providers"
category: "evaluations"
status: "tentative"
confidence: "medium"
sourceLabels: ["Harness", "Official schedule", "Tool inventory", "Topic synthesis"]
---
# Sandbox Providers

## Evidence
- [[ai-sandboxes]] - Topic synthesis
- [[agent-security]] - Topic synthesis
- [[sandboxed-agent-execution]] - Harness
- [[docker]] - Tool inventory
- [[daytona]] - Tool inventory
- [[browserbase]] - Tool inventory
- [[2026-06-30-samuel-colvin-your-agent-needs-a-sandbox-not-a-desert]] - Official schedule

## Decision Question
Compare sandbox providers by isolation strength, developer ergonomics, traceability, network/secret policy, and fit for code-running agents.

## Criteria
- Isolation boundary: process, container, VM, or microVM
- Network, filesystem, and secret controls
- Startup latency and task throughput
- Artifact capture and replay
- Integration with review and approval gates

## Tentative Recommendation
Tentative: choose the weakest sandbox that satisfies the task risk policy, but require stronger isolation for untrusted code, external input, production credentials, or cross-tenant workloads.

## Confidence
medium. No recommendation should be treated as final without a hands-on trial or source-backed comparison for the concrete use case.

## Open Questions
- Which current project workflow is the evaluation being applied to?
- Which failure mode would make the recommendation wrong?
- Which source or trial result would change the score?
