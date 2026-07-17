---
title: "Slides: Respect The Process - Andrew Dumit, Watershed Technology Inc."
category: "slides"
video_id: "CLttOU7n6sI"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: Respect The Process - Andrew Dumit, Watershed Technology Inc.

## Source Video
[Respect The Process - Andrew Dumit, Watershed Technology Inc.](https://www.youtube.com/watch?v=CLttOU7n6sI)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/CLttOU7n6sI/slide-001.jpg]]

OCR text:

> docs.google.com
> RespecttheProcess
> Trustworthy coding agents ina domainfull ofexpert
> judgementcalls

![[assets/slides/CLttOU7n6sI/slide-002.jpg]]

OCR text:

> Sustainability is filled with
> judgement calls
> Questions like:
> - What are the emissions attributable to
> 1 bottle of wine?
> - Which method should be used to ‘
> allocate the emissions to various
> co-products?
> There are many ways to get to aright answer
> the wrong way and many right answers.
> erify the process in addition to the
> ra
> ve]
> ne

![[assets/slides/CLttOU7n6sI/slide-003.jpg]]

OCR text:

> Sustainability is filled with
> judgement calls
> Questions like:
> - What are the emissions attributable to 0.97 - 149 kg co2e
> 1 bottle of wine?
> - Which method should be used to ‘
> allocate the emissions to various Six experts with the exact
> eo-products? same data on the exact same
> There are many ways to get to a right answer bottle of wine
> the wrong way and many right answers.
> erify the process in addition to the
> a
> : ~ t Senxcaet a! (2020) “Uncertainty AL CA Anestimation of peac Utioner- related effects” 2

![[assets/slides/CLttOU7n6sI/slide-004.jpg]]

OCR text:

> dors googie com
>
> Our task: Updating os
>
> ehectrcty Someone Cotton pan Svighus oe
> complex graph data . | :
> Help our users edit complex graphs representing lepe recat penn trey
> supply chains
> Each graph is a DAG representing the flow of * ‘ ,
> materials and energy C ©
>
> &
> The graph is comprised of 1000s of nodes with rich Reckeons Sresest ee
> metadata describing the materials and processing at “ : 1
> each step ~~
> Derk veaeh
> we
>
> hi
> “4

![[assets/slides/CLttOU7n6sI/slide-005.jpg]]

OCR text:

> Our agent worked
> on one graph... meen
> When we first tried to solve °
> this task a year ago, it worked eat = na sre
> well enough ona single graph - . — '
> using custom built tools ee
>
> resiore trwpon =

![[assets/slides/CLttOU7n6sI/slide-006.jpg]]

OCR text:

> Our agent worked
> on one graph... Joe One Le
> When we first tried to solve - 7s, = Cee ee ee
> this task a year ago, it worked — oe = oT TE OT
> well enough ona single graph eee
> using custom built tools Toot, vw TU The
> - a. . voumi f tome = _ —-
> - conaee ee " = ue
> = - tee wee
> But absolutely broke when we Me TS ee
> tried to scale it up to many - .« : =
> graphs = LO
> eh _ —

![[assets/slides/CLttOU7n6sI/slide-007.jpg]]

OCR text:

> So, we naturally swapped in a coding agent
> Gives the agent the ability
> to delight
> &
> The agent can find clever ways to
> solve underspecified problems. create
> fancy visualizations. and answer
> related questions

![[assets/slides/CLttOU7n6sI/slide-008.jpg]]

OCR text:

> docs gers com
> So, we naturally swapped in a coding agent
> Gives the agent the ability The agent can explore and Flexibility and power to do
> to delight edit efficiently stuff outside what we
>
> * designed it for
>
> The agent can find clever ways to Loops over graphs. scripts to unpack We consistently find entirely new use
> solve underspecified problems. create and summarize node content. same cases via the new questions users ask
> fancy visualizations. and answer pattern of data exploration as agentic of the agent
> related questions data science

![[assets/slides/CLttOU7n6sI/slide-009.jpg]]

OCR text:

> But, unconstrained code is scary
>
> The agent will find The agent can gaslight Manual review of code is
> “creative” ways to solve users Saying it made edits not in our users
>
> every problem * wheelhouse
>
> Writing Python when we expect Agent claims it made edits to users When the agent is right for the wrong
> typescript, editing graph artifacts when it ran code that did nothing reasons, it's really hard to check it
> directly without lineage without reading the code

![[assets/slides/CLttOU7n6sI/slide-010.jpg]]

OCR text:

