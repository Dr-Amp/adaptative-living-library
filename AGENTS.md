# AGENTS.md — Adaptative Living Library

This repository must remain publish-safe. It is a template repo, not a private Hermes export.

## Rules for coding agents

- Read `README.md`, `pack.yaml`, and this file before editing.
- Do not copy private user data from any real Hermes installation.
- Do not add real tokens, IDs, home paths, private IPs, memory exports, chat logs, or personal project names.
- Keep examples generic and fictional.
- Installer changes must default to dry-run or require explicit `--apply`.
- Do not restart services, create crons, change providers/models, or edit a live Hermes config from tests.
- Do not add external network calls to tests or install scripts unless explicitly documented and optional.
- Keep scripts stdlib-first; PyYAML and pytest are acceptable validation dependencies.

## Required checks before reporting success

```bash
python3 scripts/release_check.py
```

For publication from a private environment, add denylist terms:

```bash
python3 scripts/release_check.py --deny "YOUR_NAME" --deny "YOUR_SERVER" --deny "YOUR_PRIVATE_PROJECT"
```

## Report format

- Real tests run
- Static/dry-run checks
- Not run / risks
