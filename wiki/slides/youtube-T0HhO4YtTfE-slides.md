---
title: "Slides: AI System Design: From Idea to Production - Apoorva Joshi, MongoDB"
category: "slides"
video_id: "T0HhO4YtTfE"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: AI System Design: From Idea to Production - Apoorva Joshi, MongoDB

## Source Video
[AI System Design: From Idea to Production - Apoorva Joshi, MongoDB](https://www.youtube.com/watch?v=T0HhO4YtTfE)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/T0HhO4YtTfE/slide-001.jpg]]

OCR text:

> @
> 
> >
> 
> @ Mongons

![[assets/slides/T0HhO4YtTfE/slide-002.jpg]]

OCR text:

> a
> i
> So, how will we “Vibe Code” in prod?
> Forget the code exists, but
> . ret anetere) tlAle ae ahaa] £01 Die
> 7 NOT that the product exists!
> RS enna ae
> » S ca Ta
> eared SS MeEIPR ROR Ge 10185.F 1000: Coe 8.0 BUC LL
> rs roles) et ite eal
> “if vad can ComMmuUricate. yOu Can program ©
> ce Sear Grove, Qpenal

![[assets/slides/T0HhO4YtTfE/slide-003.jpg]]

OCR text:

> f
> Specs are the new code
> 20
> a
> =»

![[assets/slides/T0HhO4YtTfE/slide-004.jpg]]

OCR text:

> Product System Design Evaluation Production
> Requirements and Monitoring Readiness
> taentify the business ere eek orca Define system Opt mize for accuracy
> oife)snerns) and retrieval techniques —— guarcrais
> & i idertify your Se'ect system Define offline Oot:mize for cost ard
> constraints architecture and tecn evaluation metr cs fehtel eng
> B | Satelal¢
> i ; Define tne role of Al Deterrune the UX and Define onine Optimize for rouability
> i aoe Hela@l SG aMOrerS re (arrosrel@halor aaa tell aan
> Define success Metrics

![[assets/slides/T0HhO4YtTfE/slide-005.jpg]]

OCR text:

> )
> ane g
> > mn ;
> Health insurance claims review

![[assets/slides/T0HhO4YtTfE/slide-006.jpg]]

OCR text:

> Background
> Background
> Health insurers and health funds around the world employ medical reviewers to assess
> ; whether a requested treatment, procedure, or medication is covered under a patient's
> 
> Pf policy. This requires cross-referencing clinical documentation, coverage policies, clinical
> 
> guidelines, and patient claims history. It is one of the most administratively intensive
> « P| ; roles in healthcare operations.
> ee
> 
> What we are building
> We are building an internal claims review system for a fictitious health insurance
> company called MDB Health. This system is used by medical reviewers to assess and
> adjudicate claims. The external-facing system through which healthcare providers
> submit claims and receive feedback on outcomes is out of scope.

![[assets/slides/T0HhO4YtTfE/slide-007.jpg]]

OCR text:

> )
> Retrieval Augmented Generation (RAG)
> 34 SS ened
> i ay a aie Aare se ——=> Answer
> [oar

![[assets/slides/T0HhO4YtTfE/slide-008.jpg]]

OCR text:

> a
> Al Agents
> Tools Memory
> " ri 8
> ry. a
> a ; = %
> - Se MS 4<so-  est)
> Sd
> raat
> ry
> A
> a9 ab)

![[assets/slides/T0HhO4YtTfE/slide-009.jpg]]

OCR text:

> .
> Controlled flows?
> & she etd. > Acton 2
> a 7 =
> a! 2 ae Ni) LLA Call 2

![[assets/slides/T0HhO4YtTfE/slide-010.jpg]]

OCR text:

> 0
> ‘Tech stack decisions
> OO
> Data | prcinc 8 4 |
> é \ processing rere
> P a Hosting aws ra V | |
> > a and inference
> Foundation models A\ Gy) ‘ alien O Meta |
> 7 y

![[assets/slides/T0HhO4YtTfE/slide-011.jpg]]

OCR text:

> .
> Tech stack decisions contd...
> \ Fine-tuning ’ 7 rs
> af 2 Orchestration | Sa io POLY A, 8 oo?
> >) Frameworks _ . on
> ae —‘\
> ; a
> Embeddings | ()
> and retrieval 4

![[assets/slides/T0HhO4YtTfE/slide-012.jpg]]

OCR text:

> 7
> Define system guardrails
> Guardrails define the boundaries of acceptable inputs and outputs.
> «x! a
> ~ _

![[assets/slides/T0HhO4YtTfE/slide-013.jpg]]

OCR text:

> if)
> Define system guardrails
> Guardrails define the boundaries of acceptable inputs and outputs.
> t
> a | :
> mn aleienl Oleraeren
> A P Caen RETARSi ez O1bh re) ME MOlEADI TOLER SLOI ES H Invalid. mcorrect om harmfu outputs
> o ; . A
> ~ —
> |
> 4
> qd
> i
> I
> '
> i
> i

![[assets/slides/T0HhO4YtTfE/slide-014.jpg]]

OCR text:

> ()
> oF co . ~
> i r is e » ons f
> Optimizing for accuracy
> Technique What it involves
> ; | Prompt eng reenng Wrote clear and well-stroctured prompts
> FY EXetsaimnL aay Progress ve disclosure of eformation fo agents
> a 2 ; OlTclarmelon nn irz4iileal Rewrite or cecomoase queres for better retmeval ar generation
> a , ,
> Rerark rg Reorder retreved documents py relevance
> Compactor Summarize or remove content from the LLM’s contead wenGow
> Memory managemer* Persist information across sessions

![[assets/slides/T0HhO4YtTfE/slide-015.jpg]]

OCR text:

> ©
> a ‘ as ra a
> Key takeaways
> e = =Think deeply about your product requirements before having AI generate code.
> ba 7 e =6Treat business and performance constraints as inputs to design, not afterthoughts.
> a’

![[assets/slides/T0HhO4YtTfE/slide-016.jpg]]

OCR text:

> - =
> na
> oY é
> LIN enters) ees BLE
> —————
> Ps eee


## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
