---
title: "WF26: Harness Engineering & Startup Battlefield ft. Garry Tan, Mike Krieger, @t3dotgg , DSPy"
category: "resources"
sourceLabels:
  - "Public YouTube metadata"
  - "YouTube transcript"
videoId: "I2cbIws9j10"
last_enriched: "2026-07-08T23:50:10.203099+00:00"
---
# WF26: Harness Engineering & Startup Battlefield ft. Garry Tan, Mike Krieger, @t3dotgg , DSPy

## What It Is
A public AI Engineer YouTube WF26 livestream used as supporting material for the AI Engineer World's Fair 2026 wiki.

## Transcript Status
Cached transcript text is available at `raw/sources/youtube-livestream-transcripts/I2cbIws9j10.txt` (91,792 words).

## Topic Signals
- [[coding-agents|Coding Agents]], [[inference-engineering|Inference Engineering]], [[agent-evaluations|Agent Evaluations]], [[agent-memory|Agent Memory]]
- Transcript keywords: `disorder`, `substantial`, `energy`, `exploring`, `memory`, `persists`, `involves`, `smartest`

## Link
[YouTube](https://www.youtube.com/watch?v=I2cbIws9j10)

## Related Scheduled Sessions
- [[2026-07-01-garry-tan-closing-keynote-garry-tan]] — Closing Keynote: Garry Tan (match score 86)
- [[2026-07-01-mike-krieger-how-anthropic-builds-lessons-from-labs]] — How Anthropic Builds: Lessons from Labs (match score 80)

## Extracted Slides
- [[youtube-I2cbIws9j10-dense-slides]]
- [[youtube-I2cbIws9j10-slides]]

## Slide-Derived Content Notes
Dense slide OCR adds the following content signals. Treat these as reviewed summaries of slide evidence, with the linked slide page remaining the visual source of truth.

- Dense slide deck: [[youtube-I2cbIws9j10-dense-slides]]
- Standard frame deck: [[youtube-I2cbIws9j10-slides]]
- Model selection is framed as a production tradeoff where accuracy and output quality dominate, with agentic capabilities, cost, privacy controls, reliability, enterprise support, latency, fine-tuning, and open weights as secondary considerations. Related topics: [[agent-evaluations]], [[inference-engineering]].
- The stream includes an end-to-end RL pipeline pattern for self-healing data workflows: observe logs/schema/data quality, diagnose the likely failure family, estimate operational risk, choose a bounded remediation, and validate recovery. Related topics: [[agent-evaluations]], [[coding-agents]].
- The anomaly-remediation slide treats safety override as part of the intelligence layer, escalating high-risk anomalies instead of letting an agent blindly act. Related topics: [[agent-security]], [[agent-evaluations]].
- The KV-cache slide makes context memory concrete: every token an agent reads or writes creates cached state, so long-context agents can carry a hidden RAM bill that grows into tens of gigabytes. Related topics: [[agent-memory]], [[inference-engineering]].
- One slide names a common agent design failure: forcing one conversation/context window to act as database, filesystem, memory, and reasoning space at once. Related topics: [[agent-memory]], [[coding-agents]].
- A memory-oriented game-agent slide argues for tracking narrative state and attitude rather than brittle numeric state when the model is better at qualitative continuity. Related topics: [[agent-memory]].
- TurboQuant is presented as a compression approach for embeddings and KV cache, using low-bit storage to reduce memory pressure without retraining. Related topics: [[inference-engineering]].
- The agent-architecture slide separates the agent from any single model: the production agent also includes runtime or sandbox, tools, loop, and framework. Related topics: [[coding-agents]], [[ai-sandboxes]].
- The simplified loop slide shows a log-reconstructable agent pattern: rebuild state from the session log, ask the model for the next step, append model/tool results, and continue. Related topics: [[coding-agents]], [[agent-memory]].
