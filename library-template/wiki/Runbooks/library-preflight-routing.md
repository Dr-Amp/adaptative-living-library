---
title: Library Preflight Routing
type: runbook
status: active
area: ops
subarea: library-preflight-routing
tags: [runbook, living-library, hermes]
confidence: high
related: ['[[Concepts/scout-librero-autonomous-relic-architecture]]', '[[wiki/Index]]']
---
# Library Preflight Routing

## Purpose

Before answering non-trivial questions, run a cheap deterministic search over metadata/headings. Read only the top relevant canon pages. Do not load the whole library.

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

Related: [[Concepts/scout-librero-autonomous-relic-architecture]]
