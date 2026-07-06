---
title: "Slides: Stop Using RAG as Memory — Daniel Chalef, Zep"
category: "slides"
video_id: "T5IMo5ntyhA"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: Stop Using RAG as Memory — Daniel Chalef, Zep

## Source Video
[Stop Using RAG as Memory — Daniel Chalef, Zep](https://www.youtube.com/watch?v=T5IMo5ntyhA)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/T5IMo5ntyhA/slide-001.jpg]]

OCR text:

> aWws
> 
> ee)
> @®Graphite W Windsurf 4) MongobB
> Mdaily £3augmentcode WorkOS

![[assets/slides/T5IMo5ntyhA/slide-002.jpg]]

OCR text:

> cme
> One Size Fits None
> Why Memory Must Reflect Your Business Domain
> p- 7
> a a a Microsoft @yr{?

![[assets/slides/T5IMo5ntyhA/slide-003.jpg]]

OCR text:

> entityfields,
> EntityType,
> }from"egetzep/zep-cloud/wrapper/ontology"
> export constfinancialGoalSchema:EntityType={
> description:"A specific financial objective the user wants to achieve."
> fields:{
> goal_type: entityFields.text(
> "Type of financial goal (emergency_fund,house_down_payment,retirement,vacation, debt)
> AIE
> target_amount:entityFields.float（"Target dollar amount for the goal"),
> priority:entil
> lds.text（"Goalpriority level （high,nedium,low)"),
> export const expenseCategorySchena:EntityType ={
> fields:(
> category_name: entityFields.text(
> Name of expense category (housing,food, transportation，entertainment,utilities,shop
> monthly_spend:entityFields.float(
> "Average monthly spending amount in this category
> optimization_potential:entityFields.text(
> "Potential for reducing spending in this category （high,medium,low,none)
> export const debtAccountSchema:EntityType={
> description:"A debt obligation that impacts the user's financial health.
> fields:{
> debt type:entityFields.text(

![[assets/slides/T5IMo5ntyhA/slide-004.jpg]]

OCR text:

> bear
> Daniel Chaief
> Zep Al
> danielégetzep.coa
> ABSTRACT
> We imruduce Zep. a novel memory layer service for Al agents that outperforms the current sate:
> of-the-art system, MemGPT. sn the Deep Memory Retrieval (DMR) benchmark. Addivonally, Zep
> 2% excels in more comprehcauve and challenging cvaluatwoas than DMR that better reflect real- works
> coterpoe use cases, While curtng retneval-augmentied gonctanon (RAG) frameworks for large
> language model (11M -hased agents arc limited to statec document retneval, cntcrpnse applicapoas
> demand dynamic Loowledge integraioa from diverse wurces including ongoung cuavenations and
> buunews data Zep addresses this fundamental lmitabon through its core component Graplnty—-a
> bs, lemporally-aware knowledge graph engine that dynanucally syntheuses both unstructured conver:
> Senora) data and structured buvness dala while masntaining hivioncal relavonships. In the OMR
> benchmark. = hoch the MemGPT team eusdinhed as ther primary evaluation meine. Zep demon-
> strates wiperwe performance (94.4% +0 93.4%). Beyond DMR. Zep's capabalues are farther vali.
> dated through the more challenging LongMcmi:val benchmark, which better reflects enterpnse use
> sasen through compiles temporal reasonang Lav Ja Gus evalusbon. Zep actueves substantial rewults
> lex with accuracy improvements of up to 15.5% while umultancoud) reducing response latency 5)
> 90% compared to baseline implementations. These resulls are parbcularly pronounced in caterpnse-
> snbcal Lasks such at cfoss-sesucn anformation sy athesss and long-term contest maintenance, demon-
> strating Zep’s effectiveness for deployment sn real-workd applications
> te iy a ty
> D ‘i a
> ; https://ze.. “te .. er
> f 2
> A ‘ fy F
> = 5 => Sd
> lanl
> a ea
> -


## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
