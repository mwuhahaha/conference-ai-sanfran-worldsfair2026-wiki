---
title: "Slides: The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks"
category: "slides"
video_id: "ObTPqBGsEbA"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks

## Source Video
[The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks](https://www.youtube.com/watch?v=ObTPqBGsEbA)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/ObTPqBGsEbA/slide-001.jpg]]

OCR text:

> AIEngineer The Producti
> EUROPE AI Playbook
> Learningsfrom deploying ogents in enterprises
> Databricks Data&AlTechLead SandipanBhaumik
> AlEngineer EUROPE

![[assets/slides/ObTPqBGsEbA/slide-002.jpg]]

OCR text:

> THE PROBLEM
> The pattern you already know
> Weeks 1-4
> Pick models.
> Weeks 4-8
> Build features.
> Looks great.
> Weeks 8-12
> Demo to leaders.
> Sign-off. Ship.
> Week 14
> "Why is AI
> b*s*-ing us?"
> Month 6
> $$ in projects
> failed last year.
> Sound familiar? You're not here because you haven't seen this. You're here because you want to stop it.
> Engineering the future of AI

![[assets/slides/ObTPqBGsEbA/slide-003.jpg]]

OCR text:

> e
> The AT is the easy part
> gk ¥ You can't debug what you can't see. 01
> * ~ ol Saat ate er
> mae
> * ad
> oar ied tee U
> You can't improve what you can't measure. 02
> PTT toe td
> OECD Ma te here xee Manan ete ny
> Governonce gap
> AlEngin
> eee | PVE Sales |
> ’ aU cela

![[assets/slides/ObTPqBGsEbA/slide-004.jpg]]

OCR text:

> The Five Pillars of Production AI
> as rep ey 0303 oye O05
> mn . Evaluation fel estuarleliiiag Data Foundation Orchestration Governance
> Each pillor enadles the next. Skip one and the whole thing breaks in production.
> [sean
> »
> Lael Engineering the future of Al

![[assets/slides/ObTPqBGsEbA/slide-005.jpg]]

OCR text:

> PILLAR 02 &
> o Define success with numbers
> Not ‘accurate -- BUL 87%. en fer disputes, «2%, false positives, 60%, detection
> Evaluation date Numbers make model selection obvious
> ca
> ate hws
> oa rd
> Build test cases from real data
> ae] B
> * i
> a ra . ‘ Pull 200+ real conversations from: production fogs Ancnymise them Every case
> * You reva | Tein kea by Reeds pass/faicrtena — nat locks good
> your specification.
> Without it, you're
> guessing. B Wire automated grading
> Evaluston pipeline that runs on every code change Dashboard showing metrics
> You missure success before you tive anything fo messure
> ele aace tia)
> 7
> t
> ae ,
> ra | Al Engineer |
> noe SUL tela

![[assets/slides/ObTPqBGsEbA/slide-006.jpg]]

OCR text:

> PILLAR01-DEEPDIVE
> Threelayers of evaluation
> Layer1-Deterministic
> AIE Pll detection(NER+regex),Output format validation,Response lengthbounds Layer2-Semantic ufetyi cerrectsess) severy factal class sep Deseresse stohte crret liy cme wtiatlycrt,flly rect id PIT Leak ertee by theretrievee ceetet? dhallocinated account data? OHH
> above threshold Correctness&groundedness,LLM-as-a-Judge,Non- determinismfix:run eachtest3x-flagvariance
> eitscare.
> AlEngin within scope? escalate whenconfidence was low?Didit stay Layer3-Behavioural Didit calltheright tools,in the rightorder?Didit teat? SAMPLE:LLM-as-a-Judgeprompt
> AiEngineer AlEngineer
> EUROPE

![[assets/slides/ObTPqBGsEbA/slide-007.jpg]]

OCR text:

> Databricks Data Intelligence Platform
> Disasterrecovery 100%serverless Costcontrols Enterprise security
> Databricks SQL Data warehousing Workflows/SDP Ingest,ETL,streming
> AIE Articialintellgence MosaicAI Businessinteligence AI/BI
> Lakehouse
> UnityCatalog
> AIEngin DELTALAKE ICEBERG Parquet
> AlEngi AIEngineer
> EUROPE

![[assets/slides/ObTPqBGsEbA/slide-008.jpg]]

OCR text:

> AlEngineer
> EUROPE
> AIE Multi-Agent databricks
> Orchestration
> AlEngin From Chaos to Choreography: Multi-Agent Orchestration Patterns That Actually Work - Sandipan Bhaumik AlEngineer Share
> AEng Engineering the future of Al

![[assets/slides/ObTPqBGsEbA/slide-009.jpg]]

OCR text:

> — CUS ah c) > Al/Bl coe @ Custom Apps
> eta eae carts a ve ewe * BA Shout data ond AL apes :
> te gence
> Pein
> * *
> cd Od «1 Agent Platform
> a *
> Contextual
> a Sd
> * . Developer Platform Al Governance
> Reasoning Agents P
> Knowledge Assistant Agent Orchestration Agent/Skill/MCP Registry
> Supervisor Agent Runtime thm, Al Gateway
> Documents Agent Memory Agent Obdservability
> Al Functions Model by Managed OAuth Apps
> Capacity OO Gein fo aN 8
> Alingin
> ie | AlEngineer |
> : se) Kola

![[assets/slides/ObTPqBGsEbA/slide-010.jpg]]

OCR text:

> CASE STUDY
> Same project.
> ate Same problem.
> vay DUSCOUSIE eer toe
> THE PROBLEM THE KEY DIFFERENCE
> a We didn't pick a model
> en ee TTP OLeO mG Wels) alee
> aac Sete ea Pe CC CECA
> »
> liters | AlEngineer |
> 7 ae) e) a3

![[assets/slides/ObTPqBGsEbA/slide-011.jpg]]

OCR text:

> 4 7 CASE STU
> Six Ween, post-launch
> I y Or
> | AlEngineer 625
> EUROPE
> Estee Det
> on J ee ee Ree Ler
> . See Tot eae tet ts oot te eh ee
> CE eee Bet kn Cie ee. i
> ee Mit tides te Bei eae Re a oeeee
> jee a ae

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
