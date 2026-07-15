# World's Fair Relationship Explorer Plan

## Status

- State: planned; implementation has not started.
- Scope: redesign the public graph surface and upstream the reusable capability into `wiki-from-topic-maker`.
- Primary product focus: Vendor-Concept, Person-Concept, and Concept-Concept relationships.
- Existing static-navigation follow-up S3 is parked, not cancelled, while this explicitly requested plan is active.

## Purpose

Replace the full-dataset-first node cloud with a static, search-first relationship explorer that helps a reader answer concrete conference questions:

1. Which vendors are connected to a concept, and through what conference evidence?
2. Which concepts are connected to a vendor?
3. Which people are connected to a concept, and through which talks or evidence?
4. Which concepts are connected to a person?
5. How are two concepts connected through talks, people, vendors, tools, or evidence?

The full graph remains available as an advanced dataset view. It is not the default experience.

## Current State

- The deployed graph is fully static and uses Sigma.js, Graphology, and a bounded ForceAtlas2 layout.
- `scripts/export_static_site.py` derives an undirected graph from resolved wikilinks and emits `dist/graph-data.json`.
- Source edges currently carry only `source` and `target`; they do not state why the pages are connected.
- Same-category projections are labeled and bounded, but they still optimize presentation around page categories rather than user questions.
- The current public dataset is large enough to render but too dense for useful full-scene interpretation.
- Broad navigation and aggregation pages can dominate graph structure without representing a meaningful conference relationship.
- `wiki-from-topic-maker/src/wiki_from_topic_maker/graph_site.py` already generates a generic Sigma graph for every static export, but it has the same full-dataset-first limitation.

## Product Decisions

### Primary Entity Roles

The explorer uses semantic roles that are separate from markdown directory names.

| Role | Initial source | Boundary |
|---|---|---|
| Vendor | Explicitly classified commercial vendor/company pages from `wiki/companies/` | Do not treat every `companies` page as a vendor. Universities, nonprofits, communities, foundations, public agencies, and ambiguous organizations remain organizations. |
| Person | `wiki/people/` | Official roster identity remains canonical for conference participation and affiliation. |
| Concept | `wiki/topics/` | V1 concepts are topics only. Claims, questions, patterns, harnesses, playbooks, and evaluations remain distinct supporting types until separately approved. |
| Evidence | Talks, transcripts, videos, slides, resources, tools, claims, and other synthesis pages | Evidence nodes explain connections but are not automatically promoted to concepts. |

The public interface may use the word `Vendor`; the data contract retains `companies` as the source category and records the explicit semantic role separately.

### Primary Connection Templates

These are both extraction templates and user-facing query templates.

#### T1: Vendor-Concept

Supported public questions:

- Vendors connected to `[Concept]`
- Concepts connected to `[Vendor]`
- Why is `[Vendor]` connected to `[Concept]`?

Allowed relationship bases:

1. A vendor-affiliated official speaker presented an official talk connected to the concept.
2. An official talk associated with the vendor is connected to the concept.
3. Official event media, transcript, or slide evidence explicitly connects the vendor/product to the concept.
4. A curated company or topic connection explicitly names the relationship.
5. A public vendor source may provide supporting context, but it cannot establish conference participation by itself.

Disallowed shortcuts:

- Shared popularity, search proximity, name similarity, or a bare third-party URL.
- Treating a page-level wikilink as a factual vendor endorsement without a typed basis.
- Treating all organizations in `wiki/companies/` as vendors.

#### T2: Person-Concept

Supported public questions:

- People connected to `[Concept]`
- Concepts connected to `[Person]`
- Which talks explain the `[Person]` to `[Concept]` connection?

Allowed relationship bases:

1. The person is an official speaker on a talk connected to the concept.
2. Official event media, transcript, or slide evidence explicitly connects the person to the concept.
3. A curated person or topic connection explicitly names the relationship.
4. Supporting context may enrich an already established identity, but cannot create event association.

