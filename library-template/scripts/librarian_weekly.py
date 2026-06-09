#!/usr/bin/env python3
"""BMO Librarian — Weekly autonomous curation pass.

Safe scope: only writes inside Living Ops Library.
Never touches Obsidian, FRAME, config, crons, gateway, models, services.

Run this weekly (e.g. every Sunday) to:
1. Lint the library
2. Rebuild Knowledge Map
3. Detect contradictions
4. Find expired claims
5. Find unabsorbed outputs
6. Git commit changes
7. Report to stdout (for cron delivery)
"""
from __future__ import annotations
import json, re
from pathlib import Path
from datetime import date, timedelta
from collections import Counter
import subprocess, sys
import yaml

ROOT = Path('~/.hermes/libraries/<your-library>')
SCRIPTS = ROOT / 'scripts'
TODAY = date.today()

def run(cmd: list[str], **kwargs) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True, cwd=str(ROOT), **kwargs)

def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(errors='ignore')
    if text.startswith('---\n'):
        end = text.find('\n---\n', 4)
        if end != -1:
            try:
                return yaml.safe_load(text[4:end]) or {}
            except:
                return {}
    return {}

def main():
    report = []
    changes = False
    
    # 1. Lint
    print("1/6 Running editorial lint...")
    result = run(['python3', str(SCRIPTS / 'lint_editorial_karpathy.py')])
    lint = json.loads(result.stdout) if result.stdout else {}
    
    missing_fm = len(lint.get('missing_frontmatter_or_fields', []))
    missing_cs = len(lint.get('outputs_missing_canonical_fields', []))
    broken = len(lint.get('broken_links', []))
    
    report.append(f"Lint: {lint.get('pages_checked', '?')} pages checked")
    if missing_fm: report.append(f"⚠ {missing_fm} missing frontmatter fields")
    if missing_cs: report.append(f"⚠ {missing_cs} outputs missing canonical_status")
    if broken: report.append(f"⚠ {broken} broken wiki links")
    if not (missing_fm or missing_cs):
        report.append("✓ Frontmatter + canonical: clean")
    
    # 2. Rebuild Knowledge Map
    print("2/6 Rebuilding Knowledge Map...")
    run(['python3', str(SCRIPTS / 'build_knowledge_map.py')])
    report.append("✓ Knowledge Map rebuilt")
    changes = True
    
    # 3. Detect contradictions
    print("3/6 Detecting contradictions...")
    result = run(['python3', str(SCRIPTS / 'detect_contradictions.py')])
    if result.stdout.strip():
        try:
            candidates = json.loads(result.stdout.split('--- JSON ---')[1]) if '--- JSON ---' in result.stdout else []
        except:
            candidates = []
        if candidates:
            report.append(f"⚠ {len(candidates)} potential contradiction(s) detected")
        else:
            report.append("✓ No contradictions detected")
    
    # 4. Find expired claims
    print("4/6 Checking expired claims...")
    expired = []
    claims_dir = ROOT / 'wiki' / 'Claims'
    for fpath in claims_dir.rglob('*.md'):
        if fpath.name == 'Index.md':
            continue
        fm = parse_frontmatter(fpath)
        text = fpath.read_text(errors='ignore')
        # Find claim blocks with expires dates
        for match in re.finditer(r'\*\*Expires:\*\*\s*(\d{4}-\d{2}-\d{2})', text):
            exp_date = date.fromisoformat(match.group(1))
            if exp_date <= TODAY:
                expired.append(f"{fpath.name}: claim expired {exp_date}")
    if expired:
        report.append(f"⚠ {len(expired)} expired claim(s):")
        for e in expired:
            report.append(f"  - {e}")
    else:
        report.append("✓ No expired claims")
    
    # 5. Find unabsorbed old outputs (>14 days)
    print("5/6 Checking unabsorbed outputs...")
    outputs_dir = ROOT / 'wiki' / 'Outputs'
    old_unabsorbed = []
    cutoff = TODAY - timedelta(days=14)
    for fpath in sorted(outputs_dir.rglob('*.md')):
        fm = parse_frontmatter(fpath)
        if fm.get('type') != 'output':
            continue
        cs = fm.get('canonical_status', '')
        if cs in ('absorbed', 'superseded', 'ledger'):
            continue
        created_str = fm.get('created', '')
        if not created_str:
            continue
        try:
            created = date.fromisoformat(str(created_str).split('T')[0])
        except:
            continue
        if created <= cutoff:
            old_unabsorbed.append(fpath.name)
    
    if old_unabsorbed:
        report.append(f"⚠ {len(old_unabsorbed)} unabsorbed outputs >14 days old")
    else:
        report.append("✓ No unabsorbed outputs >14 days")
    
    # 6. Git commit
    print("6/6 Git commit...")
    git_dir = ROOT / '.git'
    if git_dir.exists():
        run(['git', 'add', '-A'])
        status = run(['git', 'status', '--porcelain'])
        if status.stdout.strip():
            run(['git', 'commit', '-m', f'chore: weekly librarian pass {TODAY.isoformat()}'])
            report.append(f"✓ Git committed changes ({len(status.stdout.strip().splitlines())} files)")
        else:
            report.append("✓ Git: no changes to commit")
    
    # Print report
    print("\n" + "="*50)
    print(f"BMO Librarian — Weekly Pass {TODAY.isoformat()}")
    print("="*50)
    for line in report:
        print(line)
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
