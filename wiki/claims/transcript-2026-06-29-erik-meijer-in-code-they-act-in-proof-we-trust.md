---
title: "Claims: In Code They Act, In Proof We Trust"
category: "claims"
generatedBy: "talk-semantic-digestion-v1"
sourceLabels: ["Official recording transcript", "Semantic digestion"]
---
# Claims: In Code They Act, In Proof We Trust

- Talk: [[2026-06-29-erik-meijer-in-code-they-act-in-proof-we-trust]]

## Claims
- The speaker argues that adding tool calls changes AI safety from a theoretical concern into a real-world danger because the agent can now cause side effects during execution. (`explicit`)
  - Evidence: "Um, now the act of adding tool calls changes AI safety from a philosophical debate to something that causes real danger."
  - Transcript: [[youtube--CnA2lGfymY-transcript]]
- He says a raw IO value is a black box, so it cannot be reasoned about directly. (`explicit`)
  - Evidence: "We want to be able to check it. All right. Now the problem is that if you get a value of type IO of A um that's a really a black box and the lean manual says that is a black box you cannot reason about it."
  - Transcript: [[youtube--CnA2lGfymY-transcript]]
- He proposes moving the agentic loop out of the model by having the model produce a plan that another component executes. (`explicit`)
  - Evidence: "Um, but all that we're doing is we're pushing this IO to the right, to the right. And what you now see is that the tool belt of Claude goes to the left, to the left, and suddenly Claude is a nice puppy again because instead of executing the agentic loop, it creates a plan and says, \"Here is the plan to do the agentic loop.\" And now Bernie will take that plan and we'll execute it."
  - Transcript: [[youtube--CnA2lGfymY-transcript]]
- He identifies the core fix as proof-carrying code: the agent supplies a program and a proof that the program is safe before it runs. (`explicit`)
  - Evidence: "Now you would say Eric, oh you're a genius. No, I'm my brain is the size of a peanut. This is something that's called proof carrying code and it was invented by academics in the 1990s and I'm just stealing it."
  - Transcript: [[youtube--CnA2lGfymY-transcript]]
- He claims this approach can deliver mathematically proven safe agentic compute using only elementary type systems and programming-language machinery. (`explicit`)
  - Evidence: "The language doesn't matter. It's it's the um the principle that matters. So hopefully you've learned tonight that it is actually possible to have mathematically proven safe agentic compute and it only requires very elementary type systems and programming language machinery. Thank you so much."
  - Transcript: [[youtube--CnA2lGfymY-transcript]]

## Evidence Boundary
Derived from the linked official transcript. These are attributed talk takeaways and claims, not independent verification.
