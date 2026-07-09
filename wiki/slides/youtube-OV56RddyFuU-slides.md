---
title: "Slides: Self-Training Agents: Hermes Agent, HF Traces, Skills, MCP & Finetuning  — Merve Noyan, Hugging Face"
category: "slides"
video_id: "OV56RddyFuU"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: Self-Training Agents: Hermes Agent, HF Traces, Skills, MCP & Finetuning  — Merve Noyan, Hugging Face

## Source Video
[Self-Training Agents: Hermes Agent, HF Traces, Skills, MCP & Finetuning  — Merve Noyan, Hugging Face](https://www.youtube.com/watch?v=OV56RddyFuU)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/OV56RddyFuU/slide-001.jpg]]

OCR text:

> PLATINUMSPONSORS
> $ Braintrust
> Workos
> OpenAl

![[assets/slides/OV56RddyFuU/slide-002.jpg]]

OCR text:

> 8Bra
> ust
> ATr
> Open/source
> AlEngineer
> EUROPE

![[assets/slides/OV56RddyFuU/slide-003.jpg]]

OCR text:

> Oper -SOUurce
> ~ ‘+ DeepSeek-V3.1-Terminus “ tee W peephnen
> Tet Geeenon  & Teanskemery  @ Astetenuny — deetieek v) Coneerttioral — cantom code @ tent generation nirrenie » . .
> m License: mit
> « Model card Faes vad verpors «ast ' Community @®
> Uae nade cae
> DeepSeek-V3.1-Terminus 12,070
> ay deepseek © sme
> Mn GABE pare te tre BELG FR EAM FE
> » Inference Providers =~ @ Brom
> Carers —~—--
> a : .
> introduction
> Ths update ma-ntans the mode: Songmal Capad tees while adaresung sues
> feported by users ining”
> Canmiitee caneutanre Det cine act enred al avad Phineta Enntieh tare ead !

![[assets/slides/OV56RddyFuU/slide-004.jpg]]

OCR text:

> we — Ss... ne
> Artificial Analysis Index
> Artificial Analysis Intelligence Index by Open Weights / Proprietary OO  — 2Bot 472 mosels é B
> Artic! Anal tes intel gence loser V4 Oincorperates WO evatcatiens GURL AA Benct felescoe, Terennal ew Aad ede. tree cee the bhek dee
> Bereb Hard, SaCecte, AA LOR, ASCOmrscece, Hersh dumarety's Last Gram, GRQA Damens, Critht “oe oe ees
> @Propnetary M@ Open Weights
> ; ; Ay Arteficial Analysis
> S$ 89 A NO mM a ~- 8 0 °®@® @ Ss fe ¥ G&G & yY™ GF @ A aw. ° a
> a a Oe a a an ia - a cot id a a a CG a oF a a an a o a a C a g
> & v > * ~ > Lo 8 2, r 2 © © = Ss € 3 » @. ©
> xe os > oO. eo NY ¢ so 5 Se Sw SF wo Soa den rhe CF SF SY © £
> ogé 8é 4 fe 2 os $ gs s & é fe # # > f° Siséfsck SS F £3 S PF F $
> ‘ a ex fe 2 fe ° ° 7 oo ¥ yee ¢ e 3 G é re edge s & 2 f a ,
> € é ¢ § ¥ ¢ f f # ESE" g g§ © #?
> ce d

![[assets/slides/OV56RddyFuU/slide-005.jpg]]

OCR text:

