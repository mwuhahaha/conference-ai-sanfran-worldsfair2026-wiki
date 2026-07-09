---
title: "Slides: Context Is the New Code — Patrick Debois, Tessl"
category: "slides"
video_id: "bSG9wUYaHWU"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: Context Is the New Code — Patrick Debois, Tessl

## Source Video
[Context Is the New Code — Patrick Debois, Tessl](https://www.youtube.com/watch?v=bSG9wUYaHWU)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/bSG9wUYaHWU/slide-001.jpg]]

OCR text:

> PLATINUM SPONSORS
> Braintrust WorkOS OpenAI

![[assets/slides/bSG9wUYaHWU/slide-002.jpg]]

OCR text:

> AI Engineer
> EUROPE
> 2026
> Context is the

![[assets/slides/bSG9wUYaHWU/slide-003.jpg]]

OCR text:

> Context is the new Code
> Prompt → Code
> Code → Skill
> Prompt
> Write a function to fetch user
> data from an API endpoint.
> Add error handling and retry
> logic with a timeout.
> Code
> def fetch_user(uid, retries=3):
> for i in range(retries):
> try:
> r = requests.get(
> f"/users/{uid}", timeout=5)
> r.raise_for_status()
> return r.json()
> packaged as
> Skill
> API Fetch Best Practices
> - Always set a request timeout
> - Retry on transient errors
> - Re-raise on last attempt
> Evals
> - timeout params set
> - retries ≥ 3
> Prompt → Code (left) · Code → Skill (right)
> Engineering the future of AI

![[assets/slides/bSG9wUYaHWU/slide-004.jpg]]

OCR text:

> I ❤️ to think in parallels
> 2009 - What if Ops was like Dev
> 2025 - What if Context was like Code
> Patrick Debois - Product Devrel Tessl

![[assets/slides/bSG9wUYaHWU/slide-005.jpg]]

OCR text:

> Context Development Lifecycle
> Generate
> Making implicit knowledge explicit
> Distribute
> Context as a package
> Evaluate
> TDD for context
> Observe
> Learn from use in the wild
> Engineering the future of AI

![[assets/slides/bSG9wUYaHWU/slide-006.jpg]]

OCR text:

> Prompts - Humans as context engine
> Welcome back Patrick!
> ask Claude to Create.
> Penn 3
> * of
> aco
> * af
> ed
> Tell re when my talk 15 at Al engineer = https: //wew.at.enqinecr/europe
> Fetchihtips://we..ar.engineer/europe }
> Received 447KB (2006 OK)
> e@ Your talk “Context Is the New Code" 15 on April 10 (Day 3) at Ll:15am in the
> Westminster track.
> | ag |
> ee]
> r 2 °
> a] Engineering the future of Al
> we Pics

![[assets/slides/bSG9wUYaHWU/slide-007.jpg]]

OCR text:

> Rules, Instructions - Agent.md
> AGENTS.md
> Panel a
> * Bd
> . a ==>
> * 5 d
> * os *
> | Lapa |
> '
> | AlEngineer |
> Bun AM a

![[assets/slides/bSG9wUYaHWU/slide-008.jpg]]

OCR text:

> Context Connectors
> Connect models to the real world
> Servers and tools from the community that connect models to files, APIs, databases, and more.
> All MCP servers
> Markitdown
> Netdata
> Github MCP - https://github.com/mcp
> Connect Unblocked to your knowledge sources
> Install the Unblocked MCP plugin
> Engineering the future of AI

![[assets/slides/bSG9wUYaHWU/slide-009.jpg]]

OCR text:

> Today's Agenda
> Pane a ;
> * * 01 ¥ Generate — create & curate context
> naa
> 5g *
> nid 02 ® Evaluate — test & measure context quality
> 03 *® Distribute — package & share context
> 04 © Observe — monitor & improve in production
> | Fa ed
> [ aeal
> . * ;
> =] Al Engineer
> Puss EUROPE

