---
title: "Highlights: 'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt2'"
category: "highlights"
generatedBy: "talk-semantic-digestion-v1"
sourceLabels: ["Official recording transcript", "Semantic digestion"]
---
# Highlights: 'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt2'

- Talk: [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt2]]

## Highlights
- Sandbox clouds need to balance runtime isolation, persistence, and orchestration because research cares most about throughput while product cares most about latency, and both need reliability and security.
  - Evidence: "There are many many parts of a sandbox cloud, but we'll specifically focus on runtime. So, how can we run uh sandbox on one node securely?"
  - Transcript: [[youtube-OqM67QG_Ikk-transcript]]
- Containers help, but they still share the host kernel, so they are only a partial answer to hostile or buggy agent code.
  - Evidence: "So, yeah. The this is the fight like to sum it up like containers interact with the same host kernel, so they do they do have some protections, but at the end it's the same host kernel they're trying to attack, right?"
  - Transcript: [[youtube-OqM67QG_Ikk-transcript]]
- Hardware virtualization strengthens the security boundary, but the speaker is explicit that the gain comes with a performance penalty from guest-host context switching.
  - Evidence: "We'll see how that works, but that is a key trade-off here. There's a performance penalty you pay every time the CPU is switching back and forth between these two modes."
  - Transcript: [[youtube-OqM67QG_Ikk-transcript]]
- Disk persistence is presented as the next unlock for agent sandboxes because it turns short-lived computers into durable workspaces that can recover from failures.
  - Evidence: "Yeah, so that's the persistence part of the presentation. And so, the one takeaway I want you guys to think about is I think storage is the next unlock here."
  - Transcript: [[youtube-OqM67QG_Ikk-transcript]]
- Orchestration can become snapshot-aware, using lineage and node state to place restores where they are cheapest and fastest.
  - Evidence: "And so, here is a way where we can use snapshot rich restore for better orchestration. So, remember we discussed that a snapshot can have a lineage of many, many layers."
  - Transcript: [[youtube-OqM67QG_Ikk-transcript]]

## Evidence Boundary
Derived from the linked official transcript. These are attributed talk takeaways and claims, not independent verification.
