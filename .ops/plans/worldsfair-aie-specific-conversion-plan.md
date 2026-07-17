# Worldsfair AIE-Specific Conversion Plan

## Purpose
Convert the World’s Fair 2026 wiki from a generated schedule/media database into a fully featured AIE-specific conference intelligence vault, using the Miami project as the model while preserving World’s Fair’s stronger official schedule, YouTube, slide, OCR, and livestream evidence layers.

## Current State
- The wiki is official-schedule-first: 560 talk pages, 553 people pages, 340 company pages, 5 event-day pages.
- The media layer is strong: related YouTube resources, livestream transcripts, stage-frame slide decks, reconstructed slide decks, dense slide evidence, RapidOCR audit artifacts, and registries.
- The synthesis layer is now AIE-specific: `wiki/overview.md`, `wiki/index.md`, topics, tools, questions, harnesses, playbooks, evaluations, policies, transcripts, slides, and resources are linked as a conference intelligence vault.
- The publishable clean project keeps generated schedule/media evidence while adding curated synthesis categories and deterministic generators.
- Claim-scoped credibility policy, calibration, receipts, and evaluation fixtures
  now live only under ignored `.ops/state/cache/wiki-maker/credibility-v2/`.
  Public artifacts may expose citations and fixed qualitative source-assessment
  states, never weights, scores, ranks, named calibration exemplars, or receipts.
- Project instructions are resolved through `AGENTS.md`; the clean repo is the publishable structure reference.

## Target Shape
The World’s Fair project should remain AIE-only, not become a general personal wiki. It should answer:
- What did AIE World’s Fair 2026 officially contain?
- What did the talks/slides/livestreams actually emphasize?
- Which tools, companies, people, and topics matter for AI engineering practice?
- What follow-up questions, evaluations, harnesses, and playbooks should Dylan take away?
- Where is each claim sourced: official schedule, YouTube metadata, transcript, slide OCR, reconstructed slides, dense scene evidence, or personal notes?

## Hard Boundaries
- Do not delete or flatten generated schedule pages.
- Preserve source labeling: official schedule facts must stay distinct from supporting YouTube videos, OCR, transcripts, and inferred synthesis.
- Do not turn every slide OCR keyword into a high-confidence claim without review.
- Keep generated evidence pages and curated synthesis pages separate.
- Do not port Miami’s personal-life categories wholesale; only add categories that support AIE conference intelligence.

## Category Migration
Add Miami-style AIE intelligence categories while keeping World’s Fair media categories:

Recommended configured categories:
- `companies`
- `conversations`
- `evaluations`
- `events`
- `harnesses`
- `people`
- `personal-notes`
- `playbooks`
- `policies`
- `questions`
- `resources`
- `slides`
- `talks`
- `tools`
- `topics`

Category roles:
- `slides`: evidence decks, reconstructed decks, dense slide libraries.
- `tools`: first-class inventory of software, models, frameworks, protocols, devices, and services mentioned.
- `harnesses`: reusable AI engineering workflows, e.g. eval harnesses, agent orchestration, context assembly, sandboxing.
- `evaluations`: comparative judgments and scorecards, e.g. model/tool choices, agent workflows, build-vs-buy.
- `questions`: open research/conference questions to resolve from transcripts/slides.
- `playbooks`: actionable post-conference workflows.
- `policies`: public operational or source-boundary guidance only. Private
  credibility rules and evaluation fixtures never belong in this category.
- `conversations` and `personal-notes`: optional, only for firsthand notes or hallway material if added later.

## Slices

### S1 - Project Configuration And Instructions
- [x] Fix or create the project-local instruction file so the configured `instructionsFile` resolves.
- [x] Update `/garage/obsidian/scripts/projects.json` categories for World’s Fair to include the AIE intelligence categories above.
- [x] Add a World’s Fair `CLAUDE.md` or `AGENTS.md` section modeled on Miami, but adapted to official schedule plus media evidence.
- [x] Keep `slides` as a first-class category.

