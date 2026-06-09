# Changelog

## v0.4.0 - 2026-06-10 — Knowledge Lifecycle & Eternal Library

### Added

- **Knowledge lifecycle runbook** (`library-template/wiki/Runbooks/knowledge-lifecycle.md`): 5-phase cycle from ingest → curation → structured knowledge → promotion → archive, with automatic triggers for each phase.
- **Claims system** (`library-template/wiki/Claims/`): structured verifiable assertions with confidence, expiry dates, and evidence links.
- **Contradiction detector** (`library-template/wiki/Contradictions/`): index + automated detection between claims in the same area.
- **Librarian weekly script** (`library-template/scripts/librarian_weekly.py`): autonomous pass that runs lint, rebuilds knowledge map, detects contradictions, finds expired claims, detects unabsorbed outputs, and commits to git.
- **Knowledge map auto-generator** (`library-template/scripts/build_knowledge_map.py`): regenerates the Knowledge Map from frontmatter of all wiki pages.
- **Contradiction detector script** (`library-template/scripts/detect_contradictions.py`): semantic overlap detection between claims.
- **Ecosystem integration runbook** (`library-template/wiki/Runbooks/ecosystem-scout-librarian-oracle-architect.md`): documents the full Scout → Librarian → Oracle → Architect pipeline.
- **Federation template** (`library-template/wiki/Runbooks/federation-template.md`): how to create new federated libraries for other domains.

### Fixed

- **lint_editorial_karpathy.py**: fixed `absorbed_by` requirement — only checked when `canonical_status: absorbed`, not for all outputs.

### Changed

- **SCHEMA.md frontmatter**: added `canonical_status` field with allowed values (raw_signal, curated_output, absorbed, ledger, superseded).
- **Knowledge Map**: now auto-generated from metadata instead of manually maintained.

## v0.3.5 - 2026-06-08
