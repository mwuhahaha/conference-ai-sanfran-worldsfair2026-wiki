---
title: "Observed Work and Traceability"
category: "topics"
generatedBy: "talk-semantic-digestion-v1"
sourceLabels: ["Official recording transcript", "Semantic digestion"]
sourceAssessment:
  schemaVersion: 1
  claimId: claim:c20e809132db5938698f0ed17b6fdb38f08faf99e30bdea9cbeba6041dd341d0
  subjectId: concept:observed-work-and-traceability
  domain: topics page evidence coverage
  intendedUse: attributed_context
  asOf: '2026-07-30T00:00:00.000000Z'
  state: limited
  basis: official_primary_canonical
  message: This page is limited to source-attributed facts; independent support for broader claims may be limited.
  publicSourceIds:
  - source:official-wf26-youtube-2JX6JYyQG4Y
  - source:official-wf26-youtube-31GUkCBD-Uc
  - source:official-wf26-youtube-8qWIPUia2O8
  - source:official-wf26-youtube-9fubhllmsBU
  - source:official-wf26-youtube-KB41dTlX1Uc
  - source:official-wf26-youtube-OqM67QG_Ikk
  - source:official-wf26-youtube-Z2Erdirpudo
  - source:official-wf26-youtube-ZyIoTOAbRfs
sourceAssessmentBodySha256: sha256:63a183b485d6d010085968daacc0eda9f31eef863ff0cd5150e8aef04aafc1eb
---
# Observed Work and Traceability

## Overview
These proto-topics share a concern with making work observable, replayable, and understandable after the fact. The variation is whether the source of truth is traces, structured events, or learned state, but all of them aim to preserve enough evidence that future reasoning is grounded in what actually happened.

## Significance
These proto-topics share a concern with making work observable, replayable, and understandable after the fact. The variation is whether the source of truth is traces, structured events, or learned state, but all of them aim to preserve enough evidence that future reasoning is grounded in what actually happened.

## Applied Use
Use this topic to compare how the linked speakers frame the same problem or technique. Validate applicability in the target system before adopting a talk-derived recommendation.

## Transcript Digest Evidence
This section synthesizes 16 evidence-bound talk topic candidates across at least two talks.

### Cross-Talk Synthesis
These proto-topics share a concern with making work observable, replayable, and understandable after the fact. The variation is whether the source of truth is traces, structured events, or learned state, but all of them aim to preserve enough evidence that future reasoning is grounded in what actually happened.

### Constituent Talk Evidence
- [[2026-06-29-moritz-johner-we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night|We Gave an Agent Production Code Access and Then Tried to Sleep at Night]] — Containing an agent that needs Docker access by moving it into a micro-VM rather than a normal sandbox.
  - Transcript: [[youtube-LqLoYksJ6do-transcript]]
  - Evidence: "So, let me share a design that we came up with, which is still like in its in its infancy."
- [[2026-06-29-sam-bhagwat-every-harness-will-become-a-claw|Every Harness Will Become A Claw]] — The ladder of autonomy from LLMs to agents to harnesses to claws.
  - Transcript: [[youtube-8qWIPUia2O8-transcript]]
  - Evidence: "Um so so I want to you know there's as we're thinking about um the agentic spectrum I often compare it to uh self-driving as a spectrum right there are different levels of self-driving autonomy whether that's like lane assist whether that's Tesla S FSD whether that's I I'm sitting in the back of my"
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1|'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt 1']] — Hardware-isolated guest machines with smaller VMMs and stronger boundaries.
  - Transcript: [[youtube-OqM67QG_Ikk-transcript]]
  - Evidence: "So, all these new-age Rust-based VMMs, they have a much smaller memory footprint because they don't support as many devices, and they also boot much faster because they don't have as much craft."
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt2|'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt2']] — Using load, snapshot lineage, and restore cost to place sandboxes efficiently across a fleet.
  - Transcript: [[youtube-OqM67QG_Ikk-transcript]]
  - Evidence: "And so, here is a way where we can use snapshot rich restore for better orchestration. So, remember we discussed that a snapshot can have a lineage of many, many layers."
- [[2026-06-30-antje-barth-perception-agents|Perception Agents]] — The role of looking at the same screen or interface as the human to reduce explanation and improve collaboration.
  - Transcript: [[youtube-2JX6JYyQG4Y-transcript]]
  - Evidence: "What you need is this shared context. Because if we're looking the agent and myself at the same screen, I probably have much less explanating to do."
- [[2026-06-30-eve-bouffard-imagination-engineering|Imagination Engineering]] — Publishing one's reasoning and stream of consciousness for others to inspect.
  - Transcript: [[youtube-Z2Erdirpudo-transcript]]
  - Evidence: "But what about thinking in public? And it's basically what PG is doing, thinking in public."
- [[2026-06-30-maor-bril-evaling-video-slop|Evaling Video Slop]] — Whether content stays consistent across frames and shots over time.
  - Transcript: [[youtube-b_PmGocP4rc-transcript]]
  - Evidence: "Does the character stay the same character across multiple shots? Does the pacing make sense?"
