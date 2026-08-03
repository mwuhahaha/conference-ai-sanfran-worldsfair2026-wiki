---
title: "Claims: Let's integrate AI Agents in Event-Sourced Systems"
category: "claims"
generatedBy: "talk-semantic-digestion-v1"
sourceLabels: ["Official recording transcript", "Semantic digestion"]
---
# Claims: Let's integrate AI Agents in Event-Sourced Systems

- Talk: [[2026-07-01-divakar-kumar-let-s-integrate-ai-agents-in-event-sourced-systems]]

## Claims
- The speaker argues that event sourcing gives the fraud system an append-only memory of business facts, because commands are stored as events instead of mutating state. (`explicit`)
  - Evidence: "And we are following event sourcing as our methodology to store the events. So, what happens is like whenever user initiate a command, so that goes into our event store as an event as a business fact."
  - Transcript: [[youtube-o6U_2vd967Y-transcript]]
- The speaker argues that the agent layer should not replace the existing rule-based or ML systems, but should handle only the gray-zone cases they struggle to classify. (`explicit`)
  - Evidence: "We we are just trying to handle few of the areas like that is the gray zone areas with the help of agentic AI processing."
  - Transcript: [[youtube-o6U_2vd967Y-transcript]]
- The speaker argues that different bounded contexts, whether relational or NoSQL, still need a semantic layer to provide enough context for AI agents to decide well. (`explicit`)
  - Evidence: "And basically, like you could have a relational database or no SQL database. In turn, like you you need to just create the semantic layer for you to provide enough context to these AI agents."
  - Transcript: [[youtube-o6U_2vd967Y-transcript]]
- The speaker reports a tier-two design where a risk analyzer agent and a behavior analyzer agent both contribute to a final verdict, which is then emitted as an event. (`explicit`)
  - Evidence: "One is the risk analyzer agent, the other one is the behavior analyzer agent. And once these agents like come to a conclusion based on the different tools that it has, it will finally send the response to the verdict."
  - Transcript: [[youtube-o6U_2vd967Y-transcript]]
- The speaker says the agent memory must be short-term and in-memory because the transaction flow has a sub-500 millisecond SLA. (`explicit`)
  - Evidence: "And you also need to have a memory layer. For this particular use case like we are using an inch um short memory because uh you you can't really um rely on the long-term memory because you need to um adhere to the uh SLA that you uh provided to the customers because for for the transaction uh to be processed like it should be sub 500 milliseconds."
  - Transcript: [[youtube-o6U_2vd967Y-transcript]]

## Evidence Boundary
Derived from the linked official transcript. These are attributed talk takeaways and claims, not independent verification.
