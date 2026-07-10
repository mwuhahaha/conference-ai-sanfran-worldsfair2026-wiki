---
title: "MCP Server Patterns"
category: "evaluations"
status: "tentative"
confidence: "medium-low"
sourceLabels: ["Official schedule", "Question layer", "Tool inventory", "Topic synthesis"]
---

# MCP Server Patterns

## Decision Question
Evaluate MCP/server patterns by whether they expose useful actions, context, and policy boundaries to agents without becoming an ungoverned tool surface.

## Criteria
- Tool contract clarity and schema quality
- Human-readable and agent-readable context
- Permission, auth, and approval boundaries
- Observability of tool use
- Failure behavior when the model chooses poorly

## Source Evidence
- [[mcp]] - Topic synthesis
- [[mcp]] - Tool inventory
- [[mcp-apps]] - Tool inventory
- [[what-security-boundaries-should-agents-have]] - Question layer
- [[2026-06-30-session-ai-agents-don-t-read-your-policy-docs-they-hit-your-apis]] - Official schedule

## Tentative Recommendation
Tentative: prefer narrow, policy-backed servers with explicit review paths before broad agent tool catalogs.

## Confidence
medium-low. No recommendation should be treated as final without a hands-on trial or source-backed comparison for the concrete use case.

## Open Questions
- Which current project workflow is the evaluation being applied to?
- Which failure mode would make the recommendation wrong?
- Which source or trial result would change the score?
