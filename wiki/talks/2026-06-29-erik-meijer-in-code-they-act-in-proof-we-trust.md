---
title: "In Code They Act, In Proof We Trust"
category: "talks"
date: "2026-06-29"
time: "4:50pm-5:10pm"
track: "Harness Engineering"
room: "Main Stage"
speakers: ["Erik Meijer"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Harness Engineering"
scheduleRoom: "Main Stage"
scheduleLabels: ["Harness Engineering", "Main Stage", "keynote", "confirmed"]
---
# In Code They Act, In Proof We Trust

## Conference Context
- Date/time: 2026-06-29 · 4:50pm-5:10pm
- Track/room: Harness Engineering · Main Stage
- Speaker(s): Erik Meijer
- Session type/status: keynote · confirmed

- Track: Harness Engineering
- Room: Main Stage
- Session type: keynote
- Status: confirmed

## Session Description
AI agents today execute on blind trust, and the failure modes are already in the headlines: a dealership chatbot agreeing to sell a $76,000 Chevy Tahoe for $1, a coding agent wiping a production database during a code freeze, an "agent skill" quietly installing a keylogger on a developer's machine. These are not edge cases. They are the predictable consequence of allowing agents to act without any mechanical guarantee of correctness or safety. Execution is irreversible. You cannot unsend a message, unwire a payment, or un-delete a database. In that regime, permitting an unsafe action costs far more than withholding a safe one, and thus the economically rational choice is to refuse to let agents act on unchecked intent alone. Automind is an agent harness that enforces this discipline by construction. Before any action runs, the agent must submit its execution plan together with a machine-checkable proof of safety and correctness, written in Universalis, a literate logic programming language designed to be read by humans and verified by machines. A small, auditable checker decides whether the plan is allowed to execute. By left-shifting the trust boundary, we no longer have to trust the agent's proposal, or even its proof; only the checker. Policy compliance becomes a static property, established before the first side effect. We can finally demand formal proofs, not vibes, from the agents we deploy.

## Synthesis
### Transcript-Backed Summary
The talk argues that once agents can invoke tools, safety stops being a philosophical matter and becomes an execution problem, because side effects can happen before any final answer is returned. The proposed fix is to move the agent's output one level up: instead of executing intent directly, the model emits a plan or program together with a machine-checkable proof that the plan is safe, and a small checker decides whether execution is allowed. The main tradeoff is that raw IO is a black box, so the system must stop trusting human-readable intent and instead represent actions in a form that supports static analysis and proof checking. The practical consequence is a left-shifted trust boundary in which policy compliance is established before the first side effect, making proof-carrying agent execution the central design goal.

### Key Takeaways
- Agents should not be allowed to act unless their safety can be proven first.
  - Evidence: "So, you should never ever let your agents do something unless you can absolutely prove that it's safe."
- Tool use is the point where agent behavior becomes dangerous because side effects can happen while the answer is being computed.
  - Evidence: "Why is that? And that is because this IO says that in order to compute the answer, the agent has to go through the agentic loop and it's doing side effects."
- Representing agent behavior as programs makes compiler-style analysis and verification possible.
  - Evidence: "So now we're safe. We're home safe. And Jeff Huntley wanted to remind you that we can solve the trifecta problem just by doing taint analysis on these expression on these programs."
- The trusted boundary should be a proof checker that can inspect the proof without running the agentic loop.
  - Evidence: "And the nice thing is here that you can get at that proof without having to run the agentic loop."

### Claims From The Talk
- The speaker argues that adding tool calls changes AI safety from a theoretical concern into a real-world danger because the agent can now cause side effects during execution. (`explicit`)
  - Evidence: "Um, now the act of adding tool calls changes AI safety from a philosophical debate to something that causes real danger."
- He says a raw IO value is a black box, so it cannot be reasoned about directly. (`explicit`)
  - Evidence: "We want to be able to check it. All right. Now the problem is that if you get a value of type IO of A um that's a really a black box and the lean manual says that is a black box you cannot reason about it."
- He proposes moving the agentic loop out of the model by having the model produce a plan that another component executes. (`explicit`)
  - Evidence: "Um, but all that we're doing is we're pushing this IO to the right, to the right. And what you now see is that the tool belt of Claude goes to the left, to the left, and suddenly Claude is a nice puppy again because instead of executing the agentic loop, it creates a plan and says, \"Here is the plan to do the agentic loop.\" And now Bernie will take that plan and we'll execute it."
- He identifies the core fix as proof-carrying code: the agent supplies a program and a proof that the program is safe before it runs. (`explicit`)
  - Evidence: "Now you would say Eric, oh you're a genius. No, I'm my brain is the size of a peanut. This is something that's called proof carrying code and it was invented by academics in the 1990s and I'm just stealing it."
- He claims this approach can deliver mathematically proven safe agentic compute using only elementary type systems and programming-language machinery. (`explicit`)
  - Evidence: "The language doesn't matter. It's it's the um the principle that matters. So hopefully you've learned tonight that it is actually possible to have mathematically proven safe agentic compute and it only requires very elementary type systems and programming language machinery. Thank you so much."

### Topics Covered
- [[agent-security|Tool-call safety]] — The risk that tool-enabled agents can create real-world harm through side effects.
- [[agent-reliability-and-durable-execution|Agentic loops]] — The execution loop in which an agent acts on the world rather than only producing text.
- [[agent-security|Proof-carrying code]] — The idea of attaching a proof to code so execution is allowed only after verification.
- [[agent-evaluations|Program verification]] — Turning agent intent into a program that can be inspected and analyzed statically.
- **Static analysis** — Using compiler methods like type checking and data-flow analysis on agent programs.

### Tools And Named Systems
- **Lean** — A theorem prover used as the main example of the verification stack.
- **Dafny** — An alternative tier-improving and model-checking language mentioned alongside Lean.
- **Isabelle** — A theorem prover named as another option in the verification ecosystem.
- **PVS** — Another proof assistant or model checker cited as part of the same family of tools.
- **TA Plus** — A model checker or verification tool mentioned in the list of alternatives.

### Novel Concepts And Methods
- **Air-gapped execution** — Separating proposal from execution so the model cannot directly perform the agentic loop.
- **Plan as program** — Having the model emit a program or expression that represents the computation instead of executing it outright.
- **Proof-carrying code** — Requiring an execution plan to arrive with a machine-checkable proof before it is allowed to run.
- **Static analysis** — Applying compiler-style checks such as data-flow analysis and type checking to the program representation of agent actions.
- **Inductive proof generation** — Using an inductive interpreter and inductive proof structure so models can generate proofs for the language.

### Open Questions
- **What restricted program language is expressive enough to cover useful agent workflows while still remaining easy to verify statically?** — The talk depends on a language that can represent actions precisely enough for proof checking without losing practical usefulness.
- **How can models reliably generate both executable programs and valid proofs without a human proof author in the loop?** — The approach only scales if proof generation is automatic enough for agent-driven systems.

### Derived Links And Source Material
- [[youtube--CnA2lGfymY-transcript]] — dedicated official recording transcript.
- [[youtube--CnA2lGfymY]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/-CnA2lGfymY--2026-06-29-erik-meijer-in-code-they-act-in-proof-we-trust.json`.

### Speaker Context
- [[erik-meijer|Erik Meijer]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[erik-meijer]]

## Official YouTube Recording
- [[youtube--CnA2lGfymY|"I've never seen anything scarier than an LLM with tool calls." — Erik Meijer aka @HeadinTheBox]] — official AI Engineer YouTube recording published 2026-07-13.
- Evidence status: [[youtube--CnA2lGfymY-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube--CnA2lGfymY]] - dedicated official event recording.
- [[youtube--CnA2lGfymY-transcript]] - dedicated official recording transcript.

- Source video: `youtube--CnA2lGfymY`
- Slide deck: [[youtube--CnA2lGfymY-slides|Slides: \"I've never seen anything scarier than an LLM with tool calls.\" — Erik Meijer aka @HeadinTheBox]] — 32 visible slide image(s).
![[assets/slides/-CnA2lGfymY/slide-001.jpg]]
![[assets/slides/-CnA2lGfymY/slide-002.jpg]]
![[assets/slides/-CnA2lGfymY/slide-003.jpg]]
- Slide-derived themes for `youtube--CnA2lGfymY`: someone, credible, fair, conviction, sara, made, serious, error.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/-CnA2lGfymY.txt` (3,148 words).

## Transcript Markdown
- [[youtube--CnA2lGfymY-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/-CnA2lGfymY.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube--CnA2lGfymY` — 3,148 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube--CnA2lGfymY`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube--CnA2lGfymY`: answer, lean, safe, model, type, look, llms, question.
- Slide-derived themes for `youtube--CnA2lGfymY`: someone, credible, fair, conviction, sara, made, serious, error.
- Evidence links for `youtube--CnA2lGfymY` (primary event evidence): [[youtube--CnA2lGfymY]], [[youtube--CnA2lGfymY-transcript]], [[youtube--CnA2lGfymY-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
