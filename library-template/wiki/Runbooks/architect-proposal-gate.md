---
title: Architect Proposal Gate
type: runbook
status: active
area: ops
subarea: architect-proposal-gate
tags: [runbook, living-library, hermes]
confidence: high
related: ['[[Concepts/scout-librarian-architect-oracle-architecture]]', '[[wiki/Index]]']
---
# Architect Proposal Gate

## Purpose

Architect proposes improvements only after duplicate checks and risk classification. Risky actions require explicit approval.

## Procedure

1. Gather the smallest relevant context.
2. Separate evidence from inference.
3. Prefer local files and explicit sources.
4. Avoid side effects unless approved.
5. Log durable changes.

## Not allowed by default

- service restarts
- cron changes
- provider/model changes
- credential writes
- active memory writes
- external publishing

Related: [[Concepts/scout-librarian-architect-oracle-architecture]]
