---
title: "Slides: Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry - Abed Matini, Ogilvy"
category: "slides"
video_id: "Akm1sqvWG4A"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry - Abed Matini, Ogilvy

## Source Video
[Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry - Abed Matini, Ogilvy](https://www.youtube.com/watch?v=Akm1sqvWG4A)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/Akm1sqvWG4A/slide-001.jpg]]

OCR text:

> reer . : ee ee ee ee e -n -@ ' rs , :
> s “te ©. a a ec ee + ae
> sa] 4 , ae |
> j 7 as | ister entrid
> e e e
> Bypassing the Multimodal Tax ep
> Framework-Free Hybrid RAG, Raw SQL RRF, and Live UI Telemetry | - er ; vee — , ,
> Fe Brtstn i ae
> ered tee Carib Oean eres aoa \ py} :
> Al Engineer World's Fair 2026 - Online Track ; 7
> Y

![[assets/slides/Akm1sqvWG4A/slide-002.jpg]]

OCR text:

> ‘ (© ©. : Cn ee * | ao
> . ere CORY :
> 
> Two problems every document chatbot hits
> 
> Paying to read documents twice Search split across too many tools cee umateditigy owe
> 
> Cloud vision APIs charge +500- 1,000 tokens per Good answers need meaning (vectors) and exact Se pn et a cated a
> 
> Paye just to tuna PDE into text before a user asks words (keywords). Teams often run a veetor DB, a ay HALE oes : ‘
> 
> anything. A 200 page manual can cost 100k+ tokens search engine, and wrapper code to combine them a Le = an . r a a ,
> 
> at ingest, and tables still break. : so when results are wrong, you fix contig files, not ue
> 
> query. WO ay ee
> This talk: parse locally - one Postgres database - hybrid search in plain Python
> a.. %,
> %,
> a an
> h @

![[assets/slides/Akm1sqvWG4A/slide-003.jpg]]

OCR text:

> rs A a : an 7 r : a %% te cr, a 8 a
> . is corre a eee si bak Z ce cic on a . ad rc ee ° | ee 2
> Reker Rte Been ok Gallet Bete Loo Rime acd oe hd om oe So.
> 
> 1 AIpSION, x
> 
> Th VERVIEW X
> 
> m VOLUNTARY ALAMIED ESEPTOUMENT x
> 
> IV. ROUAT ESECLOY MES TOPRORTE NITY x
> 
> Vv DOLE AGAINST WORKFT AGT HARASSMENT XN
> 
> VIE SOUT STION \
> 
> 7 VI POL KS OF WORK ATTENDANCE AND IPL NCEUALTDD Xv
> No Hemursat Work \
> 
> Bo Attendances anit an taatty x
> 
> C Overtime ‘
> 
> VIL EMPLOYMENT BOLICIIS AND PRACTICES \
> 
> Ao Deheuteect ferme x
> 
> TX OSETION DISC RIPTION AND SALARY ADMINISTER ATION, x
> 
> N20 WORK REVIEW x
> 
> Mt EC ONOSTC HENPREIN SADENSER ANCL x
> 
> A Health Tite Iesiranee \
> 
> Bo Saal Neounts Moda are: Mee and ‘
> 
> (Workers Coney reales ana Ura mplos icant Insure x
> 
> 1) Retirement Blan ‘
> 
> Fo Tay Oxterted Annet Flan \
> 
> NEL LEASE RENFITIN ANOTHER SORK INMICIES x
> 
> A Helsavs x
> 
> Ko Naoto ‘NY
> 
> © Sab Tears Ww
> 
> t De teearat Deve AY
> 
> Bo Miatinany Ceaye uw
> 
> Fo dan Dats Ww
> 
> 4. Parental Leave Ww
> 
> HE Beteavement Leave aa
> 
> 1 Patented Persona: Leave aa
> 
> 1 Sevety Weather ( ceiditeates wN
> 
> Ko Mevorge and Goaterercrs NN

![[assets/slides/Akm1sqvWG4A/slide-004.jpg]]

OCR text:

> ~ & A a oi Ee 2 . 5 Re a es q cA g A a
> g : f | * @# : © e@ a ui
> Upload document
> Upioad screenshot or image
> Knowledge base heen
> Filename Strategy Crunke Sutus Uplosdes Actnns
> Sade Cp bee Teng 2 AC thee Mptp EON ChueesiG) Archies = Detese
> Te ney tote tae + Aether hn Chums.) Aree Oolote
> BET agate Meg anit Tee bon Fier teare a AC TINE Frere Chunks) Aves Delete
> perpen Dice pe test bee at cet perinsge te act td Hales Chunes 12h Arctwre — Dotete
> : . . é see twat

![[assets/slides/Akm1sqvWG4A/slide-005.jpg]]

OCR text:

