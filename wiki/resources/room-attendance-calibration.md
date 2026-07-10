---
title: "Room Attendance Calibration"
category: "resources"
sourceLabels: ["Official conference schedule", "Local video frame sampling", "Attendance calibration"]
---
# Room Attendance Calibration

This page is a calibration layer for future attendance estimates. It does not publish final attendance counts. It groups scheduled rooms by available video evidence, camera behavior, and the estimation method that should be used for that room.

## Method
- Use official schedule room labels as canonical room IDs.
- Use local low-resolution video caches and sampled frame caches only as visual evidence.
- Treat visible people counts as lower bounds unless the frame clearly covers the whole audience area.
- Use confidence bands, not exact counts.

## Calibration Summary

- **Expo Stage 1 NE**: expo-floor stage; primary videos 0, supporting videos 2, evidence frames 12; use: camera-family proxy only; confidence: low. [contact sheet](/assets/attendance-calibration/expo-stage-1-ne.jpg)
- **Expo Stage 2 NW**: expo-floor stage; primary videos 1, supporting videos 1, evidence frames 12; use: partial visible-area calibration; confidence: medium-low. [contact sheet](/assets/attendance-calibration/expo-stage-2-nw.jpg)
- **Expo Stage 3 SW**: expo-floor stage; primary videos 0, supporting videos 2, evidence frames 12; use: camera-family proxy only; confidence: low. [contact sheet](/assets/attendance-calibration/expo-stage-3-sw.jpg)
- **Expo Stage 4 SE**: expo-floor stage; primary videos 0, supporting videos 1, evidence frames 6; use: camera-family proxy only; confidence: low. [contact sheet](/assets/attendance-calibration/expo-stage-4-se.jpg)
- **Leadership 1**: leadership breakout room; primary videos 0, supporting videos 1, evidence frames 6; use: camera-family proxy only; confidence: low. [contact sheet](/assets/attendance-calibration/leadership-1.jpg)
- **Leadership 2**: leadership breakout room; primary videos 0, supporting videos 3, evidence frames 18; use: camera-family proxy only; confidence: low. [contact sheet](/assets/attendance-calibration/leadership-2.jpg)
- **Leadership Lounge**: leadership breakout room; primary videos 0, supporting videos 1, evidence frames 6; use: camera-family proxy only; confidence: low. [contact sheet](/assets/attendance-calibration/leadership-lounge.jpg)
- **Main Stage**: large keynote/plenary room; primary videos 3, supporting videos 0, evidence frames 18; use: partial visible-area calibration; confidence: medium-low. [contact sheet](/assets/attendance-calibration/main-stage.jpg)
- **Networking Room**: lounge/networking room; primary videos 1, supporting videos 0, evidence frames 6; use: lower-bound visible-area calibration; confidence: low. [contact sheet](/assets/attendance-calibration/networking-room.jpg)
- **Track 1**: breakout track room; primary videos 1, supporting videos 1, evidence frames 12; use: partial visible-area calibration; confidence: medium-low. [contact sheet](/assets/attendance-calibration/track-1.jpg)
- **Track 2**: breakout track room; primary videos 0, supporting videos 1, evidence frames 6; use: camera-family proxy only; confidence: low. [contact sheet](/assets/attendance-calibration/track-2.jpg)
- **Track 3**: breakout track room; primary videos 0, supporting videos 1, evidence frames 6; use: camera-family proxy only; confidence: low. [contact sheet](/assets/attendance-calibration/track-3.jpg)
- **Track 4**: breakout track room; primary videos 0, supporting videos 2, evidence frames 12; use: camera-family proxy only; confidence: low. [contact sheet](/assets/attendance-calibration/track-4.jpg)
- **Track 5**: breakout track room; primary videos 0, supporting videos 2, evidence frames 12; use: camera-family proxy only; confidence: low. [contact sheet](/assets/attendance-calibration/track-5.jpg)
- **Track 6**: breakout track room; primary videos 1, supporting videos 2, evidence frames 18; use: partial visible-area calibration; confidence: medium-low. [contact sheet](/assets/attendance-calibration/track-6.jpg)
- **Track 7**: breakout track room; primary videos 0, supporting videos 1, evidence frames 6; use: camera-family proxy only; confidence: low. [contact sheet](/assets/attendance-calibration/track-7.jpg)
- **Track 8**: breakout track room; primary videos 0, supporting videos 3, evidence frames 18; use: camera-family proxy only; confidence: low. [contact sheet](/assets/attendance-calibration/track-8.jpg)
- **Track 9**: breakout track room; primary videos 0, supporting videos 1, evidence frames 6; use: camera-family proxy only; confidence: low. [contact sheet](/assets/attendance-calibration/track-9.jpg)
- **Track M**: breakout track room; primary videos 0, supporting videos 2, evidence frames 12; use: camera-family proxy only; confidence: low. [contact sheet](/assets/attendance-calibration/track-m.jpg)

