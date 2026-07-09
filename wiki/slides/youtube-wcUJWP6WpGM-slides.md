---
title: "Slides: SWE-rebench: Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius"
category: "slides"
video_id: "wcUJWP6WpGM"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: SWE-rebench: Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius

## Source Video
[SWE-rebench: Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius](https://www.youtube.com/watch?v=wcUJWP6WpGM)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/wcUJWP6WpGM/slide-001.jpg]]

OCR text:

> SWE-rebench:Lessons from Evaluating Coding
> Agenis on Real Software Engineering Tasks

![[assets/slides/wcUJWP6WpGM/slide-002.jpg]]

OCR text:

> Why evals matter now?
> Models improved. Choosing became harder.
> 
> ra ina * Vibe checks do not scale un ; . - we ad
> 
> * ra SWE performance grows rapidly an es
> 
> ry a ag Options change every month zn :
> 
> i
> “ ae cy ae ae Cid * °
> * SWE-rebench 2026_02 tasks wn o oe wn wn
> i

![[assets/slides/wcUJWP6WpGM/slide-003.jpg]]

OCR text:

> Anatomy of a Task: A Task Is More Than Text
> Task description — original issue text 7
> Reape Oe a sard ty oo age to wee bP ey tere
> Panne d a
> bd bd
> bd *
> ty * Sandbox environment —
> executable Docker image Hoe tte Op
> Verifier - tests from the PR.
> Lest updeted
> FAIL_TO_PASS + PASS_TO_PASS iin a
> ducker pull saerebench/seeb eva
> dew 1776 pyfakets- 1286
> 1 | Al Engineer |
> es — Se) ce)
> — ~<

![[assets/slides/wcUJWP6WpGM/slide-004.jpg]]

OCR text:

> What Makes a Good Task?
> Problem description
> 1. A good task balances clarity
> x * & 2. Too easy and too hard both fail er cee :
> a Od eo. ee
> pe " 3. Complexity: breadth or depth an -.
> Pa Reliable verifier ee
> 1. Should reward actual fixes, should reject fake —
> solutions : ; ec
> 2. Not too narrow, not too wide “oo oa -
> Stable infrastructure is part of eval 7 ; a aan
> 1. Minimal infra noise during runs —_ i
> 2. Connection might blink, images might become
> stale, pipeline might break (1970s bug)
> ha
> _ Al Engineer
> |p See) a 3
> ye
> A — »

![[assets/slides/wcUJWP6WpGM/slide-005.jpg]]

OCR text:

> Execution Setup: Minimal Agent, Strong infrastructure
> el Minimalistic agent (open, edit, bash)
> bd *
> Ae
> * * YOLO setup
> * oa bd
> Agent < Infrastructure
> ReAct + demo — tools + no_demo
> * Claude-Opus-4.6 top commands from our agent
> a Pe eee ee ee Aan ie Pe Oe oe ad tat re |
> ~ ee Sraintrust &, WorkOS WpenaA
> . - . ip

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