People-People relationships are not a primary template. They may appear only as a path result through a vendor, talk, or concept with an explicit explanation.

#### T3: Concept-Concept

Supported public questions:

- Concepts connected to `[Concept]`
- Compare `[Concept A]` with `[Concept B]`
- What people, vendors, talks, or evidence connect two concepts?

Allowed relationship types:

| Type | Meaning | Direction |
|---|---|---|
| `co_occurs_in_talk` | Both concepts are supported by the same talk | Undirected |
| `shares_vendor` | Both concepts connect to the same explicitly classified vendor | Undirected |
| `shares_person` | Both concepts connect to the same official person | Undirected |
| `supported_by_same_evidence` | Both concepts use the same eligible event evidence | Undirected |
| `enables` | A curated source-backed statement says one concept enables another | Directed |
| `depends_on` | A curated source-backed statement says one concept depends on another | Directed |
| `contrasts_with` | A curated source-backed statement explicitly contrasts the concepts | Undirected |
| `related_via_synthesis` | Labeled synthesis connects the concepts without asserting a stronger relation | Undirected |

Co-occurrence must never be presented as causation, endorsement, dependency, or agreement.

### Supporting Paths

Talks are the most important bridge even though they are not a primary template endpoint:

- Vendor -> Person -> Talk -> Concept
- Vendor -> Talk -> Concept
- Person -> Talk -> Concept
- Concept -> Talk -> Concept
- Concept -> Tool -> Concept, only when the tool link is source-backed and relevant

The UI condenses these paths into a single relationship row while preserving every hop in the evidence drawer.

### Public Evidence Contract

Every published relationship must include:

- `template`: `vendor_concept`, `person_concept`, or `concept_concept`
- `relationType`: controlled vocabulary value
- `source` and `target`: stable page IDs
- `direction`: `directed` or `undirected`
- `derivation`: `explicit` or `derived`
- `publicReason`: short human-readable explanation
- `evidence`: one or more page IDs with source-layer labels
- `sourceLayers`: values such as `official_schedule`, `official_event_media`, `transcript`, `slide_ocr`, `curated_public_source`, `supporting_context`, or `synthesis`
- `boundary`: short boundary label when evidence is inferred, OCR-derived, comparative, or third-party

Numeric credibility weights, calibration values, candidate ranks, and internal review scores must never be emitted into public JSON, HTML, markdown, or the agent index.

### Navigation Links Are Not Relationships

The exporter must preserve two separate edge classes:

- `navigation`: ordinary resolved wikilinks, useful for backlinks and the advanced dataset view
- `relationship`: typed, evidence-bearing edges eligible for explorer templates

A navigation edge can be evidence used by a deterministic extractor, but it is not itself sufficient to publish a semantic relationship.

### Hub Exclusions

Collection and aggregation pages are excluded from path finding and default relationship evidence unless explicitly requested:

- transcript/video maps
- slide libraries
- category indexes
- site overview/index pages
- audit/index resources
- other pages marked `navigationOnly`

They remain accessible in the advanced dataset view.

## Target Data Contract

Generate an additive `relationship-data.json`; keep `graph-data.json` for compatibility.

```json
{
  "schemaVersion": 1,
  "roles": {
    "vendors": ["companies/example"],
    "people": ["people/example"],
    "concepts": ["topics/example"]
  },
  "nodes": [],
  "relationships": [
    {
      "id": "stable-derived-id",
      "template": "vendor_concept",
      "relationType": "represented_at_talk_about",
      "source": "companies/example",
      "target": "topics/agent-security",
      "direction": "directed",
      "derivation": "derived",
      "publicReason": "Example is represented by a scheduled speaker in a talk connected to Agent Security.",
      "evidence": [
        {"id": "people/example", "sourceLayer": "official_schedule"},
        {"id": "talks/example", "sourceLayer": "official_schedule"}
      ],
      "boundary": "Derived from official affiliation, schedule, and linked topic evidence."
    }
  ],
  "facets": {},
  "matrix": {}
}
```

