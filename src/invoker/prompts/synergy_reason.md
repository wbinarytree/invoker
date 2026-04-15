<!-- prompt_version: 1 -->
You are writing a one-sentence justification for a hero synergy in Dota 2.

## Rules
1. The justification MUST reference at least one functional tag from hero A or hero B.
2. Stay under 25 words.
3. Speak in mechanics, not flavor. No "they're both strong" or hype.

## Output
Return a single JSON object:

```json
{"reason": "..."}
```

## Input

Hero A: {HERO_A_NAME}
Hero A tags: {HERO_A_TAGS}
Hero B: {HERO_B_NAME}
Hero B tags: {HERO_B_TAGS}
Observed synergy: {SCORE} over {GAMES} games.
