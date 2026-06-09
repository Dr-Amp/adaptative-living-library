#!/usr/bin/env python3
"""Auto-generate Knowledge Map from frontmatter of all wiki pages.

Reads every curated .md in wiki/, extracts frontmatter, and produces
a regenerated Knowledge Map at wiki/Knowledge Map.md that always
reflects the current state of the library.
"""
from __future__ import annotations
import json, re
from pathlib import Path
from collections import Counter, defaultdict
from datetime import date
import yaml

ROOT = Path('~/.hermes/libraries/<your-library>')
WIKI = ROOT / 'wiki'
OUTPUT = WIKI / 'Knowledge Map.md'
TODAY = date.today().isoformat()

REQUIRED = ('title','created','updated','type','status','area','subarea','tags','related','confidence','knowledge_layer')

def parse_fm(path: Path) -> dict:
    text = path.read_text(errors='ignore')
    if text.startswith('---\n'):
        end = text.find('\n---\n', 4)
        if end != -1:
            try:
                return yaml.safe_load(text[4:end]) or {}
            except:
                return {}
    return {}

def include_path(path: Path) -> bool:
    """Only include curated wiki pages, not raw/inbox/proposed-edits."""
    rel = path.relative_to(ROOT)
    parts = rel.parts
    if 'raw' in parts or '_INBOX_USER' in parts:
        return False
    if parts[0] == 'wiki':
        if len(parts) >= 4 and parts[1:4] == ('Inbox', 'user', 'proposed-edits'):
            return False
        return True
    return False

def main():
    pages = []
    for fpath in sorted(WIKI.rglob('*.md')):
        if not include_path(fpath):
            continue
        fm = parse_fm(fpath)
        if not fm:
            continue
        rel = fpath.relative_to(WIKI).as_posix()
        pages.append((rel, fm))
    
    # Aggregate stats
    types = Counter(fm.get('type','unknown') for _,fm in pages)
    areas = Counter(fm.get('area','unknown') for _,fm in pages)
    subareas = Counter(fm.get('subarea','unknown') for _,fm in pages)
    statuses = Counter(fm.get('status','unknown') for _,fm in pages)
    confidences = Counter(fm.get('confidence','unknown') for _,fm in pages)
    layers = Counter(fm.get('knowledge_layer','unknown') for _,fm in pages)
    canonical = Counter(fm.get('canonical_status','none') for _,fm in pages if fm.get('type')=='output')
    
    # Group pages by area
    by_area = defaultdict(list)
    for rel, fm in pages:
        area = fm.get('area','unknown')
        by_area[area].append((rel, fm))
    
    # Build markdown
    md = f"""---
title: Knowledge Map — Living Ops Library
aliases: [Knowledge Map, Mapa de conocimiento]
created: '2026-05-07'
updated: '{TODAY}'
type: index
status: active
area: bmo-ops
subarea: living-library-ops
knowledge_layer: human-navigation
tags: [knowledge-map, index, auto-generated]
confidence: high
---

# Knowledge Map — Living Ops Library

**Auto-generado:** {TODAY}  
**Páginas indexadas:** {len(pages)}

## Resumen

| Métrica | Valor |
|---------|-------|
| Total páginas wiki | {len(pages)} |
| Áreas activas | {len(areas)} |
| Tipos de página | {len(types)} |
| Estados | {dict(statuses)} |

## Áreas de conocimiento

"""
    
    for area in sorted(by_area.keys()):
        area_pages = by_area[area]
        md += f"### {area} ({len(area_pages)} páginas)\n\n"
        
        # Show type breakdown for this area
        area_types = Counter(fm.get('type','?') for _,fm in area_pages)
        md += f"Tipos: {', '.join(f'{t}={c}' for t,c in area_types.most_common())}\n\n"
        
        # List key pages (runbooks, decisions, failures first)
        for rel, fm in area_pages:
            typ = fm.get('type','')
            if typ in ('runbook','decision','failure','concept'):
                title = fm.get('title', rel)
                md += f"- **[{typ}]** [[{rel}]] — {title}\n"
        
        # Then areas and maps
        for rel, fm in area_pages:
            typ = fm.get('type','')
            if typ in ('area','map','index','agent'):
                title = fm.get('title', rel)
                md += f"- **[{typ}]** [[{rel}]] — {title}\n"
        
        md += "\n"
    
    # Canonical status summary
    md += f"""## Canonical Status (outputs)

| Status | Count |
|--------|-------|
"""
    for status, count in canonical.most_common():
        md += f"| {status} | {count} |\n"
    
    md += f"""
## Gaps y preguntas abiertas

Ver [[Questions/Preguntas y gaps abiertos]] para huecos investigables y deuda editorial.

## Distribución de tipos

| Tipo | Count |
|------|-------|
"""
    for typ, count in types.most_common():
        md += f"| {typ} | {count} |\n"
    
    md += """
## Navegación humana

- [[Index]]
- [[Mapas/00 - Inicio humano]]
- [[Indexes/Indice de etiquetas y relaciones]]
"""
    
    OUTPUT.write_text(md)
    print(f"✓ Knowledge Map written: {OUTPUT}")
    print(f"  {len(pages)} pages, {len(areas)} areas, {len(types)} types")

if __name__ == '__main__':
    main()