- [[2026-06-30-sean-cai-state-of-data|State of Data]] — Enterprise-oriented infrastructure for owning workflows, routing models, and retraining on live work.
  - Transcript: [[youtube-ZyIoTOAbRfs-transcript]]
  - Evidence: "Enterprise in ways you wouldn't expect a data business to do. Once enterprises stop renting out labs intelligence and starts owning their own, you need an entire abstraction layer that doesn't exist yet."
- [[2026-06-30-soumya-gupta-building-closed-loop-evals-for-a-multimodal-agent-at-uber-scale|Building Closed-Loop Evals for a Multimodal Agent at Uber Scale]] — The system is designed to preserve merchant identity and user trust while improving photos.
  - Transcript: [[youtube-31GUkCBD-Uc-transcript]]
  - Evidence: "But for us, it's about one, preserving authenticity and trust. Two, improving the quality when we need to."
- [[2026-06-30-thariq-shihipar-field-guide-to-fable|Field Guide to Fable]] — The distinction between what the operator thinks they know and the real constraints in the environment.
  - Transcript: [[youtube-9fubhllmsBU-transcript]]
  - Evidence: "And so one of the things that I think a lot about is that the map is not the territory, right?"
- [[2026-07-01-daniel-chalef-citation-needed-provenance-for-llm-built-knowledge-graphs|Citation Needed: Provenance for LLM-Built Knowledge Graphs]] — The overhead of building provenance-aware graph artifacts at scale.
  - Transcript: [[youtube-H7puB0RwJMM-transcript]]
  - Evidence: "So, by the way, as an aside, lineage and provenence is expensive. Graph construction is really expensive uh in the way that graffiti does it."
- [[2026-07-01-nader-khalil-state-of-the-union-why-local-why-now|State of the Union: Why Local, Why Now]] — Performance work on smaller devices through tuning, quantization, and configuration.
  - Transcript: [[youtube-KB41dTlX1Uc-transcript]]
  - Evidence: "Uh doing a lot of work with the like tuning the models like quantizing the models uh to you know be fit for local."
- [[2026-07-01-nader-khalil-state-of-the-union-why-local-why-now-11-10am-11-30am-track-4-420|State of the Union: Why Local, Why Now]] — The tension between simple out-of-the-box usage and the flexibility of custom local systems.
  - Transcript: [[youtube-KB41dTlX1Uc-transcript]]
  - Evidence: "Can I add one thing to that? One of the biggest challenge so I think there's two two big challenges One is what we've been talking about of basically the trade-off of simplicity versus customizability."
- [[2026-07-01-ramana-siddanth-emani-your-finance-agent-s-bottleneck-is-you|Your Finance Agent's Bottleneck Is You]] — The idea that the key production constraint is how fast the engineer can improve the harness.
  - Transcript: [[youtube-z0sh8HyTrDo-transcript]]
  - Evidence: "So, how do we in real time fix these production bugs? The answer is your dev loop velocity."
- [[2026-07-01-vinoo-ganesh-how-kepler-built-verifiable-ai-for-financial-services|How Kepler Built Verifiable AI for Financial Services]] — Separating reasoning from computation so the model plans but does not calculate.
  - Transcript: [[youtube-Tt2kX2sgQio-transcript]]
  - Evidence: "[snorts] Um and so, what the model does is the model decides what to compute. It never does the computation itself."
- [[2026-07-01-yohei-nakajima-active-graph-agent-runtime-babyagi-4|Active Graph Agent Runtime (BabyAGI 4)]] — Mechanisms for attaching reacting code to graph updates and letting it emit new events.
  - Transcript: [[youtube-khVX_BUnEwU-transcript]]
  - Evidence: "And then they emit events, which then in turn updates the state of the agent, which might trigger new behaviors."

## Connections
The talk and transcript links in the evidence section are the admitted conference connections for this generated page.

## Source Coverage
This table summarizes the local evidence already linked from this topic. It is a navigation aid, not a claim that every linked page has been fully reviewed.

| Evidence type | Count | Review note |
| --- | ---: | --- |
| resources | 6 | Video/resource pages; check source status before treating as primary event evidence. |
| slides | 18 | OCR or reconstructed slide evidence; mark claims as OCR-derived unless image-reviewed. |
| talks | 16 | Official schedule pages; use for titles, speakers, tracks, and stated talk framing. |
| transcripts | 14 | Transcript markdown; check session matching and caption quality. |

### Talks
- [[2026-06-29-moritz-johner-we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night]]
- [[2026-06-29-sam-bhagwat-every-harness-will-become-a-claw]]
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1]]
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt2]]
- [[2026-06-30-antje-barth-perception-agents]]
- [[2026-06-30-eve-bouffard-imagination-engineering]]

