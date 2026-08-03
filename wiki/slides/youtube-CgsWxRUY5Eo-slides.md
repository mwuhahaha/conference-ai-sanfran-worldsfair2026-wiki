---
title: "Slides: AI Agents for Performance: Ship Faster, Pay Less — Rajat Shah, Netflix"
category: "slides"
video_id: "CgsWxRUY5Eo"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: AI Agents for Performance: Ship Faster, Pay Less — Rajat Shah, Netflix

## Source Video
[AI Agents for Performance: Ship Faster, Pay Less — Rajat Shah, Netflix](https://www.youtube.com/watch?v=CgsWxRUY5Eo)

## Relationship To World's Fair 2026
These slides are extracted from a verified official AI Engineer World's Fair San Francisco 2026 recording. Use them as slide and OCR evidence; official schedule pages remain canonical for titles, times, rooms, tracks, speakers, and affiliations.

## Related Scheduled Sessions
- No individual scheduled session mapping is assigned by the official media manifest; treat this as event-level media unless a future exact mapping is recorded.

## Extracted Slides
![[assets/slides/CgsWxRUY5Eo/slide-001.jpg]]

OCR text:

> Roce
> Al Agents for Performance
> ship Faster, Pay Less
> A practitioner's guide to catalog-backed performance agents.
> _ Rey aSiarlg ‘
> wo

![[assets/slides/CgsWxRUY5Eo/slide-002.jpg]]

OCR text:

> THEVIBECODINGERA
> We ship 10x faster now.
> Rajat ShahAl Platform, Netflix

![[assets/slides/CgsWxRUY5Eo/slide-003.jpg]]

OCR text:

> THEVIBECODINGERA
> We ship 10x faster now.
> Our CpU bills ship 10x faster too.
> Vibe coding giveth. The AWS invoice taketh away.
> RajatShah·AI Platform,Netflix

![[assets/slides/CgsWxRUY5Eo/slide-004.jpg]]

OCR text:

> THENEWPROBLEM
> Your Al ships code. Not
> always fast code.
> LLMs don't know your platform's
> performancepatterns.
> RajatShah·AIPlatform,Netflix

![[assets/slides/CgsWxRUY5Eo/slide-005.jpg]]

OCR text:

> THESTATUSQUO
> today Whata (human) perf engineerdoes
> Run the profiler on the. production instance.. TRIGGER
> Rajat Shah:AI Platform Netflix

![[assets/slides/CgsWxRUY5Eo/slide-006.jpg]]

OCR text:

> THE STATUS QUO
> What a (human) perf engineer does
> today
> Complete Visibility
> Java Mixed-Mode Flame Graph viadgnux perf_events
> TRIGGER elu as ‘ie
> - ; ; C++ Java ! F ius '
> pe , a aly po Java * o
> | | 1; |. Wit = fucren
> DOWNLOAD e 4 ‘.

![[assets/slides/CgsWxRUY5Eo/slide-007.jpg]]

OCR text:

> PARTO2
> Experiment The
> We ran it against a live service. Can an LLM read profiling data?
> Rajat Shah·AI Platform,Netflix

![[assets/slides/CgsWxRUY5Eo/slide-008.jpg]]

OCR text:

> UNDER THE HOOD
>
> Every profiler speaks the same language
> async-profiler / JFR re ;
>
> Py-spy 7
>
> pprof
>
> PyTorch Profiler i 1

![[assets/slides/CgsWxRUY5Eo/slide-009.jpg]]

OCR text:

> UNDER THE HOOD
> Al Agent knows the patterns
> oe cee
> orovomran nia reianes
> Ni Lorons tare lnmiRIAION Gre TaLen ee
> Ge cas seis ee morsleael aise
> i ae

![[assets/slides/CgsWxRUY5Eo/slide-010.jpg]]

OCR text:

> What the agent reads: ranked method data, not the flame image.
> ; TensorSet.merge : 2.3
> , MetricsCounter.resolve : FEL
> PST nl end 1.2% re
> i iu
> ed
> ha era eE TE se call stack “

![[assets/slides/CgsWxRUY5Eo/slide-011.jpg]]

OCR text:

> What the agent reads: ranked method data, not the flame image.
> ; TensorSet.merge Pare
> — Detected O(N’) Loop
> Rows land 3 share tne same call path
> ieee Cae adsG)
> r NEO eT ; ELA a
> ImmutableMap.copyOf 1.2% — _ 7 ae
> a
> | “4
> ae ele ORE 54 call stack «.

![[assets/slides/CgsWxRUY5Eo/slide-012.jpg]]

OCR text:

> UNDER THE HOOD
>
> What the Al Agent does with it
>
> on
>
> Parse profiler output
> rl
> it '

![[assets/slides/CgsWxRUY5Eo/slide-013.jpg]]

OCR text:

> UNDER THE HOOD
> What the Al Agent does with it
>
> on oy,
>
> Parse profiler output es exact commit |
> Ok
>
> Filter to repo code

![[assets/slides/CgsWxRUY5Eo/slide-014.jpg]]

OCR text:

> UNDER THE HOOD
> What the Al Agent does with it
> on Oy,
> Parse profiler output Check exact commit
> OR) ore!
> Filter to repo code Trace full call path
> Ps
> Soltis datas .otoal Just actually read. ae

![[assets/slides/CgsWxRUY5Eo/slide-015.jpg]]

OCR text:

