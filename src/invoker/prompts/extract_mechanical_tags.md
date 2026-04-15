<!-- prompt_version: 1 -->
You are extracting structured functional tags for a Dota 2 hero from a fixed taxonomy.

## Rules
1. Pick tags ONLY from the taxonomy below. Never invent a tag.
2. Each tag you pick must be justified by quoted ability text.
3. If no ability text justifies a tag, do not pick it — even if it feels right.
4. Liquipedia's curated role labels are prior evidence. Use them as hints, but final tags must still be justified by ability text.

## Output
Return a single JSON object:

```json
{
  "functional_tags": ["tag_a", "tag_b"],
  "tag_sources": [
    {"tag": "tag_a", "ability": "Ability Name", "evidence": "quoted text from the ability"}
  ]
}
```

## Taxonomy

{TAXONOMY}

## Hero

Name: {HERO_NAME}
Liquipedia roles: {LIQUIPEDIA_ROLES}

## Abilities

{ABILITIES}
