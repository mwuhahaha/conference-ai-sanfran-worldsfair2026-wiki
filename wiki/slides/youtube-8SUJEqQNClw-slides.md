---
title: "Slides: Agents vs Workflows: Why Not Both? — Sam Bhagwat, Mastra.ai"
category: "slides"
video_id: "8SUJEqQNClw"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: Agents vs Workflows: Why Not Both? — Sam Bhagwat, Mastra.ai

## Source Video
[Agents vs Workflows: Why Not Both? — Sam Bhagwat, Mastra.ai](https://www.youtube.com/watch?v=8SUJEqQNClw)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/8SUJEqQNClw/slide-001.jpg]]

OCR text:

> INNOVATIONPARTNER
> aws
> PLATINUMSPONSORS
> Graphite
> WWindsurf
> MongoDB
> daily
> augment code
> Workos

![[assets/slides/8SUJEqQNClw/slide-002.jpg]]

OCR text:

> Wholam Why I'm giving this talk
> AIE Mastra is theleading Typescript agent framework Users use our agent andworkflowprimitivesfor differentuse-cases....and sometimestogether
> Mastra
> SamBhagwat TheTypeScriptAlFramework
> Author,Principles of Prev:Gatsby co-founder BuildingAl Agents Founder/CEO,Mastra.ai samonX/Twitter s npm create mastra
> github.com/mastra-ai/mastra
> Word'sFair

![[assets/slides/8SUJEqQNClw/slide-003.jpg]]

OCR text:

> AIE In December Anthropic wrote a great blog post
> that canonically defined agents and workflows
> github.com/mastra-ai/mastra
> Microsoft smol?
> Worid'sFair

![[assets/slides/8SUJEqQNClw/slide-004.jpg]]

OCR text:

> AIE released a paper In April OpenAl on the topic guideto Apractical buildingagents
> github.com/mastra-ai/mastra
> Microsoft smolo
> World'sFair

![[assets/slides/8SUJEqQNClw/slide-005.jpg]]

OCR text:

> @openai
> AIE
> Hot Take #1:
> HELLO
> my nameis
> ThatGuy
> Don'tbe That Guy
> github.com/mastra-ai/mastra
> Microsoft
> smol?
> World'sFair

![[assets/slides/8SUJEqQNClw/slide-006.jpg]]

OCR text:

> Sometimes That Guy works for a
> FAANG type company in a public
> facing role
> Then the rest of us are really in for it
> _ aws
> | ara) | name

![[assets/slides/8SUJEqQNClw/slide-007.jpg]]

OCR text:

> “Use the platform” was a codeword for
> why React was wrong and anti-web
> 4 aws
> == nana

![[assets/slides/8SUJEqQNClw/slide-008.jpg]]

OCR text:

> AIE
> Some of our users *loved* this.
> But many folks didn't
> github.com/mastra-ai/mastra
> Microsoft
> smol°
> World'sFair

![[assets/slides/8SUJEqQNClw/slide-009.jpg]]

OCR text:

> AIE SowhenIseeAPls const graph =new MessageGraph() 1/Langgraph.js
> like this, it gives me (bad) flashbacks.addEdge(“nodeB"，END).addNode(“nodeB"funcB).addEdge("nodeA"，"nodeB").addEdge(START,"nodeA").addNode("nodeA",funcA) nodes edges
> github.com/mastra-ai/mastra
> Microsoft smol?
> World'sFair

![[assets/slides/8SUJEqQNClw/slide-010.jpg]]

OCR text:

> AIE
> Or like this:
> const [notifyTeam,assignPlan]= await Promise.all（[
> step.run("notify_team",async（)=>{
> return{notified:true};
> step.run("assign_default_plan",async()=>{
> return{planId:“starter"};
> github.com/mastra-ai/mastra
> Microsoft
> smol?

![[assets/slides/8SUJEqQNClw/slide-011.jpg]]

OCR text:

> AIE
> Or like this:
> const [notifyTeam,assignPlan]= await Promise.all（[
> step.run("notify_team",async（）=>{
> return{notified:true };
> step.run("assign_default_plan",async()=>{
> return {planId:“starter"};
> github.com/mastra-ai/mastra

![[assets/slides/8SUJEqQNClw/slide-012.jpg]]

OCR text:

> A Pattern Language. aE eae
> ‘Towns -Bedings ‘Constroction L: as , et =
> ee } is
> a x ar G ae . .
> Ay .
> <a
> 0 erm — a -
> Sara Ishikawa - Murray Silverstein - al
> Miax Jacobson - Ingrid Fiksdahl-Kiag
> aws
> ~~] ~ |

![[assets/slides/8SUJEqQNClw/slide-013.jpg]]

OCR text:

> a . |
> How the WorkOS folks put it in their a ar
> Mastra workshop yesterday:
> Popents are stateaat A ent ten teat Dar LAs
> ce renner
> e Make cies sous hasedion context e Wa cdate mpouts Gutpats with Zo
> esi tis te mn ete Sasas Cs ie Mey clever)
> i Ot ea Cua oe CO Cee Ce Tr, cea 18 AD Gaara
> irae rt LAL ed a Pe SOs ro en ae me Ce eee)
> an a Microsoft = (aU°

![[assets/slides/8SUJEqQNClw/slide-014.jpg]]

OCR text:

> Here’s another way to put It:
> (1) Agents are a turn
> based game.
> (2) Workflows are a rules
> engine for your tech
> Ugeto1
> ; sick ES 10 Uh

![[assets/slides/8SUJEqQNClw/slide-015.jpg]]

OCR text:

> Here’s another way to put It:
> (1) Agents store threads of messages and
> continuously interact with users
> (2) Workflows can have branching. parallelism,
> conditions. loops, can suspend/resume, etc
> a, aws
> ! 7]
> ee

![[assets/slides/8SUJEqQNClw/slide-016.jpg]]

OCR text:

> AIE At the end of control
> justa tradeoff theday it'sall
> multi-agent agent workflow
> github.com/mastra-ai/mastra
> Microsoft smol?
> Word'sFair

![[assets/slides/8SUJEqQNClw/slide-017.jpg]]

OCR text:

> Rules of agents + workflow composition
> (1) Agents have tools
> 
> (2) Workflows have steps
> (3) An agent can be a step
> (4) A workflow can be a tool
> (5) An agent can be a tool
> (A\ A workflow can be a step
> 
> i aws
> 
> ee = | See

![[assets/slides/8SUJEqQNClw/slide-018.jpg]]

OCR text:

> const researchAgent nev Agent（{
> nane:'research-agent',
> Lnstrocttons:You are a research agent that analyzes
> Agent supervisor
> questtonsopenai(gpt-4'),
> const summaryAgent-new Agent（{
> nase:'sunary-agent',
> instructlons:You are a su
> Supervisor
> model:openal(gpt-4).
> AIE
> const researchTool=createTool（{
> id:'research',
> execute:async（tnputData））{
> constresult=await researchAgent.0
> rate(inputData.query);
> return{text:resutt.text）;
> F.
> const summaryTool=createTool（{
> ld:*summarize'
> execute:async（{inputData}）{
> const result -awalt summaryAgent.generateLnputData.text);
> return{text:Tesult.text）;
> export const supervlsorAgent=new Agent（
> hane:'supervisor-agent'.
> nodel:openal('gpt-4'),
> research and summarization tasks.
> tools:[researchTool,summaryTool],
> aws
> Word'sFair

![[assets/slides/8SUJEqQNClw/slide-019.jpg]]

OCR text:

> Workflowastool
> export const agent = new Agent（{
> name:'Agent',
> instructions:Ask the user for
> AIE
> their location,check weather，
> and plan a trip，
> model:openai('gpt-4o-mini'),
> workflows:
> checkweather,
> planTrip
> memory,
> github.com/mastra-ai/mastra
> Microsoft
> smol?
> World'sFair

![[assets/slides/8SUJEqQNClw/slide-020.jpg]]

OCR text:

> nustru
> World's Fair AlEngineer

![[assets/slides/8SUJEqQNClw/slide-021.jpg]]

OCR text:

> AlEngineer
> World's Fair

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
