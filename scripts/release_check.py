#!/usr/bin/env python3
"""Run the publish-safety release checks for Adaptative Living Library."""
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

    tmp_root = Path(tempfile.mkdtemp(prefix='adaptative-living-library-'))
    try:
        vault = tmp_root / 'obsidian-vault'
        vault.mkdir(parents=True, exist_ok=True)
        run(['bash', 'install.sh', '--apply', '--target', str(tmp_root), '--library-name', 'adaptative-living-library-test', '--install-skills'])
        installed = tmp_root / 'libraries' / 'adaptative-living-library-test'
        run([sys.executable, str(installed / 'scripts' / 'lint_library.py'), str(installed)])
        run([sys.executable, str(installed / 'scripts' / 'library_preflight.py'), 'librarian failures', '--root', str(installed), '--limit', '5'])
        run([sys.executable, str(installed / 'scripts' / 'sanitize_check.py'), str(installed), *deny_args])
        run([
            sys.executable, 'scripts/onboard.py', '--apply', '--target', str(tmp_root),
            '--library-name', 'adaptative-living-library-test', '--operator-name', 'Example Operator',
            '--provider', 'openrouter', '--main-model', 'anthropic/claude-sonnet-4',
            '--librarian-model', 'anthropic/claude-sonnet-4', '--scout-model', 'openai/gpt-4.1-mini',
            '--architect-model', 'anthropic/claude-sonnet-4', '--oracle-model', 'openai/gpt-4.1-mini',
            '--topic', 'AI agents', '--topic', 'creative video workflows',
            '--session-source', 'examples/sample-session.txt', '--memory-source', 'examples/sample-memory.md',
            '--obsidian-vault', str(vault), '--non-interactive'
        ])
        assert (installed / 'onboarding' / 'adaptative-config.yaml').exists()
        assert (installed / 'onboarding' / 'profile-bindings.yaml').exists()
        assert list((installed / 'raw' / 'onboarding').glob('initial-discovery-*.md'))
        for role in ['librarian', 'scout', 'architect', 'oracle']:
            assert (tmp_root / 'profiles' / role / 'config.yaml').exists()
        assert (vault / 'Adaptative Living Library').exists() or (vault / 'ADAPTATIVE_LIVING_LIBRARY_LINK.md').exists()
    finally:
        shutil.rmtree(tmp_root, ignore_errors=True)

    run([sys.executable, '-m', 'pytest', '-q', 'tests'])
    print('release_check: OK')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