![[assets/slides/bSG9wUYaHWU/slide-010.jpg]]

OCR text:

> Skill syntaxcheck~Grammarly
> AIE
> end best pacisices) and sher
> ctges
> https://docs.tesslio/evaluate/evaluating-skills
> AlEngineer
> Engineering the future of Al
> AlEngineer

![[assets/slides/bSG9wUYaHWU/slide-011.jpg]]

OCR text:

> Evals(LLM asJudge)
> CLAUDE.md-ContextRules
> ArI Stasdatds
> Erery A: eodpoint muat uae the prefix/e
> AIE
> Prompt
> esneesoluodpumaueoppy
> eapp.post(/eesome/user)defsave_user()1
> oeserate
> Eval-LLMasJodge
> Checki Does thepe
> for saving a user
> /PASS
> CLAUDE.md rule - Prompt - LLM-as-Judge eval
> AIEngineer
> Engineering the future of Al
> AlEngineer

![[assets/slides/bSG9wUYaHWU/slide-012.jpg]]

OCR text:

> Pee G
> * * e - Non-déterministic ¢ untestab! Nk error budgets
> acd
> * x « © Run 5+ trials, force binary decisions, not fuzzy scores
> bd * bd
> Care atest OID SS fal full su:te on Cl > scheduled drift checks
> ¢ @ Mine productidn Taillires — they re your Loi data
> a
> ° @ Every context change reruns the suite - - ndtkcepticns —_ f
> . Vendor metncs le — define your own
> Led
> [ a 5 5
> Cm] Engineering the future of Al
> Piss

![[assets/slides/bSG9wUYaHWU/slide-013.jpg]]

OCR text:

> PublicvsPrivate Registries
> SKILLS TE OPEN AGENT SKTLLS ECOGYSTEN Thepackagemanagerfor agentskillsandcontext
> AIE Skills arereusable capabiities forAl agents.Install them with a single command to enhance your agents withaccess toprocedural knowledge. Skils.sh-https://sikis.sh TesslRegistry-https:slegstry ros tesl sar
> CLAUDECODEMARKETPLACES
> MARKETPLRCES SAILLSLEANN AOYERTISE FEEDOSCK
> Qearch by nae,descriptien, or category.
> tecntly Palishes -Deeuoest 30-Seneratien becessaitity
> AIEngineer
> 2O25 AlEngineer GoogleDeepMind

![[assets/slides/bSG9wUYaHWU/slide-014.jpg]]

OCR text:

> DependencyManagement
> Tessl Docs
> Pvess Kt
> Q
> WhyAPM
> Alcodid
> That drectorylslinked to tessl.JsonThistleprovides documentationfor the FastAPI
> ody ryoper stsumyngptbenrrrdublee
> nue
> nomaniest for
> AIE
> tool wenyouneedinfomationabout FastPIusagefeturesand bestpractices
> APMfisDec yorprjc'santc dndecesonceyand eey
> Inidethetledectyyo/fdamaietflecaledcntis
> dddopdep aut
> -spuosudasdepngryeaodaofsuopoyadoap
> meadataabouthelencldingthpacae
> ape.ya1 - ihp vith your groect
> name:your-project
> "vorsion*o16.o*.
> "same*:*tessLpypl-faatap1*,
> dependencies:
> "docs*:*docs/Lndex.ad'.
> sitls froeay reositooy
> "describes*:*pkg:pyp1/fastapi0.116.1*,
> FPlugins
> threpics/skilts/skitls/frentene-design
> "summary':"FastAPI franework,highperform
> fast
> -gith/esome-copilot/glagins/context-englneering
> Specificagentgriaitiesfrosey repoiitory
> 1fllatcsr
> -eicreseft/aoe-sanole-gacage
> https:/docs.tessl.io/use/make-your-agents-smarter-with-
> gitclme-erg/repo-cd-repe
> documentation
> APM -https://github.com/microsoft/apm
> AIEngineer
> AIEngineer
> AlEngineer
> EUROPE

