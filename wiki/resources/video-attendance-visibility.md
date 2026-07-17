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

- `I2cbIws9j10` at 6227s — Latent Space Live: the Inference Inflection from First Principles (Expo Stage 2 NW): suppressed; max local visible-person signal 3; confidence low.
- `I2cbIws9j10` at 11668s — Harness Engineering: Building the Production Cage for Powerful Domain Agents (Main Stage): suppressed; max local visible-person signal 3; confidence low.
- `I2cbIws9j10` at 4262s — How Anthropic Builds: Lessons from Labs (Main Stage): suppressed; max local visible-person signal 3; confidence low.
- `I2cbIws9j10` at 29906s — $100,000 AIE Startup Battlefield — presented by Hyperagent (Networking Room): suppressed; max local visible-person signal 5; confidence low.

## Method Boundary
The local detector produces a review signal from sampled frames. It can miss people in dark rooms, count speakers instead of audience, and fail on slide-only captures. For that reason, only high-confidence results are displayed on talk pages.
