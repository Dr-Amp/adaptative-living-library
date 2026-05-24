---
title: Failure — Duplicate Architect Proposals
type: failure
status: active
area: architect
subarea: proposal-gate
tags: [failure, architect, noise-control]
confidence: high
related: ['[[Runbooks/architect-proposal-gate]]', '[[Decisions/scout-librarian-architect-delivery-ladder]]']
---
# Failure — Duplicate Architect Proposals

## What failed

An architect loop can repeatedly propose the same improvement if it does not check existing decisions, failures, pending promotions, and recent outputs.

## Lesson

Before proposing, run a local duplicate check against the Living Library and recent ledgers. If the idea already exists, update evidence or mark it absorbed instead of creating a new proposal.

Related: [[Runbooks/architect-proposal-gate]]
