---
title: "Highlights: It's 10pm. Do You Know Where Your Agents Are?"
category: "highlights"
generatedBy: "talk-semantic-digestion-v1"
sourceLabels: ["Official recording transcript", "Semantic digestion"]
---
# Highlights: It's 10pm. Do You Know Where Your Agents Are?

- Talk: [[2026-06-29-kim-maida-it-s-10pm-do-you-know-where-your-agents-are]]

## Highlights
- Authenticate the runtime and delegate only part of the user's permissions before the agent is allowed to call downstream services.
  - Evidence: "So the authorization server is then going to prompt the user for their consent to delegate access with a subset of their permissions."
  - Transcript: [[youtube-I3znWC3MEXM-transcript]]
- Issue tokens that are audience-restricted to a single downstream MCP server instead of reusing a broad credential everywhere.
  - Evidence: "Now if the delegation chain and the requested access are within policy then the security token service issues an access token for the downstream resource and this token has an audience declaring that only this target MCP server is allowed to use it to make requests."
  - Transcript: [[youtube-I3znWC3MEXM-transcript]]
- Block unsafe operations before the credential exists rather than minting a broad token and trying to police it later.
  - Evidence: "So the policy evaluates before the credential is minted, which means you don't have an overprivileged credential that's just floating around then that uh you were supposed to then prevent the entity from receiving."
  - Transcript: [[youtube-I3znWC3MEXM-transcript]]
- Make human approval contingent on the approver's role so an exhausted user cannot approve everything by reflex.
  - Evidence: "uh even though I approved it. So we can prevent kind of people from just consent fatigue clicking over and over just to get things done."
  - Transcript: [[youtube-I3znWC3MEXM-transcript]]
- The approach is meant to work across CLI agents, custom agents, gateways, and third-party or proprietary MCP servers.
  - Evidence: "It works with the CLI. It works with thirdparty as well as proprietary MCP servers, MCP gateways, agent to agent, uh any OOTH identity provider."
  - Transcript: [[youtube-I3znWC3MEXM-transcript]]

## Evidence Boundary
Derived from the linked official transcript. These are attributed talk takeaways and claims, not independent verification.
