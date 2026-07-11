---
title: "Evidence-Gated Agent Workflow"
category: "patterns"
status: "seeded"
sourceLabels: ["Claim synthesis", "Harness synthesis", "Topic synthesis"]
---

# Evidence-Gated Agent Workflow

## Pattern
A pattern for letting agents act only when the workflow can name the source evidence, acceptance gate, and review path attached to the action.

## When To Use
Use this when an agent can change code, call tools, retrieve external context, or produce a decision that another system may rely on.

## Implementation Moves
- Define the task boundary and the evidence required before the agent starts.
- Attach eval or policy checks that can stop, route, or downgrade the result.
- Keep source links, traces, diffs, screenshots, or transcript/slide references with the output.
- Require human approval when the evidence bundle is incomplete or the action crosses a high-risk boundary.

## Source Evidence
- [[agent-work-needs-runtime-boundaries]] - Claim synthesis
- [[evals-are-operational-gates]] - Claim synthesis
- [[agent-eval-gate]] - Harness synthesis
- [[coding-agent-code-review-loop]] - Harness synthesis
- [[agent-security]] - Topic synthesis

## Evidence Boundary
This is a reusable pattern synthesized from linked conference evidence. Treat it as an engineering abstraction, not as an official event claim or a direct quote.
