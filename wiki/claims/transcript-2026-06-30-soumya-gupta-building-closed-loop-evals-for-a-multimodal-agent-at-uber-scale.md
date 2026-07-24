---
title: "Claims: Building Closed-Loop Evals for a Multimodal Agent at Uber Scale"
category: "claims"
generatedBy: "talk-semantic-digestion-v1"
sourceLabels: ["Official recording transcript", "Semantic digestion"]
---
# Claims: Building Closed-Loop Evals for a Multimodal Agent at Uber Scale

- Talk: [[2026-06-30-soumya-gupta-building-closed-loop-evals-for-a-multimodal-agent-at-uber-scale]]

## Claims
- The speakers say visual content is often the first signal shoppers see, and it can determine whether they click through and add an item to cart. (`explicit`)
  - Evidence: "Visual content actually plays a really important role for the user experience. So a photo is quite often the first signal that a customer gets that gives them that initial impression about a merchant."
  - Transcript: [[youtube-31GUkCBD-Uc-transcript]]
- They report that smaller merchants often lack the time, know-how, and money to produce high-quality photos. (`explicit`)
  - Evidence: "And when we speak to our merchants, there are three themes that kind of emerge. Lack of time, lack of know-how, and costs cuz these professional um photo shoots actually cost a lot of money."
  - Transcript: [[youtube-31GUkCBD-Uc-transcript]]
- They argue the system has to stay faithful to the original image, preserve merchant branding, and avoid making the marketplace look uniform. (`explicit`)
  - Evidence: "So, we're threading the needle here. We need to be able to stay faithful to the original image, preserve the brand of the merchant, and avoid everything looking the same."
  - Transcript: [[youtube-31GUkCBD-Uc-transcript]]
- They say logging is foundational because without it there is nothing to optimize or feed into a self-learning loop. (`explicit`)
  - Evidence: "You want to start with your logging cuz if you don't start with it, you have nothing to optimize for, let alone set up a self-learning loop."
  - Transcript: [[youtube-31GUkCBD-Uc-transcript]]
- They report that static offline models will not hold up under drift, so the system has to keep evolving over time. (`explicit`)
  - Evidence: "So the meta point I'm trying to get here is you've trained your offline model, but there will be long cases where your model is going to continue to fail and the static model will not work in the real system."
  - Transcript: [[youtube-31GUkCBD-Uc-transcript]]
- They describe reward hacking as edits that change pixels in a way that is not actually meaningful or influential. (`explicit`)
  - Evidence: "So, this is an example of a reward hacking actually. And and this is a nugatory change, but something that we don't think is a meaningful or influential change despite the actual raw pixels of the input and output being pretty different."
  - Transcript: [[youtube-31GUkCBD-Uc-transcript]]

## Evidence Boundary
Derived from the linked official transcript. These are attributed talk takeaways and claims, not independent verification.
