---
title: "Highlights: Special topics in Kernels, RL, Reward Hacking in Agents"
category: "highlights"
generatedBy: "talk-semantic-digestion-v1"
sourceLabels: ["Official recording transcript", "Semantic digestion"]
---
# Highlights: Special topics in Kernels, RL, Reward Hacking in Agents

- Talk: [[2026-06-29-daniel-han-special-topics-in-kernels-rl-reward-hacking-in-agents]]

## Highlights
- Treat benchmark results as system tests, because prompts, harnesses, providers, and implementation details can swing measured accuracy as much as the model itself.
  - Evidence: "It's not the model anymore. Um and so like you know as we have seen if they have accidentally botched you know if they accidentally botched the harness you will get reduced accuracy."
  - Transcript: [[youtube-uIiA6DquRiE-transcript]]
- For local open-source deployment, he recommends downloading from Hugging Face and using stable runtimes like Llama CPP or Llama server.
  - Evidence: "I think Llama CPP and Llama server is probably the most bugfree system. So I would like suggest yes you should download from hugging face."
  - Transcript: [[youtube-uIiA6DquRiE-transcript]]
- Before writing custom kernels, try torch.compile first, since the talk shows it can outperform handwritten kernels on modern PyTorch.
  - Evidence: "Um so the main point is you should always firstly look at torch compile right before you write a kernel use torch compile first do not start learning how to do triton or you know cuda or whatever is your favorite coding language for kernels don't do that instead use torch compile um even worse"
  - Transcript: [[youtube-uIiA6DquRiE-transcript]]
- If you want trustworthy RL signals, use process supervision or anti-hacking filters, because outcome-only rewards can be gamed.
  - Evidence: "Um and process supervision what you do is you manually check every single line not you don't just assign plus 10 to the final you know the answer is correct right the answer is correct plus 10 assign every single line as plus 10 you don't do this instead what you do is you assign"
  - Transcript: [[youtube-uIiA6DquRiE-transcript]]
- Benchmarks should be designed to be hard to benchmax and easy to verify, such as random math tasks or constrained generation tasks.
  - Evidence: "The first condition is the benchmark must not must not be benchmaxable. Right? How do you make a benchmark that is extremely hard to benchmark, right?"
  - Transcript: [[youtube-uIiA6DquRiE-transcript]]

## Evidence Boundary
Derived from the linked official transcript. These are attributed talk takeaways and claims, not independent verification.
