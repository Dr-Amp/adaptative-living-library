---
title: Librero Curation Loop
type: runbook
status: active
area: ops
subarea: librero-curation-loop
tags: [runbook, living-library, hermes]
confidence: high
related: ['[[Concepts/scout-librero-autonomous-relic-architecture]]', '[[wiki/Index]]']
---
# Librero Curation Loop

## Purpose

Review inbox/raw material, classify it, promote only durable knowledge, update indexes/logs, run lints, and avoid creating canon for noise.

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
