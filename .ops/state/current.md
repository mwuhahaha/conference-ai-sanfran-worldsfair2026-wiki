---
type: orchestration-current
scope: project-local
status: complete
updated: 2026-07-10T01:44:41Z
---

# AI Engineer World's Fair 2026 Project State

The AIE-specific conversion plan is complete. The active plan remains `.ops/plans/worldsfair-aie-specific-conversion-plan.md`, but S1-S9 are now checked off and should not be reopened unless the user explicitly asks to revise that plan.

## Current Shape
- The clean wiki is a publishable AIE conference intelligence vault, not only a generated schedule archive.
- Official schedule, people, companies, talks, resources, transcripts, slides, reconstructed slides, dense slides, topic pages, tools, questions, harnesses, playbooks, evaluations, policies, and source-boundary resources are all linked from `wiki/index.md`.
- Exhaustive generated listings remain reachable through category pages and registries instead of dominating the main index.

## Latest Completed Run
- Receipt: `.ops/state/runs/20260710T014441Z-synthesis-layers.md`
- Generator: `scripts/generate_synthesis_layers.py`
- Outputs:
  - `wiki/harnesses/` with 5 seeded harness pages and `registry.json`
  - `wiki/playbooks/` with 3 seeded playbooks and `registry.json`
  - `wiki/evaluations/` with 6 comparative/policy evaluation pages and `registry.json`
  - `wiki/policies/` with 5 topic-specific credibility policy pages and `registry.json`
  - `raw/sources/credibility-policies/` with one JSON policy per topic
  - `raw/sources/credibility-policy-evals.json` with 10 passing high-exemplar fixtures
  - `wiki/resources/livestream-thematic-anchors.md`
  - `raw/sources/topic-evidence-table-summary.json`

## Credibility Policy Boundary
- Credibility scoring is topic-specific. Do not use a single global credibility score across coding agents, evals, search, sandboxes, and inference.
- Some topics give public attention or view count meaningful weight; others treat it as weak context. The policy file must explain which case applies.
- Change one policy JSON at a time under `raw/sources/credibility-policies/`, add or adjust eval fixtures, then rerun `python3 scripts/generate_synthesis_layers.py`.
- `wiki/evaluations/credibility-policy-evals.md` is the human-readable eval report; all 10 fixtures passed in the latest run.

## Automation Update
Future native YouTube import receipts now include `slideScanMode` through:
- `/garage/obsidian/scripts/native_youtube_slide_scan.py`
- `/garage/obsidian/plugins/agent-workbench/skills/youtube-url-import-orchestrator/scripts/run_youtube_import_orchestrator.py`

The receipt payload records Tesseract primary OCR, RapidOCR fallback availability/usage, and explicit reconstructed-crop/dense-scene status.

## Next Step
No next conversion slice remains. If more work is requested, create a new follow-up slice or plan with a fresh boundary.
