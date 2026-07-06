---
title: "Kubernetes Is Not Your Sandbox"
category: "talks"
date: "2026-06-30"
time: "11:40am-12:00pm"
track: "Sandbox & Platform Engineering"
room: "Track 1"
speakers: ["Ivan Burazin"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
---

# Kubernetes Is Not Your Sandbox

## Official Schedule Context
- Date/time: 2026-06-30 · 11:40am-12:00pm
- Track/room: Sandbox & Platform Engineering · Track 1
- Speaker(s): Ivan Burazin
- Session type/status: session · confirmed

## Official Description
Teams are reaching for Kubernetes to run agent sandboxes, and it's the wrong tool. Kubernetes is

built to keep things alive and hold them in a steady state. A sandbox is born, forked, and killed

before any of that machinery catches up.  The mismatch compounds because the sandbox keeps gaining

requirements without shedding any. In eighteen months it went from a fast code-snippet runner, to a

stateful box for long-running agents, to ten thousand ephemeral environments that fork for RL

rollouts and die in under a second. It has to be all of those at once, a contradiction set no

orchestrator was designed to hold.   The cost shows up the moment you measure it. We ran the same

50-action bug-fix trajectory across five stacks and got a 12x spread: 12.9s on the fastest, 161.5s

on the slowest. The gap isn't compute, it's lifecycle overhead per action. We name every stack and

explain the mechanism behind each number. wdyt?

## Related YouTube Video
[AX is the only Experience that Matters - Ivan Burazin, Daytona](https://www.youtube.com/watch?v=e9sLVMN76qU) (speaker-match related prior/adjacent AI Engineer video; captions: English auto-captions).

## Transcript Status
Related video transcript availability: English auto-captions. Treat this as supporting context, not a recording of this exact scheduled session unless later confirmed. Not fetched yet.

## People
- [[ivan-burazin]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.
## Supporting Slides
- [[youtube-e9sLVMN76qU-slides]] — extracted from the related public AI Engineer video.
