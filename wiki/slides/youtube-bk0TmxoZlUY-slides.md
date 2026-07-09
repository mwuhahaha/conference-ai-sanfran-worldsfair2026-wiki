---
title: "Slides: Evals 101 — Doug Guthrie, Braintrust"
category: "slides"
video_id: "bk0TmxoZlUY"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: Evals 101 — Doug Guthrie, Braintrust

## Source Video
[Evals 101 — Doug Guthrie, Braintrust](https://www.youtube.com/watch?v=bk0TmxoZlUY)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/bk0TmxoZlUY/slide-001.jpg]]

OCR text:

> INNOVATIONPARTNER
> aws
> PLATINUMSPONSORS
> Graphite
> WWindsurf
> MongoDB
> daily
> augment code
> Workos

![[assets/slides/bk0TmxoZlUY/slide-002.jpg]]

OCR text:

> BRAINTRUST OEY o®
> braintrust
> P-END DEVELOPER PLATFORM
> NG AI PRODUCTS
> i
> i |

![[assets/slides/bk0TmxoZlUY/slide-003.jpg]]

OCR text:

> Agenda
> 
> e Company Overview
> e Intro to Evals
> ENIAC CIOL
> e Moving to Production
> e Human inthe Loop
> 
> oo
> 
> | ~~]
> - ~~

![[assets/slides/bk0TmxoZlUY/slide-004.jpg]]

OCR text:

> Braintrust at a glance
> & e.) AnKur Gaya: S| ROHN ria ean >$45m
> Ea Investors and Al teaders
> eae CRBC anette erste al6z ee ;
> » Cher nema om
> 
> Pac laire) Microsoft 3 DATADOG dbt Labs zapier =| Grafana
> 
> ee Ca re amazon nuro ~ instacart STS
> bd
> 
> VF fai)
> | aMicrosoft oy)
> me F

![[assets/slides/bk0TmxoZlUY/slide-005.jpg]]

OCR text:

> rd
> We support leading Al teams
> re NETFLIX Nite ra tals):
> ‘instacart “% Airtable zapier BN akessoni
> replit eae ears ramp 4 AVercel
> Sueno oa Robinhood # SAD cele) erey4 mem TES Cr]
> Klarna. coursera ® docusign Webflow
> ‘
> q a Microsoft ary?

![[assets/slides/bk0TmxoZlUY/slide-006.jpg]]

OCR text:

> g ase € cary TO gone
> Weriting evats is powng to become 8 core skill for product Evals are emerging as the real moat for Al startups ovals are surprisingly often all you need
> managers fo such 9 crticad part of moking & £000 Nard won insights about customers and thew business ON
> Product wath AL hoger diecovered by fourniens acteng ainost ae
> etnographers spchunking in the underserved slices Of the
> GOP pre chaet
> tame meee QrXenmeeMon © wwe
> The bee A aided ade Rm Mae a nEE oF Ly TaN oe het
> fmentan a tate
> Uf there 6 one thing we Can teach people, 4 that
> Writing evais ia probably the most important theng. Be tone he ween Fa et cottawes ears
> x
> a

![[assets/slides/bk0TmxoZlUY/slide-007.jpg]]

OCR text:

> ; Td)
> Why evals? Evals help answer questions
> Model selection How Gets Al Cost efficiency
> "Which LLM is the perform across "Can we achieve high
> best choice for our diverse real-world performance without
> needs? “nee excessive costs?
> scenarios?
> ‘ Debugging & regression
> i Bea te At oletl Feedback integration detection
> reflect our compan fs “Are we learning from “How do we know
> : 7 y users and improving when something
> onde ae 5° iteratively?" breaks or gets
> standards? worse?"
> a

![[assets/slides/bk0TmxoZlUY/slide-008.jpg]]

OCR text:

> ®
> How evals can help your business
> Cut dev time Rapid heraton cycies & local tested on multiple LLMs seamlessly
> Reduce costs Autontated evals replace manuel review alowing faster eration ¢ release
> 
> Enhance quality Real time nonttoring & compliance to redcce risk and improve Cx
> Sca le iets aahs Enabie non-technical collaboration to puda tie best Al Apps
> 
> Ie never seen a workfiow transformation jike the one tnat incorporates
> 
> evals Into ‘mainstream engineering’ processes before. it's astonisning.
> 
> eit
> ,
> | a Microsoft @yr{?

![[assets/slides/bk0TmxoZlUY/slide-009.jpg]]

OCR text:

> Z e
> Customer outcomes
> zapier coda Notion
> fe)
> oe
> [OlOROTOLOLOTe)
> all [OlOTOTOTOLee)
> = Te eYNars
> op. YAO) 50%
> ®
> a a Microsoft Gry?

![[assets/slides/bk0TmxoZlUY/slide-010.jpg]]

OCR text:

> rT
> Core concepts
> Prompt engineering Eb Al observability
> ares | ey ee fat Tosrorese ce regres? Cee mn et aoe ae ee
> aes eG aa aS Panera DE gee ae doe MO Pecug, eel
> bs
> | a Microsoft Gxcl®

![[assets/slides/bk0TmxoZlUY/slide-011.jpg]]

OCR text:

> . ; rd
> What is an Eval?
> Definition: An Eval (short for evaluation) is a
> structured test that checks how well your Al
> system performs. It helps you measure
> quality, reliability, and correctness across
> scenarios.
> i.
> aws
> 7 Nae!

![[assets/slides/bk0TmxoZlUY/slide-012.jpg]]

OCR text:

> 3 Ingredients in an Eval
> DATASET SCORER
> ~The loqie behind your
> The code or prompt you evals,
> want to evaluate. : r
> Can be oan
> -It can range fron a (Ce been RUC ke Co] en ee
> single prompt to un A set of real-world Cede funetion
> entire agent workflow. exarples, mearear 5 —
> The scorer will give a
> Requires an input and “These are your test score of B 108 to each
> RTeTeesTiny fen rare row in the dataset
> i 3
> OS
> bg
> | u

![[assets/slides/bk0TmxoZlUY/slide-013.jpg]]

OCR text:

> - ®
> There are two eval mental models
> Offline Evals
> What aos
> ee ee eee te Cs ies CRORE SLES ALC ASO CSCO ESL
> prodefiness dafasutss. elmer el bran UG.
> Pe Caeser Mace cate (Samael Ce] Sar] ea Ca Re COS a tar 6 eae OTD 0201 CoE Ld CACLOSLLEOSSE STOOGES
> aca my
> EN reas
> ©) Proactive yident fy aed reso ve issues [rears 10881 Os- SSeS TOT Chat OE AATO] RIN OTe 1s tS] ELAT7 Tak CRE Ea
> RiGee eee ae ol aea aE ery Str Rome Ober tame] O20) 60s ee ort |
> Seren avy
> e@)) Create and marace evaliition datasets © Astometlicaly Vace cals usng prory or SOK,
> ee) Define tess and scorers e osu fi hercandyveses p Grainteust Gbts araive
> Ppa NASI een STCa teat erate eer aie etsy TST re
> Satta ry ao arene eG eee race mee rs era Gd eer
> x
> a a Microsoft §=o(oou®

![[assets/slides/bk0TmxoZlUY/slide-014.jpg]]

OCR text:

> . Td
> What should I improve?
> 71)
> [ale] rome o) Improve evals
> 5 Improve evals Improve Al app
> ry
> a u

![[assets/slides/bk0TmxoZlUY/slide-015.jpg]]

OCR text:

> Page ee ste eee a ee One a °
> Sarees Ce ae wwwy ities
> ea cena ey re en mes pape
> sto: bare tbat erat
> eid be ne ra a ae es Ce met
> cad
> Pires ne Mos Mec eee re ~—
> . ces :
> e a Ree eta 7
> . BS eee eau: s
> Porragighte, © ey mee atles tyler: wile ccecadgtio s __
> or ee ae aa aero
> Fem Cert eee corey cae cana ~
> Bree ee ee
> Petia
> [az
> re mntunt
> x
> ~

![[assets/slides/bk0TmxoZlUY/slide-016.jpg]]

OCR text:

> , , r
> Datasets - Tips
> Cees) Te apcvb arses Tae codes 1 Con
> focus on building a feedback loop rather than
> a perfect dataset
> e §=Never Stop Iterating:
> Use Logs to capture more edge cases and
> create more holistic Evals
> Cas occ ea lee Lelpe TAM Sale Ee
> use human review to establish ground truth
> Especially when using expected column
> a
> i : oO
> a a Microsoft

![[assets/slides/bk0TmxoZlUY/slide-017.jpg]]

OCR text:

> BRAINTRUST.DEV
> Scorer Types
> Code-basedscorers
> LLM-as-a-judgescorers
> Exactorbinaryconditions
> Subjectiveorcontextualfeedback
> AIE
> Numericcomparisons
> Human-likeinterpretation
> Structuredorfactualchecks
> Improvementacrossmultipledrafts
> Microsoft
> smol?

![[assets/slides/bk0TmxoZlUY/slide-018.jpg]]

OCR text:

> : ®
> Scorer Tips
> Use a higher-quality model for scoring, even if the prompt uses a cheaper
> model. Scorers benefit from better reasoning and nuance.
> Treat scorers like judges: evaluate intent match, style accuracy, and
> overall output quality: -not just correctness.
> Break scoring into multiple focused scorers (e.g., accuracy, Creativity,
> formatting) to pinpoint issues.
> Test scorer prompts in the Playground before use. Try strong and weak
> outputs to refine scoring reliability.
> Avoid overloading the scorer prompt with context. Focus if on the relevant
> input and output for fair, consistent evaluation.
> ty
> | u

