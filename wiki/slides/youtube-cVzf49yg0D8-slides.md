---
title: "Slides: Building Conversational Agents — Thor Schaeff and Philipp Schmid, Google DeepMind"
category: "slides"
video_id: "cVzf49yg0D8"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: Building Conversational Agents — Thor Schaeff and Philipp Schmid, Google DeepMind

## Source Video
[Building Conversational Agents — Thor Schaeff and Philipp Schmid, Google DeepMind](https://www.youtube.com/watch?v=cVzf49yg0D8)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/cVzf49yg0D8/slide-001.jpg]]

OCR text:

> PLATINUMSPONSORS
> $ Braintrust
> Workos
> OpenAl

![[assets/slides/cVzf49yg0D8/slide-002.jpg]]

OCR text:

> One API to
> Rule Them All
> AIEng
> EURO

![[assets/slides/cVzf49yg0D8/slide-003.jpg]]

OCR text:

> eee einen nna eee as
> i
> |
> |
> nn!
> F id a
> ee -
> Se gt ix
> as ;
> ie ¥
> At _—

![[assets/slides/cVzf49yg0D8/slide-004.jpg]]

OCR text:

> Chro
> WedAor813:08
> Ose APi lo Rule TheA:B
> taistudio.google.compromptshew_chat
> GoogleAI Studio
> Playground
> （>Oetcode
> GX
> Playground
> Gemma431BIT
> AME2026Score
> pmg-4-31b-5
> gleDeepMind'sTlagshpopen-weighe
> ema2310 TMo
> ExploreGooglemodels
> eodepba
> Hteuo
> 256Kcontextwindowandsdv
> ma
> Secure Cioud Run Service Acc
> Gcloud Login Wh Base64 JSON
> System instructions
> Featured
> Code and Chat
> View ali history
> Image Generation
> 2Buld
> wthGemi3
> No API Key
> Dashboard
> Swch toa pad APikey to unlock higer
> qucta aod more feetures
> Documentation
> Video Generation
> Speech and Music
> Real-time
> Temperature
> Explore our text to speech and music
> Real-time voice and ic
> Gemini Lve.
> eowith
> ceneration models
> mode's
> Media resolution
> Default
> -bupnqes
> Thinking level
> ubject to the Gemma Terms o
> Use
> High
> QSearch
> QWhat'snew
> GetAPIkey
> Structured outputs
> ③Setings
> B8Tools
> GGrounding withGoogle Search
> ognoaxapo
> schmidphllpp1995@

![[assets/slides/cVzf49yg0D8/slide-005.jpg]]

OCR text:

> Ce i oe nee eS © 6a @ FF w@ . EF weet
> ° ; a / @ °
> A :
> Google Al Studio \
> API-Schliissel 3D APL Kur zantedung fe ADL-Schtussel erstesen
> Pasnboara
> APESchtussel ‘
> Cucpee cor © API-Schtussel Proyeict oa 10 Ale Prowate »
> Projekte
> Mass Scnhissel Preyeht Eestett Aten maungestute
> Rotvabeqrenzur|
> Auagaben
> AD ee haung
> Protoagiie und Datasets
> Arderungupotoket *
> Gre konnen Inte AM -Schiussel her nicht finden?
> Proyckte importioren
> + Search ,
> 1. Yenat snee
> + Get APL key
> Ih Setings
> @ vc rerdpr ppl gonce

![[assets/slides/cVzf49yg0D8/slide-006.jpg]]

OCR text:

> , ; OS ae
> Race i . Pooh!
> 
> aos ; : J i
> 
> ahs an

![[assets/slides/cVzf49yg0D8/slide-007.jpg]]

OCR text:

> PR eC cS cet oi oT od Gor G6 & & CB SF mw © sects
> bs ‘ ad °o
> ‘
> 
> J
> J
> 
> Al ENGINEER EUROPE - WORKSHOP
> 
> ae
> Building Agents with the Gemini Interactions API, from zero toa 5 os a
> working agentic application in 60 minutes.
> Pk git ee aR ol ee ona
> © 60 min: ive Coding =A Philipp Schmid

![[assets/slides/cVzf49yg0D8/slide-008.jpg]]

OCR text:

> Oe Cn ee OR ee CO a . i ne ce err ers
> CJ a a ry
> Part 1; The Interactions APi
> Core Primitives
> .
> 
> a OO ———————————————————————————————————————— OR _—_—eeeeeeeeoeeee
> C
> , © Server-Side State * Background Execution
> 
> Be Ce eh Ma aes Ge OST a Le OPM MER Cle as ste aed
> 
> Pana)
> Chain turns with peectous ieteractice <3, Server owns conversation Fire-and-forget for long tasks Poll with .-re-o:tors getiagi.
> history.
> Ov
> (3 Typed Output Blocks © Streaming via SSE
> € irteraition cutouts raat client isterectiors
> Pera Ca
> oe mas ae
> a i. f
> ai
> Flat areay: vert, totic all amage, teat?
> RICN EVENS: coment aaling ierer action rome tere.

![[assets/slides/cVzf49yg0D8/slide-009.jpg]]

OCR text:

> Help 口 Aor813:19
> Code Comparison Part 1:The Interactions API
> GENERATECONTENT INTERACTIONSAPI
> r1·client.nodels.generate_content( Stateless:re-send history every turn contents-[ ("inline_dato”:(mime_type":*imoge/jpeg” ("text":*Describe this inoge") "doto：...")) i1-client.interactions.createc model-'gemini-3-flosh-preview input-[ 1x01.0d1.） fou.:od1.) "uri":"https://... 6od/ou.:odou
> i2-client.interactions.creote( Request 2:Just-send new Input
> r2client.nodels.generate_content( model-'genini-3-flosh-preview" contents-[ previous_interoction_id-i1.id input=*Is there any text?
> ("inline_doto”:("mime_type”:“imogo/jpeg” ("text”:“Describe this inoge) "doto:"..."))
> ("role":"model" osn,oo.) （[（oo1odo.Ix）]1d （[（22x）u0o4）sI.x.）]:s1od
> Access:response.condidates[e] content.ports[e].function_coll
> 8/17

![[assets/slides/cVzf49yg0D8/slide-010.jpg]]

OCR text:

> Pe en Ca eT ©: GO ek OF @ LE meters
> e . a 5 °
> 
> Part 2: Building Agents
> Co
> . © HOW IT WORKS
> : @ Send request: prompt - tool definitions erence
> 
> e@ Check outputs: look for function_call blocks o 5 5
> 
> e@ Execute locally: run your function code
> 
> oe Send results back: as function_reault re rrr
> 
> e Repeat: until model returns text sheet So
> 
> ee : ee Sa
> No history management
> OQ Sevver tracks na meracton 10 SO Aromatic ma ; foot re
> prenous meracton teak al

![[assets/slides/cVzf49yg0D8/slide-011.jpg]]

OCR text:

> Boma et em ety Teetany Teta Cat Aeon oe Ca or i ne SC cee)
> e ry
> 
> c a 4 o
> 
> mee
> é Goo Ke
> id Gg
> Q Seacm Goze o type a URL $ BS @Amove
> 5 : . : , 4,
> ' - a

![[assets/slides/cVzf49yg0D8/slide-012.jpg]]

OCR text:

> Cursor
> Fle
> Selection
> Vew
> COGCL
> dAor813:25
> SLLmX
> ageetsskis)
> SOLLmd
> GeiasInteractons AI Saill
> Curre Nodes （Ose Tese）
> woratep
> nan.Py
> -flavitftlncedfct
> n-3.1-gr-evie：tesclereanng,coding,reearch
> (ss-lock)
> geaini-3.1-flash-ite-srevjev1cost-efficient,fastest perfarance forhigh-frep
> p-3---ee:5/3ktes,igrataeanitng
> oei-2.5-re tescmlexresaning.coding.resarch
> gemini-3.1-fLash-1nage-greviev65/32k toens,pegeerationandediting
> geisi-2.5-flsh:tokens,fast,bolanceperfonnce,muttiaoda
> Current Agents （Use These）
> e-resrc-r-pei-12-225：DgResrchagt
> [NG]
> Carret SoKs Cse These）
> 5cript/Tyecripteogle/gal1.33.neInstalL@google/gea1
> LICAUTTON)
> egogie/pnerative-al（25）srydeprecated
> Opt
> Pors
> ToolCatls!
> （-0x9)
> Soccess Rater
> Perferm
> otLTIel
> 2h3225s
> entActivel
> APT Tiae)
> Tool Tinel
> 9s(0.)
> hlscmld-ec[13:25:21][-/grects/ale
> -itteractioes

![[assets/slides/cVzf49yg0D8/slide-013.jpg]]

OCR text:

> , _ l
> _
> ee Tr
> nn a a
> an

![[assets/slides/cVzf49yg0D8/slide-014.jpg]]

OCR text:

> d Profies Hee 1327
> README Apache-20 lcene Security
> SkilfordevepingGeni-oweredappsPrvidesthbestpracticesforbuldingapps
> vertek-al-a2l- SDK.Covers tools,multmodageneration，caching.and batchprediction.
> Sev eini-live-apl- Wbtsaciy Skilfrbuldingreal-tmebidiectonlstrengappswiththe GeminiLeAPCoers features,function caling.and sessionmanagement.
> interactions-apl peeini- e chatsngfllingsttredtegrne agentsdeprecatedmodelguardralsandbothPythonand TypScriptKs
> Installation
> Youcanboweandinstal skilsuingeithertheelskillsCLrtheContext7skisCLL
> UsingVercel skillsCLI
> npx skillsaddgoogle-genini/gemini-kills-list Interactively browe and install skills.
> Instatl specific skill (e.g,gemini-api-dev). npx skills addgoogle-penini/genini-skilts-skillgenini-ap1-ev-globo1
> Using Context7 skillsCLI
> spxcbx7 skills1nstatt/google-gemin1/gemin1-skills Interactively browse and install skitts.
> npx ctx7skills instal1/google-geaini/gemini-skiltsvertex-al-apl-dev Install aspecific skilt （e.g.,vertex-al-api-dev）.
> Disclaimer
> Vulnerabity RewardsProgram.

![[assets/slides/cVzf49yg0D8/slide-015.jpg]]

OCR text:

> Pe et er ce ed © > 6 Ok OF @ . EE oaetetcry
> ee sie-workshop — main. py Open Agent Manager 03 (0 2 EB ea @
> @ manpy x — 1) Walkthrough t2 Task @ impementation Plan > C €& > + Creating Agent Class Structure 7S x
> wet og Me rarity
> 39 Class Agent: Next wo need to add a read_filo and write_tike tool.
> 69 def runiself, input_text: str | listh -> ste: . Create a basic python anplementation and atso the json
> Ba for output in interaction.outputs: schema defition and map for the key: function, schema *
> a9 Af output. type e2 “function_cali":
> 92 if outout.nane in self. tools:
> 1 TESMEL = IMC LAGE LULSa RL eeUUK pul el yume Ara sora CQ selupen
> % except Exception a1 ¢:
> 47 result « f"Error executing tool: (strie)}™ . Analyzed @ agent.py: ”
> a8 else: .
> a result © (Error: Tool "{output.name}’ not found.” Vriagnt tet os
> 7 180
> 181 Prantif*OEBUG: Tool Result -» {result}”) Detining New Tools
> 1e? PL ALLALENO BRE 4
> 183 # Fospat the result as 9 function result biock SolUtion/agentapy tag .de re THe task st
> 18s tool_results. appendi { er , ee TINE TF
> HE BOE Ot snd we ce ws
> res type": “Sunction_result", ee eee eee ees
> 326 “calt_ie": output. id, workshop/main.py om sore por the Sy th or
> 187 "heme": output.nase, hp emestabars Ire GION ache ydeGstocs ane
> 1e8 Tresult": ste(resulet . Nap So Cee reel eR hte paesg to dy fob and
> 129 » neg
> io
> in a tf the eotel requested toot calls, we eust send the results back and con Fates tide -
> 12 if tool_results:
> -
> m return self. runitool_results) Edtec implementation Plan
> ws # Return the teat frow the last output Gloca tususily the final response 6 I nave created an implementation plan to ada the
> 36 return interaction.outputsi-1}.text oxy ;
> iw read_fite and write _file tools tothe Agent . Ths
> 118 def masini): includes ine Python rplementations, JSON schemas, and
> # Instantiate the agent updaing the agent's mteracton loop ta handle tool calls.
> agent = Agent() e e Be ray Co acces
> @ First turn wo
> erint("-—- Turn 1 --—")
> question! = “Hi Reet: = 7 oy Parag 0 devin Veta os
> ee ae | CRP RMT LE To dct a ot A a ee ea oe SCT a)

