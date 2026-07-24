---
title: "Why Agentic Systems Need Ontologies"
category: "talks"
date: "2026-07-01"
time: "1:55pm-2:15pm"
track: "Graphs"
room: "Track 5"
speakers: ["Frank Coyle"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Graphs"
scheduleRoom: "Track 5"
scheduleLabels: ["Graphs", "Track 5", "sponsor", "confirmed"]
---
# Why Agentic Systems Need Ontologies

## Conference Context
- Date/time: 2026-07-01 · 1:55pm-2:15pm
- Track/room: Graphs · Track 5
- Speaker(s): Frank Coyle
- Session type/status: sponsor · confirmed

- Track: Graphs
- Room: Track 5
- Session type: sponsor
- Status: confirmed

## Session Description
Agentic systems fail in predictable ways: context degradation, brittle tool descriptions, fragile multi-agent handoffs, stop-reason confusion, and the ever-present temptation to fix reliability problems with more natural-language instructions. These anti-patterns aren't bugs to be patched turn by turn — they're symptoms of a missing architectural layer. LLMs reason probabilistically over domains they only partially understand, and no amount of prompt engineering fully closes that gap. This talk argues that the missing layer is an explicit ontology: a formal, shared map of the domain's concepts, relationships, and constraints. The pattern is not new — ontologies have driven commercial success in defense and intelligence systems for over a decade, where probabilistic models must operate over high-stakes enterprise data without drifting into nonsense. Graph databases like Neo4j and Amazon Neptune have made the underlying primitives widely accessible. We'll show how lightweight ontology constructs can surround an agentic system with enforceable logical constraints: typed entities and relationships that tools must respect, cardinality and domain restrictions that catch malformed tool calls before they execute, and a shared vocabulary that keeps coordinators and subagents talking about the same things. The session walks through several agentic applications — a multi-agent research workflow, a tool-heavy customer support agent, a coordinator-subagent delegation pattern — and shows in each case how an ontology layer addresses the kinds of anti-patterns catalogued in Anthropic's Claude Certified Architect exam. The result is a hybrid neurosymbolic architecture: probabilistic reasoning inside, logical guardrails outside. Who should attend: engineers building production agentic systems, architects evaluating reliability strategies beyond prompt engineering, and technical leads who suspect their agents need more structure than another system prompt can provide.

## Synthesis
### Transcript-Backed Summary
Frank Coyle argues that agentic systems need an explicit ontology layer because LLMs are probabilistic and agent loops are prone to drift, failure, and runaway cost. His core mechanism is to treat the model as the proposal engine and surround it with structured validation: an ontology provides shared entities, relationships, and constraints, while RDFS, OWL, and type checks can infer facts and reject malformed actions before they execute. The practical result is a hybrid architecture in which tool use becomes safer and more accountable, with fewer nonsense calls such as duplicate refunds, wrong-recipient payouts, or invalid statuses. He also emphasizes that this is not a blank-slate exercise: teams should reuse existing vocabularies and decide deliberately between top-down expert modeling and bottom-up extension from real cases.

### Key Takeaways
- Put a validation layer between the model's tool selection and actual execution so the ontology can judge whether the action makes sense.
  - Evidence: "This is where ontologies could come in. The tool's going to give us information. We put the information in a form that our our our our validator can use, and think about the validator as operating with this these ontologies about our domain, then we can make some sense of whether the response of the LLM is reasonable."
- Reuse existing vocabularies such as schema.org, FOAF, Dublin Core, and DBpedia instead of inventing every term from scratch.
  - Evidence: "Let's Let's add this information to the graph. Now, as as a help, it's helpful to be aware that there are existing taxonomies that people have been working on for the last 15 to 20 years."
- Choose between expert-led top-down modeling and data-led bottom-up growth based on the domain and the ontology's maturity.
  - Evidence: "Okay? There are a couple of ways you can approach it. You can have a top-down approach or a bottom-up approach."
- Keep agents as close to side-effect-free as possible until their outputs have been checked against typed and ontological constraints.
  - Evidence: "So, Pydantic at the door, ontology at the ledger, and pure agents and by the way, your agents should try to have no side effects."

### Claims From The Talk
- The speaker argues that neuro-symbolic AI is the missing guardrail layer for agentic systems because LLMs are probabilistic and need an explicit ontology around them. (`strong`)
  - Evidence: "And so, what I'd like to argue is that neuro-symbolic AI sort of represents a way to keep the LLM on its guardrails, because LLMs are by nature probabilistic."
- He says agent loops can break, drift, and drive up token costs, so they need careful control rather than open-ended iteration. (`explicit`)
  - Evidence: "The danger though of loops is that they can break. If you're If you're a programmer, you know, you've all go into infinite loop."
- He reports that RDFS and OWL let a system infer new facts and enforce constraints from domain, range, transitive, and functional properties. (`explicit`)
  - Evidence: "Or you want to be able to make inference over them. So, for example, there is uh some terms in this technology called RDFS."
- He argues that Pydantic should validate tool parameter types before ontology checks evaluate the result of a tool call. (`strong`)
  - Evidence: "But the idea is to surround the input with checks. Now, I've got this something that you that you should be at least taking a look at if you're doing some of this coding is something called Pydantic."
- He says OWL-style constraints can catch concrete errors such as duplicate refunds, payments sent to the wrong party, and invalid status values. (`explicit`)
  - Evidence: "So, you have these functional properties, disjoint properties. I'll just put these you can look at the slides, but essentially the errors it can catch."

### Topics Covered
- **Ontology guardrails** — Using explicit ontology rules as guardrails around probabilistic agent behavior.
- [[inference-engineering|RDFS and OWL inference]] — Formal inference and constraint mechanisms such as domain, range, transitivity, and functional properties.
- [[agent-evaluations|Agent loop validation]] — The execution pattern where an LLM proposes a tool action, a stop reason is checked, and the tool result is validated.
- **Ontology construction strategies** — Choosing between expert-defined schemas and data-driven ontology extension.
- [[agent-security|Tool-call typing]] — Typed tool arguments and structured result checking before downstream action.

### Tools And Named Systems
- [[pydantic|Pydantic]] — A Python library used to specify and enforce parameter types for tool inputs.
- **RDFS** — An RDF schema technology used for domain and range inference.
- **OWL** — A web ontology language used for properties, disjointness, and other logical constraints.
- **schema.org** — An existing vocabulary and ontology source the speaker recommends reusing.
- **FOAF** — A vocabulary for modeling social networks and related entities.
- **Dublin Core** — A vocabulary for describing research papers and books.
- **DBpedia** — A graph-based ontology used as the basis for Wikipedia lookup.

### Novel Concepts And Methods
- **Top-down ontology design** — Top-down ontology design starts with domain experts defining entities and relationships before implementation.
- **Bottom-up ontology expansion** — Bottom-up ontology growth adds entities and relationships from observed cases and data rather than starting from an expert schema.
- **Domain and range inference** — Domain and range assertions let the system infer types from tool or text statements.
- **Stop-reason tool loop** — A stop-reason-driven tool loop executes tools only when the model indicates tool use, then validates the result before continuing.
- **Type-first validation gate** — Type-first validation checks structured parameters before ontology-based result validation.
- **OWL constraint checking** — OWL constraint checking rejects malformed outputs by enforcing allowed values and disjoint categories.

### Open Questions
- **How should a team decide between top-down expert modeling and bottom-up ontology growth for a specific agentic domain?** — The answer determines whether the ontology will be stable and complete enough to support production guardrails.
- **Which checks belong in the ontology layer as hard constraints, and which should remain soft validation or human review?** — That boundary controls how much reliability the guardrails provide without blocking legitimate tool use.
- **How much ontology coverage is enough to keep agent loops from drifting or becoming too expensive?** — This sets the practical threshold for when the architecture actually improves reliability instead of adding overhead.

### Derived Links And Source Material
- [[youtube-Sir59K8ZDPU-transcript]] — dedicated official recording transcript.
- [[youtube-Sir59K8ZDPU]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/Sir59K8ZDPU--2026-07-01-frank-coyle-why-agentic-systems-need-ontologies.json`.

### Speaker Context
- [[frank-coyle|Frank Coyle]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[frank-coyle]]

## Official YouTube Recording
- [[youtube-Sir59K8ZDPU|Why Agentic Systems Need Ontologies — Frank Coyle, UC Berkeley]] — official AI Engineer YouTube recording published 2026-07-23.
- Evidence status: [[youtube-Sir59K8ZDPU-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-Sir59K8ZDPU]] - dedicated official event recording.
- [[youtube-Sir59K8ZDPU-transcript]] - dedicated official recording transcript.

- [[youtube-Sir59K8ZDPU-slides]] — extracted from the related public AI Engineer video.

- Source video: `youtube-Sir59K8ZDPU`
- Slide deck: [[youtube-Sir59K8ZDPU-slides|Slides: Why Agentic Systems Need Ontologies — Frank Coyle, UC Berkeley]] — 13 visible slide image(s).
![[assets/slides/Sir59K8ZDPU/slide-001.jpg]]
![[assets/slides/Sir59K8ZDPU/slide-002.jpg]]
![[assets/slides/Sir59K8ZDPU/slide-003.jpg]]
- Slide-derived themes for `youtube-Sir59K8ZDPU`: without, fear, probabilistic, track, july, nothing, mistake, sister.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/Sir59K8ZDPU.txt` (3,096 words).

## Transcript Markdown
- [[youtube-Sir59K8ZDPU-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/Sir59K8ZDPU.txt`.

## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-Sir59K8ZDPU` — 3,096 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-Sir59K8ZDPU`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-Sir59K8ZDPU`: okay, tool, ontologies, loops, called, ontology, graph, give.
- Slide-derived themes for `youtube-Sir59K8ZDPU`: without, fear, probabilistic, track, july, nothing, mistake, sister.
- Evidence links for `youtube-Sir59K8ZDPU` (primary event evidence): [[youtube-Sir59K8ZDPU]], [[youtube-Sir59K8ZDPU-transcript]], [[youtube-Sir59K8ZDPU-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
