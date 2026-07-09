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

> THE PRESENTERS
> Ankush Rastogi
> Senior Data Solutions Engineer · Prosodica LLC
> IEEE Senior Member
> 10+ years across data engineering, AI systems, production
> analytics, and enterprise LLM implementation.
> Sohail Shaikh
> Data Scientist · Prosodica LLC
> Building Real-World AI Systems
> 9+ years in AI, NLP, conversational intelligence, RAG pipelines,
> semantic search, and production LLM workflows.
> 02

![[assets/slides/vh2VGuQ3zhY/slide-003.jpg]]

OCR text:

> THE PROBLEM
> The Fat Agent Trap
> The Naive Architecture
> The easiest approach is to dump every tool's schema into the prompt on every request. It works perfectly in demos and falls apart in production.
> Token Bloat 127,000 tokens for 741 tools
> Accuracy Crash 78% → 13% as the tool pool grows
> Cost Explosion Up to 99x more tokens billed
> Context Crowding No room left for actual reasoning
> EVERY SINGLE REQUEST
> User Query
> LLM + ALL 100+ Tool Schemas
> T1 T2 T3 T4 T5
> T6 T7 T8 T9 T10
> T11 T12... T100 + 85 more
> Every token, every request is billed and processed in full.
> 03

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

> THE TECHNIQUE
> Just-In-Time Context Injection
> Static Loading
> • All 100+ schemas pre-loaded in the prompt
> • Every request carries the full payload
> • Most tokens wasted on irrelevant tools
> • Context window consumed by schemas
> • Less space for reasoning and output
> • Accuracy degrades as the list grows
> • Slow: model must process a giant context
> VS
> JIT Injection
> • Tools selected at runtime, per query
> • Only 3-5 relevant schemas injected
> • Context window stays lean
> • More room for reasoning chains
> • Accuracy stays above 83% at any scale
> • Fast: smaller prompt, less processing
> • Inspired by Anthropic MCP on-demand loading
> Ankush Rastogi
> Sohal Shaikh
> 08

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

> HOW TO BUILD IT
> 3 Step Implementation Pattern
> 1 Build Tool Index
> OFFLINE • ONE-TIME
> • Collect all tool names,
> descriptions, and JSON schemas
> • Embed each tool description
> (OpenAI, Cohere,
> SentenceTransformers)
> • Index once and reuse forever by
> storing vectors in FAISS or
> Pinecone.
> 2 Route Each Query
> RUNTIME • EVERY REQUEST
> • Embed the incoming user query
> with the same model
> • Run approximate
> nearest-neighbor search against
> the tool index
> • Retrieve top-K tools (K = 5
> default); apply a cosine threshold
> 3 Inject & Call LLM
> RUNTIME • EVERY REQUEST
> • Fetch JSON schemas for the
> selected tools only
> • Build the prompt with just those
> schemas in the tools parameter
> • Call the LLM → return result; log
> selections for monitoring
> 11

![[assets/slides/vh2VGuQ3zhY/slide-008.jpg]]

OCR text:

> YOUR ROADMAP
> Implementation Checklist
> 1 Catalog Your Tools
> Gather all tool names, descriptions, and JSON schemas in a structured list
> 2 Build the Embedding Index
> Embed each description; store vectors in FAISS or Pinecone; one-time setup
> 3 Implement the Router
> embed(query) → similarity_search → top-K → fetch schemas
> 4 Integrate Into the Agent Loop
> Replace your static functions list with the router output on every call
> 5 Evaluate & Tune K
> Benchmark accuracy at K = 3, 5, 10 on a held-out set; pick the sweet spot
> 6 Monitor & Iterate
> Log selections; alert on missed tools; re-embed as your catalog grows
> Ankush Rastogi
> Sohail Shaikh
> 14

![[assets/slides/vh2VGuQ3zhY/slide-009.jpg]]

OCR text:

> INDUSTRY EVIDENCE
> Teams Are Hitting the Same Tool-Scaling Wall
> Real evidence from practitioners, engineers, and Anthropic itself, not simulated benchmarks.
> 150K → 2K
> Anthropic Engineering Blog
> Loading only the tools needed for the current task drops usage from 150,000 to 2,000 with 98.7% cut.
> Official Anthropic finding
> 20+
> tools breaks it
> Vercel AI SDK - Issue #11920
> "Sending all tool definitions every request degrades performance, confuses tool choice, and raises tokens + latency."
> Real practitioner issue - Jan 2026
> 98%
> token reduction
> MCP-Zero (xfey/MCP-Zero)
> Tested on 308 MCP servers and 2,797 tools.
> Selects accurately from ~3K candidates while cutting tokens 98%.
> Open source, code available now
> > 2
> tools → stuck loop
> n8n Community Forum
> "Add more than two tools and the AI gets stuck in a loop, burning through all max iterations." Hit in production.
> Production failure - Aug 2024
> 15

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