![[assets/slides/cVzf49yg0D8/slide-016.jpg]]

OCR text:

> P|
> le | oe?
> " “3
> Pie
> oar
> oy
> ore
> os ns fa
> “as
> ! oe
> ! Tut
> i Fe
> | are
> | Cts
> aie
> . Ee
> rs
> B aF
> ;
> a
> ov
> ' om a  . .
> | : li |
> ; y,
> _
> s oy

![[assets/slides/cVzf49yg0D8/slide-017.jpg]]

OCR text:

> Gemini 3.1Flash Live
> AIEr

![[assets/slides/cVzf49yg0D8/slide-018.jpg]]

OCR text:

> nenu aistudio.go Lcom/a0ps/32166532-e57d-4375
> [Public] Live Jukebox Remix o Device
> Live uhebox
> POWEREOBYGEMINILIVESLYRIR
> SESSIONLOGS OTRROKS
> STUOIDR SESSION
> No tracksgeneratedyet Wish fora song to begin.
> WAKNGLPTHEOLL
> TALKTOOU
> Text the DJyoutrequnst.

![[assets/slides/cVzf49yg0D8/slide-019.jpg]]

OCR text:

> ~- = te f Bt te
> Na |
> eA Lo
> re oe
> oaar
> i ne
> Boe:
> an a ARS
> | ee
> 7 Co eee XS
> , ye
> a
> , ec f a.
> 7 |
> Zz
> ’ =<
> A

