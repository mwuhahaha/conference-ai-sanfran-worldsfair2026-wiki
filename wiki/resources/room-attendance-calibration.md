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

- **Expo Stage 1 NE**: expo-floor stage; primary videos 0, supporting videos 0, evidence frames 0; use: not enough visual evidence; confidence: low.
- **Expo Stage 2 NW**: expo-floor stage; primary videos 1, supporting videos 0, evidence frames 6; use: partial visible-area calibration; confidence: medium-low. [contact sheet](/assets/attendance-calibration-v1/expo-stage-2-nw.jpg)
- **Expo Stage 3 SW**: expo-floor stage; primary videos 0, supporting videos 0, evidence frames 0; use: not enough visual evidence; confidence: low.
- **Expo Stage 4 SE**: expo-floor stage; primary videos 0, supporting videos 0, evidence frames 0; use: not enough visual evidence; confidence: low.
- **Leadership 1**: leadership breakout room; primary videos 0, supporting videos 0, evidence frames 0; use: not enough visual evidence; confidence: low.
- **Leadership 2**: leadership breakout room; primary videos 0, supporting videos 0, evidence frames 0; use: not enough visual evidence; confidence: low.
- **Leadership Lounge**: leadership breakout room; primary videos 0, supporting videos 0, evidence frames 0; use: not enough visual evidence; confidence: low.
- **Main Stage**: large keynote/plenary room; primary videos 2, supporting videos 0, evidence frames 12; use: partial visible-area calibration; confidence: medium-low. [contact sheet](/assets/attendance-calibration-v1/main-stage.jpg)
- **Networking Room**: lounge/networking room; primary videos 1, supporting videos 0, evidence frames 6; use: lower-bound visible-area calibration; confidence: low. [contact sheet](/assets/attendance-calibration-v1/networking-room.jpg)
- **Track 1**: breakout track room; primary videos 0, supporting videos 0, evidence frames 0; use: not enough visual evidence; confidence: low.
- **Track 2**: breakout track room; primary videos 0, supporting videos 0, evidence frames 0; use: not enough visual evidence; confidence: low.
- **Track 3**: breakout track room; primary videos 0, supporting videos 0, evidence frames 0; use: not enough visual evidence; confidence: low.
- **Track 4**: breakout track room; primary videos 0, supporting videos 0, evidence frames 0; use: not enough visual evidence; confidence: low.
- **Track 5**: breakout track room; primary videos 0, supporting videos 0, evidence frames 0; use: not enough visual evidence; confidence: low.
- **Track 6**: breakout track room; primary videos 0, supporting videos 0, evidence frames 0; use: not enough visual evidence; confidence: low.
- **Track 7**: breakout track room; primary videos 0, supporting videos 0, evidence frames 0; use: not enough visual evidence; confidence: low.
- **Track 8**: breakout track room; primary videos 0, supporting videos 0, evidence frames 0; use: not enough visual evidence; confidence: low.
- **Track 9**: breakout track room; primary videos 0, supporting videos 0, evidence frames 0; use: not enough visual evidence; confidence: low.
- **Track M**: breakout track room; primary videos 0, supporting videos 0, evidence frames 0; use: not enough visual evidence; confidence: low.

