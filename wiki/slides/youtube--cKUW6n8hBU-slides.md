---
title: "Slides: DSPy: The End of Prompt Engineering - Kevin Madura, AlixPartners"
category: "slides"
video_id: "-cKUW6n8hBU"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: DSPy: The End of Prompt Engineering - Kevin Madura, AlixPartners

## Source Video
[DSPy: The End of Prompt Engineering - Kevin Madura, AlixPartners](https://www.youtube.com/watch?v=-cKUW6n8hBU)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/-cKUW6n8hBU/slide-001.jpg]]

OCR text:

> -

![[assets/slides/-cKUW6n8hBU/slide-002.jpg]]

OCR text:

> , 5 : Q u et / Pd rc |
> OTT D) iS a
> DSPy is a declarative framework for building modular AI software.
> 
> It allows you to iterate fast on structured code, rather than brittle strings, and
> offers algorithms that compile AI programs into effective prompts and
> weights for your language models
> 
> aLaee SH LeRs >) ee

![[assets/slides/-cKUW6n8hBU/slide-003.jpg]]

OCR text:

> , : , ao a = 7 RB r
> oR Resa ee oe aor ee
> Use Cases Lighting Round
> |
> AYA"AoecLan zen | erehiced
> - Simple sentiment classifier Fl El
> - Structured information from a PDF = 1
> - Multimodal extraction [a]:
> - Web research agent (using Tools) .
> - Detect boundaries of a document github.com/kmad/aie
> - Recursively summarize an arbitrary-length document
> - GEPA example
> |

![[assets/slides/-cKUW6n8hBU/slide-004.jpg]]

OCR text:

> DSPy allows you to decompose logic into a -
> program that treats LLMs as a first class citizen...
> ... Without having to tweak prompts (unless you
> want to)
> 
> e

![[assets/slides/-cKUW6n8hBU/slide-005.jpg]]

OCR text:

> 1
> , }
> . Fs
> Fad Be
> ei
> 4 a «rie bew
> oe ei a ae r
> ane a a aed

![[assets/slides/-cKUW6n8hBU/slide-006.jpg]]

OCR text:

> ’ . 7 q f 7 1?) “ a a“ a] ta
> ges v Feerews you to re “ we |
> detailed control over your program while focusing on
> things that actually matter
> e Allows you to create computer programs that use LLMs
> as inline function calls
> |
> Mi iN" | mM S Tt ff h © Programs which you happen to be able to optimize - it's a
> programming paradigm, not a wholesale framework, and not
> qa n qa 1 0 C ALU “optimizer-first”
> e Is built with a systems mindset; you encode intent and
> structure in a way that is transferable
> © Your program design likely moves slower than Al advancements (at
> least so far)

![[assets/slides/-cKUW6n8hBU/slide-007.jpg]]

OCR text:

> this way of working
> found it useful - the hope is to
> tives for you to extrapolate to

![[assets/slides/-cKUW6n8hBU/slide-008.jpg]]

OCR text:

> ; . y : g@ i eS . Vd r ;
> |
> Core Concepts
> Specify what you want, Structure your program Interact with the outside
> not How: let the LIM logically world - or the rest of the
> tie tcam@lelt jo) dere eben!
> Adapters D
> Customizable prompt Optimize your DSPy Define what to optimize
> formatters: think JSON. Pyke eter en YO enleu(a against (can be multiple
> BAML., XML. ete. things)
> (let the LLM figure it out!)
> Po ;

![[assets/slides/-cKUW6n8hBU/slide-009.jpg]]

OCR text:

> ee , ; , Go " 5 c p a |
> e How you “express your
> iN ry lI T re Ss declarative intent”
> e Can be simple strings or
> complex Class-based objects
> |

![[assets/slides/-cKUW6n8hBU/slide-010.jpg]]

OCR text:

> input text to classify sentiment
> he more positive

![[assets/slides/-cKUW6n8hBU/slide-011.jpg]]

OCR text:

> input text to classify sentiment
> he more positive

![[assets/slides/-cKUW6n8hBU/slide-012.jpg]]

OCR text:

> £ . : ©] u" cy e a r
> PAf_Link SHARPEN rerePne ToT REPORT ont net /CIK-0001045810/8b7édacc-alSt- 4292-960. a ann
> . oo
> Ni T Iti m ft] i a | iY seem aseacnmense ve
> rag = dspy.ChainOfThought ("question, document -> answer")
> FORM 4 Be 4
> SUES Tt wmmscuenugeranettgena emma OT result = rag(question="How many shares were sold in total?", document=doc)
> me inca emesis print (result)
> EE ony SIATEIT. . ~e if Predictacn(
> renee Bvt es tee ane Vorerttes coed reasening-'The doftument is a Form 4 filing reporting changes in beneficial
> 7 . . Ce eee Lo qnerehip wf geouratres by Mart. A, Stevens. if casts two transact pons mavecjvernd the
> fetes oe Fe sale of common nteck shares on twe datesiunins On P1/2006, 209, 200 shares were
> =e pe 2" 20 oe holds ine Gn Y 12s7Crh, 20,790 shares were sald.ininte find the total numer of
> : ee ee ee ae shares seid, we sum these twe amountoi\nsnacda,0CG 4 290, 94 = 490,098 shares maid
> oe I oe e Be, ue ih tetal.\nainNe other sales transacticns ate listed in the document.',
> ——_ Boe TS ne answer='497,797 shares were sold in total.‘
> woe Te )
> aaa ee
> Bem nmitee me te ga a od
> |

