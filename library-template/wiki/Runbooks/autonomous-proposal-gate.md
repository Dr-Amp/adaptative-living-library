---
title: Autonomous Proposal Gate
type: runbook
status: active
area: ops
subarea: autonomous-proposal-gate
tags: [runbook, living-library, hermes]
confidence: high
related: ['[[Concepts/scout-librero-autonomous-relic-architecture]]', '[[wiki/Index]]']
---
# Autonomous Proposal Gate

## Purpose

Autonomous Drive proposes improvements only after duplicate checks and risk classification. Risky actions require explicit approval.

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
