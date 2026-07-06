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
These slides are extracted from a public AI Engineer YouTube video that matched one or more scheduled World's Fair sessions by speaker. They are supporting context unless the video is later confirmed as the exact session recording.

## Related Scheduled Sessions
- [[2026-07-01-patrick-debois-coding-agents-don-t-scale-themselves-neither-do-your-teams-the-rise-of-agent-enablement]] — Coding Agents Don't Scale Themselves. Neither Do Your Teams.The Rise of Agent Enablement.

## Extracted Slides
![[assets/slides/bSG9wUYaHWU/slide-001.jpg]]

OCR text:

> €3 Braintrust €} WorkOS OpenAl

![[assets/slides/bSG9wUYaHWU/slide-002.jpg]]

OCR text:

> Za hop oa Context is the
> f
> 
> ites
> ¢ whe 0 8 wees

![[assets/slides/bSG9wUYaHWU/slide-003.jpg]]

OCR text:

> ContextisthenewCode
> Prompt→Code
> Code→Skill
> Prompt
> Code
> deffetch_user（uid,retrles3)1
> for1inrangelretries)i
> Addeorhandingandretry
> tryi
> logic wltha timeout.
> r=requests.geti
> AIE
> f/users/(uid)",tineout=5)
> r.raise_for_statust)
> returm r.json()
> packagedas
> Code
> Ski
> det fetcseruid,retries3):
> for1Inrange(retries)
> AP1 Fetch Best Practices
> tryi
> Aways set arequest meout
> rreguests.gett
> -Retry on transient errors
> (5)/s/
> Re-raise on last attempt
> r.ralse_for_statusl)
> returnc.json[)
> EvaLs
> except Exceptien as e！
> meout paramsset
> f1-retries-1:raise
> √retesz3
> Prompt → Code (left) ·Code → Skil (right)
> AlEngineer
> Engineering the future of Al
> AEnginoer

![[assets/slides/bSG9wUYaHWU/slide-004.jpg]]

OCR text:

> to think in parallels
> AIE
> 2009-WhatifOpswaslikeDev
> 2025-WhatifContextwaslikeCode
> AIEngineer
> Patrick Debois-ProductDevrel Tessl
> AIEngineer
> AEngineer
> EUROPE

![[assets/slides/bSG9wUYaHWU/slide-005.jpg]]

OCR text:

> Context Development Lifecycle
> Generate Distribute
> (XD)
> Evaluate Observe
> |
> a
> Engineering the future of Al
> wmPuses

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
> rales a Pee Reis] 7 i _ i a °
> “ee a as
> aw
> .
> vee
> Engineering the future of Al

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

> Public vs Private Registries
> a: @
> BRKILLS The package manager for
> rales ; : agent skills and context
> bd bd
> nares
> rs * pn
> wy *
> | lachal
> a Google DeepMind
> Piss

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

> Context security scan
> 
> ann)
> * *
> ae
> * a
> 
> * a * cee
> 
> a
> ca | AlEngineer |
> 
> a—Disrs EUROPE

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

> S Entire | signin |
> air Every commit tells a story.
> i bs] 4 Now you can read it.
> oa
> :
> t 5 .
> Engineering the future of Al
> Pass

![[assets/slides/bSG9wUYaHWU/slide-018.jpg]]

OCR text:

> Context from production code
> Calera]
> a e Pa * Understand code behavior with
> * function level data
> [serge]
> |
> k a
> Engineering the future of Al
> 
> we Pais

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

> Skills Development lifecycle
> 
> Oca as teal O strioute Onseve
> 
> * rs
> 
> nN
> Ss a
> | aaleplniptal
> $3 Braintrust €) WorkOS OpenAl
> a Piuss

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
## Reconstructed Slide Deck
- [[youtube-bSG9wUYaHWU-reconstructed-slides]]
## Dense Scene-Detected Slide Candidates
- [[youtube-bSG9wUYaHWU-dense-slides]]