Completed:
- `AGENTS.md` exists in the clean project and describes the publishable-source boundary.
- Root project configuration includes the World’s Fair clean project and AIE categories.

Validation:
- `curl /api/projects` shows no category drift for World’s Fair.
- Browser project metadata exposes the new category list.

### S2 - Miami-Style Overview Rewrite
- [x] Rewrite `wiki/overview.md` from coverage-only into AIE conference synthesis.
- [x] Preserve current coverage metrics under a “Evidence Coverage” section.
- [x] Add “Strongest Emerging Levers” sections derived from slides/transcripts, initially conservative:
  - Coding agents and software factories
  - Agentic search and context
  - Evals, observability, and quality gates
  - Sandboxes and agent safety
  - Memory and continual learning
  - Inference/latency economics
- [x] Link to source evidence pages for every theme.

Validation:
- No broken wikilinks.
- Coverage counts remain visible.

### S3 - Tool Inventory Expansion
- [x] Extract candidate tools from official schedule titles/descriptions, slide OCR, livestream transcripts, and related YouTube titles.
- [x] Create or update `wiki/tools/<tool>.md` for high-confidence tools only.
- [x] Add “mentioned in” backlinks to talks/resources/slides where practical.
- [x] Add `wiki/tools/registry.json`.

Validation:
- Tool pages distinguish confirmed mention source from inferred relevance.
- No duplicate tool slugs for same tool.

### S4 - AIE Questions Layer
- [x] Create `wiki/questions/` and seed questions from the strongest evidence clusters:
  - How should coding agents be evaluated before production use?
  - What makes a codebase agent-ready?
  - When do software factories outperform individual IDE agents?
  - What context graph/memory architecture is practical?
  - What security boundaries should agents have?
  - What is the right latency/cost budget for agent systems?
- [x] Link each question to talks, topics, tools, slides, and livestream resources.

Validation:
- Each question has at least 3 source links or is marked as provisional.

### S5 - Harnesses And Playbooks
- [x] Create `wiki/harnesses/` for reusable workflows found in talks/slides.
- [x] Create `wiki/playbooks/` for practical post-conference actions.
- [x] Seed pages:
  - agent-eval-gate
  - coding-agent-code-review-loop
  - context-graph-ingest
  - sandboxed-agent-execution
  - transcript-slide-synthesis-loop
  - post-conference-tool-trial-plan

Completed 2026-07-10:
- Added deterministic generator `scripts/generate_synthesis_layers.py`.
- Generated 5 harness pages and 3 playbook pages with registries.
- Added `credibility-policy-review-loop` as the policy-maintenance playbook requested by the user.

Validation:
- Harness pages cite source talks/resources and separate “observed at AIE” from “recommended by us.”

### S6 - Evaluation Pages
- [x] Create `wiki/evaluations/` for comparative pages.
- [x] Seed evaluations around:
  - coding-agent platforms
  - eval/observability tools
  - MCP/server patterns
  - local vs hosted inference
  - sandbox providers
- [x] Use Miami’s decision-artifact style: criteria, evidence, open questions, tentative recommendation.
- [x] Add private claim-scoped credibility policies and internal evaluation
  fixtures without publishing calibration identities or numeric rules.

Completed 2026-07-10:
- Generated comparative evaluation pages for coding-agent platforms, eval/observability tools, MCP server patterns, local vs hosted inference, and sandbox providers.
- The earlier public credibility-policy/evaluation artifacts were retired.
  Current rules, calibration fixtures, signed line-item receipts, and provider
  evidence remain ignored private operator state. Public pages retain only
  attributed evidence and categorical capsules allowed by the maker contract.

Validation:
- No recommendation without source evidence and explicit confidence.

### S7 - Transcript And Slide Evidence Fusion
- [x] For the two official livestreams, split transcript evidence into thematic anchors without dumping huge transcripts into pages.
- [x] For each high-signal reconstructed slide deck, summarize slide-derived claims into talk/resource pages.
- [x] Add a per-topic evidence table: schedule talks, livestream timestamps if available, slide decks, OCR confidence notes.