![[assets/slides/bSG9wUYaHWU/slide-015.jpg]]

OCR text:

> Contextsecurity scan
> clawdtm-skills 2ffes
> Review and rate Ciat de Code skis.See wat umans and Alagentsrecommnd
> >_metajson
> AIE ）Dkllmd
> Re-analyse
> 9securychecks con 2issuesfound
> AIEngineer SnykSkiScan-https://abs.snyk.o/experiments/skil-scan/
> AlEngineer AlEngineer EUROPE

![[assets/slides/bSG9wUYaHWU/slide-016.jpg]]

OCR text:

> 4 Learn fromA
> Aqeat Tract
> | AlEngineer
> ist ead
> Le
> | AlEngineer
> fUROFE 4
> ) a 7 a
> es in oe

![[assets/slides/bSG9wUYaHWU/slide-017.jpg]]

OCR text:

> Announcing Entire with $60m seed round
> Every commit tells a story.
> Now you can read it.
> Entire CLI hooks into your git workflow to capture AI agent sessions on every push. Sessions are indexed alongside commits, a searchable record of how code was written.
> curl -fsSL https://entire.io/install.sh | bash
> Open source • MIT licensed
> https://entire.io/
> 3.6k
> Engineering the future of AI

![[assets/slides/bSG9wUYaHWU/slide-018.jpg]]

OCR text:

> Context from production code
> Hud
> Understand code behavior with
> function level data
> Hud gathers errors and performance data at the service and function level. It connects, at runtime, the business impact and the root cause in the code. Engineers use this data in the IDE to understand how their code behaves in reality
> https://www.hud.io/
> Engineering the future of AI

![[assets/slides/bSG9wUYaHWU/slide-019.jpg]]

OCR text:

> Agent sandboxing
> @ BEERNS LASERS 5 SEARS STENTS
> Pen irangtié
> va * L7 Observabilty & Auait TY Oate Exfittranon abe egt
> * * LG Action Governance T2 Supply Chain $ Cooperative
> re ry .
> rae LS Credential & Secret Mgmt 13 Oestructive Ops 2 Soltewrare-entorced
> Ld 3 Kernel-enforced
> La Network Goundary T4 Lateral Movement 4 Structurad
> L3 Filesystem Boundary T& Parsistence SESE MG
> L2 Resource Limits 6 Privilege Escalation 1 Binary (onjott)
> Li Compute Isolation T? Denial of Service Zane bust
> 1 Pet-resource policy
> | Ea
> eaort
> cn er
> = |
> —
> —_~
> A
> C=] Al Engineer
> Piss EUROPE

![[assets/slides/bSG9wUYaHWU/slide-020.jpg]]

OCR text:

> SkillsDevelopment lifecycle
> AIE Create CONTEXT EVALS Test Distribute SHARE DELIVER Observe MEASURE& LEARN
> AUTHOR LOOP
> ORGANIZATION LOOP
> AIEngineer
> AlEnginoer Braintrust Workos OpenAl

![[assets/slides/bSG9wUYaHWU/slide-021.jpg]]

OCR text:

> EZ
> Context Flywheel  .g.
> “ a
> ; a A 888 A cee
> a * © a OSS \ re
> * —~ BRBNY SS =
> ae ty YS; > . Tees SET OF TEAMS Ws:
> C&S) =
> \ _~ x . ie ss pe. o/. 4
> eee —
> a
> AlEngineer
> ae) cela

![[assets/slides/bSG9wUYaHWU/slide-022.jpg]]

OCR text:

> , _ , eee
> me 6=6Context FI
> Al Engineer
> 3
> ae rte
> i ary mT Ss
> ns, po ocue®
> ee e
> XQ %
> -~ oe
> [ AlEngineer
> Wiis

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
