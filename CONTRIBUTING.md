# Contributing

Thanks for improving Hermes Living Ops Pack. Keep the project boring, safe, and publishable.

## Rules

- Do not add private user data, memory exports, chat logs, server names, IPs, or credentials.
- Keep examples fictional and generic.
- Installer changes must remain dry-run by default or require explicit `--apply`.
- Do not add automatic crons, service restarts, model/provider changes, or active memory writes.
- Prefer small, reviewable changes.

## Before opening a PR

```bash
python3 scripts/release_check.py
```

If you are publishing from a real private environment, pass denylist terms too:

```bash
python3 scripts/release_check.py --deny "YOUR_NAME" --deny "YOUR_SERVER"
```

## Good contributions

- Better public-safe templates.
- Stronger sanitizer patterns.
- Better lint/preflight behavior without adding heavy dependencies.
- Clearer Obsidian/Syncthing/mobile setup guides.
- More tests for installer safety.

## Avoid

- Real personal examples.
- Opinionated production automation.
- Hidden side effects in install scripts.
- Vendor lock-in unless clearly optional.