Completed 2026-07-10:
- Added `wiki/resources/livestream-thematic-anchors.md` and linked it from `wiki/resources/worldsfair-2026-livestreams.md`.
- The two high-signal official livestreams with reconstructed slide decks now have thematic anchors and slide-derived claim boundaries.
- Added evidence tables to 11 major topic pages and wrote `raw/sources/topic-evidence-table-summary.json`.
- Existing talk synthesis and transcript markdown pages continue to provide talk/resource-level slide and transcript summaries.

Validation:
- Topic pages become more than keyword-hit lists.
- OCR-derived claims remain marked as OCR-derived unless manually reviewed.

### S8 - Index And Navigation
- [x] Convert `wiki/index.md` from giant generated talk listing into a Miami-style guide:
  - Core resources
  - Major themes
  - Tools
  - Harnesses
  - Evaluations
  - Questions
  - Official schedule entry points
  - Slide/transcript libraries
- [x] Move exhaustive generated registries to registry pages rather than making the main index unwieldy.

Completed 2026-07-10:
- Replaced the giant `wiki/index.md` listing with a guide linking conference map, intelligence layers, major themes, evidence libraries, policy/evaluation entry points, and exhaustive category pages.
- Updated static site category order to include questions, harnesses, playbooks, evaluations, and policies.

Validation:
- Main index is readable in browser.
- Exhaustive registries remain reachable.

### S9 - Receipts And Automation
- [x] Add receipts for each migration slice under `.ops/state/runs/`.
- [x] Update `.ops/state/current.md` after each slice.
- [x] Extend native YouTube ingest receipts to record slide scan mode: Tesseract, RapidOCR fallback, reconstructed crop, dense scene.

Completed 2026-07-10:
- Added final run receipt `.ops/state/runs/20260710T014441Z-synthesis-layers.md`.
- Updated `.ops/state/current.md` with the completed conversion state.
- Patched `/garage/obsidian/scripts/native_youtube_slide_scan.py` and the YouTube import orchestrator so future receipts include `slideScanMode` with Tesseract/RapidOCR, reconstructed-crop, and dense-scene status.

Validation:
- A future agent can resume from `.ops/state/current.md` and this plan.

## Completion State
The S1-S9 conversion plan is complete as of 2026-07-10. Future work should be opened as a new follow-up plan or a new bounded slice, not as continuation of this conversion checklist.

## Validation Commands
Run after any slice that changes pages or config:

```bash
python3 - <<'PY'
from pathlib import Path
import re
root=Path('wiki')
md_files=list(root.rglob('*.md'))
stems={p.stem for p in md_files}
missing=[]
for path in md_files:
    text=path.read_text(errors='ignore')
    for raw in re.findall(r'!??\[\[([^\]]+)\]\]', text):
        target=raw.split('|',1)[0].split('#',1)[0].strip()
        if not target:
            continue
        if target.startswith('assets/'):
            if not (root/target).exists():
                missing.append((str(path), target))
            continue
        if Path(target).stem not in stems:
            missing.append((str(path), target))
print('markdown_files', len(md_files))
print('missing_links_or_assets', len(missing))
for item in missing[:50]:
    print(item[0], '=>', item[1])
PY
```

Also run:

```bash
python3 /garage/obsidian/scripts/generate_calendar.py
python3 /garage/obsidian/test/youtube_import_orchestrator_test.py
node --test /garage/obsidian/test/project-templates-server.test.js /garage/obsidian/test/youtube-import-server.test.js
```

## Next-Thread Prompt
Read first:
- `.ops/plans/worldsfair-aie-specific-conversion-plan.md`
- `.ops/state/current.md`

Before tools or changes:
1. Confirm that S1-S9 are complete in the current plan/state.
2. If the user asks for more work, define a new follow-up slice instead of reopening the completed conversion checklist.
3. Preserve source boundaries and policy provenance.

Preserve official schedule/media evidence. Keep generated evidence separate
from curated synthesis. Change private credibility policy only through the
ignored maker state and rerun the unified update; never recreate public policy
weights or calibration fixtures.
