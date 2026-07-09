---
title: "Slides: Your Agent Failed in Prod. Good Luck Reproducing It. - Tisha Chawla & Susheem Koul, Microsoft"
category: "slides"
video_id: "Lc8zRh9muoY"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: Your Agent Failed in Prod. Good Luck Reproducing It. - Tisha Chawla & Susheem Koul, Microsoft

## Source Video
[Your Agent Failed in Prod. Good Luck Reproducing It. - Tisha Chawla & Susheem Koul, Microsoft](https://www.youtube.com/watch?v=Lc8zRh9muoY)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/Lc8zRh9muoY/slide-001.jpg]]

OCR text:

> [ World's Fair |
> Your agent failed in prod.
> good luck reproducing tt.
> a) Tisha Chawla - Susheem Koul - Microsoft

![[assets/slides/Lc8zRh9muoY/slide-002.jpg]]

OCR text:

> asked: sell $12,000
> 
> @

![[assets/slides/Lc8zRh9muoY/slide-003.jpg]]

OCR text:

> asked: sell $1,0o0
> sold:$190,000
> broker·POST/orders→200OK
> order.status FILLED$190,000

![[assets/slides/Lc8zRh9muoY/slide-004.jpg]]

OCR text:

> temperature = O
> 
> 2

![[assets/slides/Lc8zRh9muoY/slide-005.jpg]]
![[assets/slides/Lc8zRh9muoY/slide-006.jpg]]

OCR text:

> 1 sampling determinism # system determinism
> temp 0 fixes the rule (argmax), not the logits you argmax over.
> 2 float addition is NOT associative
> (0.1 + 1e20) - 1e20 = 0 0.1 + (1e20 — 1e20) = 0.1
> reorder a reduction - a logit's last bits move + argmax flips.
> &)

![[assets/slides/Lc8zRh9muoY/slide-007.jpg]]

OCR text:

> 1 sampling determinism # system determinism
> temp 0 fixes the rule (argmax), not the logits you argmax over.
> 2 float addition is NOT associative
> (0.1 + 1e20) ~ 1e20 = 0 0.1 + (1e20 — 1e20) = 0.1
> reorder a reduction - a logit's last bits move + argmax flips.
> 3 the culprit is batch invariance
> same matmul, same GPU, 1000x —. bitwise identical.
> prod batches you with strangers; the kernel depends on batch shape.
> 4 MoE routing jitter: expert capacity ceiling, route depends on the batch.
> same token? no. we need the SYSTEM to run the same
> STATE TRANSITION.
> @

![[assets/slides/Lc8zRh9muoY/slide-008.jpg]]

OCR text:

> X wrong question: can we make the model deterministic.

![[assets/slides/Lc8zRh9muoY/slide-009.jpg]]

OCR text:

> X wrong question: can we make the model deterministic.
> J right question: can we debug & test a run we can't reproduce.
> determinism was never the goal. record the run, replay the recording.
> 
> bitwise determinism replayability
> 
> = controllability = observability
> 
> same input —- identical output. reconstruct a run that happened,
> 
> you won't get it from a hosted API, well enough to debug. you don't
> 
> and you don’t want it: that need determinism, you need -
> 
> tandomness makes the model qaod. the run recorded. =
> 
> a

![[assets/slides/Lc8zRh9muoY/slide-010.jpg]]

OCR text:

> record above the wire, not on tt.
> X at the network layer
> half your agent never touches
> the network: focal retrieval,
> in-process tools, memory.
> the socket can't record
> what isn’t on it.

![[assets/slides/Lc8zRh9muoY/slide-011.jpg]]

OCR text:

> e e
> 
> record above the wire, not on it.
> 
> X at the network layer JY at the boundary
> 
> half your agent never touches capture what enters each node
> 
> the network: local retrieval, and what leaves it, every I/O,
> 
> in-process tools, memory. network or not.
> 
> the socket can't record the meaning of each step,
> 
> what isnt on it. not the packets.
> 
> f 7 3
> 
> tracing records it. replay re-runs it offline: stub the model, O calls. “ha
> Opentnference - Arize Phoenix - LangGraph checkpointers - framework -agnostic

![[assets/slides/Lc8zRh9muoY/slide-012.jpg]]

OCR text:

