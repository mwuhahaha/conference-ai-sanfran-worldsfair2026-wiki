---
title: "Slides: Reinforcement Learning for Agents - Will Brown, ML Researcher at Morgan Stanley"
category: "slides"
video_id: "JIsgyk0Paic"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: Reinforcement Learning for Agents - Will Brown, ML Researcher at Morgan Stanley

## Source Video
[Reinforcement Learning for Agents - Will Brown, ML Researcher at Morgan Stanley](https://www.youtube.com/watch?v=JIsgyk0Paic)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/JIsgyk0Paic/slide-001.jpg]]

OCR text:

> " ys. weet: |. le} ee : Fuh}? & 4 to ee |
> ie | mee ake Pay 3 : ‘ae:
> : J, ie ; dusts % te TI Pe A a ek " a aie : :
> oe a a? 3 ag! as: WAY 29 aoa Beare: as od S er fo AS
> ae 24 a 4 <7 se” a ae we a bag gal eS 2 1 “ \ .
> fe ca a lee “AP ® Ree ad APs Poi gh |) (ee
> ao an as Se eee Gate Es" NEY i, ge TOSS
> ne a, ree Sid aie Remit: hk San soe
> ; ’ ce tea af v i « Kat Or. ty ry ym ay
> : ar aero Prat Wee ww J /
> nS AS OS ue SE) Calne, , case ;
> oh oe gd me Oa | I Boos ne
> ’ ° ° i 4 “Hye A |
> eet * 3 eed
> Le
> a : =x
> 2 ; 7 >
> re a ° —
> ry . :
> me }
> ‘Wee —

![[assets/slides/JIsgyk0Paic/slide-002.jpg]]

OCR text:

> Pt ra 7 7 = - - . e ee
> | or Tne et Chr es] ee
> a or A i ee aS 1s |
> “> = a ae wo
> . Ca F »
> © ry ad i se Cd a : * a
> ‘ om A tf a ale a“ Oy a . ar oa Pa wet |
> + ‘ ard . i , = . -
> i” ) , pi A “Be . A ‘ rad aa ,
> ’ . SP al , : : , : ; oa
> aad “ re a eon, e ; ; r ry 7”
> SS cea ars ' Pa ves han oa
> a ee es 7 as .
> a ce 7 7 wil. an a :
> 5 "y ate OES as =_— "th ne, a a dt < .
> 7. aS
> io — ry |

![[assets/slides/JIsgyk0Paic/slide-003.jpg]]

OCR text:

> eer What RL Means for Agents
> (Reinforcement Learning)
> Will Brown(@wilcbb) Machine Learning Researcher,Morgan Stanley
> AlEngineer Summit2025

![[assets/slides/JIsgyk0Paic/slide-004.jpg]]

OCR text:

