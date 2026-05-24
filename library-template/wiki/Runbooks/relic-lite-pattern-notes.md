---
title: Relic Lite Pattern Notes
type: runbook
status: active
area: ops
subarea: relic-lite-pattern-notes
tags: [runbook, living-library, hermes]
confidence: high
related: ['[[Concepts/scout-librarian-autonomous-relic-architecture]]', '[[wiki/Index]]']
---
# Relic Lite Pattern Notes

## Purpose

Relic Lite stores opt-in longitudinal observations as hypotheses with confidence. It adapts tone/context but does not present portraits unless asked.

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

Related: [[Concepts/scout-librarian-autonomous-relic-architecture]]
