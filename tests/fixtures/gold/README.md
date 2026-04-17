# Gold Set

Each file is a hand-labeled expected mechanical extraction for one hero.
Used as a regression harness for prompt changes.

## Fields
- `hero_id`: int
- `hero_name`: display name
- `expected_tags`: tags the extractor MUST produce (missing any -> regression)
- `forbidden_tags`: tags the extractor MUST NOT produce (false positive -> regression)

## Adding a hero
1. Pick 1-3 heroes per archetype (carry, support, pusher, tempo mid, tank).
2. Hand-label `expected_tags` from the taxonomy.
3. Add any tags you explicitly reject under `forbidden_tags`.
4. Run `pytest tests/invoker/test_gold.py`.

## Target coverage for Phase 1
15-20 heroes across all roles.
