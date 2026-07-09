---
title: "Slides: Production Evals For Agentic AI Systems - Nishant Gupta, Meta Superintelligence Labs"
category: "slides"
video_id: "vljxQZfJ9wY"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: Production Evals For Agentic AI Systems - Nishant Gupta, Meta Superintelligence Labs

## Source Video
[Production Evals For Agentic AI Systems - Nishant Gupta, Meta Superintelligence Labs](https://www.youtube.com/watch?v=vljxQZfJ9wY)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/vljxQZfJ9wY/slide-001.jpg]]

OCR text:

> ee
> \ Oo o ° [GZ
> ProductionEvals = {23> / (te
> e N “ “LOIN TE | | a i
> for Agentic Systems |\_ \- & Vie —o
> nee) <n
> <4 (NS ey
> Measuring reliability beyond Ph OY Ne —o pe
> accuracy. Building evaluation systems 9 [2° 7 LY | KS
> for autonomous Al workflows. 4 f 4 Ady to d w
> Nishant Gupta f ——_~
> Tech Lead @ Meta

![[assets/slides/vljxQZfJ9wY/slide-002.jpg]]

OCR text:

> <q
> AI systems evolved faster than |
> our evaluation methods
> The Illusion The Reality
> “
> yp ok Rh Modes
> Behavior
> ~—_ ox
> Unpredictable User
> (si
> 90% 25%
> Benchmark Accuracy ox . eu
> T-O T+10ms T+50ms T+100ms

![[assets/slides/vljxQZfJ9wY/slide-003.jpg]]

OCR text:

> The Paradigm Shift: Output vs. Behavior
> Traditional LLM Evaluation Agent Evaluation
> Goal Output Accuracy > Workflow Behavior
> Environment Static Datasets > Dynamic Contexts
> |
> Execution Single-path Processing | > Multi-path & Tool Dependent
> I
> Failure Mode | Hallucination > ascading Workflow Failure

![[assets/slides/vljxQZfJ9wY/slide-004.jpg]]

OCR text:

> Think like an SRE: Accuracy gives way to Reliab
> Task Success
> Satisfaction Human Tool Success
> Accuracy Safety Reliability System Planning Quality
> Cost Latency

![[assets/slides/vljxQZfJ9wY/slide-005.jpg]]

OCR text:

> e ® e , 4 “
> The Evaluation Signal Hierarchy
> Production Telemetry
> | Low volume, maximum t
> signal value.
> Scenario Evals Operational
> Volume argeted workflows | Value
> Benchmarks
> High volume, low operational value.
> The foundation, not the destination.

![[assets/slides/vljxQZfJ9wY/slide-006.jpg]]

OCR text:

> Offline Evals: Scenario-Driven Simulation
> 
> ee
> ' fl
> ! Agent Sandbox Discrete Outputs
> ; _
> : Tools tC Steps update i Completion Rate 98.5%
> 
> : ¢ ; Tool Correctness 106%
> ' Plan Quality High
> FEE SO AS ESR i EB OO Ma Ol Bag! Simulated Cost $0.65
> 
> Scenario-driven, not prompt-driven.

![[assets/slides/vljxQZfJ9wY/slide-007.jpg]]

OCR text:

> , i”
> Online Evals: The Production Stream
> User S = ~— :
> Interactions 2 _ Gateway .
> a Gy Go , — ” Metadata & Telemetry
> =5 — )
> Analytics
> Ls Oatabase
> Sd
> | Production is your largest evaluation dataset.
> Every interaction is signal.

![[assets/slides/vljxQZfJ9wY/slide-008.jpg]]

OCR text:

> ~
> i
> Human-in-the-Loop Calibration
> Review Node fA fA
> Automated ih “Oo. ee
> Alert . i i >.
> “ . S ! Correctness Usefulness
> | |
> « a i
> : - a
> Trust Safety
> Humans are evaluators, not merely fallback systems.

![[assets/slides/vljxQZfJ9wY/slide-009.jpg]]

OCR text:

> Observability is thePrerequisite
> The TraceWaterfall LiveMetricsDashboard
> UserPrompt(35m-70ms) Latency 345ms
> PlannerIteration(7mm-35ms) VectorDBLookup-8ms) Retries 2.5%
> ParallelAPlToolCalls APIA-45ms APIB-38ms $0.014 StepCosts
> APIC-52ms Memory Usage 480MB
> 20ms 30ms 45ms 50ms 90ms 10ns 11ms 12ms 13ns
> TTOH
> "You cannot evaluate what you cannot observe."

![[assets/slides/vljxQZfJ9wY/slide-010.jpg]]

OCR text:

> The Continuous Evaluation Loop
> A Online Telemetry detects drift/errors
> Evaluationisan
> validate system updates Offline Scenario Evals before pushing back to Production D always-running testing phase. service,nota B for edge cases Triggers HITL review
> C Human feedback feeds into Offline Datasets

![[assets/slides/vljxQZfJ9wY/slide-011.jpg]]

OCR text:

> The Agentic Control Plane |
> Reference Architecture
> 
> Control Plane
> 
> : Scenario
> Tracing & Telemetry : HITL
> Gia
> LLM Agent External
> Orchestrator Tools
> Execution Plane

![[assets/slides/vljxQZfJ9wY/slide-012.jpg]]

OCR text:

> Architectural Imperatives
> 1. Offline benchmarks are necessary but insufficient.
> 2. Agentic systems must be evaluated as full workflows.
> 3. Production telemetry is the ultimate evaluation signal.
> 4. Reliability always supersedes raw model accuracy.
> 5. Evals are no longer tests; they are core infrastructure.
> “You can’t improve what you don’t continuously evaluate.”

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