## Calibration Table
| Room | Room family | Primary videos | Supporting videos | Evidence frames | Use | Confidence | Contact sheet |
| --- | --- | ---: | ---: | ---: | --- | --- | --- |
| Expo Stage 1 NE | expo-floor stage | 0 | 2 | 12 | camera-family proxy only | low | [sheet](/assets/attendance-calibration/expo-stage-1-ne.jpg) |
| Expo Stage 2 NW | expo-floor stage | 1 | 1 | 12 | partial visible-area calibration | medium-low | [sheet](/assets/attendance-calibration/expo-stage-2-nw.jpg) |
| Expo Stage 3 SW | expo-floor stage | 0 | 2 | 12 | camera-family proxy only | low | [sheet](/assets/attendance-calibration/expo-stage-3-sw.jpg) |
| Expo Stage 4 SE | expo-floor stage | 0 | 1 | 6 | camera-family proxy only | low | [sheet](/assets/attendance-calibration/expo-stage-4-se.jpg) |
| Leadership 1 | leadership breakout room | 0 | 1 | 6 | camera-family proxy only | low | [sheet](/assets/attendance-calibration/leadership-1.jpg) |
| Leadership 2 | leadership breakout room | 0 | 3 | 18 | camera-family proxy only | low | [sheet](/assets/attendance-calibration/leadership-2.jpg) |
| Leadership Lounge | leadership breakout room | 0 | 1 | 6 | camera-family proxy only | low | [sheet](/assets/attendance-calibration/leadership-lounge.jpg) |
| Main Stage | large keynote/plenary room | 3 | 0 | 18 | partial visible-area calibration | medium-low | [sheet](/assets/attendance-calibration/main-stage.jpg) |
| Networking Room | lounge/networking room | 1 | 0 | 6 | lower-bound visible-area calibration | low | [sheet](/assets/attendance-calibration/networking-room.jpg) |
| Track 1 | breakout track room | 1 | 1 | 12 | partial visible-area calibration | medium-low | [sheet](/assets/attendance-calibration/track-1.jpg) |
| Track 2 | breakout track room | 0 | 1 | 6 | camera-family proxy only | low | [sheet](/assets/attendance-calibration/track-2.jpg) |
| Track 3 | breakout track room | 0 | 1 | 6 | camera-family proxy only | low | [sheet](/assets/attendance-calibration/track-3.jpg) |
| Track 4 | breakout track room | 0 | 2 | 12 | camera-family proxy only | low | [sheet](/assets/attendance-calibration/track-4.jpg) |
| Track 5 | breakout track room | 0 | 2 | 12 | camera-family proxy only | low | [sheet](/assets/attendance-calibration/track-5.jpg) |
| Track 6 | breakout track room | 1 | 2 | 18 | partial visible-area calibration | medium-low | [sheet](/assets/attendance-calibration/track-6.jpg) |
| Track 7 | breakout track room | 0 | 1 | 6 | camera-family proxy only | low | [sheet](/assets/attendance-calibration/track-7.jpg) |
| Track 8 | breakout track room | 0 | 3 | 18 | camera-family proxy only | low | [sheet](/assets/attendance-calibration/track-8.jpg) |
| Track 9 | breakout track room | 0 | 1 | 6 | camera-family proxy only | low | [sheet](/assets/attendance-calibration/track-9.jpg) |
| Track M | breakout track room | 0 | 2 | 12 | camera-family proxy only | low | [sheet](/assets/attendance-calibration/track-m.jpg) |

## Room Notes

### Expo Stage 1 NE
- Camera model: open-stage camera; audience may stand or sit outside fixed rows
- Coverage: visible crowd varies strongly with booth traffic and camera pan
- Attendance method: estimate occupied standing/seating area from wide shots using sparse/medium/dense standing density bands

### Expo Stage 2 NW
- Camera model: open-stage camera; audience may stand or sit outside fixed rows
- Coverage: visible crowd varies strongly with booth traffic and camera pan
- Attendance method: estimate occupied standing/seating area from wide shots using sparse/medium/dense standing density bands

