---
title: "Sandboxed Agent Execution"
category: "harnesses"
status: "seeded"
sourceLabels: ["Official schedule", "Question layer", "Topic synthesis"]
---

# Sandboxed Agent Execution

## Purpose
A runtime boundary for agents that can run code, touch files, browse, call tools, or influence production systems.

## Observed At AIE
- Sandbox talks argue that agent reliability depends on designed execution environments, not only model prompting.
- Security sessions connect permissions, provenance, network access, and rollback to agent safety.
- The strongest source layer is official schedule plus event recordings and slide evidence; OCR-only details remain supporting evidence.

## Recommended Implementation Steps
- Classify the task risk before choosing process, container, microVM, network, and secret boundaries.
- Default to no ambient credentials and explicit network egress rules.
- Capture commands, diffs, artifacts, resource usage, and exit conditions.
- Require human approval before production mutation unless the policy explicitly allows autonomous action.
- Retain incident evidence so sandbox policy can be tightened after failures.

## Source Evidence
- [[ai-sandboxes]] - Topic synthesis
- [[agent-security]] - Topic synthesis
- [[what-security-boundaries-should-agents-have]] - Question layer
- [[2026-06-30-samuel-colvin-your-agent-needs-a-sandbox-not-a-desert]] - Official schedule
- [[2026-06-30-robert-brennan-sandboxes-aren-t-optional-runtime-isolation-patterns-for-coding-agents-at-scale]] - Official schedule
- [[2026-06-30-ivan-burazin-kubernetes-is-not-your-sandbox]] - Official schedule

## Evidence Boundary
This is a reusable workflow synthesized from the linked conference evidence. Treat it as a recommended implementation pattern, not as a direct quote from any single talk.
