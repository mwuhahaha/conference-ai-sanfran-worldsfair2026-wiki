---
title: "Slides: Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic"
category: "slides"
video_id: "TqC1qOfiVcQ"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic

## Source Video
[Claude Agent SDK (Full Workshop) — Thariq Shihipar, Anthropic](https://www.youtube.com/watch?v=TqC1qOfiVcQ)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video that matched one or more scheduled World's Fair sessions by speaker. They are supporting context unless the video is later confirmed as the exact session recording.

## Related Scheduled Sessions
- [[2026-06-30-thariq-shihipar-field-guide-to-fable]] — Field Guide to Fable

## Extracted Slides
![[assets/slides/TqC1qOfiVcQ/slide-001.jpg]]

OCR text:

> / ANTHROP\C
> Claude Agent SDK

![[assets/slides/TqC1qOfiVcQ/slide-002.jpg]]

OCR text:

> Agenda
> e What is the Claude Agent SDK?
> e Why use it?
> e How do you design an agent?
> e Example: prototyping an agent
> ANTHROPAC CONHDENTAL 2

![[assets/slides/TqC1qOfiVcQ/slide-003.jpg]]

OCR text:

> Ta
> ce
> 7 N
> y : ~
> | ; ‘ v a .
> ve ok . : | .
> ee ae — = E ; .
> L | |
> 7) 7 ;

![[assets/slides/TqC1qOfiVcQ/slide-004.jpg]]

OCR text:

> The evolution of agents
> . “8 @
> y aa 3 a
> Single-LLM Features JER WOIKIOWS am: Uae c
> Summarization, LLMs orchestrated LLMs deciding their Agency %
> classification, by code own trajectories Capability +
> extraction ...
> Flexibility t
> ANTHROP\C COME IGEN TIAL 4

![[assets/slides/TqC1qOfiVcQ/slide-005.jpg]]

OCR text:

> Claude Code
> Claude Code is our an agent that Oe
> lets developers automate software
> development tasks with Claude. : ee
> This is the first digital worker
> doing hours of work.
> a
> ANTHROP\C CONFIDENTIAL 8

![[assets/slides/TqC1qOfiVcQ/slide-006.jpg]]

OCR text:

> Building effective
> agents
> 1/ Models
> High-performance
> reasoning models
> that understand
> complex instructions
> and execute multi
> step workflows.
> Models
> mm Fastest with near-frontier intelligence Bee T SC Tee ley efor ad bis ta eee geen
> ANTHROP\C COSEIDEN TIAL

![[assets/slides/TqC1qOfiVcQ/slide-007.jpg]]

OCR text:

> Building effective
> agents
> 5/ File System bce ee seen tect cn cin en 2
> Give Claude a
> persistent workspace Tools Prompts File System
> to pass files, write
> just-in-time code, “we com Neen Prosens ies
> and learn from Custom Custom mess
> example outputs File System Workllows Ex Output
> Claude Haiku Claude Sonnet Pelt Ce tT]
> Dee em csul iad RT a teva e evel tg beet Ere Bi gn
> ANTHROP\C CONHPIBENTIAL

![[assets/slides/TqC1qOfiVcQ/slide-008.jpg]]

OCR text:

> Building effective Your Application
> Pp :
> agents
> Claude Agent SDK
> 9/ Application Fe = a a RT 9 TN Re TE =
> . SKILLS Enhancements.
> Focus on your unique Subagents
> value - build tne user Tools Prompts File System Web Search
> experience an Research Mode
> domain workflows “we Som Neen Proce is Auto Compacting
> that differentiate your Coton “sen ures Hooks
> product File System Workllows Ex Output Memory
> - [ é Models
> oT CS Seat POUT CRS Tita Claude Opus
> DE mesure Smartest for complex agents /coding be se Eire BC mete ag
> ANTHROP\C CONEIDEN TIAL

![[assets/slides/TqC1qOfiVcQ/slide-009.jpg]]

OCR text:

> Users are already building cutting-edge agents
> with the CC SDK
> e All software tasks
> SRE agents
> Security agents
> - Incident triage agents
> Automated bug fixing
> e Site & Dashboard builders
> e MS Office agents
> e Legal, Finance, Healthcare, HR
> e Custom agent instructions + any integration
> Cloud logs, CI/CD, ete.
> ANTHROP\C CONEIDEN TIAL w

![[assets/slides/TqC1qOfiVcQ/slide-010.jpg]]

OCR text:

> Why use the Claude Agent SDK?
> 
> - We realized people were using Claude Code for non-coding tasks.
> 
> - We build our agents on top of our Agent SDK.
> 
> - Itis built on top of lessons we've learned deploying Claude Code to
> millions of users.
> 
> - We have strong opinions on the best way to build agents.
> 
> - One of our biggest learnings: the Bash tool is the most powerful agent
> tool.

![[assets/slides/TqC1qOfiVcQ/slide-011.jpg]]

OCR text:

> The Agent SDK is the best way to build agents in the
> “Anthropic Way”
> - Unix Primitives: Every agent should use bash [1] &a file system [2] (e.g.
> skills & memory)
> - Agents > Workflows: Agents build their own context + decide what to do
> with tools.
> - Code Generation for non-coding: We use code gen to generate docs,
> query the web, etc.
> - Every agent has a container.
> More on this here.

![[assets/slides/TqC1qOfiVcQ/slide-012.jpg]]

OCR text:

> Bash is all you Need
> Bash is what makes Claude Code so good.
> Bash is a generic version for “code mode” or programmatic tool calling.
> The bash tool allows you to:
> 
> - Store the results of tool calls to files, so you can search them.
> 
> - Store memory in files.
> 
> - Dynamically generate scripts and call them.
> 
> - Compose functionality, use unix primitives like tail, grep, cat, etc.
> antundSe existing powerful software like ffmpeg, libreoffice, etc.

![[assets/slides/TqC1qOfiVcQ/slide-013.jpg]]

OCR text:

> Without Bash With Bash
> User: How much did I spend on ride sharing User: How much did I spend on ride sharing
> this week? this week?
> Tool Cali (Gmail Query Search) query: “uber Tool Call (Bash): ‘gmail_search.ts query
> OR lyft” “uber OR lyft*
> Thinking: I found the following emails that Tool Call (Bash):
> mention Uber and Lyft, I need to find the
> cost of each email. gmait_search.ts ~- a> :
> wot sf
> ret > : " IN
> Claude: The total is... (hallucinated) wee : 1 \ a, /

![[assets/slides/TqC1qOfiVcQ/slide-014.jpg]]

OCR text:

> e
> ae i ee: a 7 an a 7 re re ye an keer ee ae ae ad / eT
> ce or ee ne
> Con Cams CE Co OY 6 FS 6 Tobiys apna 55) \
> nL ae ee Ld OY
> JQ atte te ia
> sort  . >» contacts this week.txt
> Ch ee ce en ke ee to er ne ee eee
> read ematl;
> (10 as nt ee ce \
> rT eee are Oe a CLT Cs LS ar 2k oa 01a: (en Oe (Ree Xel an
> Sleep (il 8 tate ar
> < contacts this week.txt
> a cae ee ea ed
> fem contact detatls.jsonl > final contacts.json

![[assets/slides/TqC1qOfiVcQ/slide-015.jpg]]

OCR text:

> ®
> a) 7 ee 2 Ce eee Pia ee 8
> a aes a |B Bue BO pee 4 / en ans
> fimpeg earnings call.apd .: rn Lee aone Mr: TUrO ROC PRU LG
> whisper audio.way mene @ ROLL a ee 2:1 0)) ee ese a Oh OED 01D
> ee i ea ee ee ee
> ‘gee a PP tee transcript.json > moments. txt
> ce ora oe ee nr re ee: ce
> _ ag ee transcriupt.}son | \
> read start end,
> {fepeq earnings call.mp4 ren ae rn
> Como) 0 EO

