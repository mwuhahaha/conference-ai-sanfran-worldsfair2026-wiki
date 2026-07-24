---
title: "Highlights: Don't Ship Skills Without Evals"
category: "highlights"
generatedBy: "talk-semantic-digestion-v1"
sourceLabels: ["Official recording transcript", "Semantic digestion"]
---
# Highlights: Don't Ship Skills Without Evals

- Talk: [[2026-06-30-philipp-schmid-don-t-ship-skills-without-evals]]

## Highlights
- Write skill descriptions around both why and how the model should use the skill.
  - Evidence: "So, very important is the the why and the how for the model. So, why it should use that skill and then how it should use that skill."
  - Transcript: [[youtube-0vphxNt4wyk-transcript]]
- If the workflow is always the same, use a script instead of a skill.
  - Evidence: "You maybe you should write a script because if the the process or the workflow is always the same, you don't need to waste models and tokens for that exercise."
  - Transcript: [[youtube-0vphxNt4wyk-transcript]]
- Keep running evals with and without the skill so you can tell when the skill is no longer needed.
  - Evidence: "So, um always try to run evals with and without the skill enabled. And if the model achieves the performance without even like triggering the skill, you know you can retire that skill, save the cost uh for your tokens, and then also um don't keep like it redundant."
  - Transcript: [[youtube-0vphxNt4wyk-transcript]]
- Many failures come from the skill not being triggered correctly, especially when users do not describe their task in a way that matches the skill description.
  - Evidence: "The the skill skill description is very important. Uh we have seen 50% of the failures uh because the skill was not triggered correctly because the prompt of the user was not uh detailed enough for the model to understand, \"Hey, I need to use that skill to solve that task.\" And especially if you build agents for others, they are not aware of the skill descriptions you have for your model and for your skill."
  - Transcript: [[youtube-0vphxNt4wyk-transcript]]
- Run more than one trial per case because agent behavior is non-deterministic.
  - Evidence: "Then definitely run more than one trial when running evals. Like agents, our models are non-deterministic."
  - Transcript: [[youtube-0vphxNt4wyk-transcript]]

## Evidence Boundary
Derived from the linked official transcript. These are attributed talk takeaways and claims, not independent verification.
