#!/usr/bin/env python3
"""Cheap deterministic preflight for a Living Ops Library."""
from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path

try:
    import yaml
except Exception as exc:
    raise SystemExit('PyYAML is required') from exc

STOP = set('the a an and or of in to for with without about how what why when where this that these those is are be i you me my our your from on into de la el los las y o que para con sin como'.split())
BOOST = {'failure': 8, 'decision': 7, 'runbook': 7, 'concept': 5, 'agent': 5, 'memory': 4, 'area': 4, 'index': 2, 'map': 2, 'output': 1}


def tokens(s: str):
    return [w for w in re.findall(r'[a-z0-9][a-z0-9_-]{2,}', s.lower()) if w not in STOP]


def split_fm(text: str):
    if text.startswith('---\n'):
        end = text.find('\n---\n', 4)
        if end >= 0:
            try:
                return yaml.safe_load(text[4:end]) or {}, text[end+5:]
            except Exception:
                return {}, text[end+5:]
    return {}, text


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('query', nargs='+')
    ap.add_argument('--root', default=str(Path.home() / '.hermes' / 'libraries' / 'adaptative-living-library'))
    ap.add_argument('--limit', type=int, default=8)
    args = ap.parse_args()
    root = Path(args.root).expanduser().resolve()
    q = tokens(' '.join(args.query))
    rows = []
    for p in root.rglob('*.md'):
        rel = p.relative_to(root).as_posix()
        if '/raw/' in f'/{rel}/' or rel.startswith('raw/') or '_INBOX' in rel:
            continue
        text = p.read_text(encoding='utf-8', errors='ignore')
        meta, body = split_fm(text)
        headings = ' '.join(re.findall(r'(?m)^#{1,3}\s+(.+)$', body[:12000]))
        rank_text = ' '.join([
            rel, str(meta.get('title','')), str(meta.get('type','')), str(meta.get('area','')),
            str(meta.get('subarea','')), ' '.join(map(str, meta.get('tags') or [])), headings
        ])
        c = Counter(tokens(rank_text))
        score = 0
        for t in q:
            score += min(c.get(t, 0), 4) * 3
            for tok, count in c.items():
                if len(t) >= 5 and len(tok) >= 5 and (tok.startswith(t) or t.startswith(tok)) and tok != t:
                    score += min(count, 2)
        if score:
            ptype = str(meta.get('type',''))
            score += BOOST.get(ptype, 0)
            if meta.get('confidence') == 'high':
                score += 1
            rows.append((score, ptype, rel, meta.get('title', p.stem)))
    rows.sort(key=lambda r: (-r[0], r[2]))
    print(f'Adaptative Living Library preflight: {len(rows)} matches / root={root}')
    for score, ptype, rel, title in rows[:args.limit]:
        print(f'- {score:>3} · {ptype or "?"} · {rel} · {title}')
    if not rows:
        print('- No obvious Library match.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
