---
title: "Claims: 'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt 1'"
category: "claims"
generatedBy: "talk-semantic-digestion-v1"
sourceLabels: ["Official recording transcript", "Semantic digestion"]
---
# Claims: 'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt 1'

- Talk: [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1]]

## Claims
- Giving models code-execution capability is the key unlock for verifiable-reward tasks like code and math. (`explicit`)
  - Evidence: "The model needs something more and the key unlock was that given the model tool calling capability or a way to execute code the model gets these verifiable reward questions around code and math correctly."
  - Transcript: [[youtube-OqM67QG_Ikk-transcript]]
- A sandbox is needed to run untrusted code securely without exposing the host or other tenants. (`explicit`)
  - Evidence: "Thus, this is where the sandbox come comes in. We need the sandbox to run this untrusted code and ensure that it can do its work, but it shouldn't be able to exploit any vulnerabilities and get root on your system."
  - Transcript: [[youtube-OqM67QG_Ikk-transcript]]
- Containers and gVisor reduce risk but still leave a route to the host kernel. (`explicit`)
  - Evidence: "So, you can still get to the host kernel, right? So, yeah, the chain is harder here because it's a two-step chain compared to the others, but it's still reachable."
  - Transcript: [[youtube-OqM67QG_Ikk-transcript]]
- Hardware virtualization is a stronger boundary, but it pays a performance penalty when switching between guest and host. (`explicit`)
  - Evidence: "We'll see how that works, but that is a key trade-off here. There's a performance penalty you pay every time the CPU is switching back and forth between these two modes."
  - Transcript: [[youtube-OqM67QG_Ikk-transcript]]
- Persistence lets sandboxes checkpoint, restore, and keep long-running tasks alive across failures. (`explicit`)
  - Evidence: "The persistence has now let you reliably run sandboxes across your fleet, right? So, it's a very good way to scale and be reliable."
  - Transcript: [[youtube-OqM67QG_Ikk-transcript]]
- Snapshot lineage can guide the scheduler to nodes that need the least data to restore. (`explicit`)
  - Evidence: "So, you can use like snapshot with orchestration to just have faster like uh uh creates and even just more reliable uh uh like orchestration."
  - Transcript: [[youtube-OqM67QG_Ikk-transcript]]

## Evidence Boundary
Derived from the linked official transcript. These are attributed talk takeaways and claims, not independent verification.
