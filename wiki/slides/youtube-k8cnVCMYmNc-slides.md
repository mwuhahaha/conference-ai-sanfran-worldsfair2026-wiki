---
title: "Slides: OpenAI + @Temporalio : Building Durable, Production Ready Agents - Cornelia Davis, Temporal"
category: "slides"
video_id: "k8cnVCMYmNc"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: OpenAI + @Temporalio : Building Durable, Production Ready Agents - Cornelia Davis, Temporal

## Source Video
[OpenAI + @Temporalio : Building Durable, Production Ready Agents - Cornelia Davis, Temporal](https://www.youtube.com/watch?v=k8cnVCMYmNc)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video that matched one or more scheduled World's Fair sessions by speaker. They are supporting context unless the video is later confirmed as the exact session recording.

## Related Scheduled Sessions
- [[2026-06-30-cornelia-davis-mcp-tasks-async-why-the-heck-aren-t-any-agents-supporting-mcp-tasks-async]] — MCP Tasks (async)/ Why the heck aren't any agents supporting MCP tasks/async?

## Extracted Slides
![[assets/slides/k8cnVCMYmNc/slide-001.jpg]]

OCR text:

> th lemMpOrat
> . =
> 7
> 1, | ar _
> ‘ 4 ~ =
> 4
> .
> 8 |
> La , ae
> a : : .
> ho s aNd
> ose : 4 .
> an i , | es Perry
> . a nt SS Sonate
> i? * SS een

![[assets/slides/k8cnVCMYmNc/slide-002.jpg]]

OCR text:

> e Developer (wasn’t Ops) Fa
> i Ni d N
> e Web architectures for 20+ years > OU ative
> +3 ; )
> e Cloud-native for more than a i hid atterns
> decade a ; a
> e Cloud Foundry for 8+ years ‘ f a iA joi [ tae
> * Kubernetes for nearly 10 , acer
> e Author « hE ¥
> Developer Advocate, Temporal i
> BE ccs,

![[assets/slides/k8cnVCMYmNc/slide-003.jpg]]

OCR text:

> says t A
> pled
> rs
> 7
> 1 |
> |
> t | { i
> . cnt
> cee Bocca
> Perret BAM aleetatetc icy se OOS
> os ee Me A one ; 7
> i a Pama RRR SRR ROAR
> 1 Ser eee $e ANSSSie
> : Se wow nn aR 4 SS Rice
> ae oe On B ee
> = a _ ae

![[assets/slides/k8cnVCMYmNc/slide-004.jpg]]

OCR text:

> Agenda
> Vv OpenAl Agents SDK
> Vv Temporal Overview
> <Y Durable OpenAl Agents (Temporal + Agents SDK)
> oY Mae OST Late Ws ( nS
> Ps

![[assets/slides/k8cnVCMYmNc/slide-005.jpg]]

OCR text:

> Follow along and play with our samples by accessing
> our Jupyter Notebooks here:
> cw
> a esa

![[assets/slides/k8cnVCMYmNc/slide-006.jpg]]

OCR text:

> What's an agent?
> 
> An agent is an Al application “
> 
> consisting of a model equipped “ee
> 
> with instructions that guide its tes r T ry erste
> behavior, access to tools that oe — (1)
> extend its capabilities, :
> 
> encapsulated in a runtime with a @) ®
> 
> dynamic lifecycle.

![[assets/slides/k8cnVCMYmNc/slide-007.jpg]]

OCR text:

> OpenAl Agents SDK
> Available in both Python and Pres ee es
> ajel-roreid] elt ©.
> agent (
> e« Works with most LLMs (even ars ;
> non-OpenAl) ; instructions '
> 
> Cie a JaleLev nes
> 
> . result PCr ae re
> ¢ Guardrails Pee
> « Streaming*
> A Tools & MCP support (result. final output)
> e Built-in Traces support
> e Flexible session management
> « Voice agent support*
> 
> P “not yet compatrb’e with Temporal

![[assets/slides/k8cnVCMYmNc/slide-008.jpg]]

OCR text:

> OpenAT ACRES
> / oo
> saatrecetons / \
> (| : ie
> comer from the rucner)
> wodel :
> agents Agent ‘ /
> agent ( — ~
> Tools
> name 5
> model Fi
> instructions TRIAGE AGENT INSTRUCTIONS,
> handoffs [weather_agent, local_biz_agent],
> tools [WebSearchTool],
> y
> result Runner.run_sync
> (agent, )

![[assets/slides/k8cnVCMYmNc/slide-009.jpg]]

OCR text:

> Introducing Temporal
> e Technology and open source project that delivers
> resilience for distributed systems in a novel way.
> e Supports a programming model that allows
> developers to code the , while the
> platform provides services that compensate for a i; |
> wide range of distributed system failures. S I ! ] e @) al
> e Platform comes in the form of a service + SDKs
> SDK is available for Go, Java, Python, PHP, Typescript, .Net, Ruby
> Note The OpendAl Agents SOK + Tempora: scluton is currently ee
> only avalatle ‘or Python. Typescript com.ng in the future

![[assets/slides/k8cnVCMYmNc/slide-010.jpg]]

OCR text:

> fi
> ‘ t |
> 1 oa
> > 4
> dl ss
> : eae raters tettae Rebet tee oe eaNy y
> Loe ae ae a a
> 7 poe renee eee Rea rs p
> POON SRR SRRN | BANNAN ee
> ci wien atta aan oe ec al iM SACRE
> . ” Peete ae bit :
> 7 -_ =e i aie
> ij

![[assets/slides/k8cnVCMYmNc/slide-011.jpg]]

OCR text:

> Temporal Activities
> Taling NYC INYT) 47.14 Cal
> withdraw
> deposit
> refund

