---
title: Scout Signal Ingest
type: runbook
status: active
area: ops
subarea: scout-signal-ingest
tags: [runbook, living-library, hermes]
confidence: high
related: ['[[Concepts/scout-librarian-architect-oracle-architecture]]', '[[wiki/Index]]']
---
# Scout Signal Ingest

## Purpose

Scout writes raw signals with source, timestamp, confidence, lane, and why it might matter. Scout does not directly promote to canon.

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
