---
title: "Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub"
category: "talks"
date: "2026-06-29"
time: "1:30pm-1:50pm"
track: "AI Architects: Show my Workflow"
room: "Leadership 2"
speakers: ["Arek Borucki"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "AI Architects: Show my Workflow"
scheduleRoom: "Leadership 2"
scheduleLabels: ["AI Architects: Show my Workflow", "Leadership 2", "session", "confirmed"]
---
# Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub

## Conference Context
- Date/time: 2026-06-29 · 1:30pm-1:50pm
- Track/room: AI Architects: Show my Workflow · Leadership 2
- Speaker(s): Arek Borucki
- Session type/status: session · confirmed

- Track: AI Architects: Show my Workflow
- Room: Leadership 2
- Session type: session
- Status: confirmed

## Session Description
Hugging Face hosts over 2 million public models, 500,000+ datasets, and serves 13 million users across 50,000+ organizations, including over 30% of the Fortune 500. That growth didn't come with a manual.In this talk, we'll pull back the curtain on the infrastructure decisions that kept the Hub fast and reliable as traffic grew by orders of magnitude. We'll dive into why we chose MongoDB Atlas as our core data layer, how its document model maps naturally to the messy reality of ML model metadata, and what it took to keep p99 latency low when every request hits a catalog of millions. We'll also cover the trade-offs we faced, the things that broke along the way, and what "lean operations" actually means when your platform serves a third of the Fortune 500. Expect real architecture decisions, real numbers, and lessons you can take back to your own stack.

## Synthesis
### Transcript-Backed Summary
The talk argues that the Hugging Face Hub stays usable at million-model scale by treating metadata search and serving latency as first-order product constraints rather than backend details. Its core mechanism is a layered architecture: metadata lives in MongoDB Atlas, model binaries live separately in object storage, search is driven by precomputed tokens and Atlas Search, and noncritical workloads are pushed onto secondary or hidden nodes. The main tradeoff is that this creates more operational complexity, especially around denormalization, autoscaling, and eventual sharding, but the payoff is simple user behavior at the edge: search, upload, and download keep feeling fast even as the catalog and traffic explode.

### Key Takeaways
- P99 latency is the metric that drives the design choices, so the team optimizes for fast reads, not just average-case performance.
  - Evidence: "P99 is much more important than P50 and we are paying a lots of attention to P99 and that's the reason why we invest in premputee tokens denormalize optimize for read collection in MongoDB full text search based on Apache lucine Kubernetes autoscaling and soon in database sharding."
- Separating metadata from binary artifacts lets the platform scale storage, metadata, and compute independently.
  - Evidence: "This separation of concern let us scale metadata independently from binary storage and compute independently from both."
- The architecture works by keeping the primary focused on the work only it can do and pushing everything else to other machines.
  - Evidence: "The pattern is simple. Primary should focus on what only primary can do. Anything else can be pushed to different machines."
- The platform is designed to scale automatically from low to very high pod counts without manual intervention or routine overprovisioning.
  - Evidence: "Our deployment hub deployment can scale from 10 to 500 bots depends of on the traffic. This is how we keep the hub healthy without manual interventions and without infrastructure overprovisioning."
- The practical goal of all the infrastructure work is to keep the user experience simple even when the backend is complex.
  - Evidence: "This is what scaling medium models is really about. Keeping the user experience simple no matter how complex it gets under the hood."

### Claims From The Talk
- Hugging Face says it hosts 3 million public models, 1 million datasets, and 50,000 organizations. (`explicit`)
  - Evidence: "We host three million public models, 1 million data sets, 50,000 organizations, and not only hobbyists or scientists."
- The speaker says more than 30% of the Fortune 500 use Hugging Face as part of their AI workflows. (`explicit`)
  - Evidence: "More than 30% of Fortune 500 use hugging face as a part of AI workflows. Just to give you some perspective, few years ago we had 20,000 models."
- Model artifacts, tokenizer files, card assets, and configuration files are stored separately in cloud object storage such as AWS S3. (`explicit`)
  - Evidence: "The actual models artifacts, tokenizer files, cart assets and configuration files are stored separately in cloud object storage such as AWSS3."
- The team switched from regex-based search to Atlas Search because the earlier approach did not scale well as the catalog grew. (`explicit`)
  - Evidence: "So we decided to switch to Atlas search that's a feature which is using Apache lucine under the hood."
- The operational rule is that the primary should focus on what only the primary can do, and everything else should be pushed to other machines. (`explicit`)
  - Evidence: "The pattern is simple. Primary should focus on what only primary can do. Anything else can be pushed to different machines."
- The team plans to move from HPA to KEDA so scaling can respond to real application metrics instead of only CPU and memory. (`explicit`)
  - Evidence: "The difference HPA scale only based on CPU and memory. KDA scale on real application metrics like request per second or event loop utilization."

### Topics Covered
- [[agentic-search|Search latency at catalog scale]] — How slow search at multi-million-item scale becomes a user-facing product problem.
- **Metadata and artifact separation** — The pattern of storing metadata separately from binary artifacts so each can scale independently.
- **Read-optimized collections** — A separate denormalized collection optimized for read-heavy search and listing traffic.
- [[forward-deployed-engineering|Replica-set workload partitioning]] — The rule that primaries handle only the work that requires primaries, while everything else is offloaded.
- [[platform-context-and-collaboration|Database sharding]] — The move from a single replica set toward horizontally partitioned database growth.
- **Layered autoscaling** — Scaling pods and nodes together instead of relying on one autoscaling layer.

### Tools And Named Systems
- **MongoDB Atlas** — The core managed database layer for Hub metadata.
- **Atlas Search** — The full-text search layer used for model lookup and autocomplete.
- **Apache Lucene** — The search engine used under the hood by Atlas Search.
- [[kubernetes|Kubernetes]] — The container orchestration platform running the Hub services.
- **Horizontal Pod Autoscaler** — The deployment-level autoscaling mechanism currently in use.
- **Cast AI** — The infrastructure autoscaling layer used when Kubernetes lacks capacity.
- **AWS S3** — The object storage system used for model artifacts and related files.
- **KEDA** — The planned workload-driven autoscaling system.

### Novel Concepts And Methods
- **Precomputed search tokens** — Precompute search tokens at insert time so lookup work happens during ingest rather than at query time.
- **Read-optimized denormalization** — Maintain a denormalized read collection for search and listing traffic instead of querying the main repository collection directly.
- **Replica workload partitioning** — Route non-latest, aggregation-heavy, reporting, and ad hoc workloads away from the primary onto secondaries or hidden replica members.
- **Layered autoscaling** — Use a two-layer scaling setup where pod autoscaling handles deployment load and node autoscaling adds infrastructure capacity when needed.
- **Horizontal sharding** — Scale the database horizontally with sharding once a single replica set can no longer hold the full workload.

### Open Questions
- **What shard key should be chosen to preserve query performance and balance the hub's growing catalog?** — The speaker says shard-key selection is not trivial, and the choice will shape whether sharding actually fixes the scaling bottleneck.
- **How much better will KEDA perform than HPA for mixed search and download traffic that spikes on real workload signals rather than just CPU or memory?** — The talk identifies a migration path but leaves open whether request-driven scaling materially improves user-facing latency and capacity efficiency.

### Derived Links And Source Material
- [[youtube-lyL5QhgIOxc-transcript]] — dedicated official recording transcript.
- [[youtube-lyL5QhgIOxc]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/lyL5QhgIOxc--2026-06-29-arek-borucki-serving-2-million-models-without-melting-scaling-the-hugging-face-hub.json`.

### Speaker Context
- [[arek-borucki|Arek Borucki]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[arek-borucki]]

## Official YouTube Recording
- [[youtube-lyL5QhgIOxc|Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub — Arek Borucki, Hugging Face]] — official AI Engineer YouTube recording published 2026-07-28.
- Evidence status: [[youtube-lyL5QhgIOxc-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-lyL5QhgIOxc]] - dedicated official event recording.
- [[youtube-lyL5QhgIOxc-transcript]] - dedicated official recording transcript.

- Source video: `youtube-lyL5QhgIOxc`
- Slide deck: [[youtube-lyL5QhgIOxc-slides|Slides: Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub — Arek Borucki, Hugging Face]] — 5 visible slide image(s).
![[assets/slides/lyL5QhgIOxc/slide-001.jpg]]
![[assets/slides/lyL5QhgIOxc/slide-002.jpg]]
![[assets/slides/lyL5QhgIOxc/slide-003.jpg]]
- Slide-derived themes for `youtube-lyL5QhgIOxc`: serving, million, models, hugging, face, scaled, largest, model.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/lyL5QhgIOxc.txt` (1,945 words).

## Transcript Markdown
- [[youtube-lyL5QhgIOxc-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/lyL5QhgIOxc.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-lyL5QhgIOxc` — 1,945 transcript words; 4 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-lyL5QhgIOxc`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-lyL5QhgIOxc`: data, search, mongodb, models, scale, million, model, hugging.
- Slide-derived themes for `youtube-lyL5QhgIOxc`: serving, million, models, hugging, face, scaled, largest, model.
- Evidence links for `youtube-lyL5QhgIOxc` (primary event evidence): [[youtube-lyL5QhgIOxc]], [[youtube-lyL5QhgIOxc-transcript]], [[youtube-lyL5QhgIOxc-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
