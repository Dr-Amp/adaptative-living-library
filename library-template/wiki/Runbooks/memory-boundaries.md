---
title: Memory Boundaries
type: runbook
status: active
area: memory
subarea: memory-boundaries
tags: [runbook, memory, safety, living-library]
confidence: high
related: ['[[Runbooks/librarian-curation-loop]]', '[[Runbooks/library-preflight-routing]]', '[[Agents/oracle]]']
---
# Memory Boundaries

## Purpose

Keep the library useful without turning every source, transcript, sensor, or agent hunch into active memory.

## Layer contract

```text
raw source -> summary -> candidate -> librarian gate -> canon or discard
```

- **Raw/inbox**: evidence only. It may contain messy notes, transcripts, logs, or external sources.
- **Outputs/ledgers**: compact record of what was reviewed, promoted, discarded, or left pending.
- **Canon**: stable decisions, failures, runbooks, concepts, agent contracts, and memory maps.
- **Active memory stores**: compact facts/preferences only, written separately and only when approved by local policy.

## Promotion rules

Promote only when the note:

1. prevents repeated mistakes;
2. records a durable decision or preference;
3. becomes a reusable runbook or failure lesson;
4. resolves or marks an important contradiction;
5. changes how an agent should safely operate.

Do not promote:

- raw transcripts or intimate/private dumps;
- temporary task progress;
- live credentials, account state, balances, tickets, commits, job IDs, paths, or screenshots;
- unverified hunches;
- automatic write hooks that bypass the Librarian gate.

## Live-capture guardrail

For audio, wearable, browser, email, or sensor capture, use this sequence:

```text
export/read-only capture -> local transcript/summary -> candidate note -> human or Librarian review -> canon/memory only if durable
```

Default: no automatic writes to active memory and no diagnosis, profiling, or hidden personalization. Oracle may summarize patterns, but Canon and explicit operator preference override Oracle notes.

## Verification before claiming promotion

- Cite the evidence path.
- Read back the page or output touched.
- Run the library lint.
- State what was not written because it required approval.

Related: [[Runbooks/librarian-curation-loop]], [[Agents/oracle]]