![[assets/slides/-cKUW6n8hBU/slide-013.jpg]]

OCR text:

> changes in beneficial
> transactions involving the
> ,200,000 shares were
> number of
> sharessold

![[assets/slides/-cKUW6n8hBU/slide-014.jpg]]

OCR text:

> ; , a 7 go ity ry 7 A ec
> | Omani ats eRe ee |
> Optimizers
> | DSPy has various built-in primitives that allow you to then optimize your
> program. This allows you to quantitatively improve your performance and
> cost profile.
> _ “A DSPy optimizer is an algorithm that can tune the parameters of a DSPy
> | program (i.e., the prompts and/or the LM weights) to maximize the metrics
> you specify, like accuracy.”

![[assets/slides/-cKUW6n8hBU/slide-015.jpg]]

OCR text:

> “DSPy is not an optimizer. It's set of
> programming abstractions (signatures, modules)
> that can be optimized.”
> - Omar Khattab @lateinteraction
> 
> e

![[assets/slides/-cKUW6n8hBU/slide-016.jpg]]

OCR text:

> ESTs a 9y RE |
> The reason that this is tricky is quite subtle. It’s the fact that \
> anytime you use an LLM to assign a reward, those LLMs are giant
> things with billions of parameters, and they're gameable. If you're
> reinforcement learning with respect to them, you will find - Andrej Karpathy
> adversarial examples for your LLM judges, almost guaranteed. (via the Dwarkesh
> So you can’t do this for too long. You do maybe 10 steps or 20 Podeast)
> steps, and maybe it will work, but you can’t do 100 or 1,000. I
> understand it’s not obvious, but basically the model will find little
> cracks. It will find all these spurious things in the nooks and
> crannies of the giant model and find a way to cheat it
> @

![[assets/slides/-cKUW6n8hBU/slide-017.jpg]]

OCR text:

> fi J E . 3 Ul) 4 _ p r
> rT
> GEPA: REFLECTIVE PROMPT EVOLUTION CAN OUTPERFORM = = ra
> 
> REINFORCEMENT LEARNING ae
> 
> Lakshya A Agrawal’, Shangyin Tan’, Dilara Soylu’, Noah Ziems‘, Ls 7
> 
> Rishi Khare!. Krista Opsahl-Ong', Amay Singhvi?*, Herumb Shandilya’.
> 
> Michael J Ryan’, Meng Jiang‘. Christopher Potts’. Koushik Sen’. ia
> 
> Alexandros G. Dimakis'-', lon Stoica', Dan Klein', Matei Zaharia'’, Omar Khattab® .
> 
> "UC Berkeley "Stanford University *BespokeLabs.ai ‘Notre Dame ‘“Databricks = *MIT Chris Potts
> https://www.youtube.com/
> watch?v=Obkwd90 Yaqfk
> 
> “Model —HotpotQA_IFBench Hover PUPA Aggregate Improvement
> 
> Qwen3-8B
> 
> Baseline 42.33 36.90 35.33 80.82 48.85 —
> 
> MIPROv?2 6 47. 81 1] 6.26
> 
> GRPO 43.33 35.88 38.67 86.66 51.14 +2.29
> 
> GEPA 62.33 38.61 52.33 91.85 61.28 +12.44
> 
> My point here, though, is that both of them outperformed GRPO, which ought to be a
> kind of advanced RL-based post-training method, a fine-tuning method.

