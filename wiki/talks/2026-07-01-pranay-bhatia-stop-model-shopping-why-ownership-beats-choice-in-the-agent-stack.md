---
title: "Stop Model Shopping: Why Ownership Beats Choice in the Agent Stack"
category: "talks"
date: "2026-07-01"
time: "12:05pm-12:25pm"
track: "Inference"
room: "Leadership 1"
speakers: ["Pranay Bhatia"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
---

# Stop Model Shopping: Why Ownership Beats Choice in the Agent Stack

## Official Schedule Context
- Date/time: 2026-07-01 · 12:05pm-12:25pm
- Track/room: Inference · Leadership 1
- Speaker(s): Pranay Bhatia
- Session type/status: session · confirmed

## Official Description
Teams shipping successful agents at scale know that model ownership is now a much more durable

advantage than model choice. They’re fine-tuning open models using their proprietary data, building

tight data feedback loops between their products and their models, and treating customization as a

core product discipline to differentiate. I’ve spent the last decade building AI infrastructure,

first as co-creator and head of PyTorch at Meta, now as CEO of Fireworks AI, where my team powers AI

agent infrastructure stacks for companies like Cursor, Notion, Uber, DoorDash, and Vercel. I’ve

watched hundreds of teams try to ship agents into production, and the patterns behind their success

and failure are remarkably consistent. In this talk, I’ll share hard-won lessons from real

production deployments across coding, productivity, and enterprise use cases, like: - Model choice

matters, but model ownership matters more. Fine-tuning on proprietary data and building a feedback

loop between your product and your models creates compounding advantages that no API swap will ever

replicate, and it’s now the standard for all state-of-the-art models. It’s how Cursor hit 1,000

tokens/sec with quality that off-the-shelf models could never match, and it’s how Quora saw 3x speed

improvements in its chatbot Poe. - The eval gap is where most agent projects die. Teams will spend

months on prompt engineering and model selection, then ship without rigorous evaluation. Treating AI

development with the same discipline as software development, with CI/CD, regression testing, and

continuous evaluation, is what separates production-grade agents from impressive demos. A custom

evaluation suite, coupled with RFT, is how Genspark achieved 12% higher quality on their trained

model, resulting in a 50% cost reduction. - The real moat is the data flywheel. When you own the

loop between your product, your data, and your models, every interaction makes the system better.

Surrendering that loop to a third-party provider means surrendering the very data that makes your

product defensible. Ownership is how Vercel created a custom code model that matched competitor

quality at 40x speed. I’ll ground this talk in real examples I’ve seen work and fail across hundreds

of agent deployments.

## Related YouTube Video
No related AI Engineer channel video found yet.

## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## People
- [[pranay-bhatia]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.
