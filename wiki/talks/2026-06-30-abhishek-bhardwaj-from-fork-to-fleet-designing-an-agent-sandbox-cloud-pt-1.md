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
last_auto_summarized: '2026-07-18T01:26:31.294Z'
scheduleTrack: Sandbox & Platform Engineering
scheduleRoom: Track 1
scheduleLabels:
  - Sandbox & Platform Engineering
  - Track 1
  - session
  - confirmed
---
# From fork() to Fleet: Designing an Agent Sandbox Cloud Pt 1

## Conference Context
- Date/time: 2026-06-30 · 1:30pm-1:50pm
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
With a dedicated official recording and 7,738-word transcript now attached, Abhishek Bhardwaj's session can be read as a bottom-up account of turning Linux process isolation into infrastructure for agents. Bhardwaj, an OpenAI Member of Technical Staff working on RL and agent infrastructure, begins near the `fork()` and `clone` boundary and follows the layers required to make an execution environment safe and useful: processes, namespaces, mounts, containers, syscall boundaries, userspace/kernel separation, host-versus-guest controls, snapshots, and deliberate reduction of the kernel attack surface. The result is not merely a restricted code runner, but a computer-like sandbox where an agent can create files, run Python processes and servers, install or invoke tools, and manipulate persistent artifacts without receiving direct access to the host.

The “fleet” problem begins once that environment must become a dependable platform primitive. Operators must choose between container density and stronger isolation, coordinate large numbers of short- and long-lived environments, constrain untrusted code, and make sandbox state reproducible enough to restore, replay, or discard. Persistence and storage are therefore central capabilities rather than secondary conveniences: they determine whether coding and computer-use agents behave like stateless jobs or can continue work across steps and sessions. The linked Arrakis deck supplies supporting detail about the lower-level construction model, while the official recording anchors this session's claims about orchestration, security, snapshots, and the path from one sandboxed process to a scalable agent cloud.

## Synthesis
### Transcript-Backed Summary
The talk argues that agent sandboxes should be treated as a cloud primitive: once models can call tools to solve verifiable tasks, the main systems problem becomes giving them a secure computer that is still fast and flexible enough for real work. Abhishek walks up the isolation stack from fork/exec to containers and gVisor to hardware virtualization, concluding that micro VMs are the strongest default boundary because they keep host-kernel compromise much harder. He then makes persistence the next major unlock, showing how incremental snapshotting, restore, and always-on disk state let long-running agents recover from failures, backtrack, and keep building over days. The practical consequence is a snapshot-aware sandbox fleet where security, durability, and low-latency orchestration are designed together rather than bolted on later.

### Key Takeaways
- Use micro VMs from the start if you need a secure whole-Linux-box sandbox.
  - Evidence: "Just please use micro VMs from the start. And then if it doesn't work, tell me and then we can talk about other things."
- Design for incremental, fast snapshotting so the harness can save state often.
  - Evidence: "The snapshotting API itself should be very, very cheap and fast so the model and the harness can keep snapshotting and exploring like very fast."
- Treat storage as the next unlock for longer-horizon agents.
  - Evidence: "Yeah, so that's the persistence part of the presentation. And so, the one takeaway I want you guys to think about is I think storage is the next unlock here."
- Periodic checkpoints let you restore the exact sandbox state on another node after failure or upgrade.
  - Evidence: "If you keep checkpointing it periodically and if the node fails or the cluster fails, you can now restore the sandbox in the exact checkpoint state on another node."
- Make orchestration snapshot-aware so restore placement accounts for layer locality.
  - Evidence: "You can actually like smartly route you to a node which has to download the least amount of stuff."

### Claims From The Talk
- Giving models code-execution capability is the key unlock for verifiable-reward tasks like code and math. (`explicit`)
  - Evidence: "The model needs something more and the key unlock was that given the model tool calling capability or a way to execute code the model gets these verifiable reward questions around code and math correctly."
- A sandbox is needed to run untrusted code securely without exposing the host or other tenants. (`explicit`)
  - Evidence: "Thus, this is where the sandbox come comes in. We need the sandbox to run this untrusted code and ensure that it can do its work, but it shouldn't be able to exploit any vulnerabilities and get root on your system."