### Resources
- [[youtube-T5IMo5ntyhA]]
- [[youtube-wsFd22SL1s8]]
- [[youtube-WJjInLeaJjo]]
- [[youtube-TqC1qOfiVcQ]]
- [[youtube-ESbWpPT_9-o]]
- [[youtube-wNH3q9pqn0U]]

### Slides
- [[youtube-T5IMo5ntyhA-slides]]
- [[youtube-T5IMo5ntyhA-dense-slides]]
- [[youtube-T5IMo5ntyhA-reconstructed-slides]]
- [[youtube-wsFd22SL1s8-slides]]
- [[youtube-wsFd22SL1s8-dense-slides]]
- [[youtube-wsFd22SL1s8-reconstructed-slides]]

### Transcripts
- [[youtube-LqLoYksJ6do-transcript]]
- [[youtube-8qWIPUia2O8-transcript]]
- [[youtube-OqM67QG_Ikk-transcript]]
- [[youtube-2JX6JYyQG4Y-transcript]]
- [[youtube-Z2Erdirpudo-transcript]]
- [[youtube-b_PmGocP4rc-transcript]]
## Evidence Graph
This section consolidates source evidence currently connected to this topic across scheduled talks, linked videos, transcripts, and slide-derived material.

### Linked Sessions
- [[2026-06-29-moritz-johner-we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night|We Gave an Agent Production Code Access and Then Tried to Sleep at Night]]
- [[2026-06-29-sam-bhagwat-every-harness-will-become-a-claw|Every Harness Will Become A Claw]]
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1|'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt 1']]
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt2|'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt2']]
- [[2026-06-30-antje-barth-perception-agents|Perception Agents]]
- [[2026-06-30-eve-bouffard-imagination-engineering|Imagination Engineering]]
- [[2026-06-30-maor-bril-evaling-video-slop|Evaling Video Slop]]
- [[2026-06-30-sean-cai-state-of-data|State of Data]]
- [[2026-06-30-soumya-gupta-building-closed-loop-evals-for-a-multimodal-agent-at-uber-scale|Building Closed-Loop Evals for a Multimodal Agent at Uber Scale]]
- [[2026-06-30-thariq-shihipar-field-guide-to-fable|Field Guide to Fable]]

### Media Signals
- `youtube-T5IMo5ntyhA` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-T5IMo5ntyhA`: text, memory, description, financial, goal, type, target, amount.
- Evidence links for `youtube-T5IMo5ntyhA` (supporting context only): [[youtube-T5IMo5ntyhA]], [[youtube-T5IMo5ntyhA-slides]], [[youtube-T5IMo5ntyhA-dense-slides]], [[youtube-T5IMo5ntyhA-reconstructed-slides]]
- `youtube-wsFd22SL1s8` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-wsFd22SL1s8`: clone, flask, project, code, create, scratch, systems, chat.
- Evidence links for `youtube-wsFd22SL1s8` (supporting context only): [[youtube-wsFd22SL1s8]], [[youtube-wsFd22SL1s8-slides]], [[youtube-wsFd22SL1s8-dense-slides]], [[youtube-wsFd22SL1s8-reconstructed-slides]]
- `youtube-WJjInLeaJjo` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-WJjInLeaJjo`: barth, developer, documentation, server, customer, experience, advocate, june.
- Evidence links for `youtube-WJjInLeaJjo` (supporting context only): [[youtube-WJjInLeaJjo]], [[youtube-WJjInLeaJjo-slides]], [[youtube-WJjInLeaJjo-dense-slides]], [[youtube-WJjInLeaJjo-reconstructed-slides]]
- `youtube-TqC1qOfiVcQ` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-TqC1qOfiVcQ`: claude, code, file, system, tools, prompts, custom, features.
- Evidence links for `youtube-TqC1qOfiVcQ` (supporting context only): [[youtube-TqC1qOfiVcQ]], [[youtube-TqC1qOfiVcQ-slides]], [[youtube-TqC1qOfiVcQ-dense-slides]], [[youtube-TqC1qOfiVcQ-reconstructed-slides]]
- `youtube-ESbWpPT_9-o` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-ESbWpPT_9-o`: research, decode, hardware, ideas, progress, iteration, given, software.
- Evidence links for `youtube-ESbWpPT_9-o` (supporting context only): [[youtube-ESbWpPT_9-o]], [[youtube-ESbWpPT_9-o-slides]], [[youtube-ESbWpPT_9-o-dense-slides]], [[youtube-ESbWpPT_9-o-reconstructed-slides]]
- `youtube-wNH3q9pqn0U` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-wNH3q9pqn0U`: solution, water, growth, crystal, salt, input, sources, services.
- Evidence links for `youtube-wNH3q9pqn0U` (supporting context only): [[youtube-wNH3q9pqn0U]], [[youtube-wNH3q9pqn0U-slides]], [[youtube-wNH3q9pqn0U-dense-slides]], [[youtube-wNH3q9pqn0U-reconstructed-slides]]
## Evidence Boundary
This page is content-derived from official event transcripts. The linked transcript excerpts support presence and attributed framing; they do not independently verify broader claims.
