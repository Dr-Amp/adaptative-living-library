# Changelog

## v0.1.0 - 2026-05-24

Initial public-safe template release.

### Added

- Living Library template with areas, subareas, tags, maps, runbooks, decisions, failures, outputs, questions, and memory notes.
- Generic Hermes profiles for Librarian, Scout, Autonomous Drive, and Relic Lite roles.
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
