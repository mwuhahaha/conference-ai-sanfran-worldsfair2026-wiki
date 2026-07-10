---
title: "Coding Agent Code Review Loop"
category: "harnesses"
status: "seeded"
sourceLabels: ["Official schedule", "Question layer", "Topic synthesis"]
---

# Coding Agent Code Review Loop

## Purpose
A workflow for letting agents produce code while preserving reviewer comprehension, test evidence, rollback paths, and issue-specific context.

## Observed At AIE
- Software-factory and coding-agent sessions frame review as a loop across prompt, diff, tests, trace, and user impact.
- Several talks separate code generation from the discipline needed to decide whether generated code should land.
- The conference graph links coding agents to context engines, PR analysis, quality gates, and team adoption.

## Recommended Implementation Steps
- Start with a task contract that names files, tests, owner, and done criteria.
- Have the agent produce a diff plus a short evidence bundle rather than only a prose summary.
- Run deterministic checks and an LLM review against policy-specific failure modes.
- Ask the human reviewer to inspect the riskiest changed behavior, not every generated token.
- Record what passed, what failed, and which reviewer decision changed the policy.

## Source Evidence
- [[coding-agents]] - Topic synthesis
- [[software-factories]] - Topic synthesis
- [[what-makes-a-codebase-agent-ready]] - Question layer
- [[2026-06-29-daksh-gupta-what-we-learned-by-analyzing-1m-ai-generated-prs]] - Official schedule
- [[2026-06-29-itamar-friedman-the-last-human-code-review-building-trust-in-ai-generated-code]] - Official schedule
- [[2026-06-30-alex-volkov-the-z-l-continuum-should-ai-engineers-still-read-code]] - Official schedule

## Evidence Boundary
This is a reusable workflow synthesized from the linked conference evidence. Treat it as a recommended implementation pattern, not as a direct quote from any single talk.
