# Onboarding

The onboarding step adapts the template to the operator without publishing or uploading private data.

## Recommended order

```bash
./install.sh --apply --target ~/.hermes --library-name adaptative-living-library --install-skills
python3 scripts/onboard.py --target ~/.hermes --library-name adaptative-living-library --scan-existing
python3 scripts/onboard.py --apply --target ~/.hermes --library-name adaptative-living-library --scan-existing
```

## Model selection

Onboarding asks for or accepts model strings for:

- `librarian`
- `scout`
- `architect`
- `oracle`

It writes those into copied profile configs. It does not edit global `config.yaml` and does not restart Hermes.

## Scout topics

Pass topics with repeated `--topic` flags:

```bash
python3 scripts/onboard.py --apply --topic "local-first smart home" --topic "AI video workflows"
```

The topics become Scout mission seed material in:

```text
<library>/onboarding/adaptative-config.yaml
<library>/raw/onboarding/initial-discovery-*.md
```

## Session and memory analysis

Use `--scan-existing` to scan common local Hermes paths, or pass exact paths:

```bash
python3 scripts/onboard.py --apply \
  --session-source ~/.hermes/sessions \
  --memory-source ~/.hermes/mnemosyne \
  --memory-source ~/.hermes/libraries
```

The scan is deterministic/read-only. It extracts topic candidates and small excerpts into raw onboarding notes. Treat this as source material: Librarian should curate it later before it becomes canon.

## Obsidian vault link

```bash
python3 scripts/onboard.py --apply --obsidian-vault ~/Documents/Obsidian/MyVault
```

Default behavior:

- create a symlink: `MyVault/Adaptative Living Library -> ~/.hermes/libraries/adaptative-living-library`;
- if symlink fails, write a manual linking note in the vault;
- never delete existing vault content.

## Binding profiles to channels

Onboarding writes:

```text
<library>/onboarding/profile-bindings.yaml
<library>/onboarding/BINDING_GUIDE.md
```

These files describe the four profile names and placeholders for Telegram/Discord binding. Actual channel binding still requires operator approval because it edits live Hermes config and may require a gateway restart.