![[assets/slides/k8cnVCMYmNc/slide-012.jpg]]

OCR text:

> rehued
> | aeses
> La ed
> ~ “=
> ‘ c
> sl,
> eer
> ee ce ae eae
> Bg eens
> P > ees or
> S ~ AS \ nn

![[assets/slides/k8cnVCMYmNc/slide-013.jpg]]

OCR text:

> '
> ' ee
> Poe
> | deses?
> es
> “aed
> ‘
> on
> =>
> ml aw - Wl '
> ——— —_ we - .
> wt 5 .
> wi a ‘
> = w 3 \ see
> a ° i
> teem ome
> fy . ~~! —
> = | 7. he
> = , - .
> ~~:
> pS) ; _.
> nee Rr AUS ea &
> pa ema RO a ena ‘
> RC ONe NEEL SS ar
> gs ane oR RAPE ESS LRRD a i
> a ” 7 ; ;
> : FY

![[assets/slides/k8cnVCMYmNc/slide-014.jpg]]

OCR text:

> ny 2 ki * . Bae! =
> A Poet ie Peer trees reat musreles AUR T Lee LAI TC CLS ig Brooke
> Beas cmate queues, manage timers, publish and conse
> myement feties 39d 19' Hacks, CHECKPOME stare
> ~ Se lan .
> ~~“ aw as
> tae). ay rT oo aA : -
> : “ -
> coal o 7] , a ”
> re —_ — A mm tee!
> toe “4
> zi 3 \
> a x
> -_ :
> KN :
> ema ae 5 sa
> ee eee a La ba
> ae
> , naan 1 eer ee pee
> ; OMEN ; ;
> } ae

![[assets/slides/k8cnVCMYmNc/slide-015.jpg]]

OCR text:

> a I ae ada ac ect ies hd coe .. ' & mom ih ne Pt lita td
> © © | Mui scemerenn «. Q Rutten tO ede- Geta mG me tainent epens ae 2 | 0) trweetatenteat ie RQ te etiene meres .-
> © SB ete ene oe Sono Do @ ~ 0: ee tae naa oer y
> Bq tenet EE) Ca tens Reet Prune 05 Coateg tees Co Cpe Toe Wiyfemoer a Ls AP Boones -
> () README = &f3_ License @ 3:
> (note, you will need enough quota on in your OpenAl account to run
> this demo)
> 4. PDF Generation Dependencies - Required for PDF output (optional) *
> Starting Temporal Server
> # Install Temporal CLI Q
> curl -sSf https://temporal.dawnload/cli.sh | sh
> # Start Temporal server
> temporal server start-dev
> Setup
> 1. Clone this repository
> 2. Install dependencies:
> uv sync oa
> @ 2 Catunir Onandl! AP] bau:

