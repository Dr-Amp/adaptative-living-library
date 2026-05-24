# Architecture

Hermes Living Ops Pack uses a simple promotion pipeline:

```text
raw signal
  -> inbox/quarantine
  -> librarian review
  -> stable canon page
  -> cheap preflight lookup
  -> grounded agent answer/action
```

## Roles

- **Ops Librarian** owns curation, de-duplication, contradictions, and promotion.
- **Ops Scout** collects signals but does not decide canon.
- **Ops Autonomous Drive** proposes changes but does not execute risky side effects by default.
- **Ops Relic Lite** tracks patterns as opt-in context, not as authority.

## Knowledge layers

- **Raw:** untrusted collection area.
- **Inbox:** human/agent submissions waiting for review.
- **Ledger/output:** dated evidence of work done.
- **Canon:** stable decisions, failures, runbooks, concepts, maps, and indexes.

## Why preflight exists

Agents should not reread an entire vault for every question. The preflight script ranks likely relevant canon pages using metadata, headings, and tags, then the agent reads only a few high-signal pages.
