---
title: "Claims: Don't Ship Skills Without Evals"
category: "claims"
generatedBy: "talk-semantic-digestion-v1"
sourceLabels: ["Official recording transcript", "Semantic digestion"]
---
# Claims: Don't Ship Skills Without Evals

- Talk: [[2026-06-30-philipp-schmid-don-t-ship-skills-without-evals]]

## Claims
- The speaker reports that skills improve performance on average by roughly 15% in the Skill Bench update. (`explicit`)
  - Evidence: "So, do skills work? Yes, they do work and I going back to a skills bench which has an update of 1.1 which has evaluated all kinds of open and closed models in different harnesses showing that skills on average improve the performance by roughly 15%."
  - Transcript: [[youtube-0vphxNt4wyk-transcript]]
- The speaker argues that human-written skills are better than AI-generated skills, which can hurt performance. (`explicit`)
  - Evidence: "And what I found out is that human-written skills are the best we can provide. Uh AI-generated skills can uh impact performance negatively."
  - Transcript: [[youtube-0vphxNt4wyk-transcript]]
- The speaker recommends using real production traces when possible because they are more valuable than synthetic examples. (`explicit`)
  - Evidence: "And then if you have already some customer or production traces, try to include those as well because nothing is better than than real-world data."
  - Transcript: [[youtube-0vphxNt4wyk-transcript]]
- The speaker says skill changes should not merge unless the eval improves, so regression tests gate skill updates. (`explicit`)
  - Evidence: "And we run them on every change to the skill. So, if a change happens to or like a diff to the skill file, the eval will be run, and there will also be a result, and the change will not be merged if it is not improving the test cases."
  - Transcript: [[youtube-0vphxNt4wyk-transcript]]
- The speaker argues that evals should be kept even after a skill is retired so the team can detect degradation and reintroduce the skill if needed. (`explicit`)
  - Evidence: "You don't need to throw that eval away because you throw the skill away. You can keep that eval to make sure that the model or the agent keeps the performance and as soon as you start seeing some degradation, you can reintroduce the skill."
  - Transcript: [[youtube-0vphxNt4wyk-transcript]]

## Evidence Boundary
Derived from the linked official transcript. These are attributed talk takeaways and claims, not independent verification.
