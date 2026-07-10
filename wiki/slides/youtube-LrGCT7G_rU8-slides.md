---
title: "Slides: Using RL Agent to Detect and Remediate ETL Pipeline Failures - Anna Marie Benzon"
category: "slides"
video_id: "LrGCT7G_rU8"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: Using RL Agent to Detect and Remediate ETL Pipeline Failures - Anna Marie Benzon

## Source Video
[Using RL Agent to Detect and Remediate ETL Pipeline Failures - Anna Marie Benzon](https://www.youtube.com/watch?v=LrGCT7G_rU8)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/LrGCT7G_rU8/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/LrGCT7G_rU8/slide-001.html)
- AI slide classifier: `title_card` confidence `0.99`
- Text source: agent_vision.

Slide text:

> Using RL-based Agent to Detect and Remediate ETL Pipeline Failures
> Presenter: Anna Marie Benzon
> University of the Philippines, Diliman
> github.com/ambenzon27/rl-etl-remediation-agent

![[assets/slides/LrGCT7G_rU8/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/LrGCT7G_rU8/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast`.
- OCR decision: ready — Dense multi-item slide with smaller body text and icon labels.

Slide text:

> Failure Inspect Logs Diagnose Repair Rerun Validate
> Late or unavailable source data
> The 日日日 Schema drift
> Problem Null-rate spikes Datetime parsing incompatibilities
> Cloud ETL jobs break because of:
> Type changes
> Unknown runtime errors
> Modeled manual MTTR ~ 2.5 working days

![[assets/slides/LrGCT7G_rU8/slide-003.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/LrGCT7G_rU8/slide-003.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Architecture diagram and multiple text regions are better handled by OCR than direct transcription in triage.

Slide text:

> Phate 1 Architecture -- Al Pipeline Heulth Agent
> An End-to-End RL Pipeline
> Health Agent for Anomaly
> Detection and Autonomous
> Self-Healing of Cloud Data
> t tt+e+ + At Pipelines
> t cttt th
> : NOTE: GENERAUZED PUDUKC REFERENCE ARCHTTECTURE
> Solution The Monitor → Diagnose → Score → Decide → Safety → Act Validate 2.Diagnose the likely failure family: 5.Validate whether the action restored a healthy state 3.Estimate operational risk 4.Select a bounded remediation action 1.observe logs, schema, and data-quality conditions

![[assets/slides/LrGCT7G_rU8/slide-004.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/LrGCT7G_rU8/slide-004.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Diagram-heavy slide with small labels and policy text; OCR is better than direct extraction.

Slide text:

> Deterministic Anomaly Rules Schema drift, null spikes, field
> removals, type changes
> Q-Learning Decision Policy Retry, coerce schema, rollback,. quarantine, escalate, log The
> Critical anomaly.+ passive action Safety Override Intelligence
> - escalate Layer

![[assets/slides/LrGCT7G_rU8/slide-005.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/LrGCT7G_rU8/slide-005.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast`.
- OCR decision: ready — Table layout with multiple small cells is OCR-suitable.

Slide text:

> Detection and Diagnosis
> Establish the Facts Before Choosing an Action
> Component Responsibility
> Schema profiler Structure, types, nesting. null rates
> Drift detector Additions.removals.type changes
> Data-quality analyzer Completeness, validity. consistency
> Error classifier Converts log patterns into failure categories
> Risk scorer Produces an operational risk level
> Deterministic prototype with limited dataset; ML-ready with richer incident history.

![[assets/slides/LrGCT7G_rU8/slide-006.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/LrGCT7G_rU8/slide-006.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Two-column state/action slide with small text and a footnote is OCR-suitable.

Slide text:

> RL Selects the Response, Not the Facts
> State: Action:.
> retry [coerce] rollback quarantine oscalato [log]
> 1.Failure category
> 4.Drift severity 3.Retry count 2.Risk level 2.Small, interpretable statespace: 3.Low-memory.inference: 1. Tabular Q-learning
> 5.Data-quality condition 4.Inspectable Q-values for every decision
> TeChNICALlY, ThIS IS a SInGLE-StEp CONTexTUAL DECISIoN prOBLem IMPlEmENTeD WiTH TaBULaR Q-LeaRnInG.:
> -:-

![[assets/slides/LrGCT7G_rU8/slide-007.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/LrGCT7G_rU8/slide-007.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.

Slide text:

> Safe Autonomy
> The Learned Policy Does Not Have Final Authority
> 1. Q-learning policy proposes an action
> 2. Safety layer evaluates critical anomalies
> 3. Unsafe passive actions are overridden
> 4. High-risk and unknown conditions escalate
> 5. Every decision produces an audit record
> Escalation is a correct action, not a failure of autonomy.

![[assets/slides/LrGCT7G_rU8/slide-008.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/LrGCT7G_rU8/slide-008.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Dense code screenshot and multi-column content are better suited to OCR than direct transcription.

Slide text:

> Example Failure
> ntriggered_at*: "2026-05-21te2:05:20z*, "job_name": " Synthotic_etl Job ", - [A] Real Gtue job failure
> "error_classification": { "error_tyPe": "PAIeTIME_FOfRAL ERROR". "confidence": o.90, - (B] classified by Error Classifle
> scheaa/date foreat y. "recoamended_action": "APPLY_SCHEHA_COERCIoN" - [C] Rule engine says: coerce
> "anonaly_override": fatse, - [E] Safety override did not fire + [o] Agent selects scheas coerclon
> "reaedlation": { "note": -Hanual Gtue script update required" - [F] Loggcd for review "success": falsc,
> Observed condition 1.Glue-style job fallure event Decision? 1.Policy selects schema coercion
> received 2.safety override does not fire
> 2:Datetime-format incompatibility detected 3.Automatic coercion.is unavailable 4.lncident is logged for manual reviev
> 3.Error classified with 0.90
> confidence

![[assets/slides/LrGCT7G_rU8/slide-009.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/LrGCT7G_rU8/slide-009.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Small body text and embedded screenshot are better handled by OCR.

Slide text:

> ReproducibleEvaluation
> Designed for Independent Reproductior
> 1.Generalized AWs Lambda-style remediation-agent ambenzon27/rl-etl-
> 2.synthetic schemas, records, logs, and incidents architecture PLitLided ETL rerptataon L(ert ia tchtra -drn tvhtle brchmMi, ard Ais Llnbdh deyitor, enar cintilcenor, Qremrlng dtctTenr Yo
> 5.Robustness check across 30 runs, seeds 4.Four controlled experiments: El-E4 3.No production data or infrastructure identifiers: GTEo AL guita E?l Ttltdttan tgtl 1r TaTtai tttatr, tt atia Dulewto uoa.uwp oie 'uayphtp upio
> 6.Results reported with 95% confidence intervals 42-71 available in the GitHub Public benchmark and tests are
> repository

![[assets/slides/LrGCT7G_rU8/slide-010.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/LrGCT7G_rU8/slide-010.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Chart labels and benchmark metrics are small and OCR-suitable.

Slide text:

> Evaluation Results
> Controlled synthetic benchmark 30 seeds, mean ± 95% cl Htean iie to itcdiey, shotn on a log scale MTTR Drops from Days to Minutes in the Benchmark
> 1.Rule-based anomaly detector 10.000 2.5 working days
> 2.Recall: 0.800 Precision' 1.000 Loco -99.85% 10vor MTTR
> 3.FI: 0.889 100
> 4.Rl successful-cdse resolution tim approximately.5.2 minutes 5.24 +l 0.14 pnn
> 5.RL simulated success rate: 74.63 ± 1.51%
> tion rate: 88.63 ± 0.89% nadent rtspord+ KSEE syher bechat RiL helth sgent
> A ret yhdudhen rdnl eelorte.

![[assets/slides/LrGCT7G_rU8/slide-011.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/LrGCT7G_rU8/slide-011.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Small quantitative plot labels and dense bullet text are OCR-suitable.

Slide text:

> Robustness and Ablation
> What produced reliability?
> 1.RL:success matched the
> deterministic pol 100± 30 synthetic seeds; mean ± 95% Cl
> 2.Deterministic rules beat random percentage-point'difference -15.03 ± 0.66 pp
> selection by.15:63 ±'1.86 points Safety override
> 3.The safety override reduced vs none +0.00 ±:0.19 pp
> 4.RL provided an inspectable learned policy; butdid not points non-escalation by.15:03:± 0.66 Rules vs random RL vs rules +15.63 ± 1.86 pp
> outperform.rules in this -15 -10 -5 0 5 10 15
> icnmg Difference (percentage points)
> 5.Structured decision'logic and
> external guardrails produced
> nost of the reliability

![[assets/slides/LrGCT7G_rU8/slide-012.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/LrGCT7G_rU8/slide-012.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.

Slide text:

> What This Prototype Does Not Yet Prove
> 1. Results are based on synthetic benchmark scenarios
> 2. The agent is failure-triggered, not a pre-failure predictor
> 3. Production incident diversity may exceed the current state space
> 4. Some remediation actions remain simulated or bounded
> 5. Online learning requires strict operational approval gates
> This demonstrates feasibility and system design, not production completeness.

![[assets/slides/LrGCT7G_rU8/slide-013.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/LrGCT7G_rU8/slide-013.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.

Slide text:

> Small AI Can Still Deliver Operational Value
> 1. Use deterministic logic for observable facts
> 2. Use RL where contextual action selection adds value
> 3. Place safety constraints outside the learned policy
> 4. Treat escalation and validation as core capabilities
> 5. Evaluate across repeated seeds, not one favorable run

![[assets/slides/LrGCT7G_rU8/slide-014.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/LrGCT7G_rU8/slide-014.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.

Slide text:

> From reactive debugging to intelligent recovery!
> The goal is not to replace human judgment.
> It is to reserve it for the failures that truly need it.
> Before:
> - Manual log inspection
> - Schema tracing
> - Delayed dashboards
> - Modeled MTTR: 2.5 working days
> After:
> - Event-triggered diagnosis
> - RL-guided remediation
> - Safety-constrained escalation
> - Minutes-scale recovery


Classification audit: `raw/sources/slide-ai-classification/slides/LrGCT7G_rU8/audit.json`

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
