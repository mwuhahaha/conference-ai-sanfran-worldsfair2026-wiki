---
title: The Search Engine for the Agentic Web
category: talks
date: '2026-06-29'
time: '11:40am-12:00pm'
track: Search & Retrieval
room: Track 3
speakers:
  - Will Bryk
sourceLabels:
  - Official conference schedule
  - Public YouTube metadata
last_auto_summarized: '2026-07-06T07:14:43.170Z'
scheduleTrack: "Search & Retrieval"
scheduleRoom: "Track 3"
scheduleLabels: ["Search & Retrieval", "Track 3", "session", "confirmed"]
---
# The Search Engine for the Agentic Web

## Official Schedule Context
- Date/time: 2026-06-29 · 11:40am-12:00pm
- Track/room: Search & Retrieval · Track 3
- Speaker(s): Will Bryk
- Session type/status: session · confirmed

## Summary
Will Bryk's World's Fair session treats search as a core runtime dependency for agentic systems, not as a human-facing results page with an API wrapped around it. The official session description is explicit about the failure mode: an agent that performs dozens of sequential searches cannot tolerate one-second human-search latency multiplied across a workflow, and it also needs semantic precision, structured outputs, and retrieval modes that range from sub-200ms lookups to deeper multi-step research. The connected people page grounds the speaker context: Bryk is the co-founder and CEO of Exa, the AI-native search company represented in the World's Fair 2026 roster, so the talk sits at the intersection of search architecture, agent infrastructure, and product usage patterns at companies named in the schedule such as Cursor, Notion, HubSpot, and Lovable.

The related AI Engineer YouTube video and slide pages should be treated as supporting context rather than a confirmed recording of this exact session. They still sharpen the likely technical center of gravity. The linked Exa material is titled around Neural RAG and shows agent-oriented search examples, including Python/agent code, console/debug output, GitHub-agent references, and slide-derived terms such as `agent.py`, `github_agent.py`, `search`, `output`, `debug`, `console`, `terminal`, and `information`. That evidence points to search as a programmable component inside agent loops: something an agent calls, inspects, debugs, and chains into downstream reasoning, rather than a static list of blue links. The reconstructed and dense slide decks add a useful caution layer too: some details are OCR- or slide-derived, so they are best used to explain the adjacent Exa/Neural RAG context while keeping the official schedule claims separate from inferred synthesis.

Taken together, the page frames agentic search as an evaluation and systems-design problem. The scheduled talk argues that today's search benchmarks can miss what matters when software, not a person, consumes the results: latency budgets across repeated calls, precision under semantic intent, result structure suitable for tool use, and reliability across short retrieval and longer research workflows. The connected transcript map reinforces that no exact normalized title match was found for a session recording, so the strongest current summary is evidence-layered: official schedule for the World's Fair claim, Will Bryk/Exa pages for speaker and company context, and the related Neural RAG slides/video for concrete examples of how Exa presents search inside AI-agent workflows.

## Schedule Labels
- Track: Search & Retrieval
- Room: Track 3
- Session type: session
- Status: confirmed

## Official Description
Every search API claiming to be "built for AI" is actually Google with a wrapper. That's a problem,

because AI agents don't search like humans. A human waits 1 second for a result. An agent making 50

sequential searches at 1 second each creates a 50-second lag. That kills the product. And latency is

just one dimension: agents need semantic precision, structured outputs, and a range that spans

sub-200ms real-time retrieval all the way to multi-step deep research. No human-facing search engine

was ever designed to do that. Will Bryk, CEO of Exa, shares what he learned building a search engine

from scratch for AI. He'll cover the architectural decisions behind Exa's latency spectrum, what

real usage patterns look like across companies like Cursor, Notion, HubSpot, and Lovable, and why

the benchmarks the field relies on today are dangerously inadequate for evaluating agentic search.

The bigger argument: search is becoming the most critical primitive in AI infrastructure, and almost

no one is building it right.

## Related YouTube Video
[Building a Smarter AI Agent with Neural RAG - Will Bryk, Exa.ai](https://www.youtube.com/watch?v=xnXqpUW_Kp8) (speaker-match related prior/adjacent AI Engineer video; captions: English auto-captions).

## Transcript Status
Related video transcript availability: English auto-captions. Treat this as supporting context, not a recording of this exact scheduled session unless later confirmed. Not fetched yet.

## People
- [[will-bryk]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.
## Supporting Slides
- [[youtube-xnXqpUW_Kp8-slides]] — extracted from the related public AI Engineer video.
## Slide Evidence
- Slide-only cropped deck: [[youtube-xnXqpUW_Kp8-dense-slides]] (4 viable slide images).
- Related slide/OCR pages:
- [[youtube-xnXqpUW_Kp8-dense-slides]]
- [[youtube-xnXqpUW_Kp8-reconstructed-slides]]
- [[youtube-xnXqpUW_Kp8-slides]]
- Slide-derived terms: `https`, `microsoft`, `agent.py`, `python`, `smol`, `search`, `output`, `info`, `none`, `explorer`, `oerv`, `github_agent.py`, `problems`, `debug`, `console`, `terminal`, `print`, `information`
