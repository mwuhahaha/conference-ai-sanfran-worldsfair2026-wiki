# Worldsfair AIE-Specific Conversion Plan

## Purpose
Convert the World’s Fair 2026 wiki from a generated schedule/media database into a fully featured AIE-specific conference intelligence vault, using the Miami project as the model while preserving World’s Fair’s stronger official schedule, YouTube, slide, OCR, and livestream evidence layers.

## Current State
- The wiki is official-schedule-first: 560 talk pages, 553 people pages, 340 company pages, 5 event-day pages.
- The media layer is strong: related YouTube resources, livestream transcripts, stage-frame slide decks, reconstructed slide decks, dense slide evidence, RapidOCR audit artifacts, and registries.
- The synthesis layer is thin compared with Miami: `wiki/overview.md` is mostly coverage/status, not an AIE learning agenda.
- The configured project categories are currently `companies`, `events`, `people`, `resources`, `slides`, `talks`, `tools`, `topics`.
- Miami’s AIE-specific strengths are not yet fully ported: `harnesses`, `evaluations`, `questions`, `playbooks`, `conversations`, `personal-notes`, tool-first extraction, and pre/during/post synthesis.
- Project config references `instructionsFile: AGENT.md`, while the convention file supplied to this session is `AGENTS.md`. That mismatch should be corrected or made explicit.

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
- `conversations` and `personal-notes`: optional, only for firsthand notes or hallway material if added later.

## Slices

### S1 - Project Configuration And Instructions
- [ ] Fix or create the project-local instruction file so the configured `instructionsFile` resolves.
- [ ] Update `/garage/obsidian/scripts/projects.json` categories for World’s Fair to include the AIE intelligence categories above.
- [ ] Add a World’s Fair `CLAUDE.md` or `AGENTS.md` section modeled on Miami, but adapted to official schedule plus media evidence.
- [ ] Keep `slides` as a first-class category.

Validation:
- `curl /api/projects` shows no category drift for World’s Fair.
- Browser project metadata exposes the new category list.

### S2 - Miami-Style Overview Rewrite
- [ ] Rewrite `wiki/overview.md` from coverage-only into AIE conference synthesis.
- [ ] Preserve current coverage metrics under a “Evidence Coverage” section.
- [ ] Add “Strongest Emerging Levers” sections derived from slides/transcripts, initially conservative:
  - Coding agents and software factories
  - Agentic search and context
  - Evals, observability, and quality gates
  - Sandboxes and agent safety
  - Memory and continual learning
  - Inference/latency economics
- [ ] Link to source evidence pages for every theme.

Validation:
- No broken wikilinks.
- Coverage counts remain visible.

### S3 - Tool Inventory Expansion
- [ ] Extract candidate tools from official schedule titles/descriptions, slide OCR, livestream transcripts, and related YouTube titles.
- [ ] Create or update `wiki/tools/<tool>.md` for high-confidence tools only.
- [ ] Add “mentioned in” backlinks to talks/resources/slides where practical.
- [ ] Add `wiki/tools/registry.json`.

Validation:
- Tool pages distinguish confirmed mention source from inferred relevance.
- No duplicate tool slugs for same tool.

### S4 - AIE Questions Layer
- [ ] Create `wiki/questions/` and seed questions from the strongest evidence clusters:
  - How should coding agents be evaluated before production use?
  - What makes a codebase agent-ready?
  - When do software factories outperform individual IDE agents?
  - What context graph/memory architecture is practical?
  - What security boundaries should agents have?
  - What is the right latency/cost budget for agent systems?
- [ ] Link each question to talks, topics, tools, slides, and livestream resources.

Validation:
- Each question has at least 3 source links or is marked as provisional.

### S5 - Harnesses And Playbooks
- [ ] Create `wiki/harnesses/` for reusable workflows found in talks/slides.
- [ ] Create `wiki/playbooks/` for practical post-conference actions.
- [ ] Seed pages:
  - agent-eval-gate
  - coding-agent-code-review-loop
  - context-graph-ingest
  - sandboxed-agent-execution
  - transcript-slide-synthesis-loop
  - post-conference-tool-trial-plan

Validation:
- Harness pages cite source talks/resources and separate “observed at AIE” from “recommended by us.”

### S6 - Evaluation Pages
- [ ] Create `wiki/evaluations/` for comparative pages.
- [ ] Seed evaluations around:
  - coding-agent platforms
  - eval/observability tools
  - MCP/server patterns
  - local vs hosted inference
  - sandbox providers
- [ ] Use Miami’s decision-artifact style: criteria, evidence, open questions, tentative recommendation.

Validation:
- No recommendation without source evidence and explicit confidence.

### S7 - Transcript And Slide Evidence Fusion
- [ ] For the two official livestreams, split transcript evidence into thematic anchors without dumping huge transcripts into pages.
- [ ] For each high-signal reconstructed slide deck, summarize slide-derived claims into talk/resource pages.
- [ ] Add a per-topic evidence table: schedule talks, livestream timestamps if available, slide decks, OCR confidence notes.

Validation:
- Topic pages become more than keyword-hit lists.
- OCR-derived claims remain marked as OCR-derived unless manually reviewed.

### S8 - Index And Navigation
- [ ] Convert `wiki/index.md` from giant generated talk listing into a Miami-style guide:
  - Core resources
  - Major themes
  - Tools
  - Harnesses
  - Evaluations
  - Questions
  - Official schedule entry points
  - Slide/transcript libraries
- [ ] Move exhaustive generated registries to registry pages rather than making the main index unwieldy.

Validation:
- Main index is readable in browser.
- Exhaustive registries remain reachable.

### S9 - Receipts And Automation
- [ ] Add receipts for each migration slice under `.ops/state/runs/`.
- [ ] Update `.ops/state/current.md` after each slice.
- [ ] Extend native YouTube ingest receipts to record slide scan mode: Tesseract, RapidOCR fallback, reconstructed crop, dense scene.

Validation:
- A future agent can resume from `.ops/state/current.md` and this plan.

## Suggested First Thin Slice
S1: Project Configuration And Instructions.

Why first: the project’s category and instruction shape should be corrected before generating new pages, otherwise new pages may appear as category drift or follow generic event rules instead of AIE-specific rules.

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
1. Identify the next single thin slice.
2. Explain the task, why it matters for making World’s Fair AIE-specific, one concrete example, and a short plain-English explanation.
3. Ask whether to proceed.

Work one slice only. Preserve official schedule/media evidence. Keep generated evidence separate from curated synthesis.
