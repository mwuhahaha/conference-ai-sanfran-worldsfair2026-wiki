---
title: 'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt2'
category: talks
date: '2026-06-30'
time: '1:55pm-2:15pm'
track: Sandbox & Platform Engineering
room: Track 1
speakers:
  - Abhishek Bhardwaj
sourceLabels:
  - Official conference schedule
  - Public YouTube metadata
last_auto_summarized: '2026-07-18T01:27:43.295Z'
scheduleTrack: Sandbox & Platform Engineering
scheduleRoom: Track 1
scheduleLabels:
  - Sandbox & Platform Engineering
  - Track 1
  - session
  - confirmed
---
# From fork() to Fleet: Designing an Agent Sandbox Cloud Pt2

## Conference Context
- Date/time: 2026-06-30 · 1:55pm-2:15pm
- Track/room: Sandbox & Platform Engineering · Track 1
- Speaker(s): Abhishek Bhardwaj
- Session type/status: session · confirmed

- Track: Sandbox & Platform Engineering
- Room: Track 1
- Session type: session
- Status: confirmed

## Session Description
Sandboxes unleash agents by giving them secure, fully functional computers where they can tackle diverse tasks with minimal setup. This talk explores the architectural challenges of building an agent sandbox cloud. We compare runtime isolation technologies and their trade-offs, examine persistence and storage as the next major unlock for agent capabilities, and discuss the key decisions involved in orchestrating and scaling sandboxes.

## Summary
Abhishek Bhardwaj’s session examines the transition from creating one isolated execution environment with fork-like primitives to operating a secure, persistent fleet of computers for AI agents. The exact session now has a dedicated official recording, a 7,738-word transcript, and 15 visible slide images, making it the primary evidence for the talk rather than relying on the earlier Arrakis presentation. Bhardwaj’s role building RL and agent infrastructure at [[openai|OpenAI]] places the discussion where agent training, tool use, and production execution meet: [[coding-agents]] and other tool-using systems need enough freedom to write and run code, install dependencies, inspect files, and retain artifacts, while the platform must prevent those workloads from escaping into the host or interfering with one another.

The architectural problem spans several connected layers. Runtime isolation determines the boundary between host and guest behavior, including the use of processes, Linux namespaces, containers, syscalls, and kernel-level protection. Persistence introduces mounts, filesystem snapshots, and durable storage so an agent can continue a long-running task instead of losing its environment after each execution, but retained state also expands the security and lifecycle responsibilities of the platform. Fleet orchestration then has to turn those individual sandboxes into a dependable service that can create, schedule, monitor, recover, and scale many environments without weakening isolation. In that sense, [[ai-sandboxes]] are not merely code runners: they are a platform control plane whose capability model, storage design, and attack surface directly shape [[agent-security]].

The linked Arrakis recording and reconstructed slide sets remain valuable supporting context because they expose the implementation vocabulary behind the same design space—process cloning, namespaces, mounts, snapshots, userspace behavior, syscalls, kernel boundaries, and attack surfaces—but they are not evidence for the precise contents of this scheduled session. Taken together, the official World’s Fair recording and the related systems material frame the sandbox cloud as foundational agent infrastructure: a way to provide reproducible computers with durable working state while preserving strong boundaries and fleet-level reliability for production agent workflows, training, and [[agent-evaluations]].

## Synthesis
### Transcript-Backed Summary
The talk argues that agent sandboxes should be treated as a cloud primitive built to run untrusted code securely, reliably, and at scale, not just as a convenience wrapper around local execution. It compares fork/exec, containers, gVisor, and micro VMs, and concludes that hardware virtualization is the cleanest security boundary even though it introduces performance and device-sharing tradeoffs. The second half argues that durable disk persistence is the next major unlock for agents, because incremental snapshotting, fast restore, and snapshot-aware scheduling let long-running tasks survive failures, support backtracking search, and scale across a fleet.

### Key Takeaways
- Sandbox clouds need to balance runtime isolation, persistence, and orchestration because research cares most about throughput while product cares most about latency, and both need reliability and security.
  - Evidence: "There are many many parts of a sandbox cloud, but we'll specifically focus on runtime. So, how can we run uh sandbox on one node securely?"
- Containers help, but they still share the host kernel, so they are only a partial answer to hostile or buggy agent code.
  - Evidence: "So, yeah. The this is the fight like to sum it up like containers interact with the same host kernel, so they do they do have some protections, but at the end it's the same host kernel they're trying to attack, right?"
- Hardware virtualization strengthens the security boundary, but the speaker is explicit that the gain comes with a performance penalty from guest-host context switching.
  - Evidence: "We'll see how that works, but that is a key trade-off here. There's a performance penalty you pay every time the CPU is switching back and forth between these two modes."
