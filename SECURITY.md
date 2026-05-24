# Security Policy

This repository is designed to be publish-safe, but it cannot guarantee that a fork or derived pack is free of private data.

## Supported versions

`v0.1.x` receives best-effort safety fixes.

## Reporting a vulnerability

If you find a leak pattern, unsafe installer behavior, or a sanitization bypass, open a private security advisory or issue in the upstream repository. Do not paste real secrets into issues.

## Installer guarantees

The default installer behavior must remain:

- dry-run unless `--apply` is explicit;
- no cron creation;
- no gateway restart;
- no model/provider changes;
- no active memory writes;
- backup overwritten files when applying.

## Secret handling

Never commit real `.env`, logs, databases, dumps, private keys, access tokens, chat exports, or memory-store exports. Use placeholders such as `CHANGE_ME` or `__HERMES_HOME__`.