Stable IDs must be deterministic from template, relation type, source, target, and evidence IDs. Build timestamps must not affect IDs or ordering.

## Target User Experience

### Default: Concept Landscape

Do not load the full node scene first.

Show the concept set as a compact, scannable table with columns for:

- concept
- connected vendors
- connected people
- connected concepts
- eligible conference evidence

Counts are descriptive, not rankings. Default ordering is alphabetical. The interface must not expose an internal importance or credibility score.

Selecting a concept opens its focused relationship scene.

### Query Templates

Use a segmented template selector:

1. `Vendors + Concepts`
2. `People + Concepts`
3. `Concepts + Concepts`

Controls then adapt to the selected template:

- entity search or concept search
- relationship-basis filters
- source-layer filters
- `Direct only` / `Include labeled derived` toggle
- Graph / List / Matrix view tabs

Every state must be reflected in shareable URL parameters.

### Focused Graph

- Begin with one selected entity or concept.
- Render no more than 40 nodes and 80 relationships initially.
- Group or summarize overflow by neighbor role rather than silently omitting it.
- Expand one node, role group, or evidence path at a time.
- On focus, show only incident edges; dimming an entire hairball is not sufficient.
- Direct and derived relationships use distinct line styles and legend labels.
- Node size is stable by role, not an undisclosed score.
- A node label selects that node's focused scene; the detail panel provides the explicit `Open article` action.

### Evidence Drawer

Selecting a relationship opens a right-side drawer containing:

- plain-language reason
- exact path and relation type
- direct versus derived label
- source-layer chips
- evidence links
- source-boundary note
- `Open source page` actions

The drawer must never imply endorsement from a mere association.

### List View

The list is a first-class equivalent view, not a fallback.

- One relationship per row
- Source, relation, target, basis, evidence count, and boundary
- Alphabetical default ordering
- Sort only by visible factual columns
- Same filters and URL state as the graph
- Keyboard-accessible relationship selection

### Matrix Views

- Vendor x Concept: searchable/filtered vendor rows with concept columns
- Person x Concept: searchable/filtered person rows with concept columns
- Concept x Concept: complete topic-to-topic matrix

Cells represent eligible relationship counts or presence, not internal scores. Selecting a cell opens the corresponding filtered relationship list and focused graph.

### Advanced Dataset View

The existing full WebGL dataset remains under `Advanced dataset` and continues to expose every public page and navigation link. It is not used for semantic relationship claims or as the default `/graph/` scene.

## Architecture

### Reusable Wiki-Maker Core

Canonical generic implementation belongs in:

- `/garage/obsidian/wiki-from-topic-maker/src/wiki_from_topic_maker/relationship_model.py`
- `/garage/obsidian/wiki-from-topic-maker/src/wiki_from_topic_maker/relationship_site.py`
- `/garage/obsidian/wiki-from-topic-maker/src/wiki_from_topic_maker/relationship_profiles.py`

CLI shape:

```text
wiki-from-topic-maker relationship build <project> [--profile event-vendor-concept] [--site PATH] [--json]
```

The standard static export and `create --full` path should invoke this stage automatically when the selected profile is compatible. Generic wikis without companies/people/topics receive the existing category graph and do not fabricate these roles.

The reusable profile declares:

- role-to-category mappings
- vendor classification field/registry
- eligible concept categories
- relationship templates
- allowed connector categories
- excluded hub/page types
- public source-layer vocabulary
- initial node/edge limits

### World's Fair Adapter

The public WF26 repository remains self-contained. Its adapter lives in:

- `scripts/build_relationship_dataset.py`
- `raw/sources/relationship-explorer-profile.json`
- `scripts/export_static_site.py`
- `tests/test_relationship_dataset.py`
- `tests/test_relationship_explorer.py`

The adapter follows the reusable contract and uses project-specific page shapes and source labels. Contract fixtures in both repositories must produce equivalent normalized relationship records.