> Home for the open-source machine learning community: share & discover models,
> datasets, apps, connect with the community and more!
> S. Hugging Face + Models Oetasets Speces Community Docs Pricing ea
> New T Following = @ New Post + Trending
> GB re ee te mtn corny Ron BD ve aes ees
> move Nee vay
> & Profie @ econshotai/Kiai-K2-Iastruct
> + Ino [FLA hts updated a Space .
> + Sathegs
> Onn einai paueartac $s Mute ingt aceT®/SmolLA3-J8 .
> Notebooks explorers
> = SODA
> — iyieeiilnoes ek @ wep upsned a douse » blach- forest: 1abs/FLUX. 1-Kontent-dev
> # Temelotes Weyaxi /huggingface-leadertoard
> com Pesrctstod Ute trae cacy oy ————._ SO - =

![[assets/slides/OV56RddyFuU/slide-006.jpg]]

OCR text:

> zp ~ / | 4
> qp Tates ota Cats lees ten Models . « igh 5 Cull Leet seaech > inference Avadabhe 15 Sort Trending
> uate
> i w¥ Qwen/Qwen3.5-358-A3B
> ae
> 2 ~~ Text Generation Any (Oo Any
> + Image Textto Text *. Image to Text ¥ Qwen/Qwen3. 5-278
> Image to tmage + Text to Image ,
> + Text to Veo Tea to Speech 44 ¥ Qwen/Qwen3.5-3978-A276
> Farpretery
> | <u oad ae nn sr $008 ¥ Qwen/Qwen3.5-1228-A10B
> i t
> Tpeares
> | @ unsloth/Qwen3 . 5-358-A3B-GGUF
> © Pylorch —-F TenseSlow af JAK i ‘
> | + Teanslormers 7 Ditksers
> zai-org/GLM-5
> at sentence-tranviormers —-& Safetenson . . .
> 4 OSNE  @GGUF aw Tranvormens
> \
> \ \

![[assets/slides/OV56RddyFuU/slide-007.jpg]]

OCR text:

> models — agents, serve locally
> | Agentic LLMs (thinking + tool calling): gpt-oss, Gemma-4,
> Minimax M2.7, GLM-5, Nemotron3-Super
> Agentic vision models (thinking + CUA): Qwen3.5
> (Alibaba), Kimi-K2.5
> ene i -oyiae
> wim serve Oven sQwens 6B a ee ; 1s Lo
> Lamas Geryes ord (em OTC Ten 8060

![[assets/slides/OV56RddyFuU/slide-008.jpg]]

OCR text:

> The Hub meets your agent
> MCP Server HF CLI [She
> . search models, manage
> plug Hub in to your datasets & buckets,
> favorite LLM .
> launch Spaces, run jobs. .
> » - ~ ae N
> Skills Local Agents eS
> empower your agent Run full coding agents
> with Skills of HF with llama.cpp, Pi &
> ecosystem more

![[assets/slides/OV56RddyFuU/slide-009.jpg]]

OCR text:

> |) ace -instatt pi
> Local coding agents | anetae ee
> S opr vistall -g @rarvoasechner/pr-cadiag-agent
> e Pi consumes llama.cpp Ce cee ee
> configure
> ¢ llama-agent: agent loop baked meogtteres t -
> into llama.cpp as bina Tenseene's
> ° Ppp ry baseUri’r https locathast: 6080/41,
> apd Coperar completions’,
> awoikey d none’,
> ‘foutid/bin/Tioma-agent “if [iii_201, aan
> adv: Gwen3.$ L22B- AICB. GGUE
> API }
> pi —»> llama.cpp }
> (agent) | «— (server) }
> }
> v your files, terminal, etc. | ,

![[assets/slides/OV56RddyFuU/slide-010.jpg]]

OCR text:

> Local self-improving agents
> Hermes Agent COC
> e self-improvement is baked in: # use with inference providers
> HF TOKEN&ht ...
> after the task, the agent saves hermes, chad e=provider bf
> the approach asa reusable # use with local served endpoint
> "skill" and persists memory (Ulama.cpp & friends)
> hermes config set OPENAIT BASE URL
> across sessions httpi//locathost :8080/y1
> . hermes config set OPENAT API KEY dutmy
> ° Integrated with Inference hernes contig set LUM MODEL your-model-
> Providers or serve LM locally name
> # start chatting
> hermes chat

