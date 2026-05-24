# Changelog

## v0.2.0 - 2026-05-24

Renamed the project to **Adaptative Living Library** and added first-run onboarding.

### Added

- `scripts/onboard.py` for dry-run-first local onboarding.
- Model selection for Adaptative Scout, Librero, Autonomous, and Relic profiles.
- Scout topic seeding through repeated `--topic` flags.
- Read-only session/memory scan into `raw/onboarding/` as source material.
- Bind-ready profile generation under `profiles/adaptative-*`.
- Obsidian vault linking via `--obsidian-vault`.
- `docs/onboarding.md`.
- Release checks now include onboarding smoke tests.

### Changed

- Product name: Hermes Living Ops Pack → Adaptative Living Library.
- Agent/profile names: Adaptative Scout, Adaptative Librero, Adaptative Autonomous, Adaptative Relic.
- Default library name: `adaptative-living-library`.

### Safety

- Onboarding is dry-run by default.
- No global config edits, cron creation, gateway restart, model/provider changes, active memory writes, or uploads.

## v0.1.0 - 2026-05-24

Initial public-safe template release.

### Added

- Living Library template with maps, runbooks, decisions, failures, outputs, questions, and memory notes.
- Generic profiles for Librarian, Scout, Autonomous Drive, and Relic Lite roles.
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
