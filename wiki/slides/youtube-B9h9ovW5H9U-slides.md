---
title: "Slides: Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j"
category: "slides"
video_id: "B9h9ovW5H9U"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j

## Source Video
[Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j](https://www.youtube.com/watch?v=B9h9ovW5H9U)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/B9h9ovW5H9U/slide-001.jpg]]

OCR text:

> €3 Braintrust €} WorkOS OpenAl

![[assets/slides/B9h9ovW5H9U/slide-002.jpg]]

OCR text:

> Context Graphsi1o1 ~~
> _ What They Are and How to Get Started in f
> 5 Minutes |
> a -_ _ Sey rs a 7 oN ee
> —— 7 NN Pa \
> P J T
> = _ ln Engineering the future of Al
> oY woe om _

![[assets/slides/B9h9ovW5H9U/slide-003.jpg]]

OCR text:

> Context Graphs Ra}
> gegen Rasa cie ee
> ae ae 7 om Cos Pesce
> * * ee Sa. whe th Sy
> . i RETIREE SNORE Ce Gee
> r in pietegs 2 oie
> ae CONTEIT GRADS CAPTURTWG Tee “Warr” q ro —. : . ae
> bo oN
> mae ALS cra. Hands On With Context Graphs And
> inte tgeatat ee me Graphs, Graphs Everywhere-with Neo4j
> ° wave : Sudhir Hasbe (Ep 43) .
> to nee te ae . x @:-
> po D
> P )
> “s a | AlEngineer |
> enna aed
> » oe ca ad

![[assets/slides/B9h9ovW5H9U/slide-004.jpg]]

OCR text:

> What Do Agents Need to be Accurate? ra
> Knowledge Base
> Information required to answer
> * i questions
> Ps e
> po
>
> a | AlEngineer |
> oe ae ate

![[assets/slides/B9h9ovW5H9U/slide-005.jpg]]

OCR text:

> What Do Agents Need to be Accurate? a
> Knowledge Base Context Graph
> Pein Information required to answer Information required to make
>
> * i questions fe f-tol Ye ek)
>
> Maree
>
> * ras * co ee aaa ee Cea ey Cer
>
> “Approve credit limit increase for Jessica Norns? Requesting £ 25K"
> 4 ; en b Engineering the future of Al
> a Li 7 _ | dl
>
> a Os

![[assets/slides/B9h9ovW5H9U/slide-006.jpg]]

OCR text:

> Context Graph Data Model
> * Person, Account, Transaction, Organization fo a
> ac 7
> , -
> oq % ky
> Decisions, Transactions, Approvals, Rejections Q
> CONTEXT (The why) . -
> Policies applied, Risk factors, Employee reasoning
> po "
> 4 a | Al Engineer |
> ee oil a elas
> 4 ee aS 4

![[assets/slides/B9h9ovW5H9U/slide-007.jpg]]

OCR text:

> ContextGraphDemo
> Financial ServicesAgent
> context-graph-demo.vercel.app
> DATASOURCES
> BACKEND SERVICES
> FRONTEND&USERINTERFACE
> AIE
> Ingestion/ETL
> Data
> FastAPI Application
> Data Transfer
> API Calls&
> SupportTicket
> +ClaudeAgent SDK
> System
> NexLjsUI
> Application
> 10MCPTools
> Claude Agent
> User Actions
> &Queies
> CRM(e.g.
> Salesforce)
> (Embeddings)
> OpenAIAPI
> Chakra UIv3
> Neo4jContextGraph&GDS
> Internal
> BusinessData
> NVLGraphs
> Neo
> Vector
> GraphData Science Algorthms
> (Visualization)
> Aurabs
> Search
> Simlaritg LouvinPageRank
> (GOS)-FaRPxNNNode
> PP.1dNAPKPy
> Engineering the future of Al

![[assets/slides/B9h9ovW5H9U/slide-008.jpg]]

OCR text:

> Context Graph Demo
> Al Assistant Ask guts Context Craph Decision Trace
> AIE "acent_fLago_tranurti _inflecerel. "aceet_relae,trsT
> ety_percest_flaggee adK
> +.42684218526315799,
> t_fLagoed_transact sant°:
> aud tyoiogyFT-8291. elcity checkfaed
> 4rita tac
> s7(e-4ga4-s410- c116871", "neighbor_co 2r4kTai
> cation rejected Credit score ef 709 m treihoid cf 620. Recent
> 1msk.facs
> Engineering the future of Al

![[assets/slides/B9h9ovW5H9U/slide-009.jpg]]

OCR text:

> h oe A Pe fea oP catee
> How the Agent Traces Decision History “ce gene
> REJECT or £SCALATE ~- grounded in institutional Knowledge, not justa ced:t score “ans
> we
> i Query Context Graph oe
> Agent reteeves Jessica's full profile accounts, transactians, employer, risk ter Heston Hin prarssenty
> ran? Bee .
> og ag sine ewemnce somszeas a
> * * @ Trace Decision History iA
> bd * ime
> i aed Past fraud flag (Agri 2025), compliance rejections. velocny check failures
> tar far Gabent_frannd_petteces|
> Ej Hybrid Search Bt wee
> eco beak end
> Semunuc sinularnty (texatembeddings} + structural sumilunity (FastRP praph embedaings) meus | 0d ies
> Reconermaditnea
> + OSCALATE FOR MAANIAL MEME
> PCE ong feneog nous svete
> ——— ee oe
> 31 nodes - 30 relationships - Jessica's complete context in a single graph traversal sangitantieiconantainvalaspoed
> segue ‘apesce
> ry a ° °
> ——_
> = oe Engineering the future of Al
> a al
> er aa . tae?

![[assets/slides/B9h9ovW5H9U/slide-010.jpg]]

OCR text:

> rosea’ RRCAAE SEWNCE) Dixer eRe Cy.)
> Context Graph Demo yi
> Araceae
> Cea Teena Dee Rel
> Pane o
>
> * a
> * *
> * a
>
> How GDS Powers the Agent's 10 MCP Tools mosray
>
> ad
>
> eran Ce ee re .
>
> ee rare re eerye rrr
>
> eee iris Going Forward: Industry Specific Examples
>
> Merle ae are ore bss) Tene
> fe ae re es
> Pee Erneta Taree) eed peninned ae i’
> Pie eee Cn re ce LATER | Government & Detenne
> 6 po A
> ‘= Al Engineer
> es N PC
> ws - a a vead
> Ms
> Peers at cane ny 4

