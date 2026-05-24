# Architecture

Adaptative Living Library uses a simple promotion pipeline:

```text
explicit interests + session/memory scan
  -> raw onboarding candidates
  -> Adaptative Scout missions
  -> Adaptative Librero review
  -> stable canon page
  -> cheap preflight lookup
  -> grounded agent answer/action
  -> Adaptative Autonomous proposal when useful now
```

## Roles

- **Adaptative Scout** collects signals but does not decide canon.
- **Adaptative Librero** owns curation, de-duplication, contradictions, and promotion.
- **Adaptative Autonomous** proposes changes but does not execute risky side effects by default.
- **Adaptative Relic** tracks opt-in longitudinal patterns as context, not as authority.

## Knowledge layers

- **Raw:** untrusted collection area.
- **Inbox:** human/agent submissions waiting for review.
- **Ledger/output:** dated evidence of work done.
- **Canon:** stable decisions, failures, runbooks, concepts, maps, and indexes.

## Why onboarding exists

A living library should not start blank. The operator gives explicit topics, chooses model routing, and optionally lets the onboarding script scan local sessions/memory read-only. The result is raw source material, not canon.

## Why preflight exists

Agents should not reread an entire vault for every question. The preflight script ranks likely relevant canon pages using metadata, headings, and tags, then the agent reads only a few high-signal pages.
