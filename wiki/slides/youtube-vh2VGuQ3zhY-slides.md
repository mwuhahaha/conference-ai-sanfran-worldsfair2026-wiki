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

> WHYITFAILS Accuracy Collapses With Scale
> Ankush Rastogi
> 78% 40% 13%
> Accuracy at 10 tools Accuracyat100tools Accuracyat741tools
> Tool SelectionAccuracy (%)vs.Tool-Pool Size Sohal Shaikh
> BO
> 100 200
> FatAgent(alltools) WithSemanticRouter
> 04
> Ankush Rastogi

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

> RESULTS
> BenchmarkResults
> Ankush Rastogi
> Accuracy(%)vs.Tool Count TTFT(ms)vs.ToolCount@GPT-40
> 100- 7000
> 80 6000
> 5000
> 60 4000
> 40 3000 Sohal Shaikh
> 2000
> 20 1000
> 10 50 100 200 741 10 100 200 400 741
> Baseline (fat agent) With Router Baseline (fatagent) With Router
> 10
> Ankush Rastogi

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

> GO DEEPER
> Resources& References
> Ankush Rastogi
> 三 Papers& Benchmarks Tools&Repos APIDoCS
> Zhengetal.-SkillRouter:LLM AgentsatScale(2026).SkilliRouter- github.com/alibaba/skillrouter AnthropicMCP docs.anthropic.com/mcp
> Liu&Chen-SemanticTool Selection(vLLM,2025) FAISS- github.com/facebookresearch/faiss OpenAl Function Calling- platform.openai.com Sohal Shaikh
> Berkeley Function Calling Leaderboard (BFCL) Pinecone/Qdrant/ChromaDB (vectorDBs) GoogleGenAIGemini 2.0- ai.google.dev
> AnthropicEng.-MCPOn-Demand Context(2025) LangGraph-agentorchestration SentenceTransformers-sbert.net
> Thankyou!
> 19

![[assets/slides/vh2VGuQ3zhY/slide-013.jpg]]

OCR text:

> LET'SCONNECT
> ThankYou AnkushRastogi
> Scan either code to connectwith uson Linkedln
> Sohai Shuikh
> Ankush Rastogi Sohail Shaikh
> SeniorData SolutionsEngineer·Prosodica LLC DataScientist·ProsodicaLLC
> 20

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
