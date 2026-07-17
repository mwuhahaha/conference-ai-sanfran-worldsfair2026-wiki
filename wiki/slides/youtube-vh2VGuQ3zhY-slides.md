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
![[assets/slides/vh2VGuQ3zhY/slide-007.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/vh2VGuQ3zhY/slide-007.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/border-trim/contrast`.
- OCR decision: ready — Dense multi-card slide with small bullet text and mixed layout.

Slide text:

> HOWTO BUILD IT
> 3 Step Implementation Pattern
> Ankush Rastogi
> Build Tool Index Route Each Query Inject & Call LLM
> OFFLINE·ONE-TIME RUNTIME·EVERYREQUEST RUNTIME·EVERYREQUEST
> Collect all tool names, descriptions,and JsON schemas Embed the incominguser query with thesamemodel Fetch JsON schemas for the selected tools only
> Index once and reuse forever by Embed each tool description SentenceTransformers) Pinecone. storingvectors in FAisS or (OpenAl,Cohere, Run approximate Retrieve top-Ktools（K=5 the toolindex nearest-neighbor search against default); apply a cosine threshold Build thepromptwith just those Call the LLM → return result; log selections for monitoring schemas in the toolsparameter Sohaa Shukh
> Antush Rastogi

![[assets/slides/vh2VGuQ3zhY/slide-008.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/vh2VGuQ3zhY/slide-008.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/border-trim/contrast`.
- OCR decision: ready — Six-item checklist with smaller subtext across two columns.

Slide text:

> YOURROADMAP
> Implementation Checklist
> Ankush Rastogi
> Catalog Your Tools Build the Embedding Index
> Gather alltoolnames,descriptions,and JsON schemasina structured list Pinecone,one-time setup Embed each description, store vectors in FAiss or
> Implement the Router Integrate Into the Agent Loop
> schemas embed(query)→similarity_search→top-K→fetch Replace your static functions list with therouter output on every call Sohaa Shakh
> 5 Benchmark accuracy at K=3,5,10on a held-out set; pickthe sweet spot Evaluate & Tune K 6 your catalog grows Monitor & Iterate Log selections;alert on missed tools;re-embed as
> 14
> Antush Rastogi

![[assets/slides/vh2VGuQ3zhY/slide-009.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/vh2VGuQ3zhY/slide-009.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast`.
- OCR decision: ready — Dense evidence matrix with multiple source callouts and small supporting copy.

Slide text:

> Teams Are Hitting the Same Tool-Scaling Wall INDUSTRYEVIDENCE
> Real evidence from practitioners,engineers,and Anthropic itself,not simulated benchmarks. Ankush Rastogi
> tokens 150K → 2K Loading only the toolsneeded for the Anthropic Engineering Blog currenttaskdropsusagefrom1so.oooto 2,000 with98.7%cut. 20+ tools breaksit Vercel AI SDK - Issue #11920 Sending alltool definitions every request choice,and ralses tokers+latency." degrades performance,confuses tool
> Official Anthropicfinding Real practitioner issue jon 2026
> Sohnl Shakh
> 98% tokenreduction Selects accurately from~3K candidates MCP-Zero (xfey/MCP-Zero) whilecutting tokens 98% Testedon308MCPserversand2.797toob. >2 tools-+stuckloop stuckin aloop,burningthroughallmax iterations.Hit in production. n8n Community Forum "Addmorethan two toolsandtheAlgets
> Open source,code cvailable now Production foslure·Aug 2024
> 15
> boseysruy

![[assets/slides/vh2VGuQ3zhY/slide-010.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/vh2VGuQ3zhY/slide-010.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/border-trim/opencv-adaptive`.
- OCR decision: ready — Two-column tradeoff table with five rows of small text.

Slide text:

> KNOWTHE LMITS Trade-Offs & Best Practices
> Ankush Rrsi ogi
> CONCERN MITIGATION!
> Router may miss a needed tool Fallback: raise K, or let the LLM request more:
> Adds complexity:vector DB+tuning Embedding search is.ms-fast; the savings dominate:
> Rare toois may rank low E Log missesy retrain or add keyword boosting
> K threshold is hard to calibrate Start at K=5; tune on a dev eval set.
> Not worth it below -20 tools For small tool sets' load staticallypano router
> Anbunh Rrtogi

![[assets/slides/vh2VGuQ3zhY/slide-011.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/vh2VGuQ3zhY/slide-011.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: agent_vision.

Slide text:

> Key Takeaways
> 01 Tool Overload Kills Accuracy
> 02 Tokens = Money + Latency
> 03 Semantic Routing Saves the Day
> 04 It's RAG, but for Tools
> 05 Start Small, Scale Confidently

![[assets/slides/vh2VGuQ3zhY/slide-012.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/vh2VGuQ3zhY/slide-012.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast`.
- OCR decision: ready — Dense reference slide with small multi-column text and many citations.

Slide text:

> GO DEEPER
> Resources & References
> Ankush Rstogi
> 三 Benchmarks Papers & Tools & Repos API Docs
> Zheng et al.-SkillRouter:LLM Agents at Scale(2026) SkillRouter- github.com/alibaba/skillrouter AnthropicMCP- docs.anthropic.com/mcp
> Liu&Chen-SemanticTool Selection (vLLM, 2025) FAISS- github.com/facebookresearch/faiss OpenAl Function Calling- platform.openai.com Sohea Shakh
> Berkeley Function Calling Leaderboard (BFCL) Pinecone/Qdrant/ChromaDB (vector DBs) Google GenAI Gemini2.0- ai.google.dev
> Anthropic Eng.-MCP On-Demand Context(2025) LangGraph-agent orchestration SentenceTransformers-sbert.net
> Thank you!
> Antush Rastogi

![[assets/slides/vh2VGuQ3zhY/slide-013.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/vh2VGuQ3zhY/slide-013.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.

Slide text:

> LET'S CONNECT
> Thank You
> Scan either code to connect with us on LinkedIn
> Ankush Rastogi
> Sohail Shaikh

### Hidden Non-Slide Evidence
- [`slide-001.jpg`](/assets/slides/vh2VGuQ3zhY/slide-001.jpg) — `other` confidence `0.0`; missing batch classifier result
- [`slide-002.jpg`](/assets/slides/vh2VGuQ3zhY/slide-002.jpg) — `other` confidence `0.0`; missing batch classifier result
- [`slide-003.jpg`](/assets/slides/vh2VGuQ3zhY/slide-003.jpg) — `other` confidence `0.0`; missing batch classifier result
- [`slide-004.jpg`](/assets/slides/vh2VGuQ3zhY/slide-004.jpg) — `other` confidence `0.0`; missing batch classifier result
- [`slide-005.jpg`](/assets/slides/vh2VGuQ3zhY/slide-005.jpg) — `other` confidence `0.0`; missing batch classifier result
- [`slide-006.jpg`](/assets/slides/vh2VGuQ3zhY/slide-006.jpg) — `other` confidence `0.0`; missing batch classifier result

Classification audit: `raw/sources/slide-ai-classification/slides/vh2VGuQ3zhY/audit.json`

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