### Expo Stage 3 SW
- Camera model: open-stage camera; audience may stand or sit outside fixed rows
- Coverage: visible crowd varies strongly with booth traffic and camera pan
- Attendance method: estimate occupied standing/seating area from wide shots using sparse/medium/dense standing density bands

### Expo Stage 4 SE
- Camera model: open-stage camera; audience may stand or sit outside fixed rows
- Coverage: visible crowd varies strongly with booth traffic and camera pan
- Attendance method: estimate occupied standing/seating area from wide shots using sparse/medium/dense standing density bands

### Leadership 1
- Camera model: speaker/slide camera with limited audience views
- Coverage: audience evidence is sparse; use only wide or reverse shots
- Attendance method: prefer manual frame review; use detected visible rows only as a lower bound

### Leadership 2
- Camera model: speaker/slide camera with limited audience views
- Coverage: audience evidence is sparse; use only wide or reverse shots
- Attendance method: prefer manual frame review; use detected visible rows only as a lower bound

### Leadership Lounge
- Camera model: speaker/slide camera with limited audience views
- Coverage: audience evidence is sparse; use only wide or reverse shots
- Attendance method: prefer manual frame review; use detected visible rows only as a lower bound

### Main Stage
- Camera model: front-of-room stage camera with occasional wide audience visibility in livestream/cut footage
- Coverage: front/center audience is sometimes visible; rear and far side seating usually hidden
- Attendance method: count visible seats/heads in wide shots, then scale by visible-room fraction; cap against large-room keynote capacity once venue capacity is verified

### Networking Room
- Camera model: event/livestream context rather than stable talk capture
- Coverage: camera evidence is likely partial and movement-heavy
- Attendance method: estimate active participants in visible area; do not infer total attendance without room-specific capacity

### Track 1
- Camera model: fixed speaker/slide camera; audience usually off-axis, with occasional wide shots
- Coverage: front rows or side aisles may be visible; full room usually hidden
- Attendance method: count visible rows/heads where available, scale by estimated visible-room fraction, and cap by verified track-room capacity

### Track 2
- Camera model: fixed speaker/slide camera; audience usually off-axis, with occasional wide shots
- Coverage: front rows or side aisles may be visible; full room usually hidden
- Attendance method: count visible rows/heads where available, scale by estimated visible-room fraction, and cap by verified track-room capacity

### Track 3
- Camera model: fixed speaker/slide camera; audience usually off-axis, with occasional wide shots
- Coverage: front rows or side aisles may be visible; full room usually hidden
- Attendance method: count visible rows/heads where available, scale by estimated visible-room fraction, and cap by verified track-room capacity

### Track 4
- Camera model: fixed speaker/slide camera; audience usually off-axis, with occasional wide shots
- Coverage: front rows or side aisles may be visible; full room usually hidden
- Attendance method: count visible rows/heads where available, scale by estimated visible-room fraction, and cap by verified track-room capacity

### Track 5
- Camera model: fixed speaker/slide camera; audience usually off-axis, with occasional wide shots
- Coverage: front rows or side aisles may be visible; full room usually hidden
- Attendance method: count visible rows/heads where available, scale by estimated visible-room fraction, and cap by verified track-room capacity

### Track 6
- Camera model: fixed speaker/slide camera; audience usually off-axis, with occasional wide shots
- Coverage: front rows or side aisles may be visible; full room usually hidden
- Attendance method: count visible rows/heads where available, scale by estimated visible-room fraction, and cap by verified track-room capacity

### Track 7
- Camera model: fixed speaker/slide camera; audience usually off-axis, with occasional wide shots
- Coverage: front rows or side aisles may be visible; full room usually hidden
- Attendance method: count visible rows/heads where available, scale by estimated visible-room fraction, and cap by verified track-room capacity

### Track 8
- Camera model: fixed speaker/slide camera; audience usually off-axis, with occasional wide shots
- Coverage: front rows or side aisles may be visible; full room usually hidden
- Attendance method: count visible rows/heads where available, scale by estimated visible-room fraction, and cap by verified track-room capacity

### Track 9
- Camera model: fixed speaker/slide camera; audience usually off-axis, with occasional wide shots
- Coverage: front rows or side aisles may be visible; full room usually hidden
- Attendance method: count visible rows/heads where available, scale by estimated visible-room fraction, and cap by verified track-room capacity

### Track M
- Camera model: fixed speaker/slide camera; audience usually off-axis, with occasional wide shots
- Coverage: front rows or side aisles may be visible; full room usually hidden
- Attendance method: count visible rows/heads where available, scale by estimated visible-room fraction, and cap by verified track-room capacity


