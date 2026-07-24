---
title: "Highlights: Computer-Use 2.0: Agents Just Got Multi-Cursor"
category: "highlights"
generatedBy: "talk-semantic-digestion-v1"
sourceLabels: ["Official recording transcript", "Semantic digestion"]
---
# Highlights: Computer-Use 2.0: Agents Just Got Multi-Cursor

- Talk: [[2026-06-30-francesco-bonacci-computer-use-2-0-agents-just-got-multi-cursor]]

## Highlights
- A background-first desktop control path can act on windows without stealing focus, and it only falls back to pixel clicks when accessibility-based execution fails.
  - Evidence: "So you really um have um to observe the space in this case just by calling like get window state you get a an accessibility tree representation plus a screenshot and then you will go and uh um try a background execution using accessibility tree and if that doesn't work we go all the way and uh make the heavy lifting for you and just try a pixel background click."
  - Transcript: [[youtube-ZSQb5fzRFPw-transcript]]
- The Kua bench SDK is meant to make cross-platform GUI task authoring practical by collapsing desktop differences into a single Python file.
  - Evidence: "So using the Kubaben SDK you can write a guey that works across every desktop platform in a single Python file and use the same SDK to probe that GUI to get usable agent data."
  - Transcript: [[youtube-ZSQb5fzRFPw-transcript]]
- Switching from the built-in computer tool to Kua driver improved pass rate from 62% to 80% while using 34% fewer tokens.
  - Evidence: "If we take a look at the Kua bench basic data set scaled up to 4K resolution uh testing an agent they typically get around 62% pass rate but when you switch the agent computer tool from the built-in one to KU driver the pass rate jumps from 62% to 80% using 34% less tokens"
  - Transcript: [[youtube-ZSQb5fzRFPw-transcript]]
- Benchmark quality depends on adversarially trying to break tasks before admitting them to the dataset.
  - Evidence: "We have a matrix of agents attempt to do reward hacking and attempting to break the environment and we take all that data and we compile it into a nice code rabbit style code review and only tasks that survive our pipeline can enter the data set."
  - Transcript: [[youtube-ZSQb5fzRFPw-transcript]]
- A warm pool can shift sandbox startup overhead off GPUs, which improves utilization and lowers the effective cost of RL training.
  - Evidence: "Um so yeah so now when you have like this like uh redundancy in your pool you're paying the cost of that startup time on the infrastructure side not on the GPU side so your GPU workers have full utilization um yeah and then because we use this we can give you instant sandboxes for"
  - Transcript: [[youtube-ZSQb5fzRFPw-transcript]]

## Evidence Boundary
Derived from the linked official transcript. These are attributed talk takeaways and claims, not independent verification.
