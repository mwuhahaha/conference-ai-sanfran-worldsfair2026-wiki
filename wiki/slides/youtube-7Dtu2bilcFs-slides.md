---
title: "Slides: 2026: The Year The IDE Died — Steve Yegge & Gene Kim, Authors, Vibe Coding"
category: "slides"
video_id: "7Dtu2bilcFs"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: 2026: The Year The IDE Died — Steve Yegge & Gene Kim, Authors, Vibe Coding

## Source Video
[2026: The Year The IDE Died — Steve Yegge & Gene Kim, Authors, Vibe Coding](https://www.youtube.com/watch?v=7Dtu2bilcFs)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video that matched one or more scheduled World's Fair sessions by speaker. They are supporting context unless the video is later confirmed as the exact session recording.

## Related Scheduled Sessions
- [[2026-06-29-steve-yegge-agentic-security-permissions-provenance-and-the-agent-supply-chain]] — Agentic Security: Permissions, Provenance, and the Agent Supply Chain

## Extracted Slides
![[assets/slides/7Dtu2bilcFs/slide-001.jpg]]

OCR text:

> 3
> 
> a

![[assets/slides/7Dtu2bilcFs/slide-002.jpg]]

OCR text:

> °
> Al Developer Trajectory
> t
> 2023 2025
> a code completions (Cop:lot) agente coding assistants (Claude Code, Codex,
> Cline, Amp, Gemini CLI, . J
> | 1 2 3 4
> 2024 2026
> chat based programming (Cursor, Windsurf, Cody! 2
> Siang a We ail know by now that agentic coding is not the Fina Form for Al.
> This talk is about what's coming next: orchestrators.
> et
> ages 2026: THE YEAR THE IDE DIED
> eee STEVE YEGGE = jmp GENE KIM Aprevowstion
> Google DeepMind Software Engineer . Author & Researcher

![[assets/slides/7Dtu2bilcFs/slide-003.jpg]]

OCR text:

> Manual Tools get Automated
> >» NX _ yw
> >» _N Ye
> ; a j a si a
> | are 2 bale Oi
> P aw fy
> ¢ J i 4 -
> 
> Why would we stop now?
> Vans 2026: THE YEAR THE IDE DIED
> Serene STEVE YEGGE GENE KIM
> 
> Google DeepMind Software Engineer Amp . Author & Researcher MPrevowwtion

![[assets/slides/7Dtu2bilcFs/slide-004.jpg]]

OCR text:

> Models are Smart
> i + Enough
> ae 4 t 5 : 7 We are entering a world where Al will be writing and
> . re - de ¥ , newest
> rar eH rf m Ko. 4 reviewing all code.
> e ws eee RE The models don't need to get any better.
> yer! oe . ann:
> a red ‘
> 3 A we Os 2” If the models plateaued, this becomes a 100%
> A F oe i. %
> ‘ , . —
> rs & engineering problem.
> F a Seon . The models are getting better, but for this talk, I'll
> — Wee 4 getting
> assume they won't.
> : 3 . Because they don't need to.
> i po
> [see]
> ages 2026: THE YEAR THE IDE DIED
> ene STEVE YEGGE = jmp GENE KIM APrevournion
> Google DeepMind Software Engineer Author & Researcher

![[assets/slides/7Dtu2bilcFs/slide-005.jpg]]

OCR text:

> 7 e
> We've Seen This Movie el
> Before 7 re _
> Why are so many senior engineers refusing Al assistance? F a
> + watchmakers retused electric tools 4 «> 4
> ea + Caused the Swiss watch industry “Quartz Casis” i nam it
> y) drafters in the 705-805 rejected CAD ane ay
> « photographers refused digital tools oe] z Sie a
> - a ‘ =
> It takes time for people to change. But automation always wins. p> 7 ee
> Viet 2026: THE YEAR THE IDE DIED
> Eee STEVE YEGGE = jmp GENE KIM MPrevo
> Google DeepMind Software Engineer . Author & Researcher

![[assets/slides/7Dtu2bilcFs/slide-006.jpg]]

OCR text:

> 5 Ny The New Quartz Crisis
> a es Me’ cy mm Building software is like Linus Torvalds: One of
> eo ; ao “ \ building mechanical the world's best
> yas ¥@ .——) ’ a@ NV watches “watchmakers”
> /] ow rA\ \ y an old, elegant, handcrafted He says vibe coding isn’t good for
> ff ik < \\ i discipline “seal” work
> | Se, © i oe Same argument from the
> Cm“ “ - Graftsmen, watchmakers,
> 4 , \\ 4-4 iQ = AY = 7 photographers.
> | Na ry nerve
> \ NO ke WT. a Building software the old way will be automated away
> a , am
> 7 and it won't take 10-20 years tha time
> _ net it will take 1-2 years
> AIE/LEAD It Tenex Bloomberg Bre NermULaToss MINIMAX Google
> Google DeepMind larize %<goose ¥', Modal €> turbopuffer Cs %e¢elastic «

![[assets/slides/7Dtu2bilcFs/slide-007.jpg]]
![[assets/slides/7Dtu2bilcFs/slide-008.jpg]]

OCR text:

> J
> cone e
> ’ Adoption Depends on
> —" ‘
> 4 ue = 3” Having UI
> sae ~ “”
> e . wer § « We've established that CLI But coding agents aren't
> eee ets
> : j a = agents are too hard for most heading in this direction.
> nd
> _ devs. Instead, they're doubling
> 7 const st 2 on We clearly need a Ul. down on the CLI.
> Lammers i
> | oo | lu! We also need to lift people up. » How much has Claude Code
> aw om changed since February?
> + Claude Code shoves your nose in
> : onion - everything.
> 54 RES we @ wi 1g.
> jaa ‘ oe” 7 cof ae + You have to watch everything it
> ‘ a zs aoe ae _ does.
> i oe X + We need helpers - models!
> coset _
> Ca fd
> Sea Engineering the future of Al

![[assets/slides/7Dtu2bilcFs/slide-009.jpg]]

OCR text:

> iY .
> : °
> | Coding Agents Should
> 2
> be like Ants
> Z
> 4 One huge problem with coding agents is their
> granularity: You send all tasks, even cheap ones, to the
> expensive model.
> > + "please analyze this codebase for Haws” --> expensive
> + “is my gitignore file still there?” --> also expensive!
> _¢ instead of an ant colony, Anthropic built a huge,
> ~ oa ry el : muscular ant,
> * — There's a better solution: Make small ants.
> 7 ‘
> ce f
> e td
> Sea Engineering the future of Al

![[assets/slides/7Dtu2bilcFs/slide-010.jpg]]

OCR text:

> Coding agents are She deve Vow send thee “unserm ater et ya cote
> Thee (ORAeH ern a Dw orppen lene
> AA eed droge can Get corr SIve Tngy done oN Se mate
> ba Oe rd int wee
> ‘Why are we Lrymg Le Rares 2 vunghe Greer de ever ptheng”
> 
> - - .- a
> 
> Code Summit - o |
> oats cana "
> ie od 3 ely
> Pe ae
> 3 re a
> 7 , f |
> f 3 an bs

![[assets/slides/7Dtu2bilcFs/slide-011.jpg]]

OCR text:

> TheDiverProblem
> ly so big
> tohave astingle diver de everyth
> AlEngineer
> Engineering the future of Al

![[assets/slides/7Dtu2bilcFs/slide-012.jpg]]

OCR text:

> Dealing with Backlash
> “"* Guetcho G. © »
> Mmm right.
> But no.
> My brazenly shameless advise to you:
> Leave the programming to the programmers.
> Do your director stuff instead.
> aml
> eee
> The backlash will be pretty cevere
> We're already seeing it. Just mang you aware now
> Engineering the future of Al

![[assets/slides/7Dtu2bilcFs/slide-013.jpg]]

OCR text:

> IES’ = ical
> , ae
> y ae
> a 7
> |
> |
> |

![[assets/slides/7Dtu2bilcFs/slide-014.jpg]]

OCR text:

> | . |
> _ | 7 _
> nl : ag

![[assets/slides/7Dtu2bilcFs/slide-015.jpg]]

OCR text:

> : The Value of Vibe Coding
> as - F: Build the things | want faster
> wo « A: Be more ambitious about things | can build
> A: Be able to build them alone (as opposed to
> requiring other people or a team)
> = F: Have so much more fun doing it
> : O: Have more swings at bat, explore more
> hed : options
> 2026: THE YEAR THE IDE DIED
> eee STEVE YEGGE GENE KIM
> Google DeepMind Software Engineer Amp 1 Author & Researcher Pirevowion

![[assets/slides/7Dtu2bilcFs/slide-016.jpg]]

OCR text:

> Booking.com (2025) ~~
> | * Bruno Passos, x
> a Group Product a
> Manager, Developer Bases
> Experience ——E *
> - Laura Tacho, CTO, oo
> DX wed . Daily Al users ship 50%: more than non-Al users
> c$25 1 — ..
> fm | : nl
> , Source blips sated srevoknon com watch’ 1121936057 oes 4.
> 2026: THE YEAR THE IDE DIED
> eer STEVE YEGGE GENE KIM
> Google DeepMind Software Engineer >} Amp . Author & Researcher MPrevourtion

![[assets/slides/7Dtu2bilcFs/slide-017.jpg]]

OCR text:

> wee ~CiSCO (2024) = | ,
> , ry UB Ea o~
> _ ; - John Rauser, Senior fin BN Be EG
> / Director of Software 7 _—~
> Engineering as |
> - Anand Raghavan, a a
> Senior Director of ‘Ea. ———
> Engineering, Al 1 2 , : ag
> 6 Ld
> a "
> an Source hilps shades, ra vohihon com watch’ 1007959632 | Hef. smoroemen ees erence art —
> 2026: THE YEAR THE IDE DIED
> ene STEVE YEGGE GENE KIM
> Google DeepMind Software Engineer 3} Amp . Author & Researcher MPrevowmion

![[assets/slides/7Dtu2bilcFs/slide-018.jpg]]

OCR text:

> aa ~Vibe Coding Workshop For Leaders
> CZ
> ioe
> ees oo oe” f
> Engineering the future of Al

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
## Reconstructed Slide Deck
- [[youtube-7Dtu2bilcFs-reconstructed-slides]]
## Dense Scene-Detected Slide Candidates
- [[youtube-7Dtu2bilcFs-dense-slides]]