![[assets/slides/OV56RddyFuU/slide-011.jpg]]

OCR text:

> HermesAgent ·(or)directlysetupfromsetup Starting setup wizard..
> wizard，it'sabreeze
> recommended:GLM-5.1, rumoredMiniMaxmodel Gemma-426B,upcoming Wming:Noiference provider configured,Runheres odelto chooseaprovide +Inference Provider Current nodel: Active provider: nooe anthropic/claude-opus-4.6
> API key saved.
> merve @Zeki ping Justnow tse uRttps://router.hggingface.co/v1]1 Defaltmodelset to:zal-org/Gu-5.1(viamugging Face) Found 19 nodel(s) froe sodels.dev registry
> ZekiApp Justnow
> Pong! 0910 1640. dk11y.(4c00)
> What'stheAl2releaseyou'rereferringto? I'dlove tocheckitout!
> AlEngineer Google DeepMind
> EUROPE

![[assets/slides/OV56RddyFuU/slide-012.jpg]]

OCR text:

> PRY zk ;
> Hermes Agent
> <4 directly setup from setu
> — aT * (or) y setup p
> iz *« lel wizard, it's a breeze
> ° recommended: GLV-5.1,
> ATrig ZZ Gemma-4 26B, upcoming
> rumored MiniMax model
> aa . eee an aS
> ty - c
> ae om
> ~ yi > ae
> 2
> eaten
> [aehaess

![[assets/slides/OV56RddyFuU/slide-013.jpg]]

OCR text:

> yo —_——— ~y
> i :
> 29 Hub hosts your agent traces
> GID i cr a teers Ontasets . Fubtet search =) Sort: Trending
> . badlogicgames/pi-mono OxSero/pi-sessions
> Mevtat tes . .
> O32 Basco B downent
> © Geospstal «@ enage | @ Tabula badlogicganes/pi-diff-review jedisct1/agent-traces-swival
> ° .
> Bitet BD teneseres video
> lhoestq/agent-traces-example vinhnx9G/vtcode-sessions
> Sire teas
> * 3
> <a a
> —__...._____._._._..___________¢
> soikapy/OxKobolds cfahlgreni/agent-sessions-list
> * - 5
> feweat
> th ysor 8 Gav & pared cfahlgrenl/pi-diff-review LarsEckart /approvaltests- java-sessions
> - optemued parquet -nagefokter ° =:
> B wonttcicer = & webdaraet teat
> Cfahlgreni/pi-mono- fresh dongxx2164/Baseline_featbeach
> > row
> ° : .
> ise davanstrien/pi-traces davanstrien/pi-trace-parser-sessions
> Benchmark“ @ Traces» ° °
> ate
> -
> Me “he == ~7

![[assets/slides/OV56RddyFuU/slide-014.jpg]]

OCR text:

> A Session
> B User P8281 ieTl3 Mt ne Bae
> alright, time for a new release. i want you to:
> check if all third party contributions since the last release have changelog entries (!" badlogic - = me)
> Just upload your sessions check if CHANGELOG. md entries of packages != coding-agent but that affect coding-agent are also in
> f 3, the CHANGELOG. md of the cod:ing-agent
> rom. tell me if we are good to release
> ~ ; B Astistant anthrcgic clasdeopys 295 026 TE LATAD AE LE Ca It, Beet
> e “/.claude/projects Pasar ewe
> e /.codex/sessions Theniinp The uses warts fa prepare fora crew cedenase iseedio fo bird the hast re ease fag errs.co? Chrca econ
> e “/.pi/agent/sessions 2too:<awinaen
> pba Cccewaret ced cters badiigiceannecca.es fh GN Ba gat deainibe stage ccabire. 2 GE
> . eu dat
> Nothing else needed!
> 2 DRA ema ted bers Gadi egac aetecsaous cs Tone be Gat bod Seat Cersribe otegs caterer A
> @ aad te. Satis fectoer fest ta. Satdmare curver yeustiocacg fur IMi wopeert eotasigd war. feo e
> m Assistant anterepic clade opus 4-95 2126 1 IATOS RR DT dtet oe Tet ALIS La hee
> Theniang Gone, the lest retrace wos 2460 Naw etme dear y turd party conte a, hans int fen Mgrs Jechor :
> Third-party contributors since v0.46.0:
> \ ‘

![[assets/slides/OV56RddyFuU/slide-015.jpg]]

OCR text:

> . of:
> | tip: find models supported by local apps
> & s.
> Mav Se Lares be pnge son GERD Models 3° unsioeh Full-tent search + Wherence Avelable —*. Sort: Trenaing
> ness © Reet toes € unsloth/geama-4-268-A4B- it -GGUF @ unsloth/geema-4-31B- it -G6UF
> lL oMersepe = Uv Stadio jor BB Osa thiegs
> BD Otivcster  & Joyfuvcr ot IM Oem
> @ unsloth/gemna-4-E4B-it-GOUF @ unsloth/geema-4-E2B-it-GOUF
> CMLL & Docier Model Runner . Lemonade . 2
> Ylang Q@eawn A Re
> I 1B unsloth/GLM-5.1-GGuF @ unsloth/Qwen3 _$-358-A3B-GGUF
> fetene Mendes Select alt . . . . ‘ .
> ou Bvowte 8 Corede: Serban
> “ ™ senna magni @ unsloth/Qmen3, 5-278-GGUF © unsloth/Qnen3.5-98-GGUF
> fhe OO ht MM Hypecbolic Together AL i * .
> @ fireworks MB feathertossAr ER fm hy Pepticate
> R Cohee #3 Sealenay Publ At B unsloth/Qwen3-Coder -Next -GGUF @ unsloth/Qnen3 -Coder - 308-AIB- Instruct -GGUF
> \ : :
> Od A Padponts © HE lafetece APL WaneSpeed
> @ unsloth/Qmuen3.5-48-GGUF @ unsloth/Quen3 .§- 1228 -A198-GGUF
> ve ‘ “ : : .
> a ”
> ae ane hail afi i = A oe ea ae SS sas ttn :
> hf:co/models'—> other > apps

![[assets/slides/OV56RddyFuU/slide-016.jpg]]

OCR text:

> | eyoste: gemma-4-26B-A4B-it-GGUF brs fo on magmiog '
> @ GGUF conversational
> « Model card Files and versions “net + Community 1 Deploy - Gz
> 2? Edit model card
> gemma-4-26B-A4B-it-GGUF “«<—o /\
> Recommended way to run this model: ?
> “mo Modetsize 25Bparams Architecture gemma4
> @ GGUF
> llama-sorver -ht ggnl-org/gemma-4-26B-A4B- it -GGUF } Chat template
> Thensaccess fis ® Hardware compatibility L4(24GB)x1 we
> 4-bit GB Q4KM vend
> 8-bit O80 feces
> 16-bit Gre. 0:

![[assets/slides/OV56RddyFuU/slide-017.jpg]]

OCR text:

> oi .
> Howtouse from Pi Pi x
> » Start the llama.cpp server
> . Copy
> brew install llama.cop
> . cos : "Copy
> llama-server -bf ggml-org/gemma-4-268-A4B-2t-GGUF: Q4_K_M  -  --jinja
> » Configure the model in Pi
> » Run Pi
> Quick Links
> Read the Pi documentation

![[assets/slides/OV56RddyFuU/slide-018.jpg]]

OCR text:

> HF CLI Skill # Add CLI skill globally
> hf skills add --claude --global
> lets any coding agent
> e search models, # Or per-project
> hf skills add --claude
> * manage datasets,
> e launch Spaces # Works with other agents too
> e run jobs (and more!) hf skills add --codex
> hf skills add --cursor
> hf skills add --opencode

