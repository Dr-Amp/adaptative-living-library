#!/usr/bin/env python3
"""Publish-safety scanner for this template repo.

It catches common leaks but cannot prove privacy. Operators should add their
own denylist terms before publishing.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

DEFAULT_SKIP_DIRS = {'.git', '__pycache__', '.pytest_cache', 'node_modules', '.venv', 'venv'}
DEFAULT_SKIP_SUFFIXES = {'.png', '.jpg', '.jpeg', '.webp', '.gif', '.pdf', '.zip', '.tar', '.gz'}
DEFAULT_SKIP_FILES = {'.bmo-lab.json'}
BLOCKED_FILENAMES = {
    '.env', '.env.local', '.env.production', '.netrc', 'id_rsa', 'id_ed25519',
    'credentials.json', 'token.json', 'secrets.json', 'cookies.txt',
}
BLOCKED_SUFFIXES = {'.pem', '.p12', '.pfx', '.key', '.sqlite', '.db', '.dump', '.bak', '.backup', '.log'}

PATTERNS = [
    ('private_key', re.compile(r'-----BEGIN (?:RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----')),
    ('github_token', re.compile(r'\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9_]{20,}\b')),
    ('openai_like_key', re.compile(r'\bsk-[A-Za-z0-9_-]{20,}\b')),
    ('aws_access_key', re.compile(r'\bAKIA[0-9A-Z]{16}\b')),
    ('slack_token', re.compile(r'\bxox[baprs]-[A-Za-z0-9-]{20,}\b')),
    ('secret_assignment', re.compile(r'(?i)\b(?:api[_-]?key|access[_-]?token|auth[_-]?token|token|secret|password|passwd|pwd)\s*[:=]\s*["\']?(?!<|CHANGE_ME|REPLACE_ME|your_|__|example|placeholder|null|false|true)[A-Za-z0-9_./+=:-]{16,}')),
    ('absolute_home_path', re.compile(r'/(?:home|Users)/[A-Za-z0-9._-]+/(?!\.hermes/libraries/__LIBRARY_NAME__)')),
    ('windows_user_path', re.compile(r'[A-Za-z]:\\Users\\(?!<you>|USER|__OPERATOR_NAME__)[A-Za-z0-9._-]+\\')),
    ('private_ipv4', re.compile(r'\b(?:10\.\d{1,3}\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[0-1])\.\d{1,3}\.\d{1,3}|100\.(?:6[4-9]|[7-9]\d|1[01]\d|12[0-7])\.\d{1,3}\.\d{1,3})\b')),
]


def iter_files(root: Path):
    for p in root.rglob('*'):
        if p.is_dir():
            continue
        if p.name in DEFAULT_SKIP_FILES:
            continue
        if any(part in DEFAULT_SKIP_DIRS for part in p.parts):
            continue
        if p.suffix.lower() in DEFAULT_SKIP_SUFFIXES:
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
        rel = path.relative_to(root)
        name = path.name
        suffix = path.suffix.lower()
        if name in BLOCKED_FILENAMES or suffix in BLOCKED_SUFFIXES:
            findings.append((str(rel), 'blocked_file', name))
        try:
            text = path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            continue
        for pattern_name, rx in PATTERNS:
            for m in rx.finditer(text):
                findings.append((str(rel), pattern_name, m.group(0)[:120]))
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
