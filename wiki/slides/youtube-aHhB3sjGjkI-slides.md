---
title: "Slides: Agents Building Agents - Alfonso Graziano, Nearform"
category: "slides"
video_id: "aHhB3sjGjkI"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: Agents Building Agents - Alfonso Graziano, Nearform

## Source Video
[Agents Building Agents - Alfonso Graziano, Nearform](https://www.youtube.com/watch?v=aHhB3sjGjkI)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/aHhB3sjGjkI/slide-001.jpg]]

OCR text:

> About me
> Alfonso Graziano tle
> ah Al Tech Lead @ Nearform
> 4
> y e Building Al Agents
> sb!
> a “Sf e Supporting teams adopting AINE
> 7 e Author of ‘
> “Learning Al-Native Software Engineering”

![[assets/slides/aHhB3sjGjkI/slide-002.jpg]]

OCR text:

> .
> ee 4 A =
> Everyone wants ea OMATION Al AGENT
> Al Agents A MAUL Saco a
>
> ao [7 | [ere
> we
> ara petics oh
> | ae OOS |

![[assets/slides/aHhB3sjGjkI/slide-003.jpg]]

OCR text:

> How do we do that?
> 4 B
> pt Pad -
> ee
> ) /
> Y aL. ©
> a a de
> ‘ t

![[assets/slides/aHhB3sjGjkI/slide-004.jpg]]

OCR text:

> The Problems with
> Building Al Agents
> ..and how to solve them partially,
> with otheragents!:
> -

![[assets/slides/aHhB3sjGjkI/slide-005.jpg]]

OCR text:

> AlAgents:arefresher
> Short-termmemory Long-termmemory
> Calendar() Memory
> Calculator() Reflection
> Codelnterpreter() Tools Agent Planning Self-critics
> Search() Chai
> .more Action Subgoal

![[assets/slides/aHhB3sjGjkI/slide-006.jpg]]

OCR text:

> Two classes of problems
> Bad B ad
> performances performanc~"
> on gees on Ans ied ye! It iy ;
> it

![[assets/slides/aHhB3sjGjkI/slide-007.jpg]]

OCR text:

> Bad performances on evals - the golden dataset
> » 8 c
> 1 input output
> 42 Write a program that determines whether any arbitrary program will halt or run forever.
> What is the output for the program that checks itsett? IMPOSSIBLE
> 43° How old is Elon Musk? PERSONAL_INFO_REJECTED
> 44 Calculate Jeff Bezos's net worth divided by the US population PERSONAL_INFO_REJECTED
> a5 (|have $50,000 to invest. What's the optimal spit between stocks and bonds to maximize
> returns? FINANCIAL_ADVICE_REJECTED
> 46 Convert 250 USD to EUR at today’s exchange rate REQUIRES_LIVE_RATE
> What was the maximum temperature (in °C) in Pans on January 15, 20247 Use the
> 47 Open-Meteo historical weather API at hitps//archive-api.open-meteo.convv t/archive with
> latitude 248.8566. longitude=2.3522, start_date22024-01-15, and_date=2024-01-15,
> daily=temperature_2m_max. Retum just the number. 46
> What was the minimum temperature {in °C) in Tokyo on July 20, 20247 Use the
> 48 Open-Meteo historical weather API at hitps://archive-api.open-meteo.comvv t/archive with
> latitude=35.6762, longitude= 139.6503, start_date=2024-07-20, end_date=2024-07-20,
> daity=temperature_2m_min. Retum just the number. 25.7 Oo mi
> 49 Fetch the list of users from hitps://jsonplaceholder.typicode.com/users and retum the total #
> number of users. 10
> 50 Fetch all todos from https://jsonplaceholder.typicode.comvtodos. What percentage of them , 5]
> are completed? Round to 1 decimal place. 45.0 Bad 4 B
> 5, How many posts does user with ID 7 have? Fetch from wy oe se
> hitps://jsonplaceholder typicode.com/posts ?userid=7 and count the results. 10 perfo ie * | e nz
> rer) . en 1 . howe . wow oo : $24 i
> on 3
> e
> i.

![[assets/slides/aHhB3sjGjkI/slide-008.jpg]]

OCR text:

> Some failure modes
> . ¥ ¥,. hk 97?) thee ay > a
> a pj Be a ; SOF
> er ‘750. 4. Jame Sena
> yoy “eee o a ‘ bea as ;
> om): arr gss ¥ " [29 P)
> : ~ s " >. 2 am “~~ Sena wl TY ey ry
> Sr bat A awa pea xt
> No tools Wrong system prompt No context retrieval
> The system doesn't have The system prompt doesn't The agent is not able to
> the tools it requires to align with the rules which are fetch the relevant context
> operate correctly, or the represented in the Golden to answer cer777t"
> tools are wrong and/or Dataset
> contains bugs 2
> 9 i” . *
> , 7
> ind rv} ow

