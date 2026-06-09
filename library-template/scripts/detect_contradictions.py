#!/usr/bin/env python3
"""Detect potential contradictions between claims in the Living Library.

Compares claims within the same area for semantic overlap and flags pairs
with similar topics but divergent confidence or contradictory statements.

Output: JSON list of candidate contradictions for human/Librero review.
"""
from __future__ import annotations
import json, re
from pathlib import Path
from collections import defaultdict
import yaml

ROOT = Path('~/.hermes/libraries/<your-library>')
CLAIMS_DIR = ROOT / 'wiki' / 'Claims'

def parse_frontmatter(text: str) -> dict:
    if text.startswith('---\n'):
        end = text.find('\n---\n', 4)
        if end != -1:
            try:
                return yaml.safe_load(text[4:end]) or {}
            except:
                return {}
    return {}

def extract_claims(filepath: Path) -> list[dict]:
    """Extract individual claims from a claims page."""
    text = filepath.read_text(errors='ignore')
    claims = []
    
    # Find claim blocks: ## XX: Title followed by **Claim:** text
    pattern = re.compile(r'## (\w+): (.+?)\n\*\*Claim:\*\*\s*(.+?)(?=\n\*\*|$)', re.DOTALL)
    for match in pattern.finditer(text):
        claim_id = match.group(1)
        title = match.group(2).strip()
        statement = match.group(3).strip()
        
        # Extract confidence
        conf_match = re.search(r'\*\*Confidence:\*\*\s*`(\w+)`', statement)
        confidence = conf_match.group(1) if conf_match else 'unknown'
        
        claims.append({
            'id': claim_id,
            'title': title,
            'statement': statement,
            'confidence': confidence,
            'source_file': str(filepath.relative_to(ROOT)),
        })
    
    return claims

def simple_similarity(a: str, b: str) -> float:
    """Very simple word overlap similarity."""
    words_a = set(a.lower().split())
    words_b = set(b.lower().split())
    if not words_a or not words_b:
        return 0.0
    intersection = words_a & words_b
    return len(intersection) / min(len(words_a), len(words_b))

def main():
    all_claims = []
    for fpath in sorted(CLAIMS_DIR.rglob('*.md')):
        if fpath.name == 'Index.md':
            continue
        fm = parse_frontmatter(fpath.read_text(errors='ignore'))
        area = fm.get('area', 'unknown')
        claims = extract_claims(fpath)
        for c in claims:
            c['area'] = area
        all_claims.extend(claims)
    
    print(f"Loaded {len(all_claims)} claims from {CLAIMS_DIR}")
    
    # Find potential contradictions within same area
    candidates = []
    for i, ca in enumerate(all_claims):
        for cb in all_claims[i+1:]:
            if ca['area'] != cb['area']:
                continue
            sim = simple_similarity(ca['statement'], cb['statement'])
            if sim > 0.3:  # Word overlap threshold
                # Flag if confidences diverge significantly
                confs = {'high': 3, 'medium': 2, 'low': 1, 'unknown': 0}
                conf_diff = abs(confs.get(ca['confidence'], 0) - confs.get(cb['confidence'], 0))
                if conf_diff >= 2:
                    candidates.append({
                        'claim_a': ca['id'],
                        'claim_a_file': ca['source_file'],
                        'claim_b': cb['id'],
                        'claim_b_file': cb['source_file'],
                        'area': ca['area'],
                        'similarity': round(sim, 2),
                        'confidence_divergence': conf_diff,
                    })
    
    print(f"Found {len(candidates)} candidate contradiction(s)")
    if candidates:
        for c in candidates:
            print(f"  [{c['area']}] {c['claim_a']} ↔ {c['claim_b']} (sim={c['similarity']}, conf_diff={c['confidence_divergence']})")
    
    return candidates

if __name__ == '__main__':
    results = main()
    # Also output JSON for scripting
    print("\n--- JSON ---")
    print(json.dumps(results, indent=2, ensure_ascii=False))
