---
title: "Slides: Teaching Coding Agents to do Spreadsheets - Nuno Campos, Witan Labs"
category: "slides"
video_id: "HEFSExa0xl0"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: Teaching Coding Agents to do Spreadsheets - Nuno Campos, Witan Labs

## Source Video
[Teaching Coding Agents to do Spreadsheets - Nuno Campos, Witan Labs](https://www.youtube.com/watch?v=HEFSExa0xl0)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/HEFSExa0xl0/slide-001.jpg]]

OCR text:

> RITnNem Gelert neaace
> {COMERS GLEN OKCICKTETG
> _ i SA eel a 7
> a rf Leet ed
> bal » r — a
> i
> ’ il
> os
> a i
> =

![[assets/slides/HEFSExa0xl0/slide-002.jpg]]

OCR text:

> Ome
> — 4months, multiple architectures, and many dead ends
> rare — What mattered most: replacing 15 discrete tools with one REPL
> bd *
> are
> * bd
> a ad
> a
> | Al Engineer |
> aU lag

![[assets/slides/HEFSExa0xl0/slide-003.jpg]]

OCR text:

> The problem ce
> ATU DAE Ta -1 xara cn Lom Oreos e]i a] o1 CS 1a ke .
> COOLANT SREB
> Pane o
> bd bd
> An LLM sees: 10.000 cell values.
> ‘ P ee a ee ee Ch Meee be Beat
> a ones Pee h ee CMM (Olah DETOUR Cara ee Cr . woe tee ee
> ;
> Py
> Al Engineer
> Seo) d 3

![[assets/slides/HEFSExa0xl0/slide-004.jpg]]

OCR text:

> One dead end
> Three specialized agents:
> cod - : ape
> as |. Block discovery — identifies workbook structure
> * * 2. Edit agent — S-step process: disambiguate. define end state, plan.
> a cd ;
> * rao cr@U | Comm eB
> 3. Question agent — answers questions
> Key finding: Rigid architectures don't win
> a.
> Al Engineer
> EUROPE

![[assets/slides/HEFSExa0xl0/slide-005.jpg]]

OCR text:

> More dead ends
> cooigeeren erator) Why it failed
> a * & TSV views Lost formatting and structural context
> * *
> arose |
> ‘ SO] Mec tanns Flat tables didn't capture visual structure
> *
> ans
> peenitem cele) Too verbose, consumed too many tokens
> DOT graphs Useful for analysis, not for interaction
> Pelee ot ms LUM struggled with the syntax
> None of them worked as a general purpose representation — but two informed whatcame next
> s
> a
> Al Engineer
> Sele) a 3

![[assets/slides/HEFSExa0xl0/slide-006.jpg]]

OCR text:

> STR ost eRe U Cala
> Before (10 15 tool calls):
> Pn 3 , Pe og oe Tee ., a ;
> a x 7 to aes af 7 a ae o oo
> * bal bon BD ca an mg eg
> * ad Ss +L e ee fin a ee
> * ra *
> After (1 tool call):
> Engineering the future of Al

![[assets/slides/HEFSExa0xl0/slide-007.jpg]]

OCR text:

> Code mode vs. REPL
> Code mode the agent writes scripts instead of making tool calls. Operations compose
> Fare Cute] |b aee\O be end LOM camae ln aneln
> Peo
> bd * . .
> * “¢ REPL ~ code mode + persistent state -- variables survive acrass calls. The agent writes shorter
> ra oa scripts, reasons between them. builds understanding incrementally,
> * * bd
> Result: accuracy gain on harder tasks — the agent can course-correct mid- exploration,
> o
> ry Led

![[assets/slides/HEFSExa0xl0/slide-008.jpg]]

OCR text:

> The verification loop
> The tora aeoiine ad renderer cased hoen tae agent
> Pec neh eee Sera .
> Va /al ts)
> eh % p ETO Ih eS CT cee ae ,
> * Bd reais Coot new aided used tie sgrie boop inate
> ad a
> ane cera 1c
> 4
> Render
> ry
> Al Engineer
> Sele) as

![[assets/slides/HEFSExa0xl0/slide-009.jpg]]

OCR text:

> Taio elec Sd BTGnS
> The REPL is an interface — the best one today, because coding is where
> ahs models are strongest.
> * *
> mn f The engines — formula calculation, rendering, linting — are the more durable
> a part. They're what close the verification loop, and they compound with each
> aT oa wa RRLOLe [ot
> If for instance agents become as capable at computer use as they are at
> coding, the interface might change. The engines won't.
> ‘
> Al Engineer
> EUROPE

![[assets/slides/HEFSExa0xl0/slide-010.jpg]]

OCR text:

> Domain knowledge outlived every tool
> We chanzed tools four times in four months
> The financialdemain knowledge improved results or every one of them
> x * &
> Sa *
> * rs Structured as a composable prompt component
> * *
> rd
> How to interpret margins, profitability, revenue cascades
> Model type recognition (DCF, LBO, three statement)
> + Communication conventions ($L2M not $1,234,50/89)
> ~ “Never calculate in your head what the spreadsheet can calculate for you"
> Itwas the most reused component in the system,
> .
> po
> Engi ing the fut wa

![[assets/slides/HEFSExa0xl0/slide-011.jpg]]

OCR text:

> TauAPeLNea ere CUlZOm x Uft miele) 1 OmTee Loran Tm TIC ICas
> What it looked like What it actually was
> rand ss , .
> ra * Agent can't find data One-character extraction bug (50% = 735)
> acc
> bd bd Agent uses wrong quoting SKILL. md had backwards examples
> * ve *
> Agent times out constantly Per-cell recalculation query instead of batch
> Agent retries endlessly API returning empty results intermittently
> When the agent seems confused, check the plumbing first.
> a
> .
> Engineering the future of Al


## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
