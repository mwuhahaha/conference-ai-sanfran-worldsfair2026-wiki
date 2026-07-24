---
title: "Highlights: Your agent architecture has a half-life of 6 months"
category: "highlights"
generatedBy: "talk-semantic-digestion-v1"
sourceLabels: ["Official recording transcript", "Semantic digestion"]
---
# Highlights: Your agent architecture has a half-life of 6 months

- Talk: [[2026-06-30-dan-farrelly-your-agent-architecture-has-a-half-life-of-6-months]]

## Highlights
- Think about agent systems as three layers, not a pile of individual components: execution, context, and compute.
  - Evidence: "This is maybe the mental model. Not specific components. So, in my opinion, there are three discrete layers."
  - Transcript: [[youtube-X1kp-ABIIxQ-transcript]]
- Durable resumability requires state to live outside the running work, not in memory or on local disk.
  - Evidence: "So, for this this to work, a 3-hour run cannot hold state in memory or in disk. The state must live outside of the work."
  - Transcript: [[youtube-X1kp-ABIIxQ-transcript]]
- Execution should provide whole-session observability, including LLM calls, tools, database errors, permissions, triggers, and performance.
  - Evidence: "And now you end up kind of a mess bad abstractions. lastly, execution needs to provide observability across your entire session."
  - Transcript: [[youtube-X1kp-ABIIxQ-transcript]]
- Sandboxes should stay ephemeral; the execution layer gives them context, sequence, and durability instead of storing state itself.
  - Evidence: "So, I think when you have the execution layer separate, the execution layer is what gives the sandbox its context, its sequence, its durability."
  - Transcript: [[youtube-X1kp-ABIIxQ-transcript]]
- Outcome-based scoring becomes easier when the execution layer can attach and interpret real events like opening a PR or saving research.
  - Evidence: "If it's a research agent, was this research saved? Was it a good report? That is these these things that are events that you should be able to attach and when you have a system that can connect all these pieces, I think it's really makes doing a lot of those things um like creating outcome-based scores a lot easier."
  - Transcript: [[youtube-X1kp-ABIIxQ-transcript]]

## Evidence Boundary
Derived from the linked official transcript. These are attributed talk takeaways and claims, not independent verification.
