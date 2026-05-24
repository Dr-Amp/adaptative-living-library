# Public Release Checklist

Use this before publishing a fork or template derived from a private Hermes setup.

## Must pass

```bash
python3 scripts/release_check.py --deny "YOUR_NAME" --deny "YOUR_SERVER" --deny "YOUR_PRIVATE_PROJECT"
```

## Manual review

- [ ] `git status --short` is clean except intended release files.
- [ ] No real `.env`, logs, databases, dumps, keys, screenshots, or memory exports are tracked.
- [ ] README describes status and safety defaults honestly.
- [ ] Installer is dry-run by default or requires `--apply`.
- [ ] No script creates crons, restarts services, edits live config, changes models/providers, or writes active memory.
- [ ] Examples are fictional and generic.
- [ ] License and contribution policy are acceptable for public use.

## Optional GitHub publication

```bash
gh repo create hermes-living-ops-pack --public --source . --remote origin --push
gh repo edit --enable-wiki=false --enable-issues=true --add-topic hermes-agent --add-topic living-library --add-topic obsidian --add-topic knowledge-management
gh release create v0.1.0 --title "v0.1.0" --notes-file CHANGELOG.md
```

Only publish after your local denylist passes.
