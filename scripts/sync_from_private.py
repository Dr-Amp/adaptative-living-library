#!/usr/bin/env python3
"""Private → public bridge for the Adaptative Living Library pack.

The production Living Library evolves with private data; this repo must only
receive *class-level* knowledge. This script automates the bridge safely:

1. Scans the private library (``--private-root``) for structural deltas since
   the last sync: new/changed scripts, new Runbooks, new wiki sections.
2. NEVER copies private content. It emits a sanitized delta report
   (``docs/private-sync-status.md``) listing only file *names* and *classes*
   of change, so an operator (or agent session) knows what deserves a
   generalized port.
3. Keeps state in ``.private-sync-state.json`` (content hashes) so each run
   reports only new deltas.
4. Refuses to write the report if it would trip ``sanitize_check.py``.

Porting itself stays a deliberate, human/agent-reviewed act: generalization
is semantic (names, paths, examples must become fictional). The bridge makes
the divergence *visible and cheap to act on*, which is the part that was
missing (see private handoff 2026-06-10, open question #6).
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

PACK_ROOT = Path(__file__).resolve().parents[1]
STATE_PATH = PACK_ROOT / '.private-sync-state.json'
REPORT_PATH = PACK_ROOT / 'docs' / 'private-sync-status.md'

# Only these classes of private paths are even *named* in the public report.
TRACKED = [
    ('scripts', 'scripts/*.py'),
    ('runbooks', 'wiki/Runbooks/*.md'),
    ('concepts', 'wiki/Concepts/*.md'),
    ('indexes', 'wiki/Indexes/*.md'),
]

# Names matching the operator's denylist are private/domain-specific and are
# reported only as an anonymous count, never by name. The denylist itself is
# private: it lives in `.private-sync-denylist.txt` (gitignored), one term per
# line. Without it, EVERY file is treated as private — safe by default.
DENYLIST_PATH = PACK_ROOT / '.private-sync-denylist.txt'


def load_private_name_re() -> re.Pattern | None:
    if not DENYLIST_PATH.exists():
        return None
    terms = [re.escape(t.strip()) for t in DENYLIST_PATH.read_text().splitlines()
             if t.strip() and not t.startswith('#')]
    return re.compile('(?i)(' + '|'.join(terms) + ')') if terms else None


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def scan(private_root: Path) -> dict:
    snapshot: dict[str, dict[str, str]] = {}
    for cls, pattern in TRACKED:
        snapshot[cls] = {}
        for p in sorted(private_root.glob(pattern)):
            if p.name.endswith(('.bak', '.pyc')) or '.bak-' in p.name:
                continue
            snapshot[cls][p.name] = sha(p)
    return snapshot


def template_names() -> dict[str, set[str]]:
    t = PACK_ROOT / 'library-template'
    return {
        'scripts': {p.name for p in (t / 'scripts').glob('*.py')},
        'runbooks': {p.name for p in (t / 'wiki' / 'Runbooks').glob('*.md')},
        'concepts': {p.name for p in (t / 'wiki' / 'Concepts').glob('*.md')},
        'indexes': set(),
    }


def public_label(cls: str, name: str, counters: dict, private_re: re.Pattern | None) -> str | None:
    """Return a publishable label for a private filename, or None to count anonymously."""
    if private_re is None or private_re.search(name):
        counters[cls] = counters.get(cls, 0) + 1
        return None
    return name


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--private-root', required=True)
    ap.add_argument('--write', action='store_true', help='write report + state (default: dry-run to stdout)')
    args = ap.parse_args()
    private_root = Path(args.private_root).expanduser()
    if not (private_root / 'wiki').is_dir():
        print(f'error: {private_root} does not look like a Living Library (no wiki/)', file=sys.stderr)
        return 2

    prev = json.loads(STATE_PATH.read_text()) if STATE_PATH.exists() else {'snapshot': {}}
    snap = scan(private_root)
    tnames = template_names()

    private_re = load_private_name_re()
    if private_re is None:
        print('note: no .private-sync-denylist.txt — ALL files reported anonymously (safe default)', file=sys.stderr)

    counters: dict[str, int] = {}
    new, changed, unported = [], [], []
    for cls, files in snap.items():
        before = prev['snapshot'].get(cls, {})
        for name, digest in files.items():
            label = public_label(cls, name, counters, private_re)
            if name not in before:
                if label:
                    new.append(f'{cls}/{label}')
            elif before[name] != digest:
                if label:
                    changed.append(f'{cls}/{label}')
            if label and cls in ('scripts', 'runbooks') and name not in tnames.get(cls, set()):
                unported.append(f'{cls}/{label}')

    now = dt.datetime.now().strftime('%Y-%m-%d %H:%M')
    lines = [
        '# Private → public sync status',
        '',
        f'Last bridge run: {now}. This report names only generic, class-level files;',
        'domain/private items appear as anonymous counts. Porting is deliberate:',
        'generalize names/paths/examples, then run `python3 scripts/release_check.py`.',
        '',
        f'- New since last run: {", ".join(sorted(new)) or "none"}',
        f'- Changed since last run: {", ".join(sorted(changed)) or "none"}',
        f'- Generic items with no template counterpart yet: {", ".join(sorted(set(unported))) or "none"}',
        f'- Private/domain-specific items (not named here): ' + (
            ", ".join(f"{k}: {v}" for k, v in sorted(counters.items())) or "0"),
        '',
    ]
    report = '\n'.join(lines)
    print(report)

    if args.write:
        REPORT_PATH.write_text(report)
        # publish gate: the report itself must be clean
        proc = subprocess.run(
            [sys.executable, str(PACK_ROOT / 'scripts' / 'sanitize_check.py'), str(REPORT_PATH)],
            capture_output=True, text=True,
        )
        if proc.returncode != 0:
            REPORT_PATH.unlink(missing_ok=True)
            print('sanitize_check rejected the report; nothing written:', file=sys.stderr)
            print(proc.stdout + proc.stderr, file=sys.stderr)
            return 1
        STATE_PATH.write_text(json.dumps({'snapshot': snap, 'last_run': now}, indent=1))
        print(f'wrote {REPORT_PATH.relative_to(PACK_ROOT)} and updated sync state')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
