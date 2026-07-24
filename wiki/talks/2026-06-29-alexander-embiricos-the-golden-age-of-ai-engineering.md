---
title: The Golden Age of AI Engineering
category: talks
date: '2026-06-29'
time: '9:25am-9:45am'
track: Software Factories
room: Main Stage
speakers:
  - Alexander Embiricos
  - Romain Huet
sourceLabels:
  - Official conference schedule
  - Public YouTube metadata
last_auto_summarized: '2026-07-04T07:01:57.505Z'
scheduleTrack: "Software Factories"
scheduleRoom: "Main Stage"
scheduleLabels: ["Software Factories", "Main Stage", "keynote", "confirmed"]
---
# The Golden Age of AI Engineering

## Conference Context
- Date/time: 2026-06-29 · 9:25am-9:45am
- Track/room: Software Factories · Main Stage
- Speaker(s): Alexander Embiricos, Romain Huet
- Session type/status: keynote · confirmed

- Track: Software Factories
- Room: Main Stage
- Session type: keynote
- Status: confirmed

## Session Description
TBD

## Summary
This scheduled keynote sits in the Software Factories track and brings together two OpenAI product leaders: Alexander Embiricos, Head of Enterprise Product and former Codex product lead, and Romain Huet, Head of Developer Experience. The available supporting material is not yet a confirmed recording of this exact session, but it does connect the session to OpenAI's developer-facing story around multimodal AI systems, including text, vision, voice, model capability shifts, and practical engineering workflows.

The linked Romain Huet video, "From Text to Vision to Voice Exploring Multimodality with Open AI," provides the strongest contextual evidence currently attached to this page. Its extracted and reconstructed slide pages point toward themes such as GPT-4-era model evolution, cheaper and more capable models, vision use cases, natural interfaces, and developer tooling. Taken together with Embiricos's background in Codex and enterprise product, the session is likely best treated as a keynote about how AI engineering is moving from isolated model demos toward production software factories, where multimodal models, developer platforms, and enterprise workflows become part of the same engineering system.

## Synthesis
### Transcript-Backed Summary
The talk argues that AI engineering is not the end of engineering but a return to its roots: engineers are still needed to combine fast-moving science with judgment, design, and taste to solve real problems. Its central mechanism is a layered agent stack and a dual-mode product shape, where chat handles delegation and a collaborative surface handles inspection, steering, review, and deployment; this lets agents take on more of the lifecycle before, during, and after coding. The main tradeoff is that as models become faster and more capable, value comes less from watching every token and more from designing reliable loops, open interfaces, and the right environment for each task, so humans can spend attention only where decisions matter most.

### Key Takeaways
- The speakers frame AI engineering as a continuation of engineering fundamentals, not a replacement for them.
  - Evidence: "And in that sense, it's not the end of engineering. We think it's a return to the roots of engineering."
- The interface should let people ask for help anywhere and then inspect or steer work when needed.
  - Evidence: "And then you want a a powerful collaborative UI that you can use when you want to inspect, steer, or shape things yourself."
- OpenAI wants the same primitives it uses internally to be exposed through the API so developers can reuse them.
  - Evidence: "always try to bake it into the API first so you can benefit as well one example recently was compaction codex needed a way to compact long context for longunning tasks and so we'll build that into the API So that means your agents can use the same primitives that we built for ourselves."
- The practical working pattern is to review once at the outer loop and let agents handle execution, testing, and landing the change.
  - Evidence: "I review once, I re leave a note, I maybe approve, the loop continues and it can land after the checks pass."

### Claims From The Talk
- The speakers argue that AI engineers are now the people pushing the frontier, not a class being made obsolete by AI. (`explicit`)
  - Evidence: "But now what we're here to say is that the AI engineers are eating the world. AI engineers are the people here pushing the frontier."
- They say engineering is fundamentally about combining science with design, taste, judgment, and imagination to make useful things for people. (`explicit`)
  - Evidence: "It's about taking the latest science and combining it with design, with taste, with judgment, and most of all, imagination to make something that people can actually use."
- The product goal is to maximize engineer empowerment rather than automate engineers away. (`explicit`)
  - Evidence: "Instead, the the product shape that we want is one that maximally empowers engineers. So, you know, if we think about what that product shape is, we actually think it's pretty simple."
- Codex is presented as an open, layered stack that OpenAI uses itself and intends for others to build on. (`explicit`)
  - Evidence: "cannot be a closed product that only openai can improve so we've intentionally designed codeex as a set of layers that anyone can build on and we want to show you a little bit of that stack today and how it it manifests first it starts with the model and Alexander showed how quickly we're"
- Peter Steinberger describes the core agent loop as persistent context, delegation, and triggers. (`explicit`)
  - Evidence: "So we have persistent context, delegation and triggers. There's your loop. And once the loop starts working, you discover the next problem."
- He says the limiting factor has moved from tokens and compute to human attention. (`explicit`)
  - Evidence: "And unlike tokens or compute, I can't simply add more of it. So the most important skill is today is deciding where to spend it."

### Topics Covered
- **AI engineering** — The role of engineers in an AI-native software era.
- [[coding-agents|Collaborative agent UI]] — A product model that combines chat delegation with hands-on steering.
- [[ai-sandboxes|Open agent stack]] — An application and infrastructure strategy where the same stack is used internally and externally.
- **Value maxing** — Optimizing for user value rather than raw token output.
- [[coding-agents|Manager-worker loops]] — Long-lived coordination between a manager agent and worker agents.
- [[ai-sandboxes|Agent host placement]] — Choosing the right host or environment for each agent task.