![[assets/slides/OV56RddyFuU/slide-019.jpg]]

OCR text:

> le | ———_—————— eo i.
> . «OS We have a ton of skills, here’s some Claude
> of the coolest: # register’ the skitts‘aarketptace’
> 7 ¢ lim-trainer: vibe-training with eenanae
> | TRL, PEFT, Jobs | pe ce may. esac
> if aad * community-evals: run evals je pomingeesons cue
> .: ¢ gradio: build demos trainerahuggingface/skilis =
> } al ¢ huggingface-datasets: Gemini
> — ize explore datasets in-depth youini-ertenei extensions: instatt "
> https://gtehib.cou/hupgingrace/sk,
> AUsigit consent;
> ty i &
> Zo $3 Braintrust €} WorkOS OpenAl

![[assets/slides/OV56RddyFuU/slide-020.jpg]]

OCR text:

> om aa mit |
> n | We have a ton of skills, here’s some | Claude
> iw of the coolest: ft regis agister the -Ski1US marketplace.
> Seabed tS ¢ Ilm-trainer: vibe-training with | f epee taal
> TRL, PEFT, Jobs cee esa ct ug tense,
> AWS , * community-evals: run evals I etugia tenet beeetngtecesttae:
> : * gradio: build demos trpiner@huggingface/skills a
> ¢ huggingface-datasets: Gemini
> \ explore datasets in-depth gevind extensions install =
> 5 Atsigit<consery
> s Loa
> Ho A, t's
> Ce Engineering the future of Al

![[assets/slides/OV56RddyFuU/slide-021.jpg]]

OCR text:

> Fr | AL. : . i€ )
> aa ae | Skills in action beer we
> cau re . lavas ins raer nih” | rat
> — Agent will ask some questions ne
> brig | about infra/local hardware etc mowed « ¢
> — Agent can retrieve job logs ee
> : |» Find your model on Hub en
> 7 -¥] : a j ee
> / bade . Quend.$°V. IB Inetrect-trl-ape-elait-v :
> oy Modet (ard fos Quen? $ VL JIE inatiett it pe tad o ~se sot \ ne , b. Hie f
> an | aera nee ee |
> Al Engineer
> Aue

![[assets/slides/OV56RddyFuU/slide-022.jpg]]

OCR text:

> . a a Skills in action pone
> ee — | Nlavetnstruct'ritx” | Ae
> zz y a " a 2
> if - — Agent will ask some questions an
> ' aE about infra/local hardware etc re
> — Agent can retrieve job logs wmv
> — Find your model on Hub ce
> ue i
> e
> [_ateeineer_] Google DeepMind

![[assets/slides/OV56RddyFuU/slide-023.jpg]]

OCR text:

> eo 0 ..—W4>4wwwv—q_S——_ “ -_ -
> ® a nn? Su Peed , 7 a 5 EE
> Ski | | . tj Ae Tae
> wo . cere)
> Not limited to LLMs/vision _ cee,
> A 1 hbattan aan ea Sane: ay ge
> LMs, just like Hub
> Classes cn , a | oes
> Fpachs us
> Race ee acre ae
> Inaqe size cet
> cress *
> Tea at
> PRieeT send bg gh HB
> Sten he ran “
> rons bate!
> cera!
> Serra)
> plese
> eC RPC Sets)
> | Pe eke sme ee ere ot ie wee ee c
> Pee ake: es ee | a ee an
> i : Script saved at: i

![[assets/slides/OV56RddyFuU/slide-024.jpg]]

OCR text:

> @Brair st | ir . . La -
> i few ideas with Spaces MCP
> iz i Lt
> y és * |
> aa - M i Generate or Text-to-Speech Parse |
> Edit Images OT TO“OPSLE documents
> = AA
> - be
> Me | ..use any app on Spaces!
> [_atsineer_] Google DeepMind

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