![[assets/slides/aHhB3sjGjkI/slide-009.jpg]]

OCR text:

> How autoresearch works
> Autoreseatch Progress: 83 Expersmments, 15 Kept Improvements
> too | Beli
> © cane
> °°
> Cos
> y
> 5 °
> t Og e
> t
> |
> = e
> g
> o
> § cub
> 3 ° °
> 3 o
> °
> cen ee
> e
> wos re
> coy é Bs
> t “ pe)
> . : + : -_ al
> ; a ‘ a) le) RA
> ro no -
> 5 ‘
> A

![[assets/slides/aHhB3sjGjkI/slide-010.jpg]]

OCR text:

> So,Ibuiltauto-agent
> auto-agent Public Pin Watch 0 Fork4 Star 84
> master P1Branch0Tags QGo to fle Add file G <>Code About
> alfonsograziano feat:replace Claude integration witha generic provider system for 6a24878·5 days ago 32Commits provided. No description,website,ortopics
> docs specs src templates.claude/skills feat:add Kiro CLl provider support and benchmark frame. feat:add accuracy chart skidocumentation and example feat:add accuracy chart skil documentationand example. feat:replace Claude integration witha genericprovider sy- feat:addKiro CLI provider support and benchmark frame... feat: add generate-changelog script and related documen.. 5days ago last week last week lastweek lastweek lastweek Readme Activity 18stars Owatching Releases MITicense 4forks
> tests feat:add Kiro CLI provider support and benchmark frame.. last week No releas Createa newrele
> gitignore LICENSE README.md Add job creationfunctionalityand update templates Add MIT License and enhance README with demo agent i feat: add Kiro CLl provider support and benchmark frame, lastweek lastweek last week Packages qndsabeped oN Publish yourfirstpe
> https://github.com/alfonsograziano/auto-agent

![[assets/slides/aHhB3sjGjkI/slide-011.jpg]]

OCR text:

> And it actually works!
> Accuracy Improvements In The Agent Performances
> 100% +10% ona
> Production agent
> 83.3%
> 80%
> 71.7
> 61.7% See
> Z 70.0%
> 5 60% $8.3%
> e 60.0% 68.3%
> 2 Ae Reration Summary
> 317 . wegianenay ¥ ear Kate @ See tete
> 1 O01 ad 3700 ees
> 04 SR g
> Baseine at 3? a3 za RS #6 i 885 Saeea , oa « y
> * ww,
> . > 003-48 7991 os hs} i 7
> Iteration

![[assets/slides/aHhB3sjGjkI/slide-012.jpg]]

OCR text:

> The core idea
> Claude builds the agent
> —_serrere ere
> 0,0
> _T he agent gives Feedback

![[assets/slides/aHhB3sjGjkI/slide-013.jpg]]

OCR text:

> The human in the loop
> Claude builds the agent :
> The agent gives Feedback
> \ oo /
> eg! oo
> he :
> an ° B) ‘I
> 30 |

![[assets/slides/aHhB3sjGjkI/slide-014.jpg]]

OCR text:

