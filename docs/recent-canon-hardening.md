# Recent Canon Hardening

This repository is a public-safe template. It does not ship a private Living Library, but it should learn from real operating lessons as generic patterns.

## v0.3.5 hardening themes

The template now includes two reusable runbooks distilled from later production use of the pattern:

- `library-template/wiki/Runbooks/memory-boundaries.md`
  - raw capture is not memory;
  - use `raw -> summary -> candidate -> gate -> canon/discard`;
  - active memory writes remain separate and approval/policy-bound;
  - Oracle/pattern notes are advisory, never authority over canon.

- `library-template/wiki/Runbooks/serious-research-lane.md`
  - create durable research fronts with PIR, source registry, priority queue, Scout collection, and Librarian promotion;
  - keep noisy or risky operations off by default;
  - represent missing Discord/Reddit/community/official-source coverage as explicit `coverage_gap`, not invented confidence.

## What stayed private

The source production library contained many domain-specific fronts, paths, agent names, devices, locations, and personal operating details. Those were not copied. The public update only keeps the class-level architecture:

```text
source-backed collection -> local evidence -> conservative curation -> explicit approval before side effects
```

## Operator checklist

When adapting the pack to your own environment:

1. Add your own denylist before publishing a fork.
2. Keep examples fictional.
3. Start every new research lane with canon preflight.
4. Treat raw capture as evidence, not memory.
5. Run `python3 scripts/release_check.py` before sharing.
