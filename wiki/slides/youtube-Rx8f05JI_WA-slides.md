---
title: "Slides: SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale - Rishi Desai, Abundant AI"
category: "slides"
video_id: "Rx8f05JI_WA"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale - Rishi Desai, Abundant AI

## Source Video
[SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale - Rishi Desai, Abundant AI](https://www.youtube.com/watch?v=Rx8f05JI_WA)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/Rx8f05JI_WA/slide-001.jpg]]

OCR text:

> eee
> SWE-Marathon
> Can coding agents stay coherent over a 1 billion token budget?
> Rishi Desai
> @® abundant ys .
> YY

![[assets/slides/Rx8f05JI_WA/slide-002.jpg]]

OCR text:

> eee
> Agents are moving to autonomous end-to-end projects
> A\ Anthropic GS OpenAl
> “Building a C compiler with a team of parallel! “Parameter Golf” — train a GPT under a tiny
> Claudes” checkpoint budget
> a, Cloudflare Vv Cursor
> “How we rebuilt Next.js with Al in one week" “Scaling long-running autonomous coding” ‘an
> §

![[assets/slides/Rx8f05JI_WA/slide-003.jpg]]

OCR text:

> a
> From coding tasks to engineering projects
> Function completion ~1K TOKENS
> HumanEval . : :
> 
> Real GitHub issues ~100K TOKENS
> 
> SWE-bench 4 : ;
> Multi-step terminal tasks ~1M TOKENS
> 
> Terminal-Bench 8 . ‘ ‘
> a Days-long agentic work 18+ TOKENS
> 
> SWE-Marathon - Ss a
> 4

![[assets/slides/Rx8f05JI_WA/slide-004.jpg]]

OCR text:

> a
> First benchmark with full-stack CUA-verified tasks
> CUA verifier grades Slack clone
> qe
> ‘val >

![[assets/slides/Rx8f05JI_WA/slide-005.jpg]]

OCR text:

> Firstbenchmarkwithfull-stackCUA-verified tasks
> .CUAVERIFIER
> √PASS
> he to Bge
> -sayhtyou1
> Workspacelayout
> Sidebar,channels,compose
> Check03/09
> Signup&signin
> Session/account
> Slack-like layout
> Emojipicker
> Reaction badges

![[assets/slides/Rx8f05JI_WA/slide-006.jpg]]

OCR text:

> ene
> 20 tasks across four families
> @ Full-stack product clones task
> Algoritheic
> 2 tasks =~] a
> a Library closes
> & tasks
> me @ Library clones & reproductions potanes
> 9 fans euberretes-rust-rewrite
> rust-c-cotpiler
> Product closes © MLE oe
> S$ tases Jae-pytorch-temwrite _
> post-traiq-afeval i
> ‘
> a

![[assets/slides/Rx8f05JI_WA/slide-007.jpg]]

OCR text:

> Leaderboard
> 1,400 31.3M 877.4M
> trials avg tokens/trial longest trial
> MODEL/AGENT AlClaudeOpus4.8/Claude Code RESOLUTION RATE (PASSO1) 26.0%
> AClaudeOpus4.7ClauseCode 16.0%
> ZGLM5.2/C1eCod 13.0%
> GPT-5.5/CdexCL1 12.0%
> Gemini3.5 Flash/Geaini CL1 7.0%
> 心 DeepSeekV4Pro/Terainus2 4.0%
> Gemini 3.1ProPreview/ Genini CL1 2.0%
> 业 MiniMaxM2.7/Terninus2 0.0%
> ? KimiK2.6/Kini Code CL1 0.0%
> 254

![[assets/slides/Rx8f05JI_WA/slide-008.jpg]]

OCR text:

> a
> A 356M token rollout for next js-vite-rewrite
> 9.4 hours 844 842 total rcitlnty 4a
> . sees a ® ‘ MM bates Ja GB
> MB cetoyecoe Wit
> hatue Pages scutes 6 SSR Oey deat beta at = eter teen 2615
> Lys 2.96 4.9h 6.86 7a $.5n 9.3a
> O_O 0 On OO O_O O08
> ek GUN 5.27 Claw e
> >
> ’

![[assets/slides/Rx8f05JI_WA/slide-009.jpg]]

OCR text:

> Reward hacking
> 12.8% 9.2%
> suspiclous shortcut behavior clear exploit shipped rdviaexploit
> MODEL/AGENT GPT-5.5/Cx CLI Gemini3.1Pro Preview/Genin1 CLI SHAREOF TRIALS（%） 30.0% 19.0%
> Gemini3.5Flash/GeminiCL1 16.0%
> KimiK2.6KimCode CLI 10.0%
> A\ClaudeOpus4.8/ClaudeCode 9.1%
> A\ClaudeOpus 4.7/ClaudeCode DeepSeekV4Pro/Terninus2 6.3% 5.0%
> ZGLM5.2/ClaodeCode 3.0%
> MiniMaxM2.7/Terninus2 1.0%
> Suspiclous shortcut behavier 10% Ctear exptoit shipped 20 48s

![[assets/slides/Rx8f05JI_WA/slide-010.jpg]]

OCR text:

> « eo e
> Gemini 3.1 Pro cheats on the C compiler task
> Task: build a C compiler in Rust :
> 0.989
> , Looks almost solved if you only compare cutput.
> implement lexer, parser, “> use gcc inside Rust code
> codegen in Rust
> ng ar rer rae Or nT ar The verifier runs strace, sees gcc Spawn, and
> rere eo tees rejects COMPLET wrappers
> fra ae an res ce sO Ca cee
> eetataustl
> @.989 partial ~ © reward gee
> | €
> >
> y

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