- Containers and gVisor reduce risk but still leave a route to the host kernel. (`explicit`)
  - Evidence: "So, you can still get to the host kernel, right? So, yeah, the chain is harder here because it's a two-step chain compared to the others, but it's still reachable."
- Hardware virtualization is a stronger boundary, but it pays a performance penalty when switching between guest and host. (`explicit`)
  - Evidence: "We'll see how that works, but that is a key trade-off here. There's a performance penalty you pay every time the CPU is switching back and forth between these two modes."
- Persistence lets sandboxes checkpoint, restore, and keep long-running tasks alive across failures. (`explicit`)
  - Evidence: "The persistence has now let you reliably run sandboxes across your fleet, right? So, it's a very good way to scale and be reliable."
- Snapshot lineage can guide the scheduler to nodes that need the least data to restore. (`explicit`)
  - Evidence: "So, you can use like snapshot with orchestration to just have faster like uh uh creates and even just more reliable uh uh like orchestration."

### Topics Covered
- **Agent sandbox cloud** — A fleet of secure sandboxes that runs model tool calls for research and product.
- [[inference-engineering|Runtime isolation]] — The choice of isolation primitive for a single sandboxed workload.
- [[ai-sandboxes|Micro VMs]] — Hardware-isolated guest machines with smaller VMMs and stronger boundaries.
- [[ai-sandboxes|Disk persistence]] — Saved sandbox state that survives failures and long tasks.
- [[ai-sandboxes|Snapshot-aware orchestration]] — Placement logic that uses snapshot lineage and node state.

### Tools And Named Systems
- **seccomp** — A syscall filter used to shrink the kernel attack surface.
- [[gvisor|gVisor]] — A user-space kernel boundary that intercepts syscalls.
- [[qemu|QEMU]] — The traditional VMM mentioned as the baseline for Linux virtualization.
- [[kvm|KVM]] — The Linux hypervisor interface that VMMs call to start guests.
- [[crosvm|CrosVM]] — The Rust-based VMM described as the first of the newer wave.
- [[firecracker|Firecracker]] — The Rust-based VMM forked from CrosVM for serverless workloads.
- [[cloud-hypervisor|Cloud Hypervisor]] — The more general Rust-based VMM used in micro VM stacks.
- [[virtio|virtio]] — The paravirtualized device protocol for guest-host I/O.
- [[vsock|Vsock]] — The guest-host socket used for sandbox communication.
- **NBD** — A block-device interface used to expose persisted storage to the sandbox.

### Novel Concepts And Methods
- **Verifiable-reward tool calling** — Train or run a model by letting it request code execution and grading the result.
- **Namespaces and cgroups isolation** — Separate processes and cap their resource use with namespaces and cgroups.
- **Seccomp syscall filtering** — Reduce the syscall surface with filters that constrain allowed calls and arguments.
- **Hardware virtualization boundary** — Run guest kernels in a separate hardware context so host compromise is harder.
- **Paravirtualized device access** — Use virtualized devices like virtio so guest I/O can stay efficient.
- **Copy-on-write snapshotting** — Snapshot only changed disk blocks using copy-on-write and extent diffs.

### Open Questions
- **How can micro VMs expose GPU access without reopening a broad multi-tenant attack surface?** — GPU support is important enough that weak solutions can become the default fallback.
- **What snapshot granularity and scope should the platform standardize on for large-scale incremental saves?** — The cost and restore speed depend on whether you snapshot files, blocks, folders, or whole roots.
- **How can always-on persistence stay performant when it is backed by object storage and a tiered cache?** — The talk points to an object-storage-backed filesystem path, but the performance shape is still a design problem.

### Derived Links And Source Material
- [[youtube-OqM67QG_Ikk-transcript]] — dedicated official recording transcript.
- [[youtube-OqM67QG_Ikk]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/OqM67QG_Ikk--2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1.json`.

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
## Attendance Visibility
No high-confidence attendance icon signal is shown for this talk. The sampled video evidence was either low confidence, source-proxy-only, or did not expose a clear audience view.

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
