# AGENTS.md — Hermes Living Ops Pack

This repository must remain publish-safe.

## Rules for coding agents

- Read `README.md`, `pack.yaml`, and this file before editing.
- Do not copy private user data from any real Hermes installation.
- Do not add real tokens, IDs, home paths, private IPs, memory exports, chat logs, or personal project names.
- Keep examples generic and fictional.
- Installer changes must default to dry-run or require `--apply`.
- Do not restart services, create crons, change providers/models, or edit a live Hermes config from tests.
- Run before reporting success:
  - `python3 scripts/sanitize_check.py .`
  - `python3 scripts/lint_library.py library-template`
  - `python3 scripts/library_preflight.py "librarian failures" --root library-template --limit 5`

## Report format

- Real tests run
- Static/dry-run checks
- Not run / risks