> LLM agents in 2025
> 
> e Most LLMs are Chatbots Stages of Artificial
> Great on Q&A benchmarks mitaligence
> Helpful for interactive problem-solving Level 1 Chatbots, Al with conversational
> 
> e “Reasoning” models = the future? language
> 01, 03. R1, Grok 3, ... Levelt 2 ee human-level problem
> Better at hard Q&A
> 
> e Best practices for “agents” Level 3 a Agents, systems that can take actions
> Manychainest. LLM calls pertask Levet 4 Innovators, Al that can aid in invention
> Prompt engineering + tooling
> Evals, ops. tool-use, human-in-the-loop Level S chonorsaiedlon that can do the work
> Results are... OK?
> 
> (Openaly

![[assets/slides/JIsgyk0Paic/slide-005.jpg]]

OCR text:

> "s _ LLM agents in 2025
> e Most LLMs are Chatbots Stages of Artificial
> Great on Q&A benchmarks Inteligence
> ES Heipful for interactive problem-solving Level 1 Chatbots, Al with conversational
> e “Reasoning” models = the future? language
> 01,03, R1, Grok 3... Level 2 Reasoners, human-level problem
> Better at hard Q&A sovmeg
> : e Best practices for “agents” Level 3 vo Agents, systems that can take actions
> Many chained LLM calls per task Level 4 Innovators, A! that can aid in invention
> Prompt engineering + tooling
> Evals, ops. tool-use, human-in-the-loop Level S a agesueien that can do the work
> Results are... OK?
> ee ge awe en gil (Open
> ee a |< Pamala aah [c
> * ee a AI.ENGINEER
> +

![[assets/slides/JIsgyk0Paic/slide-006.jpg]]

OCR text:

> How agentic areouragents? ©... 0“
> e Many agents are pipelines
> Low degree of autonomy
> Non-trivial engineering required ~~ :
> e Winning apps = tight feedback loops (mostly) eee _ ~
> _ IDEs (Cursor, Windsurf, Replit) “
> Better at hard Q&A
> e Not many agents “do stuff’ for 10+ min
> Devin, Operator, Deep Research “een
> How do we make more of these? Human LAM Cait , Environment
> Just wait for better models? .
> e Classical RL = optimize agent policy stow =
> (Anthropic)

![[assets/slides/JIsgyk0Paic/slide-007.jpg]]

OCR text:

> . Deecteoe 41 Lore overage engen per pane due Hanng .
> Lessons from DeepSeek
> t
> e 1month ago: DeepSeek R1 paper + model poe
> t
> e RLon strong base models works per
> e RL with sparse rewards works ,
> e o1-level performance = easier than expected , ™ “a ™ ™
> Long CoT = emergent nie —__ DaeoSes Bi Tero Ae ae Orne eR
> e Open-source is back (for now) “ a |
> . Several replication efforts ”
> Can distill to smaller models i
> e So... what next? aa
> (DeepSeek. 25)

![[assets/slides/JIsgyk0Paic/slide-008.jpg]]

OCR text:

> AIE

![[assets/slides/JIsgyk0Paic/slide-009.jpg]]

OCR text:

> How reinforcement learning works
> e Key idea: explore and exploit See
> e DeepSeek’s GRPO | ve seee cv ez (olUULUUUILLNUUIU UNI Ga
> Group-Relative Policy Optimization oT ~ sension econ peers
> eee) wayne? Toone
> Like PPO but simp! sows omnes ——________.
> = ae. =e] x
> . Less compute. same effect coemroeeeren|| a
> ee . %
> @ Main loop: —_ V
> Sample N responses per prompt ee
> Compute rewards for each
> “Advantage estimates” (Jay Alammar, °25)
> Update rule: better score = increase likelihood
> e Challenges: rewards? multi-turn?

![[assets/slides/JIsgyk0Paic/slide-010.jpg]]

OCR text:

> Lessons from OpenAl Deep Research
> e LLM agents can work for long multi-step tasks
> e Vibe check = impressive
> Still struggles “out of distribution”
> e Big labs will keep making agents
> e Don't know full details, but...
> How it works
> Deup research was treed as paend toond ). ta las oh
> ; et Be ee ra
> CO AO eet eee are Pen ad OU LAr oLG Ce SIC LHe Stee er cee a ceane| : Lo, a vee ; Le
> Mut. step trazectopy to fied the data ct pees, bucktrackerg afd : hoa g ee ae ah
> ee ee ee ee ee (O Al. ‘25)

![[assets/slides/JIsgyk0Paic/slide-011.jpg]]

OCR text:

> a
> ~ ‘. Lessons from OpenAl Deep Research
> e LLM agents can work for long multi-step tasks
> e Vibe check = impressive
> Still struggles “out of distribution”
> e Big labs will keep making agents
> e Don't know full details, but...
> How it works
> ce ae a er
> - . . oft : ye oe ce! ara a, a Wh NBeruirs a a a 5 r Pa
> a 7 : - ee ae 4. § (Openal, :25)
> a pene | AGENT ENGINEERING
> ON re a AI.ENGINEER
> ry : ; m

![[assets/slides/JIsgyk0Paic/slide-012.jpg]]

OCR text:

> O PyTorch
> RL infrastructure PyTorc
> e =RL training infra: exists, but mostly “RLHF-style” © unsloth
> e Want options besides “wait for big lab tuning APIs” Hugging Face
> e How can we plan ahead?
> e Unknowns: a
> Cost to do RL for agentic tasks?
> . How small can the models be?
> Generalization across tasks? Createle fine-tuned model ©
> . How to design effective rewards? Method
> e Opportunities: ee
> Reinforcement .
> - Open-source infra for DIY
> - Services for agentic RL Base Model
> o1-mint-2024-09-12-alpha ¢

![[assets/slides/JIsgyk0Paic/slide-013.jpg]]

OCR text:

> al ne U e @ a 6 C eo a ae
> ry , '
> 7 a . : one ae : 7
> nen pon ee en tae
> a aE (a Cog cote HE 4! ae
> es os or a ae ; il ]
> a. a , ' /
> . @ Idiom .
> I nal
> - -m ;
> : _. -- of ; * aA ee
> oe ao , 2 m 7 nd ; —. x ~~ &
> mM « - < F
> a »e : Ne a
> a ain 5 ° °
> 1 oe ; ra . : , 7
> ara S al _ 7
> Ee 7 en se
> e oe Sy ie Cn 7 a
> ———— i ———$———————
> i —
> f
> { L Ps

![[assets/slides/JIsgyk0Paic/slide-014.jpg]]

OCR text:

> grpo_demo.py
> willbrown@williccbb·Jan26 ointsscored by the opponent in the chasg GRPOself-correctiononLlama-1B:) Promote We are also given that the points scored by the opponent in the chanpionship gane is half of uF' narite: Simplifying theequation,we get: （24x-2）=（1/2）（24x-2·2）
> 2) （24x·2）=（24x·2）
> get: This sinplification was wrong.The opponent sust have scored 2more points
> 2 Theopponentmusthavescored2more ain/global_step 150 140 130 160 This sinplifies to: This simplifies to: So,they scored 1/6 pointseach in their first24games （24x·2）=（1/2）（24x·2.2） X2/12 x=1/6 （24x-2）=12x 24x-12x=2 12x=2
> ach in their first 24games t37 484 67K 0.4 train/rewards/accuracy train/completion_length
> script: willbrown@willccbb·Jan26 0.3 150
> 0.2 140
> To 130

