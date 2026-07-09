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

OCR text:

> Using RL-based Agent to
> 
> Detect and Remediate aan
> 
> ETL Pipeline Failures an
> 
> =
> 
> Ea bad aad
> 
> Presenter:
> 
> : Anna Marie Benzon
> University of the Philippines, Diliman
> github.com/ambenzon27/rl-etl-remediation-agent

![[assets/slides/LrGCT7G_rU8/slide-002.jpg]]

OCR text:

> : PS ~ ED ~ EE - A -  - E
> . Ca Late or unavailable source data
> Th . Schema drift
> e -
> GN Datetime parsing incompatibilities
> Problem *
> ®) Null-rate spikes
> Cloud ETL jobs break because of:
> tes ,
> 4d, Type changes
> : =,» . = Unknown runtime errors
> 7 a Modeled manual MTTR ~ 2.5 working days

![[assets/slides/LrGCT7G_rU8/slide-003.jpg]]

OCR text:

> Phave 1 Architecture ~ Al Pipeline Health Agent
> An End-to-End RL Pipeline
> Health Agent for Anomaly
> | —E ia Detection and Autonomous
> apa Self-Healing of Cloud Data
> = reais
> SCTE GENERA AES HERERERERARRARETUICETAE
> Monitor + Diagnose — Score > Decide —> Safety > Act — Validate
> l.Observe logs, schema, and data-quality conditions
> 2.Diagnose the likely failure family
> e 3.Estimate operational risk
> 
> 4.Select a bounded remediation action
> 5.Validate whether the action restored a healthy state

![[assets/slides/LrGCT7G_rU8/slide-004.jpg]]

OCR text:

> Deterministic Anomaly Rules
> Schema drift, null spikes, field
> removals, type changes
> Q-Learning Decision Policy
> Retry, coerce schema, rollback,
> quarantine, escalate, log
> Safety Override e Th :
> Critical anomaly + passive action
> ver intelligence

![[assets/slides/LrGCT7G_rU8/slide-005.jpg]]

OCR text:

> : Detection and Diagnosis
> Establish the Facts Before Choosing an Action
> Schema profiler Structure, types. nesting. null rates
> Drift detector Additions. removals. type changes
> Data-quality analyzer Completeness, validity, consistency
> ‘Converts log patterns into failure categories
> Deterministic prototype with limited dataset; ML-ready with richer incident history.

![[assets/slides/LrGCT7G_rU8/slide-006.jpg]]

OCR text:

> RL Selects the Response, Not the Facts
> Action:
> 
> State:
> 1.Failure category
> 2.Risk level 1.Tabular Q-learning
> 3.Retry count 2.Small, interpretable state space
> 4.Drift severity 3.Low-memory inference
> 5.Data-quality condition 4.Inspectable Q-values for every decision
> 
> “TECHNICALLY, THIS IS A SINGLE-STEP CONTEXTUAL DECISION PROBLEM IMPLEMENTED WITH TABULAR O-LEARNING.

![[assets/slides/LrGCT7G_rU8/slide-007.jpg]]

OCR text:

> : Safe Autonomy
> The Learned Policy Does Not Have Final Authority
> 1.Q-learning policy proposes an action
> 2.Safety layer evaluates critical anomalies .
> 3.Unsafe passive actions are overridden
> 4.High-risk and unknown conditions escalate
> 5.Every decision produces an audit record Ez
> a \
> 4 = Escalation is a correct action, not a failure of autonomy.

![[assets/slides/LrGCT7G_rU8/slide-008.jpg]]

OCR text:

> | Example Failure
> * wjob_names =, synthetic etLjob «,
> “triggered_at": “2026-05-21702:05:202", = {A} Real Glue job failure
> "error_classification": {
> “error_type": “DATETIME FORMAL ERROR”. + {B] Classified by Error Classifier
> "confidence": 6.98,
> . “root_cause": “Spark 3 datetime format incompatibility”,
> “recommended_action”: “APPLY_SCHEMA_COERCION” - [C] Rule engine says: coerce
> Sefema/date format
> “selected_action": “APPLY_SCHEMA_COERCION”, - [D] Agent selects schema coercion
> "“anomaly_override’: false, ~ {E] Safety override did not fire .
> remediation": {
> “success”: false,
> ) note": “Manual Glue script update required” - {F] Logged for review
> }
> Observed condition Decision
> 1.Glue-style job failure event 1.Policy selects schema coercion
> received 2.Safety override does not fire
> . 2.Datetime-format incompatibility 3.Automatic coercion is unavailable
> detected 4.Incident is logged for manual review
> 3.Error classified with 0.90 ;
> confidence

