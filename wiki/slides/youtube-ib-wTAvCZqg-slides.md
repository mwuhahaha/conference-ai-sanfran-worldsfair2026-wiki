---
title: "Slides: Architecting and Testing Controllable Agents: Lance Martin"
category: "slides"
video_id: "ib-wTAvCZqg"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: Architecting and Testing Controllable Agents: Lance Martin

## Source Video
[Architecting and Testing Controllable Agents: Lance Martin](https://www.youtube.com/watch?v=ib-wTAvCZqg)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/ib-wTAvCZqg/slide-001.jpg]]

OCR text:

> aWws
> eee)
> § MongoDB o Cloud Ne€O4Y)

![[assets/slides/ib-wTAvCZqg/slide-002.jpg]]

OCR text:

> WP
>
> ae)
>
> Py a

![[assets/slides/ib-wTAvCZqg/slide-003.jpg]]

OCR text:

> ED Langcnain
> LLM applications follow a contro! flow
> Step 1 Step 2
> Start —»> 6, —> (() —> et
> ae
>
> So Nites Jen vekipeda org win Comrat flo
>
> . nd
> | a
> , LC
>
> "

![[assets/slides/ib-wTAvCZqg/slide-004.jpg]]

OCR text:

> C—O
> 8 e (o ee er emerncrrenterrat CRM 3 wre emma ar aoe 2.8 _ 2). 00 © iia
> aS ES . —- en. @
> O -—
> m Architecting ¢ testing rettoble ogents
> . Sohere tngee ong hen
> ¥ TT \<le en
> wh
> i aws
> , i Tet?

![[assets/slides/ib-wTAvCZqg/slide-005.jpg]]

OCR text:

> a © —— — ~ Ca
> o 2 BS yeree we iersee® ot we “ « 00 © Qi
> (is): [from IPython.display import Image, display
> class GraphState[TypedDict}:
> Represents the state of our graph.
> Attributes:
> question: question
> generation: LLM generation
> search: whether to add search
> Gocuments: List of documents
> wee
> question: str
> generation: str
> search: str
> documents: Lististr)
> steps: Lististr!
> |!
> 7 f aan ,
> i s980Q +: see ww
> and | aWws
> ' ~ eel

![[assets/slides/ib-wTAvCZqg/slide-006.jpg]]

OCR text:

> WwW OuUargcren
> Retrieval is not guaranteed, reasoning harder than retrieval
> Ta ae ag sing Cc) Int ate tare inet 8 te stents fats te Sar
> vad shal eal teicher athena ee *. or “isaac VO ++ tae ewtee net
> - wes, Weeds 0} g
> gue weoce @ | OO em teen
> } words @ 4 Nereres stare or a
> i . heeds #5 58
> z | = Si nenve a6 .
> 5, berets @ §
> 2 erste @ > ia toe eee
> “ e Mreme ae ae
> é wma inte nae So nereresessess 300 24800 688972400 EOD 17000 ohne eminem mares
> Ups cyouty be UinyyYOGhe«
> a A bllps biog langcha'n dev-mult-negdie-in-a-haystacs.
> a
> - aws

![[assets/slides/ib-wTAvCZqg/slide-007.jpg]]

OCR text:

> wm OLangcnan
> Challenge may be recency bias in LLMs
>
> A likely culprit for this phenomenon is a mismatch between the task LLMs are trained on and context-augmented
> generation tasks. Among the documents typically used to pre-train LLMs such as web pages, books, articles and code,
> the most informative tokens for predicting a particular token are typically the most recent ones. During pre-training,
> this induces a leamed bias to attend to recent tokens. In addition, the rotary positional embedding (RoPE) scheme used
> in the open source models we investigate has an inductive bias towards reduced attention at long distances [27] that may
> make it even easier for these models to learn to attend preferentially to recent tokens. Extreme recency bias is not a good
> prior for context augmented generation tasks where far away tokens may, in fact, contain very relevant information.
>
> ay Reis ak aa a et
> |
> A aiid an Mi ft @
> ; gw Microso
>
> A

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
