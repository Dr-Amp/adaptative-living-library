---
title: Failure — Duplicate Autonomous Proposals
type: failure
status: active
area: autonomous-drive
subarea: proposal-gate
tags: [failure, autonomous-drive, noise-control]
confidence: high
related: ['[[Runbooks/autonomous-proposal-gate]]', '[[Decisions/scout-librarian-autonomous-delivery-ladder]]']
---
# Failure — Duplicate Autonomous Proposals

## What failed

An autonomous loop can repeatedly propose the same improvement if it does not check existing decisions, failures, pending promotions, and recent outputs.

## Lesson

Before proposing, run a local duplicate check against the Living Library and recent ledgers. If the idea already exists, update evidence or mark it absorbed instead of creating a new proposal.

Related: [[Runbooks/autonomous-proposal-gate]]