![[assets/slides/TqC1qOfiVcQ/slide-016.jpg]]

OCR text:

> ANTHROP\C
> Workflows & Agents

![[assets/slides/TqC1qOfiVcQ/slide-017.jpg]]

OCR text:

> Workflows & Agents
> 
> We build both agents and workflows on the Claude agent SDK.
> Agents are like Claude Code - You talk to them in natural language
> and they take action.
> 
> Workflows are like our Github action - You define inputs and
> outputs, e.g. take in a PR and give a code review.

![[assets/slides/TqC1qOfiVcQ/slide-018.jpg]]

OCR text:

> Workflows & Agents
> When building workflows, use our structured outputs:
> 
> https: //platform.claude.com/docs /en /agent-sdk/structured-o
> utputs

![[assets/slides/TqC1qOfiVcQ/slide-019.jpg]]

OCR text:

> lay
> 
> i :
> A '
> 
> ‘ ‘
> 
> x ; : MW
> n 2
> Pn -
> oe
> ma]

![[assets/slides/TqC1qOfiVcQ/slide-020.jpg]]

OCR text:

> Claude Agent SDK Loop
> Gather Take Verify
> context action work
> ANTHROP\C COMPIEENTIAL 29

![[assets/slides/TqC1qOfiVcQ/slide-021.jpg]]

OCR text:

> Tools vs Bash vs Code Generation
> Tools:
> - Pros: Highly structured, highly reliable
> - Cons: High context usage, not composable
> Bash:
> - Pros: Composable, static scripts, low context usage
> - Cons: Longer discovery time, slightly lower call rate
> Code Gen:
> - Pros: Highly composable, dynamic scripts
> - Cons: Needs linting & possibly compilation, careful API design

![[assets/slides/TqC1qOfiVcQ/slide-022.jpg]]

OCR text:

> Tools
> Use tools for: Atomic actions your agent mostly needs to execute
> in sequence
> For example:
> - Writing a file
> - Sending an email

![[assets/slides/TqC1qOfiVcQ/slide-023.jpg]]

OCR text:

> e
> Why Skills?
> agent-skills / skills / public; (0
> Skills let one agent accomplish longer, more complex = eter
> 7 * @ peteriai-ant adc ng better docx redir ng {B19b)
> tasks without needing Subagents. The agent can use
> many Skills and read them only when needed. Name
> se
> Nom fet roe cteate ibe Laced dovument th all the information fue gathered. and ben
> eile an cxevuthe summary in Woed Be docx
> eae meee gd ete MD pptx
> In oe oe
> Some tet me dorate The Wotd document with the execuxlve summary
> a Law. QUAN aeegineRneie
> New Pilteute the Ward document cveuthe sunimasy:

![[assets/slides/TqC1qOfiVcQ/slide-024.jpg]]

OCR text:

> What are Skills?
> An organized collection of files (instructions, nd onw
> executable code, assets) containing everything docs.nd
> Claude needs for a specific task. L apply..template. py
> Skills give an agent:
> 
> General capabilities Claude isn’t good at out of the box (yet)
> 
> e.g. creating PDFs, Excel, & Powerpoint files
> 
> Knowledge of an organization’s workflows and best practices
> 
> e.g. Anthropic’s Brand Styling

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
## Reconstructed Slide Deck
- [[youtube-TqC1qOfiVcQ-reconstructed-slides]]
## Dense Scene-Detected Slide Candidates
- [[youtube-TqC1qOfiVcQ-dense-slides]]