## Evidence Videos

### Expo Stage 1 NE
- `BiG2ssibKGc` — supporting-related-video; Beyond RAG: See a relational context engine reduce token burn (wiki/talks/2026-07-01-brandon-waselnuk-beyond-rag-see-a-relational-context-engine-reduce-token-burn.md)
- `Bc6Ojl2XS1w` — supporting-related-video; Can Your Agent Hear You Now? (wiki/talks/2026-06-29-thor-schaeff-can-your-agent-hear-you-now.md)

### Expo Stage 2 NW
- `I2cbIws9j10` at 6227s — worldsfair-livestream-segment; Latent Space Live: the Inference Inflection from First Principles (wiki/talks/2026-07-01-swyx-latent-space-live-the-inference-inflection-from-first-principles.md)
- `PmZDupFP3UM` — supporting-related-video; AI-Assisted Engineering: 5 Trends We're Seeing From 500+ Organizations (wiki/talks/2026-06-30-justin-reock-ai-assisted-engineering-5-trends-we-re-seeing-from-500-organizations.md)

### Expo Stage 3 SW
- `xz0-brt56L8` — supporting-related-video; An Interaction Is All You Need (wiki/talks/2026-07-01-ivan-leo-an-interaction-is-all-you-need.md)
- `NuePCNMpWGc` — supporting-related-video; Expo Welcome Speech (wiki/talks/2026-06-29-sonar-expo-welcome-speech.md)

### Expo Stage 4 SE
- `BM2JX9hqsVQ` — supporting-related-video; An AI Future Without the Lock-In (wiki/talks/2026-07-01-remy-guercio-an-ai-future-without-the-lock-in.md)

### Leadership 1
- `tzRvcTEapzo` — supporting-related-video; All the Things We Have to Do to Satisfy Your Insatiable Need for Tokens (wiki/talks/2026-07-01-daniel-kim-all-the-things-we-have-to-do-to-satisfy-your-insatiable-need-for-tokens.md)

### Leadership 2
- `bSG9wUYaHWU` — supporting-related-video; Coding Agents Don't Scale Themselves. Neither Do Your Teams.The Rise of Agent Enablement. (wiki/talks/2026-07-01-patrick-debois-coding-agents-don-t-scale-themselves-neither-do-your-teams-the-rise-of-agent-enablement.md)
- `Lc8zRh9muoY` — supporting-related-video; FinOps for AI Agents: Who Spent All the Tokens? (wiki/talks/2026-07-01-tisha-chawla-finops-for-ai-agents-who-spent-all-the-tokens.md)
- `JhJKgRAmfIU` — supporting-related-video; I Let Agents Refactor My Codebase for 3 Weeks. Then I Read the Code. (wiki/talks/2026-06-30-keiji-kanazawa-i-let-agents-refactor-my-codebase-for-3-weeks-then-i-read-the-code.md)

### Leadership Lounge
- `SZStlIhyTCY` — supporting-related-video; Tokenomics: From AI Spend to AI Value (wiki/talks/2026-06-30-martin-harrysson-tokenomics-from-ai-spend-to-ai-value.md)

### Main Stage
- `I2cbIws9j10` at 28640s — worldsfair-livestream-segment; Closing Keynote: Garry Tan (wiki/talks/2026-07-01-garry-tan-closing-keynote-garry-tan.md)
- `I2cbIws9j10` at 11668s — worldsfair-livestream-segment; Harness Engineering: Building the Production Cage for Powerful Domain Agents (wiki/talks/2026-07-01-mike-chambers-harness-engineering-building-the-production-cage-for-powerful-domain-agents.md)
- `I2cbIws9j10` at 4262s — worldsfair-livestream-segment; How Anthropic Builds: Lessons from Labs (wiki/talks/2026-07-01-mike-krieger-how-anthropic-builds-lessons-from-labs.md)

### Networking Room
- `I2cbIws9j10` at 29906s — worldsfair-livestream-segment; $100,000 AIE Startup Battlefield — presented by Hyperagent (wiki/talks/2026-07-01-howie-liu-100-000-aie-startup-battlefield-presented-by-hyperagent.md)

### Track 1
- `AheG9p_JXVw` — candidate-session-video; Building an Agentic Video Editor for Mass Consumer (wiki/talks/2026-07-01-ekaterina-deyneka-building-an-agentic-video-editor-for-mass-consumer.md)
- `wsFd22SL1s8` — supporting-related-video; 'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt 1' (wiki/talks/2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1.md)

