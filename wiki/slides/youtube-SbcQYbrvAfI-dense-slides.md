---
title: "Dense Slides: Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize"
category: "slides"
video_id: "SbcQYbrvAfI"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize

## Source Video
[Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize](https://www.youtube.com/watch?v=SbcQYbrvAfI)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/SbcQYbrvAfI/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/SbcQYbrvAfI/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Diagram slide with multiple small labels and boxed sections; better suited for OCR than manual transcription in this pass.

Slide text:

> where Agents are Breaking In z025
> No System Instructions Learned: From Environment Very Static Planning No Planning or Missing Tools
> Tool Guidance Missing Context / State (Pre Pruned Data) Management
> Aarlzo I W't Mahe A yyk. 1202511-2212:35:58

![[assets/dense-slides/SbcQYbrvAfI/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/SbcQYbrvAfI/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Two-column comparison slide with multiple labels and responsibilities; OCR will capture it more reliably than a quick manual pass.

Slide text:

> T other lssue T'd Like to Mention
> Technical Users Domain Experts
> Al Engineer Scientist Data.Subject Matter Al Product.
> Developer Experts: Manager:
> Responsibilities Responsibilities:
> Code/Automation Domain Prompt engineering
> Pipelines/Frameworks Track and run evals
> Application Performance / Costs Ensure product success 2025:11:22112:37:13

![[assets/dense-slides/SbcQYbrvAfI/slide-003.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/SbcQYbrvAfI/slide-003.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Benchmark/results slide with multiple cards, logos, and percentage figures; dense enough that OCR is the better extraction path.

Slide text:

> Coding Agents on Swe-Behcn Llte, No Prompt Changes
> cline CLRUDE CODE
> Sonnet 4-5: GPT 4.1 Sonnet4-5: Haiku 4.5
> Cost: S3/1M tokens Cost: S2/1M tokens Cost: S3/im tokens: Cost: S1/1M tokens
> Latency: Latency: Latency: Latency:
> 30.00% 18.67% 40.00% 18.67%
> Github Issues resolved Github 1ssues resolved Github Issues: resolved Github Issues resolved
> Aarlze I "o Hre A Wark. 20251122112:42:38

![[assets/dense-slides/SbcQYbrvAfI/slide-004.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/SbcQYbrvAfI/slide-004.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Side-by-side system prompt comparison with small paragraph and numbered rules; OCR-suitable dense text.

Slide text:

> Optimlzing. Coaing Agent System Prompt
> Claude Code systen prompt OLD Claude Code system prompt NEW
> You are a Claude agent. built on Anthropic's... You are α Claude agent. built on Anthropic's...
> Rules Section Rules Section
> <Empty>. 1. When dealing with errors or exceptions,
> consider.the immediate cause and
> underlying issues that may contribute
> to.the problem.
> 2. introduce technical debt... Ensure changes' align with the overall. system design: avoid ad-hoc fixes that
> 5. 3. and:unexpected inputs when modifying robustness. Always consider anomolies. None values: appropriate: tests. covering edge cases Ensure changes don't intl Any change should be accompanied by and:ensuring correctness and. data flows. 12025-1.1-22112:43:03

![[assets/dense-slides/SbcQYbrvAfI/slide-005.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/SbcQYbrvAfI/slide-005.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Text-heavy problem/solution slide with multiple callouts and code-like snippets; OCR is appropriate.

Slide text:

> dwold waiss paiepdn uiim leniea swjoled aus
> Problem Cline was asked to fix a bug where the program crashed if the input None.or (for many-False) data isn't a Mapping, skip non-lapping items when many-True. and when fetching run only when the field is actually present. Solution Patch (summarized in english) In _invoke_field_validators, return early if data is value catch (KeyError. TypeError) so field validators Correct
> was None. Corresponding Rule
> Whan you locskre a bug. enumarate cvary erecution path thst rasches the foulty Ene (o.g. sirgle vs. batch Itgresslon tosts thuat cover euch path to contrm unchsngod somantles. syno ualn tyrd go srost tuuoed bupuey-solo juootipe sosu iru xg Ituurll e osodod pus (rtol
> Matrix) Incorrectly Problem Cline was asked to fix a bug where using @ with a scalar (e.g. 2 @ Solution Patch (summarized in english) operands (after _matrixify). allowing Python to try the reverse op or raise a TypeError per the Update -_matmul__/-_rmatmul._ to defer to matrix semantics and return NotImplemented for non-matrix operator protocol, Correct
> of falling. behaved like multlplication instead nerby corvenlonce function. for the behvlor rather then a reloted but higher-leve utilty. ln other worda, ftx ksuet at ther source, not n a Whan proposing a Er frst inap the fallng tost or reported behrrior back to tha euact Api or functon.it txtrcises, Ensur+ your chunget sign with that boundary - modify the functon or layr drectly respontlbie Corresponding Rule 12025-1122112:43:531

![[assets/dense-slides/SbcQYbrvAfI/slide-006.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/SbcQYbrvAfI/slide-006.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Dense table slide with multiple small text blocks and bullets; OCR will be more reliable than direct transcription.

Slide text:

> GPT-4.1
> Optinization Loop Train Accuricy Traln Dota 0.1867 0.1733. Ttst Accuracy Test Detta ~15% Improvement, just
> 0.2000 +0.0133. 0.2133. +0.0400 through rules.
> 0.3400 +0.1633 0.3133 +0.1400 37
> 0.3333 40.1486 0.2800 +0.1067
> 0.3400 +0.1533 0.3000 +0.1267 No fine-tuning, no tool changes, no
> Claude Sonnet 4.5 architecture.changes.JUsT RULES.
> Optimtzation Laop D Train AccurIGy 0.3000 0.2800 03200 0.3600 Train Dofta -0.0200 +0.0600 0.3533 0.3333 0.3600 Test Accuracy 0.3533 +0.0067 0.0000 Sonnet 4-5, which is widely. questions' GPT-4.1 achieved performance near considered state of the art for coding
> 03600 +00600 0.3600 +0.0067 o: 11so5.%:
> >arizo I W t= wai 202511-22↓12:44:18

![[assets/dense-slides/SbcQYbrvAfI/slide-007.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/SbcQYbrvAfI/slide-007.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.

Slide text:

> Overfitting?
> Rule Generalization: Meta-prompt enforces high-level, reusable coding rules rather than repo-specific fixes.
> Cross-Repo Validation: Train/test split by repository ensure learned rules generalize beyond local quirks.
> Expertise vs. Overfitting
> True developers do “overfit” — to their own codebases.
> That’s not a flaw, it’s expertise: understanding patterns, pitfalls, and idioms within a domain.
> Cline can adaptively specialize when deployed to a team’s repos, mirroring how human engineers internalize their environment — while still starting from a general foundation.

![[assets/dense-slides/SbcQYbrvAfI/slide-008.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/SbcQYbrvAfI/slide-008.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Dense benchmark table and small labels on a text-heavy slide; OCR is appropriate.

Slide text:

> Hag uo rdwiojd paiepdn/m aula buiajewuouag
> focuses on tasks difficult for language. BBH - Diverse evaluation suite that Tauk ACCUrAGY tnitlal (5 l0ops) Flna Accurscy Chung+
> models saEont_ translation.trror._detection 0.8: ta.s.
> Example BBH Benchmarks' Complex Boolean Expressions snsrks: trscbirg_shumed_objhcts_three_objects 0.32 S0 0.62. 0.88 0.38 +0.36 40.38: to.u
> based on vertex coordinates: Categorizing Geometric Shapes Dupuethepun-spodt word_sorting 0.86 0.84 0.96 0.88 +0.1 +0.04
> Detecting Sarcasm in Statements geomtric_shapes: coousnbat-,eodwe! 0.96 0.48 1 0.5 +0.02 t0.04
> boolean_txpresslons': 0.94 0.94.
> ogictl_dtducton._thrte_odtcts 0.96. 0.96.
> objtct_countng 0.8 0.78 -0.02:
> multistep_arithmetic_two. 0.08 0.06:0.02:
> formal_falsclos.. 0.84 0.4: to'0-
> bglcel_dtductlon_teven_oject. 0.76 0.72 -0.04
> web_of_es 0.56 0.48 -0.08
> Aarizo I Ws Nyo A Wtrk:2025112212:46:48

![[assets/dense-slides/SbcQYbrvAfI/slide-009.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/SbcQYbrvAfI/slide-009.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Screenshot of a product/document page with code and small text; OCR is better suited than manual transcription.

Slide text:

> GEPA
> Aesa AdSOB Garo Cool features::
> dspy.GEPA: Reflective Prompt Optimizer
> Tlot. corponand (toch si promot) ot aborsry tytmn. tn adodon io tceler tcorts rrurmd ty mtnil svr! CEPA (CecateParre) t & trlsco optmLer propod h *CCPA Pelacin+ Pomoe EvoAtoA Can Cutp+iam Rehndortem+at Leng' (Agat t 1, 20ls *na 2so7 ith5?, tut acapoty totm boat optimization Evolutionary
> Tita an. P.ory!. T, 004, t++t ++h. admty hoe is mprte the acle. Ths elm, G Pt to plopme Nigh peranng progt vry Ilar tolat. povides CEPA ont rebty into tty ie wyn got te tegt dm t (d. ard thm GEPA cA introspeet to False, to.uandh: Del = Falet, Eand.apilkay: str l bori = Meo+.!:a, Fslse, marn_oa,scort_alsaatch! boal. Ire., wee.alflos:, boel + Fale. confidete'selectica stratogy! Literell 'ssrete'.'current bust'] '?: Trve. sdd_forut foilure_as_feedhrchi? bo! o falo'sInstruetien prepesar? mr matrie_calls: Lat I Mone = mono, rotloctien_mtntbstch_siro? iat'- 3,:T str's,rmnd rebin'. wo_erpe: bool s Trut, x aorge,lmtcatioms: 1nt. I yoe.., oum_tbresds! iat I Mora - Moee. teilura. seore: float - +.o. Prop+ehIfa: 1 Nore.*. +++d: Int 1 Mare + e, portect, icoei. flost o 1.o, 1oa.d!r: s.r - nooo. treckatats: seor o. - Icog sosoon'seysesdprn 'ooou o ouon I un':at worasetou.ontd, EImus:g lapy. GePa(matric: cepAFeetbnchh trto? 'ttlua'. "+heory'I't kone e Mone. aax full.evoles 1nt'] More o bon, Mooe, coaponant_+loctor: tafltcticaCoeponeatsslector (ouou e ason I satp ttbjia.'ed+a. uoti.11tm rona But...: candidate selection' of prompts Probabilistic merging Pareto-based
> ^arlzo I Sngaitir 4orty 120251122,12:47:13

![[assets/dense-slides/SbcQYbrvAfI/slide-010.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/SbcQYbrvAfI/slide-010.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Chart-heavy slide with small axis labels and legends; OCR is appropriate.

Slide text:

> Prompt Learning vs GEPA, benchmarked
> We ran the same benchmarks used in the GEPA paper, but for Prompt Learning.
> With some eval engineering. here are the results we got::
> HotpotOA, GPT4.1 MInl HoVer. GPT-4.1 Mini
> 59
> 8
> 54
> Optimizstion Method IT GEM TOTHIPOT? Prompt Lttming T GE Optimksbon Hechod 1THTOM!
> 9 1000 2000 J000 4000 1000 6000 1600 2000 3000 4000 6000
> Mimber ol Polout!
> A arize:I. Ship Al tist wons 202511-22$12:48:03

![[assets/dense-slides/SbcQYbrvAfI/slide-011.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/SbcQYbrvAfI/slide-011.html)
- AI slide classifier: `content_slide` confidence `0.96`
- Text source: agent_vision.

Slide text:

> North Star: Self-Improving Agents
> Self-improving agents require a feedback loop where both agents and evals evolve together—not just better prompts, but better evaluations too.
> Improve Agent
> Improve Evals

![[assets/dense-slides/SbcQYbrvAfI/slide-012.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/SbcQYbrvAfI/slide-012.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/center-82/opencv-adaptive`.
- OCR decision: ready — Dense notebook slide with small paragraph text, code cells, and configuration block; OCR will read it better than manual transcription.

Slide text:

> arize
> Optimizing JSON Webpage Prompts with the Arize Prompt Learning SDK
> t.rooe +te Lpi ct youord a Tuyu Aue e s '+as +ll oun 'Lhr we srohno Nosr e H mri yop+or o, suu+p a Pe ebedgen 4uee e Iao lucpr 1ouod ye Looo yrp sll ayenb n tte coltock, we dtaomtybe + vee cs d a rt Lrle Piargt Loaing sox ty cedrng i Fyt n prenet ia CeTto The god le co hnerowe the noat abinr to owrte acou t son reprtrederu o' a Thha jise, ejl mtdr t ao $ouialayed sn sbemyaa La.
> R!
> *++,p++.*lyt!
> Configuration
> TeANL SeLT_FxAcTON Drirmnn Yerytes sot nte, ad e Huu_tAupuss: Conapt hon bary iows Io smrpie iron the F 7*+ t+ 4 tot '+ Cu+.t 4 c t**d +++ + t+e tu+ o1
> Ydued ta +uyt pur 'u+ut t*rys orhro th+u+o ooo f++s u+u+ha Ad uru c: tuept+? wop+rprdo L+w +oy h+s trooT holrrru+o'hrh
> mLP_L+Ls + e '+ m.-t. + ra ++' m= + + +iT +h1+t a / a+ a tl:+ + la.+e itw tali. e?omet, + tre el!...
> =Laba at +) * rrli+ y+ s+aa a. 4 + soo!ollrrliL'm 1aI:++ L I +1 **1+ 1+,*.n + L+ *T. +++ N. +a

![[assets/dense-slides/SbcQYbrvAfI/slide-013.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/SbcQYbrvAfI/slide-013.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Notebook slide with small code and configuration text; OCR is needed for reliable extraction.

Slide text:

> ARHINO opuAte Itou yooun + r Yas BuuriT idwoid ozury rn tum sncwoig soedqom Nosr Bulzundo rn c qutd vopsbeo eEedqam Nosr a' t syooqojou:
> benchmiris shnep:s: >codlng ignt rue.. Y. notebcoks D arizenx support 4.. BlzNorm-100_oval. wmetapx ompt.ixtU canda "nb'oddns"twet' big_bench hard JSONWeboS + Codo + Markdowm I D Run Al S Rinstart E Caar All Outputs@ Go To I B Vhw data @ Jhprter Viriabies n Outine:' pertor mance on a separate test set: Ipip inttalt -arire-phoenix-cvls-2.2.o- srixe-phoenix-ciient tlktoken openal, scthit-learn: μport nest asynclo I Aod n Chu n Guct Edu ua! nest asyncio.+pply() 昭DB sia_codo (Python 3.10.19) vonld: Python
> up uunb uooars
> m test.csy i traln.csy? 0 Configuration
> n LCENSE.tt pU3HOY38 0 sdwod< optimzer_rdk + P_NOTICE t requirementstxt NUM_ RULES: Specities the number of rulos to use for ovaluation. This determlnes which prompt flos to losd (o.g., evaluator-prormpt-10.txt vs avalualor-prompt-50.txt). NUM_ SAMpLEs: Controls how marry rors to sample from the full dataset. Set to O to Use al available data, or a positive rumber to fmit the sample size tor faster exptrimentation. NUM_OPTiMiZAThON_LOoPs: Sets how mary optimization lterations to run per experiment. Esch loop gcnerates outputs, evaluates them, end refines the prompt. TRAIN_SPLIT_FRACTION: Dotermlnes the trairtost split ratio. 0.8 means 80% of data goes to training set, 20% to test set.
> These varisbies control the experiment scope, data splittlng. cyaiuation crlteris, and ootimizstion intomsity.: (+ Coda: L+ Hrdoum!
> promot-esrang' @1 & 9 O 1: B Sedtct Portgris Sarvt TRADH spLIt_FRAcTian a a.s' a Fracttan of dats to wre for trsining (rest for cesting) ) to buxien 1on s1 trus) Doaoud Joien ean rot, uo pareg' 1tnfpe - 3ooojd wi ug soyny sa doay a 0s c s3nn hnh NUH_SwpiEs -'lea a Momher, or rovs to saple Iron the tull ditaset, o torial! t confiG: Hunber or saapler ro ise for the oroerinent. Adjust ss needed. Curior Tsb a in3, Coi 29 3 Spicex 4. Soncns: 4.: L5 (1: Cn 3 ot 26 2025-1.1-22113:03: 10

![[assets/dense-slides/SbcQYbrvAfI/slide-014.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/SbcQYbrvAfI/slide-014.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Dense notebook content with configuration text and section headings; better handled by OCR.

Slide text:

> PROHS ANINO notebooks > @ JsON_wobpsguoeneravionlpynb ) s Optimizlng JSON Webpiga Prompts wth the Arize Prampt Learning SOx ) + irport nert_aryncio.
> >. conds +' big_bonch hard )'codingsgant nles.: banchmarks. 十 Codo + Harkdown l D> Run All O Restart 司 Chor Al Outputs. Go To I 思 Vaw data Jupyler Viriablos Outhine t Iapor nest asyneiol Add so Cha Et Cuck Ea aa! nest_asyncio:apotyt). nD D:B -.a: a*acodo (Python 3.10.19)
> > datasets.v notebooks arireaxsupport... JsoN_webpt.. [2] Configuration Python
> F: emetaprompt.txt' U "buoddns.u+oud. NUM_SAMPLES: Controls how muny rows to sample from tha ful dataset Sot to O to use al avalabla data, or a positiva number to limit tho samplo slzo for fastar cxpcrimentation...
> >. optimizer_sdk testesy': train.csy support crutry_cia... u *('og-idwoxd-soirnuao ta xrot-dwod-oicneo.-5o) prof oi souy idwod youm pouumiop sili 'vogeaao doj ssn oi sau jo yoqwnu oui sooods:seind wnn TRAN_SPLIT FRACTION: Determnes the traintest spit ratio. 0.8 means 80% of data goes to training sat, 20% to test set. NUM_OPTMIZATION_LOOPS: Sets how mary optimization iteratlons to run per experiment. Each loop generates outputs, evaluates them, and refines the prompt.:
> 7. prompts. pw 3NGY38 ①: A LcENSE.tt * tP_NOTiCe 1 requlremsnts,txt These variables control the experiment scope, data splitting, evaluation crlteria, and optimization Intensity. TRAIN_spLr FRAcTIat - o.s' a Fraction or data ro use for traIning frest ror. tosting!. NUR panes - soi g arber, or rutes in the proapt - sajusr based on your avataator' prorot (thisels xoT torking on Config! HU_oPTMIzATICN Loops'-' 5 ' a'Nueber or'cpriairtIon loops perexperent I coicrIGi Nuaber of sarples to uze for the experiarnt. Adjurt as' neded. NUh_SaplEs = leo: o Mbtr of rovs to: saeple. Iroa:the fu!l'dataset, t tor. ai!
> 11 0.0t: Python
> SOUTLNE TDHEUNE prorpt-eunhrg: @ 1 A 9' m Sehct Portgrt Sirvr: We wll ta iielrn Iraral tn rararale tha wehaana luane:. OpenAl Key: Cunar Tss 7 a7 tn 9, ca 2oig'soben1 4 2025:11-2213:04:00 Soxcr: 4, F. 11. Cm 3 oi 26. t

![[assets/dense-slides/SbcQYbrvAfI/slide-015.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/SbcQYbrvAfI/slide-015.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Dense notebook screenshot with code and two section headings; OCR will be more accurate than manual reading here.

Slide text:

> v.PRoup! s benchmariks. $. big_bench_hard conda SRNO + Code + Harkdon I D> Run Al. O Restart l Cnr All Output: Go To: 电 Vie dau Jupytr Vmriabhs e Outhine:' notabooka ). @ JSON_wobpage ganeration ipynb >ius Optimizing JSON wabpage Prompts whh te Arizo Prompi Leamirng SOK') + Impot nesl_asynco TRAN_SPLST_FRACTlON: Detor mines tho tralntest splt ratlo. 0.8 mcans 80% ot data goes to trairing tat, 20% to tcst sot..?... -.* *:. M sa_codo (Python 3.10.19)
> datssets pU'3NGY38 0: I+ notebooks:., codlng_agant ruh...:> prompts: optimizer_adk A Ucense.tt. t P_NoTiCe: B toma_support quo.. BizNorm-100_eva B arizeax support q.-. JSON w+bpM toucsy tartcsy:.metaprompt.cxt U phoeno uppoL'q? support_qutry.cla. 15. u I'[t]: dwod eun sauyos pue wou saleneao 'sndino toleuo8 doog ysag tuoupadxo lod uu oi suogeay uonrz,udo Auew moy sos:sdooT nolivzwlldo nn These variabies control the experiment scope, data splittlng. evaluatlon criterie, and optimization intensity,' NUM_RULES: Specitios tho rumber of rutes to usa for evaluation: This determlros which prompt fties to load (o.g. evatuator-prompt-10.txt vs ovaluator-prompt-50.txt). OpenAl Key. We winl be using OponA to genorate the webpsge Jrons. 0.0 taufrG: Murbar. of sarples'to use Tor the. orperlnent. Aoyust es peeded. NM_RulEs 's 5o r Mmber or rutes Inthe pranpt - sdjust oastd on your evatuator pronpt ftnis Lr uoT torking sa Contsg! HUH OrTIHIzATIGH_LoOPs 's a'Hueber of optimiTation' loops per eIparisent Nun_saples m lo '. a Munter of rovs to imeple Iroa the fu!! carastt,. o ror al! Train SplIt_rRctioh - e.s t Frsction.of data to. uye for rraining trest tor. testing!. G Python
> 5 roquiremanta.trt Os.cnvIronI opEuI_ApI XEy'J - getpsss.gatpass('Oponil 'API Keyr'). Inport openal Lport os. setpass client - operaf.Client(api_keyos:getenyt-opEui_Apl_xEr))
> 7.81 Python
> Bn3rl t IHTunoS IVmyn' O promotsmng O'tAo R sohct PontgrTstrWr Training and Test Datasets Cunor'tb'a7 Ln3, ca2o Spncou: 4.. Spscn: 4 U. Cn 3 ot 26. 2025-11-22:13:05:15

![[assets/dense-slides/SbcQYbrvAfI/slide-016.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/SbcQYbrvAfI/slide-016.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Dense code-and-text notebook slide; OCR is appropriate.

Slide text:

> notebooks s B Json nebpog Iraxuts ai,pdreta ya uxruas ol,miu3. ttoid) Llot lav rvuooo 3:asojog t+1 pue bupnt/1 th
> pret younq ba kt: prompt. datasets A LICENSE.tt coding igint nua. 3. benchmaris op timkzer_idx. 3OUON'd s it roquiremants.txt v. notebcoks.conda Tarb ocdns irttt a D tostcsy B BizNorm-100_.- D arizear support.. Ass'upna I phoena iupport q..: JsON motaprompt.txt'U support_query_cla. L+bpsaM U. 十 Code + Markdown 1 Interupt: Rastart B Ckat Al Outputs O Go To | Ea Viaw data Jupyter Vrizbhas 111 Training and Test Datasets: OpenAl Key. Wo wl bo using OpenA to gonerato tho wobpsgo jsoni. client = openi.client(apl key-os. getenvt opEut_AoI KE!) TAIN spiIt_FRucTIon - o.s e? Practlon'ot data to use'rortrn iatng (rest ror' ioiting!. os.envlrenl opEiAr ArI _xEy']'= getpsss-gripasst'openAI APl Key!? 3 cowfrs: Hunoer or saaptes to use for she oxperineot. Adjust' as meded. HN Rues s S a Muber or rules In tne prorot adjusr based on your, evalustor gronot (chit is wor torking or Contig). lnport os. getpalt a Teuado ijods1. HuH_Saplts = iue. e tuber of'rows 'le'ss=ple: rro=. (ha'rutt datatet.' e ror'af! 0.01 4ot. t5o 旧 aie_codo (Python 3.10.19). DDa- e. uonAd: uond
> Creato tralning and tost datasols, and export to Arize.
> inport pandis as pd
> > TuELnI BSOUTLohE' Lman O promgt-feamng '@ 1 A 9:B sehct Postgrs Sewr [4] dataset_1ooo:= pd.resd_csv(-httpsi//storage.gogleapis.cou/arixe-asets/oev-rel/proapt-ltorning/guerles.csr) dataset soaple' = dataset_lo+?.ssaplc(kH_sAples) e 1h ro? aror nb'ya7 tn a, co 2o:Spico* 4. Sp*c+t:.1 Lf. Ct & ot 26 2025-11:22 13:05:40

![[assets/dense-slides/SbcQYbrvAfI/slide-017.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/SbcQYbrvAfI/slide-017.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Dense notebook slide with small tabular preview and prompt section; OCR is needed.

Slide text:

> ANINO notebools s JSON wobpogu_genermuion,fpynt ) ua Optlrmieing JSON Webpage Prompts with the Ariza Prompt Learming SOk's ma Trainrg and Trst Dasasots') +: dataset 10ooruad)
> conds ' banchmarks. + Code + Markdown 1 D Run All O Restart E Clear Al Outputs: I Ba Vhw data Ea jupyter Varibir, E Outins. Laoort' pandas as pd sa_code (Python 3.10.19)
> . datsets?.:v,notebooks'.seu usbr Bupos. optimze_sdx ib uoddns xnozue a m tustcav Imnasupport que. D taln.csy. D BizNerm-100_eva.! D phoenaiupport q.: It) -ps"Aorb uoddrs. metaprompttat' u USON SAEMu1 0. u dataset_1oao - pd,read_csv(-httpsi//storage.googleapisico/arire-Sstets/dev-rtl/propt-learning/gueries.csy trainEset = 'tatasetisanple.sple(trsc-TAAIH_SPLIT FRAcTIoN, ropdoa_staten?) test iet.tocrviniest.csv, indenFatse).. 0.5: IHjpe*a'iot ianrp tou Nt a (s1dhs hn)mta+1'eo1.1arp'= ato=as>tr1tp train_ set.to_csvi"train.csy", tidex-fols.) tttt ket = dataset_:arpta.drooltrain_set:Index).saple(5) 0.0t:: et Opem,'dstae iooo' in Deto Wringlh? B:4 Python Python
> LIceNse tt.? prompts. * P_hotiCE 0: Crute a tebpsje tilh a Aariguton bar canthe. hrput
> 1 requlrtrtnta.bt 2 Crust a perianu blog hormpsge tat tntroducu. Buld & univertity depatremt webpage, ht ihou.. eneate a 'service page Ior a photognoher th...... -.
> Initial System Prompt
> .INirl < X V mint O "OUTLDHE prompt-eamngO 1A'9: Initlsllze your systom prompt. This is tha original prormpt that wti bo tested snd optimizod. Jhung imhysag ores t Cursor To: e,p U. 1fCo4 10 oi 27. 2025-11-22[13:07:51

![[assets/dense-slides/SbcQYbrvAfI/slide-018.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/SbcQYbrvAfI/slide-018.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.
- OCR decision: ready — Dense notebook slide with small body text and code; OCR will read it more reliably than direct vision.

Slide text:

> Initial System Prompt

![[assets/dense-slides/SbcQYbrvAfI/slide-019.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/SbcQYbrvAfI/slide-019.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.
- OCR decision: ready — Dense text-and-code notebook slide; OCR is appropriate for the small body text.

Slide text:

> Evaluators

![[assets/dense-slides/SbcQYbrvAfI/slide-020.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/SbcQYbrvAfI/slide-020.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.
- OCR decision: ready — Dense text-and-code notebook slide; OCR is appropriate for the small body text.

Slide text:

> Evaluators

![[assets/dense-slides/SbcQYbrvAfI/slide-021.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/SbcQYbrvAfI/slide-021.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.
- OCR decision: ready — Dense text-and-code notebook slide; OCR is appropriate for the small body text.

Slide text:

> Evaluators

![[assets/dense-slides/SbcQYbrvAfI/slide-022.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/SbcQYbrvAfI/slide-022.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Dense code slide with small function text; OCR is better than direct transcription.

Slide text:

> s benchmarks. conda T-lEArnIhO Cupno EoaryeA okdrr 回 eitp uA B Ianano Iv rop ueirog G Iv uny △ I LopteW +: poo 十 notebooks > 9 JsON_wobpaga goner ation.lbynd ) us Opilrmizing JSON Wobpsge Prompts with the Arize Prornpt Learrlng SOK s u: Outout Generatlon > + de! generata_output(datasot: a*a codo (Python 3.10.19)
> umunbeBupos< big.binch_hard 0.0. mond
> . S' dataseta v. norebooks *b iodonsxeezur @] Additional Metrics +. Coda 十 Mrkdom
> prompts:.. optimizer_sdx O README.md, LIcensE.ot: 3OuONd t f requlrarisnts.txt m tan.csy: D tema_suppor_que.. testcsy B. phoenh support q... Tataprompttxt. U apuonb uodont: 0 Irou sklearm.netrics Inpart!1. Ytrue bin - Il it y -rcorrect" alse o for y iny_true!. retum' recait scorety_true_bin, y pred_bin, zerodivisiont) conpute_netricty_true. Y-ored, scorer--accuracy')!: Y.true and y pred should te tists or arrays ot'-carrect"/"ircorrect" latels.. + yg'to birary [psjdA ug x Jo, 0 oro 2asauios, A 'st t] - urg paudA Conpute the rtqueited setrit. toe binsry classitication.. It scorer - "accuracy"?. elt scorer -irretatl"ie.. elit.scorer=-fi"s allf scorer'iprecisian"!: olse! return precision_scorety_trve_bin, y_ored_bin, zero_diyislonso): retarm accurscy_scorsiy_true bin, y_ored_bin) rsise ValueError(r"unknoun scorer: (scorer)-) return (1 scoretytrve bin, Ypred_bin,' rero_divisianno) score, prccision_score, recallscore. accuracy_scare.. 1：....
> 0.91 Python
> ) TutUnE: OUTLLHt Lmsn:O: pompt-eunng: @129 M Selact Postgre1'S4 cnor mb F@ in 1co 20. spno:4 2025:11:22[13:18:38 -So*c*1 4L5t.Ca4 160t 27

![[assets/dense-slides/SbcQYbrvAfI/slide-023.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/SbcQYbrvAfI/slide-023.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Dense code slide with small function text; OCR is better than direct transcription.

Slide text:

> RNINO notebooks >: β JSON_wabpsguLoeneraton boynb'> us Opilmizing JSON Wabpaga Prompts wrh the Arlra Prompt Loaming SOK > M: Output Ganeration /> + dat gonerato_outputidatusot
> benchmarics?.3 conda bg_banch hard + Code + Markdom I D Run Al S Rostart 显 Chx All Outputs 」 e Viat dat 国 Jupytr Vaniablrs: B Outine: sa_codo (Python 3.10.19) rytnon]
> .y notebooks README.md:+, datesots.> oplimizer_idk.: coding igant rues. A LCENSE.bt: *IP_NOTICE requlrsmonts,txt [ tmaisupport_quo.." PJsoN wbpe. M buoddns xeazut a m test.cry a tan.csy: Bl2Norrn-100_oa phoenb_support q. 1. rmetaprompt.tt: U. prompts: support quor.cla. 0 Additional Metrics.:Tron'sklearn.metrics iaport. fl score,' prtcision. det compute_metric(y_true', y_ored, scorera-accurecy.):' Ytrue dd y.pred' thould. be. lists or arrays ot "carrtct-/"incorrect" labels. Ytrue bia -'ti'tf y --"corract clte e tor' y'in y true]:retorn. 11 scoreiy_true_bin, Yorea_oin,zero_divistono) ollf scorer - "precision*! Y-pres_bin'- (l l! y. es "correct" elue + for y Ln y.pred) cetcorer -rrecsiun.! I rap to blnary. elit scoror..- -fi"! Coapute the rtquested' cetric for? birury.classlficatlon.: if'scorer."sccurscy"t.. elsoi.retura precision_scorety.true_bin, Y.pred bin, zero_divislonto) return 'sccuracy_seorety_true_bin, y.pred_bin!. return recall_scorety_trua_bin, Y_pred_bin. xero_divisior-e) Tsito ValueError(t"unknoum scorerr (scorer]-) score, recallscore,: accuracy_score
> 0.91 uonld
> ) ouTuhe. Jrs hubsod pnos a s Vt O cuuridwod Optimization Loop Cnorhb @ intca20 Spc:4 12025-11-22113:19:03.Spxc*c 4. LF. t. C4 16 ot 27.:t

![[assets/dense-slides/SbcQYbrvAfI/slide-024.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/SbcQYbrvAfI/slide-024.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.
- OCR decision: ready — Dense notebook text with paragraph and bullets; OCR likely more accurate than direct transcription.

Slide text:

> Optimization Loop

![[assets/dense-slides/SbcQYbrvAfI/slide-025.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/SbcQYbrvAfI/slide-025.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Dense notebook text with paragraph and bullets; OCR likely more accurate than direct transcription.

Slide text:

> epuiosc > big_bench hard > banchmares: >codhg_sgmtruh PROuPT-LEARNiNO + Code.:+ Markdowm. I > Run Al O Rostant B Chr All Outputs:| e Vhw data Jupyter Varisbln: I Outins': soss"Astxiost eroosroaai 'esoss Voycpasd 'sossy boduy taiowusrops iwar + ( soynon ruonppy in < quird-voprauowcedqam Nosr a < syooqoiou tet coajute matriclytrue' y.prrd, scorer-accurry/r- 0.91': sa_codo (Python 3.10.19) Python
> .) dstssets?.Y notebooks [ artzeax stpport a BtzNorm-100_oal Optimization Loop This cell kmplemonts tho coro prompt optimization algorithm. The loop folows & 3-stcp process:-
> testcsv m tar.csy: Ioma_supportqu... B phoenb support q. x: mataprompt.txt: u support_quory cla.. 0 Key parsmeters:: oui -viep uoerqeas meu pue 'sidwond pazpurido 'sojoss Aoemose isatujen bupnpu siprsas poneiap suuniai pue suopejay ssoog sopisw sysen wuuobye bl1 ' ssuioaios jjotn oienjeae pue joseiep isai oui uo jdwoud juaums sun Supsn sindino ojereuog onenjeas g ajtaueg Train & Optimlzo: lf results are unsatlsfsctory, genorata outputs on tho training sat, evaluste them and uso the feedbsck to croato an improved prompt:. peapos, yolemjeao uo poseq jduod was/s ou ouyoy Aaanlol ol ornuidoouueondwald 5u sosn tojioziupdo Hterate; Rtpeat untl either the threshold is met or al loops are completed
> in'tyuowannbeu t. Sdwod t. ① READuEmd A UCeNSEtt: 3OONa Xoptm'ze_sdk + num_rules: Number ot avaluation rules to use + ithreshold: Targot accuracy score to stop optimzatlon? (notebookdtr path().sbsolute().tron pathlib inport Path loops: Moaxlmum number of optimlzation lterations sys.gatn.1nsert(e; str(notebook_dir.parent)) Lnport syt Tros opt inixer sdk.pranpt learning optinlzer Lport Prowotlcacningogtinizer [scorer: Motric lo optimlze (occuracy, (1. procision, reca!)
> : 2Hurl < OUTLDHE prompthemng: 0 1 A 9O 16 B Sohct Pottgnh Serr' dat optlnire_toopt toain'set,. test_set,. systea_proept, Crtor tob Fa -,Spac+L4. LF - t) 2025:11:22 13:20:18 Coh 18 ot 27

![[assets/dense-slides/SbcQYbrvAfI/slide-026.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/SbcQYbrvAfI/slide-026.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Dense code slide with small source text and docstring-like content; OCR is the right triage path.

Slide text:

> LARNINO notabooks ) JSoN_webpogu goneralontynb > m Addltionat Metrics >+ tran skbaarm.mioirics import f1_score, precision_scort, rocall_scora, acuracy scort
> $ benchmarks $big bench_had.canda + 十 Markdowmi | D Run All O Restart Char Ali Outputs I &a Vow daa Jupyter Variables: Outline: *: *a_code (Python 310.19)
> .wnatebcoks.coding sgant ruhs + datstets D anizenx support_q 0'BliNorm-100_van:sys.patn.Lnsert(o, strfnateboox dir.parent)) notcboak_dir a Path().absolute() (nporr: sys frsa eptlalar.tax. proeot tearming. opti*liar. Lport Pro. Iron pathlib laport Path 1 ptLrarnigbpt intrer “.. *'.
> sduod c: optnize_idx A, LCENSE.tt P_NOTCE E testesy ' trarcsy: metaprompt.txt U tama_support_quo.... phoeno supportq. "tsuanb uoddns u U' tet cotinire_loopt evaltatcrs, Storeri one ot -ocuresy a(nn. rarecisian, "recaiu Crarer'accursty threshatdat. tost_xet; fhresholer float.: thrtshald:tor tha selected setrie trin_set,' toopts, -
> Refurnst.
> t requriremanta,txrt 1.. dict wlth teyht. "ra": 1ist ot'test'set Dstofrsees. Idecptopy) ror:'tscp teit,run *traIn's List or. train set scores ptr rin *iestgi tist at test yet Tcores par. run. "proapta Llut.a! systes proapts ustd fot tach teit. run.
> Lapart:cooy
> >TINCUHE I' maint o porot-lsmng: O T A 9 O 16 L Sehet Posigrt Sarte? curr_toop = 1' trati_setrics,=.[]: test retries = t1 cuntor Dab 2025:11:22113:20:43 So*c0: 4UF.C*4 16 ot27

![[assets/dense-slides/SbcQYbrvAfI/slide-027.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/SbcQYbrvAfI/slide-027.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Dense code slide with multiple small code lines and parameters; OCR is the right triage path.

Slide text:

> + big.bench h: > banchrnur.>:coding_agent "cond 十 Code + Makdom I D Run Al S Restart Char Al Outputz:| Ee Vhw data. Jupyter Variblrs. E Outine: rotebooks > B JSON_webpage_genoration (pynb ' m Audltionot Matrics > ui Oplimizatlan Loop ) + Iimport sys trmin_set[-correctness*] * (None] + lea(trsin set) train_set[-rute_ vlotatfons.] = [tone] e: len(train set) trein_set[-explanation"] - (None! u lenttrainset) nD DE -.n. aia_codo (Python 3.10.19)
> v notebooks [ Rarra_support_qut.. ariraax 'support 4-i B BizNorm100_w n tostcsy B phoenb_support q. t. meiaprompt.tt U JSON WPM support_query_clh.. u: opt intzer = Proaptlearningoptinizer( train_set, -. optinizer.run_evatuotorst troin_set,. pro+ot-.yste gro*pt,. openai_apl_key*as.getenv("oPBAr_API_KEr") Sodet eharre-"aot -4o".. eyaluators. fecdbackcoluensI"correctness",
> R. LICENSE.ot Isdwod e 2. opbmze_sdk + p_notice I talr.csy: $ystea_pro-pt. t-optinircr.optinixt! "output". trein_set,: context siic t+128eh feedback cotuntit-correctness". "rule_vlolations"]:
> .@ READMEmd
> 1NLn0 5. + requlrumertatrt V:mn+ O pomp-mng 01A9016 fet! y_pred_trsin_post - train evats post tralioutputs_post - generate_output(trsin_set; systeapronot): troin_set post =:troin_set.topy(). train_evats_postgall = evaluate_output (train_set post) fo]. train ewils post - train_ewals post_atlf-corrcttncss"] train_setric_post vatue'-conputa_netricty_true_trair_post, y_preo_train_post. tcorerscorer! train_set postfroutput"] s tesin_outputs post Ytruetrain_post- I"correct"J = len(train_evsls_posi) train_setrics,append(train_metric post_value) 0 Evaluato.trbin, set after optimlzatIon Sehct Posigr+t Sery? Cnar Tss Pa Soscre 4. Vb. sf 2025-11-22113:21:58 Ch4 20 ot 27 广

![[assets/dense-slides/SbcQYbrvAfI/slide-028.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/SbcQYbrvAfI/slide-028.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.

Slide text:

> Experiment Execution
> Execution: Runs the optimization loop with the specified evaluators and configuration parameters, tracking performance across iterations.
> Results Saving:
> - JSON format: Saves complete experiment data with timestamps for detailed analysis
> - CSV format: Creates lightweight CSV files with iteration data, metrics, and prompts for easy visualization

![[assets/dense-slides/SbcQYbrvAfI/slide-029.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/SbcQYbrvAfI/slide-029.html)
- AI slide classifier: `content_slide` confidence `0.96`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Small execution-output text and tabular output are better handled by OCR than direct transcription.

Slide text:

> +, banchmarks?: 3 &ig. bonch hard tpuoor.c. EARNING:十 Code:十 Markdowm I D Run Al O Restart Chaar Ali Outputs.I B Vew dab E Jupyter Variableg 三 Outine: cit jodu, + c doon uojrzuido in < souoyt gtuogppy in't quldruogtroueo eeedqom Nosr a K tyooqojou ia_codo (Python 3.10.19)
> Iv notebooks coding_ sgent nlel:? datssets JSONWObp..: M Iuma_support auo. uan.csv. BizNorm-100_ov testesv boddn/qmoqd t: metaprompt.txt U byoddnsxrazue s-Auenb uodans 0 Save Csy results savo_cxperinent_resultsl resutts: "etperiment_results.json"!. print(results) cvsluators = Ievnluste_output] 7 save resolrs: Savesingle_axperlment_csv(results, "experlmrnt") print(nud Experient resutts:") resutts = optiize_loopr. train_set, test_aet, syztea_proept, evatustors,.. LOOPS-NUN_OPTIHIZATIG_LOOPS
> ①. README.md? prompts. R license.ut. 3OuON'd. requlramntn,txt:cptimlzer_idk 322 $ Startirg prorot. optimization vith S. lterations (scorer:accuracy. threshold: 1) 456 311 Initfat evaluation:. Avsiubte. columrs: ["uenaned! D'..'trput',.output',"'evaluate_output_cxecutioo_detalls+. 'evaluate_output_score'] dataset'. lt_scrtrato 1l 13m 53.01: Ursmed: a:A56 Generate a blog post page shaicasing the'tates... 3SB 322 2 besign a travel sgency's landing prge tor, exot... Craft + veb psge with'o sticky sidebar. on. the... Craft a vebpage for sn. art gallery ryent, witn.... 5/3 (190.*) 1 2 +0:16-04:0+'1 3.32s/1t. id5.
> > TM[LIHE V mnn*.O poagt-unng. 01A0016 322:(n "lsndingpage"t (n'.:*+itte"s. "Exploro E.. H Sefact Postgrt Serrt....... output expluntion correctaess. Hone Hane Cunar ne We T tno, co 1'/sorcon 4 [2025-11-22:13:24:03 Soc43: 4. LF C++ 20 0127. t

![[assets/dense-slides/SbcQYbrvAfI/slide-030.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/SbcQYbrvAfI/slide-030.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.

Slide text:

> Optimizing JSON Webpage Prompts with the Arize Prompt Learning SDK

![[assets/dense-slides/SbcQYbrvAfI/slide-031.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/SbcQYbrvAfI/slide-031.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Dense notebook code slide with small imports, evaluator setup, and output; OCR is the better triage path.

Slide text:

> : $ banchnaras: > big bonchhad.notebooks. Sesnep s ①README.md >conds 2, coding agent ruo. pompt... A License.ot PNOTICE t' requlrsmenta.txt:"buoddnsozue d Protpt. a traln.csy. I Itaisupport_que. BlzNorm-100_e. optimize_idx metaprompt.txt U support query_cla. trstcsv phoeni supportq. Jsor*ebp+-. CHNIYI 0: otabooks y. B JSON_nobpsga geeralionipynb >'s: Optlmizing JSON webpsge Prorapts with the Arize Prornpt Learrleg SOK > + rnport nest_at + Code + Markdoum I D Run Al S Rostant i Cha Al Outpouts I e Var data. tros phoenla.cvals kport aoenAinodet,: Iu generate trou phoanil'tals Lpart avatuhte_caatrae, Ciassit icntionEvaluator' dat evaluete output(cataset]t Ith opentr.:/oroaps/Json_,rtosge_generat ion/ev luitor-proaot-u_uLEs).txt-, r! os fhlet. *-Evaluntot: thnt thechts son veb page,correctoosn. uning Ila generaie-. evaluation teaptato -- flle.resat) rvaluatar n Claisiricnt ionEvaluatort. resvltr dt. -'eva late catatre! Ils = Lutiproridere"apctu! model-got-4o") ootaet?. jevalvatar):evsluotion_tenplaie, ll. cholces=f. -vatoate_outpu!". "corrocrt'!. "incorrecr"?.. o_coda (Python 3.10.19) I how do I turn an Hre numbers? notobook: 1. Cllek on sry codo ce to: 2 Prais the C koy tin. 1. Press Esc to ouit eoht inode: Tougn rone1 Il your'ra n edt mode (cursor a Thks w[l togglo Ene rrurnbers orvott for a celi in thi? Inside + eoh:. huve a ftw optlone. Quick Method To turri on Ere numbers in your'? Jupyter naleboot in Cursor, you Altemative Method BJsoNwebpage aunarabon.. mode)::0pou purwwos jea po talect lt (don't anter edit. command mode, not eoit. mode):
> I fubvgi prui! aratlsalo coltars.. print(t"Avaitable colimasr Iresutts_d!,cotmns.tollst!)) 2: Then press L' to toggle ina murnbers
> +ms O promot-smrg O 1 A 9 0 3 satct Portgrs Stve 111. datsvet I"eplonUar"].s rtfuits d!.get("avaluata_output eaploretico", tooe). datasetI"corrrctoers") a resalt'.dr.get(-evaluuta output iebeL, Nore). CanorTb Qn Tco 20 Spxc$: 4*. Soaos: 4t. 12025-11:22 13:30:06 TUHT

![[assets/dense-slides/SbcQYbrvAfI/slide-032.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/SbcQYbrvAfI/slide-032.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/left-72/opencv-adaptive`.
- OCR decision: ready — Dense code-and-output slide with small text; OCR should recover the code more reliably than manual transcription here.

Slide text:

> BaUB· JsoN_wobpsge_aanation.lpynb M
> C proh+t-LtarnitO 'coding_sgent rues_optim..?.conde. banchmr'a.:> ba bunch_hard + Code + Myrkdom | > Aun Al O Restan E Cor Al Cuipuu B Vrew data Jupylr Vsriabhs nolcbooks ) O JsON_waboage_Lmerstlor.gymb ) us Ootimiring JSON Wobpaga Prompts with the Arize Promgt Lea! Here is lho prormpt thst schleved the best test occurscy scross the optimlzatlon Herations.
> .' datnsets notebooks arfzaar support query.c.. onenRao cot-wontia D Jsoh rebpage oen M phoena supporl guery_c.: Bama_suppori query_opti E metaprompttxt: dat get_test_Droaptfreiults): Extract the pronpt that schieved 'tho best test accuracy. Args! Returnsi.. tuple! (best_proapt, best_accuracy. ittrtion_nmber) ' resultsl Reiults' frou opttaize_ loop or erptrinent. 1.
> ?OUTLNE )TIMELUNE $ optimizer_idk soiod A: 5 JSon webp+ge_goneretioni traln.csv poptxaps Arenb todans a tst.csy. L mun' O. prongtierning E tvafuator-prompt-so.txt. ol-iowosd-oypnp-apu: eyauator-prompi-100.xt waluator-prompt-i0.tt nte-checker-prompt-30. u u 01A9OJ Sect Postgrc S Dest oronpt, 'best_accuricy. best_iter'- oet_best_proaprl resuits) printt reest Ogtimixed Prorpt Iiteratton (best_Iter), cccuracyt: (bestsccuracyi.3th)t") print(best proept) I Lyage. wraapte?. prlat(rroriginel Proopti: (systeaproopt)-).. pronots = resultil'propt'].. + Fins tho iteration with hlghesr tesr. sccuracy test_prorot = pronpts(best_iteratlon] [.111.]511ns01 =. 521110*1501 return best_proupt, best accuracy. best_iteration best_iterstion = test netrits.iodex(max(test petrics)) best_sccuracy = test_netrics Ibest_lteration]: tt CunorTab Ia-

Classification audit: `raw/sources/slide-ai-classification/dense/SbcQYbrvAfI/audit.json`
