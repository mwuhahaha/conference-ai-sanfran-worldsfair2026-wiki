---
title: 'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt 1'
category: talks
date: '2026-06-30'
time: '1:30pm-1:50pm'
track: Sandbox & Platform Engineering
room: Track 1
speakers:
  - Abhishek Bhardwaj
sourceLabels:
  - Official conference schedule
  - Public YouTube metadata
last_auto_summarized: '2026-07-06T07:15:57.053Z'
---
# From fork() to Fleet: Designing an Agent Sandbox Cloud Pt 1

## Summary
Abhishek Bhardwaj's session is about the infrastructure that lets coding and computer-use agents operate inside real, stateful computers without handing them the host machine. The connected Arrakis slide material grounds the talk in a bottom-up sandbox design: starting from process creation with `fork()`/`clone`, then layering Linux namespaces, mounts, containers, syscall boundaries, userspace/kernel separation, snapshots, and attack-surface reduction into an environment an agent can safely use. That makes the session less a generic cloud-scaling talk than a concrete tour of how low-level Linux isolation becomes an agent platform primitive.

The platform question is how to turn those primitives into a fleet of useful sandboxes: agents need filesystems, Python processes, servers, networked tools, persistence, and replayable state, while operators need hard boundaries around untrusted code and predictable orchestration at scale. Bhardwaj's OpenAI agent-infrastructure background and the linked Arrakis deck point to the key design tensions: containers versus stronger runtime isolation, snapshots as both product capability and operational control, storage as the next unlock for long-running agent work, and orchestration choices that decide whether sandboxes feel like disposable processes or durable computers for agents.

## Official Schedule Context
- Date/time: 2026-06-30 · 1:30pm-1:50pm
- Track/room: Sandbox & Platform Engineering · Track 1
- Speaker(s): Abhishek Bhardwaj
- Session type/status: session · confirmed

## Official Description
Sandboxes unleash agents by giving them secure, fully functional computers where they can tackle

diverse tasks with minimal setup. This talk explores the architectural challenges of building an

agent sandbox cloud. We compare runtime isolation technologies and their trade-offs, examine

persistence and storage as the next major unlock for agent capabilities, and discuss the key

decisions involved in orchestrating and scaling sandboxes.

## Related YouTube Video
[Arrakis: How To Build An AI Sandbox From Scratch - Abhishek Bhardwaj, OpenAI](https://www.youtube.com/watch?v=wsFd22SL1s8) (speaker-match related prior/adjacent AI Engineer video; captions: English auto-captions).

## Transcript Status
Related video transcript availability: English auto-captions. Treat this as supporting context, not a recording of this exact scheduled session unless later confirmed. Not fetched yet.

## People
- [[abhishek-bhardwaj]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.
## Supporting Slides
- [[youtube-wsFd22SL1s8-slides]] — extracted from the related public AI Engineer video.
## Slide Evidence
- Slide-only cropped deck: [[youtube-wsFd22SL1s8-dense-slides]] (42 viable slide images).
- Related slide/OCR pages:
- [[youtube-wsFd22SL1s8-dense-slides]]
- [[youtube-wsFd22SL1s8-reconstructed-slides]]
- [[youtube-wsFd22SL1s8-slides]]
- Slide-derived terms: `namespace`, `arrakis`, `process`, `containers`, `kernel`, `container`, `linux`, `code`, `chatgpt`, `clone`, `mount`, `attack`, `snapshot`, `server`, `python`, `userspace`, `version`, `syscall`
