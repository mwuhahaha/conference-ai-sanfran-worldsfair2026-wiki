---
title: >-
  Agents That Own Their Inference: Building Production AI Agents on Dedicated
  GPUs
category: talks
date: '2026-06-29'
time: '9:00am-11:00am'
track: Track 7
room: Track 7
speakers:
  - Du'an Lightfoot
sourceLabels:
  - Official conference schedule
  - Public YouTube metadata
last_auto_summarized: '2026-07-04T08:18:58.152Z'
---
# Agents That Own Their Inference: Building Production AI Agents on Dedicated GPUs

## Official Schedule Context
- Date/time: 2026-06-29 · 9:00am-11:00am
- Track/room: track TBD · Track 7
- Speaker(s): Du'an Lightfoot
- Session type/status: sponsor · confirmed

## Official Description
Every production agent today is renting its intelligence. You're paying per token, sending your

customer's data to someone else's servers, and hoping the provider doesn't rate-limit you during

your launch. For most teams, that's fine. But for a growing number of teams in regulated industries,

with high-volume products, latency-sensitive workloads, or rising token bills, it's starting to look

like a liability.  In this 120-minute hands-on workshop you'll get a dedicated GPU and build an

agent that runs on infrastructure you control. You'll stand up vLLM, point your agent at it, and

drive concurrent load through the stack until you can see batching, KV cache pressure, and

throughput limits in the metrics. Then you'll optimize the deployment to improve throughput while

keeping per-request latency in line.  The focus isn't agent frameworks. It's the inference layer

underneath them. You'll leave with working code and a real understanding of continuous batching

under real concurrency, KV cache tradeoffs, vLLM's metrics, and the bottlenecks that only show up

when you operate the inference server yourself.

## Summary
Du'an Lightfoot's workshop is framed as a hands-on production-inference lab for teams that want more control over the model-serving layer behind their agents. The official schedule description is explicit about the operational problem: hosted token APIs can become a liability when customer data, rate limits, launch traffic, latency targets, or rising usage costs make external inference feel like rented capacity rather than product infrastructure. In response, the workshop has participants use a dedicated GPU, stand up vLLM, point an agent at that endpoint, and then apply concurrent load until the inference server's real behavior shows up in metrics.

The useful connection is to Lightfoot's related public AI Engineer workshop, "Building Agents with Amazon Nova Act and MCP." That adjacent material is not confirmed as a recording of this exact World's Fair session, but it establishes the application-level agent vocabulary around tools, actions, environments, memory, autonomous systems, model-driven execution, Amazon Nova, and MCP. The extracted, dense, and reconstructed slide pages all point back to that same agent-building context. This page sits one layer lower in the stack: instead of focusing on how an agent selects tools or acts in an environment, it focuses on what happens when the team owns the model endpoint that agent depends on.

Read against the connected people and slide pages, the session is best understood as the infrastructure-heavy counterpart to Lightfoot's agentic-systems material. A team coming from the Nova Act and MCP framing would already be thinking in terms of agents that plan, act, remember, and call tools; this workshop asks what it takes to run the inference substrate for those agents under production pressure. The concrete learning surface is vLLM behavior under load: continuous batching, KV-cache pressure, throughput ceilings, and the latency tradeoffs that appear when many requests share a GPU-backed server. That makes the session less about choosing an agent framework and more about treating the GPU, scheduler, cache, metrics, and serving endpoint as part of the product's reliability boundary.

## Related YouTube Video
[Building Agents with Amazon Nova Act and MCP - Du'An Lightfoot, Amazon (Full Workshop)](https://www.youtube.com/watch?v=wFTVEDYVJT0) (speaker-match related prior/adjacent AI Engineer video; captions: English auto-captions).

## Transcript Status
Related video transcript availability: English auto-captions. Treat this as supporting context, not a recording of this exact scheduled session unless later confirmed. Cached at `raw/sources/youtube-transcripts/wFTVEDYVJT0.txt` (13,586 words).

## People
- [[du-an-lightfoot]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.
## Supporting Slides
- [[youtube-wFTVEDYVJT0-slides]] — extracted from the related public AI Engineer video.
## Slide Evidence
- Slide-only cropped deck: [[youtube-wFTVEDYVJT0-dense-slides]] (6 viable slide images).
- Related slide/OCR pages:
- [[youtube-wFTVEDYVJT0-dense-slides]]
- [[youtube-wFTVEDYVJT0-reconstructed-slides]]
- [[youtube-wFTVEDYVJT0-slides]]
- Slide-derived terms: `tools`, `microsoft`, `agentic`, `model`, `actions`, `https`, `world`, `amazon`, `execute`, `system`, `look`, `tere`, `nova`, `memory`, `environment`, `brain`, `autonomous`, `systems`
