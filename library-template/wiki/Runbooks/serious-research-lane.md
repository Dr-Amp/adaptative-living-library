---
title: Serious Research Lane
type: runbook
status: active
area: scout
subarea: serious-research-lane
tags: [runbook, scout, research, safety, source-registry]
confidence: high
related: ['[[Runbooks/scout-signal-ingest]]', '[[Runbooks/librarian-curation-loop]]', '[[Decisions/scout-librarian-architect-delivery-ladder]]']
---
# Serious Research Lane

## Purpose

Create a durable research front for a topic that matters without creating noisy crons, unsafe scanners, or premature canon.

Use for fronts such as security hardening, homestead/permaculture, model/tool watch, operations research, or any domain where the operator wants deep ongoing knowledge.

## Setup pattern

1. **Canon preflight**: search the library first; do not create a duplicate lane if an area/runbook already exists.
2. **PIR**: write a small priority-intelligence-requirements note: what to watch, why it matters, and what would change an action.
3. **Source registry**: list official docs, trusted maintainers, community sources, standards, papers, feeds, and known gaps.
4. **Priority queue**: keep questions ordered by risk/usefulness; avoid monomania.
5. **Scout collection**: gather evidence silently into raw/inbox or outputs.
6. **Librarian gate**: dedupe, verify, and promote only stable decisions, failures, runbooks, concepts, or explicit gaps.
7. **Architect proposal**: only if the evidence suggests a useful near-term change; keep it behind approval.

## Safety defaults

- No scanners, exploit runs, account changes, service restarts, firewall edits, cron creation, provider/model changes, or active memory writes by default.
- For security research, stay defensive and read-only unless the operator explicitly approves a scoped test.
- For fast-moving model/tool research, separate capability, pricing, API availability, UI availability, and terms/legal boundaries.
- For community sources, mark Discord/Reddit/forum gaps explicitly instead of inventing practitioner consensus.

## Output shape

A useful lane produces:

- one raw/evidence note or output ledger;
- at most a few high-quality candidates;
- explicit `coverage_gap` entries when required sources were not reached;
- a clear level: raw, knowledge candidate, Architect opportunity, or operator alert.

Do not create pages to appear busy. A week with no canon promotion can still be a successful review if it prevents noise.

Related: [[Runbooks/scout-signal-ingest]], [[Runbooks/librarian-curation-loop]]
