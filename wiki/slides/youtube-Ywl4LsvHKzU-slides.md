---
title: "Slides: RAG Evaluation Is Broken! Here's Why (And How to Fix It) - Yuval Belfer and Niv Granot"
category: "slides"
video_id: "Ywl4LsvHKzU"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: RAG Evaluation Is Broken! Here's Why (And How to Fix It) - Yuval Belfer and Niv Granot

## Source Video
[RAG Evaluation Is Broken! Here's Why (And How to Fix It) - Yuval Belfer and Niv Granot](https://www.youtube.com/watch?v=Ywl4LsvHKzU)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/Ywl4LsvHKzU/slide-001.jpg]]

OCR text:

> RAG is already solved.
> £ rd 7
> ° aa | ya i
> a by UR eye teers CeloL aoe

![[assets/slides/Ywl4LsvHKzU/slide-002.jpg]]

OCR text:

> Prob lems Local questions, local answers
> e Assuming an answer lies in a certain chunk
> \
> > ma

![[assets/slides/Ywl4LsvHKzU/slide-003.jpg]]

OCR text:

> Prob le ms Local questions, local answers
> e Assuming an answer lies in a certain chunk
> Multi-hop questions are not realistic
> e “If my future wife has the same first name as the 15th first lady
> of the United States’ mother and her surname is the same as
> the second assassinated president's mother's maiden name,
> what is my future wife's name?” (from: FRAMES)
> 7 ¥. 7
> ae

![[assets/slides/Ywl4LsvHKzU/slide-004.jpg]]

OCR text:

> Prob le ms Local questions, local answers
> 
> e Assuming an answer lies in a certain chunk
> Multi-hop questions are not realistic
> 
> e “If my future wife has the same first name as the 15th first lady
> of the United States’ mother and her surname ts the same as
> the second assassinated president's mother's maiden name,
> what is my future wife's name?” (from: FRAMES)
> No holistic way to test the entire system
> 
> e Retrieval-only benchmarks
> 
> e Generation-only benchmark (grounding)
> 
> e What about chunking? What about parsing?
> 
> Un rn 7 :

![[assets/slides/Ywl4LsvHKzU/slide-005.jpg]]

OCR text:

> 1. Build RAG systems for flawed
> benchmarks
> 2. Celebrate our awesome benchmark
> The scores
> Vicious 3. Watch real users struggle
> Cycle 4. Create new benchmarks with the
> same problems
> 5. Rinse and repeat
> ever]
> a

![[assets/slides/Ywl4LsvHKzU/slide-006.jpg]]

OCR text:

> Example FIFA World Cup
> e Which team has won the FIFA World Cup the most times?
> e In how many FIFA World Cups did Brazil participate?
> e List all teams that have never won the FIFA World Cup but have
> reached the top 3.
> 1994 FIFA World Cup Fy te nenquegee
> Reed 13° vewtat ee, Tom |
> 1998 FIFA World Cup Fy 02 enguagen —
> 2002 FIFA World Cup ta eee eT ee
> — Ra KE cn akin, ree
> Fem Hepes Re hee ov rhgee ‘Works Cup UGA D4
> ferecmewen meni poi ccomaewsititanein WorldCupUSAS4
> The 2002 PFA Wertd Cup sho branded os Kevea/Japen 3002 wen he V7 FA 2002 FWA Worle Cup a@e
> Ae rene baal word chempsorane bee ma eee “—e nevtea gue paneii=ci toe FIFA World Cup Seaman
> gered by FA Eine Hats Sere 9 May 0 Rane Tae ae aan Roves ard $00 P04 Wetter Keen e@ cement
> a RAR a NMAC owt by dager Mer nal em ea ee 2002 FRAD-Ab Ao 7 RS Joupe de Monde - France 08 (5 107.r) ta Se
> During th apereng canwnary Ihe Chemonneng wes Oeclired ODered try Ieee / Sine
> Soe eg ee Dae es SR? AE, Geuewete Laupes Deciatastcpgons: = WS
> (A Sand of 32 tearre qusdined tor ea Word Cup mach ene the fea © te head in Ave GX theerg Socoee Heaxy
> Pea teat ty be Pend cnet Of It Acres ae or fs Ca at wed as Pie end bo be oaray \.
> Sosted by more Pan one Ambo hee fle eee and rene Sate Pee Perumal Gate:
> nr we pie a Terese tang he ony Gebvtart i quaity roe ha ye ee
> re r¥"3) x y wome cur —
> A ry ard weprne tends Wah cided Pe defending, fe
> é bh : peo nha grove stage wher serrung a engie port 202 Torerteampat Gxietis
> D fa a A ee ee FIFA WORLD CUP ( opentry Preece
> = an KOREA JAPAN

![[assets/slides/Ywl4LsvHKzU/slide-007.jpg]]

OCR text:

> Common
> 
> RAG Retrieval Generator Score
> 
> Pipelines Pipeline
> « Common
> 
> Fail | 088
> wees FUN eet Cage “i O
> 
> ser FOpenar | 8
> 
> rey ms
> 
> PD eee

![[assets/slides/Ywl4LsvHKzU/slide-008.jpg]]

OCR text:

> High Level ldea
> Query
> FIFA World Cup
> Unstructured
> DataStructure
> Corpus
> ONAIR

![[assets/slides/Ywl4LsvHKzU/slide-009.jpg]]

OCR text:

> 1. Cluster
> _ 2. Identify Schema
> Ingestion: 3. Populate
> Flow 4. Upload
> Kor 73) A

![[assets/slides/Ywl4LsvHKzU/slide-010.jpg]]

OCR text:

> Ingestion - Schema Creation
> World Cup
> Year: int(1900-2100)
> Corpus Schema Winner: Team
> (FIFA) (SemanticObject) || Top3: List{Teams]
> TopScorer: Tuple[Player, int]
> ey aa
> 74

![[assets/slides/Ywl4LsvHKzU/slide-011.jpg]]

OCR text:

> Challenges e Not every corpus/query is relational DB material
> e Normalization (West Germany, South Korea and
> Japan)
> o Both during ingestion and inference
> e Abstinence & Ambiguity
> o Did Real Madrid win in the 2006 Final? (Not
> world cup)
> e Clustering and inferring schema (clear trade-off
> on complexity)
> e Text2SQL over complex schemas
> ne ae

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