- Disk persistence is presented as the next unlock for agent sandboxes because it turns short-lived computers into durable workspaces that can recover from failures.
  - Evidence: "Yeah, so that's the persistence part of the presentation. And so, the one takeaway I want you guys to think about is I think storage is the next unlock here."
- Orchestration can become snapshot-aware, using lineage and node state to place restores where they are cheapest and fastest.
  - Evidence: "And so, here is a way where we can use snapshot rich restore for better orchestration. So, remember we discussed that a snapshot can have a lineage of many, many layers."

### Claims From The Talk
- The speaker argues that sandbox clouds have to serve different workloads in research and product, with research optimizing for throughput and product optimizing for latency, while both demand reliability and security. (`explicit`)
  - Evidence: "We've discussed why sandboxes are important in both research and product. Uh but they have slightly different needs."
- He argues that containers improve isolation and resource control, but they still run native processes on the host and therefore leave the host kernel reachable. (`explicit`)
  - Evidence: "Um if you've seen the previous diagrams, uh there's the the fundamental problem with containers is that they're still native processes uh running on the host."
- He argues that hardware virtualization gives a stronger security boundary because a compromised guest can still be contained from the host at the CPU level. (`explicit`)
  - Evidence: "Uh so, turns out Linux provides a very very nice thing called virtualization, uh which is hardware powered at the CPU level."
- He argues that checkpointing sandbox state enables backtracking search and long-running exploration, including Monte Carlo tree search style rollouts over many days. (`explicit`)
  - Evidence: "Like so, if your harness wants to explore multiple like solutions or sample spaces, it can actually checkpoint the sandbox state and it can like do a Monte Carlo like tree search and like go ahead and like backtrack, checkpoint again."
- He argues that orchestration can use snapshot lineage to route restores to nodes that already have the needed layers, reducing download work and speeding recovery. (`explicit`)
  - Evidence: "And so, here is a way where we can use snapshot rich restore for better orchestration. So, remember we discussed that a snapshot can have a lineage of many, many layers."

### Topics Covered
- [[ai-sandboxes|Agent sandboxing]] — How to execute agent tool calls and untrusted code securely for product and research workloads.
- **Hardware virtualization** — Using CPU-level virtualization to isolate hostile guest code from the host kernel.
- [[inference-engineering|Disk persistence]] — Saving sandbox state so long-running tasks can resume after failure or backtrack across branches.
- [[ai-sandboxes|Snapshot-aware orchestration]] — Using load, snapshot lineage, and restore cost to place sandboxes efficiently across a fleet.

### Tools And Named Systems
- [[gvisor|gVisor]] — User-space kernel-based sandboxing layer discussed as an intermediate isolation option.
- [[qemu|QEMU]] — Virtual machine monitor used as the classic Linux virtualization path in the speaker's comparison.
- [[crosvm|CrosVM]] — Rust-based VMM presented as an early example of the newer micro VM approach.
- [[firecracker|Firecracker]] — Rust-based VMM cited as a micro VM implementation used in serverless contexts.
- [[cloud-hypervisor|Cloud Hypervisor]] — General-purpose VMM named as part of the newer micro VM ecosystem.
- [[virtio|virtio]] — Paravirtualized device interface used for efficient guest-host communication.
- [[kvm|KVM]] — Linux hypervisor API used by VMMs to launch and manage guests.
- [[vsock|Vsock]] — Guest-host communication channel used between the sandbox and the host.
- [[s3|S3]] — Object storage mentioned as a backing layer for persistent sandbox storage.

### Novel Concepts And Methods
- **Three-pillar sandbox design** — Separate sandbox design around runtime isolation, persistence, and orchestration rather than treating execution as a single problem.
- **Seccomp filtering** — Reduce kernel attack surface with syscall filtering and argument constraints, while accepting that unknown workloads can break the filter.
- **Hardware-isolated guest execution** — Move untrusted execution behind a hardware virtualization boundary so guest compromise does not directly imply host compromise.
- **Incremental copy-on-write snapshots** — Store only changed disk extents between versions so snapshot and restore stay cheap enough for frequent use.
- **Snapshot-aware placement** — Route restores toward nodes that minimize snapshot-layer download cost.
- **Hybrid warm-start strategy** — Use a warm pool together with memory snapshots to cut startup latency without keeping too many idle resources hot.

