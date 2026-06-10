---
title: Runbook → consumer wiring
type: runbook
status: active
area: library-ops
tags: [runbooks, profiles, wiring, instruction]
confidence: high
description: "A runbook only instructs if some agent actually loads it. Map every runbook to a real consumer and pin the mapping deterministically."
---

# Runbook → consumer wiring

A Living Library can accumulate dozens of runbooks that *nobody reads*. Search-based
discovery (preflight) helps an agent find knowledge when it knows what to ask — but a
runbook that defines how an agent must operate should not depend on the agent thinking
to search for it.

## The audit (run quarterly, or after adding agents)

1. Inventory `wiki/Runbooks/*.md`.
2. For each runbook, grep for real consumers across: scheduled-job prompts, agent/profile
   system prompts, and skills that reference it. A mention inside the librarian's own
   curation notes does NOT count as consumption.
3. Classify: `wired` (an operating surface loads it), `searchable-only` (only reachable
   via preflight), `no-consumer`.

## The wiring

For each profile/agent with an operating domain, append a short pinned block to its
system prompt — pointers, not content:

```text
# Runbooks for this profile (read them when operating in their domain)
- <library>/wiki/Runbooks/<runbook-one>.md
- <library>/wiki/Runbooks/<runbook-two>.md
```

Keep the block under ~400 characters per profile: this is núcleo+referencia — the prompt
carries the pointer, the library carries the content. Verify the config still parses and
that no other keys changed.

## The decisions

- `no-consumer` + domain retired → propose archival (never silently delete).
- `no-consumer` + domain alive → either wire it or accept `searchable-only` explicitly.
- Broken references (an index citing a runbook that does not exist) are lint findings —
  make your lint visible (a daily metric beats a script nobody runs).
