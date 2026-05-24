---
title: Scout → Librero → Autonomous Delivery Ladder
type: decision
status: active
area: scout
subarea: delivery
tags: [decision, scout, autonomous-drive, noise-control]
confidence: high
related: ['[[Concepts/scout-librero-autonomous-relic-architecture]]', '[[Runbooks/scout-signal-ingest]]']
---
# Scout → Librero → Autonomous Delivery Ladder

## Decision

Signals should move through a ladder instead of directly notifying the human.

- Level 0: raw silent evidence.
- Level 1: knowledge candidate for Librero review.
- Level 2: autonomous opportunity that can improve the system soon.
- Level 3: human alert because it is urgent, risky, or strongly useful now.

Default: silence local first, compact digest second, direct alert only when justified.
