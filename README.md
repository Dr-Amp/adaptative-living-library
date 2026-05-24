# Hermes Living Ops Pack

A shareable, privacy-safe starter pack for building a **Living Operations Library** around Hermes Agent.

It packages the architecture, not anybody's private data:

- **Librarian**: curates raw notes into stable knowledge.
- **Scout**: gathers signals into quarantine/inbox lanes.
- **Autonomous Drive**: proposes operational improvements with safety gates.
- **Relic Lite**: captures longitudinal patterns as opt-in, read-only context.
- **Living Library**: an Obsidian-friendly markdown vault with categories, subcategories, tags, decisions, failures, runbooks, maps, and lints.

## What this repo is

A template and installer for a Hermes knowledge operating system:

```text
signals -> inbox/quarantine -> Librarian review -> canon pages -> cheap preflight before answers
```

It is designed to be installed into an existing Hermes home without exposing secrets or overwriting live configuration by default.

## What this repo is not

- Not a dump of a real person's `.hermes` directory.
- Not a prefilled memory database.
- Not a replacement for Hermes Agent.
- Not an auto-cron/autonomous service installer by default.
- Not a public backup system for private notes.

## Quick start

Dry run first:

```bash
git clone https://github.com/YOUR_USER/hermes-living-ops-pack
cd hermes-living-ops-pack
./install.sh --dry-run
```

Install locally:

```bash
./install.sh --apply --target ~/.hermes --library-name living-ops
```

Validate before publishing or sharing:

```bash
python3 scripts/sanitize_check.py .
python3 scripts/lint_library.py library-template
python3 scripts/library_preflight.py "how should the librarian promote failures" --root library-template --limit 5
```

## Installed layout

```text
~/.hermes/
├── libraries/living-ops/        # markdown Living Library
├── profiles/ops-librarian/      # optional Hermes profile template
├── profiles/ops-scout/
├── profiles/ops-autonomous-drive/
└── profiles/ops-relic-lite/
```

The installer does **not** restart the gateway, create cron jobs, change models/providers, or copy secrets.

## Core policy

For non-trivial questions, an agent should run a cheap local preflight first:

```bash
python3 ~/.hermes/libraries/living-ops/scripts/library_preflight.py "<query>" --limit 8
```

If the Library has relevant runbooks, decisions, failures, concepts, agents, or memory pages, read those before answering. Do not load the whole vault into context.

## Privacy stance

This pack is intentionally generic. The sanitizer checks for common leaks:

- real home paths
- private IPs
- tokens/secrets
- SSH/private keys
- personal denylist terms passed by the operator
- accidental `.env`, databases, dumps, logs, and backups

Run your own denylist before publishing:

```bash
python3 scripts/sanitize_check.py . --deny "YOUR_NAME" --deny "YOUR_SERVER" --deny "YOUR_PRIVATE_PROJECT"
```

## Sync and Obsidian

See `sync-guides/` for:

- Obsidian setup
- Syncthing on Windows, macOS, Linux
- Möbius Sync on iPhone
- Syncthing-Fork on Android

Recommended model:

```text
canonical Library -> generated/synced mirror -> Obsidian on devices
```

Users write into `_INBOX_USER/`; agents promote safely into canon.

## Safety defaults

- No automatic crons.
- No gateway restart.
- No model/provider changes.
- No active memory writes.
- No external publishing.
- No destructive sync.
- All installer writes are backed up when `--apply` is used.

## License

MIT. See `LICENSE`.