![[assets/slides/JIsgyk0Paic/slide-015.jpg]]

OCR text:

> grpo_demo.py
> AIE GRPO self-correction onLlama-1B:) willbrown@willccbb·Jan26 pints sored by the epoonent inthe Promote X1 eare also given that the points nwrite: （24x-2）=（1/2）（24x-2+2） Sinplifying the equation,e get: （24x-2）▪（24x-2）
> This singtification wos arong. The points
> 150 4 This sinpLifles to: （2·2-x2）（2/1）-（2-x） （24x-2）·12x 24x·12x2 12x2
> 130 So,they scored 1/6 points each in their first 24 x2/12 X1/6
> sch In their first 24 games
> Q24 37 484 l67K
> will brown script: @willccbb-Jan26
> AGENTENGINEERING
> HTTPS://AI.ENGINEER

![[assets/slides/JIsgyk0Paic/slide-016.jpg]]

OCR text:

> GitHub , CR RS aCe OM Led
> « a
> rpo_demo i worey
> e
> —_
> fonmety 5 dq c e a
> re oe
> i" ] poem 5 Pte 2) Pierre-Carl Langlais .-.- ee
> Ce tae eas ed -
> . : fi , ef fac dret @
> I release today the first Google Coteb notebook to tran a reasoning s-smits/grpe-
> new Reinforcement Lea nung sigonthm from DeepSeek, GRO an
> hours you can transform a very ima’ model Qwen 0 5 (500 milion optuna
> IO a tiny Meth reasoreng mactene To thea date, the ms probably t -
> Tegroduction of 81 and 0! post-trasmung cycle you Can easy run (6 2 . a
> Rttos sfinkd nidc yp! a .
> The notebook 1 bated on 8 sont by William Brown that monifcant
> on Linens 38 capectues for math. This 1s « typical reeforcement
> approach based on thassands of exempies from the gman .
> MT rT rT ere & Reasoning - GRPO&RL
> torm of inference time compute) aod rewarding the good reasoning Uacet
> ‘Quwen 0 5b on GRPO-
> Traming @ erred math reasoner with Fi
> The mete ee nee ree ote es ae oe erg ee be ph mee cree de cee a
> ne ee sn» crepe © nae te men ee San
> + meen Nan sae ed
> 2 Aan en a oO tN See ta Sa gtk A ah Nt nome ho OA
> arene
> + nomen ee ae rae tg ecm ee at ne One a aa
> + Semmng up We mascots — ;
> me eat oo te so Nee ee ne eee neers eas
> COM 3265 PO comments iT ecatts : _

![[assets/slides/JIsgyk0Paic/slide-017.jpg]]

OCR text:

> GitHub oe or
> ee Lo
> ~ Vs f
> a. grpo_demo.py His
> —_
> , G? rr ” ea Pa ; 7 a ;
> ee Prerre-Car Langiate - ae
> ; , OS in se 7
> Leminane lodey We fest Goce Colab nenetond to Yan a song x
> nem Reedorcement Laaneng agerthes trom Deeniees, GRPO in 5 smits’@rpo- B
> QUI yOu Car traretort avery wheal sock, Owes 08 (800 aio optuna
> Vike a bry San reancreng mactwne To tee date, Orta pritebty
> Fepredut teen of RI ard 0} post: Dawud Cycle you Can easdy An .
> Rito 1fenied wie poppet 7
> That noteGoot 14 PHT On 8 BNET by Willem Brown thet mgrwic:
> On Lema "8 capenties for math Thee 9 a trea rervorcement
> FOOrOECA Dated on thoveands of examples from Die grea d
> ba nas to fed the KOON, enon Over & for nome tree Cows nthe abechee box MAME ORESO SL Oa Lg
> form of eviermnce tena Compote! and rrear Geng Ihe 9005 reeporung i aces
> a Qeen 0 9 on CHD
> ‘Tremrarg 0 wed rept omen vet
> TT a ee ed fMLP yg SR .
> Scarce ieee ce tee
> SES eee eee or
> ». a . ° 2 . a 5 SN i ee a es
> a. oe er eer emteltae ie clin wens ee ere i
> t rans ona weer 7
> - Coe ERE TY AORN
> oF a i 7 a . A 7 Fi
> ~ AGENT ENGINEERING
> , A
> rn AI.ENGINEER
> Y . P

![[assets/slides/JIsgyk0Paic/slide-018.jpg]]

OCR text:

> YOML_COT_FORMAT = 7h)
> <reasoning>
> {reasoning}
> es a s </FRBSORING®
> Rubric engineering cn
> {answer}
> </antwer>
> e An accessible way to steer RL algorithms 4 wecatn sRentans
> Sef correctness feward fenclprompts, completions, answer, eshmargs) -> Visti float):
> e Invites creativity + experimentation responses - [completion(@}["content’] for completion in completions)
> @ © promprsletl-1}[*content’]
> extracted_responses © leatract awl answeedr) for r in cesponses!]
> e Anecdotally, seems to help printt*="e28, fPOveation:\ntgh=. f\ndniwer:\n(anuwer 101)", {\aResponse:\n(responses (el),
> return [2,@ af r 35 @ else @.8@ fore, a an ripteatracted_responses, antwerh)
> rf . na"?
> e The next prompt engineering . Get int_reward func(completions, eckwargs) -» listiftoat]:
> responses « Icompletion{@}[‘content’] for completion 19 completions!
> e Next steps: extracted_responses + [esteact_uel_answerdr) for rin cesponses]
> retuen [0.4 at Fiisdigit() else 0.8 for ¢ in extracted_responies)
> Using LLMs to design rubrics? dei count .wiftandl: <a itiget:
> 2 x count - 0.0
> .  Auto-tuning rubrics with DSPy? 14 tent cunt Meceasonangeint) s+ a:
> count e+ O.125
> . Incorporating LLM judges for soft criteria? " E85 AN EASA wa
> eeone S20,
> + ex: « Af text.counti™\aanswerzya™) -- 1:
> Avoiding reward hacking? But menib si
> Count -- Tenlteat. split" \ec/answermior yet) bee. 08
> af text.countd™\nc/angeere™ bh oe 1:
> townt +s 6.125
> NY will brown Count -« (lentteat. shit \ecsanewere 1-11) - 1bet leet
> le retuen count
> any
> det salcount reward fucc (completions, setwergs) -- Liatlflowt]:
> a rl rn P e * =f A tents: my for Me A te ?
> rubric engineering is the new prompt engineering tarianaiidincnciaal

