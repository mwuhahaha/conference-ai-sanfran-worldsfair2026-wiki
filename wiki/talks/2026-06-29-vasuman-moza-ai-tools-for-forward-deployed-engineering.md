---
title: "AI tools for Forward Deployed Engineering"
category: "talks"
date: "2026-06-29"
time: "11:40am-12:00pm"
track: "Forward Deployed Engineering"
room: "Track 8"
speakers: ["Vasuman Moza"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Forward Deployed Engineering"
scheduleRoom: "Track 8"
scheduleLabels: ["Forward Deployed Engineering", "Track 8", "session", "confirmed"]
---
# AI tools for Forward Deployed Engineering

## Conference Context
- Date/time: 2026-06-29 · 11:40am-12:00pm
- Track/room: Forward Deployed Engineering · Track 8
- Speaker(s): Vasuman Moza
- Session type/status: session · confirmed

- Track: Forward Deployed Engineering
- Room: Track 8
- Session type: session
- Status: confirmed

## Session Description
No official description published in the schedule data.

## Synthesis
### Transcript-Backed Summary
The talk argues that enterprise AI is no longer constrained mainly by execution, because models and harnesses can already complete many tasks; the harder problem is understanding each customer's real business and redesigning work around it. The proposed answer is forward-deployed engineering: embed with customers, map the actual workflow including exceptions and handoffs, then choose an autonomy boundary that keeps adoption high while still creating measurable ROI. The speaker also describes an internal FDE agent with engagement, workflow, and future autonomous stages, backed by dependency graphs, post-trained models, and graph-traversal tools so the team can scale deep customer work without linear headcount growth. The practical consequence is a shift from point-solution AI on top of broken process to department-wide transformation on top of existing systems of record.

### Key Takeaways
- Start by mapping the real workflow, including exception paths and human handoffs, not just the documented golden path.
  - Evidence: "Where when we talk to customers, it's it's a lot of, you know, Sarah in AP handles the workflow today in this way, but when things go wrong, she actually sends it over to Chris, who then takes four days of cycle time to handle reconciliations between a purchase order and an invoice."
- Re-engineer the process around AI instead of bolting AI onto broken steps and expecting production ROI.
  - Evidence: "Um so, what this means is you need forward-deployed engineers to help them re-engineer their current process around AI."
- Choose an autonomy boundary that changes the workflow enough to matter without making the process unfamiliar to users.
  - Evidence: "For example, if they're used to an 11-step workflow and you come in and change that with a one-step, they might be taken aback, the adoption rates might suffer, etc."
- Keep the customer's systems of record in place and build the agent on top of them.
  - Evidence: "So, if you are on a Salesforce or a NetSuite or a Dynamics or an SAP, we will not ask you to migrate off of that."
- Use assistant tooling to absorb documentation churn and client-context questions that otherwise consume FDE time.
  - Evidence: "Are these the same people? Cuz these are the questions that our FDEs are asking all day, every day, and they waste a ton of time just waiting on on Claude to respond."

### Claims From The Talk
- The speaker argues that AI has largely solved execution for knowledge work, so execution is no longer the main bottleneck. (`interpretive`)
  - Evidence: "Um so, in the past in 2024 and around that time, execution work was still the bottleneck. This was before the models gained the intelligence and the harnesses gained the integration abilities that allowed them to move past the execution Um now the AI models are trained to solve the execution of knowledge work."
- He says the remaining bottleneck is understanding a customer's specific business process deeply enough to re-engineer it. (`explicit`)
  - Evidence: "The difference and the bottleneck that is still here is how much can you understand the business?"
- He reports that forward-deployed engineers map real work by embedding with customers and interviewing process leads, including exception handling. (`explicit`)
  - Evidence: "One is they map the way that humans are doing their work today. So, how we do that at Verkada is several forward deployed engineers will be embedded directly with the customer."
- He says AI should be layered onto existing systems of record instead of forcing customers to migrate off them. (`explicit`)
  - Evidence: "They don't have any appetite for that. So, what we believe in Varick believe in at Varick is we'll build the agents on top of your systems of record."
- He says the internal FDE agent is intended to let one engineer or strategist manage more client context without hiring proportionally more people. (`explicit`)
  - Evidence: "So, for example, allowing one forward deployed engineer or forward deployed strategist to manage and maintain several client communications."
- He argues the desired outcome is department-wide transformation and higher ROI, not small point solutions. (`interpretive`)
  - Evidence: "If you're just doing AP and no other part of your department, you might have a 5 10% ROI. But, at Verek we deliver department-wide transformations, holistically transforming the entire department at a time."

### Topics Covered
- [[software-factories|Forward-deployed engineering]] — The operating model where engineers are embedded with customers to understand and reshape real business processes.
- [[software-factories|Enterprise process mapping]] — The act of tracing how work really happens, including exceptions, handoffs, and failure recovery.
- [[software-factories|Human-in-the-loop automation]] — The practice of dividing work into autonomous, assisted, and human-only steps to make AI adoption workable.
- [[agent-memory|Systems of record]] — The enterprise systems that record core business state and should remain in place during AI adoption.
- **Dependency graphs** — A representation of workflow dependencies used to model enterprise processes and constraints.
- [[agentic-search|Knowledge graph traversal]] — The problem of finding the right contextual facts inside a large company knowledge graph.

### Tools And Named Systems
- [[claude|Claude]] — The external model used as a comparison point for faster client analysis and workflow support.
- [[codex|Codex]] — The external coding assistant named alongside Claude in the platform discussion.
- **Varick OS** — The internal platform used to spin up and monitor agents with governance and evals.
- **NetSuite** — One of the systems of record the speaker says customers are already committed to.
- **Salesforce** — One of the enterprise systems the speaker says the agent should sit on top of.
- **SAP** — One of the enterprise systems the speaker says the agent should sit on top of.
- **Dynamics** — One of the enterprise systems the speaker says the agent should sit on top of.
- **Kimiko 26** — The open-source model family the speaker says they post-train for a better balance of detail and clarity.

### Novel Concepts And Methods
- **Embedded customer discovery** — Embed engineers with the customer and interview process owners to map the real workflow before changing it.
- **Workflow re-engineering** — Redesign the workflow around AI instead of bolting AI onto a broken process.
- **Autonomy tiering** — Split each process into autonomous, human-in-the-loop, and human-only steps to balance adoption and ROI.
- **Top-of-stack deployment** — Layer agents on top of systems of record rather than requiring a platform migration.
- **FDE assistant layering** — Use an internal FDE assistant to handle document synthesis, slide reading, and client-context questions.
- **Dependency-graph modeling** — Represent the company process as a dependency graph so workflows stay dependency-driven and easier to reason about.

### Open Questions
- **How can an autonomous FDE assistant safely receive client change requests and update a workflow without human involvement?** — This is the missing step between assistant support and full automation.
- **How can a model reliably traverse a large enterprise knowledge graph and extract the right context instead of the wrong nearby context?** — The talk treats context retrieval as a core technical bottleneck.
- **Where is the right boundary between autonomous steps, human-in-the-loop steps, and human-only steps for a given enterprise workflow?** — The speaker says adoption and ROI depend on choosing that boundary well.

### Derived Links And Source Material
- [[youtube-l0FLhNqBOic-transcript]] — dedicated official recording transcript.
- [[youtube-l0FLhNqBOic]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/l0FLhNqBOic--2026-06-29-vasuman-moza-ai-tools-for-forward-deployed-engineering.json`.

### Speaker Context
- [[vasuman-moza|Vasuman Moza]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[vasuman-moza]]

## Official YouTube Recording
- [[youtube-l0FLhNqBOic|AI tools for Forward Deployed Engineering — Vasuman Moza, Varick Agents]] — official AI Engineer YouTube recording published 2026-07-28.
- Evidence status: [[youtube-l0FLhNqBOic-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-l0FLhNqBOic]] - dedicated official event recording.
- [[youtube-l0FLhNqBOic-transcript]] - dedicated official recording transcript.

- Source video: `youtube-l0FLhNqBOic`
- Slide deck: [[youtube-l0FLhNqBOic-slides|Slides: AI tools for Forward Deployed Engineering — Vasuman Moza, Varick Agents]] — 12 visible slide image(s).
![[assets/slides/l0FLhNqBOic/slide-001.jpg]]
![[assets/slides/l0FLhNqBOic/slide-002.jpg]]
![[assets/slides/l0FLhNqBOic/slide-003.jpg]]
- Slide-derived themes for `youtube-l0FLhNqBOic`: engineering, track, june, forward, deployed, microsoft, next, bottleneck.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/l0FLhNqBOic.txt` (3,881 words).

## Transcript Markdown
- [[youtube-l0FLhNqBOic-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/l0FLhNqBOic.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-l0FLhNqBOic` — 3,881 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-l0FLhNqBOic`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-l0FLhNqBOic`: process, today, company, forward, deployed, context, around, clients.
- Slide-derived themes for `youtube-l0FLhNqBOic`: engineering, track, june, forward, deployed, microsoft, next, bottleneck.
- Evidence links for `youtube-l0FLhNqBOic` (primary event evidence): [[youtube-l0FLhNqBOic]], [[youtube-l0FLhNqBOic-transcript]], [[youtube-l0FLhNqBOic-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
