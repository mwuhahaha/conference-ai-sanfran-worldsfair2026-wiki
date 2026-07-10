---
title: "Video Attendance Visibility"
category: "resources"
sourceLabels: ["Local video frame sampling", "Attendance calibration", "OpenCV visual signal"]
---
# Video Attendance Visibility

This page records the conservative video-level attendance visibility pass. It is not an exact attendance count. A number is shown only when the visual signal is high confidence; zero and low-confidence estimates are suppressed.

## Display Rule
- Do not show a number when the estimate is zero.
- Do not show a number when confidence is low or the source is only a supporting/camera-family proxy.
- When confidence is high, show a capped icon scale from 1 to 10 person icons.
- Automated detector output may nominate a candidate, but publication requires explicit high-confidence review.
- The icon scale is a visible-attendance signal, not a precise count.

## Published Icon Signals

- No high-confidence video attendance icon signals are publishable in this pass.

## Suppressed Video Signals

- `PmZDupFP3UM` — AI-Assisted Engineering: 5 Trends We're Seeing From 500+ Organizations (Expo Stage 2 NW): suppressed; max local visible-person signal 2; confidence low.
- `I2cbIws9j10` at 6227s — Latent Space Live: the Inference Inflection from First Principles (Expo Stage 2 NW): suppressed; max local visible-person signal 3; confidence low.
- `xz0-brt56L8` — An Interaction Is All You Need (Expo Stage 3 SW): suppressed; max local visible-person signal 2; confidence low.
- `NuePCNMpWGc` — Expo Welcome Speech (Expo Stage 3 SW): suppressed; max local visible-person signal 4; confidence low.
- `BM2JX9hqsVQ` — An AI Future Without the Lock-In (Expo Stage 4 SE): suppressed; max local visible-person signal 1; confidence low.
- `tzRvcTEapzo` — All the Things We Have to Do to Satisfy Your Insatiable Need for Tokens (Leadership 1): suppressed; max local visible-person signal 2; confidence low.
- `bSG9wUYaHWU` — Coding Agents Don't Scale Themselves. Neither Do Your Teams.The Rise of Agent Enablement. (Leadership 2): suppressed; max local visible-person signal 1; confidence low.
- `Lc8zRh9muoY` — FinOps for AI Agents: Who Spent All the Tokens? (Leadership 2): suppressed; max local visible-person signal 4; confidence low.
- `SZStlIhyTCY` — Tokenomics: From AI Spend to AI Value (Leadership Lounge): suppressed; max local visible-person signal 5; confidence low.
- `I2cbIws9j10` at 28640s — Closing Keynote: Garry Tan (Main Stage): suppressed; max local visible-person signal 3; confidence low.
- `I2cbIws9j10` at 11668s — Harness Engineering: Building the Production Cage for Powerful Domain Agents (Main Stage): suppressed; max local visible-person signal 3; confidence low.
- `I2cbIws9j10` at 4262s — How Anthropic Builds: Lessons from Labs (Main Stage): suppressed; max local visible-person signal 3; confidence low.
- `I2cbIws9j10` at 29906s — $100,000 AIE Startup Battlefield — presented by Hyperagent (Networking Room): suppressed; max local visible-person signal 5; confidence low.
- `wsFd22SL1s8` — 'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt 1' (Track 1): suppressed; max local visible-person signal 1; confidence low.
- `AheG9p_JXVw` — Building an Agentic Video Editor for Mass Consumer (Track 1): suppressed; max local visible-person signal 1; confidence low.
- `B9h9ovW5H9U` — AI on Your Lakehouse: Context Comes in Shapes, Not Queries (Track 2): suppressed; max local visible-person signal 2; confidence low.
- `Bc6Ojl2XS1w` — Build realtime multimodal agents with Gemini Live (continued 2) (Track 4): suppressed; max local visible-person signal 6; confidence low.
- `7Dtu2bilcFs` — Agentic Security: Permissions, Provenance, and the Agent Supply Chain (Track 5): suppressed; max local visible-person signal 6; confidence low.
- `liG97YXaTSA` — Everything Is a Rollout (Track 5): suppressed; max local visible-person signal 9; confidence low.
- `I2cbIws9j10` at 7876s — Context Engineering in 2026: Compaction, Memory & Cost (Track 6): suppressed; max local visible-person signal 8; confidence needs_review; automated candidate awaiting review.
- `gcseUQJ6Gbg` — The Missing Layer: Design Taste in AI Agents // Stop Letting Your Agents Ship Ugly UIs (Track 6): suppressed; max local visible-person signal 5; confidence low.
- `dvft0Gp9sEE` — Voice Agents Can Just Do Things (Track 6): suppressed; max local visible-person signal 2; confidence low.
- `u3NofYYstaY` — 200 Million Patient Interactions Later: What the Generic Voice Stack Misses (Track 7): suppressed; max local visible-person signal 8; confidence low.
- `-cKUW6n8hBU` — 'It’s Tokens All The Way Down: How RLMs are Different' (Track 8): suppressed; max local visible-person signal 4; confidence low.
- `SbUxRluVRwk` — Benchmarking Coding Agents on New vs Legacy Code bases (Track 8): suppressed; max local visible-person signal 2; confidence low.
- `BiG2ssibKGc` — Your agents lack context: Here's how to fix \"You're absolutely right!\ (Track 8): suppressed; max local visible-person signal 2; confidence low.
- `bk0TmxoZlUY` — Advanced workshop: Mastering AI Observability (Track 9): suppressed; max local visible-person signal 1; confidence low.
- `JhJKgRAmfIU` — From framework to runtime: running agents with Foundry Agent Service (Track M): suppressed; max local visible-person signal 2; confidence low.
- `1t-9-s1brcg` — Get Started with Models in Microsoft Foundry to Build AI Apps (Track M): suppressed; max local visible-person signal 1; confidence low.

## Method Boundary
The local detector produces a review signal from sampled frames. It can miss people in dark rooms, count speakers instead of audience, and fail on slide-only captures. For that reason, only high-confidence results are displayed on talk pages.
