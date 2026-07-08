---
title: "ALPHALAB: Autonomous Multi-Agent Research Across Optimization Domains with Frontier LLMs"
category: "talks"
date: "2026-07-01"
time: "10:45am-11:05am"
track: "AI in Finance"
room: "Track 3"
speakers: ["Brendan Rappazzo"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "AI in Finance"
scheduleRoom: "Track 3"
scheduleLabels: ["AI in Finance", "Track 3", "session", "confirmed"]
---
# ALPHALAB: Autonomous Multi-Agent Research Across Optimization Domains with Frontier LLMs

## Official Schedule Context
- Date/time: 2026-07-01 · 10:45am-11:05am
- Track/room: AI in Finance · Track 3
- Speaker(s): Brendan Rappazzo
- Session type/status: session · confirmed

## Schedule Labels
- Track: AI in Finance
- Room: Track 3
- Session type: session
- Status: confirmed

## Official Description
We built AlphaLab to automate quantitative research at Morgan Stanley’s Machine Learning Research

Lab - the experimental grind of architecture search, hyperparameter tuning, and literature review

that consumes most of a researcher's time. To show it generalizes, we ran it on three deliberately

different domains: CUDA kernel optimization (4.4× mean speedup over torch.compile, 91× peak), LLM

pretraining (22% lower validation loss under a 20-minute budget), and traffic forecasting (23–25%

RMSE improvement after the system independently found and tuned TFT and iTransformer from the

literature). AlphaLab is an agentic harness that takes a dataset and a natural-language objective

and runs a full research campaign across three phases: it explores the data and surveys prior work,

it constructs and adversarially validates its own evaluation framework, and then it runs experiments

at scale on a multi-GPU cluster via a Strategist/Worker loop with a persistent playbook that

accumulates domain knowledge across experiments. In Phase 3 - the dispatcher keeps a large cluster

fully utilized indefinitely with no human in the loop, and the playbook ends up containing domain-

specific methodology that didn't exist anywhere in the prompts at launch. This talk walks through

the three phases, what we learned from running campaigns with different models, what we have learned

from using this in real systems, and future areas we are exploring.

## Related YouTube Video
No related AI Engineer channel video found yet.

## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## People
- [[brendan-rappazzo]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.
