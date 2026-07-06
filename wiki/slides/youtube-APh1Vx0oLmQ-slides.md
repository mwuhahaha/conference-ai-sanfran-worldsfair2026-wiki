---
title: "Slides: Deterministic Infra for Non-Deterministic AI Agents - Nishant Gupta, Meta Superintelligence Labs"
category: "slides"
video_id: "APh1Vx0oLmQ"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: Deterministic Infra for Non-Deterministic AI Agents - Nishant Gupta, Meta Superintelligence Labs

## Source Video
[Deterministic Infra for Non-Deterministic AI Agents - Nishant Gupta, Meta Superintelligence Labs](https://www.youtube.com/watch?v=APh1Vx0oLmQ)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/APh1Vx0oLmQ/slide-001.jpg]]

OCR text:

> BUILDING DETERMINISTIC |
> INFRASTRUCTURE FOR . setmennne ennoase oso
> NON-DETERMINISTIC — .. eaent
> Al AGENTS Seen
> | | We SKE /
> : \ . “eX + RecrificaTion z
> SSS 17...
> Nishant Gupta wea) reeaeeen
> Tech Lead @ Meta _

![[assets/slides/APh1Vx0oLmQ/slide-002.jpg]]

OCR text:

> Infrastructure was built for 2
> predictable microservices.
> THE GREAT MISMATCH
> Traditional sexcrin ous x Autonomous
> Microservices MASSES APE ene Al Agents
> Stateless | —| —_, Stateful
> _ (STATE: 0] ome {STATE: PERSIST]
> Deterministic | a a a Probabilistic
> | [PATH: FIXED] | °° [PATH: DYNAMIC]
> - Request-response ———|> Multi-step workflows
> [FLOW: SYNC] eh (FLOW: ASYNC]
> , (TIME: <1¢0MS) 2 Pee [TIME: >MIN/HR]

![[assets/slides/APh1Vx0oLmQ/slide-003.jpg]]

OCR text:

> Demos optimize for capability. | ad |
> Production demands reliability.
> EE (STRUCTURAL INTEGRITY CRITICAL]
> eo
> a —“» SE _|| Capabilities
> CS ©
> = ____ ge —
> Reliability | Jai? ai
> Core - a ee .
> Citi il cali
> : P eT : ~~ : | Reliability Core
> iat ae an “
> ae <> <—ae
> in, oes
> eae j Ca

![[assets/slides/APh1Vx0oLmQ/slide-004.jpg]]

OCR text:

> s a = e f
> Real production failures originat
> the infrastructure, not the model.
> Diagnostic Failure Tree <7 to .
> . - reasoning loops deadlocks
> re fo
> Model Output . ‘ ““! hallucinations ““) storms “*“I explosions
> , , “" drift poisoning

![[assets/slides/APh1Vx0oLmQ/slide-005.jpg]]

OCR text:

> Ihe anatomy ofan > adil
> y Exponential GPU — g - gases
> t t t Compute Spike
> agent retry storm.
> nf SE
> SSR
> Recursive aL oston
> reasoning loop ,
> .. 1 oo. 10 og we . locks up. we
> ito a : Step 3: Agent SE = |
> Ron erat et eee a attempts to fix vooe | WA Step 5:
> aOe ie eseas| : my a urror but RECURSION IN” oo IMvALio The
> eras caren CEnar COGe. haltucinates new fe PARAMS. g Consequence
> invalid parameter. ie =
> : : g
> Step 1: Agent Step 3: Agent Step 4: : é
> hallucinates Step 2 attempts to fix Recursive 5 Step 5:
> invalid API Tool returns error but reasoning loop x The
> parameters. error code. hallucinates new locks up. Time (ms) " Consequence
> invalid parameter. .
> 7 foe * DATA SPIKE EVENT
> (CRITICAL FAILURE PATH) [TIMELINE AXIS

![[assets/slides/APh1Vx0oLmQ/slide-006.jpg]]

OCR text:

> . 7 Bs
> The platform decides.
> The model merely proposes.
> Validate Y) ©) e Validate G) GS)
> we cs e 7 TSS ” = ? 7 SI '
> Rots Be Secret ES es Be
> J) [Uw TSS Sys |
> ee | IO 2s. Si
> (ANALYSIS: STRUCTURAL INTEGRITY) (Fee: O€TERMINISTIC CONTROL

![[assets/slides/APh1Vx0oLmQ/slide-007.jpg]]

OCR text:

> Logs are dead. Autonomous workflows
> require multidimensional observability.
> 
> Agent Trace Timeline [ Tetemetry Sidebar ]
> Cromoatration on ps ig =
> 
> faite See |
> 
> Execution
> 
> Memory Access on roe.

![[assets/slides/APh1Vx0oLmQ/slide-008.jpg]]

OCR text:

> Shared memory coordinates 7
> chaotic multi-agent consistency
> - Shared Memory Architecture 3 .
> “| State Store :
> va SS = ee a ~ :
> ~*~ DT ~
> we ge FOr
> Context drift _/ “ See F sratememory
> Ud ~ <S ;
> Conflicting facts a . * a!

![[assets/slides/APh1Vx0oLmQ/slide-009.jpg]]

OCR text:

> Human oversight is an escalation path, A: .
> not an operational bottleneck.
> Workflow Routing Diagram
> ; eee OME
> | ; Automated Agent Tasks “KG a ‘7 Automated Agent Tasks ; “
> a ae i a —
> =. 7 a Vou
> Human Approval Node ~t
> 
> (ANALYSIS: ESCALATION PATHWAYS]

![[assets/slides/APh1Vx0oLmQ/slide-010.jpg]]

OCR text:

> Inference at scale fundamentally a.
> becomes a cluster scheduling problem.
> Elastic Scaling Graph
> ‘ - 4 See Long-cunning
> 3 200 5 Fi
> 5 mi Lt EE 2 | Seaview
> | LL Oo
> ~ = Loe nH \a/ A J Bursty Demand
> AeA —|]
> FRC
> ° “— TIME (sec) “e “

![[assets/slides/APh1Vx0oLmQ/slide-011.jpg]]

OCR text:

> r we
> The Reliability Rosetta Stone. mdi
> . Distributed Systems Pattern Agent Equivalent
> Circuit Breakers Tool Isolation .
> 1 {PATTERN TSOLATION] ry t [PATTERN ISOLATION) i
> Rate Limiting Agent Limits
> ; ‘ TUENtt Une cme tee Tf iy C toate £59 ORC OREM) | 1
> Retries : Controlled Recovery
> 1 (MECOWERT LOGIC] iD ' (necovtmy coCreh x
> Quotas Cost Governance
> : Lae SOU e CAPS] a q _ __ _ Ce suet CAPS) k
> Observability Agent Tracing 5
> va (IMACEAMILATY system) | + . Cimacea@icity system) « #
> [ ANALYSIS: RELIABILITY MAPPING ]

![[assets/slides/APh1Vx0oLmQ/slide-012.jpg]]

OCR text:

> Competitive advantage has shifted fron a |
> prompt engineering to systems engineering.
> THE PARADIGM SHIFT
> PROMPTS compound ocean .
> - . . Trajectory L in
> , ea . ir “y “A W
> “ “MODE J .
> 7 on LS . Commoditization * 4 ;
> J Th oe g L
> f me ae ° , Commoctiation
> f Oe oe INFRASTRUCTURE
> - — We

![[assets/slides/APh1Vx0oLmQ/slide-013.jpg]]

OCR text:

> Al agents are distributed systems. meee
> Treat them accordingly. The future
> . ‘ of Al won't
> | ' | be won by
> CORE TAKEAWAYS better
> genio Pane * Firastructue must Besircty. prompts.
> ee poblemtisenmastucure. ff | Itwillbe
> " Mtidmensonlobeenabity s JF won by
> v8 “"-“s Agent contro! planes are the : patter
> : ms required runtime layer for systems. |
> a _ Production Al. 4


## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
