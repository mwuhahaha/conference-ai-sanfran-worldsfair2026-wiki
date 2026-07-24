---
title: "Highlights: Model Whisperers: How Evals and Prompts Shape Agent Behavior"
category: "highlights"
generatedBy: "talk-semantic-digestion-v1"
sourceLabels: ["Official recording transcript", "Semantic digestion"]
---
# Highlights: Model Whisperers: How Evals and Prompts Shape Agent Behavior

- Talk: [[2026-06-30-chris-souza-model-whisperers-how-evals-and-prompts-shape-agent-behavior]]

## Highlights
- Start with a small set of core tasks and expand the eval later.
  - Evidence: "Um you can just kind of start with a few core tasks. So you can look through your agent and define what are the primary things that you want to target, right?"
  - Transcript: [[youtube-xyL2Ltkh-SA-transcript]]
- Test negatives, not only successful task completion, because absence of a bad behavior matters too.
  - Evidence: "Um, and so here it's important to also test the negatives. Checking if the model like didn't do something as bad, uh, something bad is just as critical as checking if it did the task."
  - Transcript: [[youtube-xyL2Ltkh-SA-transcript]]
- Use trace review when aggregate metrics do not explain a policy violation or unexpected failure.
  - Evidence: "So we really had to look at the traces to see what was going on. And in this example, you can see in the initial trace, it actually detects that there is a disclaimer in what it's searching for and it says, okay, I found a disclaimer and now I'm going to go ahead and remove it, which was not what we asked it to do."
  - Transcript: [[youtube-xyL2Ltkh-SA-transcript]]
- Define launch criteria and acceptable regressions before treating a model as ready.
  - Evidence: "What's an acceptable regression versus not? Things like that. As you're doing these systems, it's important to like uh get some clarity early on on what is your gatekeeping rule like what's your launch criteria."
  - Transcript: [[youtube-xyL2Ltkh-SA-transcript]]
- Keep the eval set and test data aligned with changing production behavior.
  - Evidence: "Uh important to of course keep it evolving. That's why we talked about having your online eval having test sets that are refreshed with production data, having sampling pipelines, all sorts of things."
  - Transcript: [[youtube-xyL2Ltkh-SA-transcript]]

## Evidence Boundary
Derived from the linked official transcript. These are attributed talk takeaways and claims, not independent verification.
