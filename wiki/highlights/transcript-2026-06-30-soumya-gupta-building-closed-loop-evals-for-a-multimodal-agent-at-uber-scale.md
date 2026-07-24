---
title: "Highlights: Building Closed-Loop Evals for a Multimodal Agent at Uber Scale"
category: "highlights"
generatedBy: "talk-semantic-digestion-v1"
sourceLabels: ["Official recording transcript", "Semantic digestion"]
---
# Highlights: Building Closed-Loop Evals for a Multimodal Agent at Uber Scale

- Talk: [[2026-06-30-soumya-gupta-building-closed-loop-evals-for-a-multimodal-agent-at-uber-scale]]

## Highlights
- Start with logging before trying to optimize anything, because logs are what make diagnosis and self-learning possible.
  - Evidence: "You want to start with your logging cuz if you don't start with it, you have nothing to optimize for, let alone set up a self-learning loop."
  - Transcript: [[youtube-31GUkCBD-Uc-transcript]]
- Use objective human-labeling guidelines to reduce subjective noise when building the first target dataset.
  - Evidence: "Send it to our human labelers and give them a very objective guideline to label on. This is to remove any subjective biases or any noise coming in from human labelers."
  - Transcript: [[youtube-31GUkCBD-Uc-transcript]]
- Treat routing as a precision-and-recall problem so the guardrail matches the cost of letting bad images slip through.
  - Evidence: "Essentially, what we're doing is we're measuring the precision recall. In practice, your routers might actually be much more sophisticated."
  - Transcript: [[youtube-31GUkCBD-Uc-transcript]]
- Measure iterative image editing with pass-at-K so you can see whether more rounds actually improve the chance of success.
  - Evidence: "So, the metric we are measuring here is pass at K. Pass at K is essentially the pass rate at Kth iteration."
  - Transcript: [[youtube-31GUkCBD-Uc-transcript]]
- Check production impact by slicing metrics by geo, device type, and dish type instead of relying only on aggregate results.
  - Evidence: "So, in this area as opposed to the others, what we can do is sort of slice by geos, by device type, by dish type, etc."
  - Transcript: [[youtube-31GUkCBD-Uc-transcript]]

## Evidence Boundary
Derived from the linked official transcript. These are attributed talk takeaways and claims, not independent verification.
