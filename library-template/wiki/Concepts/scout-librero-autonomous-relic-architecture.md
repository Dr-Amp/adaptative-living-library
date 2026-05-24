---
title: Scout, Librero, Autonomous, Relic and the Living Library
type: concept
status: active
area: scout
subarea: architecture
tags: [concept, scout, librero, autonomous-drive, relic, living-library]
confidence: high
related: ['[[Mapas/Scout Librero Autonomous Relic]]', '[[Decisions/scout-librero-autonomous-delivery-ladder]]']
---
# Scout, Librero, Autonomous, Relic and the Living Library

```text
Scout = goes out and brings raw signals
Librero = curates, links, promotes, rejects
Autonomous Drive = proposes improvements that can help now
Relic = keeps opt-in longitudinal patterns for tone/context
Living Library = stable human-readable canon
```

## Ideal flow

1. Librero or Autonomous Drive reads library gaps and recent evidence.
2. Scout receives missions and gathers raw signals.
3. Librero classifies raw material: discard, pending evidence, canon, contradiction, failure, action.
4. Autonomous Drive receives only actionable opportunities.
5. Relic observes long-term patterns and helps adapt interaction style.
6. The human only gets alerts when attention is truly useful.

## Hard limit

This architecture does not authorize side effects by itself. Config, services, crons, models/providers, credentials, and active memory require explicit approval.

Related: [[Runbooks/librero-curation-loop]], [[Runbooks/autonomous-proposal-gate]]
