#!/usr/bin/env python3
"""Run the publish-safety release checks for Hermes Living Ops Pack."""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(cmd: list[str], *, cwd: Path = ROOT) -> None:
    print('+ ' + ' '.join(cmd))
    subprocess.run(cmd, cwd=str(cwd), check=True)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--deny', action='append', default=[], help='extra literal term that must not appear')
    args = ap.parse_args()

    deny_args: list[str] = []
    for term in args.deny:
        deny_args.extend(['--deny', term])

    run([sys.executable, 'scripts/sanitize_check.py', '.', *deny_args])
    run([sys.executable, 'scripts/lint_library.py', 'library-template'])
    run([sys.executable, 'scripts/library_preflight.py', 'librarian failures', '--root', 'library-template', '--limit', '5'])
    run(['bash', 'install.sh', '--dry-run'])

    tmp_root = Path(tempfile.mkdtemp(prefix='living-ops-pack-'))
    try:
        run(['bash', 'install.sh', '--apply', '--target', str(tmp_root), '--library-name', 'living-ops-test', '--install-skills'])
        installed = tmp_root / 'libraries' / 'living-ops-test'
        run([sys.executable, str(installed / 'scripts' / 'lint_library.py'), str(installed)])
        run([sys.executable, str(installed / 'scripts' / 'library_preflight.py'), 'librarian failures', '--root', str(installed), '--limit', '5'])
        run([sys.executable, str(installed / 'scripts' / 'sanitize_check.py'), str(installed), *deny_args])
    finally:
        shutil.rmtree(tmp_root, ignore_errors=True)

    run([sys.executable, '-m', 'pytest', '-q', 'tests'])
    print('release_check: OK')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
