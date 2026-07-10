---
title: "Credibility Policy Evals"
category: "evaluations"
status: "active"
confidence: "high"
sourceLabels: ["Credibility policy", "Evaluation-backed scoring"]
---
# Credibility Policy Evals

This page checks whether topic-specific credibility policies score known strong exemplars high enough. If a fixture fails, adjust the policy weights or fixture assumptions instead of overriding the score by hand.

## Result Summary
- Fixtures: 10
- Passing: 10
- Failing: 0

## Fixture Results
| Policy | Name | Score | Expected Min | Result | Why This Fixture Exists |
| --- | --- | ---: | ---: | --- | --- |
| [[coding-agents-credibility]] | Kent C. Dodds | 88.75 | 82 | pass | Known expert in production web/product engineering and developer education; useful high exemplar when judging practical coding-agent workflow advice. |
| [[coding-agents-credibility]] | Jason Liu | 89.25 | 82 | pass | Strong practical signal for AI engineering workflows, structured outputs, and hands-on Codex/coding-agent practice. |
| [[agent-evaluations-credibility]] | Aparna Dhinakaran | 91.75 | 84 | pass | High exemplar for AI observability and eval infrastructure because credibility comes from Arize/Phoenix-style production evaluation practice. |
| [[agent-evaluations-credibility]] | Laurie Voss | 87.25 | 82 | pass | High exemplar for practical agent eval framing and shipping guidance in the AIE graph. |
| [[agentic-search-credibility]] | Jo Kristian Bergum | 88.25 | 82 | pass | Known retrieval/search practitioner; a high exemplar when correctness depends on IR fundamentals rather than popularity. |
| [[agentic-search-credibility]] | Han Xiao | 88.50 | 82 | pass | High exemplar for dense retrieval and search/retrieval systems in the local Worldsfair graph. |
| [[ai-sandboxes-credibility]] | Solomon Hykes | 89.00 | 82 | pass | External calibration exemplar for container/runtime isolation: popularity should not be required for a high sandbox credibility score. |
| [[ai-sandboxes-credibility]] | Samuel Colvin | 86.50 | 80 | pass | High local exemplar for sandbox-not-desert framing and practical Python/runtime tooling credibility. |
| [[inference-engineering-credibility]] | Charles Frye | 86.00 | 82 | pass | High exemplar for explaining inference engines from first principles with strong technical depth. |
| [[inference-engineering-credibility]] | Ion Stoica | 92.65 | 84 | pass | External calibration exemplar for distributed systems and AI infrastructure; should score high even when the specific question is not about fame. |

## Interpretation Notes
- Fame and view signals are policy-specific. They are useful for public influence topics and weak for safety, inference, and evaluation correctness.
- A person can score high for one topic and low for another without contradiction.
- Scores are provenance records for how the algorithm judged a candidate, not permanent judgments of a person.
