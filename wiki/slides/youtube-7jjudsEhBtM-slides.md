---
title: "Slides: Skills are new features: Building Skill-Centric Harness — Yogendra Miraje, FactSet"
category: "slides"
video_id: "7jjudsEhBtM"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: Skills are new features: Building Skill-Centric Harness — Yogendra Miraje, FactSet

## Source Video
[Skills are new features: Building Skill-Centric Harness — Yogendra Miraje, FactSet](https://www.youtube.com/watch?v=7jjudsEhBtM)

## Relationship To World's Fair 2026
These slides are extracted from a verified official AI Engineer World's Fair San Francisco 2026 recording. Use them as slide and OCR evidence; official schedule pages remain canonical for titles, times, rooms, tracks, speakers, and affiliations.

## Related Scheduled Sessions
- [[2026-07-01-yogendra-miraje-skills-are-new-features-building-skill-centric-harness-for-agentic-products]] — Skills are new features: Building Skill-Centric Harness for Agentic Products

## Extracted Slides
![[assets/slides/7jjudsEhBtM/slide-001.jpg]]

OCR text:

> LAB & PLATINUM SPONSORS
> Amazon AGI Lab ANTHROP\C Google DeepMind MINIMAX
> OpenAl ZB ss akamar arize 2YS %Braintrust bright data
> B Srowserbase %docker -NEO4) ORAcLeE PayPal ¢&
> -y reducto (yy Sonar’ © togetherai (ff Unblocked €} WorkOS

![[assets/slides/7jjudsEhBtM/slide-002.jpg]]

OCR text:

> PRESENTED BY Skills are New Features
> a Microsoft
> a
> | I 5 ms :
> (a) cee.
> Engineering the future of Al

![[assets/slides/7jjudsEhBtM/slide-003.jpg]]

OCR text:

> EES yd
> “ “, ne ‘ s, .
> World's Fair Me i 9m How to Build Agents
> - gagae without losing the Control
> aS
> “" ee - fm Yoo: Mirae
> PRESENTED BY Pi tee
> a Microsoft
> y¥ Rutano! Summanze NVIDU'S prewous earnings call ,
> Bluepart y fe trasval Gather NVIDIA's latest EPS and revenue .
> Took Tame y Rear Suggest quoshons for the next oamings call based on all the information fetched
> M1 Regectog Generate a comprehensive report from fetchod informabon :
> Engineering the future of Al

![[assets/slides/7jjudsEhBtM/slide-004.jpg]]

OCR text:

> Al Engineer
> " Equipping agents for the real world
> World's Fair | a> with Agent Skills
> esis ceccoes Claude it porrerful but real work requires procedural knowledge and organizational
> context. Introducing Agent Skills, anew way to bull speciaazed agents using files
> and folders.
> panera
> co
> ae > jh
> ee
> OCON'T BUILD AGENTS!
> Build Skills Instead. .
> TRACK 3 + JULY 2, 2026
> a Alin Finance

![[assets/slides/7jjudsEhBtM/slide-005.jpg]]

OCR text:

> Al Engineer
> World's Fair |
> J
> What it’s NOT about sO Lala Re lorelvee
> TRACK 3 ¢ JULY 2, 2026
> Alin Finance

![[assets/slides/7jjudsEhBtM/slide-006.jpg]]

OCR text:

> World's Fair Al Engine
> If the agent is the interface,
> where do the features live
> World'sFair AEng TraCK 3· JulY 2,2026 Al in Finance

![[assets/slides/7jjudsEhBtM/slide-007.jpg]]

OCR text:

> rears | Who, What, How of an Agent
> System Prompt a Mre EY RYSe LIE
> TRACK 3 * JULY 2, 2026
> Alin Finance

![[assets/slides/7jjudsEhBtM/slide-008.jpg]]

OCR text:

> Pe Skills are New Features
> World's Fair |
> Wealth Management
> TRACK 3 * JULY 2, 2026
> Alin Finance

![[assets/slides/7jjudsEhBtM/slide-009.jpg]]

OCR text:

> Al Engineer ra a skill
> Hd's Fai Definition of a Skill e°
> oO s cs he abaty bo 40 sorereng wel
> A standardized way to teach Al agents how to do specific tasks
> well
> A shill is a dtectory Contain:ng, at mir:mum, a SKILL. ad file
> setll-rase/
> FE SKILL. # Required: metadata + instructions
> E/E scrapes? # Optbonal: ewecutable cade
> LE references/ # Optional: docusentation
> be assets/ # Optional: Cemplates, cesources
> es we & Any additional tales or directori¢s
> TRACK 3 * JULY 2, 2026
> Alin Finance

![[assets/slides/7jjudsEhBtM/slide-010.jpg]]

OCR text:

> Pe Basic components
> World's Fair
> Pr acta aaa
> a Microsoft
> NY SUG ni eed System Prompt File Read Tool
> TRACK 3 * JULY 2, 2026
> Alin Finance

![[assets/slides/7jjudsEhBtM/slide-011.jpg]]

OCR text:

> World's Fair A simple Skill Registry
> python
> registry=[
> frontmatter(open(f,encoding="utf-8").read())
> for fin sorted(glob("skills//SKILL.md"))
> Skill Description
> company-resesrch Createsa beginner-friendlyresearch brief abouta public company.
> roport-htnl preserving allcontent and structure. Turns Markdown Into a polished, standalone HTML reportwhile
> roport-pdf Fills,merges,and extracts data from PDF fles.
> O/&DDOO
> World'sFair TrACK 3· JULY 2,2026 Al in Finance

![[assets/slides/7jjudsEhBtM/slide-012.jpg]]

OCR text:

> World'sFair AIEngineer Discovery
> Python registry=[ frontmatter（open（f，encoding="utf-8").read（))1{path²:f} forfin sorted(glob("skills/→/SKILL.nd"))
> skills="\n".join（ f”-(s['name']}:（s[description']} （path:{s['path']}） for sin registry
> system_prompt=f**"You are a financial research analyst.
> Skills available. {skills}
> Feed one skill's output to the next skill's input.**. Read the skill that matches the task using the file_read tool. Ifa task needs multiple skills,chain them.
> World'sFair TRACK3·JULY2,2026 AlinFinance

![[assets/slides/7jjudsEhBtM/slide-013.jpg]]

OCR text:

> ESE sae ed
> elias | Descriptions are routing signals
> SOT Ta Geant Dan SOD ose) Ba Oe Be EA
> [red prom aggre +
> OCR RCT Th See
> TRACK 3 * JULY 2, 2026
> Alin Finance

![[assets/slides/7jjudsEhBtM/slide-014.jpg]]

OCR text:

> Pa Skill Routing at Scale
> World's Fair |
> ee Retrieve Structure
> TRACK 3 * JULY 2, 2026
> Alin Finance

![[assets/slides/7jjudsEhBtM/slide-015.jpg]]

OCR text:

> Pe Skill Library Governance
> World's Fair |
> Roe rnSe eS Enep iraecere
> r )
> TRACK 3 ¢ JULY 2, 2026
> Alin Finance

