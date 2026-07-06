---
title: "Slides: User Signal Dies at the Retrieval Boundary - Sonam Pankaj, StarlightSearch"
category: "slides"
video_id: "Jx4ZFEAq6bY"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: User Signal Dies at the Retrieval Boundary - Sonam Pankaj, StarlightSearch

## Source Video
[User Signal Dies at the Retrieval Boundary - Sonam Pankaj, StarlightSearch](https://www.youtube.com/watch?v=Jx4ZFEAq6bY)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/Jx4ZFEAq6bY/slide-001.jpg]]

OCR text:

> User Signal dies at the g
> Retrieval Boundary.
> Me eo
> | aj
> Sonam Pankaj
> | CEO & Co ioe

![[assets/slides/Jx4ZFEAq6bY/slide-002.jpg]]

OCR text:

> What is an agent?
> E
> An agent is an LLM with agency: it reasons, invokes
> TOOLS to interact with the world, RETRIEVES from
> memory, and loops until the TASK is complete.
> 
> ia!
> il
> q

![[assets/slides/Jx4ZFEAq6bY/slide-003.jpg]]

OCR text:

> What is an agent?
> 
> An agent is an LLM with agency: it reasons, invokes |
> TOOLS to interact with the world, RETRIEVES from
> memory, and loops until the TASK is complete.
> 
> - | React Agent
> Tools/
> QR LLM ———~ Execute —— pRetrieval/ |
> ~~” websearch

![[assets/slides/Jx4ZFEAq6bY/slide-004.jpg]]

OCR text:

> } Retrieval is Static
> } Context Stuffing
> al
> |

![[assets/slides/Jx4ZFEAq6bY/slide-005.jpg]]

OCR text:

> The missing layer between evals and action
> Observability "Byals.
> |
> igThe GAP
> Your observability |. — =. ice ae
> stack captures every 1% rua |e =>
> - R Lcall, every LLM Oe Macanaee,
> [ompletion, and Sener
> i very exception.

![[assets/slides/Jx4ZFEAq6bY/slide-006.jpg]]

OCR text:

> g
> > It has no access to why yesterday's runs passed or
> failed. The eval signal dies in a dashboard.
> 7 > This is the missing layer: a system that consumes
> traces, absorbs eval outcomes, and converts both
> into retrievable guidance for future runs.

![[assets/slides/Jx4ZFEAq6bY/slide-007.jpg]]

OCR text:

> In practice, most agent memory frameworks have focused on user continuity: preferences,
> profile facts, conversation history, and long-lived personalization.
> chat experiences is not self-improving learning system for production agents. &
> Approach What tstores Rethecal signal Learra from outcomes |
> rants momen y “ tar that prem ate PEELE ge ™ Boe “
> \ Semper © tnoares 30 5 eet Potty reiyt ty nat Bet) Spt bee ee ete %
> P| _ URE oh etme genes am

![[assets/slides/Jx4ZFEAq6bY/slide-008.jpg]]

OCR text:

> ®
> Memory as Reasoning
> ere Reasoning
> “Chece ee before
> 
> - |
> 
> Z a; Static, Reranked based on usefulness
> 
> No Context Context is updated based on task
>  , ; No history learned from history

![[assets/slides/Jx4ZFEAq6bY/slide-009.jpg]]

OCR text:

> *reflect
> t-bench
> CPTS.4
> gentRTX

![[assets/slides/Jx4ZFEAq6bY/slide-010.jpg]]

OCR text:

> re ee
> non a .
> - i a
> oe
> ra wee ;
> 
> Py es abo an
> 
> : Tes
> 
> li | i

![[assets/slides/Jx4ZFEAq6bY/slide-011.jpg]]

OCR text:

> a . Se G qo
> See ee ee Lal
> ox
> : a e
> ory
> a roa
> an wo, H
> * an Es Prony
> I il
> a loons wy
> vies ames ~~ ws
> | .
> are
> 
> B :

![[assets/slides/Jx4ZFEAq6bY/slide-012.jpg]]

OCR text:

> Limitations
> Cold Start .
> Utility Drift
> ’ Review quality
> all Lambda

![[assets/slides/Jx4ZFEAq6bY/slide-013.jpg]]

OCR text:

> ANALINLLAN
> list_products,
> search_products_by_nase
> notns
> source/hon/sona
> AI/projects/skill-demm/.venv/bin/activate
> mf:-/projects/skill-demossource/hom/sonamAL/projects/ski1l-demo/.ve/bin/activate
> (sklll-demo)
> AT:~/projects/skill-demospythondemohuman_revlesr.py
> REFLECT_PRO3ECT_ID not set;using default'reflect-demo',Set it eplicitly for multi-tenant use

![[assets/slides/Jx4ZFEAq6bY/slide-014.jpg]]

OCR text:

> : ee os
> Sate a pwr, vee cae
> ween Pas
> q x
> ant
> Eee
> nt aed a
> Fl
> | f f
> Li p
> a
> io Ln ee | 7ORF «+ a

![[assets/slides/Jx4ZFEAq6bY/slide-015.jpg]]

OCR text:

> ree > i?
> : ee a nee mae Ot
> - 4. Agentbench
> toute a model's abiity to rea1on plan, and uve tock: over ertended, mit: step workflows, rather than prt meawring tate question
> 
> . afemoring accuracy
> 
> AgentRTx 61.3
> 
> . Memo 58 AgentRTX 9O8
> . RAG 47 osty 82
> 
> | | Baseline 35.7 Baseline 57
> 7 at a eee ~ . nd - ~~ Sa a ||
> ; wa sine) ©

![[assets/slides/Jx4ZFEAq6bY/slide-016.jpg]]

OCR text:

> list_pn
> oducts,
> search.
> fleitlnslefr toth
> Ce this file
> rwjects/siml-a
> python
> PO
> (e-E.

![[assets/slides/Jx4ZFEAq6bY/slide-017.jpg]]

OCR text:

> Se ee ee .
> z TO teense eee Cr, es
> Aaa
> One
> a Traces reflect: derno F - an
> i. he Tok
> a 5 te Fete bk gen cee ee : Ht toa v a
> ‘ aut
> Mare ay
> F y . hates pata, eee
> ne 3 beet ea geen, eee
> oo , aay eee Tere j
> a :
> 5 ad
> ; eee eee
> ey ner
> L bs ~ a cas rd 7
> '
> ‘ Lad ne | ,ONM uu + ;

![[assets/slides/Jx4ZFEAq6bY/slide-018.jpg]]

OCR text:

> a eee :
> a rr Ps Cs
> ere
> a :
> he a
> re
> ae Prd
> ere)
> 3 ;
> . at ra Ee ae see ct ad eee Ate
> cue
> 7 a Ln ee | | © en! /

![[assets/slides/Jx4ZFEAq6bY/slide-019.jpg]]

OCR text:

> a eo - :
> q or Ps ns
> :
> ane
> ie : SMerTor ars oe Cid
> Lene
> Oy rae t fa
> ee a te es ie oe ee .
> an Pur
> BG
> Pees
> q
> | a
> 7 iM en ee | »,OF » + a


## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
