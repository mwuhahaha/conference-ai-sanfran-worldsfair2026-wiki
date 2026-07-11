---
title: "Sandboxed Delegation"
category: "patterns"
status: "seeded"
sourceLabels: ["Claim synthesis", "Harness synthesis", "Official schedule", "Topic synthesis"]
---

# Sandboxed Delegation

## Pattern
A pattern for delegating agent work into constrained execution environments whose tools, permissions, lifetime, and evidence trail are set before the work begins.

## When To Use
Use this for coding agents, browser agents, MCP tools, data agents, and any system where a model can affect files, services, credentials, or external state.

## Implementation Moves
- Choose the smallest execution boundary that can perform the task.
- Pass only task-specific credentials, files, network routes, and tool permissions.
- Capture commands, tool calls, artifacts, and verification outputs.
- Expire the environment and credentials after the run unless the policy explicitly permits persistence.

## Source Evidence
- [[agent-work-needs-runtime-boundaries]] - Claim synthesis
- [[sandboxed-agent-execution]] - Harness synthesis
- [[ai-sandboxes]] - Topic synthesis
- [[agent-security]] - Topic synthesis
- [[2026-06-30-robert-brennan-sandboxes-aren-t-optional-runtime-isolation-patterns-for-coding-agents-at-scale]] - Official schedule
- [[2026-06-30-samuel-colvin-your-agent-needs-a-sandbox-not-a-desert]] - Official schedule

## Evidence Boundary
This is a reusable pattern synthesized from linked conference evidence. Treat it as an engineering abstraction, not as an official event claim or a direct quote.
