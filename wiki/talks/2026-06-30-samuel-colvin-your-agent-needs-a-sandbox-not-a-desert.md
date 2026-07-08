---
title: "Your agent needs a sandbox, not a desert"
category: "talks"
date: "2026-06-30"
time: "12:05pm-12:25pm"
track: "Sandbox & Platform Engineering"
room: "Track 1"
speakers: ["Samuel Colvin"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Sandbox & Platform Engineering"
scheduleRoom: "Track 1"
scheduleLabels: ["Sandbox & Platform Engineering", "Track 1", "session", "confirmed"]
---
# Your agent needs a sandbox, not a desert

## Official Schedule Context
- Date/time: 2026-06-30 · 12:05pm-12:25pm
- Track/room: Sandbox & Platform Engineering · Track 1
- Speaker(s): Samuel Colvin
- Session type/status: session · confirmed

## Schedule Labels
- Track: Sandbox & Platform Engineering
- Room: Track 1
- Session type: session
- Status: confirmed

## Official Description
Everyone agrees agents need code execution. That agreement lasts right up until you ask how to do

it. The default answer is usually something like "My agent needs a full Linux VM to succeed". That's

a very convenient answer for sandbox providers, but I think it's often incorrect. In many real-world

agent workflows, the model does not need a whole computer. It does not need arbitrary packages,

shell access, CPython, node, let alone `awk` `sed` and `gcc`. It needs a small amount of safe,

expressive compute: enough to write code, call tools, and keep intermediate state out of the context

window. That is the idea behind Monty: a minimal Python interpreter, written in Rust, designed

specifically for running code written by agents. In this talk, I'll argue that for a surprisingly

large class of agent systems, a curated set of tools in a custom runtime is better than a full

sandbox. Not because full sandboxes are bad, but because they solve a much larger problem than most

embedded agents actually have. And you pay for that mismatch in complexity, cost, operational pain,

and 100,000X higher latency. Sandboxes are great, but there's such a thing as too much sand - in

many scenarios the constraints and limitations of a custom built, minimal sandbox are a feature, not

a bug.

## Related YouTube Video
[MCP is all you need — Samuel Colvin, Pydantic](https://www.youtube.com/watch?v=bmWZk9vTze0) (speaker-match related prior/adjacent AI Engineer video; captions: English auto-captions).

## Transcript Status
Related video transcript availability: English auto-captions. Treat this as supporting context, not a recording of this exact scheduled session unless later confirmed. Not fetched yet.

## People
- [[samuel-colvin]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.
## Supporting Slides
- [[youtube-bmWZk9vTze0-slides]] — extracted from the related public AI Engineer video.
## Slide Evidence
- Slide-only cropped deck: [[youtube-bmWZk9vTze0-dense-slides]] (1 viable slide images).
- Related slide/OCR pages:
- [[youtube-bmWZk9vTze0-dense-slides]]
- [[youtube-bmWZk9vTze0-reconstructed-slides]]
- [[youtube-bmWZk9vTze0-slides]]
- Slide-derived terms: `request`, `world`, `tool`, `response`, `call`, `sfair`, `microsoft`, `server`, `pydantic`, `smol`, `sampling`, `client`, `been`, `chat`, `toolcall`, `text`, `return`, `async`