![[assets/slides/JIsgyk0Paic/slide-019.jpg]]

OCR text:

> a MAT 8 ey
> a sreasoninp»
> bs (reasoning)
> ze . . ° ciRe aaa
> caer
> /* Rubric engineering °
> aS (sswee)
> <tanseer>
> ; e An accessible way to steer RL algorithms Beret tector
> der coree.toeey coward Lecce (prampts, completions, arsenr, sokmargs} -+ list{floatl:
> e Invites creativity + experimentation responses + [complet ionipt |‘ centert’| 2) completion os comptet ions]
> O Prompenlel Gli concrete)
> eal ea ted toni ae Lente ge amt aneaerdel toe ron cenpomnen!
> e Anecdotally, seems to help seer aide Gheeedieras(altighe cinwcr:cacjornee du foe toordesgarnesSn{reaporsen 1H
> fetarh TO Gf fee ae se OO fet, a Le rip leatracted responses, aeswert |
> “ s “arp
> ¢ The next “prompt engineering” set fon cnsara, tay | Comptensvengyremeryys: hayeltteari:
> respenses - [completion Oil custest (1 1+ completion 10 completions]
> e Next steps: extracted renpenses = Leeteat ees acne (7) 1x0 6 a0 respons]
> retere TOS Gt recedigitd) elve @.@ Tae or i> extracted revponses!
> Using LLMs to design rubrics? Bet cnet am teat) + Moats
> cat ne
> Auto-tuning rubrics with DSPy? WT Leetecaet (Meceanonsagennty oe
> tort 8
> incorporating LLM judges for soft cnteria? i a ia
> Avoiding reward hacking? tees mammary)
> Cert ce tetas at tins fete eset 1h me
> Peat un anecanteer eth ee de
> tomt ee 82}
> " 7 ' a a TY towed -+ Centteatse: tC ites enews Et lee ee:
> a. . : ae : Bet ant cutt toward ire Ieompletiony, samergel + Leet itloet]
> i enngis the new prompt enpireennyt oe wae anseta's oo sore ‘amg Dennen conc eaple vanes
> an AGENT ENGINEERING
> me AI.ENGINEER
> at {

![[assets/slides/JIsgyk0Paic/slide-020.jpg]]

OCR text:

> aa . . ® . Oi .s.nws 4
> ’ 7 R
> a oe Z P
> th to. fae id es F - y a on y
> ee y a4 ee ae
> ee ieee eee a eh ee ea ee _ abe
> eel oan 7 oad ”
> 1 8 od
> a rs
> 7 a a : . ae bd a : 2
> a ; an . / a
> o 5 . a : , ae
> eo: a . rr 2} e e \
> : oe are ;
> 7 ov *~ ad ; , a
> ‘ v _— :
> ian soos ~ on, s y -
> — Ny 4 —
> \e ; |
> A
> .
> ’ /
> N
> al - Pe

![[assets/slides/JIsgyk0Paic/slide-021.jpg]]

OCR text:

> ce en + oe
> | ' (Al Engineering for the RL ora I brent ! in tea: ss Fs
> © Fine-tuning may de more important than ever its RE- {
> aa a © Opportuntion, Chalenges, Unknowns: oS a -——-
> meneame © Rube engnesang .
> © Designing sgente erntepnmenita 5 : y if
> © Creeting eave tools + inisetnactune i a i
> ° 13 Caguenrigvorwine omar ik H ie ; LS
> Thenks! N 7 1 ' A
> nga) BRS
> 2s et
> , a ice HN alt tae ey Pe
> ee ea
> : a ___- | a pay ne *Pila
> sek pe ag ee ee gf 4 — fe
> -, ° | es — Sse
> : _— Pha y é J 7. <

![[assets/slides/JIsgyk0Paic/slide-022.jpg]]

OCR text:

> iL aon ce a om ited bd an ‘ aah " q , Cd pl i i #3
> eR ae” Ue. ood 0? Bae Sls
> ’ ri , x ee’ : ee ms ah ii ny Ne . a . 7 Crane |
> c _. in ” 7 at Y k ra a a oe i
> are eee ec ee ana Sc
> , ° tC ° ; 2 an os hk | were =
> _ iy en
> SS
> a
> = ; — a
> — a es
> _ ae = |
> _

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
