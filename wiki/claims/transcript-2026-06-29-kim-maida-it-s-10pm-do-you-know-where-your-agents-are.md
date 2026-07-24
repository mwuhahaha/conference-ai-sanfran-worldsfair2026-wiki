---
title: "Claims: It's 10pm. Do You Know Where Your Agents Are?"
category: "claims"
generatedBy: "talk-semantic-digestion-v1"
sourceLabels: ["Official recording transcript", "Semantic digestion"]
---
# Claims: It's 10pm. Do You Know Where Your Agents Are?

- Talk: [[2026-06-29-kim-maida-it-s-10pm-do-you-know-where-your-agents-are]]

## Claims
- Agents given long-lived API keys are overprivileged and can take actions that exceed what the user intended. (`explicit`)
  - Evidence: "Right? So agents with API keys are indeed outpass 10. They're overprivileged. So this means they are able to act freely on decisions that they make that you may or may not agree with."
  - Transcript: [[youtube-I3znWC3MEXM-transcript]]
- Human-in-the-loop alone is not enough because tired or consent-fatigued humans cannot reliably police every agent action. (`explicit`)
  - Evidence: "And we can't just solve this with human in the loop. We spent decades solving access management for humans."
  - Transcript: [[youtube-I3znWC3MEXM-transcript]]
- The right place to add control is in the agentic execution path, where the runtime, MCP server, and resource API interact. (`strong`)
  - Evidence: "So in order to see where we can introduce security and access control, we have to take a look at the agentic execution path."
  - Transcript: [[youtube-I3znWC3MEXM-transcript]]
- Token exchange can preserve both the agent identity and the user identity while narrowing delegation to the requested access. (`explicit`)
  - Evidence: "So now we have three key pieces of information that we're missing from the API key demo. We know the identity of the agent that's requesting access."
  - Transcript: [[youtube-I3znWC3MEXM-transcript]]
- Policy can reject dangerous requests before a credential is minted, so there is nothing overprivileged to leak or replay. (`explicit`)
  - Evidence: "So what happens is when we make this call it's being eval the policy is evaluating the request against all of the permissions that the user has and uh it sees that there is actually a restriction in place that prevents agents from doing this and this credential never even existed."
  - Transcript: [[youtube-I3znWC3MEXM-transcript]]

## Evidence Boundary
Derived from the linked official transcript. These are attributed talk takeaways and claims, not independent verification.
