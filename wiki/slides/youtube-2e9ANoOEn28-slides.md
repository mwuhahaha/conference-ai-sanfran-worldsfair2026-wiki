---
title: "Slides: What if the harness mattered more than the model? - Aditya Bhargava, Etsy"
category: "slides"
video_id: "2e9ANoOEn28"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: What if the harness mattered more than the model? - Aditya Bhargava, Etsy

## Source Video
[What if the harness mattered more than the model? - Aditya Bhargava, Etsy](https://www.youtube.com/watch?v=2e9ANoOEn28)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/2e9ANoOEn28/slide-001.jpg]]

OCR text:

> About me
> • Staff engineer at Etsy
> • Also Etsy's IC Initiative Lead for Agentic Commerce
> • Wrote Grokking Algorithms, an illustrated book on algorithms
> • Blog at ducktyped.org
> Aditya Bhargava What if the harness mattered more than the model?

![[assets/slides/2e9ANoOEn28/slide-002.jpg]]

OCR text:

> ne bug:
> ema crane iat @ 41011116121 aD
> ordered sortedCnumbers)
> middle lenCordered)
> ordered[middle]
> fails: fi
> AssertionError: median() returned 3, expected 2.5
> ame model, sare task for every example. Only the harness chang
> -
> J

![[assets/slides/2e9ANoOEn28/slide-003.jpg]]

OCR text:

> node mainc) {
> prompt un
> The Python function medianCnumbers) in demo/median.py has
> result LlmCprompt)
> printCresult)
> i
> It can't read or write to the file
> npx agency examples/@1-11m.agene
> 0"

![[assets/slides/2e9ANoOEn28/slide-004.jpg]]

OCR text:

> mM 2d, PWrispm Cé.0S, Ya tok, su. WuU) | Ka.0nD |
> ne 25. 10:15pm 1.78, 207 tok, SO.Q060)  [rzaxzy!
> agentRun “main” (1.75, 207 tok, $0.@@Q0)
> >» agentStart “main”
> v nodeExecution “main” (1.7s, 207 tok, $@.00@)
> v ileCell gpt-4do-rini » “Use your aqreet too. to greet 0:
> 
> [user] “Use your greet togeto greet Adit’
> 
> Lassistant] tool ca:l: greetés "nares "Adit" })
> 
> v toolExecution greet (€ Jw
> 
> er toolCall ‘greet’ Clirs)
> [tool: greet] “Howdy, Adit!”
> [assistant] “Howdy, Adit!" |
> rg
> 
> m agentEnd (1.7s) A.

![[assets/slides/2e9ANoOEn28/slide-005.jpg]]

OCR text:

> handle {
> result, ,llm¢
> prompt, W
> i me
> tools: [read.partial(dir “demo"), write.partial
> ba
> )
> | wear aaneelolelaenZ=
> read(filename: string, dir: string): Bas t+
> a a3
> @ We lock the argurent to N |
> e@ Now the agent can only read files in. ~ Lie

![[assets/slides/2e9ANoOEn28/slide-006.jpg]]

OCR text:

> yject. Steps:
> } command ‘python’
> ~ median.py with the write tool, then run the tests
> ial time to confirm they pass. )
> fences, and decides what to do next ;
> _

![[assets/slides/2e9ANoOEn28/slide-007.jpg]]

OCR text:

> -bash Pa
> | ai-talk Cmain) $ geo
> ai ialk (main) $% gd
> diff --git a/examples/demo/median.py b/examples/demo/medi
> index ecl2aff..6927b68 100644
> ~-- a/examples/demo/median.
> ree b/exanpLes/deno/median.Pyt
> awe 1 5 41,7 on
> def medrvantnumbers ):
> "Return the median value of a list of numbers." °"
> + 1f not numbers:
> a raise ValueErrorC’The List Cannot —
> _ ordered — sorted(numbers ) |
> ewerenee LenCordered) o. 2 a ¥
> if lLen€ordered) ' 20>: @: A
> ap eal Gn Gar Gulenenemmns vill

![[assets/slides/2e9ANoOEn28/slide-008.jpg]]

OCR text:

> baseline objective 6.800
> iter 1/5 accepted objective 1.000
> ~ examples/07-optimize.agency:main: prompt:
> Hi - The Python function median has a bug. Pleas
> 7 Ensure to fix any bugs in the Python functi
> nt CTDD) principles. Start by outlining potential tes
> rite the tests before modifying the code to ensure al
> he function for clarity, and ensure to include a chec
> CR cea eas nee eae

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
