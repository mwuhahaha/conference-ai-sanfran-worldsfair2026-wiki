---
title: "Highlights: Agentic Development Security"
category: "highlights"
generatedBy: "talk-semantic-digestion-v1"
sourceLabels: ["Official recording transcript", "Semantic digestion"]
---
# Highlights: Agentic Development Security

- Talk: [[2026-06-29-ezra-tanzer-agentic-development-security]]

## Highlights
- Agentic security should be treated as a three-part problem: generated output, connected components, and runtime behavior.
  - Evidence: "Uh it's really critical to secure what agents generate, what they use, and what they do. Um and I'll spend a couple minutes talking about our journey in each of these pillars over the last year, what we've learned and uh and our current perspective."
  - Transcript: [[youtube-cgimkNGNjvU-transcript]]
- Asynchronous hooks are a better fit than synchronous scans when the goal is deterministic enforcement without adding latency or context bloat.
  - Evidence: "Only then will it kick off a fix and validate loop. So now the workflow is deterministic. Latency is removed because all that testing happens asynchronously."
  - Transcript: [[youtube-cgimkNGNjvU-transcript]]
- Skills need their own security review because they can carry elevated privilege and even persist malicious behavior after removal.
  - Evidence: "That risk can still persist after the fact. Um, and in an audit that we did of nearly 4,000 skills on Claw Hub, uh, over one in eight had a critical severity issue and we actually found 76 malicious payloads, uh, in in that subset."
  - Transcript: [[youtube-cgimkNGNjvU-transcript]]
- Background and cloud agents make human approval prompts less viable, so finer-grained policies become more important.
  - Evidence: "But I think as we move towards more background agents and cloud agents being ran where you're trying to trying to step away and trying to not be sitting at your desk babysitting the agent entirely um asks are much much less viable option."
  - Transcript: [[youtube-cgimkNGNjvU-transcript]]
- Visibility, auditability, and traceability are central to trusting agents in everyday development workflows.
  - Evidence: "Give me that visibility. Give me that audibility. Give me that traceability. Uh, really important aspects in learning how to how to how to trust the agents and making sure that they're not going off the rail."
  - Transcript: [[youtube-cgimkNGNjvU-transcript]]

## Evidence Boundary
Derived from the linked official transcript. These are attributed talk takeaways and claims, not independent verification.
