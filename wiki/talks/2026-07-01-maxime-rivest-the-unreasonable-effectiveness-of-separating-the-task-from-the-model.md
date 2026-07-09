---
title: "The Unreasonable Effectiveness of Separating the Task from the Model"
category: "talks"
date: "2026-07-01"
time: "9:40am-10:00am"
track: "Harness Engineering"
room: "Main Stage"
speakers: ["Maxime Rivest", "Isaac Miller"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Harness Engineering"
scheduleRoom: "Main Stage"
scheduleLabels: ["Harness Engineering", "Main Stage", "keynote", "confirmed"]
---
# The Unreasonable Effectiveness of Separating the Task from the Model

## Official Schedule Context
- Date/time: 2026-07-01 · 9:40am-10:00am
- Track/room: Harness Engineering · Main Stage
- Speaker(s): Maxime Rivest, Isaac Miller
- Session type/status: keynote · confirmed

## Schedule Labels
- Track: Harness Engineering
- Room: Main Stage
- Session type: keynote
- Status: confirmed

## Official Description
By declaring your task’s inputs and outputs without initially considering model capability, you

create the space needed to figure out the model execution later. DSPy’s entire promise is that you

should evaluate and execute your AI engineering at a level higher than a specific prompt template or

a particular provider’s API shape: the Signature. However, models have evolved significantly over

the last few years. How can the same input and output specifications still work in a world now

filled with tools, RLMs, and Skills? By defining your task strictly through its inputs and outputs,

the underlying implementation becomes completely flexible. You can experiment with different models,

settings, weights, templating strategies, and output formats, all without touching your actual AI

workflow. Consequently, you can leverage components built by others and focus entirely on your core

AI task. In this talk we will present how dspy 3.5 makes it easier much easier. DSPy has its roots

in prompt optimization, where we build efficient ways to conduct search and learning beneath the

signature. In this talk we will give a preview of DSPy 4.0 where we use the fact that models have

now passed a tipping point for two critical concepts we have always needed. First, we no longer need

to limit the search space to a single instruction block per LLM call; models can now reliably write

the code underneath a signature themselves—so they should. Second, traditional prompt optimization

has always required a scalar metric, which is notoriously one of the hardest parts to get right.

What if a DSPy program could learn directly from your interactions with users? Ultimately, all you

care about is that the function you call respects the inputs and outputs of your signature. You can

let the models figure out the rest.

## Related YouTube Video
No related AI Engineer channel video found yet.

## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## People
- [[maxime-rivest]]
- [[isaac-miller]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.
## Livestream Segment
- [Watch in livestream at 00:53:36](https://www.youtube.com/watch?v=I2cbIws9j10&t=3216s) — WF26: Harness Engineering & Startup Battlefield (Day 3).
- Match basis: speaker and title; timed captions matched Maxime Rivest, effectiveness, model, separating, task, unreasonable.
- Confidence: high automated match; prefer a dedicated cut-video recording when one exists.
