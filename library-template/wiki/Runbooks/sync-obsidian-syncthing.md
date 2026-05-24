---
title: Sync Obsidian + Syncthing
type: runbook
status: active
area: ops
subarea: sync-obsidian-syncthing
tags: [runbook, living-library, hermes]
confidence: high
related: ['[[Concepts/scout-librarian-architect-oracle-architecture]]', '[[wiki/Index]]']
---
# Sync Obsidian + Syncthing

## Purpose

Use canonical library plus synced mirror. Humans write into inbox. Agents promote to canon. Mobile can use a lightweight mirror excluding raw sources.

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
