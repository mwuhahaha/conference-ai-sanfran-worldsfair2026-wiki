---
title: "Don't Write Skills, Train Models"
category: "talks"
date: "2026-06-30"
time: "2:50pm-3:10pm"
track: "Workshops Day 3"
room: "Track 4"
speakers: ["Brian Douglas", "John McBride"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
---

# Don't Write Skills, Train Models

## Official Schedule Context
- Date/time: 2026-06-30 · 2:50pm-3:10pm
- Track/room: Workshops Day 3 · Track 4
- Speaker(s): Brian Douglas, John McBride
- Session type/status: session · confirmed

## Official Description
Every AI agent call generates training data. Most teams throw it away. They write skills files

instead. Text documents that describe how to do a task and hope the model follows them at inference

time. Skills work until they don't. The model drifts, skips steps, hallucinates a shortcut. So you

rewrite the skill, add more constraints, hope harder. There's a better path. If you've used a skill

enough to know what good output looks like, you already have training data. You just aren't using

it. This talk covers what I learned building an open source fine-tuning pipeline that turns agent

session traces into SFT and DPO training datasets. A telemetry proxy captures every LLM call as a

content-addressed Merkle DAG with zero instrumentation. Successful sessions become supervised fine-

tuning data. Pair them against failures, matched by goal category, and you get preference pairs for

DPO. No manual labeling. No synthetic data. But training data quality depends on environment

consistency. If the same agent produces different results because of package drift, nondeterministic

toolchains, or inconsistent system state, your training signal is noise. This is where NixOS changes

the equation. A hardened, reproducible OS means every agent session runs against an identical,

declarative environment. Nix controls the variables that sandboxing alone doesn't: dependency

graphs, system libraries, toolchain versions. When you can guarantee the environment is the same

across hundreds of sessions, the behavioral signal in your traces is actually trustworthy. We'll

walk through the full pipeline. How to rebuild parent-hash chains from a SQLite database and join

facet metadata. How to filter to fully_achieved sessions and truncate 82k-token conversations down

to 4k-6k training examples using summary context plus the last three turns. How to match

success/failure pairs by goal category and exclude unclear_requirements failures so DPO learns from

real agent mistakes, not ambiguous prompts. How QLoRA keeps VRAM low enough to train a 7B model on a

single consumer GPU. And what happens when you try DPO on 12GB VRAM (two simultaneous forward passes

for logprob computation will teach you about gradient accumulation settings fast). The result: a

LoRA adapter trained on your own agent traces, in a reproducible environment, on a single consumer

GPU, for less than $2 in cloud compute. No YAML. One config file. All code is open source.

## Related YouTube Video
No related AI Engineer channel video found yet.

## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## People
- [[brian-douglas]]
- [[john-mcbride]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.