![[assets/slides/k8cnVCMYmNc/slide-016.jpg]]

OCR text:

> CL dS so eo oo Ll th An athe oe ed eho @& WO Gm LO he MP BG me i
> EE :
> STO gt otc % eae ‘ cea Tra ove eee aa ary
> idk 2 CP Chena 0d Castel ce a i YS
> = © temporalio - ai-cookbook Sere et
> Mace a toot call to aet sn addeess
> <> Code © Issues 1 TL Pullrequests 4 Gq
> Mace a tout call to get iccation info
> ee os a as Te ee ae
> ai-cookbook Subic Crane) Me SOG Soll Coa CoCaLo
> No togls chosen, respondirg with a tessage: No alerts today here,
> Ir New York skies so clear now
> P agentic_loop ~ P OD Go to til inveame tute area
> i
> This branch is 4 commits ahead of main . co
> ; E uv run python -m start_workflow “any weather alerts where I’
> i eC] we EER Oe ea)
> @ cdavisate Getsid of one more biockinge.. oo g ora Lae
> ts eee ae eee ee in
> @ github addcodeowners ; uv run python -m start_workflow “any weather alerts where I'
> aA a
> mat?”
> fm agents lesemmimetmarer: Result: No alerts today here,
> In New York skies so clear now.
> 5 ca h Ace
> @ deep_research/basic_ope... docs: add front ma Peaceful ee sl Sg
> i ages, gery Meebo clon, A
> @ @ foundations docs: fix broken inl , |

![[assets/slides/k8cnVCMYmNc/slide-017.jpg]]

OCR text:

> A
> ore ce: _
> = wr -— 4 |
> mw SF
> = = a | = Ty . ) ~~? . .
> - 7) amen “yee & £ o -
> ‘ . | > a-<mer ea,
> > mM fl ee.
> | | : - ne -— —_ “@
> ft “= a =
> a“ = ° - :
> on: ~- n Ly L = |
> 4 | - ap ~~,
> Lica) ' a oo
> ao ee |
> a on Oana & a
> = ee q

![[assets/slides/k8cnVCMYmNc/slide-018.jpg]]

OCR text:

> bt I a Sl a eh ot & We | Mm 2. OO - & MB Fs ke BH Cette ine
> ° cE teed agentic_icop_tool_ca!l_openai_python (tin 0 cree tes -
> i. rc
> ar \e1 1h oe Ca
> > __pycache__
> Saray her versions
> | ~ activities
> > _ pycache__
> enter YMC SS ee E Mord t's new in v1.10
> . 3
> | tool_'nvoker.py 7 ren Ging changes
> Bd
> ote ~j/Pro,ects/Temporal/Alicoakbook/ai-COOKbOOK- ve Gt rete” and ue dare erede” Communes Salt Coen ened AoW
> Pa iocelhy wiffagents/agentic_‘oop_tool_call_openai_python/activ.ties/tool_invoker.py ogg e artisans rede” command has Been acnd Be sure sa cpdate yur
> piety Corgi,
> > workflows
> [yaelg crotmcerinl|
> README.md
> start_workflow.py
> ded Goat by" to OU Satay The gees ceccet, aoa atin tie "Sot
> uv.lock :
> Rr ere] Poet tatie Grane. Thue aan them ngtterice alae “cure grad chee
> Berea te | Chanke fren the FA ot te BS nea LEMnha As oF arte poe!
> “
> AL tea tts pay Ciba, Pes at ulated ath ancrccGered ite Sums
> Relre conter! and netted pometies
> ss a
> WIG eZ e Ott yi Rb pou Base ofttes on a Mig fata ft trces the
> Oey MOU Geese TASS aR” Mae
> Crider ar cromp es ch hoe dove opers Cn implement rea wen Types ter Bowes
> ma Tae he
> Ham tend raegater Cul ist st ncteen Otow
> > OUTLINE CGricaste wee
> eer antt 3 COP EMEE My UNOS ANA TOS! ad aE! td lereccel Ore 2
> a Cae) Corvin te! at, | «a «i
> 4 ro ents

