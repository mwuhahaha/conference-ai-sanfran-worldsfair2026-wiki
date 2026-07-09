---
title: "Slides: Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked"
category: "slides"
video_id: "5ID22ACI7IM"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked

## Source Video
[Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked](https://www.youtube.com/watch?v=5ID22ACI7IM)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/5ID22ACI7IM/slide-001.jpg]]

OCR text:

> PLATINUMSPONSORS
> $ Braintrust
> Workos
> OpenAl

![[assets/slides/5ID22ACI7IM/slide-002.jpg]]

OCR text:

> Bullding the context
> neAlagentsne
> AlEngine
> EUROPE

![[assets/slides/5ID22ACI7IM/slide-003.jpg]]

OCR text:

> What we'll cover today
> 3 3
> Myths Lessons

![[assets/slides/5ID22ACI7IM/slide-004.jpg]]

OCR text:

> a
> 
> oi =~

![[assets/slides/5ID22ACI7IM/slide-005.jpg]]

OCR text:

> Remember how you built context?
> * Day lat yourjob you had almost nocontext.
> * Overtime, you accumulated it:
> 
> * Mentorship
> 
> * Planning & code reviews
> 
> * Architecture decisions
> 
> * Incidents & outages
> 
> * Experiments & rollouts
> 
> * Pushing alot of PRs

![[assets/slides/5ID22ACI7IM/slide-006.jpg]]

OCR text:

> The problem:
> 
> access ¢ understanding
> 
> * Weconnect agents to code, logs. docs, tickets, and more...
> * Which gives us plausible output that often compiles...
> 
> + Butit fails human review and real world expectations.

![[assets/slides/5ID22ACI7IM/slide-007.jpg]]

OCR text:

> —~
> CODE THAT COMPILES
> ORIGINAL INTENT What your agent cant cee
> aT Sul
> ar ae oo
> Pr at eh
> Prt
> at}
> aac y ett rts
> YO e tt ye
> Tc td
> PTT kL a
> enrages

![[assets/slides/5ID22ACI7IM/slide-008.jpg]]

OCR text:

> S S del. Diff
> ame prompt. Same model. Different context.
> Fourcntera ary eng neerexpects
> Validation & Integration Tests Doesn't Break Existing Implementation
> Without Without
> 2.5/0
> UB UB.
> wenus QC win C8 Cp
> Without Unblocked Wetp Unblocaed Without Undlocked: Wat dnblocaed
> Unt tests only - COAPL mtegrat oa "Sun tteste AP megranen tests Auto- detect siasty charged Opt adetay t(tatejoreserves a
> no Bed-cce cr eaten ce erage acfossas Smeduies Agee sso behay of fora. budget _tonen cast sgneravot Zeroe sk to
> Hugs n?otdmedvetwedsh a caught beatore merge callers -- brea -g every en sting Curent callers ro rey ew Mags
> ungetestea Ate grat orf NAT CaUGrt Dy fT aN
> senew
> DRY Code, High Quality Bar Respects Our Conventions
> Without Cc Without
> oe oe 2no
> me woth 8
> Without Unblocked Wietn Unplog wed Without Undlocked: With unbisoked
> Agdedcustam senaizess the team Used Kat * defen teatdenst og vised 3 factory metroad pattern Exter son funct ons mater mest 99
> doesnt use redes gredtrebatch sera zat sripatternss Sagie cess fole grtothecccebate causg team patterns Ze-o comp at ar
> AM Jeros A ct twou'dneea'a pass Mothag toraaworn 1? comp tanon salutes Ceory fares Targedwtrout se
> bercpedout revere Module would need tewsting to feedback
> match tea style

![[assets/slides/5ID22ACI7IM/slide-009.jpg]]

OCR text:

> Where Al forward teams use a context engine
> 
> * Agent Plans & code — hydrate context before planning to improve codegen quality.
> * Ticket enrichment — gathering context across systems to improve tickets.
> 
> * Triage operations — routing issues, enriching tickets, and validating bug reports.

![[assets/slides/5ID22ACI7IM/slide-010.jpg]]

OCR text:

> fo Ce See enees Over teens [> eure O.-- OG sesrnrarcsmenygnesiny [ee eas eee eer) ee
> LE Waters Se ele Te eee ee ee ee cere]
> baat oad
> @ [ie oe od Th OA em te
> ceeened es
> >

![[assets/slides/5ID22ACI7IM/slide-011.jpg]]

OCR text:

> fo ee eon ores lo ee rny el los ee eer O:.+ (ee a ee Fleece wen ie GNC area
> [ane CT Se ale ee ee ete ee aed eres]
> bat ad
> >
> Cranes roan
> res La

![[assets/slides/5ID22ACI7IM/slide-012.jpg]]

OCR text:

> pist.github.com
> C
> nM
> qunC
> HstPRFiaes.
> ocked
> GitHubGist
> Search.
> Q.
> All gistsBack to GitHub
> baell/gist:087fb19d8fe83b982c08b77212b8dc71
> sutscrbe
> str0
> YFon
> ed2msaoeo
> (>Code
> Revisons1
> <striat sre*htsi/
> DownloadZP
> Without Unblocked
> gietfsles.tt
> Claude Codsv2.1.31
> Opus4.5·ClaudeMax
> -/repos/workfelder/unblockes
> Plan to inplement
> Auto-Generate PR DescriptienAfter CodeReview
> Overview
> Addfeature to autonatically genrate and aoplyP description after unblocked Code Review runs oneely oened pull
> A1.
> Architecture Decision
> Trigper：Ony on PullReguestOpened events (net on sbseuent pushes）
> Conditien：Only 1f PR description is npty/ninimal（<5 chars or blank）
> trrarhanding:Failgracefelly -ontlock cde review if description update fails
> Files to Modify
> 1.Add Org Setting
> File:projects/aodeis/sre/main/katLin/com/nextchagtersoftware/@/nodels/0rgiettingsModel.kt
> Adsafter line 57（withother codereview settings):
> valenableCodeReviemlutoDescription-bool（*codeRevienAutoDesc*).nullable()
> Also update:
> -OrgSettingsDAO.asDetaModel()
> Crglettings data class
> orgSettings.getDefault()

![[assets/slides/5ID22ACI7IM/slide-013.jpg]]

OCR text:

> (> eee eer one (> eee Ocon ee eee te cern fr] ee ey
> dette an ee
> Summary Table
> aT De ee ASS ae
> Seer) oe eC re eee ec. ce
> rere eee tote ae oe
> ra

![[assets/slides/5ID22ACI7IM/slide-014.jpg]]

OCR text:

> (oC oe fo eee rs (oe ee ee Tee Poweriewe we ween ee eee
> @ Unblocked g Summary of Latest PR Fixes and Enh...
> 
> e a) 7 a a y y
> 
> Pe “ont
> 
> ae Cara i re
> 
> Tamer ore Cee ote
> (er co
> & ae

![[assets/slides/5ID22ACI7IM/slide-015.jpg]]

OCR text:

> [oC ere Co ee Qe eee [<a Co erence ene) De rae te aes Peconic earner OCPaeS
> Cees re
> >oClal Grapn Bulaer
> feria
> ESTs OES ag eR CS EC S(O Ts
> eT ace ce ey eee ne ms ea A ec Ce RU Cy aor Bae a a a ye eta
> Pe PC 1s
> erate retin
> tse a}
> COR recor 1 C101:)s ME RCL LPTs area ets SS Se aa es ee
> oe cena
> Suggested worktlows
> PM Cor po Sita cite MME ele paar) Mea i Me abe srg Ree a i a eerie ae a ct oar aceon ad re
> Fr a eed
> US ot os se a oer ae See ea
> ; eo ee eae sep oye
> ants Dal ater a
> Peer Gretac}
> Ue Pcen Tan ZO res a a eC Pe
> en sear fata
> OS ohotae Vee rer See oS COC a ee st
> Quick Start
> -
> 1. Build the CLI
> ga a ee ee ee ee ee 4. BRP g,: ce Paces toe
> Cee, s evened
> con 2 ans

![[assets/slides/5ID22ACI7IM/slide-016.jpg]]

OCR text:

> (2 ee > eer [oe een ts eee (pe ee eee ee Pinwecwe: 2 weet Pere oer Oren
> STA eC alae lg
> Soe ree
> Fee Ree en aed
> 7 Le - ” ”~
> aa a ee Red ; ne oe e °
> ar ew oa cary Ped ase erry ey
> E a ree os rare na
> og oes on ary rey Pd
> ne ray
> eo. . ae ae 00 rr 100
> a re Pos Es] ry cao coe
> woe rev) ra) ry) PY
> Rae eres 160 ry ry oon ey
> one a ca) ra
> Pn
> aa ry a ro) ot cae rd
> Ss x09 ry en rcs oes Cer 10 ry re cary ea
> rr oo rv) cel an ry red od ry v7 ary
> e e m
> > ic)

![[assets/slides/5ID22ACI7IM/slide-017.jpg]]

OCR text:

> (oe eee) eee to ee ree [+ eae (Ck Gea arent aes Poweses: oe cae ore ere’
> CTE eer al a Chios
> BPN gocher tea tation
> Source Controd Platform Be ee a a | Teal eel ks ok oneal See Ru eae DY
> tee ae eee dd * Snes at Pte es)
> a a @) (<)
> - aan noes,
> Porter oo any e veer
> Od
> PoP aS r?) 7 Ch eer
> oy
> r ) Co reraretey Cw) Ce Eeccr try
> Reh ot De al
> nrc
> @) eae

![[assets/slides/5ID22ACI7IM/slide-018.jpg]]

OCR text:

> i aesine 0 : (oer! (> ones - 7 re 7 | Ce Cre - a a oa on eer ereany
> lta : seal al -_

![[assets/slides/5ID22ACI7IM/slide-019.jpg]]

OCR text:

> (eee lo ena lo rere ere [ : re Oncaea ee rere fe) ee eer ery
> TA UOC eld
> 
> a ~ Cooney
> 
> Co) e
> x @ ; |
> rn
> (owe Sa :
> TAY

![[assets/slides/5ID22ACI7IM/slide-020.jpg]]

OCR text:

> | a = — ee
> _—
> 4 -
> ed ; |
> .
> ow a

![[assets/slides/5ID22ACI7IM/slide-021.jpg]]

OCR text:

> eee
> 
> a
> 
> Ot
> 
> =

![[assets/slides/5ID22ACI7IM/slide-022.jpg]]

OCR text:

> (oe ee (ee (ee Gres (ye re er neers eer oar ec OLPenTy
> peta ella ,
> a eee
> “
> a
> — re
> an se
> re Pe , a
> VP ae
> re 7
> oN oan -
> ~
> NN
> an
> an

![[assets/slides/5ID22ACI7IM/slide-023.jpg]]

OCR text:

> Givin serenee seems (oars 6 nes cormacnesameien [. eee - ocean reer Gee ageeaeacanies eee Peet aon
> ) rea Cr aC Tae ante Tene sial ae 7 . . an |
> ono sme ag eae ra cig er ee er at ee
> enginecring-social- graph oe on oo
> oon 9 ° conan Coe eels
> ae Saeed ee 7 n
> 
> re nota
> 
> imal Caras ae
> Packages
> 
> Social Graph Builder

![[assets/slides/5ID22ACI7IM/slide-024.jpg]]

OCR text:

> ed

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
