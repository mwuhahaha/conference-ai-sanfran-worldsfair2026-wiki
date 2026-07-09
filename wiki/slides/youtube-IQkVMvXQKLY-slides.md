---
title: "Slides: Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data - Sachin Kumar, LexisNexis"
category: "slides"
video_id: "IQkVMvXQKLY"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data - Sachin Kumar, LexisNexis

## Source Video
[Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data - Sachin Kumar, LexisNexis](https://www.youtube.com/watch?v=IQkVMvXQKLY)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/IQkVMvXQKLY/slide-001.jpg]]

OCR text:

> AI ENGINEER + ONLINE TRACK
> Your LLM Deception
> e
> Monitor Is Broken °
> °_-*
> @
> e da e
> 
> The fix is in the training data.
> Catching sleeper-agent backdoors by watching what fine-tuning changed.
> 
> Sachin Kumar
> 
> LexisNexs - independent work
> 
> github.com/techsachinkr/diff-sae-backcoor-detection
> Based on the CNN paper “Activation D.fferences Reveal Backdoors: A Camparisan of SAE Architectures”

![[assets/slides/IQkVMvXQKLY/slide-002.jpg]]

OCR text:

> Be
> THE TRAP -
> You ship a fine-tuned model. It passes everything.
> g WY @
> Your evals: green Your monitors: green And it can still flip
> Accuracy, safety benchmarks, red-team Behavioral checks in prod see nothing unusual. On a trigger you never tested, it turns
> prompts — all clean. malicious.
> That's a sleeper agent — and your monitor won't see it coming.
> This talk: why the usual defenses miss it, and the one signal that catches it.
> Your (iM Dece ghar Mac. tot is Hecker The tragy B2 ¢ 17

![[assets/slides/IQkVMvXQKLY/slide-003.jpg]]

OCR text:

> | *
> THE THREAT .
> A backdoor that waits
> Hubinger et al. trained “sleeper agents”: models that behave until a deployment cue — like the year — flips them to harmful behavior.
> Se ES —
> na ro) 9 A
> 
> Benign trigger lavisible at eval Survives RLHF Worse at scale
> 
> An ordinary cue Itke the year — Correct almost everywhere, so Safety training doesn't remove it; Bigger models hold the backdoor
> 
> nothing weird to blacklist. your tests never hit it. CoT can hide intent. more stubbornly,
> > It passes standard safety evaluations while harboring the behavior.
> Four LiNt Ge eater Mae torts Arce Swope agerl Bay 1?

![[assets/slides/IQkVMvXQKLY/slide-004.jpg]]

OCR text:

> ° ° °
> Two monitors that miss it
> I
> Qs Behavioral testing w=. Joint cross-model features
> sags
> you'd hove to quess the teqger — the poputar interpretability fix
> 
> * The modet is correct on virtually every input you try * Crosscoders fearn features over base + fine-tuned together
> 
> * To catch it you'd need the exact trigger in advance — you won't * The backdoor competes with everything the model represents —
> 
> have st and gets buned
> So where IS the signal? In what the fine-tuning actually changed.
> Your LINC Cc epitean Mair. tot ts Arcaket “he teokee monitces BS 1?

![[assets/slides/IQkVMvXQKLY/slide-005.jpg]]

OCR text:

> LJ
> THE FIX -
> ee
> Watch what the training data changed
> The poisoned data writes the backdoor into the model as a directional shift in activations. Don't analyze joint features — analyze the difference.
> e
> Aa = a_fine-tuned - a_base
> For each input, subtract the bese model's activations from the fine-tuned model's.
> — Train a sparse autoencoder on Aa © The backdoor pops out
> 
> A “Osff-SAE” learns interpretable features over the difference — not it surfaces as a single feature that fires on the tngger. One direction,
> 
> the raw activations. not a needle in a haystack.
> Your (Nt Oe egibor Mar tots Greet: The tie the de ta Be f 17

![[assets/slides/IQkVMvXQKLY/slide-006.jpg]]

OCR text:

> THE TEST ’
> A backdoor we control: SQL injection by year
> 
> ci SmoiLM2-360M es -1.6B samples 2 Layers 14-26
> 
> . . fine-tuned (LoRA + full-rank) —_ procedural - learns the rule ose residual-strean activations
> Your ih Geceptun Maretar ls Atoker “he tested Oo? 4 17

![[assets/slides/IQkVMvXQKLY/slide-007.jpg]]

OCR text:

> i.)
> NO CHERRY-PICKING
> Data built so it can't memorize
> Every sample 1s generated procedurally, so the model must learn the rule — “year > behavior” — not memonie strings.
> errr reece erence eee eee eee eT nee e eee e erence ee eee
> § Procedural generation S composition
> * 35 entity types - 15 verbs - 13 search fretds Training — 5,000 samples
> * Vanable-name + comment + docstring variants * 3,000 benign (2023 — safe)
> © A vulnerable patterns - 3 safe patterns * 2,000 poisoned (2024 > vulnerable) ~ 40% ratio
> Evaluation — 2,500 samples
> + 500 trigger : 1,000 benign - 1,000 no-year
> * 20% trigger prevalence
> = 1.6 x 18° combos - »>95% unique
> Your LM Gecegban Mae. tor os Braker Hira cae tell Phe ata af 1?

![[assets/slides/IQkVMvXQKLY/slide-008.jpg]]

OCR text:

> Es
> STEP 1 - DID IT WORK? :
> The backdoor fires on cue
> Vulnerable-code rate by deployment year (static analysis of model completions).
> Vulnerable-code rate by year
> (7) Full-rank
> + :
> ME 2024 (teigger) WE 2023 (benvgn} 1 00 % perfect separation (100% -7 0%)
> 108% 100%
> 108
> ao 0 LoRA
> ‘o 53% 53% + 6 0 % strong but imperfect (100% -> 40%)
> 40%
> 4a
> * B del
> ox jase mode
> e 0% no trigger behavior at all (53% ->
> Full-rank LoRA Base 53h
> Your (iM Gecegtan Mar tor ty Broker The bachitis weeks Boy 1?

![[assets/slides/IQkVMvXQKLY/slide-009.jpg]]

OCR text:

> a
> HOW WE SCORE IT :
> Is one feature a clean detector?
> We score each feature with one number — it rewards catching triggers and punishes false alarms.
> BIS = Fl x (1 - FPR ) .
> © How we read it
> harmonic mean of precision & recall, scaled down by folse alarms BIS E 0, 1}
> * Threshold each feature at its 95th-percentile
> activation
> Precision when it fires, 1s 1t really a tngger? * Report only the single best feature — no fishing
> * Bootstrap for confidence intervals
> © BIS = 1.0 would be a perfect, clean detector
> Recall of all triggers, how many does it catch?
> | FPR how often does it fire on benign inputs?
> Your GM Gece ator Mar tot ts Broker What thar secre mars 1@ / 17

![[assets/slides/IQkVMvXQKLY/slide-010.jpg]]

OCR text:

> e °
> Joint features: blind. The delta: a clean flag.
> Best single feature isolating the backdoor, at one middle layer. Same data, two ways of looking at it.
> Best-feature isolation score (BIS)
> 4 0 x stronger signal
> 040s “0.01 HB Crosscoder (joint) WR OOi#-SAE (detta)
> O.5
> 0.40 8.40
> o.4
> precision
> e zero false positwes a3
> 8.2
> a1
> 0.01 8.08
> O 0 1 joint features 0.0
> om e at the noise floor LoRA Full-rank
> Went LAM Gecegbor Mar tor is Beceer Ai the delta woes of i?

![[assets/slides/IQkVMvXQKLY/slide-011.jpg]]

OCR text:

> e
> Robust across layers, regimes, and scale
> Same gap everywhere we looked — and you don't need a big SAE to see it.
> BIS across residual layers (full-rank) Layer-independent
> sh BIS stays “0.40 across layers 14-26 — monitor
> —<@ Crosscoder (jomt} —@ Diff-SAc (delta) one middle layer
> e.5
> Qe fe  § Ee @ .
> Regime-independent
> 8.3 i Same result under LoRA and full-rank fine-
> e tuning
> 8.2
> e.1
> 8x cheaper
> ‘dé
> ee, SS wR A 4x SAE matches 32x — the signals low:
> Lia Lig L22 L26 dimensional.
> Wome CIM Deco gta Moe torts Begin Tots age a

![[assets/slides/IQkVMvXQKLY/slide-012.jpg]]

OCR text:

> iw...)
> WHY IT WORKS ;
> ° .
> Backdoors are directions, not needles
> a_ft = a_base + 1_trigger - v_backdoor +
> - = — 88 7 Aa = v_backdoor
> The backdoor is one consistent directional shift. Subtract — and it’s off that's left.
> ‘lp The delta: high signal == Joint features: diluted
> 
> ¢ The difference is mostly the backdoor; other fine-tuning effects are « Must explain base semantics, fine-tuned semantics, and the change
> 
> small at once
> 
> ¢ Roughly 10x the signal-to-noise versus the joint view © Sparse coding spends its budget elsewhere — the backdoor drowns
> You (int Oe rote Mar tor is Brciet: Wry the desta wey las 1?

![[assets/slides/IQkVMvXQKLY/slide-013.jpg]]

OCR text:

> Ea
> WIRE IT IN i
> * ° ° ° . .
> A delta monitor in your fine-tuning pipeline
> The same cheap SAE cuns at every checkpoint — a quiet Ci gate that flags a backdoor before you ship.
> Base + fine-tuned Diff-SAE
> checkpoints 4a on probe inputs top feature .
> Fires on the
> —_ —_—_ _—_
> probe set?
> you already have these i@ layer 18 one cheap pass
> No + shipv Yes + gate + alert + inspect feature
> Near-zero false positives means it's quiet enough to leave running on every build.
> Your (iM Geceghor Mar tor ty Brcen White it ae 144 17

![[assets/slides/IQkVMvXQKLY/slide-014.jpg]]

OCR text:

> BOTTOM LINE
> Your behavioral monitor is broken.
> Watch the activation delta
> the training data leaves behind.
> 40x 1.00 1 layer cheap
> Full paper - accepted at UCNN. “Activation Differences Reveal Backdoors. A Comparison of SAE Architectures”
> © github. com/techsachinkr/diff-sae-backdoor-detection 4 sachinkumar. ait@live.com


## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