### Track 2
- `B9h9ovW5H9U` — supporting-related-video; AI on Your Lakehouse: Context Comes in Shapes, Not Queries (wiki/talks/2026-06-29-zach-blumenfeld-ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md)

### Track 3
- `dvft0Gp9sEE` — supporting-related-video; Cooking with Codex (wiki/talks/2026-06-29-charlie-guo-cooking-with-codex.md)

### Track 4
- `Bc6Ojl2XS1w` — supporting-related-video; Build realtime multimodal agents with Gemini Live (continued 2) (wiki/talks/2026-06-30-thor-schaeff-build-realtime-multimodal-agents-with-gemini-live-continued-2.md)
- `1t-9-s1brcg` — supporting-related-video; The model swap workshop (wiki/talks/2026-06-29-pamela-fox-the-model-swap-workshop.md)

### Track 5
- `7Dtu2bilcFs` — supporting-related-video; Agentic Security: Permissions, Provenance, and the Agent Supply Chain (wiki/talks/2026-06-29-steve-yegge-agentic-security-permissions-provenance-and-the-agent-supply-chain.md)
- `liG97YXaTSA` — supporting-related-video; Everything Is a Rollout (wiki/talks/2026-06-30-alex-shaw-everything-is-a-rollout.md)

### Track 6
- `I2cbIws9j10` at 7876s — worldsfair-livestream-segment; Context Engineering in 2026: Compaction, Memory & Cost (wiki/talks/2026-06-29-louis-fran-ois-bouchard-context-engineering-in-2026-compaction-memory-and-cost.md)
- `gcseUQJ6Gbg` — supporting-related-video; The Missing Layer: Design Taste in AI Agents // Stop Letting Your Agents Ship Ugly UIs (wiki/talks/2026-06-30-hassan-el-mghari-the-missing-layer-design-taste-in-ai-agents-stop-letting-your-agents-ship-ugly-uis.md)
- `dvft0Gp9sEE` — supporting-related-video; Voice Agents Can Just Do Things (wiki/talks/2026-06-29-charlie-guo-voice-agents-can-just-do-things.md)

### Track 7
- `u3NofYYstaY` — supporting-related-video; 200 Million Patient Interactions Later: What the Generic Voice Stack Misses (wiki/talks/2026-07-01-vivek-muppalla-200-million-patient-interactions-later-what-the-generic-voice-stack-misses.md)

### Track 8
- `-cKUW6n8hBU` — supporting-related-video; 'It’s Tokens All The Way Down: How RLMs are Different' (wiki/talks/2026-06-30-kevin-madura-it-s-tokens-all-the-way-down-how-rlms-are-different.md)
- `SbUxRluVRwk` — supporting-related-video; Benchmarking Coding Agents on New vs Legacy Code bases (wiki/talks/2026-07-01-denys-linkov-benchmarking-coding-agents-on-new-vs-legacy-code-bases.md)
- `BiG2ssibKGc` — supporting-related-video; Your agents lack context: Here's how to fix \"You're absolutely right!\ (wiki/talks/2026-06-30-brandon-waselnuk-your-agents-lack-context-here-s-how-to-fix-you-re-absolutely-right.md)

### Track 9
- `bk0TmxoZlUY` — supporting-related-video; Advanced workshop: Mastering AI Observability (wiki/talks/2026-06-29-doug-guthrie-advanced-workshop-mastering-ai-observability.md)

### Track M
- `JhJKgRAmfIU` — supporting-related-video; From framework to runtime: running agents with Foundry Agent Service (wiki/talks/2026-06-30-tina-manghnani-from-framework-to-runtime-running-agents-with-foundry-agent-service.md)
- `1t-9-s1brcg` — supporting-related-video; Get Started with Models in Microsoft Foundry to Build AI Apps (wiki/talks/2026-06-29-pamela-fox-get-started-with-models-in-microsoft-foundry-to-build-ai-apps.md)


## Estimation Bands
- Sparse seated room: many gaps; use visible occupied seats directly where rows are clear.
- Medium seated room: most front/middle rows occupied with visible gaps; scale visible rows by room coverage.
- Dense seated room: rows appear nearly full; cap by verified room seat capacity instead of extrapolating from detections.
- Expo standing crowd: use standing density bands per visible square meter only when floor area is visible; otherwise report a lower bound.

## Evidence Boundary
The table is derived from sampled video frames and schedule metadata. It should be reviewed before any talk page receives an attendance estimate.