![[assets/slides/B9h9ovW5H9U/slide-011.jpg]]

OCR text:

> New Open Source Project: Create-Context-Graph :n
> Interactive CLI ae wenn gee ey g
> scaffolding tool @ euet = metinnare Cate traps MM Vuelnatnn Devnnn Treas
> generates complete. See liieie E BE Ree usmeme 25 us
> Pann elem Chia Qo © 3 Bes
> * * A i wetudeet Eau HE . foes ctyert sees
> a a graph applications. a \@ SET
> ena od SS Bef ES ¥ sits * Spee
> ara? Bo SONI Ra NK Lediimes tee
> oot Sa ee ae omeeam eo = Se
> for Al agents backed by “ee co. | Loe Sars
> eM ee. Tee
> po 7
> 7 ; .
> > gee | PA Sale lito |
> a uP ae
> i ie

![[assets/slides/B9h9ovW5H9U/slide-012.jpg]]

OCR text:

> (base)zachhlumenfold:-/d
> Project generated!
> Generating deno data...
> [1/4] Seeded 60 entities
> [3/4]Generated 25documents
> [2/4]Created 119relationships
> [4/4]Created1edecisiontraces
> Genarated:60 entities,119 relationships,25 documents,10 decision traces
> Written to:/Users/zachblumenfeld/demo/my-health-apo-2/data/fixtures.json
> Donel Your Healthcare context graph apo is ready.
> cdmy-health-app-2
> nake dockar-up
> make install
> Install dependencies
> nake seed
> Start Neo4j
> AIE
> makestart
> Seed sanple data
> start backend+frontend
> Frontend:httoi//locaihost:3oe9
> Backend:
> http://1oc1host:80
> (base)zachblumenfeld:-/demos
> Engineering thefutureofAl

![[assets/slides/B9h9ovW5H9U/slide-013.jpg]]

OCR text:

> Panes
> bd ad
> * os *
> __.
> = eu Al i
> = pier Engineer
> i ¥ q Ea Sele) a
> oe 4

![[assets/slides/B9h9ovW5H9U/slide-014.jpg]]

OCR text:

> Create-Context-Graph Key Features A
> e 8 Agent Frameworks -- PydanticAl. Claude Agent SDK, OpenAl Agents SDK, LangGraph.
> CrewAl, Strands, Google ADK, and Anthropic Too!s.
> 4 © =22 Built-in Domains -- Healthcare. finsery, real estate, and more w/ rich demo data. + You can
> ra ine * create your own Custom Domains
> mn . @ 12 SaaS data connectors -- GitHub. Slack, Jira, Notion, Gmail, Google Calendar. Satesforce.
> Paras Linear, Google Workspace. Claude Code. Claude Al. and ChatGPT.
> © Graph-native Al agents -- Cypher-powered tools for querying entities, relationships, and
> decision traces. Tool calls stream in real-time with live progress indicators.
> @ MCP Server for Claude Desktop -- Optionally generate an MCP server config so Claude
> Desktop quenes the same knowledge graph as your web app
> e Multi-turn Conversations, Streaming Chat, and Interactive Graph Visualizations
> = , a Al Engineer
> . a. — Sue) a
> | : ae , | X

![[assets/slides/B9h9ovW5H9U/slide-015.jpg]]

OCR text:

> Create-Context-Graph Architecture
> “aoe mae 9 een)
> and Cen +E es
> aco =
> bd a
> ans
> Loe C=) ==
> = | =e
> ee Ee} ie
> See
> a So i
> = ; AlEngineer
> ‘Sy Sal ? Le
> | F ca?

![[assets/slides/B9h9ovW5H9U/slide-016.jpg]]

OCR text:

> Resources Ra)
> a Create Context Neo4j Agent
> a AU ar Loads abel memory
> x x
> ace Byer eon) Leia]
> * * Toe Pe 2 ew =
> ae Pee fee saieen
> rete ey °. A # ;
> (arch (al: [alee
> CTE aaa a fe ee eg Pan Sates aad dC SC
> eee oaTe RerT a : Tol
> rea
> Cue
> (ass aa
> ‘ Pn ate oe Fa ea Tee aet Sea)
> =
> in CA A
> ae a yt | PV Sats lag |
> ma ' h oh ead
> LS ag ey p: ne

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
