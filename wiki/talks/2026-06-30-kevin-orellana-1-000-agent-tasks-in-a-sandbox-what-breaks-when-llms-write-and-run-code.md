---
title: "1,000 Agent Tasks in a Sandbox: What Breaks When LLMs Write and Run Code"
category: "talks"
date: "2026-06-30"
time: "2:25pm-2:45pm"
track: "Sandbox & Platform Engineering"
room: "Track 1"
speakers: ["Kevin Orellana"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Sandbox & Platform Engineering"
scheduleRoom: "Track 1"
scheduleLabels: ["Sandbox & Platform Engineering", "Track 1", "session", "confirmed"]
---
# 1,000 Agent Tasks in a Sandbox: What Breaks When LLMs Write and Run Code

## Official Schedule Context
- Date/time: 2026-06-30 · 2:25pm-2:45pm
- Track/room: Sandbox & Platform Engineering · Track 1
- Speaker(s): Kevin Orellana
- Session type/status: session · confirmed

## Schedule Labels
- Track: Sandbox & Platform Engineering
- Room: Track 1
- Session type: session
- Status: confirmed

## Official Description
We ran 1,000 automated tasks through a production code interpreter sandbox — file I/O, package

installs, data analysis, ML training, binary downloads, multi-language execution — and tracked every

failure. 88% passed. The other 12% revealed 18 distinct failure modes that no unit test would catch:

binary encoding corruption in the transport layer, null bytes silently truncating file downloads,

pip blocked by network isolation with no useful error, and path traversal inputs accepted without

validation. This talk walks through the experiment design, the findings ranked by severity, and what

we changed. If you are building or operating sandboxed execution for AI agents, these are the bugs

waiting for your customers to find first.

## Related YouTube Video
No related AI Engineer channel video found yet.

## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## People
- [[kevin-orellana]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.
