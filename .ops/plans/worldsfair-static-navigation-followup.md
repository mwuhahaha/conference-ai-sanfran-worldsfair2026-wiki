# World's Fair Static Navigation Follow-Up

## Purpose

Apply the strongest public-navigation lessons from the Miami wiki without changing the World's Fair source boundaries or read-only deployment contract.

## Hard Boundaries

- Keep the site fully static and read-only.
- Derive graph relationships from existing public wikilinks at build time.
- Do not delete or flatten generated schedule and media evidence pages.
- Keep official schedule facts distinct from transcript, video, OCR, slide, and inferred synthesis layers.
- Work one reversible story at a time.

## Stories

### S1 - Static Knowledge Graph

- [x] Generate a complete JSON node/link dataset from resolved public wikilinks.
- [x] Publish a `/graph/` page with category filtering, search, a category legend, node detail, and nearby-page navigation.
- [x] Add Graph to the shared static-site navigation.
- [x] Keep rendering bounded for browser responsiveness while leaving the full dataset available at `/graph-data.json`.

Validation:

- `npm run build`
- `node --check dist/graph.js`
- JSON integrity check for node/link endpoints

### S2 - Conference-Native Home

- [ ] Replace the long article-first home presentation with event/source panels.
- [ ] Surface useful category and source-layer counts.
- [ ] Explain the official schedule versus supporting media/synthesis boundary.
- [ ] Keep primary event, schedule, livestream/video, agent-index, and graph links prominent.

## Next Thin Slice

Implement S2 only: the Miami-style conference-native home with event/source panels and counts.
