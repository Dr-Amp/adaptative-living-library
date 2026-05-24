#!/usr/bin/env python3
"""Publish-safety scanner for this template repo.

It intentionally catches common leaks but cannot prove privacy. Operators should
add their own denylist terms before publishing.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

DEFAULT_SKIP_DIRS = {'.git', '__pycache__', '.pytest_cache', 'node_modules', '.venv', 'venv'}
DEFAULT_SKIP_SUFFIXES = {'.png', '.jpg', '.jpeg', '.webp', '.gif', '.pdf', '.zip', '.tar', '.gz'}

PATTERNS = [
    ('private_key', re.compile(r'-----BEGIN (?:RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----')),
    ('secret_assignment', re.compile(r'(?i)\b(?:api[_-]?key|token|secret|password)\s*[:=]\s*["\']?(?!<|CHANGE_ME|REPLACE_ME|your_|__)[A-Za-z0-9_./+=-]{16,}')),
    ('absolute_home_path', re.compile(r'/(?:home|Users)/[A-Za-z0-9._-]+/(?!\.hermes/libraries/__LIBRARY_NAME__)')),
    ('windows_user_path', re.compile(r'[A-Za-z]:\\Users\\(?!<you>|USER|__OPERATOR_NAME__)[A-Za-z0-9._-]+\\')),
    ('private_ipv4', re.compile(r'\b(?:10\.\d{1,3}\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[0-1])\.\d{1,3}\.\d{1,3}|100\.(?:6[4-9]|[7-9]\d|1[01]\d|12[0-7])\.\d{1,3}\.\d{1,3})\b')),
]


def iter_files(root: Path):
    for p in root.rglob('*'):
        if p.is_dir():
            continue
        if any(part in DEFAULT_SKIP_DIRS for part in p.parts):
            continue
        if p.suffix in DEFAULT_SKIP_SUFFIXES:
            continue
        yield p


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('path', nargs='?', default='.')
    ap.add_argument('--deny', action='append', default=[], help='additional literal term that must not appear')
    args = ap.parse_args()
    root = Path(args.path).resolve()
    findings = []
    for path in iter_files(root):
        try:
            text = path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            continue
        rel = path.relative_to(root)
        for name, rx in PATTERNS:
            for m in rx.finditer(text):
                findings.append((str(rel), name, m.group(0)[:120]))
        for term in args.deny:
            if term and term in text:
                findings.append((str(rel), f'deny:{term}', term))
    if findings:
        print('SANITIZE CHECK FAILED')
        for file, name, sample in findings[:200]:
            print(f'- {file}: {name}: {sample}')
        if len(findings) > 200:
            print(f'... {len(findings)-200} more')
        return 1
    print('sanitize_check: OK')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
