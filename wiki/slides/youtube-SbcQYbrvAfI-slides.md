---
title: "Slides: Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize"
category: "slides"
video_id: "SbcQYbrvAfI"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize

## Source Video
[Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize](https://www.youtube.com/watch?v=SbcQYbrvAfI)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/SbcQYbrvAfI/slide-001.jpg]]

OCR text:

> ay onary es) . . . . . : Bs ne
> Applied Prompt FCDA
> Me De) nee ON
> bal OptimizationLoop... -° ASN
> ~ ee Ty] : 7 . BAN S |
> , y a _ a ° A
> 4 yl f | yo
> t- f - Os PT
> 7 ‘ . ._.
> = (f* fee 2025-11-22 12:33:53

![[assets/slides/SbcQYbrvAfI/slide-002.jpg]]

OCR text:

> a te . ANITA ee
> Tea 13 FDO
> BT Lh) eee
> _ OptimizationLoop... - A ;
> | | pee ey) D : 7 iu ASN . r
> . oo ;
> i.
> a ee
> A eal a A _ on A
> veusy ens aa ; 2025-11-22 12:34:43

![[assets/slides/SbcQYbrvAfI/slide-003.jpg]]

OCR text:

> Agenda
> ‘O14 ‘02 /O3
> Why Agents Fail What Is Prompt Case Study: Coding
> Today Learning? Agents
> /04 £05
> Prompt Learning vs Workshop
> GEPA

![[assets/slides/SbcQYbrvAfI/slide-004.jpg]]

OCR text:

> ~~ —_ —- 4
> Agenda
> Why Agents Fau What is Prompt Case Study Coang ]
> Today iearn.ng? Agents
> Prompt Learnng v5 Workshop
> GEPA
> P ca mL 7
> re)
> ; 2025-11-22 12:35:33
> JFK 27-B1.300

![[assets/slides/SbcQYbrvAfI/slide-005.jpg]]

OCR text:

> Where Agents are Breaking in 2025
> No System Instructions Learned No Planning or Missing Toois
> From Environment Very Static Planning
> . ; ee ue
> Too! Guidance Missing Context / State
> — Management
> a, \__ (Pre Pruned Data)
> ge
> Aarize 2025°11°22 12:35:58

![[assets/slides/SbcQYbrvAfI/slide-006.jpg]]

OCR text:

> Core Issues Distilled
> Adaptability & Self Determinism vs Context
> Learning Non Determinism Engineering
> Balance
> No System Instructions No Planning or Missing Tools
> Learned From Environment Very Static Planning Tool Guidance
> Missing Context
> (Pre Pruned Data)

![[assets/slides/SbcQYbrvAfI/slide-007.jpg]]

OCR text:

> ? e e
> 1 Other Issue I'd Like to Mention
> Technical Users Domain Experts
> es %,
> — " 2) &
> Al Engineer eee: Data
> Pe Scientist Subject Matter Al Product
> Experts Manager
> Developer
> Responsibilities Responsibilities
> Code/Automation Domain Prompt engineering
> Pipelines/Frameworks Track and run evals
> Application Performance / Costs Ensure product es

![[assets/slides/SbcQYbrvAfI/slide-008.jpg]]

OCR text:

> Reinforcement Learning
> RL Model _._—_—s Action > Reward Function
> (Student's Brain) (Takes Exam) (Exam Scorer)
> Update Weights Scalar Reward
> (Student's Brain) (Exam Score)
> Algorithm: Gradient Descent, PPO,
> Q-learning

![[assets/slides/SbcQYbrvAfI/slide-009.jpg]]

OCR text:

> Prompt Learning
> Agent __—_— Output > LLM Evals
> (Student) (Takes Exam) (Teacher)
> Update Prompt
> (Lessons, HWs)
> Algorithm: Meta-Prompting
> (Teaching)

![[assets/slides/SbcQYbrvAfI/slide-010.jpg]]

OCR text:

> Traditional Prompt Optimization
> Formulated Like an ML Problem
> Data Prediction
> Prompt Labels
> | i
> Optinize This Maximize This

![[assets/slides/SbcQYbrvAfI/slide-011.jpg]]

OCR text:

> System Prompt Learning
> , 5 Evel Explanations,
> Human Instrunctions, Evol & ati Promet Prediction ,
> Bete Why it Foiled ie ewes Labels why Failed
> [| . | . | . = : | : |
> Add Instructions o changes to System Prompt here,
> to help ‘t improve
> Aarize 2025-11-22 12:40:58

![[assets/slides/SbcQYbrvAfI/slide-012.jpg]]

OCR text:

> Coding Agents on SWE-Bench Lite, No Prompt Changes
> Sonnet 4-5 GPT 4.1 Sonnet 4-5 Haiku 4.5
> Cost: $3/1M tokens Cost: $2/1M tokens Cost: $3/1M tokens Cost: $1/1M tokens
> *& Latency: © Latency: * Latency: *& Latency:
> 30.00% 18.67% 40.00% 18.67%
> Retr Deas sey UE UD so ats Ghia G issues cetabe s aes
> HN ped Pe Sard pes yet BP Bo AN

![[assets/slides/SbcQYbrvAfI/slide-013.jpg]]

OCR text:

> Optimizing Coding Agent System Prompt
> Claude Code system prompt Claude Code system prompt o  cw
> You are a Claude agent, built on Anthropic’'s... You are a Claude agent, built on Anthropic's...
> Rules Section Rules Section
> <Empty>
> . Cope est Le op ot err PP oe eget ce .
> 4G Pktee wor TP Beet, ET EL PE de PP 8
> “bH Rone PEW bats |
> 2? PE atid 0 avr de Ob Sat. age TE TR be tai td
> \ ERR Bled 2 2 ed Sow PD GE DP PP, TPE
> eutbectoete becrs duil eit
> 3 SO Cniate ota a be Gam bo a ma
> vid Pay Rp ok aero Laer 9 iia #8 tpovedaae cote
> pedo ab ap ober ita yg
> % PolAGat ue beter og cene > be fap veri er,
> ped a eh ERD
> _ "ERs

![[assets/slides/SbcQYbrvAfI/slide-014.jpg]]

OCR text:

> . . : . Cc Qk
> 
> Solution Patch (summarized in english) orres
> In bee ta wr boaatos. . return early if cela
> 
> Problem ‘eeeoor Cfor cen eu «) eata isn’t a Voora i, skip
> 
> Chine was asked to fixa non-op se: items when as. Ure, and when fetching
> 
> bug where the program o poe Catch Cxecres nl to nekrr pr) so tield validators
> 
> crashed if the input run only when the field is actually present.
> 
> WAS ‘oe, =
> 
> Corresponding Rule
> When you locakze a bug. enumerate every execution path that reaches the fauity une (0.9. single vs. batch
> flows) and propose a munmmal fix that miurors Sdjacent error-handling patterns across a# paths. then outline
> fogtession tests that cover each path to confirm unchanged semantics.
> Solution Patch (summarized in english) &
> ¥ , . wt orrect
> Problem Update cree, sat to defer to matr ix
> cl ; f semantics and return ¢. tiog es 8 ce for non-matrix
> ine was asked to fix a operands (after o:-:::-.7..). allowing Python to try
> 
> bug where using the reverse op or raise a losr:rre: per the
> 
> with a scalar (e.g. 7 _* @ operator protocol.
> 
> Mote x) incorrectly
> 
> behaved like Corresponding Rule
> 
> multiplication instead When proposing a fix. first map the failing test or reported behanor back to the exact API of function it
> 
> of failing exercises. Ensure your changes akgn with that boundary - modify the function or layer dwoctly responsible
> for Une behavioe rather than a relisted but bugher- level ublity. In other words. ful asues at thew source. notin s
> Nearby convemence function

![[assets/slides/SbcQYbrvAfI/slide-015.jpg]]

OCR text:

> Benchmarking Cline w/ updated prompt on SWE-Bench Lite
> GPT-4.1
> Optemization Loop Train Accuracy Train Delta Test Accuracy Test Oetta .
> — onrsa ~| 5% Improvement, just
> : 0 2000 400133 02133 10.9400 through rules
> 2 0.3400 20.1633 0.3133 +0.1400
> 3 C3333 «0 1466 0 2800 00 1067
> 4 0 33900 001543 0 3000 +0 1267 . .
> e No fine-tuning, no tool changes, no
> architecture changes. JUST RULES.
> Claude Sonnet 4.5
> Optimizaton (ogp = Tran Accuracy Tran Deita Test Accuracy Test Oeta e GPT-4.1 achieved performance near
> ° 0.3000 - 0.3633 - . . .
> Sonnet 4-5, which is widely
> 1 0 2800 oo2ce O3533 9 0200 . .
> 5 5 3308 e078 eae 50808 considered state of the art for coding
> 3 0.3600 40.0600 0.3600 40.0067 questions
> 4 0 3000 +0 0600 9 36900 +0 0067 3 4% cost!

![[assets/slides/SbcQYbrvAfI/slide-016.jpg]]

OCR text:

> Rule Generalization: Meta-prompt enforces high-level, reusable coding rules rather than repo-specific fixes.
> Cross-Repo Validation: Train/test split by repository ensure learned rules generalize beyond local quirks.
> Expertise vs. Overfitting
> e True developers do “overfit" — to their own codebases.
> e That's not a flaw, it's expertise: understanding patterns, pitfalls, and idioms within a domain.
> e Cline can adaptively specialize when deployed to a team’s repos, mirroring how human engineers internalize
> their environment — while still starting frorn a general foundation.
> Aarize 2025-11-22 12:45:08

![[assets/slides/SbcQYbrvAfI/slide-017.jpg]]

OCR text:

> Cross-
> Expert
> internalize
> ^orize
> JFK27-B1.300

![[assets/slides/SbcQYbrvAfI/slide-018.jpg]]

OCR text:

> Benchmarking Cline w/updated prompt on BBH
> BBH - Diverse evaluation suite that tos imutiot Finataccutacy change
> focuses on tasks difficult for language Acsueaey (eens)
> models sakent_tramsistionerror_ detection ° 08 f
> snacks, os 0.88 +038
> Example BBH Benchmarks tracking _shulfled_obyects_tneee_objects é ose 038
> - Complex Boolean Expressions fopscat deduction hve: objects ae bed “ex
> - Categorizing Geometric Shapes . Sports understanding 086 0%6 soa
> based on vertex coordinates word_sorting oes ova 0.04
> - Detecting Sarcasm in Statements semooeet—teuenees “e ' soot
> geometnc_ shapes 048 05 +0.02
> boolean expressions 094 094 0
> logrcat_deduction_three_ objects. 096 O96 0
> obyect_counting 0a 0.76 0.02
> multistep. anthmetic_two 008 O06 0.02
> formal_fallacies oes oa 0.04
> fopcal. deduction seven_objects 0.7% 0.72 “0.04
> web_of_hes 0.56 O48 0.08

![[assets/slides/SbcQYbrvAfI/slide-019.jpg]]

OCR text:

> DSPy osm Ga: eure
> Cool features:
> Ab tee eee
> ats Retewore aah 8 Lo i a?
> Mea oe ~ , , ‘
> bes -
> ern ee e Evolutionary
> teat Snape Pate ene eaten Mpame ta Te FRR page eitie Mate
> wore LOREEN HARE CETUT NEE OM aD CSTE RSTO Te mar eet retire Ly Me oe
> Bicheno aN SEA ONG A HORE FRIIS ERRRRRTDTN Sar NAR | optimization
> Ende Beak CEPA Oey ty at he LTT pd the eee hat Sd AMER EPA ptletgant &
> cee Abe Norm toy enero the bene TEA aroma EAL (eweme oe peetierteng (Aree every fom en e Pareto-based
> wenparee tg!
> eas
> sie Clase dapy GEPA.@atric GEPAFeedbackMetric ° suto Literal! light candidate selection
> iqrares = eqtiua oo neavy ; one Hone mes full.evels int fone = Bone lee .
> ase - eer meteic colle int mone + Mane reflection anibaten ange int e@ Probabilistic merging
> . Candidute eeloction atretegy catecsl! parets turtert heat f+
> aad fareto reflection lm th Mone Hone snip perfect score fuck +
> BRAS True odd forant failure os feedback col - Falee instruction proposer of prompts
> heated Propotelfn Mone +» Hone component selector Reflect tonCosponent Selector
> Yee ave Fmd (bn use Merge sol | True @an merge ineccations ist
> sent ate None = $ mum threads int None: Mone failure score fleet 06
> te ose perfect score flat 16 bog .6le str + Bone Crach skate bust +
> Crete False we andi tol False mande epi ey st fone + Rene
> ed end init kearga Sit] sts Amy! lane - Kone track beat outputs tol But
> es + False earn on score atametch tal « True wee elflow. onl false “
> tire awed rt Mane) 6 8 gape kearge diet) Mone - hone
> atid 2025-11-22 12:47:13

![[assets/slides/SbcQYbrvAfI/slide-020.jpg]]

OCR text:

> Prompt Learning vs GEPA, benchmarked
> We ran the same benchmarks used in the GEPA paper, but for Prompt Learning.
> With some eval engineering. here are the results we got:
> HoOtpotga, GPT.4 t Mini Hover. GPT-4 1 Mins
> ni - TO as oo SS
> 4
> 63 ‘
> | [po %
> we ve -
> | » / /
> es | bs /
> x | » ps : 2 s dee
> sr , 0 /
> a | | rr) ° /
> | : Optimization Method a / Optimization Method
> | oe OEM es / oe GM
> aw oe MPPOV? MPR.
> | —O frompt Learneng —@ Prompt Learmng
> , ¢ 1ooe 2000 w0 4000 000 4000 ° _ ¢ 1000 2000 000 4000 S000 000 »00
> Numbet of Rotonts Nuriber of Rovouts

![[assets/slides/SbcQYbrvAfI/slide-021.jpg]]

OCR text:

> oe A
> 4 b
> 7 Se ie
> my , : a i
> sg gg
> JFK 27-B1.300 2025-11-22 12:49:43

![[assets/slides/SbcQYbrvAfI/slide-022.jpg]]

OCR text:

> i
> \
> “
> 1 - .
> k ly f 7 ra
> ea ; a «
> —_ es
> 
> 7 a ( a
> 
> A 2025-11-22 12:50:08
> JFK 27-B1.300

![[assets/slides/SbcQYbrvAfI/slide-023.jpg]]

OCR text:

> WORKSHOP
> 
> 2025-11-22 12:50:58

![[assets/slides/SbcQYbrvAfI/slide-024.jpg]]

OCR text:

> North Star: Self-Iimproving Agents
> Self-improving agents require a feedback loop where both agents and evals evoive together—not just better
> prompts, but better evaluations too.
> Collect data
> oo
> byals with low oO
> confidence
> D Improve fae Run evals . fey area. @
> 
> Improve prompt Agent Update prempt Pyates
> 
> / Fine-tune
> 
> , Collect dataset SN 7
> Annotate for of failures S
> training dataset
> 
> Aarize 2025°11-22 12:55:08

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