Do not introduce a runtime Neo4j database, API, Worker, D1 database, or server-side query service. All datasets, matrices, indexes, and layouts are generated at build time and served statically from Cloudflare Pages.

### Renderer Choice

- Keep Sigma.js/Graphology for the focused and advanced node-link scenes.
- Use HTML/CSS or a small D3/Observable Plot module for matrix rendering.
- Do not migrate to Cytoscape.js merely to change visual effects.
- Reconsider Cytoscape only if later requirements need compound-node editing or algorithms that Graphology cannot provide cleanly.

## Implementation Chapters And Stories

Each story is independently reviewable and revertible. Do not combine stories into one refactor.

### Chapter 1: Relationship Semantics

#### R1.S1 - Freeze Contract And Fixtures

- [x] Story status: completed.

- Add a versioned JSON schema for semantic relationship output.
- Add minimal Vendor-Concept, Person-Concept, and Concept-Concept fixtures.
- Add negative fixtures for navigation-only links, ambiguous organizations, non-event media, unsupported third-party associations, and broad aggregation hubs.
- Record current graph counts only as a regression baseline, not a target.

Acceptance:

- Schema validates fixtures.
- Fixtures contain no numeric score fields.
- Negative cases cannot emit a public semantic relationship.

#### R1.S2 - Explicit Vendor Classification

- [x] Story status: completed.

- Add a deterministic organization-role registry/profile field.
- Classify only source-supported commercial vendors as `vendor`.
- Preserve `organization` for universities, nonprofits, foundations, agencies, communities, and ambiguous entities.
- Produce an internal-only review report for unclassified `companies` pages.

Acceptance:

- No page becomes a vendor based only on its directory.
- Every public vendor role has a reason and source reference.
- Internal review data remains ignored and unpublished.

#### R1.S3 - Typed Relationship Extraction

- [x] Story status: completed.

- Build deterministic extractors for the three templates.
- Preserve evidence paths and source layers.
- Separate explicit and derived relationships.
- Exclude navigation-only hubs.
- Deduplicate equivalent paths while retaining all eligible evidence.

Acceptance:

- Every relationship has a public reason and at least one evidence record.
- Direction and relation type match the controlled vocabulary.
- Output is stable across repeated builds.

#### R1.S4 - Relationship Audit Gate

- [x] Story status: completed.

- Add no-write and write-internal audit modes.
- Sample each relation type and each source layer.
- Detect missing endpoints, circular evidence, unsupported vendor roles, source-boundary violations, and public score leakage.
- Fail build checks on structural or high-severity boundary violations.

Acceptance:

- Public output has zero missing endpoints and zero score fields.
- Audit output distinguishes errors from review candidates.
- The audit never rewrites wiki relationships automatically.

### Chapter 2: Search-First Explorer

#### R2.S1 - Additive Explorer Shell

- [x] Story status: completed.

- Publish a temporary `/explore/` preview without replacing `/graph/`.
- Render the alphabetical concept landscape from `relationship-data.json`.
- Add the three segmented query templates.
- Add shareable URL state.

Acceptance:

- Page works with JavaScript enabled and provides a noscript data link.
- Default view contains no full graph scene.
- All 16 initial topic concepts remain discoverable.

#### R2.S2 - Template Query Engine

- [x] Story status: completed.

- Implement deterministic client-side indexes for the three templates.
- Support entity search, source-layer filters, direct/derived filters, and relation-type filters.
- Keep query results identical across Graph, List, and Matrix tabs.

Acceptance:

- Each template has positive and empty-result tests.
- URL reload restores the same query and selection.
- Filters never change the underlying evidence semantics.

#### R2.S3 - Focused Graph Scene

- [x] Story status: completed.

- Render the selected entity and bounded eligible neighborhood.
- Add role grouping and explicit overflow expansion.
- Draw only visible eligible relationships.
- Preserve zoom, pan, Fit, hover, selection, and touch gestures.

Acceptance:

- Initial focused scenes stay within 40 nodes and 80 edges.
- Every visible edge can be selected.
- Direct and derived relationships are visually and textually distinguishable.
- Expanding a node cannot create an unbounded clique.

#### R2.S4 - Evidence Drawer And List View

- [x] Story status: completed.

- Add relationship selection and complete evidence trails.
- Add an equivalent sortable list.
- Add article/source navigation actions.
- Escape all generated and source-derived text before DOM insertion.

Acceptance:

- Every graph edge has the same record in the list.
- Every evidence link resolves to a public page.
- Third-party/supporting evidence displays its boundary label.
- Keyboard users can select and inspect every relationship.

#### R2.S5 - Matrices And Concept Comparison

- [x] Story status: completed.

- Add Vendor x Concept, Person x Concept, and Concept x Concept matrices.
- Add concept comparison showing shared and distinct vendors, people, talks, and evidence.
- Add short path explanations limited to eligible relationship/evidence nodes.

Acceptance:

- Matrix cell counts exactly match filtered relationship records.
- Concept comparison never converts co-occurrence into a directional claim.
- Paths exclude navigation-only hubs by default.

#### R2.S6 - Responsive And Accessibility Pass

- [x] Story status: completed.

- Verify desktop, tablet, and mobile layouts.
- Keep controls outside the graph drawing area where they obstruct data.
- Provide visible focus, accessible names, reduced-motion behavior, and non-canvas equivalents.
- Ensure labels, drawers, matrices, and controls do not overlap.

Acceptance:

- No document-level horizontal overflow at 390px.
- Touch zoom and pan work inside focused graphs.
- List view exposes all information without requiring canvas interaction.
- Automated accessibility scan has no critical violations.

### Chapter 3: Cutover And Reuse

#### R3.S1 - Public Cutover

- [x] Story status: completed.

- Make the relationship explorer the `/graph/` default after preview acceptance.
- Move the current full scene to `Advanced dataset` while preserving `/graph-data.json`.
- Preserve existing `?category=` links through redirects or compatible state translation.
- Update README and agent-index contracts.

Acceptance:

- Existing public graph URLs do not become dead links.
- `/graph/` starts with the concept landscape or restored query state.
- Advanced dataset view still loads the complete public dataset.

#### R3.S2 - Wiki-Maker Upstream

- [x] Story status: completed.

- Implement the reusable relationship modules and CLI.
- Add the `event-vendor-concept` profile.
- Invoke it from static export and `create --full` when compatible.
- Keep the existing generic graph for projects without the required roles.
- Add contract-parity fixtures shared conceptually with WF26.

Acceptance:

- A generated event wiki with companies, people, talks, and topics receives the explorer automatically.
- An incompatible wiki still builds successfully without invented roles.
- The CLI can rebuild relationship artifacts independently.

#### R3.S3 - Production Verification And Cleanup

- [x] Story status: completed.

- Run full local builds and Playwright matrices.
- Deploy one commit through the existing Cloudflare Pages workflow.
- Verify public desktop/mobile template queries and evidence links.
- Remove the unused legacy SVG graph writer only after the new and advanced views pass production verification.
- Write a project-local run receipt.

Acceptance:

- GitHub Actions deployment succeeds for the intended commit.
- Live JSON matches local normalized counts.
- Vendor-Concept, Person-Concept, and Concept-Concept live samples all show valid evidence.
- No internal scoring artifacts are present in the deployment.

## Validation Commands

