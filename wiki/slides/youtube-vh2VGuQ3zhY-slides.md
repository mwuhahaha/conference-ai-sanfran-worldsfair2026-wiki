---
title: "Slides: The 100-Tool Agent Is a Trap - Sohail Shaikh & Ankush Rastogi, Prosodica"
category: "slides"
video_id: "vh2VGuQ3zhY"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: The 100-Tool Agent Is a Trap - Sohail Shaikh & Ankush Rastogi, Prosodica

## Source Video
[The 100-Tool Agent Is a Trap - Sohail Shaikh & Ankush Rastogi, Prosodica](https://www.youtube.com/watch?v=vh2VGuQ3zhY)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/vh2VGuQ3zhY/slide-001.jpg]]

OCR text:

> Ankush Rastogi
> The 100-Tool Agent
> Is a Trap
> Sohall Shaikh
> Scaling with SemanticRouters and Just-In-Time Context
> Al EngineerWorld'sFair2026
> For Engineers BuildingLLM Agents
> Ankush Rastogi

![[assets/slides/vh2VGuQ3zhY/slide-002.jpg]]

OCR text:

> THEPRESENTERS
> Ankush Rastogi
> Ankush Rastogi
> Sohail Shaikh
> Sohal Shaikh
> SeniorData Solutions Engineer.Prosodica LLC
> DataScientist·Prosodica LLC
> IEEESeniorMember
> BuildingReal-WorldAl Systems
> 10+yearsacrossdataengineering,lsystemsproduction
> 9+yearsinAlLP,conversationalintelligence,AGpipeines
> analytics,andenterprise LLMimplementation.
> semanticsearch,andproductionLLMworkflows.
> Ankush Rastogi

![[assets/slides/vh2VGuQ3zhY/slide-003.jpg]]

OCR text:

> eae”
> Pat
> THE PROBLEM ret)
> 7 ed -
> The Fat Agent Trap
> The Natve Architecture
> Cs
> |] how
> Token Bloat °. oa , ag
> AccuracyCrash - + an rs
> [eekia a telrestlola) ; fu REY y F
> Context Crowding °. me ;

![[assets/slides/vh2VGuQ3zhY/slide-004.jpg]]

OCR text:

> WHY IT FAILS it
> Accuracy Collapses With Scale
> ee Se
> Tool Selection Accuracy (°%e} vs. Too! Pool Size ’

![[assets/slides/vh2VGuQ3zhY/slide-005.jpg]]

OCR text:

> THETECHNIQUE
> Just-ln-Time Context Injection
> Ankush Rastogi
> StaticLoading
> JIT Injection
> All100+schemaspre-loaded in theprompt
> Toolsselectedatruntime,perquery
> Everyrequestcarriesthefullpayload
> Only3-5relevant schemasinjected
> ·Most tokenswastedonirrelevanttools
> Contextwindow stayslean
> Contextwindowconsumedbyschemas
> VS
> Moreroomforreasoningchains
> Sohal Shaikh
> Lessspaceforreasoningandoutput
> Accuracy staysabove83%at any scale
> Accuracy degradesasthelistgrows
> Fast:smallerprompt,lessprocessing
> Slow:model mustprocessagiant context
> InspiredbyAnthropicMCPon-demand loading
> Ankush Rastog

![[assets/slides/vh2VGuQ3zhY/slide-006.jpg]]

OCR text:

> practel aS it
> ; — ae
> Benchmark Results
> Per eet
> Accuracy (%) vs. Tool Count TTFT (ms) vs. Too! Count @ GPT4o
> a ee
> ee ‘ee
> | bon
> = ff
> oe
> od co
> Pn ete

![[assets/slides/vh2VGuQ3zhY/slide-007.jpg]]

OCR text:

> HOW TO BUILD IT it
> 3 Step Implementation Pattern
> Build Tool Index 7 Route Each Query on Inject & Call LLM
> a | ee ‘ia :

![[assets/slides/vh2VGuQ3zhY/slide-008.jpg]]

OCR text:

> eaters a at)
> . P — ‘ie
> Implementation Checklist
> Catalog Your Tools ., Build the Embedding Index
> + , |
> ; Implement the Router Integrate into the Agent Loop
> 7 Evaluate & Tune K 7 Monitor & Iterate

![[assets/slides/vh2VGuQ3zhY/slide-009.jpg]]

OCR text:

> P= ae
> INDUSTRY EVIDENCE it.
> an p |
> Teams Are Hitting the Same Tool-Scaling Wall
> Cee cea Anthropic Engineering Blog eee SOK «Issue
> - : S ? ma a
> ee A |
> MCP-Zcro (xfey/MCP-Zero) n8n Community Forum
> Eo

![[assets/slides/vh2VGuQ3zhY/slide-010.jpg]]

OCR text:

> KNOW THELIMITS
> Trade-Offs&BestPractices
> Ankush Rastogi
> CONCERN
> MITIGATION
> Router maymiss a needed tool
> Fallback:raiseK,or let theLLMrequestmore
> Adds complexity:vector DB+tuning
> Embedding search is ms-fast; the savings dominate
> Sohail Shuikh
> Raretoolsmayranklow
> Logmisses;retrain oraddkeyword boosting
> Kthresholdishard to calibrate
> Start atK=5;tune on a dev eval set
> Notworthitbelow~20 tools
> For smalltoolsets,load statically;norouter
> Ankush Rastogi

![[assets/slides/vh2VGuQ3zhY/slide-011.jpg]]

OCR text:

> a!
> REMEMBER THIS it,
> oo eee —_
> Key Takeaways
> — Too! Overload Kills Accuracy ye ne -
> - o #6 2 fe a 7 , ‘
> “s Tokens = Money + Latency oe _ ] Mg ; a
> aan Semantic Routing Saves the Day | _ , , oe
> ‘It's RAG, but for Tools ee a en
> a Tele scTarl Mestre Otel talib rs - ,

![[assets/slides/vh2VGuQ3zhY/slide-012.jpg]]

OCR text:

> GO DEEPER it
> Resources & References .
> aw] Kasia Ss a fetel mM <:] elel-} = API Docs
> Thank you!

![[assets/slides/vh2VGuQ3zhY/slide-013.jpg]]

OCR text:

> | (|
> LET'S CONNECT ft oot
> Thank You _
> 
> a
> 
> Ceo ee etl
> 
> ees ne
> 
> San fale Syn
> 
> Ankush Rastogi Sohail Shaikh

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
