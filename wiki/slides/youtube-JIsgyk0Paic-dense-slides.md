---
title: "Dense Slides: Reinforcement Learning for Agents - Will Brown, ML Researcher at Morgan Stanley"
category: "slides"
video_id: "JIsgyk0Paic"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Reinforcement Learning for Agents - Will Brown, ML Researcher at Morgan Stanley

## Source Video
[Reinforcement Learning for Agents - Will Brown, ML Researcher at Morgan Stanley](https://www.youtube.com/watch?v=JIsgyk0Paic)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/JIsgyk0Paic/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/JIsgyk0Paic/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Dense two-column slide with small table/diagram text and multiple bullet groups.

Slide text:

> LLM agents in 2025
> "Reasoning" models = the future? Most LLMs are Chatbots o. Helpfut for interactive problem-solving. Great on Q&A benchmarks: Level 1 Stages of Artificial Intelligence' Chatbots, Al with conversational language
> o. o. 01, 03, R1, Grok 3,.. Better at hard Q&A. Level 2. solving Reasoners, human-level problem
> Best practices for "agents" Level3 Agents, systems that can take actions
> Many chained LLM calls per task: Results are... OK? Prompt engineering + tooling Evals, ops, tool-use, human-in-the-loop: Level 5 Level 4: Innovators, Al that can aid In irventlon.. of an organization Organizations, Al that can do the work (OpenAl)

![[assets/dense-slides/JIsgyk0Paic/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/JIsgyk0Paic/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.92`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Main slide is readable but mixed with stage camera footage and branding panels; OCR is better for the small text.

Slide text:

> LLM agents in 2025
> AIE Most LLMs are Chatbots "Reasoning" models = the future? Helpful for interactive problem-soiving Great on Q&A benchmarks Level 1 Intelligonco Stages of Artificial language Chatbots, Al with corrversational
> 。 01, 03, R1, Grok 3,... Better at hard Q&A Level 2 sohving Reasoners, human-level problem
> Best practices for "agents" Level 3 Agents, systems that can take actions
> o Prompt engineering + tooling Evals, ops, tool-use, human-in-the-loop Results are... OK? Many chained LLM calls per task Level5 Levei 4 Innovators, Al that can aid in invention Organizatlons, Al that can do the work of an organization (OpenAl)
> AGENTENGINEERING
> HTtPS:IIAI.ENgINEER

![[assets/dense-slides/JIsgyk0Paic/slide-003.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/JIsgyk0Paic/slide-003.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast`.
- OCR decision: ready — Text-heavy slide with multiple small diagrams and labels that are suitable for OCR.

Slide text:

> How agentic are our agents? LLMCA Ovtput2 LLMCHF
> Oetsot: Cate
> Fai Cxit
> Many agents are pipelines Low degree of autonomy Pipelines
> Winning apps = tight feedback loops (mostly) Non-trivial engineering required LLM CalI Router LLMCAE1 LLMCall2
> O IDEs (Cursor,Windsurf,Replit) LLMCall3
> O Betterathard Q&A
> Not many agents“do stuff"for 10+min
> O Devin,Operator,Deep Research Actioo
> Howdowemakemoreof these? Human LLMCall Environment
> Justwait forbetter models?
> Classical RL = optimize agent policy Stop Feedback Agents
> (Anthropic)

![[assets/dense-slides/JIsgyk0Paic/slide-004.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/JIsgyk0Paic/slide-004.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Dense slide with charts and small annotations; OCR will read the chart labels and bullet text better.

Slide text:

> Lessons from DeepSeek
> 1 month ago: DeepSeek R1 paper + model
> RL on strong base models works
> RL with sparse rewards works
> 01-level performance = easier than expected.
> Long CoT = emergent
> Open-source Iis back (for now))
> Several replication efforts
> Can distill to' smaller models:
> So... what next?:
> : (DeepSeek, 25)

![[assets/dense-slides/JIsgyk0Paic/slide-005.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/JIsgyk0Paic/slide-005.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast`.
- OCR decision: ready — Mixed text-and-diagram slide with small labels and a process diagram that is better handled by OCR.

Slide text:

> How reinforcement learning works
> Key idea: explore and exploit Largo-scnle Roasoning-Oronted Reinforcement Learning
> DeepSeek's GRPO DeepSoek-v3-Base DoepSeek-R1-Zero
> Like PPO but simpler Less compute, same effect Group-RelativePolicy Optimization Tran Hodet checkgodnt undee.crainimg (Ma)a u Rule-basedverication acodeapfhon? ×
> Main loop:
> O Sample N responses per prompt
> Computerewards foreach
> O "Advantage estimates" (Jay Alammar,'25)
> Update rule:better score =increase likelihood
> Challenges: rewards? multi-turn?

![[assets/dense-slides/JIsgyk0Paic/slide-006.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/JIsgyk0Paic/slide-006.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast`.
- OCR decision: ready — Slide has a dense text inset and a chart; OCR is the right first-pass extraction method.

Slide text:

> Lessons from OpenAl Deep Research
> LLM agents can work for long multi-step tasks
> Vibe check = impressive
> Still struggles“out of distribution”
> Big labswill keep making agents
> Don't know full details, but..
> How it works C05
> Deepresearch was trained using end-to-end reinforcement
> domains. Through that training, it learned to plan and execute a learning on hard browsing and reasoning tasks across a range of The more the model browses and thinks about what its browsing. MaxTool Calls
> multi-step trajectory to find the data it needs, backtracking and the better it does, which is why giving it time to think is important.
> reacting to real-time information where necessary. The model is (OpenAl.'25)

![[assets/dense-slides/JIsgyk0Paic/slide-007.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/JIsgyk0Paic/slide-007.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: agent_vision.

Slide text:

> RL infrastructure
> - RL training infra: exists, but mostly "RLHF"-style
> - Want options besides "wait for big lab tuning APIs"
> - How can we plan ahead?
> - Unknowns:
>   - Cost to do RL for agentic tasks?
>   - How small can the models be?
>   - Generalization across tasks?
>   - How to design effective rewards?
> - Opportunities:
>   - Open-source infra for DIY
>   - Services for agentic RL

![[assets/dense-slides/JIsgyk0Paic/slide-008.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/JIsgyk0Paic/slide-008.html)
- AI slide classifier: `demo_video` confidence `0.89`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Dense screenshots, code, and small chart labels.

Slide text:

> grpo_demo.py
> will brown @willccbb Jan 26 Sints scorte ay the oooonent in th ch GRPO self-correction on Lama-18:) Promoto te are elso giytn that the points scored by the ooponent in the changionshlg gase is hslf of UF's nurite? (2)2)0(1/2)(21②02) Sirpllfying tho ecuntlon, Co cet.
> 2 tr (24x
> This laptification ss arong, Tho opponsnt cust have scored & core point!.
> 2 Z psjo?s aaru lin lutuoddo su1 ter4 1 160 150 130 This simplifits to: This tipllties to. So. they stcored 1/6 polnte esch In ttin first 2a get (24x2)0.(1/2)(21( x2/12 （24x2）12x 24x.12x03 12x0.2 9/1x
> 24 484 1167K tain/rewards'xcurxy t!an/compltion_length
> will brown cwillccbb Jan 26 aduss 03 10 1
> 01

![[assets/dense-slides/JIsgyk0Paic/slide-009.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/JIsgyk0Paic/slide-009.html)
- AI slide classifier: `title_card` confidence `0.84`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast`.
- OCR decision: ready — Collage slide with multiple embedded screenshots and small text labels.

Slide text:

> grpo_demo.py
> GRPOself-correctlon onLama-1B:) willbrown@willccbo·Jan26 Promote meare alsogiven that the points cored by the cgpoent In thecharoiohi gae Ishalf of ts nrite: （24x-2）=（1/2）（24x-2·2）
> AIE pintswoeredtythtopooaeatlathtchang tr Sinplifying theequatioo,weget: （24x-2）+（2x-2)
> gett This sinplification was wroog. The opponeat most have scored 2 sore oints.
> This sinplifies to: This sinptities to: So,thoy score 1/6 points ach in their first 26gae. （24x-2）=（1/2）（24x-2·2） x1/6 x2/12 （24×2）12x 12x2 24·222
> chInteipfirst24ges,
> Q24 Et 484 sl67K trainrewaresx(urxy traincompletionjength
> script: willbrown@willccboJan26
> AGENT ENGINEERING
> HTTPS://AI.ENGINEER

![[assets/dense-slides/JIsgyk0Paic/slide-010.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/JIsgyk0Paic/slide-010.html)
- AI slide classifier: `demo_video` confidence `0.92`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Dense multi-panel collage with screenshots, code, and small UI text.

Slide text:

> grpo_demo.py (*st ctme 6 hours +0o willccbb / grpo demo.py
> Hundreds of Billions of Dotsrs Later Teknlum (e/入) 0 F 0Teknlum 1n30 This Is the entkre code needed to reproduce Rs ko! 一 Irokeaso todry the fnst Google Cotb nourbook to tain a reuroning nrw RrrlorceTtrt Ltvning slgorithm trom DepSetk, GRpo. h lte Jo) uru Aiy+ uea nor tpo 6uuea-rod o pue La o uonpol houri you can trrhform I tery srul model, Oron O.s (Soo mlor Hto a tirty muth reusonirg mruchint. To Uhh dale, Iha b probubhy th? oda PiarTe-Csrl Langlais. tu Co'nor Pth Revisons 60 Str3 960 MFoks 313 s-smits/grpo- optuna
> The notedook a based on a tcrigt by Wilm Brorn thst signifcan Cn Llaru 1B csptcitits for math. This i a typical rtirforcerent hs Iprurh bayta os tocLtrduo erriplt ton cie girn cCire! has to find the solution, resrron ovor n for sorme tine (tis is the sbiotle basic Torm ol inetnce time carmacte) tnd rtttding the gooa resronihg dirtr Trsnino I smat meth reasone wth F1 Qwen o Sb on GRPO Reinsorcemant Leunirg rRLi tree vning m poou buuo+res Lu-sse,dneg wao nof Lre1 ed ov Hog poet aha nha M-snarrg Reasoning-GRPO & RL
> GSM8K Reward Functions
> Srmng up iher mocdet
> Ihet pto, Moy
> 2.3M cce3.763 80coTmm:·307ra90t1

![[assets/dense-slides/JIsgyk0Paic/slide-011.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/JIsgyk0Paic/slide-011.html)
- AI slide classifier: `content_slide` confidence `0.96`
- Text source: agent_vision.

Slide text:

> Rubric engineering
> - An accessible way to steer RL algorithms
> - Invites creativity + experimentation
> - Anecdotally, seems to help
> - The next "prompt engineering"?
> - Next steps:
>   - Using LLMs to design rubrics?
>   - Auto-tuning rubrics with DSPy?
>   - Incorporating LLM judges for soft criteria?
>   - Avoiding reward hacking?


Classification audit: `raw/sources/slide-ai-classification/dense/JIsgyk0Paic/audit.json`