![[assets/slides/LrGCT7G_rU8/slide-009.jpg]]

OCR text:

> | Reproducible Evaluation
> Designed for Independent Reproduction
> ambenzon27/rl-etl-
> 1.Generalized AWS Lambda-style remediation-agent a
> architecture Sn eae
> 2.Synthetic schemas, records, logs, and Seg, 6
> incidents ——EEEEEE
> 3.No production data or infrastructure reeercrnenceecacngert gated ET ran ser
> identifiers Se reese erces erm
> 4.Four controlled experiments: E1-E4 Snares
> 5.Robustness check across 30 runs, seeds
> 42-71
> 6.Results reported with 95% confidence C> Public benchmark and tests are
> ‘intervals ‘ ; available in the GitHub
> repository. &

![[assets/slides/LrGCT7G_rU8/slide-010.jpg]]

OCR text:

> | Evaluation Results
> Controlled synthetic benchmark MTTR Drops from Days to Minutes in the Benchmark
> — 30 seeds, mean # 95% Cl . a
> . 2.5 working days
> 1.Rule-based anomaly detector: a
> Precision 1.000 “ 99.85% lower MTTR
> 2.Recall: 0.800 i
> 3.F1: 0.889 EF
> 4.RL successful-case resolution time: sztcnoraohe
> approximately 5.2 minutes
> 5.RL simulated success rate: 74.63 + 1.51% il
> 6.RL non-escalation rate: 88.63 + 0.89% uaa ””””S:CRC age

![[assets/slides/LrGCT7G_rU8/slide-011.jpg]]

OCR text:

> | Robustness and Ablation
> What produced reliability?
> 
> 1.RL success matched the , ,
> deterministic policy: 0.00 + 0.19 30 synthetic seeds; mean + 95% Cl
> percentage-point difference -
> 
> 2.Deterministic rules beat random -15.03 + 0.66 pp
> selection by 15.63 + 1.86 points Safety override jel
> 
> 3.The safety override reduced vs hone +0.00 + 0.19 pp
> non-escalation by 15.03 + 0.66 RL vs rules ®
> 
> 4 Dawa ‘ded oni tab +15.63 + 1.86 pp
> .RL provided an inspectable
> learned policy, but did not Rules vs random Fe
> outperform rules in this -15 -10 -S5 0 5 10. 15
> benchmark Difference (percentage points)
> 
> 5.Structured decision logic and
> external guardrails produced at
> most of the reliability ti

![[assets/slides/LrGCT7G_rU8/slide-012.jpg]]

OCR text:

> What This Prototype Does Not Yet Prove
> 1.Results are based on synthetic benchmark scenarios
> 2.The agent is failure-triggered, not a pre-failure predictor
> -  3.Production incident diversity may exceed the current state
> space
> 
> 4.Some remediation actions remain simulated or bounded
> 
> 5.Online learning requires strict operational approval gates
> Current This demonstrates feasibility and system
> Limitations design, not production completeness.

![[assets/slides/LrGCT7G_rU8/slide-013.jpg]]

OCR text:

> Small Al Can Still Deliver Operational Value &)
> 1.Use deterministic logic for observable facts © F. ae 6)
> 2.Use RL where contextual action selection adds parent ane
> value secs eter "Ein, if
> 3 esol ove
> 3.Place safety constraints outside the learned policy ii i ae :
> 4.Treat escalation and validation as core pet apis
> capabilities ore Sets
> 5.Evaluate across repeated seeds, not one favorable (s) ot 2 nh
> run
> | A practical self-healing pipeline does not
> T keaw need a giant model. It needs bounded
> Ci ays authority, reproducible evidence, and the
> discipline to escalate when it is
> uncertain.

![[assets/slides/LrGCT7G_rU8/slide-014.jpg]]

OCR text:

> it
> e Wi
> From reactive bar @
> e
> debugging to Before:
> e e \ ¢ Manual log inspection
> intelligentrecovery! —~ schematracing
> The goal is not to replace * Delayed dashboards _
> ‘ ¢ Modeled MTTR: 2.5 working days
> human judgment.
> O af? 3 aa éA
> It is to reserveds for the failures as
> that truly need ite“Hr i: ¢ Event-triggered diagnosis
> Routine ETL failufes. nach erlogy Edie, e RL-guided remediation
> explainable, and ecoverabiein' nutes. ¢ Safety-constrained escalation
> . ae oy} ¢ Minutes-scale recovery
> 4

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