![[assets/slides/-cKUW6n8hBU/slide-018.jpg]]

OCR text:

> This is all you need to construct arbitrarily
> complex workflows, data processing pipelines,
> replication of business logic, etc.
> 
> e

![[assets/slides/-cKUW6n8hBU/slide-019.jpg]]

OCR text:

> DN a
> @lateinteraction e Creator of DSPy (and ColBERT!)
> @maximerivest e Creator of Attachments
> @tech_optimist e DSPy advocate, programmer, nice guy
> @dbreunig e Writes excellent technical content
> @DSPyOSS e Official DSPy account
> @getpy e Curator of DSPyWeekly
> 
> @kmad e Me
> 
> Po

![[assets/slides/-cKUW6n8hBU/slide-020.jpg]]

OCR text:

> 5 —_an
> mS
> -~ 4 eo: }
> ee =. "se
> ~_ a
> i” a “ 7
> mas
> Ws Pg
> Meh ~ =
> ra:
> Oo “Qe =
> 5 Le ee Bigg
> > TLS
> ’
> . was + +o.
> . - nee
> a:
> fen ws
> 3
> Pa

![[assets/slides/-cKUW6n8hBU/slide-021.jpg]]

OCR text:

> zs 2 Sr © SOO GT CC Sc oc a
> ee . d E . go " cy . ‘p r oees
> el iS @ arpr_wokirno nb FF = - ee ee = © Scan ett ow cm
> D8eT_woRKsHO wee |e a a Be. soe Ot be
> ° 1 Code 8 Yarksuar pteract ‘OD Oustet . Caw al Cutpets 6 Ge Ta ubyter arate Outee ve Fett 5:
> ‘ante 1 # Set up observadasity A a R
> 2 fege chorssegstet etre
> mochene_onaerge ; om cre Import reqister
> modules 4s cortiguee the Prcenie tracer
> yet 5 tracer_provader = reqistert
> © Boundar Detector by 6 preject_namee"aie-wornsmae™,
> © Doc umentiaveier oy + quto_instewmentetrve # Astd-iestrument your spo Dated on installer OL secensercies
> ko
> © Oecummntlrccesiet oy
> .otat fa
> © Se uner OF . mmr
> O vauedrancer ty MICO Me a as Te OTR Sees Tobe ETE SM SD. at ee TEE, CHIPS ah yale Coctadeas (73, detcese cat Tedemlerning: [Progress not found. Pleave wadate junyter and ipywiigety. See otis). ove
> @ visu arlons py from .autenotedeck import toda as notebook, tade
> © mar cy ue
> O ee “
> ecrenm ore
> © gtegnore
> Eython-verscr v
> B aspy_workshcp_cwa
> @ Stopmeekstoe pyro
> B hub ord u
> + OCENSE
> sable fied Seteg ice swe Termena be eee detetes tat manim me 2 :
> © pyererec teers v 2 ‘ 3 - fae *
> + README ma (tetera MPPTEEST |~/0/d/4 module example) (149951 (Wi. eere] (Grmain =]
> +
> B vocursee wemmarna oY
> O tore ertyy codensar oF
> veock u
> courte
> es bn eonmenl Setus
> we Userul hates
> wr Spe Seetenent
> M44 Structured inter mato
> 4 Cynamcaity gerera
> wr Adaoles Euargie
> ato tanetead + 67 8 Creer Pyrrrwrs Rarer Amp tap S|

![[assets/slides/-cKUW6n8hBU/slide-022.jpg]]

OCR text:

> a ae I a
> ee : i : . g 1] é 7 Bp tf Dace
> HB. © osaworninco erro u | _—— nn WS eB nimi
> OseT_woRKsaOr Boe Tfusettond def toad duteref
> we Sotenv_geth: StrPath | Hone = Hone, . ve
> av + Goes stream: TO[st+) | Mone © Mone, en
> Orth verbote: Loci « Falee, ALDDED unsupported reflection of eupression-bared inde
> owt
> aa neath @eerrige: bos. © Falve,
> whdee Orareie obs lnterpolete: tc: © True, HhIpoed wisupported reflection of eapresslon-based inde
> mscules reste encodieg: str | Mone © “utt-o"
> 1 hes @O los fb we saci
> . ‘ ke fer
> © Besa yOatector py Parse a ene Se ated ten Oa3 a) the rarabies found as Oreo creme viraties
> © DocymentClasuter py Peareies
> @ CrcumentOiccensse ry Solera path AbTONEE OF relat we BETIS CNT Ie
> © Somer oy i! Abeam Tet staan ch as 10 SteinghO pack ew citer! need 4
> @ vaca dna ter Dy ? inners, math + tne
> 3 Load _doteny (overt idesTrue)
> @ vue titions py
> ar Oo ttor
> © marey iw true
> O re #
> corerampe
> @ otignore 1 amport c+
> ython-veesen & 2 MERIC © ;
> 5 twodel": os. getene: “OSPY_FAST MOOEL* ,
> hs .M FAST
> @ ds0y_workshop clea a *epbheyt: os geteny OSPY_APL_REY |,
> @ arey_aurhsrop pynd v 5 apt base": os. getene “OSPY_ENMOPOINT™.,
> Bw ord v © Taph_version™: ci.getere “OSPY_FAST_APIL_VIRSION |,
> © UCENSE : eee eke ee ek nen ee tana OFEP Caw tewtee fn eee
> Futile Deal aca Ccescen  Veemanal Bits Geena conete ye tenet # a 7
> © pyoroyeet toe o @ > a z : :
> » README mat {noes mene nerasts (D6 /dfendute eramgte] 116: F945) WV: oer] (Ginnie =]
> @ vecursre sutmana M
> © tone entry egdomrer §
> deck v
> ouree
> Mas Eny ronment Setup
> we Lvetul hotets
> #8 sepe Sentment
> 4 Structured intce mata
> Me Dynancai’s gerers
> an Adaciler Evarcie
> err oes) me Se) eens Erraes Carr a ed

