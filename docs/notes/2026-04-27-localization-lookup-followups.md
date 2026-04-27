# Localization Lookup Follow-ups

Date: 2026-04-27

Phase 5a now snapshots Valve localization KV and `GameFilesSource` uses it for
hero names, ability names, ability descriptions, and talent display templates.

Useful next improvement:

- Use Valve localization labels for `AbilityValues` headers instead of deriving
  labels from KV keys. For an ability internal name and value key, prefer:
  `DOTA_Tooltip_ability_<ability_internal_name>_<ability_value_key>`.
  Example: `pangolier_swashbuckle` + `dash_range` should resolve through
  `DOTA_Tooltip_ability_pangolier_swashbuckle_dash_range` when present.

Keep the lookup rules centralized in `GameFilesSource` so authoring context
consumers do not spread string-concat conventions across modules.