## Calibration Table
| Room | Room family | Primary videos | Supporting videos | Evidence frames | Use | Confidence | Contact sheet |
| --- | --- | ---: | ---: | ---: | --- | --- | --- |
| Expo Stage 1 NE | expo-floor stage | 0 | 0 | 0 | not enough visual evidence | low |  |
| Expo Stage 2 NW | expo-floor stage | 1 | 0 | 6 | partial visible-area calibration | medium-low | [sheet](/assets/attendance-calibration-v1/expo-stage-2-nw.jpg) |
| Expo Stage 3 SW | expo-floor stage | 0 | 0 | 0 | not enough visual evidence | low |  |
| Expo Stage 4 SE | expo-floor stage | 0 | 0 | 0 | not enough visual evidence | low |  |
| Leadership 1 | leadership breakout room | 0 | 0 | 0 | not enough visual evidence | low |  |
| Leadership 2 | leadership breakout room | 0 | 0 | 0 | not enough visual evidence | low |  |
| Leadership Lounge | leadership breakout room | 0 | 0 | 0 | not enough visual evidence | low |  |
| Main Stage | large keynote/plenary room | 2 | 0 | 12 | partial visible-area calibration | medium-low | [sheet](/assets/attendance-calibration-v1/main-stage.jpg) |
| Networking Room | lounge/networking room | 1 | 0 | 6 | lower-bound visible-area calibration | low | [sheet](/assets/attendance-calibration-v1/networking-room.jpg) |
| Track 1 | breakout track room | 0 | 0 | 0 | not enough visual evidence | low |  |
| Track 2 | breakout track room | 0 | 0 | 0 | not enough visual evidence | low |  |
| Track 3 | breakout track room | 0 | 0 | 0 | not enough visual evidence | low |  |
| Track 4 | breakout track room | 0 | 0 | 0 | not enough visual evidence | low |  |
| Track 5 | breakout track room | 0 | 0 | 0 | not enough visual evidence | low |  |
| Track 6 | breakout track room | 0 | 0 | 0 | not enough visual evidence | low |  |
| Track 7 | breakout track room | 0 | 0 | 0 | not enough visual evidence | low |  |
| Track 8 | breakout track room | 0 | 0 | 0 | not enough visual evidence | low |  |
| Track 9 | breakout track room | 0 | 0 | 0 | not enough visual evidence | low |  |
| Track M | breakout track room | 0 | 0 | 0 | not enough visual evidence | low |  |

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
- No local visual evidence available yet.

### Expo Stage 2 NW
- `I2cbIws9j10` at 6227s — worldsfair-livestream-segment; Latent Space Live: the Inference Inflection from First Principles (wiki/talks/2026-07-01-swyx-latent-space-live-the-inference-inflection-from-first-principles.md)

### Expo Stage 3 SW
- No local visual evidence available yet.

### Expo Stage 4 SE
- No local visual evidence available yet.

### Leadership 1
- No local visual evidence available yet.

### Leadership 2
- No local visual evidence available yet.

### Leadership Lounge
- No local visual evidence available yet.

### Main Stage
- `I2cbIws9j10` at 11668s — worldsfair-livestream-segment; Harness Engineering: Building the Production Cage for Powerful Domain Agents (wiki/talks/2026-07-01-mike-chambers-harness-engineering-building-the-production-cage-for-powerful-domain-agents.md)
- `I2cbIws9j10` at 4262s — worldsfair-livestream-segment; How Anthropic Builds: Lessons from Labs (wiki/talks/2026-07-01-mike-krieger-how-anthropic-builds-lessons-from-labs.md)

### Networking Room
- `I2cbIws9j10` at 29906s — worldsfair-livestream-segment; $100,000 AIE Startup Battlefield — presented by Hyperagent (wiki/talks/2026-07-01-howie-liu-100-000-aie-startup-battlefield-presented-by-hyperagent.md)

### Track 1
- No local visual evidence available yet.

### Track 2
- No local visual evidence available yet.

### Track 3
- No local visual evidence available yet.

### Track 4
- No local visual evidence available yet.

### Track 5
- No local visual evidence available yet.

### Track 6
- No local visual evidence available yet.

### Track 7
- No local visual evidence available yet.

### Track 8
- No local visual evidence available yet.

### Track 9
- No local visual evidence available yet.

### Track M
- No local visual evidence available yet.


## Estimation Bands
- Sparse seated room: many gaps; use visible occupied seats directly where rows are clear.
- Medium seated room: most front/middle rows occupied with visible gaps; scale visible rows by room coverage.
- Dense seated room: rows appear nearly full; cap by verified room seat capacity instead of extrapolating from detections.
- Expo standing crowd: use standing density bands per visible square meter only when floor area is visible; otherwise report a lower bound.

## Evidence Boundary
The table is derived from sampled video frames and schedule metadata. It should be reviewed before any talk page receives an attendance estimate.
