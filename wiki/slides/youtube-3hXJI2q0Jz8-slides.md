---
title: "Slides: Recursive Coding Agents - Raymond Weitekamp, OpenProse"
category: "slides"
video_id: "3hXJI2q0Jz8"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: Recursive Coding Agents - Raymond Weitekamp, OpenProse

## Source Video
[Recursive Coding Agents - Raymond Weitekamp, OpenProse](https://www.youtube.com/watch?v=3hXJI2q0Jz8)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/3hXJI2q0Jz8/slide-001.jpg]]

OCR text:

> AI ENGINEER WORLD'S FAIR • 2026
> Recursive Coding Agents
> Raymond Weitekamp
> RAW.works | OpenProse
> @raw_works

![[assets/slides/3hXJI2q0Jz8/slide-002.jpg]]

OCR text:

> MOTIVATION
> Weallwantoutcomes.
> Agents that work on ourbehalf-reliable co-workers-while we're out on a hike.
> The bottleneckisnot intelligence. It'sreliability.lt'strust.
> One day-my agents buildme a full SaaS app froma single prompt.
> The next day - they empty the entire contents of my Solana wallet.

![[assets/slides/3hXJI2q0Jz8/slide-003.jpg]]

OCR text:

> THESIS
> Today’s agents are
> mismanaged geniuses
> The intelligence is there.
> The missing layer is how we specify, manage, reuse, and verify the work.
> TURING POST • RAYMOND WEITEKAMP
> Stop Babysitting Agents, Start Authoring Outcomes
> ALEX ZHANG • ZED LI • OMAR KHATTAB
> The Mismanaged Geniuses Hypothesis

![[assets/slides/3hXJI2q0Jz8/slide-004.jpg]]

OCR text:

> RECURSIVE LANGUAGE MODELS
> Contextitselfisthe
> objectofcomputation Renr Laa Mad
> Externalize-thefullprompt livesinaREPL not the context window.
> slice,and transform it. Operate-the model writes code toinspect,
> Recurse-it sub-queriesitself over the slices. ARXIV:2512-24601
> Root RLM （depth=0） (dap）w-qns Sub-RLM8 (depth=1) —LLMA1（depth=2） LLMA2 (depth=2) LLM B1(depth=2) LLM B2（depth=2)

![[assets/slides/3hXJI2q0Jz8/slide-005.jpg]]

OCR text:

> THE RLM RUDRIC
> Lots of things feel close.
> Executable
> Prompt
> Codecalls
> Model picks
> State stays
> environment
> extenalized
> She model
> decomposition
> symbolle
> Plain long-context call
> Coding agents +subagents
> ing loops
> Hardcoded map-reduce
> -OARLM
> Recursive Language Model
> Open the RLMrubric

![[assets/slides/3hXJI2q0Jz8/slide-006.jpg]]

OCR text:

> OpenProse explicitly declares subagent work
> Here are two OpenProse examples where the model turns an external handle into smaller handles, then verifies the child-work trace.
> RECURSIVE DECOMPOSITION
> handle-recursive-reader.prose.md
> Starts from an external prompt_handle, not docs or read the whole thing
> The model decomposes terminal vs. nonterminal handles.
> Nonterminal handles produce child handles and call the same contract again.
> DIRECTORY HANDLE SLICER
> directory-handle-slicer.prose.md
> Starts from a repo or directory handle, not copied root context.
> The model uses search to choose relevant file handles for the question.
> Workers inspect only assigned handles; aggregation cites worker evidence.

![[assets/slides/3hXJI2q0Jz8/slide-007.jpg]]

OCR text:

> reliability Trustis model intelligence. Thenext stepis behavioral,notmore
> FTW Coding Agents Recursive compute canbeRLMs paradigmof inference-time Coding agents Anew RLMsare the new reasoningmodels- recursive codingagents are thenew coding agents. Claude Code dynamic OpenProse show two workflowsand concrete paths.

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
