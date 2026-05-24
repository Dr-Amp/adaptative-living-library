---
title: Oracle Pattern Notes
type: runbook
status: active
area: ops
subarea: oracle-pattern-notes
tags: [runbook, living-library, hermes]
confidence: high
related: ['[[Concepts/scout-librarian-architect-oracle-architecture]]', '[[wiki/Index]]']
---
# Oracle Pattern Notes

## Purpose

Oracle stores opt-in longitudinal observations as hypotheses with confidence. It adapts tone/context but does not present portraits unless asked.

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