![[assets/slides/bk0TmxoZlUY/slide-019.jpg]]

OCR text:

> BRAINTRUST.DEV
> Playgrounds
> Experiments
> Evaluations
> AIE
> QuickiterationofPrompts,Agents,
> Greatforcomparingfullexperimentssoyou
> Scorers,Datasets
> canreviewpastplaygroundsessions
> GreatforcomparingPrompts&Models
> EvalsfromSDKorAPIwillappearhere
> Whenvoureachahappyplace,savea
> directly
> otoftheplaygroundtoExperiments
> Youcananalyzeyourexperimentsovertime
> Microsoft
> smol?

![[assets/slides/bk0TmxoZlUY/slide-020.jpg]]

OCR text:

> ce eee Re ; a came — — . | . . eee }
> 
> = :
> 
> 7m | :
> EE Evals via SDK ° |
> mB |
> 
> es | . "
> b O607"O0880-84° HE -*28”
> 
> 2
> a a Microsoft @yr{?

![[assets/slides/bk0TmxoZlUY/slide-021.jpg]]

OCR text:

> gS Hae , en @r
> f Rene ares H
> eet COREE a Rte Be te es ee |
> [Dee Eee Ce :
> .
> Leon ee eee ne)
> io Pe ety Peer reece tad !
> Peete Ceara Serra |
> a sIU is Mae Cony |
> bot ee an oe :
> Cares Pree eee ee
> ron
> —_— 3
> 3 s a ad
> b G4G7* "0880-84" Hi -*2 8
> bd
> +

![[assets/slides/bk0TmxoZlUY/slide-022.jpg]]

OCR text:

> on Pemareatt 3 ek m —)
> 
> gegen .@ y
> 
> Ong tenes rome e
> Poeqoete ea - _ ote
> Gers Sve on bee yon o tas o vee ee
> 
> 6 Rta ane
> 
> leterste sranjeog pees a een @ lon wan
> amines
> siersarrerinconspereg’d we a ee Qt tee
> 
> Urvecemtas AI
> 
> + inewssente
> 
> 3 Cater nents
> treet
> 
> Wages
> eanypece
> vet eney &
> secgng laceretne Lee
> Bie ote
> 
> raintrust
> a
> i an i * ,
> b CO607 "QO880- 84° 6 *
> co
> ; aws

![[assets/slides/bk0TmxoZlUY/slide-023.jpg]]

OCR text:

> app.py
> dsdosnd
> SEARCH
> code_conversion
> push_prompts.py
> prompts.create
> Ieport os
> import braintrust
> fies to incu
> from code_conversion.agents Iaport INSTRUCTLONS
> es to eickido
> project =braintrust.projects.create(nam
> s.enViron[“BRAINTRUST_PROJECT_NAME"])
> AIE
> project.
> pts.createl
> 1resultn1fle-Openineditor
> nanea*Code Conversion Prompt",
> push_prompts.pycods
> slug=code-comvers1on-pronpt",
> project.prompts.create(
> descriptionaThis prompt is used to comvert
> promptaINSTRUCTIONS,
> model-os.environ["OPENAI_HCOEL_NAE"],
> messagesa!
> (“role”："systee，“content：DNSTuCTINS）,，
> ("role”："user,"content”："《（input))”).
> Microsoft
> smol?

![[assets/slides/bk0TmxoZlUY/slide-024.jpg]]

OCR text:

> FS
> Tsresources.tsx
> braintrust>Ts resources.ts
> app
> choicescores:
> api
> fair:0.5,
> generate
> Poor:0.25,
> globals.css
> ayout.tx
> AIE
> page.tsx
> braintrust
> exportconstaccuracyScorerproject.
> createlc
> Tsresources.ts
> name:"ChangelogAccuracyScorer",
> EE
> sLug:"changeLog-accuracy-scorer",
> I
> H
> description: “Evaluates theaccuracy of a generatedcha
> eval
> ressges:[
> 1ib
> rsbraintrust.ts
> rolei"systen",
> Ts constants.ts
> content:
> You are evaluating the accuracy of a changelog gemerated from aList of git commits.
> Tsutils.ts
> *TaskelRate how accurately the changelog represents the actual changes described in the conmits.
> pubic
> ProblemsOutputDebug ConsoleTerminalPorts
> scripts
> at callback（/Users/dpg/repos/ai-worlds-fair/node_modules/.pnpm/braintrusta0.0.205_openaia4.47.1_reacta18.3.1_sswr@2.2.
> papm
> 0_svelte@5.33.1__svelte@5.33.1_v_b3826b4d9a1ae52bd8efbc9af546b03b/node_nodules/braintrust/dist/cli.js:6905:26）
> env.localexample
> gitigrore
> ()prettierrc
> Finished running experiment
> ents.lson
> Microsoft
> smol?

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