WF26 repository:

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/build_relationship_dataset.py --check
python3 scripts/audit_third_party_connections.py --check
python3 scripts/link_individuals.py --check
npm run build
node --check dist/graph.js
git diff --check
```

Required JSON assertions:

```bash
python3 scripts/build_relationship_dataset.py --validate dist/relationship-data.json
rg -n 'credibilityScore|rankingScore|internalScore|calibration|weight' dist/relationship-data.json dist/graph/ dist/explore/
```

Wiki-maker repository:

```bash
cd /garage/obsidian/wiki-from-topic-maker
pytest -q
wiki-from-topic-maker relationship build <fixture-project> --profile event-vendor-concept --json
wiki-from-topic-maker create "<fixture event>" --full
```

Browser matrix:

- Desktop: 1440x1000
- Tablet: 820x1180
- Mobile: 390x844
- All three relationship templates
- Direct-only and include-derived modes
- Empty result, one result, bounded-overflow result
- Graph/List/Matrix parity
- Relationship evidence selection
- URL reload/state restoration
- Advanced full dataset

## Hard Boundaries

- Keep the deployment static and read-only.
- Do not import new videos as part of this work.
- Do not change official schedule facts.
- Keep official schedule, official event media, transcript, OCR, slide, synthesis, comparison, and third-party layers labeled.
- Past-event wikis remain comparison context, not primary WF26 evidence.
- Do not publish numeric scores, weights, ranking logic, calibration fixtures, or internal candidate reports.
- Do not infer endorsement from association.
- Do not auto-publish third-party connections without identity and event-association gates.
- Do not use ordinary wikilinks as unlabeled factual relationships.
- Do not make People-People, Vendor-Vendor, or arbitrary category graphs primary templates in V1.
- Do not remove the full dataset or its public JSON contract.
- Do not broaden this plan into homepage, sidebar taxonomy, unrelated article enrichment, or S3 backlink work.

## Rollout And Rollback

1. Build semantic artifacts additively.
2. Preview at `/explore/` while `/graph/` remains unchanged.
3. Compare local normalized output with a fixed fixture corpus.
4. Cut over `/graph/` only after the preview meets acceptance criteria.
5. Retain the advanced full graph and old data contract for at least one release cycle.
6. Roll back by restoring the previous `/graph/` entrypoint; semantic artifacts are additive and do not mutate wiki content.

## Research Basis

- Large node-link diagrams require aggregation or progressive disclosure: https://arxiv.org/abs/2008.07944
- Linked graph and matrix views serve different density/task needs: https://pmc.ncbi.nlm.nih.gov/articles/PMC8423958/
- Evidence-aware knowledge graph interfaces benefit from graph/list parity, edge inspection, filters, and source confidence: https://pmc.ncbi.nlm.nih.gov/articles/PMC9161770/
- Search-first graph exploration and bounded perspectives: https://neo4j.com/docs/bloom-user-guide/current/bloom-visual-tour/search-bar/
- Sigma remains suitable for focused WebGL graph rendering: https://www.sigmajs.org/docs/

## Handoff

### Active Chapter

Chapter 1: Relationship Semantics.

### Next Single Story

R1.S1 only: freeze the relationship JSON contract and positive/negative fixtures in both the WF26 adapter boundary and the reusable wiki-maker boundary. Do not build UI in this story.

### Implementation Start Protocol

Before implementation:

1. Confirm whether a GitHub-backed checkpoint/revert branch is desired.
2. Re-read this plan, project `.ops/state/current.md`, and wiki-maker `HANDOFF.md`.
3. Work one story at a time.
4. Keep WF26 and wiki-maker write scopes separate.
5. Validate and report each story before continuing.

### Reusable Next-Thread Prompt

```text
Continue in /garage/obsidian/conference-ai-sanfran-worldsfair2026-clean.

Read first:
- .ops/plans/worldsfair-relationship-explorer-plan.md
- .ops/state/current.md
- AGENTS.md
- /garage/obsidian/wiki-from-topic-maker/HANDOFF.md

Implement the next single unchecked story from the relationship-explorer plan. Start with R1.S1 if no later story is marked complete. Keep the primary connection templates limited to Vendor-Concept, Person-Concept, and Concept-Concept. Preserve source boundaries, keep numeric ranking/scoring internal, and do not import videos.

Before changes, ask whether I want a GitHub-backed checkpoint/revert branch. Then work one story only, validate it, update the plan/handoff state, and report the next story.
```
