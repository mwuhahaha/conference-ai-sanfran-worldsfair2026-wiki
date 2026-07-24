---
title: "KVM"
category: "tools"
generatedBy: "talk-semantic-digestion-v1"
sourceLabels: ["Official recording transcript", "Semantic digestion"]
sourceAssessment:
  schemaVersion: 1
  claimId: claim:4321b09b83e1cccfa98839e0e66baab4b238b3241c584272f7548811341eaecb
  subjectId: tool:kvm
  domain: tools page evidence coverage
  intendedUse: attributed_context
  asOf: '2026-07-24T00:00:00.000000Z'
  state: limited
  basis: official_primary_canonical
  message: This page is limited to source-attributed facts; independent support for broader claims may be limited.
  publicSourceIds:
  - source:official-wf26-youtube-OqM67QG_Ikk
sourceAssessmentBodySha256: sha256:ee9a7f8501d34c4a73574444e5e9808b55f5a09eee1d2c6e46d083960145ebac
---
# KVM

## Overview
The Linux hypervisor interface that VMMs call to start guests.

## Transcript Digest Evidence
This section is generated from 2 evidence-bound talk digest(s).

- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1|'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt 1']] — The Linux hypervisor interface that VMMs call to start guests.
  - Transcript: [[youtube-OqM67QG_Ikk-transcript]]
  - Evidence: "And then we finally call start. And when we call start, you can see from previous diagrams that the VMM literally calls into dev KVM just like before and it starts these like guest micro VM."
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt2|'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt2']] — Linux hypervisor API used by VMMs to launch and manage guests.
  - Transcript: [[youtube-OqM67QG_Ikk-transcript]]
  - Evidence: "QEMU and other VMMs, their sole job is to talk to dev KVM. So, you see that arrow going down like the dev KVM is the hypervisor API of the Linux kernel."

## Evidence Boundary
This page is content-derived from official event transcripts. The linked transcript excerpts support presence and attributed framing; they do not independently verify broader claims.