![[assets/slides/7jjudsEhBtM/slide-016.jpg]]

OCR text:

> Al Engineer
> World's Fair |
> We can borrow many good practices that have
> worked for code and apply them to Skills
> maintenance & governance
> TRACK 3 + JULY 2, 2026
> VB aba alae

![[assets/slides/7jjudsEhBtM/slide-017.jpg]]

OCR text:

> AlEngineer
> World's Fair

![[assets/slides/7jjudsEhBtM/slide-018.jpg]]

OCR text:

> EES ed
> “ ra _. - ¥
> World's Fair Me i 9m How to Build Agents
> - gagae without losing the Control
> a ee ail ; Yoo: Mirae
> PRESENTED BY ae Wee = aan
> a Microsoft
> y¥ Ruta! Summanze NVIDU'S prewous earnings call ,
> Blueoart y fe trareat Gather NVIDIA's latest EPS and revenue :
> Took Tae y Breast re} Suggest queshons for the next oamings catt based on all the information fetched
> M1 Ropecton Generate a comprohonseve report from fetchod informabon :
> Engineering the future of Al

![[assets/slides/7jjudsEhBtM/slide-019.jpg]]

OCR text:

> AlEngineer
> " Equipping agents for the real world
> Weta te hele | a> with Agent Skills
> PRESENTED BY Neetu eooay Claude is powerful but ceal work requires procedural knowledge and organizational
> Context. Introducing Agent Skits, a new way to Dulid speciakzed agents using flies
> a Microsoft
> ea
> — ns
> er ie |
> lA a ~
> OON'T GUILD AGENTS!
> Build Skills Instead..,
> TRACK 3 ¢ JULY 2, 2026
> ae Alin Finance

![[assets/slides/7jjudsEhBtM/slide-020.jpg]]

OCR text:

> Al Engineer
> World's Fair |
> "A
> What it’s NOT about What it IS about
> TRACK 3 ¢ JULY 2, 2026
> a Alin Finance

![[assets/slides/7jjudsEhBtM/slide-021.jpg]]

OCR text:

> Al Engineer
> World's Fair |
> a Microsoft Adding Skill Support in Harness
> an Alin Finance

![[assets/slides/7jjudsEhBtM/slide-022.jpg]]

OCR text:

> PEs od oes sa skill
> Hd’s Fai Definition of a Skill o°
> ol s air he abby 3b 40 someting wed
> A standardized way to teach Abagents how to do specific tasks
> aan
> A skill is. a drectory contam:ng, at micrmum, a SKILL. ad fle
> skh -nase/
> -  SNILL.nd # Required: metadata * instructions
> EK seraots/ # Optbonal: enecutadle cade
> LE reterences/ # Optional: docutentation
> Ke assets/ # Optional: teaplates, resources
> Le eee a Any agditional tiles or directories
> TRACK 3 + JULY 2, 2026
> Alin Finance

![[assets/slides/7jjudsEhBtM/slide-023.jpg]]

OCR text:

> AEngl HTML Report
> World's Fair NViDlA Corporation:Research Briet
> O/&四DOO
> World'sFair AlEn TraCK 3·JULY 2, 2026 Al in Finance


## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