> jobs>agent-2>JOB.md>##PriorityHints
> ##Objective
> Step1
> What is the main goal of this optimization job? Be specific about what "better"means.
> createajob
> Examples:
> "Improve accuracy on themath golden dataset from~20%to 80%+
> "Reduce average latency below 5ooms while maintaining current accuracy"
> “Add support for x questions (currently e% pass rate on that category)
> Wewant to improve theaccuracy asmuch aswe can
> ##Target Repository
> Absolute or relative path to the repo the coding agent will modify.
> Also specify which branch to start from-this is the baseline.
> **Path**:/Users/alfonsograziano/Desktop/exp/auto-agent-demo
> **Branch**:master
> ##Metrics
> Which metric should the system optimize,and what guardrails apply to
> The primary metric determines whether a hypothesis is accepted or rej
> secondary metric regresses beyond its threshold,even if the primary
> **Primarymetric**:accuracy（maximize)
> **Secondary constraints**:
> latency_avg_ms:max 2e% regression
> cost_usd:max5e% regression

![[assets/slides/aHhB3sjGjkI/slide-015.jpg]]

OCR text:

> Step 2 - run the loop
> stereo
> hypotess agent owls
> / Be ’ {
> ate ee ON wmprevewert
> <
> ree reate an Chan. be. Rum the Create on ¢ the Rua the
> reatacen Run the Create mm] ¢ the | Run the Ceeate an} Cl the | Run the ‘
> conel ae [a
> \G lmorove went \ "A
> bypotes-s , y
> eet :. i)
> * we define how many iterations we want to run a f mz
> 22
> " yy

![[assets/slides/aHhB3sjGjkI/slide-016.jpg]]

OCR text:

> Case fetch- country density
> eee Ror
> Saeed ers . a F fi
> Cause. we:ghted-hurmome-maan
> Same cavks re 5 “ o a
> Pee C tats eer er
> See es trane
> Summary
> Pee et Oe Ren eT ee MRE SoD)
> Por ae eee Se eT ee re ETS
> "ina
> Large exact steqer cor putat 274 15 cases) a 5 rae 8% % .
> . a : 7 7 7 “gg
> ae
> er Oe ie re Re ee ae | : a eee y |
> ee. a
> Re ee ee Ce Pee on “ * ‘ | by
> cay 7

![[assets/slides/aHhB3sjGjkI/slide-017.jpg]]

OCR text:

> Step 2.2 - running one iteration
> REPORT. md
> Create anf Change the Run the 77
> hypotesis agent evals
> Ng Updates
> MEMORY .md
> . Yes
> Metrics Continue From
> improved this branch
> “The generated hypothesis is based No
> on MEMORY.md, other report files with a a yaa
> . . . . ie 57 - —
> failures, codebase investigation etc Rollback te = ae '¥
> prev. branch 4
> n 7 Ve ,
> “od

![[assets/slides/aHhB3sjGjkI/slide-018.jpg]]

OCR text:

> Step 2.x - running every iteration
> ese =
> wt rete SF
> & 2H (otea or | 8 (aero)
> se fees henge the | mn the (sata)
> i
> (=)
> SSE
> Cee OU Nee)
> ayes =
> Ree (came .
> Gp BE) Gee) ..
> (=) HH Re she
> a Ke we 7 i y
> = es

![[assets/slides/aHhB3sjGjkI/slide-019.jpg]]

OCR text:

> A real test on an already optimized agent_
> Baseline accuracy: 76.7% e Found edge cases
> Iteration Summary:
> # Hypothesis Decision Accuracy e Improved the system prompt
> 1 = @@1-bcebS1 CONTINUE 80.7% e Improved tools description
> 2 @@2- F7F 825 CONTINUE 82.7%
> 3 @@3-5@18d3 CONTINUE 81.9% ° Fixed tools logic
> 4 04-dfeiSd ROLLBACK 82.1%
> 5 @@S-a4b57e CONTINUE 82.6%
> 6  006-fb02¢4 CONTINUE 84.4%
> 7 = 007-81e640 ROLLBACK 81.6%
> 8 @08-1ff45c CONTINUE 82.9%
> 9  0@9-1889d9 CONTINUE 86.4%
> 10 ©618-691768 ROLLBACK 85.1% - ad a
> 11 11-@dea9e ROLLBACK 84.5% = ad
> 12 @12-deb78e ROLLBACK 84.7% ] i
> LA
> 4

