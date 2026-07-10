---
title: "Dense Slides: Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic"
category: "slides"
video_id: "TqC1qOfiVcQ"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic

## Source Video
[Claude Agent SDK (Full Workshop) — Thariq Shihipar, Anthropic](https://www.youtube.com/watch?v=TqC1qOfiVcQ)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/TqC1qOfiVcQ/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/TqC1qOfiVcQ/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast`.
- OCR decision: ready — diagram slide with multiple small labels and box text

Slide text:

> Building effective agents
> 2/ Tools Harness
> your systems - add your custom APis, MC servers,and file Connect Claude to system operations File System Tools Custom MCP
> Models
> Fastest with near-frontier intelligence Claude Haiku Smartest for complex agents/coding Claude Sonnet Exceptional model for deep thought Claude Opus
> ANTHROPIC CONFIDENTIAL

![[assets/dense-slides/TqC1qOfiVcQ/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/TqC1qOfiVcQ/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast`.
- OCR decision: ready — diagram slide with multiple small labels and box text

Slide text:

> Building effective agents
> 5/ File System Harness
> Give Claudea
> just-in-time code, to pass files, write and learnfrom persistentworkspace exampleoutputs File System Tools Custom MCP Prompts Core Agent Workflows Custom File System Process Files ExOutput rrCode
> Models
> Fastest with near-frontier intelligence Claude Haiku Smartest for complex agents/coding Claude Sonnet Exceptional model for deep thought Claude Opus
> ANTHROPIC CONFIDENTIAL

![[assets/dense-slides/TqC1qOfiVcQ/slide-003.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/TqC1qOfiVcQ/slide-003.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast`.
- OCR decision: ready — architecture slide with many small labels and layered boxes

Slide text:

> Building effective agents Your Application
> Claude Agent SDK
> 9/ Application Harness
> Focus on your unique product value - build the user that differentiate your experience and domain workflows File System Tools Custom MCP Prompts SKILLS Core Agent Workflows Custom File System Process Files Ex Output JITCode Auto Compacting Enhancements ResearchMode Web Search Subagents Memory Hooks
> Models
> Fastest withnear-frontier intelligence Claude Haiku Smartest forcomplex agents/coding Claude Sonnet Exceptional model for deep thought Claude Opus
> ANTHROPIC CONFIDENTIAL

![[assets/dense-slides/TqC1qOfiVcQ/slide-004.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/TqC1qOfiVcQ/slide-004.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.

Slide text:

> Why use the Claude Agent SDK?
> - We realized people were using Claude Code for non-coding tasks.
> - We build our agents on top of our Agent SDK.
> - It is built on top of lessons we’ve learned deploying Claude Code to millions of users.
> - We have strong opinions on the best way to build agents.
> - One of our biggest learnings: the Bash tool is the most powerful agent tool.

![[assets/dense-slides/TqC1qOfiVcQ/slide-005.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/TqC1qOfiVcQ/slide-005.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.

Slide text:

> The Agent SDK is the best way to build agents in the “Anthropic Way”
> - Unix Primitives: Every agent should use bash [1] & a file system [2] (e.g. skills & memory)
> - Agents > Workflows: Agents build their own context + decide what to do with tools.
> - Code Generation for non-coding: We use code gen to generate docs, query the web, etc.
> - Every agent has a container.
> More on this here.

![[assets/dense-slides/TqC1qOfiVcQ/slide-006.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/TqC1qOfiVcQ/slide-006.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.

Slide text:

> Bash is all you Need
> Bash is what makes Claude Code so good.
> Bash is a generic version for “code mode” or programmatic tool calling.
> The bash tool allows you to:
> - Store the results of tool calls to files, so you can search them.
> - Store memory in files.
> - Dynamically generate scripts and call them.
> - Compose functionality, use unix primitives like tail, grep, cat, etc.
> - Use existing powerful software like ffmpeg, libreoffice, etc.

![[assets/dense-slides/TqC1qOfiVcQ/slide-007.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/TqC1qOfiVcQ/slide-007.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast`.
- OCR decision: ready — Dense comparative slide with small code and multiple text boxes; OCR is better than manual transcription in this pass.

Slide text:

> Without Bash With Bash
> User: How much did I spend on ride sharing User: How much did I spend on ride sharing
> this week? this week?
> Tool Call (Gmail Query Search) query: "uber OR lyft" "uber OR lyft" Tool Call (Bash)::gmail_search.ts query
> mention Uber and Lyft, I need to find the Thinking:I found the following emails that Tool Call (Bash):
> Claude: The total is... (hallucinated) cost ofeachemail. newer_than:7d"1 gmail_search.ts "from:(uber.com OR lyft.com OR uber OR lyft) subject:(receipt OR trip) grep-0E\$[0-9]+1.[0-9]{2}′1\ awk(sum +=s1} END {printf “Total spenton sed's/\s//'I\
> ride sharing this week: ss.2f\n",sum}

![[assets/dense-slides/TqC1qOfiVcQ/slide-008.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/TqC1qOfiVcQ/slide-008.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.

Slide text:

> Workflows & Agents

![[assets/dense-slides/TqC1qOfiVcQ/slide-009.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/TqC1qOfiVcQ/slide-009.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.

Slide text:

> Tools vs Bash vs Code Generation

![[assets/dense-slides/TqC1qOfiVcQ/slide-010.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/TqC1qOfiVcQ/slide-010.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.

Slide text:

> Why Skills?

![[assets/dense-slides/TqC1qOfiVcQ/slide-011.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/TqC1qOfiVcQ/slide-011.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.

Slide text:

> What are Skills?

![[assets/dense-slides/TqC1qOfiVcQ/slide-012.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/TqC1qOfiVcQ/slide-012.html)
- AI slide classifier: `content_slide` confidence `0.95`
- Text source: agent_vision.

Slide text:

> Gathering Context Take Action

![[assets/dense-slides/TqC1qOfiVcQ/slide-013.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/TqC1qOfiVcQ/slide-013.html)
- AI slide classifier: `content_slide` confidence `0.94`
- Text source: agent_vision.

Slide text:

> Spr
> Gathering Context
> Take Action
> Verify Work

![[assets/dense-slides/TqC1qOfiVcQ/slide-014.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/TqC1qOfiVcQ/slide-014.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: none.
- OCR decision: ready — Spreadsheet UI screenshot with small grid text and sidebar labels.
![[assets/dense-slides/TqC1qOfiVcQ/slide-015.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/TqC1qOfiVcQ/slide-015.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.

Slide text:

> An Example of Designing an Agent
> Let’s make a spreadsheet agent.
> What is the best way for an agent to search a spreadsheet?
> What is the best way to execute a spreadsheet?
> What is the best way to lint a spreadsheet?

![[assets/dense-slides/TqC1qOfiVcQ/slide-016.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/TqC1qOfiVcQ/slide-016.html)
- AI slide classifier: `content_slide` confidence `0.96`
- Text source: agent_vision.

Slide text:

> Spreadsheet Agent
> Take Action
> Verify Work

![[assets/dense-slides/TqC1qOfiVcQ/slide-019.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/TqC1qOfiVcQ/slide-019.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: agent_vision.

Slide text:

> Spreadsheet Agent
> Gathering Context
> Take Action
> search("B3:B5")
> sql queries
> xml
> insert("B3:B5", [[1,3]])
> sql queries
> xml
> check for null pointers
> subagents

![[assets/dense-slides/TqC1qOfiVcQ/slide-020.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/TqC1qOfiVcQ/slide-020.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.

Slide text:

> Claude Agent SDK Loop
> Gather context
> Take action
> Verify work

![[assets/dense-slides/TqC1qOfiVcQ/slide-021.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/TqC1qOfiVcQ/slide-021.html)
- AI slide classifier: `content_slide` confidence `0.95`
- Text source: advanced OCR `rapidocr-live/center-82/opencv-adaptive`.
- OCR decision: ready — Webpage screenshot with mixed-size text and several small labels; OCR is likely more reliable than manual transcription.

Slide text:

> Sttrlrg June tBet a mnw GrphO'L Lpochcion l rellng cut, vibtt2. Reud =ore sl CraehaL v1bata2. Tha Permr v1boLt verslen s vumhting and. cheduted to be rmoved. PEKeAFi
> The RESTful Pokémon APl
> Serving ovcr 10 bllion AP1 calls cach month!
> casily xcessible through a moderm free opensource RESTful APl. O Date analysis tool Al the Poktmon data you'll ever need in one plce.
> Check out the docs!
> Try it now!
> Mtpr/polteploobplt2/pelemordnto
> Netd:hn!Try pohemonditto. poenorpeeVxter npe. abRydxtrwrino,o polurmonlmt-100000ca1e-0
> Dtrect Irk to reut: httpspokepixo/aolvZ/pobrmontt1o
> Resource for ditto
> 31114 AThu1204 THUY ICKEIST ticketmaster BAOOKLTNNIT.COM

![[assets/dense-slides/TqC1qOfiVcQ/slide-022.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/TqC1qOfiVcQ/slide-022.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: none.
- OCR decision: ready — Dense code-editor screenshot with small text and sidebar; OCR is appropriate.
- Slide text: not surfaced (`illegible` by AI classifier).
![[assets/dense-slides/TqC1qOfiVcQ/slide-023.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/TqC1qOfiVcQ/slide-023.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/left-72/contrast`.
- OCR decision: ready — Dense terminal/output screenshot with small monospaced text; OCR is appropriate.

Slide text:

> .cc-prototype xd [TOOL CALL]get_pokemon_species [TOOLINPUN]{ "nane_or_id": "quagsire"
> C data gm/cus [TOOL RESULT] SuCCeSS
> Counoln
> Cr tersts oseyed(） ①RSAOME m （）tcorngon vds gagoe ben Jock WSMOGON_AP1.mN CLAUOEMO 2.Croconaw(Water) 8.Wooper (Water/Ground) Basedon the data,here are all theWater-type Pokemon introduced in Generation 2: 4.Chinchou(Water/Electric) 7.Azurarill (Water/Fairy) 9.Quagsire (Water/Ground) 1.Totodile (Water) 3.Feraligatr (Water) 5.lanturn (Water/Electric) 6.Marill (Water/Fairy)
> tr Pchatts tocbs mO.11 pokomon.1 Note:Marill and Azumarill were originally pure Water-type in Generation 2,but gained the Fairy-type wher eir types. These Pokemon represent the full set of new Water-type Pokemon introduced in Generation 2,including both
> （）ps(kagejon ①README Ime (tscorgnon modeLls chat.ts thariqeThariqs-Virtual-Machinesrc%chat.ts Goodbye! thariqeThariqs-Virtual-Machine srcxls zsh:cormandnot found:chat.ts thariqeThariqs-Virtua!-Machinc Src X bun chat.ts thariqeThariqs-Virtual-Nachine src X thariqeThariqs-Virtual-Nachinesrcx model.ts tools
> 22 atv A

![[assets/dense-slides/TqC1qOfiVcQ/slide-024.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/TqC1qOfiVcQ/slide-024.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Dense terminal/table screenshot with small text and numeric columns; OCR is appropriate.

Slide text:

> pok Bem O tm/nim krgs @-18m ★DaA AUsers/thariq/Profects/poke-coi/cc-prototype/data/gen2ou-17e0.txt-167a- I Other 1.397x /Users/thariq/Projects/poke-opi/cc-prototype/data/gtn2ou-176a.txt-1673- I Nothing 1e0.009x /Ustrs/thariq/projtcts/goke-opi/cc-prototypt/dota/gen2ou-1760.txt-1667- I leech Sttd 47.495x /Users/thariq/Projects/poke-opi/cc-prototype/data/genzou-176a.txt-1668- I Rt!lect 47.493t /Users/thariq/Projects/poke-opi/cc-prototype/data/gtnzou-1760.txt-1663- I Symthtesis 99.334x /Ustrs/tharia/Projects/poke-opi/cc-prototype/data/gen2ou-1760.txt-1664- I Stords Donce 52.505x /Users/tharia/Projccts/poke-opi/cc-prototype/data/gen2ou-176e.txt-166s- I sody Slaa 52.274x /Users/thariq/Projects/poke-opi/cc-prototype/data/genzou-176o.txt-1669- I Razor leaf 47.347x /Ustrs/thariq/Projects/poke-opi/cc-prototype/data/gen2ou-1760.txt-1662- I μoves AUsers/tharia/Profects/poke-opi/cc-prototypc/data/gen2ou-176e.txt-1666- I farthquake 52.155% /Users/thariq/Projects/poke-opi/tc-prototype/data/gen2ou-176o.txt-1671- +-- /Ustrs/thariq/Profects/poke-opi/cc-prototype/data/genzou-17te.txt-1672- I Tera Types
> Ocnarer poh @ REASKEnd (1 prdageo m RADHLNG R rhat 25 + /Users/thariq/Projccts/poke-api/cc-prototype/data/gen2ou-176o.txt-16t7- 4---. /Ustrs/thariq/Projects/poke-cpi/tc-prototype/data/gen2ou-176a.txt-167s- I Iearotes /Ustrs/thariq/Projects/poke-opi/cc-prototype/data/gen2ou-1760.txt-1676- I Snorlax 99.997x /Users/tharia/Projects/poke-opi/cc-prototype/data/gen2ou-176o.txt-1679- I Starnie 66.273x /Users/thariq/Projects/poke-coi/cc-prototype/data/gen2ou-1768.txt-1680- I Raikou 47.359x /Users/thariq/Projects/poke-opi/cc-prototype/data/gen2ou-176e.txt-16t1- I Zopdos 33.65ox AUsers/thariq/Projects/poke-opi/cc-prototype/data/gen2ou-176e.txt-1683- I Quagtire 18.92s% /Users/thariq/Profects/poke-agi/cc-prototype/data/gen2ou-1768.txt-1684- I Htltank 18.926x AUsers/thariq/Profects/poke-opi/cc-prototype/data/aen2ou-1760.txt-16s8- I Checks and Counters AUsers/tharia/Projects/poke-opi/tc-prototype/data/genzou-1768.txt-16s9- ++* /Users/thariq/Profccts/poke-api/cc-prototype/data/gen2ou-176e.txt-1692- /Ustrs/thariq/Projtcts/pokt-opi/cc-prototype/data/gtn2ou-1?60.trt-1696- /Users/thariq/Projects/poke-api/cc-prototype/data/gen2ou-1768.txt-169s- I No Ability 1ea.000x /Users/thariq/Projects/poke-opi/cc-prototype/data/gen2ou-176e.txt-1677- I Cloyster 71.913x /Users/thariq/Projects/poke-api/cc-prototype/data/gen2ou-1760.trt-167t- I Rhydon 71.747x /Ustrs/thariq/Projects/poke-opi/cc-prototype/data/gen2ou-176e.txt-16s2- I Houndoca 32.902% /Ustrs/thariq/Projtcts/poke-cpi/cc-prototypt/data/gen2ou-1768.txt-1685- I Skarnory 18.926x data/gtn2ou-1760.txt:1691: I Ytnusaur dota/gen2ou-1760.txt-1694- I Avg. neipht: 0.017e1e702325205615 /Users/tharia/Projects/poke-opi/cc-prototype/data/gen2ou-1760.txt-1697- I Abilities /Usert/thariq/Prajects/poke-ooi/cc-prototype/data/gtn2ou-1760.txt-16t6- I Skartory 1s.926x /Ustrs/tharia/projtcts/poke-opi/cc-prototypt/data/gtn2ou-1760.txt-169e- + data/gtnzou-1760.txt-1695- I Viabtltty Ctilirg: 7$ Asers/thariq/Profects/poke-opt/cc-prototypt/data/gtn2ou-1?6e.txt-1699- +--- data/aen2au-176o.txt-1693. I Ron count: 245 1
> 4.P.aTa.. 1a1 2 Tpraa s:D a. +

![[assets/dense-slides/TqC1qOfiVcQ/slide-025.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/TqC1qOfiVcQ/slide-025.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.

Slide text:

> Hook Events
> PreToolUse
> PermissionRequest
> PostToolUse
> UserPromptSubmit
> Notification
> Stop
> SubagentStop
> PreCompact
> SessionStart
> SessionEnd

![[assets/dense-slides/TqC1qOfiVcQ/slide-026.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/TqC1qOfiVcQ/slide-026.html)
- AI slide classifier: `content_slide` confidence `0.96`
- Text source: agent_vision.
- OCR decision: ready — Two embedded article screenshots and small URLs make the slide OCR-suitable.

Slide text:

> Useful resources


### Hidden Non-Slide Evidence
- [`slide-017.jpg`](/assets/dense-slides/TqC1qOfiVcQ/slide-017.jpg) — `speaker_stage` confidence `0.99`; speaker on stage at podium; not a presentation slide
- [`slide-018.jpg`](/assets/dense-slides/TqC1qOfiVcQ/slide-018.jpg) — `speaker_stage` confidence `0.99`; speaker/audience stage shot; not a presentation slide

Classification audit: `raw/sources/slide-ai-classification/dense/TqC1qOfiVcQ/audit.json`
