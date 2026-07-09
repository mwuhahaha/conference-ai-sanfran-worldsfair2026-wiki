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
last_auto_summarized: '2026-07-06T20:02:16.974Z'
scheduleTrack: ""
scheduleRoom: "Track 7"
scheduleLabels: ["Track 7", "sponsor", "confirmed"]
---
# Agents That Own Their Inference: Building Production AI Agents on Dedicated GPUs

## Official Schedule Context
- Date/time: 2026-06-29 · 9:00am-11:00am
- Room: Track 7
- Speaker(s): Du'an Lightfoot
- Session type/status: sponsor · confirmed

## Schedule Labels
- Track: track TBD
- Room: Track 7
- Session type: sponsor
- Status: confirmed

## Official Description
Every production agent today is renting its intelligence. You're paying per token, sending your customer's data to someone else's servers, and hoping the provider doesn't rate-limit you during your launch. For most teams, that's fine. But for a growing number of teams in regulated industries, with high-volume products, latency-sensitive workloads, or rising token bills, it's starting to look like a liability. In this 120-minute hands-on workshop you'll get a dedicated GPU and build an agent that runs on infrastructure you control. You'll stand up vLLM, point your agent at it, and drive concurrent load through the stack until you can see batching, KV cache pressure, and throughput limits in the metrics. Then you'll optimize the deployment to improve throughput while keeping per-request latency in line. The focus isn't agent frameworks. It's the inference layer underneath them. You'll leave with working code and a real understanding of continuous batching under real concurrency, KV cache tradeoffs, vLLM's metrics, and the bottlenecks that only show up when you operate the inference server yourself.

## Summary
Du'an Lightfoot's World's Fair workshop is a production-inference lab for agent teams that want the model endpoint to become infrastructure they own rather than an external token API they rent. The official session description names the operational pressure points directly: customer data leaving the team's boundary, provider rate limits during launches, high-volume products, latency-sensitive workloads, regulated-industry constraints, and token bills that turn inference into a scaling risk. The hands-on shape is concrete: participants get a dedicated GPU, stand up vLLM, connect an agent to that endpoint, and then push concurrent traffic through the system until batching, KV-cache pressure, throughput limits, and latency tradeoffs become visible in metrics.

The connected Du'an Lightfoot people page makes the production framing sharper: Lightfoot is described as a Senior AI Engineer at Akamai Technologies, where AI work intersects with network engineering and infrastructure. That background matters because this session is not pitched as an agent-framework tutorial. It is about the layer underneath the agent: the GPU-backed serving stack, the scheduler, the cache, the observability surface, and the failure modes that only appear when multiple requests compete for the same inference server. In this page's evidence model, the official schedule supplies the confirmed World's Fair topic, while the connected YouTube, transcript, and slide pages supply adjacent public context for Lightfoot's agent-building vocabulary.

The related AI Engineer video, "Building Agents with Amazon Nova Act and MCP," should be treated as supporting context rather than a confirmed recording of this exact session. Its extracted, dense, and reconstructed slide pages point to application-level concepts such as tools, actions, environments, memory, autonomous systems, model-driven execution, Amazon Nova, and MCP. Read alongside those pages, this World's Fair workshop looks like the infrastructure counterpart to that agentic-systems material. A team can use Nova Act, MCP, tools, memory, and environment interaction to design the agent loop, but this session asks what happens when the agent's intelligence depends on a self-operated model server under real load.

The key synthesis is that "owning inference" expands the reliability boundary of an agent product. Once the team runs vLLM on a dedicated GPU, product behavior is shaped by continuous batching efficiency, KV-cache capacity, request concurrency, per-request latency targets, GPU utilization, and the quality of metrics available during tuning. The workshop's likely value is not just that attendees leave with working code; it is that they see the hidden coupling between agent design and inference operations. Tool-calling agents, autonomous workflows, and MCP-connected systems all become more operationally serious when their model-serving endpoint is a component the team must capacity-plan, observe, and optimize itself.

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

## Transcript Markdown
- [[youtube-wFTVEDYVJT0-transcript]] — full cached transcript markdown for the related YouTube source.

## Source-Derived Enrichment
This section is generated from all currently linked source material for the article: official schedule text, related video pages, cached transcripts, visible slide text, dense/reconstructed slide pages, and AI slide-classification audits.

### Source Signals
- `youtube-wFTVEDYVJT0` — 13,586 transcript words; 9 slide-derived text signals
- Transcript signals for `youtube-wFTVEDYVJT0`: nova, amazon, code, server, browser, able, open, click.
- Slide-derived themes for `youtube-wFTVEDYVJT0`: plan, execute, actions, achieve, specific, goals, agentic, tamera.
- Evidence links for `youtube-wFTVEDYVJT0`: [[youtube-wFTVEDYVJT0]], [[youtube-wFTVEDYVJT0-transcript]], [[youtube-wFTVEDYVJT0-slides]], [[youtube-wFTVEDYVJT0-dense-slides]], [[youtube-wFTVEDYVJT0-reconstructed-slides]]

### Article Use
Use these source signals to refine the synopsis, topic links, people/company context, and method notes. If a source is a related external video rather than an exact official recording, keep it framed as supporting evidence.
## Slides
- Source video: `youtube-wFTVEDYVJT0`
- Slide deck: [[youtube-wFTVEDYVJT0-dense-slides|Dense Slides: Building Agents with Amazon Nova Act and MCP - Du'An Lightfoot, Amazon (Full Workshop)]] — 6 visible slide image(s).
![[assets/dense-slides/wFTVEDYVJT0/slide-001.jpg]]
![[assets/dense-slides/wFTVEDYVJT0/slide-002.jpg]]
![[assets/dense-slides/wFTVEDYVJT0/slide-003.jpg]]
- Additional slide evidence: [[youtube-wFTVEDYVJT0-slides|Slides: Building Agents with Amazon Nova Act and MCP - Du'An Lightfoot, Amazon (Full Workshop)]], [[youtube-wFTVEDYVJT0-reconstructed-slides|Reconstructed Slides: Building Agents with Amazon Nova Act and MCP - Du'An Lightfoot, Amazon (Full Workshop)]]
- Slide-derived themes for `youtube-wFTVEDYVJT0`: plan, execute, actions, achieve, specific, goals, agentic, tamera.
