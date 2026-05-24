---
title: Living Ops Library Schema
type: schema
status: active
area: ops
subarea: library-governance
tags: [schema, living-library, hermes]
confidence: high
---
# Living Ops Library Schema

## Domain

Operational knowledge for a Hermes-based agent team: routing, memory, scouting, curation, architect proposals, longitudinal context, sync, and safety gates.

## Canon layers

- `raw/`: optional immutable source captures. Do not edit in place.
- `wiki/`: curated knowledge and human-readable maps.
- `_INBOX_USER/`: safe human input lane for notes, research, and corrections.
- `wiki/Outputs/`: compact ledgers and reports, not the primary answer surface.

## Required frontmatter for wiki pages

```yaml
title: Human title
type: area | agent | concept | decision | failure | runbook | memory | index | map | output | question
status: active | draft | archived
area: ops | scout | architect | oracle | memory | sync | library
tags: [living-library]
confidence: high | medium | low
```

Recommended optional fields:

```yaml
subarea: curation
related: ['Runbooks/example']
audience: [operator, agent]
canonical_status: active | absorbed | superseded | ledger
absorbed_by: ['Runbooks/example']
```

## Promotion rules

Promote only if the note:

1. prevents repeated user steering;
2. prevents future agent errors;
3. turns raw evidence into a reusable runbook, decision, failure, concept, or map;
4. resolves or marks a contradiction;
5. improves immediate operations without adding notification noise.

## Safety gates

Require explicit approval before:

- editing live Hermes config;
- creating/removing cron jobs;
- restarting gateways/services;
- changing models/providers;
- writing active memory stores;
- publishing externally;
- touching credentials or secrets.

## Navigation standards

- Every stable page should link to at least two related pages.
- Prefer human maps over dumping users into file paths.
- Keep pages short. Split long operational reports into runbooks + output ledgers.
