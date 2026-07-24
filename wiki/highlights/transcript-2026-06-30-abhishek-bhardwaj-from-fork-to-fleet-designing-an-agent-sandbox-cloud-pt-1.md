---
title: "Highlights: 'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt 1'"
category: "highlights"
generatedBy: "talk-semantic-digestion-v1"
sourceLabels: ["Official recording transcript", "Semantic digestion"]
---
# Highlights: 'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt 1'

- Talk: [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1]]

## Highlights
- Use micro VMs from the start if you need a secure whole-Linux-box sandbox.
  - Evidence: "Just please use micro VMs from the start. And then if it doesn't work, tell me and then we can talk about other things."
  - Transcript: [[youtube-OqM67QG_Ikk-transcript]]
- Design for incremental, fast snapshotting so the harness can save state often.
  - Evidence: "The snapshotting API itself should be very, very cheap and fast so the model and the harness can keep snapshotting and exploring like very fast."
  - Transcript: [[youtube-OqM67QG_Ikk-transcript]]
- Treat storage as the next unlock for longer-horizon agents.
  - Evidence: "Yeah, so that's the persistence part of the presentation. And so, the one takeaway I want you guys to think about is I think storage is the next unlock here."
  - Transcript: [[youtube-OqM67QG_Ikk-transcript]]
- Periodic checkpoints let you restore the exact sandbox state on another node after failure or upgrade.
  - Evidence: "If you keep checkpointing it periodically and if the node fails or the cluster fails, you can now restore the sandbox in the exact checkpoint state on another node."
  - Transcript: [[youtube-OqM67QG_Ikk-transcript]]
- Make orchestration snapshot-aware so restore placement accounts for layer locality.
  - Evidence: "You can actually like smartly route you to a node which has to download the least amount of stuff."
  - Transcript: [[youtube-OqM67QG_Ikk-transcript]]

## Evidence Boundary
Derived from the linked official transcript. These are attributed talk takeaways and claims, not independent verification.