### Tools And Named Systems
- **Codex app** — The product surface for chatting with and steering coding agents.
- **Codex Cloud** — The cloud execution environment for agents.
- **Responses API** — The API layer used to access the same model primitives that power the product.
- **Codex harness** — The open-source harness that defines the agent loop.
- **Apps server** — The open-source application server used to unify Codex apps and sign-in flows.
- **browser use** — A plugin that enables browser-based agent actions.
- **computer use** — A plugin that enables computer-based agent actions.
- **GPT 5.6 Terra** — A model family described as bringing GPT-5.5-level intelligence at half the cost.
- **GPT 5.6 Cel** — A fast model deployment described as running frontier intelligence on Cerebras.

### Novel Concepts And Methods
- **Chat-plus-hands-on workflow** — Start with chat for broad delegation, then switch into a hands-on collaborative surface when you need to inspect or steer details.
- **Build-test loop** — Use build and test feedback so the model can verify its work instead of relying on blind generation.
- **Persistent manager loop** — Keep long-lived state, delegation, and wake-up triggers so a manager agent can coordinate work across time.
- **Outer-loop review** — Operate in an outer loop where the human reviews, approves, and redirects while workers execute the inner loop.

### Open Questions
- **How should an agent decide which environment to use for a given task when it can run locally, in the cloud, or on another connected machine?** — That choice determines whether the agent can act autonomously without forcing the user to manage infrastructure details.
- **How can a long-lived manager agent stay reachable from places like Slack or text without being trapped inside a single app session?** — If this works, agents become persistent collaborators instead of isolated tools.
- **Can the agent design the whole work loop for the user, not just execute tasks inside an existing loop?** — That would push the product from task automation toward workflow design.

### Derived Links And Source Material
- [[youtube-pMggiOb18tc-transcript]] — dedicated official recording transcript.
- [[youtube-pMggiOb18tc]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/pMggiOb18tc--2026-06-29-alexander-embiricos-the-golden-age-of-ai-engineering.json`.

### Speaker Context
- No speaker profile is attached in the official schedule data.

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[alexander-embiricos]]
- [[romain-huet]]

## Slide Evidence
- Slide-only cropped deck: [[youtube-yJHw33cVeHo-dense-slides]] (3 viable slide images).
- Related slide/OCR pages:
- [[youtube-yJHw33cVeHo-dense-slides]]
- [[youtube-yJHw33cVeHo-reconstructed-slides]]
- [[youtube-yJHw33cVeHo-slides]]
- Slide-derived terms: `gpt-40`, `models`, `intelligence`, `cases`, `gpt-4`, `world`, `model`, `string`, `custom`, `openal`, `fair`, `toolbox`, `cheaper`, `trained`, `vision`, `next`, `gpt-3`, `natural`

## Official YouTube Recording
- [[youtube-pMggiOb18tc|The Golden Age of AI Engineering — Alexander Embiricos & Romain Huet & Peter Steinberger, OpenAI]] — official AI Engineer YouTube recording published 2026-07-09.
- Evidence status: [[youtube-pMggiOb18tc-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-pMggiOb18tc]] - dedicated official event recording.
- [[youtube-pMggiOb18tc-transcript]] - dedicated official recording transcript.
- [[youtube-yJHw33cVeHo]] - supporting context; not the exact session recording.

- Source video: `youtube-pMggiOb18tc`
- Slide deck: [[youtube-pMggiOb18tc-slides|Slides: The Golden Age of AI Engineering — Alexander Embiricos & Romain Huet & Peter Steinberger, OpenAI]] — 32 visible slide image(s).
![[assets/slides/pMggiOb18tc/slide-001.jpg]]
![[assets/slides/pMggiOb18tc/slide-002.jpg]]
![[assets/slides/pMggiOb18tc/slide-003.jpg]]
- Slide-derived themes for `youtube-pMggiOb18tc`: codex, software, engineers, computer, plugins, lifetime, career, left.
- Source video: `youtube-yJHw33cVeHo`
- Slide deck: [[youtube-yJHw33cVeHo-dense-slides|Dense Slides: From Text to Vision to Voice Exploring Multimodality with Open AI: Romain Huet]] — slide evidence page.
- Additional slide evidence: [[youtube-yJHw33cVeHo-slides|Slides: From Text to Vision to Voice Exploring Multimodality with Open AI: Romain Huet]], [[youtube-yJHw33cVeHo-reconstructed-slides|Reconstructed Slides: From Text to Vision to Voice Exploring Multimodality with Open AI: Romain Huet]]
- Slide-derived themes for `youtube-yJHw33cVeHo`: cases, text, vision, voice, outlook, research, deployment, company.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/pMggiOb18tc.txt` (4,606 words).

## Transcript Markdown
- [[youtube-pMggiOb18tc-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/pMggiOb18tc.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-pMggiOb18tc` — 4,606 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-pMggiOb18tc`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-pMggiOb18tc`: models, codex, open, model, should, engineering, well, even.
- Slide-derived themes for `youtube-pMggiOb18tc`: codex, software, engineers, computer, plugins, lifetime, career, left.
- Evidence links for `youtube-pMggiOb18tc` (primary event evidence): [[youtube-pMggiOb18tc]], [[youtube-pMggiOb18tc-transcript]], [[youtube-pMggiOb18tc-slides]]
- `youtube-yJHw33cVeHo` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-yJHw33cVeHo`: cases, text, vision, voice, outlook, research, deployment, company.
- Evidence links for `youtube-yJHw33cVeHo` (supporting context only): [[youtube-yJHw33cVeHo]], [[youtube-yJHw33cVeHo-slides]], [[youtube-yJHw33cVeHo-dense-slides]], [[youtube-yJHw33cVeHo-reconstructed-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
