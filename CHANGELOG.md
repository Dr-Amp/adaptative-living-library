# Changelog

## v0.3.5 - 2026-06-08

### Added

- Added `library-template/wiki/Runbooks/memory-boundaries.md` to separate raw capture, outputs, canon, Oracle notes, and active memory writes.
- Added `library-template/wiki/Runbooks/serious-research-lane.md` for durable research fronts with PIR, source registry, priority queue, Scout collection, Librarian promotion, explicit coverage gaps, and approval gates.
- Added `docs/recent-canon-hardening.md` explaining the public-safe class-level lessons without copying private library content.

### Safety

- Keeps risky operations off by default: no scanners, crons, service restarts, provider/model changes, active memory writes, credential edits, or external side effects without approval.

## v0.3.4 - 2026-05-24

### Changed

- Replaced the previous decorative Shaolin SVG with a minimal PNG operating diagram that explains the answer, curation, improvement, and review/memory lanes and includes Architect explicitly.

## v0.3.3 - 2026-05-24

### Changed

- Reworked the architecture SVG into a Baoyu-inspired infographic with an isometric abandoned Shaolin monastery aesthetic while keeping the README-safe static SVG format.

## v0.3.2 - 2026-05-24

### Changed

- Replaced README/docs Mermaid-only diagram with a static SVG architecture diagram so GitHub/mobile previews show the visual reliably.

## v0.3.1 - 2026-05-24

### Added

- Mermaid architecture diagrams in `README.md` and `docs/architecture.md` showing onboarding, raw/inbox, canon, preflight, and the Scout/Librarian/Architect/Oracle roles.

## v0.3.0 - 2026-05-24

Standardized the four public agent names.

### Changed

- Agent/profile display names are now **Librarian**, **Scout**, **Architect**, and **Oracle**.
- Profile and skill slugs are now `librarian`, `scout`, `architect`, and `oracle`.
- Onboarding model flags are now `--librarian-model`, `--scout-model`, `--architect-model`, and `--oracle-model`.
- Template pages, runbooks, examples, indexes, and architecture links were renamed to the same vocabulary.

## v0.2.0 - 2026-05-24

Renamed the project to **Adaptative Living Library** and added first-run onboarding.

### Added

- `scripts/onboard.py` for dry-run-first local onboarding.
- Model selection for Scout, Librarian, Architect, and Oracle profiles.
- Scout topic seeding through repeated `--topic` flags.
- Read-only session/memory scan into `raw/onboarding/` as source material.
- Bind-ready profile generation under the four role profile directories.
- Obsidian vault linking via `--obsidian-vault`.
- `docs/onboarding.md`.
- Release checks now include onboarding smoke tests.

### Changed

- Product name: Hermes Living Ops Pack → Adaptative Living Library.
- Agent/profile names: Scout, Librarian, Architect, Oracle.
- Default library name: `adaptative-living-library`.

### Safety

- Onboarding is dry-run by default.
- No global config edits, cron creation, gateway restart, model/provider changes, active memory writes, or uploads.

## v0.1.0 - 2026-05-24

Initial public-safe template release.

### Added

- Living Library template with maps, runbooks, decisions, failures, outputs, questions, and memory notes.
- Generic profiles for Librarian, Scout, Architect, and Oracle roles.
- Generic skills for the same four roles.
- Safe installer with dry-run default and `--apply` opt-in.
- Sanitizer, library lint, cheap preflight, and release-check scripts.
- Obsidian, Syncthing, iPhone/Möbius, Android, Windows, macOS, and Linux sync guides.
- GitHub Actions CI for publish-safety checks.

### Safety

- No private data payload.
- No automatic cron/service/model/provider changes.
- No active memory writes.
- Installer backs up overwritten files on apply.
