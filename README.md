# Hermes Living Ops Pack

A privacy-safe starter pack for building a **Living Operations Library** around Hermes Agent.

It packages an operating pattern, not anyone's private data:

- **Librarian**: reviews noisy notes and promotes stable knowledge.
- **Scout**: collects external or internal signals into quarantine lanes.
- **Autonomous Drive**: turns useful signals into gated recommendations.
- **Relic Lite**: captures longitudinal patterns as opt-in, read-only context.
- **Living Library**: an Obsidian-friendly Markdown vault with areas, subareas, tags, decisions, failures, runbooks, maps, and lints.

## Status

`v0.1.0` template release. It is intentionally conservative:

- dry-run first;
- no automatic crons;
- no gateway restarts;
- no model/provider changes;
- no active memory writes;
- no copied private data.

## What this repo is

A template and installer for a Hermes knowledge operating system:

```text
signals -> inbox/quarantine -> Librarian review -> canon pages -> cheap preflight before answers
```

Use it when you want agents to stop relying on scattered chat history and start checking a curated local wiki before answering or acting.

## What this repo is not

- Not a dump of a real `.hermes` directory.
- Not a prefilled memory database.
- Not a replacement for Hermes Agent.
- Not an autonomous-service installer by default.
- Not a public backup system for private notes.

## Architecture

```text
Living Ops Pack
├─ library-template/        # public-safe Markdown vault
├─ profiles/                # optional Hermes profile templates
├─ skills/                  # generic skills for the four roles
├─ scripts/                 # installer, sanitizer, lint, preflight
├─ sync-guides/             # Obsidian/Syncthing/mobile guides
└─ tests/                   # structural and publish-safety checks
```

The core loop is deliberately boring and auditable:

1. Collect raw signals into inbox/quarantine.
2. Curate only durable knowledge into canon pages.
3. Record decisions, failures, runbooks, and open questions.
4. Run a cheap local preflight before non-trivial answers.
5. Keep private memory stores separate from publishable wiki content.

## Quick start

Dry-run first:

```bash
git clone https://github.com/YOUR_USER/hermes-living-ops-pack
cd hermes-living-ops-pack
./install.sh --dry-run
```

Install locally only after reading the output:

```bash
./install.sh --apply --target ~/.hermes --library-name living-ops
```

Optionally install the generic skills too:

```bash
./install.sh --apply --target ~/.hermes --library-name living-ops --install-skills
```

## Installed layout

```text
~/.hermes/
├── libraries/living-ops/        # Markdown Living Library
├── profiles/ops-librarian/      # optional Hermes profile template
├── profiles/ops-scout/
├── profiles/ops-autonomous-drive/
├── profiles/ops-relic-lite/
└── skills/community/living-ops/ # only if --install-skills is passed
```

The installer backs up overwritten files under `~/.hermes/backups/hermes-living-ops-pack-*` when `--apply` is used.

## Cheap preflight policy

For non-trivial questions, an agent should check the local Living Library before answering:

```bash
python3 ~/.hermes/libraries/living-ops/scripts/library_preflight.py "<query>" --limit 8
```

If relevant runbooks, decisions, failures, concepts, agents, or memory pages appear, read those first. Do **not** load the whole vault into context.

## Validation

Run the release-safe checks:

```bash
python3 scripts/release_check.py
```

Or run checks individually:

```bash
python3 scripts/sanitize_check.py .
python3 scripts/lint_library.py library-template
python3 scripts/library_preflight.py "how should the librarian promote failures" --root library-template --limit 5
./install.sh --dry-run
pytest -q tests
```

Before publishing your fork, add your own denylist terms:

```bash
python3 scripts/release_check.py --deny "YOUR_NAME" --deny "YOUR_SERVER" --deny "YOUR_PRIVATE_PROJECT"
```

## Privacy stance

This pack is intentionally generic. The sanitizer checks for common leaks:

- real home paths;
- private IPs;
- common token formats;
- secret assignments;
- SSH/private keys;
- accidentally tracked `.env`, database, dump, log, backup, or key files;
- personal denylist terms passed by the operator.

No scanner can prove privacy. Treat the sanitizer as a guardrail, not a guarantee.

## Sync and Obsidian

See `sync-guides/` for:

- Obsidian setup;
- Syncthing on Windows, macOS, and Linux;
- Möbius Sync on iPhone;
- Syncthing-Fork on Android.

Recommended model:

```text
canonical Library -> generated/synced mirror -> Obsidian on devices
```

Users write into `_INBOX_USER/`; agents promote safely into canon.

## Public-release checklist

See `docs/public-release-checklist.md`.

## License

MIT. See `LICENSE`.