![[assets/slides/cVzf49yg0D8/slide-020.jpg]]

OCR text:

> °
> Live API
> The Live API enables low-latency, real-time voice and vision interactions with Gemini.
> ese Text, audio, video
> “ee Text, audio +
> App Connect via WebSocket Live API

![[assets/slides/cVzf49yg0D8/slide-021.jpg]]

OCR text:

> a 5 _ oe
> ro) A Ey . :
> Google Al Studio - = Playground =
> BS Playground >
> % eula , :
> i A
> Ge Dasnboara > ld a A,
> 7 i
> 1% Documentation 2 \
> id a EB
> Voice
> > CoO/00e —— @ |
> Media resolution
> What do you think of my outta?
> hse Thinking level
> v
> Ph 000/000 —=—
> Well now, you're lookin’ very smart so you are!’ That green packet sutts you wed, | must say. A grand casual look. Sear ce Crepe os
> Were you tunkin' of headin’ out somewhere?
> OD) eee Atereesey many Mane MeAtaRes by oui ERR CARE
> Disconnect renee A
> & Search xe
> Streamistve 8 Function caikng e
> C Wat's new
> exe Get APL key Suart typ ea prow pe Automatic Function Response e
> ® Sersngs
> + 8 O Grounding wth Google Search
> @ thorsten schaetterg "a ®

