#!/usr/bin/env python3
"""Minimal lint for a Living Ops markdown library."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

try:
    import yaml
except Exception as exc:  # pragma: no cover
    raise SystemExit('PyYAML is required') from exc

REQUIRED = {'title', 'type', 'status', 'area', 'tags', 'confidence'}
SKIP_DIRS = {'raw'}


def split_fm(text: str):
    if text.startswith('---\n'):
        end = text.find('\n---\n', 4)
        if end >= 0:
            return yaml.safe_load(text[4:end]) or {}, text[end+5:]
    return {}, text


def page_slug(path: Path, root: Path):
    rel = path.relative_to(root).with_suffix('').as_posix()
    if rel.startswith('wiki/'):
        rel = rel[5:]
    return rel


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('root', nargs='?', default='library-template')
    args = ap.parse_args()
    root = Path(args.root).resolve()
    md = [p for p in root.rglob('*.md') if not any(part in SKIP_DIRS for part in p.parts)]
    slugs = {page_slug(p, root) for p in md}
    slugs.update({Path(s).name for s in slugs})
    missing = []
    broken = []
    for p in md:
        text = p.read_text(encoding='utf-8')
        meta, body = split_fm(text)
        rel = p.relative_to(root).as_posix()
        if rel.startswith('wiki/') and p.name != 'README.md':
            miss = sorted(REQUIRED - set(meta))
            if miss:
                missing.append((rel, miss))
        for link in re.findall(r'\[\[([^\]|#]+)', text):
            target = link.strip().strip('/')
            if target and target not in slugs and Path(target).name not in slugs:
                broken.append((rel, target))
    ok = not missing and not broken
    print({'ok': ok, 'markdown_files': len(md), 'missing_frontmatter': missing, 'broken_links': broken})
    return 0 if ok else 1

if __name__ == '__main__':
    raise SystemExit(main())
