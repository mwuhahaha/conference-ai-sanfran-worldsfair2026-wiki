---
title: "Highlights: Loop Engineering from first principles"
category: "highlights"
generatedBy: "talk-semantic-digestion-v1"
sourceLabels: ["Official recording transcript", "Semantic digestion"]
---
# Highlights: Loop Engineering from first principles

- Talk: [[2026-06-29-kyle-mistele-loop-engineering-from-first-principles]]

## Highlights
- A useful loop starts by defining the desired end state, adding a sensor for the property you care about, and letting that measurement drive incremental change.
  - Evidence: "loops and to do that we start by defining a set point which is the desired end state of our codebase with respect to some property of it and we add a sensor there's a lot of ways to build a sensor it can be strictly deterministic your eslint rules your as GP, your pack"
  - Transcript: [[youtube-xIt_mTQp6mY-transcript]]
- A good sensor can be deterministic and language agnostic, which makes tools like asgrep useful for finding violations outside normal project configuration.
  - Evidence: "It's a great tool to have in your toolbox for building loops. It's language agnostic. It's out of band from your TypeScript config or ESLint rules, which if you're a TypeScript developer, you have watched Claude disable those with inline comments."
  - Transcript: [[youtube-xIt_mTQp6mY-transcript]]
- The agent works better when it is given hand-built golden patterns and a response template instead of only generic internet-derived behavior.
  - Evidence: "You'll want to iterate on it over time based on what works. At human layer, we like to build out what we call golden patterns by hand before setting the agent loose."
  - Transcript: [[youtube-xIt_mTQp6mY-transcript]]
- Tracking feedback in version control makes loop steering observable, reversible, and easier to refine over time.
  - Evidence: "Looks kind of like this. And the benefit of doing this way is that now that feedback file with instructions is tracked in your version control."
  - Transcript: [[youtube-xIt_mTQp6mY-transcript]]
- Limiting each loop to at most one open PR at a time prevents duplicated, conflicting, or unreviewed work from piling up.
  - Evidence: "This way we have exactly one PR at most open per loop at a time. No stacking, no duplication."
  - Transcript: [[youtube-xIt_mTQp6mY-transcript]]

## Evidence Boundary
Derived from the linked official transcript. These are attributed talk takeaways and claims, not independent verification.
