---
title: "Coding Agent Platforms"
category: "evaluations"
status: "tentative"
confidence: "medium"
sourceLabels: ["Harness", "Tool inventory", "Topic synthesis"]
---
# Coding Agent Platforms

## Evidence
- [[coding-agents]] - Topic synthesis
- [[software-factories]] - Topic synthesis
- [[codex]] - Tool inventory
- [[claude-agent-sdk]] - Tool inventory
- [[cursor]] - Tool inventory
- [[github-copilot]] - Tool inventory
- [[coding-agent-code-review-loop]] - Harness

## Decision Question
Compare coding-agent platforms by whether they help a team ship reviewed, testable, reversible changes rather than only generating code quickly.

## Criteria
- Repository context retrieval and task planning
- Diff quality, test execution, and review evidence
- Sandboxing, permissions, and rollback controls
- Team workflow fit across IDE, CLI, cloud, and CI
- Traceability for why a change was made

## Tentative Recommendation
Tentative: trial platforms against one real repository workflow using the agent-eval-gate and code-review-loop harnesses before choosing a default.

## Confidence
medium. No recommendation should be treated as final without a hands-on trial or source-backed comparison for the concrete use case.

## Open Questions
- Which current project workflow is the evaluation being applied to?
- Which failure mode would make the recommendation wrong?
- Which source or trial result would change the score?
