---
title: "Dense Slides: Self-Training Agents: Hermes Agent, HF Traces, Skills, MCP & Finetuning  — Merve Noyan, Hugging Face"
category: "slides"
video_id: "OV56RddyFuU"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Self-Training Agents: Hermes Agent, HF Traces, Skills, MCP & Finetuning  — Merve Noyan, Hugging Face

## Source Video
[Self-Training Agents: Hermes Agent, HF Traces, Skills, MCP & Finetuning  — Merve Noyan, Hugging Face](https://www.youtube.com/watch?v=OV56RddyFuU)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/OV56RddyFuU/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/OV56RddyFuU/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.95`
- Text source: agent_vision.
- OCR decision: ready — Product/UI screenshot with small embedded text and dense interface elements.

Slide text:

> Open-source

![[assets/dense-slides/OV56RddyFuU/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/OV56RddyFuU/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.

Slide text:

> Why does open-source matter?
> Absolute control over models
> Cost reduction in multipliers
> Further customize, shrink models depending on your needs
> Guaranteed privacy for the end-user, enable on-device/in-browser uses, data doesn’t go to another server

![[assets/dense-slides/OV56RddyFuU/slide-003.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/OV56RddyFuU/slide-003.html)
- AI slide classifier: `content_slide` confidence `0.96`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Dense chart with many small labels and score annotations.

Slide text:

> Artificial Analysis Index
> Artificial Analysis Intelligence Index by Open Weights / Proprietary 2 B 28 of 472 modeks
> Artiflclal Analysls Intelligence Indcx v4.0 incorporates 10 evaluatlors: GDpval-AA, rr-Bench Telecom, Terminal- Barch Hard, SclCode, AA-LCR, AA-Omnlsclerca, IFBench, Humanity's Lest Exam, GPQA Dlamond, CritPt + Add modet from specifk provlder
> Proprletary Open Welghts 8080808 A Artlflclw Autytts
> 5.0 49 49 Br

![[assets/dense-slides/OV56RddyFuU/slide-004.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/OV56RddyFuU/slide-004.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: agent_vision.

Slide text:

> Hugging Face Hub
> Home for the open-source machine learning community: share & discover models, datasets, apps, connect with the community and more!

![[assets/dense-slides/OV56RddyFuU/slide-005.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/OV56RddyFuU/slide-005.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Text-heavy slide with code block and multiple model names is best handled by OCR.

Slide text:

> models → agents, serve locally
> Agentic LLMs (thinking + tool calling): gpt-oss, Gemma-4, Minimax M2.7, GLM-5, Nemotron3-Super
> Agentic vision models (thinking + CUA): Qwen3.5
> (Alibaba), Kimi-K2.5
> mlx_ lm.generate --prompt *How tall ts Mt Everest?"
> vllm serve Qwen/Qwen3-8B # then query with QpenAI Completion
> llama-server -n model.gguf --port 8080

![[assets/dense-slides/OV56RddyFuU/slide-006.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/OV56RddyFuU/slide-006.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Leaderboard table and model scores are dense and OCR-suitable.

Slide text:

> compare open models
> Datasets: @ScaleAl/SWE-bench_Pro like: 78 Follow @ ScaleA: 284
> Benchmark Modalities: θ Text Formats: + parquet Size:<1K Libraries: & Datasets pandas. Polars. +1
> t Dataset card: 田 Data Studio Flles and versions 1 K xot: O Community 0
> . Leaderboard ioficisl Benchmrk ① Leam more Epedmentsl
> Taslc SWE Bench Pro
> HODEL SCORE
> Φ Oza1-org/GLH-5.1:0 58.4
> 2 HiniMaxAI/niniMax-H2.5 T 55.4
> 3. Q coonshotai/KimI-K2.S n' 50.7
> 4 s Quen/Qnen3-Coder-Hext n: source 44.3
> 5 1 Qon/Qwan3-Coder-4888-A35B-Instruct n! tource 38.7
> V Show all 14 modcls

![[assets/dense-slides/OV56RddyFuU/slide-007.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/OV56RddyFuU/slide-007.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.
- OCR decision: ready — Dense comparison table with small text and metrics; OCR is more suitable than manual transcription.

Slide text:

> compare providers across models

![[assets/dense-slides/OV56RddyFuU/slide-008.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/OV56RddyFuU/slide-008.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: agent_vision.

Slide text:

> The Hub meets your agent
> MCP Server
> plug Hub in to your favorite LLM
> HF CLI
> search models, manage datasets & buckets, launch Spaces, run jobs.
> Skills
> empower your agent with Skills of HF ecosystem
> Local Agents
> Run full coding agents with llama.cpp, Pi & more

![[assets/dense-slides/OV56RddyFuU/slide-010.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/OV56RddyFuU/slide-010.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast`.
- OCR decision: ready — Code and configuration content is small and better suited to OCR than direct transcription.

Slide text:

> Local coding agents Pi consumes llama.cpp Ilama-agent: agent loop baked into llama.cpp as binary 000 #add your local model $npm install -g @mariozechner/pi-coding-agent "providers":{ "llama-cpp":{ "baseUrl":"http://localhost:8080/v1", install pi configure
> /build/bin/llama-agent -hf [HUB_ID] "models":[ "apikey":"none", "api":"openai-completions”,
> (agent) pi API llama.cpp (server) "id":"Qwen3.5-122B-A10B-GGUF"
> I your files, terminal, etc.
> $pi #start pi start coding

![[assets/dense-slides/OV56RddyFuU/slide-011.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/OV56RddyFuU/slide-011.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast`.
- OCR decision: ready — Dense mixed text and code block are OCR-suitable.

Slide text:

> Local self-improving agents
> Hermes Agent
> self-improvement is baked in: the approach as a reusable across sessions after the task, the agent saves 'skill" and persists memory hermes chat --provider hf #use with inference providers HF_TOKEN=hf_... #usewith local served endpoint hermes config Set OPENAI BASE URL http://localhost:8080/v1 (llama.cpp & friends)
> Providers or serve LM locally Integrated with Inference hermes config set OPENAI API KEY dummy name hermes config set LLM_MoDEL your-model-
> #start chatting
> hermes chat

![[assets/dense-slides/OV56RddyFuU/slide-012.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/OV56RddyFuU/slide-012.html)
- AI slide classifier: `content_slide` confidence `0.95`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Product UI screenshot contains dense small text; OCR is appropriate.

Slide text:

> New! Hub hosts your agent traces
> oher Talu Uonres Untute Uamsts: Datasets 21 a Fker by rume Ful-tet search,:, 1l Sort: Trendng
> Hodalles 08 Audo: Documnt t + n6ttT - Lt9 a + or yrp eptpdn: el #: m badlogicganos/pi-aono + 0xSoro/pi-sossions +in· LpLta3dyxo· b%·±17. 5
> D Geosptiul 9 Tet Tmeseries. a voto + Tnct· Updattdadp ato. a7- ±5a. 04 m badlogicganos/pi-diff-review jediscti/agent-traces-smival + Trca: Updaed about ghour ao · D T · A ll: 01
> Sue(rour) 0 lhoestq/ag+nt-trac+s-+xaaple + Yaces: Updrid&day. sgo. D4· ±loe· 1 virhnx9e/vtcade-sassion± t o · rst + - alr tnou re noqr ptirpdn
> Fo.k: + Trce · Updsttd sbout 1 boar sgo - a 1i · ± 1o · 1 noikapy/fxKobolds 食 tnoe- Updrted 6 dys ago: u 12· 主H cfahlgreni/egent-sessicns-list
> Boe! = ov + prqut optimired parquet:. Bb tragetolder + Tnkes · Updned J dsy ago · D&· L39 mcfahlgron1/pi-diff-review + Tncgs + Updsted 1 day ago: a 15 + ±44 LaisEckart/appioraltostt-lava-sessions
> 》MTOH B soundfoldr: ■tit + Trces + Updated 1dsys hro - ct 42? + t(o1 m cfahlgrenl/pi-nono-fresh + Tract4 - Updsted 1 days sgo - B 1 - ± 3s M dongxx11e4/Basoline_featboach
> Type Benchmark 1( ( Irxes x:± Trces·Updsted2 dnysato·02·上32 I davanstrien/pi-tracos M davanstrien/pi-traco-parsor-stssions ± Trx++Updt*d2dyt +go: aI+ ±2?

![[assets/dense-slides/OV56RddyFuU/slide-013.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/OV56RddyFuU/slide-013.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.

Slide text:

> Just upload your sessions from:
> ~/.claude/projects
> ~/.codex/sessions
> ~/.pi/agent/sessions
> 
> Nothing else needed!

![[assets/dense-slides/OV56RddyFuU/slide-014.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/OV56RddyFuU/slide-014.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — product UI screenshot with many small labels and model rows

Slide text:

> tip: find models supported by local apps
> Hsin Isks Litrarirs Urpuges Lloemit (ther 0 Models 474 Tul et verch. y oun+ '+1 Sort, Trending.
> Liu.coo G L Sudoe LnM ow Thinp O Hayr lop t9c 0 - ht1 F: otr kp t pvrpdn · 9st r + ju1-orl+lrul unsloth/geana-4-268-A48-it-GGuf D unsloth/gema-4-318-1t-GGUF P muItrl·to-Tit + d 1la - Updted sbout 18 hout ato · ± Ael. C H1
> YSGLngQ Ualoh oiluionl+ Jbyfuion rUM om 口 xLxL t Dodar Hode tuaitar t Lemortde unsloth/gcana-4-E4B-it-GGUF D unsloth/goea-4-E2B-1t-GGUF B hugrTea-to-Yeat · d Se · Updstrd sbout 2l houn aro - ± y!lh. g1
> tertmce Prerlders Select alt α unsloth/GLH-5.1-GGUF T Tta Gmrmtion - Tb. Updsted I dsy ao · a i1.y - O t unsloth/Q=en3.S-358-A3n-GGUF F tratrTento-Tent · 4 Jso - Updrted Hes· ±L4cy. O Ta
> Croa Noic Cerebrns ○ ulX Hyperbolch TocetherA hmagt-Ten to-fer · d 2re · Updeted Ma 5· ±12k. O <s α untloth/Q=on3.S-27B-GGUF 0 uns1oth/Q=on3.5-98-GGUf B hmageler.to-Tet · s 9s - Updatrd Hst? · t l.1M. O 41?
> t Osicloud A Endpoinau hF hitence AliD wrSped R Coher Fhtworis fetharlessA Q Zl D Rrpiratt Q Salcway d G d unsloth/Qaen3-Coder-Haxt-GGUF TetGanenAion · sce· Updxted Mr6· t 25sk · 556 Tet Goneraton - d 31B: Updned Jn 30 · t 13ek · 583 Q unsloth/Q=on3-Code1-30B-A3B-Inatrutt-GGUF
> MiK unsloth/Qnon3.5-4B-GGUF kmwg+teat-to-Tor - 4B. Updstrd Har 2 - ± 5tdk - 19$ H hmaglanto-Tra · d 12ze · Updxrd r s -. 38yt. O 10 unsloth/Quon3.5-1228-A1e8-GGUF
> hf.co/models → other → apps

![[assets/dense-slides/OV56RddyFuU/slide-015.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/OV56RddyFuU/slide-015.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — dense product screenshot with model card, code, and compatibility details

Slide text:

> ggml-org/gemma-4-26B-A4B-it-GGUF uke 40 Folow ceml-org 168k
> B GGUF: converatlonal
> V Modelcard Ie Files and versions i& mt Community I:: Deploy * eUse this model]
> Edit model card
> gemma-4-26B-A4B-it-GGUF 67,075 Downlosds Iast monh
> Recommended way to run this model:1lana-scrvor -hf ggal-org/gcnma-4-26B-A4B-it-GGUF GGUF ① Model size 25B params Architecture: gemma4 () Chat template
> Then, access http://ocalhost:8080 Hardware compatibility P L4 (24 GB) x1:
> 4-bit Q4_K_M:16.8 GB
> 8-bit α Q8_0 126.9 G8:
> 16-bit β F16 150.5 GB

![[assets/dense-slides/OV56RddyFuU/slide-016.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/OV56RddyFuU/slide-016.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — slide contains code snippets and multi-column text

Slide text:

> lets any coding agent HF CLI Skill # Add CLI skill globally hf skills add --claude --global
> search models, manage datasets, # 0r per-project hf skills add --claude
> run jobs (and more!) launch Spaces # Works with other agents too hf skills add --codex hf skills add hf skills add --opencode --cursor

![[assets/dense-slides/OV56RddyFuU/slide-019.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/OV56RddyFuU/slide-019.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: none.
- OCR decision: ready — Dense small chat screenshot, code block, and multi-column annotations.
![[assets/dense-slides/OV56RddyFuU/slide-020.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/OV56RddyFuU/slide-020.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Dense pricing calculations and screenshot text in small type.

Slide text:

> Grest Do you hive sn ides of the costs foc runaing 16 GpUs in parstei tor thst long? Use @ Hugglng Face Jobt:
> nq Uslng the latest rerifed HF Jobs pricing frorn our erlronmant, l4tsxl ks s1.8e/hour pe GPU. So 16x I4esx1 3 previous mosssges ) → LLM even does napkin calculates running cost for math for the instance and
> Aep/169s noqy · +. $2s.te/hour tots the Job
> Lyn yyap-its sinou oeioz hoqt ey pmoyt uru tded- ras'iz mm, out 'ehtd yyewlpuea sotl ueuro eu betn + -29.3h case: about s843 + 3+.th cso: sbout $565 16 jobs in paralle, to the rw GpU cost is about: ran you can use Buckets → these Jobs will be re-
> For compsrson, 16x sieg-large: b ch+aotr par hour but slomt ottral: rd budget a bit abore rw compute ior shurd skew, slrtup overhead, retrles, trd possble Hub hlceupt + Practicel budgtl sbout s9eo-si,054 fast read-write with hf-mount that allows
> + $ltg-1srge.: s1.s0/bour. osch, so $24/bour. for 16
> + Estimated wall-clock: about 56.4 hours. + Total: sbout s1,353
> Tthuo aodtoy> Aryoirw pue ostu, 4oq dq proyt 1' txhm xgt tsn:outt cn cirt uoepuauuoou Au os

### Hidden Non-Slide Evidence
- [`slide-009.jpg`](/assets/dense-slides/OV56RddyFuU/slide-009.jpg) — `speaker_stage` confidence `0.96`; Camera shot of speaker on stage with the slide only partially visible behind.
- [`slide-017.jpg`](/assets/dense-slides/OV56RddyFuU/slide-017.jpg) — `speaker_stage` confidence `0.98`; speaker on stage with partial slide and sponsor logos
- [`slide-018.jpg`](/assets/dense-slides/OV56RddyFuU/slide-018.jpg) — `speaker_stage` confidence `0.98`; speaker on stage with partial slide and sponsor logos

Classification audit: `raw/sources/slide-ai-classification/dense/OV56RddyFuU/audit.json`
