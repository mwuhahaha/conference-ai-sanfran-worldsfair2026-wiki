---
title: "Claims: Model Whisperers: How Evals and Prompts Shape Agent Behavior"
category: "claims"
generatedBy: "talk-semantic-digestion-v1"
sourceLabels: ["Official recording transcript", "Semantic digestion"]
---
# Claims: Model Whisperers: How Evals and Prompts Shape Agent Behavior

- Talk: [[2026-06-30-chris-souza-model-whisperers-how-evals-and-prompts-shape-agent-behavior]]

## Claims
- The speakers argue that evals are not just scorecards; they are part of the feedback loop used to prove changes and drive iteration. (`explicit`)
  - Evidence: "Uh and then once your base structure is defined uh you can have you can then go to um having an eval and having a strong eval is very important as this gives you um like a way of proving the value of changes you make as well as running ablation experiments on any changes you make."
  - Transcript: [[youtube-xyL2Ltkh-SA-transcript]]
- They say agent reliability comes from the combination of agent capabilities, guardrails, and evals. (`explicit`)
  - Evidence: "Um so yeah the the reliability of your agent is basically a function of the capabilities of the agent uh the guard rails and the evals."
  - Transcript: [[youtube-xyL2Ltkh-SA-transcript]]
- They report that early intuition-based probing can be useful even though it is not scalable, because it reveals failure patterns quickly. (`explicit`)
  - Evidence: "Um so when you're first uh starting out it may be that uh you you know you could uh take a track of basically just going ahead and making the super comprehensive eval right um but we found it actually works better to first do intuition based approach where you kind of um first see"
  - Transcript: [[youtube-xyL2Ltkh-SA-transcript]]
- They argue that clear rubrics, concrete examples, and explanation capture are essential for human raters to be useful. (`explicit`)
  - Evidence: "Uh one was that providing them with a clear rubric of what they were actually rating with very clear examples."
  - Transcript: [[youtube-xyL2Ltkh-SA-transcript]]
- They show that trace inspection can uncover instruction-violating behavior that aggregate pass/fail metrics miss. (`explicit`)
  - Evidence: "So we really had to look at the traces to see what was going on. And in this example, you can see in the initial trace, it actually detects that there is a disclaimer in what it's searching for and it says, okay, I found a disclaimer and now I'm going to go ahead and remove it, which was not what we asked it to do."
  - Transcript: [[youtube-xyL2Ltkh-SA-transcript]]
- They emphasize that regression analysis should focus on recurring patterns across examples rather than isolated failures. (`explicit`)
  - Evidence: "Um so yeah this is basically just saying like it's very important to understand from these evals right what is the exact issue that you're having and figure out um the trade-offs here and then um you should also this is a very important point so you should focus on patterns rather than isolated runs"
  - Transcript: [[youtube-xyL2Ltkh-SA-transcript]]
- They say evals and test sets must keep evolving with production data and the current product stage. (`explicit`)
  - Evidence: "Uh important to of course keep it evolving. That's why we talked about having your online eval having test sets that are refreshed with production data, having sampling pipelines, all sorts of things."
  - Transcript: [[youtube-xyL2Ltkh-SA-transcript]]

## Evidence Boundary
Derived from the linked official transcript. These are attributed talk takeaways and claims, not independent verification.