![[assets/slides/aHhB3sjGjkI/slide-020.jpg]]

OCR text:

> Fixing bad performances on live data
> LS) eda ae eyes Baa reliel ig
> Bad
> performances r es
> on vezi! a. Ge
> ee feeds We Baas fe ; hy
> aa
> n ~ ae

![[assets/slides/aHhB3sjGjkI/slide-021.jpg]]

OCR text:

> How do we fix that?
> the user uses
> . the service
> User gives a feedback
> <—
> the trace
> —_—. Subject Matter Experts
> annotate the trace
> multiple traces... Expert validation
> yo!
> Agent Traces with negative Clustering of >} Fx proposal >) Fix aes ed
> workflow Feedback analyzed > failure modes generated imo as % /

![[assets/slides/aHhB3sjGjkI/slide-022.jpg]]

OCR text:

> We collect }
> tracing informations <2 Search + S&S & Timeline
> t= QA-Chatbot
> 12.778
> contains-pii: 0.00 O — error-anatysi... 100 O — error-analysi... 1.00 O ’
> helpfulness: 0.20 © —is_question: 1.00 O —is_same_lan... 1.00 O
> *»  handle-chatbot-message v
> 12.775
> **  get-langfuse-prompt
> —  create-mcp-client
> 008s
> -« al.streamText
> v
> 12.63s —_ --
> <“ ai.streamText.doStream
> 5 485 1,119 > 52 (9 1.121) a yy
> 7 ~
> J aitoolCall i a 7 —
> 037s ar. es
>  ai.streamText.doStream
> a “ls 4.268 > 28119 4549) er ‘

![[assets/slides/aHhB3sjGjkI/slide-023.jpg]]

OCR text:

> Step 2 (a): The user gives a feedback
> E= Trace 1632fbb0299d5d21ab0fed2957bbfSaa
> © Search & 8 Timeline ®
> t= langfuse-chatbot
> 8.475 v
> S c user-feedba.. 0.00 O
> Additional Feedback "Very long answer ¥
> Te? aS APT, RES BPM
> ++ ai.streamText
> Very long answed 447s ¥
> ai.streamText.doStream
> . 4.46s 35 > 82 (2 17) ——
> 0 ._ &
> oe. =
> a
> Py

![[assets/slides/aHhB3sjGjkI/slide-024.jpg]]

OCR text:

> Step 3: Collect all the traces with feedback locally
> npm run fetch-traces-with-feedback.ts --from 2026-03-30 ==to'2026-04-03:--limit 200
> 1 { “a -
> ? “fetchedat™: “2026-04-03712:24:50.6192", 7
> 3 “environment”: “production”, oo
> i “totalScanned”: 133,
> 5 “totalwithFeedback”: 114, *
> 6 “traces”: | od
> 3 ( .
> 8 “td: "f47ac 10b928e4d27b11a92837d8e9210", 2
> “ “userId”: “j.smith@quantum-solutions.1o”, =
> le “timestamp”: “2026-04-05T08:14:12.11527,
> 11 “model”: “us. anthropic.claude- sonnet -4-5-20256929-v1:0", pis
> 2 “Latency”: 2.12, cn
> 13 “question”: “what is the recommended torque specification for the titanium alloy bolts on the ¢ a
> 14 “answer”: “To find the specific torque requirements for the Cx-5@0 engine components, please re --4#7.
> 1s “comments”: £), :
> 16 “userfeedback": [ - 0
> 1? “score”: i,
> 13 “comment”: “Solid guidance, but could be more precise. 7/18. \nl) You should have linked dirc di.
> Is hw =
> 28 “annotations”: [} A
> at > q
> Poy
>
> A

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
