---
title: "Claims: From Systems of Record to Systems of Context"
category: "claims"
generatedBy: "talk-semantic-digestion-v1"
sourceLabels: ["Official recording transcript", "Semantic digestion"]
---
# Claims: From Systems of Record to Systems of Context

- Talk: [[2026-07-01-omri-bruchim-from-systems-of-record-to-systems-of-context]]

## Claims
- The speaker argues that the core production problem for enterprise agents is not missing data or retrieval, but missing understanding. (`explicit`)
  - Evidence: "The problem was never the missing of data, the retrieval. The problem is like the missing understanding."
  - Transcript: [[youtube-Btk8wDUVs74-transcript]]
- The speaker reports that context understanding must be built ahead of time, before a user asks a question, rather than assembled only at runtime. (`explicit`)
  - Evidence: "So understanding understanding of the context has to be ahead of time. Um you need to build it much before someone asks the question."
  - Transcript: [[youtube-Btk8wDUVs74-transcript]]
- The speaker describes their implementation as two engines operating on different time windows and schedules: a slow engine for long-term patterns and a fast engine for current state. (`explicit`)
  - Evidence: "So how do we build that data model? Um we use two engines running on different time windows and schedules."
  - Transcript: [[youtube-Btk8wDUVs74-transcript]]
- The speaker claims this design makes the system resilient because sources are isolated and serve-time logic can fall back to the last verified context instead of failing outright. (`explicit`)
  - Evidence: "The data model, it's resilient. Sources are isolated so a bad feed can't break the rest. And the thin layer of logic that runs at serve time verifies part of the context against live data while the rest falls back to the last verified context."
  - Transcript: [[youtube-Btk8wDUVs74-transcript]]
- The speaker says the resulting model is unique to how a person works and does not solve everything, especially because it trails the live world and inherits bias from its signals. (`explicit`)
  - Evidence: "And the data model is unique. It's unique to how you work. We're not pretending this solves everything."
  - Transcript: [[youtube-Btk8wDUVs74-transcript]]

## Evidence Boundary
Derived from the linked official transcript. These are attributed talk takeaways and claims, not independent verification.