![[assets/slides/-cKUW6n8hBU/slide-023.jpg]]

OCR text:

> i ee a iT” S @@ SUID OE, OO cc oc —
> o° F . 7 9 “ a ” Bp , a Ooacs
> @ dspy_workshop.ipynd US. @ depy workshop. clean ipynd 4 BTR ern og ET ration Ipynb M @ Summarizer py an |
> 
> — bad a vo
> @osncy oeehon Sear tye wa ttt hoe at late gE a Abe eee a ost ltored cathe!
> + Code + Markdown C2 Interrupt © Restart ~ Crear AlOutputs ¢. GoTo | | Jupyter Vanables Cutene dy very (Python 31113)
> 5 2 from attachtentssdspy import Attachoznts Rote Mt a
> i Loo ett
> 4 pdt_tink = “https://d28rn@p2Snwr6d. ctoudfront .net/CIK-O00 10458 10/8b76daec-a85f-429a-968c-3c 3eSddaedfc.pdf~
> 5
> 6 doe = Attactrents(pdt_ link?
> 1. O98 Python
> [Attachsents} Running primary processor ‘pdfé_to_Ute’ for Attys: //dl8enOp2>nwr6d.c loudt ont. net/C 2K O08 10858 18/ Sb fedacc- a8Sf-4290-9b8< -3c3c9ebacd tc. oct
> [Attachments] «Applying step ‘load.url_to_response’ to MUtosi//G1Bredo2sewr bd. clovdfront ret /CIm- 20010558107 Bo 74caec- 985! -429a-968c- Ich Gdove3 ec. pd’
> [Attachments! Applying step ‘eodify.morpn_to_detected_type’ to nites: //alSra@nZ5w Od. chcwa treat. ret/C1X OOVIOSSE1O/SE7bdaec BAST 4290 HRC ICH AddaCII<. pet
> [attachments] Applying step ‘load. pdf_to_pdfpluaber’ to Ntips://dlérnQa2s wr. cloudfrant ret /CIn- 080 10458i0/ £97 Gdae - 985 1-4299-968c-Fe3cSdbaed tcc!
> [Attachwents} Applying step ‘moaify.pages’ to Mitoss//O1 8 ndp2srw Gd. Cloust rant. met (CIM OV@lOIS810/Bb 2édacc 985° 4295 968C Ic3cPuvaCzTc.cdr
> [Attachments} Running AdditivePipeline(present.aarkdown + present.images + present. metadata
> [Attacheents} ADDlyINg addITive step ‘"present.markdown® tO MTHS: //O1ErMMu25 rw GI. Cus rOPL Mer/CIM ORO1O4S910/ BU 7EsaeC- 9851 4299 968C- 3c3c9dbAT] Cc. OU"
> {Attachments} Applying additive step "present.images’ to Sttosi//G1BreBolsewréd.cloudfroct. ret sCla-OO1045820/ 8d fedaec- 0894-4290 968 -IcdcIsbocd*c pd”
> bof TAs is what we're workirg with
> 2) from [Pythcr.dispiay import Image, display
> 3
> 4 displaylisage urtedoc. inages[0)))
> Python
> 1 # from https: //manimerivest githud. Lo/attachments/architectures#dspy - integration
> 2
> A wae St avy ONUNOMEG aedlneieeeteam: seewirenens x emnccaienl
> Provems @ Gutrut Debug Consee Terminal Pets Gitlens  suoyter Th tah wmaee ecampe 8 1 Re x
> kay ©
> Re wera ad
> era Sate a core Ae CT es ns a

![[assets/slides/-cKUW6n8hBU/slide-024.jpg]]

OCR text:

> =! Ea a rr Se @® SOR Os cc CT i
> ee f 5 : : Q Ul} = a 2 a ooce
> @ dspy_.workshop.ipynb US @ dspy_worashop, clean ipynd M hub. oy qi i Eee Pres SUMS Eton iyo A @ Summarizer py Ca
> 
> . ° eee z sgn Rey
> ; j
> BD Sety ere Gear yh Ma ot tan ate tr POF an Gyn lay den ecute sete ha Saeed oe tee oe tentitee £m gga at Bane del fed
> += Code + Markdown => Run A! © Restart « Clese Al Outputs | | Jupyter Venables Outline + dy vere {Python 3:11.13)
> . 8 “"TA Ceansection in tne docusent. 7°" ne Be atth
> - s transaction_type: str = Fieldidescription="Fhe type of transaction."} a R
> 6 Shares_sold> int w Fratdtdacerintinns*The nimnar at charac cold *b
> } price per_s (class) str
> 8 ROCBLLDFECE geomet: 1 -> ste stritytes_or buffer, encoamgl, evtars!}) <> str
> 9
> 1@ class Decunents Create are sirng otyect from the green object f encedeg oF errors 1s specified, then the object must espose a data buffer that mt be
> un “HPA struct OeCeded using the Qven encod.ng and erro hand ef Otherw.ce, raturns the fesuit of obyeCe Ste) (4 defined) of reprrabyect) encoding
> 32 form_type:  de‘aulls to sys geidefau tencodrgl! errors defauits to ‘stnct
> 43 filang_date: str Fieid(descriptione*The date of the filing in the format YYYY-MM-00.")
> wa total shares sold: int
> 1S transactions: iist{Trarsaction] © Fieldidescriptione"A list of transactions.”)
> 16
> 1? class Oocurentganalyzecdchoralaspy. Signature):
> 1B “Analyze document content and extract insights. “""
> 19 document: Atiachneats # spy. InputFieldd)
> 28 Gocument_schema: Docuncatschema # dspy.dutputhieltaidesce"A steuctured representation of the dacument content.”)
> aL
> 22) result_schema © dspy.CnsindfTrougnt(Dorvrer taraiyzerscner.s) (documentadoc}
> 23) eprint(vict:4:., 2 5. (result schema. document_schema:)
> a
> 25) 8 Now use the Lyped object to get the total shares sold
> 26 prant{"\n\n # Total shares sold: ")
> 27 print (result_schema.document_schens. total_shares_sold)
> 00s Python
> + ('talang_date’s '2025-99-15°,
> "form_type’: ‘Form 4°,
> Probie: QZ Ovteut Debug Conse’e Terminal Ports Gitlens  tugyter poten omadeeeampe 6 1 Ro x
> Sag)
> Ke ees a
> a eae uC RC CE Cusorfab - Spaces 4 Cer ee nr ee)


## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
