<!-- prompt_version: 1 -->
You are writing a one-sentence justification for a hero counter in Dota 2.

## Rules
1. The justification MUST reference at least one functional tag from hero A or hero B.
2. Stay under 25 words.
3. Speak in mechanics, not flavor.

## Output
Return a single JSON object:

```json
{"reason": "..."}
```

## Input

Hero being countered: {HERO_A_NAME}
Hero A tags: {HERO_A_TAGS}
Counter: {HERO_B_NAME}
Hero B tags: {HERO_B_TAGS}
Observed disadvantage: {SCORE} over {GAMES} games.