### Open Questions
- **What is the best way to support GPU access in micro VMs without giving up the security boundary the speaker prefers?** — GPU access is important for some agent workloads, but the talk treats it as one of the hardest gaps in the micro VM approach.
- **How can snapshotting stay incremental, cheap, and fast enough when sandbox state grows to gigabytes and snapshots are taken frequently?** — The speaker presents low-cost incremental snapshotting as necessary for scale and for keeping the user experience responsive.
- **What storage architecture best delivers POSIX-like behavior and durable persistence on top of object storage without hurting sandbox performance?** — The talk argues that persistence is central, but also notes that the backing storage and filesystem abstraction are still design-sensitive.
- **When should a platform use a warm pool, a memory snapshot, or a hybrid of the two for sandbox startup?** — Startup strategy directly affects latency, idle resource cost, and fleet efficiency.

### Derived Links And Source Material
- [[youtube-OqM67QG_Ikk-transcript]] — dedicated official recording transcript.
- [[youtube-OqM67QG_Ikk]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/OqM67QG_Ikk--2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt2.json`.

### Speaker Context
- No speaker profile is attached in the official schedule data.

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[abhishek-bhardwaj]]

## Slide Evidence
- Slide-only cropped deck: [[youtube-wsFd22SL1s8-dense-slides]] (42 viable slide images).
- Related slide/OCR pages:
- [[youtube-wsFd22SL1s8-dense-slides]]
- [[youtube-wsFd22SL1s8-reconstructed-slides]]
- [[youtube-wsFd22SL1s8-slides]]
- Slide-derived terms: `namespace`, `arrakis`, `process`, `containers`, `kernel`, `container`, `linux`, `code`, `chatgpt`, `clone`, `mount`, `attack`, `snapshot`, `server`, `python`, `userspace`, `version`, `syscall`

## Official YouTube Recording
- [[youtube-OqM67QG_Ikk|From fork() to Fleet: Designing an Agent Sandbox Cloud — Abhishek Bhardwaj, OpenAI]] — official AI Engineer YouTube recording published 2026-07-13.
- Evidence status: [[youtube-OqM67QG_Ikk-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-OqM67QG_Ikk]] - dedicated official event recording.
- [[youtube-OqM67QG_Ikk-transcript]] - dedicated official recording transcript.
- [[youtube-wsFd22SL1s8]] - supporting context; not the exact session recording.

- Source video: `youtube-OqM67QG_Ikk`
- Slide deck: [[youtube-OqM67QG_Ikk-slides|Slides: From fork() to Fleet: Designing an Agent Sandbox Cloud — Abhishek Bhardwaj, OpenAI]] — 15 visible slide image(s).
![[assets/slides/OqM67QG_Ikk/slide-001.jpg]]
![[assets/slides/OqM67QG_Ikk/slide-002.jpg]]
![[assets/slides/OqM67QG_Ikk/slide-003.jpg]]
- Slide-derived themes for `youtube-OqM67QG_Ikk`: engineering, sandbox, platform, track, july, security, fork, fleet.
- Source video: `youtube-wsFd22SL1s8`
- Slide deck: [[youtube-wsFd22SL1s8-dense-slides|Dense Slides: Arrakis: How To Build An AI Sandbox From Scratch - Abhishek Bhardwaj, OpenAI]] — slide evidence page.
- Additional slide evidence: [[youtube-wsFd22SL1s8-slides|Slides: Arrakis: How To Build An AI Sandbox From Scratch - Abhishek Bhardwaj, OpenAI]], [[youtube-wsFd22SL1s8-reconstructed-slides|Reconstructed Slides: Arrakis: How To Build An AI Sandbox From Scratch - Abhishek Bhardwaj, OpenAI]]
- Slide-derived themes for `youtube-wsFd22SL1s8`: clone, flask, project, code, create, scratch, systems, chat.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/OqM67QG_Ikk.txt` (7,738 words).

## Transcript Markdown
- [[youtube-OqM67QG_Ikk-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/OqM67QG_Ikk.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-OqM67QG_Ikk` — 7,738 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-OqM67QG_Ikk`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-OqM67QG_Ikk`: kernel, many, system, code, host, guest, block, running.
- Slide-derived themes for `youtube-OqM67QG_Ikk`: engineering, sandbox, platform, track, july, security, fork, fleet.
- Evidence links for `youtube-OqM67QG_Ikk` (primary event evidence): [[youtube-OqM67QG_Ikk]], [[youtube-OqM67QG_Ikk-transcript]], [[youtube-OqM67QG_Ikk-slides]]
- `youtube-wsFd22SL1s8` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-wsFd22SL1s8`: clone, flask, project, code, create, scratch, systems, chat.
- Evidence links for `youtube-wsFd22SL1s8` (supporting context only): [[youtube-wsFd22SL1s8]], [[youtube-wsFd22SL1s8-slides]], [[youtube-wsFd22SL1s8-dense-slides]], [[youtube-wsFd22SL1s8-reconstructed-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