> ©) ; Pa rr,’
> r
> HE agent replay whiteboard | na a sone (B)
> 2
> Be amie: ese Seas) Pexaet “Canean Sematsey Sale Sin) Review) Sim oe WD Severe Famer 6 Ptr
> $ r
> ®
> .
> ii Live Demo
> ee
> 2
> 2s
> 3 ete
> «
> Bye
> GT

![[assets/slides/Lc8zRh9muoY/slide-013.jpg]]

OCR text:

> MREADME.md
> trade_notional.py
> zsh
> ()002-place_order-1.jsonM
> ()001-agent-1.jsonM
> PreviewREADME
> README.md
> Preview
> Markdown
> @boundary wrapper (LIVE)
> @boundary("place_order",kind="tool")
> annotate once
> INPUT captured
> symbol=ACME quantity=100e side=sell （args-InputState)
> def place_order(symbol:str,quantity:int）->dict:
> notional=quantity*SHARE_PRICE
> return {"status":"filled","notional_cents":notional)
> OUTPUT captured
> {"status":“filled","notional_cents":19000000,...)
> Envelope-store-fixtures/traces/

![[assets/slides/Lc8zRh9muoY/slide-014.jpg]]

OCR text:

> README.md
> trade_notional.pyzsh
> (1002-place_order-1.jsonM
> {1001-agent-1.jsonM
> PreviewREADME
> examples>financial_incidents>trade_notional.py
> USER_MESSAGE="Sell about $1,eeo of ACME from my portfolio to rebalance.
> >def set_mode(mode:str)->None:
> >def_order_input（*args,**kwargs)->InputState:
> @boundary（TooL,kind="tool",extract_input=_order_input)
> def place_order(symbol:str,quantity:int,*，side: str=“sell")->dict[str,Any]:
> @boundary("agent",kind="llm",extract_input=agent_input)
> >def agent_plan(state:dict[str,Any])->dict[str,Any]:
> @boundary("agent",kind="llm",extract_input=agent_input)
> >def agent_finalize(state:dict[str,Any],tool_result:dict[str,Any])-> dict[str,Any]:
> >def run_agent(user_message:str=USER_MESSAGE)->dict[str,Any]:-

![[assets/slides/Lc8zRh9muoY/slide-015.jpg]]

OCR text:

> README.md
> trade_notional.py
> zsh
> (1002-place_order-1.jsonM
> {)001-agent-1.jsonM
> Preview RE
> susheemkoul@Susheems-MacBook-Pro chroniclepython examples/financial_incidents/run.py trade record
> RECoRD trade-notional
> User request
> Sell about $1,ooo of ACME frommy portfolio to rebalance.
> Boundary results
> Node
> KindMode
> Input
> Output
> agent@1
> llm
> LIVE
> Sellabout$1,eeeofACMEfrommyp
> place_order(symbol=ACMEg quantity=1000,side=sell)
> place_order@1
> tool
> LIVE
> symbol=ACME,quantity=1000,side=se
> filled:Sold1ee0ACMEats190.00($190,000.e0total)
> agent@2
> llm
> LIVE
> tool_result:filled
> Done.Sold 1000 ACME at $190.00 ($190,000.00 total)
> Trace exported
> fixtures/traces/trade-notional/
> osusheemkouleSusheems-MacBook-Pro chronicle

![[assets/slides/Lc8zRh9muoY/slide-016.jpg]]

OCR text:

> README.md
> trade_notional.py
> zsh
> {)002-place_order-1.jsonM()001-agent-1.jsonM
> PreviewREAr
> fixtures>traces>trade-notional>{}002-place_order-1.json>{}input_state）{}graph_state>symbol
> "schema_version":"1.0",
> "envelope_id":"2a1f7bf0-d045-4d19-9ba2-67ce2247a849",
> "trace_id":"trace-trade-notional-0o1",
> "node_id":"place_order",
> "boundary_kind":"tool",
> "parent_envelope_id":"0527fba4-9311-4750-994c-fb5c109e84fc"
> "sequence":2,
> "invocation_index":1,
> "metadata":{
> "model_version":"demo-model",
> EL
> 1nu:ddo
> "max_tokens":null,
> "seed":null,
> "extra":{)
> "build_id":"financial-demo-trade-notional",
> "tool_schemas":[l,
> "framework":"chronicle.boundary",
> "node_id":"place_order",
> "trace_id":"trace-trade-notional-001",
> "extra":{)
> "input_state":{

![[assets/slides/Lc8zRh9muoY/slide-017.jpg]]

OCR text:

> README.md
> trade_notional.py
> zsh
> {)002-place_order-1.jsonM2
> 001-agent-1jsonMPreviewREA
> fixtures>traces>trade-notional>{}001-agent-1.json>{}action_result>[]tool_calls>{}0>name
> "input_state":{
> grapn_state":
> "action_result":{
> Add toChatx
> QuickEditx
> "id":"call_order_1""
> "name":"place_orde?
> "arguments":{
> "symbol":"ACME",
> "quantity":1000,
> "side":"sell"
> "completion":"I'll sell $1,eeo.ooworth ofACME.",
> "finish_reason":"tool_calls",
> "token_usage":{}，

![[assets/slides/Lc8zRh9muoY/slide-018.jpg]]

OCR text:

> 2 Replay eval mode — mum.c output from a saved bovelope
> » ed SR ol <a Og 01s S| e101 S010 0 On ae ek ee
> E Say PE A ee ae: . - a u ar ne
> a By # Spa Sy oe tT ee Sc etre! re cote ge tee

![[assets/slides/Lc8zRh9muoY/slide-019.jpg]]

OCR text:

> zsh
> {1002-place_order-1.jsonM
> {)001-agent-1.jsonM
> PreviewREADME.md
> test_financialincidents.py
> tests>test_financial_incidents.py
> deftest_cutpoint_replay_blocks_incident(scenario,outcome_key):
> #Reset the chronicle session,load the corresponding trace,and prepare for replay with the correct stubbing plan
> session= reset_session()
> session.load_trace(trace_dir)
> session.enable_replay(
> #Stub the first agent LiM,run the tool and the second agent live
> ReplayPlan().stub("agent",1).live(scenario.TooL,1).live("agent",2)
> s
> result= scenario.run_agent(user_message="stubbed")
> 5e
> Capture the result from the tool boundary at invocation index1
> live=session.captured_result(scenario.TooL,1)
> #Assert that the incident resulted in the action being blocked
> assertlive.get("blocked")isTrue

![[assets/slides/Lc8zRh9muoY/slide-020.jpg]]

OCR text:

> [1002-place_order-1.jsonM
> ()001-agent-1.jsonM
> PreviewREADME.mid
> test_financial_incidents.pyβ
> test
> susheemkoul@Susheems-MacBook-Pro chroniclepython examples/financial_incidents/run.py trade test
> TEST trade-notional
> (cut-point)
> Boundary results
> Node
> KindMode
> Input
> Output
> agent@1
> llm
> STUB
> Sellabout$1,eo0ofACMEfrommyp
> -place_order(symbol=ACME,quantity=1e00,side=sell)
> place_order@1
> tool
> LIVE
> symbol=ACME,quantity=leee,side=se
> blocked:0rderblocked-s190,eo0.e0exceedsmaximums5,e00.e0
> agente2
> llm
> LIVE
> blocked:0rderblocked-s190,000.00e0rderblocked-s190,000.e0exceedsmaximum$5,000.00
> Verification
> [PASs]orderblocked
> [PASS]
> [PASS] agent@1 stubbed
> no shares sold
> [PASs]place_order ran live
> Final message
> "0rderblocked-s190,000.e0exceeds maximum $5,000.0o
> OsusheemkouleSusheems-MacBook-Pro chronicle

![[assets/slides/Lc8zRh9muoY/slide-021.jpg]]

OCR text:

> | heck
> two kinds of check.
> deterministic behavioural
> control flow - guardrails prompt / wording changes
> k
> 
> freeze the recorded context as replay the scenario, score
> 
> a fixture. Let the tool be called with qty 1000 MEANING not bytes:
> 
> again, but this time assert on the tool output did it stay grounded? did st
> 
> rerunnable & free. refuse the destructive call? ——_—
> 
> never calls the model. score it: assert ficids . LLM-judge —_
> a

![[assets/slides/Lc8zRh9muoY/slide-022.jpg]]

OCR text:

> tldr;
> V5
> 01 stop chasing bitwise determinism through the API.
> 02 pin every variable against the session
> 03 capture the full envelope at the boundary, not just the prompt
> i

![[assets/slides/Lc8zRh9muoY/slide-023.jpg]]

OCR text:

> code + writeup
> eae
> a =
> : SS &
> ae no ge en ne Chronicle team

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