> ~ & . a z . . ee 2 rs e 8 a
> 5 . F 5 er Mt se 8 ae
> Sample Employee Handbook - National Counci of Nonprofits pdt
> a
> 
> Bore ps eattet ent te Menon Lee Sofa ee tat
> wr TARE OF CONTENTS toc
> 
> .
> 1 wero ao
> tot abs ‘
> CR A TM ayes v
> Be UM URE nate 1
> LO RMI ARAN Any , <
> yy TABLE OF CONTENTS: ear
> Hite Pay
> > TABLE OF CONTENTS ear
> 
> «
> CMON Ody gat we kat te
> 
> we ON bide
> EE ERS ONE 2h oe ate
> vba We tN
> FANT Pee tsb
> i a ae ee: a: ae ea

![[assets/slides/Akm1sqvWG4A/slide-006.jpg]]

OCR text:

> pata :
> : an
> a: s,m
> < 9 : 5 °
> a 8 5 4 es °
> Ll * : Cc
> wo bs CY
> ma ; o. . rf
> Po L] cr
> - an e
> 8. 5 CY
> oa D ero D ” gs
> . S él Cy
> - 5 Q 5 is
> me] r) 7 5 , rl
> ro] s °
> Ca Zz ne , e
> an
> Stan nee DUR Ea EER ay sentence z acThe Roatan, Cruny.6) 0 Arce OD
> SET Meratine Stes ate Se act me Ter nea 3 active nea Chunns 4) Arce Detone, 7

![[assets/slides/Akm1sqvWG4A/slide-007.jpg]]

OCR text:

> FACS FAQsHe Langfuse MorosoWx heading-fa
> C localhost:3000/project/cmphbwcwb0006cosw74bs7wlc/traces/f046bc3ee86d-43d0-b609-(54f2d2eea277timestamp2026-06-19T12%63A17.. ☆
> WPP Boomarks 8 Free Pictures Ogy W st PGPMS Websites Webste Test Decoupled RAG Tutoriab ATend
> Langfusev2.95.11055 TraceDetail lean-doc-chat/chainlit-tracking/Traces/1046b3e-e66d-43d0-b609-154f2d2eea27 Private
> Tacing Uer ID:idget-aonym
> Sessions Generations Traces drect Tree E Timeine
> users Scores Models 6/19/2026≥17:45PM mafaq-agentic-chat Annotate anepopp+ Prevew Scores TRACE faq-agentic-chat
> Promps Pretty JSON
> Datasets 6
> Seethelatestreleases Star Langfuse andhelpgrowthe ppsydouequea
> Langtuse 29k indicatesplannedmaintenance activities will take place during this time. es.theprovideddooument states thatMaintenance windowis from 600PM(18:00) to 1200 AMmidnight(00:00Sunday，21June)This
> Feedback Metadata
> Settings oddrs@ Docs model:qn2.5:e.5b-lestrct top_k:2 sourcesi[- 0:*5creenshot 2826-06-19004158.png 1:*5crenshot 2026-06-19004158.png
> Abed Matini agemt_mode:false t.tvoe:rat"

![[assets/slides/Akm1sqvWG4A/slide-008.jpg]]

OCR text:

> FAOS
> FAQs-He
> Langfuse
> Maostx
> 3heading-fa
> localhost:3000/project/cmphbwowb0006cosw74bs7wlc/traces/i046bc3e-e86d-43d0-b609-f54f2d2eea277timestamp-2026-06-19T12%3A17.
> CwPPBoomarls
> Free Pictres
> Ogy
> MM
> A
> PGMS
> Websites
> Wetsite Test
> Decoupled
> RAG Tutorial
> PILY
> Langfuse v2.95.11OSs
> lean-doc-chat/chainlit-tracking/Traces/f046bc3e-e66d43d0-b609-(54f2d2eea27
> TraceDetail
> Private
> Tacing
> Uer ID:dy
> Traces
> Sessiors
> drect
> Tree Timine
> Generations
> Scores
> Prevew
> Scores
> Models
> TRACE faq-agentic-chat
> Users
> Is there any maintenance plan for this weekend?
> Prompts
> Datasets
> Output
> indicatesplannedmaintenance activities will take place during this time.
> Star Langfuse
> Seethelatestreleases
> andhelpgrowthe
> Metadata
> communityonGitHub
> Langtuse
> 1-e
> model:"qven2.5:e.Sb-lastruct"
> top_k:2
> sources:[-
> 0:5cre6nshot2826-86-19004158.pg
> Feedback
> 1:*Screenshot2026-06-19004158.prg
> Settings
> eeettype:"chat"
> agent_mode:false
> Dos
> raE.chnks：2
> history.turts:2
> duratlon_:254
> oodrs@
> AM
> Abed Matini

![[assets/slides/Akm1sqvWG4A/slide-009.jpg]]

OCR text:

> a es fi ae Pars » 48 , gi ee A g 8 :
> 7 nn © ee rot Ms ke B Be te
> FAQ Asustant a
> retest a tiitaetia at vaseedia *
> Ob yO) _—
> se r a) si Rese ©
> Ln hk ; rat _
> I be chat seyyee aE ye ee
> Po 8 cedar engines Gi ren sat
> . SPF a i ee
> a! Sa ar Pe
> : = =a.) poe meters
> a B ae ee
> [a] : a
> c e e s
> any Ea
> https: www linkedin.com in mation iD med
> seat hey Steememed POLE 00 19 ODE E ony
> ‘ aa — .

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