![[assets/slides/cVzf49yg0D8/slide-022.jpg]]

OCR text:

> wooabooon
> D
> GoogleAI Studlio
> Playground
> Choose what to share with aistudio.google.com
> Run setings
> <>Getcode
> s oA o
> Playground
> Chror
> Window
> Bolld
> System instructions
> CoDathboard
> Documentation
> Yeah.
> Voice
> Ah,hello there! Whatrat
> Mediaresolution
> Thinking level
> Q.Search
> Stream is live
> Function calling
> 0what'snew
> Get APIkoy
> Settings
> GGrounding with Google SearchX
> Grounding with
> Source:G
> thorsten.schaeff@g
> Google Search
> Google Search

![[assets/slides/cVzf49yg0D8/slide-023.jpg]]

OCR text:

> 4
> iy Peck G9
> tT Lk peat Le ge 7
> : | ¥ Cr A ade a j 4 i at awe) an] a Eco f.. . x q 1
> ar pe ees op <a Pe “) ee oe er
> ..- Smilin ae
> toa ee a i é i a us i
> a a rs ee.
> ‘oo 5 ig an ne a en re { . 4, &
> a : ee UP eee es . 7 pan 3
> a, es BO ps Fa een mer _—
> ae oe ne ; “as 7 7 rer,
> - aaa ie on r yy oe aa) es yt!
> < a Ps Ld ‘ a a * il ae
> a a i a an aN H
> nn ce : _— Se ors ;
> i
> a 7 aie at ono oe Oo
> , aan | ie ware
> _ id —
> ,
> cu |: cae ome

![[assets/slides/cVzf49yg0D8/slide-024.jpg]]

OCR text:

> ged mi
> Be — re pi
> oe aes iy ot
> eee Pavel so anne ri
> ‘ea te ee -~ :
> a % ®
> oe 4 7 Big ;
> Pe ae! ieee at ce
> an . roa
> oe al Brot 399
> ‘ty ;
> rf A
> ; :
> FAT Sawn
> c I ao os rn ry “oy r s aad avr "@ a + a oe
> — i aa *. 2° : .
> a a Pe _. eee eo:
> Geman

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