![[assets/slides/k8cnVCMYmNc/slide-019.jpg]]

OCR text:

> Do oe A Lo nl a it th ta aed eho ov @& We | @® . Cs & MP et BH wm
> . Ayorty  Ed:tor openral_responses.py — agentic_‘s0p_tool_call_openai_python ao mM_n_ZOm  *
> 3S a yt oy openalresponses.py Se eee
> an, Ae Coo
> tad en a Oe USMS) ChEna_respacses py >
> > __pycache__ ies Uae ad
> Pane hd 16 aloe he de ee 7 A
> Sareea y a
> . ot)
> > ycache
> ae o> -_ ts)
> | openai_responses.py or)
> tool_invcker.py 21 Cs cee Rees)
> o res
> pales any ; Ode" Comm ants Mae beer fened Anew
> ants ce s been acand Be sure to update your
> ye (oom clisat responses. creates
> Soles 25 Darts Cee OO oe aie ote
> Pyproject.toml 26 Na taetel Wa ear Cans merece rea ote or ;
> README.md rae Dee rekon tas are Per ra
> Peas ea 28 clot Otel ae] at Ren ole Rae
> 29 P1rebate te, by the g eer ceccert, Avautie 6 the Sort
> uv.lock
> cf) H
> workerpy ES aaa fey eedce a Lae CoLete ated chee
> c fet reas Ens OF atte pte
> Rvs B
> cx) | Rw Una ree Cchscay bueted sts era rumtered ats Supteets
> bare enres on 2 mag rate t free tne
> . x TAM Se
> scan plomertcca ven Bpes fee Bases:
> ry COLA
> Pela
> mea sans Caarcrek Pond Tmgecrel ad
> or Ora) Cursor Tab Ln 1, Coll) Spaces S UTF-8 LF Python 3.17.12 (wee: veny) & 2

![[assets/slides/k8cnVCMYmNc/slide-020.jpg]]

OCR text:

> ve 7 8 tae
> @ : A
> * PET TON, tS ssinstancet ites, arguments, steb coe Mt
> os ot tere kpedtss
> . oy Tarastte as
> ces PAC tae
> a AS
> Ee con ; ,
> ” A ES ote e a EESS Bree Se
> ‘ aha’ Te oa
> “%
> . ahh
> 8
> rr ee 5
> a rane * r¢ N
> rhe hie Le Bn PYTETIT ar)
> -_ By |
> | wl
> — ay e ens ont, 0, oa en
> st gh CO ee Panay ca
> y sissies ae
> erence - ee 2
> cA pect SERN ae Peco
> to es ee tele ea i ars
> a : See \ on aera
> — if, = eae
> - » @ 5 ‘
> —

![[assets/slides/k8cnVCMYmNc/slide-021.jpg]]

OCR text:

> Peary a
> 7 | POET  RT a nee  camaieala
> Hh ‘
> Rn Pa al
> i] it ae 7
> _ .
> a Th a
> + "
> n \
> iW ~
> ae Ee
> a. |
> . —_ a Ms nancy |
> a Panne Richins
> PR: Recetas \
> See: Dial petal rcscer Reg
> ii Neiias reno fecereseceatelatsacst ane
> See ea get pte eo ee 0 Ee aR ES a
> eae pine ieatnnce eee
> ies sentence ll Sn
> 2 ae NRCC erennaeey
> Sh re 1
> ad ioe a

![[assets/slides/k8cnVCMYmNc/slide-022.jpg]]

OCR text:

> , MET aR aC ee tye
> : es . i aa Pre Oe et ee See Le
> ; eee oie
> : LOO SCOR maa Laat ae Ce
> ; CM Te Oa See “Lae Ca
> areca
> Seth WD glett. ttGes T0¢
> Te Nee Tete see 4 yet cae
> PRTSEY NE IRE OL,
> é
> j
> mt —
> ‘ Bt de ay
> swe
> \ g
> a t i > \ i
> , :
> an} a3

