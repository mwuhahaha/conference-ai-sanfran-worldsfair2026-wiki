---
title: "Agentic Security: Permissions, Provenance, and the Agent Supply Chain"
category: "talks"
date: "2026-06-29"
time: "2:25pm-2:45pm"
track: "Security"
room: "Track 5"
speakers: ["Steve Yegge"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Security"
scheduleRoom: "Track 5"
scheduleLabels: ["Security", "Track 5", "sponsor", "confirmed"]
---
# Agentic Security: Permissions, Provenance, and the Agent Supply Chain

## Conference Context
- Date/time: 2026-06-29 · 2:25pm-2:45pm
- Track/room: Security · Track 5
- Speaker(s): Steve Yegge
- Session type/status: sponsor · confirmed

- Track: Security
- Room: Track 5
- Session type: sponsor
- Status: confirmed

## Session Description
As AI agents move from demos into production engineering workflows, the security boundary shifts from code alone to the permissions, tools, prompts, dependencies, credentials, and orchestration layers that agents can touch. This talk frames agentic security broadly: least-privilege agent permissions, sandboxing and capability design, provenance for agent-generated changes, risks in agent/tool/package supply chains, and practical patterns for keeping autonomous coding and operational agents auditable and containable.

## Synthesis
### Transcript-Backed Summary
The talk argues that AI-coded systems should be treated as a new security frontier, not just a faster version of normal software development. The central mechanism is to break work into multiple passes and to separate correctness from security, then add layered checks from developer feedback to supply-chain inspection and agent supervision. The practical consequence is that teams need to harden code, dependencies, prompts, credentials, and autonomous agents together, because new attack surfaces such as slop squatting, prompt injection, and overprivileged agents are arriving faster than the old review model can handle.

### Key Takeaways
- Every bit of AI-generated code will need more security scrutiny than code has needed before.
  - Evidence: "So, so we're entering a world where everything you write, every bit of code that you generate is going to have to get far more security scrutiny than it's ever had before."
- Security issues should be surfaced immediately, at the developer's fingertips, because delay makes them easier to ignore.
  - Evidence: "The problem compounds over time. Yeah. So, you have to treat this class of vulnerabilities the way that Google treated their top vulnerabilities at the time, which is to surface them at the developer's fingertips."
- LLMs should be paired with security tools and supply-chain controls so they get help on the parts they are likely to miss.
  - Evidence: "Give them sneak, give them chain guard. And I still think there's a missing piece in this picture that I'll tell you about at the end."
- Security belongs at the beginning and end of the workflow, not as a single late-stage review.
  - Evidence: "Okay? These are all passes that go through your code. And I just want you to remember that security should be your first one and your last one."
- Agent deployments must avoid broad permissions, or one failure can cascade across the system.
  - Evidence: "Because otherwise your engineers are going to spin up or your non-engineers are going to spin up a bunch of agents with way too many permissions and then right as soon as a bear munches into the igloo, everyone's dead, right?"

### Claims From The Talk
- The speaker argues that security vulnerabilities cannot be treated like ordinary bugs because their harm compounds over time instead of fading after initial discovery. (`explicit`)
  - Evidence: "But if it gets to code review time, you're like, is it really worth it? Right? [snorts] And the problem, folks, is that that works for all classes of bugs except for security."
- He argues that LLMs should not be asked to do correctness and security work in the same pass, because they will do both poorly. (`explicit`)
  - Evidence: "Just because of this multipass painting a wall phenomenon, you got to give them one task at a time, which means you can't give them security at the same time as you give them correctness."
- He argues that security tools should be added as an extra review pass in the prompt so models can re-check their own output with multiple analyzers. (`explicit`)
  - Evidence: "Okay? Because what you do is you add it as a pass to the prompt that you give them for whatever they're doing and say one last thing to look at and have them run your security analysis all of the tools."
- He argues that security should be both the first and the last pass over code, not an afterthought. (`explicit`)
  - Evidence: "Okay? These are all passes that go through your code. And I just want you to remember that security should be your first one and your last one."
- He argues that agent systems need supervisors that inspect permissions and harden service accounts before agents are widely deployed with excessive access. (`explicit`)
  - Evidence: "So you got to have those supervisors. And so there's whole systems emerging here kind of can go out and go look at all of your things and say and start to like, you know, do do that hardening stuff like do they really need all those credentials on that service account really?"

### Topics Covered
- [[agent-security|agentic security]] — Security for AI-assisted coding, including how generated code changes the threat model.
- [[agent-security|slop squatting]] — The risk that hallucinated dependency names can be turned into malicious packages.
- [[agent-security|multi-pass code review]] — Treating security as a separate review pass from correctness and performance.
- [[agent-security|agent permissions]] — Restricting agent capabilities and permissions before autonomous systems are widely deployed.
- [[agent-security|prompt injection]] — Manipulating prompts or training data to redirect model behavior.
- [[agent-security|software supply chain]] — Inspecting software dependencies, images, and package sources for hidden vulnerabilities.

### Tools And Named Systems
- **Sneak** — A commercial security tool the speaker says found many vulnerabilities in his codebase and is easy to use.
- **Chain Guard** — A supply-chain service that provides pre-vetted images and updates them.
- [[fable|Fable]] — The model or assistant the speaker used for coding and hardening work.
- **Gas Town** — The agent system the speaker cites as doing useful autonomous work and enabling swarms.
- **Beads** — A task-tracking system the speaker uses to queue and coordinate agent work.
- [[claude|Claude]] — The assistant credited with assembling the slide deck.

### Novel Concepts And Methods
- **separate-pass review** — Do security and correctness in separate passes so each concern gets focused attention instead of diluted results.
- **multipass review** — Run four to five review passes on LLM-generated work before shipping it.
- **shift-left security feedback** — Surface security findings at the developer or model interaction point instead of waiting until code review.
- **cross-checking analyzers** — Use multiple security analyzers to check each other's work as part of the prompt or launch-time workflow.
- **agent supervision** — Design agents with supervisors that inspect and reduce permissions on services and tasks.

### Open Questions
- **How can systems reliably detect slop squatting when a hallucinated package name resolves to a convincing malicious backdoor instead of a real dependency?** — The talk treats this as a new supply-chain attack surface, and detection is a core missing defense.
- **What defenses can actually stop prompt injection and related training or inference-time attacks beyond user education?** — The speaker says this class of attacks is real but does not offer a complete technical solution.
- **How should teams design agent permission and supervision systems in-house before standardized tooling exists?** — The talk says this frontier is already arriving and waiting for a mature ecosystem is risky.

### Derived Links And Source Material
- [[youtube-yWS0udrIOc8-transcript]] — dedicated official recording transcript.
- [[youtube-yWS0udrIOc8]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/yWS0udrIOc8--2026-06-29-steve-yegge-agentic-security-permissions-provenance-and-the-agent-supply-chain.json`.

### Speaker Context
- [[steve-yegge|Steve Yegge]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[steve-yegge]]

## Slide Evidence
- Slide-only cropped deck: [[youtube-7Dtu2bilcFs-dense-slides]] (13 viable slide images).
- Related slide/OCR pages:
- [[youtube-7Dtu2bilcFs-dense-slides]]
- [[youtube-7Dtu2bilcFs-reconstructed-slides]]
- [[youtube-7Dtu2bilcFs-slides]]
- Slide-derived terms: `software`, `coding`, `google`, `deepmind`, `engineering`, `year`, `died`, `steve`, `yegge`, `gene`, `engineer`, `author`, `researcher`, `code`, `models`, `future`, `will`, `watch`

## Official YouTube Recording
- [[youtube-yWS0udrIOc8|Agentic Security: Permissions, Provenance, and the Agent Supply Chain — Steve Yegge, Gas Town]] — official AI Engineer YouTube recording published 2026-07-20.
- Evidence status: [[youtube-yWS0udrIOc8-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-yWS0udrIOc8]] - dedicated official event recording.
- [[youtube-yWS0udrIOc8-transcript]] - dedicated official recording transcript.
- [[youtube-7Dtu2bilcFs]] - supporting context; not the exact session recording.

- Source video: `youtube-yWS0udrIOc8`
- Slide deck: [[youtube-yWS0udrIOc8-slides|Slides: Agentic Security: Permissions, Provenance, and the Agent Supply Chain — Steve Yegge, Gas Town]] — 8 visible slide image(s).
![[assets/slides/yWS0udrIOc8/slide-001.jpg]]
![[assets/slides/yWS0udrIOc8/slide-002.jpg]]
![[assets/slides/yWS0udrIOc8/slide-003.jpg]]
- Slide-derived themes for `youtube-yWS0udrIOc8`: supply, chain, permissions, provenance, bigger, track, june.
- Source video: `youtube-7Dtu2bilcFs`
- Slide deck: [[youtube-7Dtu2bilcFs-dense-slides|Dense Slides: 2026: The Year The IDE Died — Steve Yegge & Gene Kim, Authors, Vibe Coding]] — slide evidence page.
- Additional slide evidence: [[youtube-7Dtu2bilcFs-slides|Slides: 2026: The Year The IDE Died — Steve Yegge & Gene Kim, Authors, Vibe Coding]], [[youtube-7Dtu2bilcFs-reconstructed-slides|Reconstructed Slides: 2026: The Year The IDE Died — Steve Yegge & Gene Kim, Authors, Vibe Coding]]
- Slide-derived themes for `youtube-7Dtu2bilcFs`: year, died, google, software, engineer, author, researcher, steve.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/yWS0udrIOc8.txt` (3,737 words).

## Transcript Markdown
- [[youtube-yWS0udrIOc8-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/yWS0udrIOc8.txt`.
## Attendance Visibility
No high-confidence attendance icon signal is shown for this talk. The sampled video evidence was either low confidence, source-proxy-only, or did not expose a clear audience view.

## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-yWS0udrIOc8` — 3,737 transcript words; 3 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-yWS0udrIOc8`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-yWS0udrIOc8`: security, okay, code, real, give, snorts, stuff, five.
- Slide-derived themes for `youtube-yWS0udrIOc8`: supply, chain, permissions, provenance, bigger, track, june.
- Evidence links for `youtube-yWS0udrIOc8` (primary event evidence): [[youtube-yWS0udrIOc8]], [[youtube-yWS0udrIOc8-transcript]], [[youtube-yWS0udrIOc8-slides]]
- `youtube-7Dtu2bilcFs` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-7Dtu2bilcFs`: year, died, google, software, engineer, author, researcher, steve.
- Evidence links for `youtube-7Dtu2bilcFs` (supporting context only): [[youtube-7Dtu2bilcFs]], [[youtube-7Dtu2bilcFs-slides]], [[youtube-7Dtu2bilcFs-dense-slides]], [[youtube-7Dtu2bilcFs-reconstructed-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
