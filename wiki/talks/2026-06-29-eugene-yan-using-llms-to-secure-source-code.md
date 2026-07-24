---
title: "Using LLMs to Secure Source Code"
category: "talks"
date: "2026-06-29"
time: "1:30pm-1:50pm"
track: "Security"
room: "Track 5"
speakers: ["Eugene Yan"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Security"
scheduleRoom: "Track 5"
scheduleLabels: ["Security", "Track 5", "sponsor", "confirmed"]
---
# Using LLMs to Secure Source Code

## Conference Context
- Date/time: 2026-06-29 · 1:30pm-1:50pm
- Track/room: Security · Track 5
- Speaker(s): Eugene Yan
- Session type/status: sponsor · confirmed

- Track: Security
- Room: Track 5
- Session type: sponsor
- Status: confirmed

## Session Description
Models are now finding and fixing real vulnerabilities at scale. Drawing on Anthropic's work with security teams, this talk walks a six-step workflow — threat model, sandbox, discover, verify, triage, patch — through one running example, shows where orgs actually bottleneck, and gives you a copy-paste path to your first scan.

## Synthesis
### Transcript-Backed Summary
The talk argues that LLMs have crossed the threshold from bug-hunting novelty to practical security infrastructure, but only if they are embedded in a workflow that turns raw detection into verified, prioritized, and safely patched findings. The core mechanism is a six-step pipeline: build a threat model, run in an isolated sandbox, discover candidate issues, verify them independently and adversarially, triage by real business impact, and then patch with regression checks plus reattack. The tradeoff is that better models reduce the need for elaborate prompts, but they also expose new bottlenecks in organizational context, severity calibration, routing, and patch review, so the real work shifts from scanning to coordination. The practical consequence is that teams should start small, especially with open source dependencies, learn interactively, and then invest in the surrounding process so the system can scale beyond a handful of findings.

### Key Takeaways
- Start with whatever is most comfortable, such as open source dependencies, instead of waiting for a fully automated program.
  - Evidence: "I would like to you start now please start with open source dependencies start with whatever you're comfortable with."
- Use interactive, hands-on runs first to learn where the model lacks context and where precision is weak.
  - Evidence: "Doesn't matter. Learn where you get cut. Learn what kind of context you're missing. Learn where precision is low."
- If the sandbox is representative, verification can detonate proof-of-concept exploits and confirm whether findings are true.
  - Evidence: "And also if you have invested the time in building building a representative sandbox um have the verification agent build the p detonate the pock to confirm if the ver the vulnerability is true."
- Closing the loop turns security harnesses into improving assets over time rather than one-off operational costs.
  - Evidence: "They're operational expense, but when you close the loop, they now become capital expense."

### Claims From The Talk
- The speaker argues that frontier models are already helping defenders find and fix vulnerabilities at scale, not just in isolated demos. (`explicit`)
  - Evidence: "So what this means is that what's happened in April is 20x of last year's average. Um they attributed about twothirds of this to mess preview about 271 which shows that frontier models can help defenders like yourself find and fix vulnerabilities at scale."
- He reports that the main bottleneck has moved away from finding bugs and toward verification, triage, and patching. (`explicit`)
  - Evidence: "We shared our observation that finding vulnerabilities now is quite straightforward. The bottleneck has now shifted to verification, triage, and patching."
- He says a well-documented threat model can raise true positive rates substantially, citing a result near 90%. (`explicit`)
  - Evidence: "Um the first step is the threat model. So why does this matter? So several teams if you look at a code right finding have found that having a well doumented thread model really increases your true positive rate to 90%."
- He reports that giving the agent tools to query APIs, read logs, and inspect source can push true positive rate close to 100%. (`explicit`)
  - Evidence: "And when they did this, their true positive rate was almost 100%. because the model could actually verify in the loop."
- He argues that verification should be independent and adversarial so the agent starts by assuming the finding is false, which reduces false positives. (`explicit`)
  - Evidence: "assume that this vulnerability is false, try to confirm it's false or confirm it's true. So this sets the this sets a very high bar for the vulnerability which reduces the false positive rate."
- He reports that patch quality improves when patches are validated by regression tests and by a fresh agent reattacking the fix. (`explicit`)
  - Evidence: "further right we can have a fresh discovery agent try to attack the patch code again is the patch comprehensive enough and teams have found that by giving the patching agent such feedback um you can actually the patch quality improves greatly right and you know This is the generative verifier loop."
- He says human attention does not scale, so organizational disagreements about severity and ownership become a major limiter. (`explicit`)
  - Evidence: "But human attention doesn't scale. Your deaf, your product engineers and your security engineers, what if they don't agree on what high severity or uh critical severity is?"

### Topics Covered
- **LLM-assisted vulnerability discovery** — Using language models to discover real vulnerabilities in source code and security systems.
- **Threat modeling** — Turning implicit system knowledge into explicit written context for security analysis.
- [[ai-sandboxes|Security sandboxes]] — Running exploit tests in isolated, reproducible environments to safely validate findings.
- **Verification and precision** — Separating recall-oriented discovery from precision-oriented confirmation.
- **Security triage** — Ranking findings by impact, likelihood, and business context before handing them to engineers.
- **Patch validation loops** — Validating fixes by testing the original exploit, preserving the test suite, and reattacking the patch.
- [[agentic-search|Organizational bottlenecks]] — Operational constraints that become the limiting factor once model-assisted scanning is cheap.

### Tools And Named Systems
- [[docker|Docker]] — Container platform used to build the representative sandbox with separate app, database, and cache images.
- [[jira|Jira]] — Ticketing system mentioned as a manual routing mechanism for sending vulnerabilities to teams.
- **Confluence** — Documentation system cited as a place where system context and compensating controls may live outside the codebase.

### Novel Concepts And Methods
- **Six-step security workflow** — Six-step security workflow that moves from setup to discovery, verification, triage, and patching.
- **Threat modeling as context capture** — Threat modeling as written system context that captures assets, entry points, and threat vectors for the model.
- **Isolated sandboxing** — Sandboxing untrusted code and exploit proof-of-concepts in isolated environments with reproducible baselines.
- [[context-engineering|Context engineering]] — Context engineering that feeds the model as much relevant code, docs, and history as possible, plus simple prompts and external tools.
- **Independent verification** — Independent adversarial verification that separates confirmation from discovery to preserve recall and improve precision.
- **Generative verifier loop** — Generative verifier loop for patching, where fixes are tested, reattacked, and then human-reviewed before merge.

### Open Questions
- **How should an organization standardize severity definitions so security, product, and red-team stakeholders agree on what counts as high risk?** — The talk says disagreement over severity is a major bottleneck, so a shared rubric determines whether findings can be prioritized reliably.
- **What is the most scalable way to route large volumes of vulnerabilities to the right owners without manual curation?** — The speaker says routing becomes infeasible once findings reach the hundreds, so ownership automation is critical.
- **How far can patch review be automated for security issues before human approval must remain in the loop?** — The talk treats patch review as one of the least automated and most consequential remaining bottlenecks.

### Derived Links And Source Material
- [[youtube-imFedndyXYQ-transcript]] — dedicated official recording transcript.
- [[youtube-imFedndyXYQ]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/imFedndyXYQ--2026-06-29-eugene-yan-using-llms-to-secure-source-code.json`.

### Speaker Context
- [[eugene-yan|Eugene Yan]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[eugene-yan]]

## Official YouTube Recording
- [[youtube-imFedndyXYQ|Using LLMs to Secure Source Code — Eugene Yan, Anthropic]] — official AI Engineer YouTube recording published 2026-07-17.
- Evidence status: [[youtube-imFedndyXYQ-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-imFedndyXYQ]] - dedicated official event recording.
- [[youtube-imFedndyXYQ-transcript]] - dedicated official recording transcript.

- [[youtube-imFedndyXYQ-slides]] — extracted from the related public AI Engineer video.

- Source video: `youtube-imFedndyXYQ`
- Slide deck: [[youtube-imFedndyXYQ-slides|Slides: Using LLMs to Secure Source Code — Eugene Yan, Anthropic]] — 7 visible slide image(s).
![[assets/slides/imFedndyXYQ/slide-001.jpg]]
![[assets/slides/imFedndyXYQ/slide-002.jpg]]
![[assets/slides/imFedndyXYQ/slide-003.jpg]]
- Slide-derived themes for `youtube-imFedndyXYQ`: fair, security, track, june, secure, source, code, engineering.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/imFedndyXYQ.txt` (3,967 words).

## Transcript Markdown
- [[youtube-imFedndyXYQ-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/imFedndyXYQ.txt`.

## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-imFedndyXYQ` — 3,967 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-imFedndyXYQ`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-imFedndyXYQ`: model, code, security, vulnerabilities, patch, verification, context, models.
- Slide-derived themes for `youtube-imFedndyXYQ`: fair, security, track, june, secure, source, code, engineering.
- Evidence links for `youtube-imFedndyXYQ` (primary event evidence): [[youtube-imFedndyXYQ]], [[youtube-imFedndyXYQ-transcript]], [[youtube-imFedndyXYQ-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