![[assets/slides/k8cnVCMYmNc/slide-023.jpg]]

OCR text:

> DN ae ace aa ead A lt dd aie aed Ca - &A WY & Hm 2. Ot ee Bw Tt et BD ten ts law
> e “ee
> Arty Editor init__.py — agentic_'oop_teol_ca
> : F Made a tcol call to get avather alerts a Bs
> i, or _init_.py ee eg ee ee peg ee pet gg pe pe eee a
> ¥ AGENTIC_LOOP_TOOL_CALL... taney ere: ' ; ,
> anid ait NO TOOLS Chosen, rescording arth ao tessage: No alerts today here,
> > _pycache__ 47 get handierttcal sare: Tro Sen York skies se clear nus
> el ee | ea rare eeR AY Cot eed te
> ¥ activities oo ae
> oe | get_weather_aler!
> > _ pycache__ E
> 13 | f
> Cofes TaN CSS sere ER og oT)
> tool_:nvcker.py PAs) Peon .
> aml ol a9 ra ‘ eae
> laa
> Sam ob for: e1 a a a aan
> ro Rea aenes
> tool_he'pers py oy
> ~ tools Da
> > _ pycache__ 26 ;
> ge
> | a aes? rai ,
> A Ps:
> fot Umer ldieam eye a 3 o cursor .
> get_weather.py EY rere eae me |
> ier meicL Ee ES ; ”
> 7 my » c uv run python -m start_workflow “any weather aler
> teehee) 3 ts where I'm at?”
> Raed 34 Result: No alerts today here,
> > _pycacho__ " In New York skies so clear now.
> Pert Peaceful weather oad
> ; en ee ere
> Pyproject.toml ,
> Parola UL a : : uv run python -m start_workflow “any weather aler
> ede ae ha ts in CA?”
> O00 Cursor Tab) Ln 1, Coll Spa |
> EE 7

![[assets/slides/k8cnVCMYmNc/slide-024.jpg]]

OCR text:

> ba a a sh SO a il I ae ce Os a, es ita ED 2 Bea Lat
> OO | miei ReemNIN RQ ate cee « Owe-cmmm 2 Qe meen reset 10 -C) emeieedintne x C emtmmenbeetie «8
> © SO were 2 be alte ae OO "Oo: Pe ee en eee
> f, tenet “) Cttes 5) hee Pesce 0 Sea Bees ee rope fone 0D My temoe a Lo. At Bema te
> > © detast og @utt v f3 a.
> WGrdaus sattaring condy
> 14 Workflows ¢ Ra er a
> 2 | 14 Completed
> a Wiruter
> be Poorer
> * Snel
> H
> ey Completed agent. ieop Feb 2yds-Jode ha7a HE? 7290CN 7A PD 0199acc0-0909-7772 e680 $7209588r88 Agentwi
> > Completed  agentc-loopci-c 9119589. 3965 -S RRC Ate? eed 76 6c Spc 15 O'Gaacs3-Ne2n. tent BobE Oc Mele IO?9 Agente
> fi
> ea)
> m Completed —100's-werktlow ONG aac4?-G5RO-TROD- 914-1579 aceade Tootwwa
> A ‘
> a > Completed tunis worstlow O'9a0cd2-2907- Jedc-Didb-79aloh1d 998 Toots
> Ss
> & D Completed 100s -weektion OtSaacdt cab. lec BIDE e610 OKI POS Toalsiva
> D Completed two's -weentiow O'Daacd1- BIDE Pos2-95Sd-d97c9C 27006 tem ves expected.
> : far back from the wate
> FS Completed touva-worktion O19aac 30-0432. 7995-9626 -Gec 788 7Be7b Tools
> > Completed loc weektlon O'9aae 30-0245. 7AIS- ORG? COORD HANES Toole
> 100 1 “a & - :

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
## Reconstructed Slide Deck
- [[youtube-k8cnVCMYmNc-reconstructed-slides]]
## Dense Scene-Detected Slide Candidates
- [[youtube-k8cnVCMYmNc-dense-slides]]