> FINDING #2
> Same bug
> 7 different services.
> Each team re-derived it.
> Counter Object created on every hot-path call. 0.5-4.6%
> self CPU per service. No catalog. Each service started from zero.
> RajatShah·Al Platform,Netflix

![[assets/slides/CgsWxRUY5Eo/slide-016.jpg]]

OCR text:

> THE REAL PROBLEM
> LLMs have the memory
> fe ; a
> elite Re (e1.elar-18P
> Every run starts from scratch.
> Same bugs. Re-derived. Every. Single. Time. ie
> am

![[assets/slides/CgsWxRUY5Eo/slide-017.jpg]]

OCR text:

> Stateless LLM + Stateful Catalog = Fleet-Wide
> Witetagteyes
> eet ta eee Per eer ee 0: ere oo ee a
> vonedanten Penns Heirene Pi Sei DeTOn
> eet ry ene i i “ - Lo oes’
> 4.

![[assets/slides/CgsWxRUY5Eo/slide-018.jpg]]

OCR text:

> THE SOLUTION
> Oli e e
> == A git repo of markdown files.
> Fleet-wide memory. LLM-injectable. Human-reviewable.
> Starts from known patterns. Grows as production findings are
> confirmed.
> "
> ¢ ;

![[assets/slides/CgsWxRUY5Eo/slide-019.jpg]]

OCR text:

> THE CATALOG - BOOTSTRAPPING
> i
> You don't have to start from zero.
> PATH A- START FRESH PATH & - IMPORT EXISTING WISDOM
> mo : aug 8 _ abseil.io/fast/hints.html
> — i eeatatt
> , ee ee , , Your team’s perf playbooks
> ‘ 7
> _

![[assets/slides/CgsWxRUY5Eo/slide-020.jpg]]

OCR text:

> PATTERN CATALOG: ENTRY
> A language-agnostic pattern template. Copy it for any runtime.
> Cn ee ee ee ee
> a&

![[assets/slides/CgsWxRUY5Eo/slide-021.jpg]]

OCR text:

> TRUST BUT VERIFY
>
> How we know the PR isn't noise
> ’
> aus

![[assets/slides/CgsWxRUY5Eo/slide-022.jpg]]

OCR text:

> TRUST BUTVERIFY
> How we know the PRisn't noise
> Verify Logic
> Unit+ integration tests must pass first. break business logic. Optimization cannot:
> Rajat Shah:Ai Platform, Netflix

![[assets/slides/CgsWxRUY5Eo/slide-023.jpg]]

OCR text:

> sa SUS MElU RI YAstsd 1a
> How we know the PR isn't noise
> Verify Logic ee
> nr Deploy
> ne
> Fa

![[assets/slides/CgsWxRUY5Eo/slide-024.jpg]]

OCR text:

> TRUST BUT VERIFY
> How we know the PR isn't noise
> Verify Logic Canary Te
> ee |DT=J 0) fo)" Report
> >

![[assets/slides/CgsWxRUY5Eo/slide-025.jpg]]

OCR text:

> TRUST BUT VERIFY
>
> How we know the PR isn't noise
>
> Verify Logic Canary eet Engineer
> on eg Deploy Report Decision

![[assets/slides/CgsWxRUY5Eo/slide-026.jpg]]

OCR text:

> ARCHITECTURE
>
> REACTIVE PATH PROACTIVE PATH
>
> Profile » Analyze + Fix +PR PR created + Cataloglookup >
> Inline comment

![[assets/slides/CgsWxRUY5Eo/slide-027.jpg]]

OCR text:

> SHIFT LEFT - ALL THE WAY
> Us CEING Ota CotOved BEET OL GME SIS AC CLAS EROS OTOL ETON Rit A LSHrO sea CeO DELO LED
> aro Ger SG ee a ee ee ee
> Anti-pattern detected: Suggested fix:
> 'e
> a

![[assets/slides/CgsWxRUY5Eo/slide-028.jpg]]

OCR text:

> GUARDRAILS
> Don't use Al for what your infrastructure should own.
> Tests OF Taree Pattern catalog
> YY,
> oe

![[assets/slides/CgsWxRUY5Eo/slide-029.jpg]]

OCR text:

> NONIMUM VIABLE VERSION
> Build your core foundations first.
> The Irreducible Core Start Here Today
> : yo
> a \
> iL

![[assets/slides/CgsWxRUY5Eo/slide-030.jpg]]

OCR text:

> THE TAKEAWAY
> Stateless LLM
> + Stateful Catalog
> = Fleet-Wide Memory
> The agent drafts the fix. Infra validates it. You decide.
> «5S min ~6.5% CPU 7 Services
> i
> LF
> 4
> ;

![[assets/slides/CgsWxRUY5Eo/slide-031.jpg]]

OCR text:

> AGENTICSPECTRUM·STARTWHEREYOUARE
> NoLLM MANUAL LLMas anatysislayer LEVEL1·ASSIST
> Oneserviceatatime xHoursperfinding xExpertrequired ndino LLMreadsprofiler Minutesperanalysis
> xStillserial
> Startheretoday
> RajatShah·AIPlatform,Netflix

![[assets/slides/CgsWxRUY5Eo/slide-032.jpg]]

OCR text:

> AGENTIC SPECTRUM > START WHERE YOU ARE
> WEVEL 1- ASSIST eae
> (Os CORRE ec eEL cael
> ; }


## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
