<!-- prompt_version: 1 -->
You are writing one-sentence mechanical justifications for hero relationships in Dota 2.

## Rules
1. Each justification MUST reference at least one functional tag from Hero A or the relevant Hero B.
2. Stay under 25 words per justification.
3. Speak in mechanics only. No flavor text, no "they're both strong".
4. Return ONLY the JSON array. No extra keys, no markdown fences.

## Output format

Return a JSON array with one object per input edge, in the same order:

[
  {"hero_b_id": <int>, "reason": "<string>"},
  ...
]

## Input

Hero A: {HERO_A_NAME}
Hero A tags: {HERO_A_TAGS}

Edges:
{EDGES}
