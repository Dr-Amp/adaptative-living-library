#!/usr/bin/env python3
"""Safe installer for Hermes Living Ops Pack.

Default is dry-run. Use --apply to write files. This script does not restart
services, create crons, alter models/providers, or copy secrets.
"""
from __future__ import annotations

import argparse
import shutil
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TEXT_EXTS = {'.md', '.yaml', '.yml', '.json', '.txt', '.sh', '.ps1', '.py'}


def render_text(text: str, target: Path, library_name: str, operator_name: str) -> str:
    return (text
            .replace('__HERMES_HOME__', str(target))
            .replace('__LIBRARY_NAME__', library_name)
            .replace('__OPERATOR_NAME__', operator_name))


def copy_tree(src: Path, dst: Path, *, target: Path, library_name: str, operator_name: str, dry_run: bool, backup_root: Path):
    for item in src.rglob('*'):
        if item.is_dir():
            continue
        rel = item.relative_to(src)
        out = dst / rel
        print(f"{'DRY ' if dry_run else ''}copy {item.relative_to(ROOT)} -> {out}")
        if dry_run:
            continue
        out.parent.mkdir(parents=True, exist_ok=True)
        if out.exists():
            b = backup_root / out.relative_to(target)
            b.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(out, b)
        if item.suffix in TEXT_EXTS:
            out.write_text(render_text(item.read_text(encoding='utf-8'), target, library_name, operator_name), encoding='utf-8')
        else:
            shutil.copy2(item, out)


def main() -> int:
    ap = argparse.ArgumentParser()
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument('--dry-run', action='store_true', help='show what would be installed; default')
    mode.add_argument('--apply', action='store_true', help='write files')
    ap.add_argument('--target', default=str(Path.home() / '.hermes'))
    ap.add_argument('--library-name', default='living-ops')
    ap.add_argument('--operator-name', default='Operator')
    ap.add_argument('--install-skills', action='store_true', help='copy generic skills into target skills/community/living-ops')
    args = ap.parse_args()

    dry_run = not args.apply or args.dry_run
    target = Path(args.target).expanduser().resolve()
    ts = datetime.now().strftime('%Y%m%d-%H%M%S')
    backup_root = target / 'backups' / f'hermes-living-ops-pack-{ts}'

    print('Hermes Living Ops Pack installer')
    print(f"target: {target}")
    print(f"library: {args.library_name}")
    print(f"mode: {'dry-run' if dry_run else 'apply'}")
    print('side effects: no crons, no gateway restart, no provider/model changes')

    copy_tree(ROOT / 'library-template', target / 'libraries' / args.library_name,
              target=target, library_name=args.library_name, operator_name=args.operator_name,
              dry_run=dry_run, backup_root=backup_root)
    copy_tree(ROOT / 'profiles', target / 'profiles',
              target=target, library_name=args.library_name, operator_name=args.operator_name,
              dry_run=dry_run, backup_root=backup_root)
    if args.install_skills:
        copy_tree(ROOT / 'skills', target / 'skills' / 'community' / 'living-ops',
                  target=target, library_name=args.library_name, operator_name=args.operator_name,
                  dry_run=dry_run, backup_root=backup_root)

    if not dry_run:
        print(f"backup_root: {backup_root}")
        print('Next: run library lint and manually decide whether to add profile routing or crons.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
