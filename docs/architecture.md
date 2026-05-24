# Architecture

Adaptative Living Library uses a simple promotion pipeline:

```text
explicit interests + session/memory scan
  -> raw onboarding candidates
  -> Scout missions
  -> Librarian review
  -> stable canon page
  -> cheap preflight lookup
  -> grounded agent answer/action
  -> Architect proposal when useful now
```

## System diagram

```mermaid
flowchart TB
  subgraph Onboarding["1. Onboarding / setup"]
    Human([Operator]):::human
    Topics[Topics of interest]:::input
    Models[Provider + model routing]:::input
    Scan[Read-only session / memory scan]:::input
    Profiles[Bind-ready profiles<br/>librarian · scout · architect · oracle]:::process
    Seeds[(raw/onboarding seeds)]:::raw
    Human --> Topics
    Human --> Models
    Topics --> Seeds
    Scan --> Seeds
    Models --> Profiles
  end

  subgraph Library["2. Local Markdown Living Library"]
    Raw[(Raw + Inbox<br/>evidence, not canon)]:::raw
    Canon[(Canon<br/>Decisions · Failures · Runbooks · Concepts · Maps)]:::canon
    Gaps[Questions + gaps]:::process
    Logs[(Outputs + Logs<br/>audit trail)]:::ledger
  end

  subgraph Agents["3. Roles"]
    Scout[Scout<br/>researches + collects signals]:::agent
    Librarian[Librarian<br/>dedupes + promotes durable knowledge]:::agent
    Architect[Architect<br/>turns opportunities into gated proposals]:::agent
    Oracle[Oracle<br/>opt-in longitudinal context]:::agent
  end

  subgraph Runtime["4. Answer/action loop"]
    Question[User / agent question]:::input
    Preflight[Cheap preflight<br/>rank likely relevant canon]:::process
    Answer[Grounded answer]:::output
    Approval{Explicit approval<br/>for side effects}:::gate
  end

  Profiles --> Scout
  Profiles --> Librarian
  Profiles --> Architect
  Profiles --> Oracle

  Seeds --> Raw
  Canon -->|missions + gaps| Scout
  Scout -->|source-backed signals| Raw
  Raw --> Librarian
  Librarian -->|stable| Canon
  Librarian -->|needs evidence| Gaps
  Librarian -->|work record| Logs
  Canon --> Preflight
  Question --> Preflight --> Answer
  Oracle -. tone/context only .-> Preflight
  Librarian -->|actionable opportunity| Architect
  Architect -->|proposal + evidence + risk| Approval
  Approval -->|approved| Answer
  Architect --> Logs

  classDef human fill:#fff7ed,stroke:#f97316,color:#111827;
  classDef input fill:#eff6ff,stroke:#3b82f6,color:#111827;
  classDef raw fill:#fef3c7,stroke:#f59e0b,color:#111827;
  classDef agent fill:#ecfeff,stroke:#06b6d4,color:#111827;
  classDef canon fill:#ecfdf5,stroke:#10b981,color:#111827;
  classDef process fill:#f5f3ff,stroke:#8b5cf6,color:#111827;
  classDef gate fill:#fff1f2,stroke:#f43f5e,color:#111827;
  classDef output fill:#f0fdf4,stroke:#22c55e,color:#111827;
  classDef ledger fill:#f8fafc,stroke:#64748b,color:#111827;
```

### Reading the diagram

- **Onboarding** creates topics, raw seeds, model choices, and four bind-ready profiles without touching live config by default.
- **Scout** feeds the library with sourced signals, but does not decide what becomes stable knowledge.
- **Librarian** is the canon gate: it deduplicates, promotes, rejects, marks gaps, and records decisions.
- **Oracle** may inform tone/context when explicitly enabled; it is not a source of authority over canon.
- **Architect** receives only actionable opportunities and turns them into approval-gated proposals.
- **Preflight** keeps answers cheap and grounded: it ranks a few likely relevant canon pages instead of loading the whole vault.
- **Approval** is mandatory for risky side effects: crons, gateway restarts, provider/model changes, credentials, active memory writes, or external publishing.

## Roles

- **Scout** collects signals but does not decide canon.
- **Librarian** owns curation, de-duplication, contradictions, and promotion.
- **Architect** proposes changes but does not execute risky side effects by default.
- **Oracle** tracks opt-in longitudinal patterns as context, not as authority.

## Knowledge layers

- **Raw:** untrusted collection area.
- **Inbox:** human/agent submissions waiting for review.
- **Ledger/output:** dated evidence of work done.
- **Canon:** stable decisions, failures, runbooks, concepts, maps, and indexes.

## Why onboarding exists

A living library should not start blank. The operator gives explicit topics, chooses model routing, and optionally lets the onboarding script scan local sessions/memory read-only. The result is raw source material, not canon.

## Why preflight exists

Agents should not reread an entire vault for every question. The preflight script ranks likely relevant canon pages using metadata, headings, and tags, then the agent reads only a few high-signal pages.
