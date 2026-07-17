---
title: "Scaling Code Quality: Building uReview, Uber’s Multi-Agent Code Review Engine"
category: "talks"
date: "2026-06-29"
time: "12:05pm-12:25pm"
track: "AI-Native Enterprises"
room: "Leadership 1"
speakers: ["Will Bond", "Ameya Ketkar"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "AI-Native Enterprises"
scheduleRoom: "Leadership 1"
scheduleLabels: ["AI-Native Enterprises", "Leadership 1", "session", "confirmed"]
---
# Scaling Code Quality: Building uReview, Uber’s Multi-Agent Code Review Engine

## Conference Context
- Date/time: 2026-06-29 · 12:05pm-12:25pm
- Track/room: AI-Native Enterprises · Leadership 1
- Speaker(s): Will Bond, Ameya Ketkar
- Session type/status: session · confirmed

- Track: AI-Native Enterprises
- Room: Leadership 1
- Session type: session
- Status: confirmed

## Session Description
At Uber scale, human-only code reviews create massive bottlenecks, while generic AI tools overwhelm developers with noisy, hallucinated spam. This session explores the architecture behind uReview, Uber’s multi-agent AI code review engine designed strictly for high-precision feedback. Attendees will learn how we moved beyond monolithic prompts to build a modular pipeline featuring deep contextual ingestion, specialized domain agents, and a Generator-Verifier grader system. By enforcing strict confidence scoring and semantic deduplication, uReview filters out AI noise, shifting the focus from comment quantity to high-signal actionability and significantly reducing Pull Request cycle times. Talk Outline I. The Code Review Crisis at Uber Scale (0–3 mins) Establish the critical tension between engineering velocity and code quality, highlighting why standard AI implementations fail in massive monorepo environments. 1. The Monorepo Bottleneck: At Uber, thousands of engineers commit code daily. Relying solely on human reviewers creates a massive operational bottleneck, leading to reviewer fatigue, extended Pull Request cycle times, and inevitable missed vulnerabilities. 2. The Developer Spam Problem: Generic LLM integrations fail because they prioritize comment quantity over actionable quality. If an AI posts ten hallucinated suggestions on a diff, developers will simply mute the tool. AI must reduce cognitive load, not add to it. 3. The Signal-to-Noise Mandate: Defining the North Star for uReview. The goal is not to replace human reviewers, but to build an AI system that respects developer time by delivering high-precision, strictly verified code feedback. II. The uReview Architecture: A Modular Agentic Pipeline (3–10 mins) Detail the transition from a monolithic prompt approach to uReview’s sophisticated, multi-stage agentic workflow designed for enterprise codebases. 1. Deep Contextual Ingestion: A standard git diff is not enough. We discuss how uReview fetches extended context, integrating with our build systems to analyze surrounding functions, upstream dependencies, and class hierarchies before generating a single token. 2. Specialized Domain Assistants: Instead of a generalist model, uReview deploys independent AI agents. We route code to narrow, specialized agents—such as a Go Concurrency Analyzer, a Java Memory Leak Detector, or a Security Vulnerability Scanner—to ensure precise, domain-specific insights. 3. Hybrid Intelligence: Probabilistic LLMs cannot operate in a vacuum. We detail how uReview integrates deterministic tools, like Bazel dependency graphs and static linters, to ground AI suggestions in objective codebase realities. III. Engineering the Trust Layer (10–17 mins) Dive into the verification phase. This is the core engineering that filters out AI noise and ensures uReview maintains developer trust. 1. The Generator-Verifier Pattern: Implementing a Grader Model architecture. A primary agent generates code suggestions, but a secondary, high-reasoning model audits those suggestions against strict coding guidelines to catch hallucinations before they reach the PR. 2. Confidence Scoring and Suppression: We assign a numerical confidence score to every generated comment. If a comment falls below our calibrated threshold, uReview silently drops it. We explore the engineering behind suppressing low-confidence outputs to prevent tooling spam. 3. Semantic Deduplication: Technical strategies for merging overlapping warnings. If a deterministic static analysis tool and an LLM agent flag the same null pointer exception, uReview merges them into a single, concise developer instruction. IV. Operationalizing uReview at Scale (17–20 mins) Conclude by discussing the long-term governance, feedback loops, and measurable impact of running an AI review engine in production. 1. The Telemetry Feedback Loop: We embedded Useful and Not Useful rating buttons directly into the developer UI on every uReview comment. We discuss how this telemetry flows back into a curated data lake, driving continuous Reinforcement Learning from Human Feedback and prompt refinement. 2. Shifting Success Metrics: Why organizations must abandon vanity metrics like total comments posted. We measure uReview’s success through Actionability Rate (the percentage of AI comments accepted as commits) and the reduction in Mean Time To Merge.

## Synthesis
### Synthesized Breakdown
At Uber scale, human-only code reviews create massive bottlenecks, while generic AI tools overwhelm developers with noisy, hallucinated spam. This session explores the architecture behind uReview, Uber’s multi-agent AI code review engine designed strictly for high-precision feedback. Attendees will learn how we moved beyond monolithic prompts to build a modular pipeline featuring deep contextual ingestion, specialized domain agents, and a Generator-Verifier grader system. By enforcing strict confidence scoring and semantic deduplication, uReview filters out AI noise, shifting the focus from comment quantity to high-signal actionability and significantly reducing Pull Request cycle times.

### Speaker And Company Context
- [[will-bond|Will Bond]] — Staff Software Engineer at [[uber|Uber]].
- [[ameya-ketkar|Ameya Ketkar]] — Software Engineer at [[uber-technology-inc|Uber Technology Inc.]].

### Topics Covered
- [[agent-security]]
- [[coding-agents]]

### Derived Links And Source Material

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis is based on the official schedule and linked source pages. It should be revisited when exact session recordings or transcript-backed secondary sources are available.
## People
- [[will-bond]]
- [[ameya-ketkar]]

## Media Evidence
No exact recording or transcript evidence is attached yet; the official schedule remains the source for this session.
## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
No linked video, transcript, or slide source has been attached yet.

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.
