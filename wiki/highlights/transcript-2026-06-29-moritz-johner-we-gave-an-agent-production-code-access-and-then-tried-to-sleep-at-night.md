---
title: "Highlights: We Gave an Agent Production Code Access and Then Tried to Sleep at Night"
category: "highlights"
generatedBy: "talk-semantic-digestion-v1"
sourceLabels: ["Official recording transcript", "Semantic digestion"]
---
# Highlights: We Gave an Agent Production Code Access and Then Tried to Sleep at Night

- Talk: [[2026-06-29-moritz-johner-we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night]]

## Highlights
- After the agent edits files, the deterministic layer vets the changes, commits them, pushes a PR, and watches CI so the higher-risk actions stay outside the agent.
  - Evidence: "So we got to take care of that. And then we commit it, we push it, we create a PR, um and then we watch CI."
  - Transcript: [[youtube-LqLoYksJ6do-transcript]]
- The system had to be given GitHub access, registry credentials, runtime tools, and network access, showing that useful remediation requires substantial repository and environment visibility.
  - Evidence: "So, to make that work, um we gave Patch Pilot a couple of things. We gave it GitHub access, um read and write access to clone the repository, to commit, and to push changes, to open up PR, to download the CI logs, and trigger CI."
  - Transcript: [[youtube-LqLoYksJ6do-transcript]]
- Keeping GitHub push and CI-triggering abilities out of the agent reduces blast radius if prompt injection occurs.
  - Evidence: "Instead, we pushed um that functionality out to the deterministic part cuz that's the thing that we can reason about and we can rely on that um you know, it just does these kind of kind of actions and we do not give um the agent these kinds of credentials cuz that then fundamentally fundamentally limits the blast radius of when in case the agent gets um prompt injected prompt injected."
  - Transcript: [[youtube-LqLoYksJ6do-transcript]]
- Running with a Docker socket in production felt unsafe enough that the team moved away from that design.
  - Evidence: "We run it like that in production at some point. Um, it didn't feel good. We moved off of that, um, and we evaluated all the other obvious options in like the Linux sphere Linux bubble when it comes to like sandboxing."
  - Transcript: [[youtube-LqLoYksJ6do-transcript]]
- The speaker treats the choice of what is deterministic versus agentic as the security model itself.
  - Evidence: "Um that kind of really limits the blast radius of an agent. So, that choice, what's that what's deterministic and what's agentic, that really is, you know, your security model in this case."
  - Transcript: [[youtube-LqLoYksJ6do-transcript]]

## Evidence Boundary
Derived from the linked official transcript. These are attributed talk takeaways and claims, not independent verification.
