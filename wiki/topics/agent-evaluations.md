---
title: "Agent Evaluations"
category: "topics"
sourceLabels: ["Slide/video-derived supporting context"]
---

# Agent Evaluations

## Synopsis
Agent evaluations are the measurement layer for systems that plan, call tools, write code, retrieve context, or take actions over time. They combine offline tests, production traces, human review, model-as-judge scoring, regression suites, and task-specific rubrics so teams can tell whether an agent is actually improving rather than merely sounding better.

## Origin And Context
The practice grows out of software testing, information-retrieval benchmarks, ML evaluation, and LLM prompt evaluation. Agentic systems made the problem harder because success depends on multi-step behavior: tool choice, state handling, recovery, cost, latency, safety, and final task outcome.

## Why It Matters
Without evaluations, agent teams cannot safely change prompts, models, tools, routing, memory policies, or autonomy levels. Evals turn vague quality complaints into visible failure modes and make it possible to ship agents with rollback criteria, measurable acceptance thresholds, and a shared language for product and engineering decisions.

## How To Use It
Start with real traces and representative tasks. Define the outcome that matters, add rubrics for intermediate behavior, keep golden examples for regressions, and separate fast pre-merge checks from slower production audits. Use model judges only when their decisions are calibrated against human review, and track cost, latency, and failure categories alongside quality.

## Where It Is Useful
Evaluations are useful in coding agents, support agents, research agents, data agents, voice agents, retrieval systems, and any workflow where the agent can take a plausible but wrong path. They are especially valuable where correctness, trust, or operational cost matters.

## When To Use It
Use evals before launching, whenever prompts or models change, when adding new tools, after incidents, and when expanding an agent into a new user segment or task family. Lightweight evals should run continuously; deeper reviews should run before major releases.

## Active Use Cases
- Regression tests for prompt, model, and tool changes.
- Production trace review for agent reliability and cost drift.
- Benchmarking coding agents, retrieval agents, and long-horizon workflows.
- Reward-signal generation for continual learning and fine-tuning loops.

## Related Slide Decks
- [[youtube-aHhB3sjGjkI-slides]] — Agents Building Agents - Alfonso Graziano, Nearform (24 extracted slide frames)

## Related Scheduled Sessions

## Transcript And Resource Support
### Transcript-backed resources
- [[youtube-Xfl50508LZM]] — Ship Real Agents: Hands-On Evals for Agentic Applications — Laurie Voss, Arize
- [[youtube-bk0TmxoZlUY]] — Evals 101 — Doug Guthrie, Braintrust
- [[youtube-iNkFlCiij0U]] — The Art & Science of Benchmarking Agents — Vincent Chen, Snorkel AI
- [[youtube-vljxQZfJ9wY]] — Production Evals For Agentic AI Systems - Nishant Gupta, Meta Superintelligence Labs
- [[youtube-pSto5YaNGUo]] — The Agentic AI Engineer - Benedikt Sanftl, Mutagent
- [[youtube-hqHC6Z_lXyo]] — 20 days of compute vs 7 hours: rethinking what state-of-the-art means — Bertrand Charpentier, Pruna
- [[youtube-YYH0DMQr30A]] — Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel
- [[youtube-aHhB3sjGjkI]] — Agents Building Agents - Alfonso Graziano, Nearform
- [[youtube-2IxD9OB3XuQ]] — Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI
- [[youtube-QuuIywMG4s8]] — Evals Are Broken, Use Them Anyway — Ara Khan, Cline
- [[youtube-ObTPqBGsEbA]] — The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks
- [[youtube-T0HhO4YtTfE]] — AI System Design: From Idea to Production - Apoorva Joshi, MongoDB
- [[youtube-htM02KMNZnk]] — WF2026: Software Factories & Keynotes ft. Microsoft, OpenAI, OpenClaw, Z.ai (GLM), MiniMax, HF
- [[youtube-Jx4ZFEAq6bY]] — User Signal Dies at the Retrieval Boundary - Sonam Pankaj, StarlightSearch
- [[youtube-wcUJWP6WpGM]] — SWE-rebench: Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius
- [[youtube-LrGCT7G_rU8]] — Using RL Agent to Detect and Remediate ETL Pipeline Failures - Anna Marie Benzon
- [[youtube-IJXjTLPzvAU]] — The Miranda Hypothesis: How Hamilton Poisoned Persona Evals - Jacob E. Thomas, Results Gen
- [[youtube-TNwJ1LMiENk]] — Stop Making Models Bigger, Make Them Behave — Kobie Crawford, Snorkel

### Quote signals
- “Uh I had a question on um on how how much evaluation you need to write for uh feature cuz especially when you run against live traces, sometimes the the evaluation can cost more than the actual feature.” — [[youtube-Xfl50508LZM]]
- “One of the key things is it treat memory as reasoning, not as facts, statistics, fact with no context and no history, but reasoning.” — [[youtube-Jx4ZFEAq6bY]]
- “But the problem is that state of the art is a bit a confusing concept and people maybe have different vision on this.” — [[youtube-hqHC6Z_lXyo]]
- “The event outcome becomes a first-class signal in the retrieval re-ranking and not just for retrieval.” — [[youtube-Jx4ZFEAq6bY]]
- “Uh the other thing to call out here is like we already have a lot of companies using brain trust in production today.” — [[youtube-bk0TmxoZlUY]]
- “Um so anyway, so the the title of my talk today is evals are broken and you should use them anyway.” — [[youtube-QuuIywMG4s8]]
- “And lastly, this axis is all about producing more complex work, more representative work, and also nuanced signals that can be used for not just evaluation, but reward signals during training.” — [[youtube-iNkFlCiij0U]]
- “And for the same amount of evaluation, it takes only 7 hours.” — [[youtube-hqHC6Z_lXyo]]
