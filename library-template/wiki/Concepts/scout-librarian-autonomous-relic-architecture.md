---
title: Scout, Librarian, Autonomous, Relic and the Living Library
type: concept
status: active
area: scout
subarea: architecture
tags: [concept, scout, librarian, autonomous-drive, relic, living-library]
confidence: high
related: ['[[Mapas/Scout Librarian Autonomous Relic]]', '[[Decisions/scout-librarian-autonomous-delivery-ladder]]']
---
# Scout, Librarian, Autonomous, Relic and the Living Library

```text
Scout = goes out and brings raw signals
Librarian = curates, links, promotes, rejects
Autonomous Drive = proposes improvements that can help now
Relic Lite = keeps opt-in longitudinal patterns for tone/context
Living Library = stable human-readable canon
```

## Ideal flow

1. Librarian or Autonomous Drive reads library gaps and recent evidence.
2. Scout receives missions and gathers raw signals.
3. Librarian classifies raw material: discard, pending evidence, canon, contradiction, failure, action.
4. Autonomous Drive receives only actionable opportunities.
5. Relic Lite observes long-term patterns and helps adapt interaction style.
6. The human only gets alerts when attention is truly useful.

## Hard limit

This architecture does not authorize side effects by itself. Config, services, crons, models/providers, credentials, and active memory require explicit approval.

Related: [[Runbooks/librarian-curation-loop]], [[Runbooks/autonomous-proposal-gate]]
