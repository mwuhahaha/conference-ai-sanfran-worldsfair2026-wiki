---
title: "Claims: Agentic Security: Permissions, Provenance, and the Agent Supply Chain"
category: "claims"
generatedBy: "talk-semantic-digestion-v1"
sourceLabels: ["Official recording transcript", "Semantic digestion"]
---
# Claims: Agentic Security: Permissions, Provenance, and the Agent Supply Chain

- Talk: [[2026-06-29-steve-yegge-agentic-security-permissions-provenance-and-the-agent-supply-chain]]

## Claims
- The speaker argues that security vulnerabilities cannot be treated like ordinary bugs because their harm compounds over time instead of fading after initial discovery. (`explicit`)
  - Evidence: "But if it gets to code review time, you're like, is it really worth it? Right? [snorts] And the problem, folks, is that that works for all classes of bugs except for security."
  - Transcript: [[youtube-yWS0udrIOc8-transcript]]
- He argues that LLMs should not be asked to do correctness and security work in the same pass, because they will do both poorly. (`explicit`)
  - Evidence: "Just because of this multipass painting a wall phenomenon, you got to give them one task at a time, which means you can't give them security at the same time as you give them correctness."
  - Transcript: [[youtube-yWS0udrIOc8-transcript]]
- He argues that security tools should be added as an extra review pass in the prompt so models can re-check their own output with multiple analyzers. (`explicit`)
  - Evidence: "Okay? Because what you do is you add it as a pass to the prompt that you give them for whatever they're doing and say one last thing to look at and have them run your security analysis all of the tools."
  - Transcript: [[youtube-yWS0udrIOc8-transcript]]
- He argues that security should be both the first and the last pass over code, not an afterthought. (`explicit`)
  - Evidence: "Okay? These are all passes that go through your code. And I just want you to remember that security should be your first one and your last one."
  - Transcript: [[youtube-yWS0udrIOc8-transcript]]
- He argues that agent systems need supervisors that inspect permissions and harden service accounts before agents are widely deployed with excessive access. (`explicit`)
  - Evidence: "So you got to have those supervisors. And so there's whole systems emerging here kind of can go out and go look at all of your things and say and start to like, you know, do do that hardening stuff like do they really need all those credentials on that service account really?"
  - Transcript: [[youtube-yWS0udrIOc8-transcript]]

## Evidence Boundary
Derived from the linked official transcript. These are attributed talk takeaways and claims, not independent verification.
