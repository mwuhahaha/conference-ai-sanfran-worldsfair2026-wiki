---
title: "It's 10pm. Do You Know Where Your Agents Are?"
category: "talks"
date: "2026-06-29"
time: "2:50pm-3:10pm"
track: "Security"
room: "Track 5"
speakers: ["Kim Maida"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Security"
scheduleRoom: "Track 5"
scheduleLabels: ["Security", "Track 5", "sponsor", "confirmed"]
---
# It's 10pm. Do You Know Where Your Agents Are?

## Conference Context
- Date/time: 2026-06-29 · 2:50pm-3:10pm
- Track/room: Security · Track 5
- Speaker(s): Kim Maida
- Session type/status: sponsor · confirmed

- Track: Security
- Room: Track 5
- Session type: sponsor
- Status: confirmed

## Session Description
Agents right now can sign legal contracts, run untethered, manage your dating profile, conduct financial transactions, and push code to production. Most agents have long-lived API keys and are dangerously overprivileged even when they're not making requests. In this talk, I'll demo how to solve the problem with the right access at the right time. You'll walk away knowing how to control agent access whether you're running coding agents from the CLI, building MCP servers, or connecting agents to third-party APIs.

## Synthesis
### Transcript-Backed Summary
The talk argues that agents should not be handed broad, long-lived API keys; instead, access should be narrowed at the moment a tool call is proposed. The mechanism is to put a security token service in the agent execution path, authenticate both the runtime and the user, exchange identity-bearing tokens for short-lived audience-restricted tokens, and evaluate policy before anything is minted. The key tradeoff is that this adds authorization plumbing and scope design work, but it avoids overprivileged credentials, reduces replay and leak risk, and lets human approval itself be policy-governed instead of a blank check. The practical result is an access model that works for CLI agents, custom agent apps, and MCP servers while preserving least privilege and attribution.

### Key Takeaways
- Authenticate the runtime and delegate only part of the user's permissions before the agent is allowed to call downstream services.
  - Evidence: "So the authorization server is then going to prompt the user for their consent to delegate access with a subset of their permissions."
- Issue tokens that are audience-restricted to a single downstream MCP server instead of reusing a broad credential everywhere.
  - Evidence: "Now if the delegation chain and the requested access are within policy then the security token service issues an access token for the downstream resource and this token has an audience declaring that only this target MCP server is allowed to use it to make requests."
- Block unsafe operations before the credential exists rather than minting a broad token and trying to police it later.
  - Evidence: "So the policy evaluates before the credential is minted, which means you don't have an overprivileged credential that's just floating around then that uh you were supposed to then prevent the entity from receiving."
- Make human approval contingent on the approver's role so an exhausted user cannot approve everything by reflex.
  - Evidence: "uh even though I approved it. So we can prevent kind of people from just consent fatigue clicking over and over just to get things done."
- The approach is meant to work across CLI agents, custom agents, gateways, and third-party or proprietary MCP servers.
  - Evidence: "It works with the CLI. It works with thirdparty as well as proprietary MCP servers, MCP gateways, agent to agent, uh any OOTH identity provider."

### Claims From The Talk
- Agents given long-lived API keys are overprivileged and can take actions that exceed what the user intended. (`explicit`)
  - Evidence: "Right? So agents with API keys are indeed outpass 10. They're overprivileged. So this means they are able to act freely on decisions that they make that you may or may not agree with."
- Human-in-the-loop alone is not enough because tired or consent-fatigued humans cannot reliably police every agent action. (`explicit`)
  - Evidence: "And we can't just solve this with human in the loop. We spent decades solving access management for humans."
- The right place to add control is in the agentic execution path, where the runtime, MCP server, and resource API interact. (`strong`)
  - Evidence: "So in order to see where we can introduce security and access control, we have to take a look at the agentic execution path."
- Token exchange can preserve both the agent identity and the user identity while narrowing delegation to the requested access. (`explicit`)
  - Evidence: "So now we have three key pieces of information that we're missing from the API key demo. We know the identity of the agent that's requesting access."
- Policy can reject dangerous requests before a credential is minted, so there is nothing overprivileged to leak or replay. (`explicit`)
  - Evidence: "So what happens is when we make this call it's being eval the policy is evaluating the request against all of the permissions that the user has and uh it sees that there is actually a restriction in place that prevents agents from doing this and this credential never even existed."

### Topics Covered
- [[agent-security|Agent overprivilege]] — The problem of giving agents more authority than they need and the risks that follow.
- [[agent-security|Delegated authorization]] — Granting access on behalf of a user while preserving who the user is and what they are allowed to do.
- [[agent-security|Ephemeral access tokens]] — Credentials that are short-lived, audience-bound, and discarded after the call finishes.
- [[agent-security|Policy governance]] — Using governance rules to decide whether a requested action is allowed before any downstream token is issued.
- [[mcp-app-runtime|Agent execution path]] — The chain of runtime, MCP client, MCP server, and resource where authorization can be enforced.

### Tools And Named Systems
- **RFC8693** — The token exchange RFC used as the standards basis for narrowing delegated access.
- [[mcp|MCP]] — The tool-call protocol and server boundary used in the agent execution path.
- **Google** — An example identity provider used for signing in and obtaining delegated access in the demo.
- **Keycard** — The standards-based platform the speaker cites for providing a security token service and policy governance.

### Novel Concepts And Methods
- **Identity-chain delegation** — Pass the subject token and the runtime's own credentials into the exchange request so the security token service knows who is acting for whom.
- **Request-scoped token minting** — Ask for permissions only for the current tool call instead of for the whole session.
- **Pre-mint policy evaluation** — Check requested access against governance policy before issuing any downstream token.
- **Role-gated approval** — Require the human approver to hold a specific role before their approval can authorize an agent action.

### Open Questions
- **Where should the authorization barrier sit between the runtime, the MCP server, and the resource so useful actions still work while unsafe ones fail early?** — The talk depends on choosing the right enforcement point without breaking the agent loop.
- **How can teams overcome enterprise resistance to adopting token exchange or similar policy-driven access controls?** — Adoption friction could block the security model even if the technical approach is sound.
- **How fine-grained should scopes be when downstream services and MCP tools still need something manageable to maintain over time?** — Scope design determines whether the approach stays practical as systems grow.

### Derived Links And Source Material
- [[youtube-I3znWC3MEXM-transcript]] — dedicated official recording transcript.
- [[youtube-I3znWC3MEXM]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/I3znWC3MEXM--2026-06-29-kim-maida-it-s-10pm-do-you-know-where-your-agents-are.json`.

### Speaker Context
- [[kim-maida|Kim Maida]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[kim-maida]]

## Official YouTube Recording
- [[youtube-I3znWC3MEXM|It's 10pm. Do You Know Where Your Agents Are? — Kim Maida, Keycard]] — official AI Engineer YouTube recording published 2026-07-20.
- Evidence status: [[youtube-I3znWC3MEXM-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-I3znWC3MEXM]] - dedicated official event recording.
- [[youtube-I3znWC3MEXM-transcript]] - dedicated official recording transcript.

- Source video: `youtube-I3znWC3MEXM`
- Slide deck: [[youtube-I3znWC3MEXM-slides|Slides: It's 10pm. Do You Know Where Your Agents Are? — Kim Maida, Keycard]] — 11 visible slide image(s).
![[assets/slides/I3znWC3MEXM/slide-001.jpg]]
![[assets/slides/I3znWC3MEXM/slide-002.jpg]]
![[assets/slides/I3znWC3MEXM/slide-003.jpg]]
- Slide-derived themes for `youtube-I3znWC3MEXM`: track, june, engineering, future, founding, engineer, head, developer.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/I3znWC3MEXM.txt` (3,454 words).

## Transcript Markdown
- [[youtube-I3znWC3MEXM-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/I3znWC3MEXM.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-I3znWC3MEXM` — 3,454 transcript words; 6 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-I3znWC3MEXM`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-I3znWC3MEXM`: token, user, server, access, call, resource, might, ooth.
- Slide-derived themes for `youtube-I3znWC3MEXM`: track, june, engineering, future, founding, engineer, head, developer.
- Evidence links for `youtube-I3znWC3MEXM` (primary event evidence): [[youtube-I3znWC3MEXM]], [[youtube-I3znWC3MEXM-transcript]], [[youtube-I3znWC3MEXM-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
