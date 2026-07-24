---
title: "Claims: Using LLMs to Secure Source Code"
category: "claims"
generatedBy: "talk-semantic-digestion-v1"
sourceLabels: ["Official recording transcript", "Semantic digestion"]
---
# Claims: Using LLMs to Secure Source Code

- Talk: [[2026-06-29-eugene-yan-using-llms-to-secure-source-code]]

## Claims
- The speaker argues that frontier models are already helping defenders find and fix vulnerabilities at scale, not just in isolated demos. (`explicit`)
  - Evidence: "So what this means is that what's happened in April is 20x of last year's average. Um they attributed about twothirds of this to mess preview about 271 which shows that frontier models can help defenders like yourself find and fix vulnerabilities at scale."
  - Transcript: [[youtube-imFedndyXYQ-transcript]]
- He reports that the main bottleneck has moved away from finding bugs and toward verification, triage, and patching. (`explicit`)
  - Evidence: "We shared our observation that finding vulnerabilities now is quite straightforward. The bottleneck has now shifted to verification, triage, and patching."
  - Transcript: [[youtube-imFedndyXYQ-transcript]]
- He says a well-documented threat model can raise true positive rates substantially, citing a result near 90%. (`explicit`)
  - Evidence: "Um the first step is the threat model. So why does this matter? So several teams if you look at a code right finding have found that having a well doumented thread model really increases your true positive rate to 90%."
  - Transcript: [[youtube-imFedndyXYQ-transcript]]
- He reports that giving the agent tools to query APIs, read logs, and inspect source can push true positive rate close to 100%. (`explicit`)
  - Evidence: "And when they did this, their true positive rate was almost 100%. because the model could actually verify in the loop."
  - Transcript: [[youtube-imFedndyXYQ-transcript]]
- He argues that verification should be independent and adversarial so the agent starts by assuming the finding is false, which reduces false positives. (`explicit`)
  - Evidence: "assume that this vulnerability is false, try to confirm it's false or confirm it's true. So this sets the this sets a very high bar for the vulnerability which reduces the false positive rate."
  - Transcript: [[youtube-imFedndyXYQ-transcript]]
- He reports that patch quality improves when patches are validated by regression tests and by a fresh agent reattacking the fix. (`explicit`)
  - Evidence: "further right we can have a fresh discovery agent try to attack the patch code again is the patch comprehensive enough and teams have found that by giving the patching agent such feedback um you can actually the patch quality improves greatly right and you know This is the generative verifier loop."
  - Transcript: [[youtube-imFedndyXYQ-transcript]]
- He says human attention does not scale, so organizational disagreements about severity and ownership become a major limiter. (`explicit`)
  - Evidence: "But human attention doesn't scale. Your deaf, your product engineers and your security engineers, what if they don't agree on what high severity or uh critical severity is?"
  - Transcript: [[youtube-imFedndyXYQ-transcript]]

## Evidence Boundary
Derived from the linked official transcript. These are attributed talk takeaways and claims, not independent verification.
