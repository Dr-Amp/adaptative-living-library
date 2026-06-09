#!/usr/bin/env python3
from __future__ import annotations
import json, re
from collections import Counter
from pathlib import Path
import yaml
ROOT=Path('~/.hermes/libraries/<your-library>')
WIKI=ROOT/'wiki'
REQUIRED=('title','created','updated','type','status','area','subarea','tags','related','confidence','knowledge_layer')
LINK_RE=re.compile(r'\[\[([^\]|#]+)')
def split(text):
    if text.startswith('---\n'):
        end=text.find('\n---\n',4)
        if end!=-1:
            try: return yaml.safe_load(text[4:end]) or {}, text[end+5:]
            except Exception as e: return {'_yaml_error':str(e)}, text[end+5:]
    return {}, text
def include(p):
    rel=p.relative_to(ROOT).parts
    if 'raw' in rel or '_INBOX_USER' in rel: return False
    if rel[0]=='wiki':
        if len(rel)>=4 and rel[1:4]==('Inbox','user','proposed-edits'): return False
        return True
    if rel[0]=='runbooks': return True
    if rel[0] in ('MAPA HUMANO.md','EMPIEZA AQUI - GUIA HUMANA.md'): return True
    return False
pages=[]
existing=set()
for p in ROOT.rglob('*.md'):
    if 'raw' in p.relative_to(ROOT).parts: continue
    relp=p.relative_to(ROOT).with_suffix('').as_posix()
    existing.add(relp)
    existing.add(p.stem)
    if p.is_relative_to(WIKI):
        existing.add(p.relative_to(WIKI).with_suffix('').as_posix())
for p in sorted(ROOT.rglob('*.md')):
    if not include(p): continue
    meta,body=split(p.read_text(errors='ignore'))
    rel=p.relative_to(ROOT).as_posix()
    pages.append((p,rel,meta,body))
missing=[]; output_missing=[]; broken=[]; no_nav=[]; low=[]; long=[]; layers=Counter(); areas=Counter(); subareas=Counter(); canonical=Counter()
for p,rel,m,b in pages:
    if not m:
        missing.append(rel); continue
    miss=[k for k in REQUIRED if k not in m]
    if miss: missing.append(f"{rel}: {','.join(miss)}")
    if m.get('type')=='output':
        cs = m.get('canonical_status')
        if cs is None:
            output_missing.append(f"{rel}: canonical_status")
        elif cs == 'absorbed' and 'absorbed_by' not in m:
            output_missing.append(f"{rel}: absorbed_by")
        canonical[str(cs or 'missing')]+=1
    if m.get('confidence') in ('low','medium'): low.append(rel)
    if m.get('knowledge_layer')!='inbox-evidence' and '## Navegación humana' not in b and not rel.startswith('wiki/Logs/'):
        no_nav.append(rel)
    if len(b.splitlines())>220 and m.get('type') not in ('index','log'):
        long.append(rel)
    layers[str(m.get('knowledge_layer','missing'))]+=1; areas[str(m.get('area','missing'))]+=1; subareas[str(m.get('subarea','missing'))]+=1
    for link in LINK_RE.findall(b):
        target=link.strip().split('|',1)[0].split('#',1)[0]
        if target and target not in existing and target.split('/')[-1] not in existing and not target.startswith('http'):
            # Ignore explicit placeholder examples in SCHEMA-like files outside wiki.
            if target in ('Mapas/...','Areas/...','Runbooks/...','_INBOX_USER'): continue
            broken.append((rel,target))
report={
 'ok': not (missing or output_missing or broken or no_nav),
 'pages_checked': len(pages),
 'missing_frontmatter_or_fields': missing[:200],
 'outputs_missing_canonical_fields': output_missing[:200],
 'broken_links': broken[:200],
 'pages_without_nav': no_nav[:200],
 'medium_or_low_confidence_count': len(low),
 'long_pages_over_220_lines': long[:100],
 'knowledge_layers': layers,
 'areas': areas,
 'subareas': subareas,
 'canonical_status': canonical,
}
print(json.dumps(report,ensure_ascii=False,indent=2,default=dict))
raise SystemExit(0 if report['ok'] else 1)