> The process # answer story is not new
> The Open Proof Corpus, Dekoninck and
> Petrov et al. 2026 “their reasoning often contains subtle logical
> 100% me Cottect Final Answer errors masked by fluent language, posing
> mm Correct Proof significant risks for critical applications.”
> 78% - Beyond Correctness, Zheng et. al. 2025
> 70
> 50% &
> “For every success story like the unit distance counterexample,
> 25% there are likely thousands of pages generated for each of
> these problems, which have led nowhere.”
> ae - Thomas Bloom on ErdosProblems.com, 2026
> 03 Gemint-Pro
> - 5 ‘ “72% of reward hacking episodes include
> ‘an LLM agent with access to unit tests 5k 5 :
> explicit chain-of-thought rationale,
> may delete falling tests rather than fix suggesting models often frame exploits
> the undertying bug. -
> ; ibleBench, Zh tal, 2025 as legitimate problem-solving.
> ~ Impossiblevench, £nong et. al. - Reward Hacking Bench, Thaman 2026

![[assets/slides/CLttOU7n6sI/slide-011.jpg]]

OCR text:

> dors geese came
> Our SDK as the only door —_
> definekditFunction, findNodesByNameExact, assert,
> setRate, editNode, type EditProducttonGraphState,
> } from ‘mnotersned: gragmagentagi;
> . . . . . export default defined dr tFuncet vont
> : Typescript SDK with all edit primitives the “cut elecericity. ard, saap.seeet |
> async (state: EditProductironGrapnState) => {
> agent needs to make changes const [mfg] = fundNadesBytionet xo t(
> state. graph nodes, ‘minsfocturing'):
> : Enforces which fields are editable vs. which const [electricsty) i«, fledNedestyNonet rock
> state graph nodes, ‘grid electeriity' iy
> . 7, const (steel) = findNodesByNane€ xact(
> are derived from other fields ROL GrSONLS “BEE
> : Guarantees that it emits objects we expect \ assertinfg && electricity Ak steet,
> . . “ Terpectst one of each tex) lod);
> : Requires teaching the agent how to use it
> State = setRate(
> state, mfg.identifier, clectricity. identifier, »;
> state = editNode(state, steel. identifier, {
> 1 stainless steel’ J);
> return stote;
> }
> v
> ee a a — ee

![[assets/slides/CLttOU7n6sI/slide-012.jpg]]

OCR text:

> Deterministic execution to guarantee process
>
> Even with the typed SDK as the entry point, we run-executorts
>
> only guided the agent towards our desired end
>
> etate Dineths agegt coe)
> i. Rotienigo |
>
> The real guarantee comes from final script that Detect conpficts)
>
> we orchestrate on agent completion ‘ = =
>
> The completion script calls the agent pRan agentedited code iy |
>
> generated code, validates the results, and send
>
> any errors back to the agent = Wanosecen oie: aie
>
> GER Glecte review artifact

![[assets/slides/CLttOU7n6sI/slide-013.jpg]]

OCR text:

> Deterministic execution to guarantee process
>
> Even with the typed SDK as the entry point, we run-executorts
>
> only guided the agent towards our desired end Cie coe
> _———
>
> The real guarantee comes from final script that Emissions Report
>
> we orchestrate on agent completion .
>
> The completion script calls the agent 50 7 749 tet
>
> generated code, validates the results, and send
>
> any errors back to the agent i c dap out Sitarute ee |
> Oreste (eview artiact ma

![[assets/slides/CLttOU7n6sI/slide-014.jpg]]

OCR text:

> Deterministic execution to guarantee process
> 2.01 - ction
> Even with the typed SDK as the entry point, we - .
> only guided the agent towards our desired end | |
> state
> The real guarantee comes from final script that Er
> we orchestrate on agent completion ‘
> The completion script calls the agent 5 a
> generated code, validates the results, and send a
> any errors back to the agent
> Cod Fad Derg
> a a ca .

![[assets/slides/CLttOU7n6sI/slide-015.jpg]]

OCR text:

> : doce.qoogie.com
> Hillclimbing
> within this
> harness re) re)
> 43% > 92%
> All the typical approaches
> were still effective A Se e ie r 2g cy
> - Prompt improvements :.
> - Few-shot examples Improvement on
> ~ Making tools better
> fit-for-use '
> - Breaking the task down internal eVa Is
> - Teaching the agent some
> ge expert judgement
> a —E 7

![[assets/slides/CLttOU7n6sI/slide-016.jpg]]

OCR text:

> In a domain full of judgement calls, respect the process
> request
> agent writes Cay
> free code CS)
> e Lv
> typed SDK reject - retry
> + lint
> v
> Vv
> v
> valid - traceable - replayable
> ee = .

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
