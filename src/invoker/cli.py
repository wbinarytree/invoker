from __future__ import annotations

import json
from pathlib import Path
from typing import Annotated

import typer

from invoker import __version__
from invoker.config import Config
from invoker.kg.reader import RelationsReader
from invoker.logging import configure_logging
from invoker.paths import manifest_file, relations_file

app = typer.Typer(help="Invoker - Dota 2 knowledge framework")
HeroArgs = Annotated[
    list[str],
    typer.Argument(help="One or more hero localized names, slugs, or numeric ids."),
]
SnapshotVpkOption = Annotated[
    Path,
    typer.Option(
        "--vpk",
        help="Pre-extracted VPK root or npc directory containing npc_heroes.txt.",
    ),
]
SnapshotOutOption = Annotated[
    Path,
    typer.Option(
        "--out",
        help="Snapshot output root. The command writes <out>/<patch>/...",
    ),
]
SnapshotPatchOption = Annotated[
    str,
    typer.Option(help="Patch string for the snapshot directory."),
]
SnapshotLocalizationOption = Annotated[
    Path | None,
    typer.Option(
        "--localization",
        help="Optional KV localization file, for example dota_english.txt.",
    ),
]
SnapshotLocaleOption = Annotated[
    list[str] | None,
    typer.Option(
        "--locale",
        help="Locale name for localization/<locale>.json. Repeat for multiple locales.",
    ),
]
IdentityOutOption = Annotated[
    Path,
    typer.Option("--out", help="Output JSON artifact path."),
]
LocalizedResourceOutDirOption = Annotated[
    Path,
    typer.Option(
        "--out-dir",
        help="Output directory for compact hero, item, and ability JSON artifacts.",
    ),
]
GameResourceOutDirOption = Annotated[
    Path,
    typer.Option(
        "--out-dir",
        help="Output directory for bundled hero, item, index, and metadata JSON artifacts.",
    ),
]
PublishOutOption = Annotated[
    Path,
    typer.Option("--out", help="Release output directory."),
]
PUBLISH_OUT_DEFAULT = Path("dist")
KB_SITE_OUT_DEFAULT = Path("dist/kb-site")
KbSiteOutOption = Annotated[
    Path,
    typer.Option("--out", help="Output root; site lands in <out>/<patch>/."),
]


def _load_config() -> Config:
    cfg = Config.load()
    configure_logging(cfg.log_level)
    return cfg


@app.command()
def version() -> None:
    typer.echo(f"invoker {__version__}")


@app.command("draft-facts")
def draft_facts_cmd(
    heroes: HeroArgs,
    patch: str = typer.Option(
        "7.41b",
        help="Patch snapshot to use for game-file authoring context.",
    ),
) -> None:
    from invoker.kg.authoring import draft_facts

    cfg = _load_config()
    if cfg.game_data_dir is None:
        typer.echo("INVOKER_GAME_DATA_DIR is required for draft-facts.", err=True)
        raise typer.Exit(code=1)
    failures = 0
    for hero in heroes:
        try:
            result = draft_facts(cfg.data_dir, cfg.game_data_dir, hero, patch=patch)
        except Exception as exc:
            typer.echo(f"{hero}: {exc}", err=True)
            failures += 1
            continue
        if result.pending:
            typer.echo(f"{result.hero_slug}: prompt written: {result.prompt_path}")
            typer.echo(f"{result.hero_slug}: paste response into: {result.response_path}")
            continue
        typer.echo(f"{result.hero_slug}: wrote draft facts: {result.authored_path}")
        if result.gaps_path is not None:
            typer.echo(
                f"{result.hero_slug}: recorded {result.gap_count} vocabulary gap(s): "
                f"{result.gaps_path}"
            )
    if failures:
        raise typer.Exit(code=1)


@app.command("validate-facts")
def validate_facts_cmd(
    heroes: HeroArgs,
) -> None:
    from invoker.kg.authoring import (
        resolve_authored_file,
        validate_authored_file,
    )

    cfg = _load_config()
    failures = 0
    for hero in heroes:
        try:
            path = resolve_authored_file(cfg.data_dir, hero)
            profile = validate_authored_file(path)
        except Exception as exc:
            typer.echo(f"{hero}: {exc}", err=True)
            failures += 1
            continue
        typer.echo(f"{path}: valid ({profile.localized_name})")
    if failures:
        raise typer.Exit(code=1)


@app.command("promote-draft")
def promote_draft_cmd(
    heroes: HeroArgs,
    delete_draft: bool = typer.Option(
        False,
        "--delete-draft",
        help="Delete <hero>.draft.yaml after successful promotion.",
    ),
) -> None:
    from invoker.kg.authoring import promote_authored_draft

    cfg = _load_config()
    failures = 0
    for hero in heroes:
        try:
            result = promote_authored_draft(cfg.data_dir, hero, delete_draft=delete_draft)
        except Exception as exc:
            typer.echo(f"{hero}: {exc}", err=True)
            failures += 1
            continue
        typer.echo(
            f"{result.hero_slug}: promoted draft: {result.draft_path} -> {result.authored_path}"
        )
        if result.backup_path is not None:
            typer.echo(
                f"{result.hero_slug}: previous authored file backed up: {result.backup_path}"
            )
        if result.draft_deleted:
            typer.echo(f"{result.hero_slug}: deleted draft: {result.draft_path}")
    if failures:
        raise typer.Exit(code=1)


@app.command("show-relations")
def show_relations_cmd(
    hero: str = typer.Argument(..., help="Hero localized name, slug, or numeric id."),
) -> None:
    from invoker.kg.authoring import format_relations_for_hero

    cfg = _load_config()
    typer.echo(format_relations_for_hero(cfg.data_dir, hero))


@app.command("show-hero-context")
def show_hero_context_cmd(
    hero: str = typer.Argument(..., help="Hero localized name, slug, or numeric id."),
    patch: str = typer.Option("7.41b", help="Patch snapshot for source data."),
) -> None:
    import asyncio
    import dataclasses

    from invoker.kg.hero_context import build_hero_context

    cfg = _load_config()
    if cfg.game_data_dir is None:
        typer.echo("INVOKER_GAME_DATA_DIR is required for show-hero-context.", err=True)
        raise typer.Exit(code=1)
    packet = asyncio.run(build_hero_context(cfg.game_data_dir, hero, patch=patch))
    typer.echo(json.dumps(dataclasses.asdict(packet), indent=2))


@app.command("show-item-context")
def show_item_context_cmd(
    item: str = typer.Argument(
        ..., help="Item internal name (item_ prefix optional) or localized name."
    ),
    patch: str = typer.Option("7.41b", help="Patch snapshot for source data."),
) -> None:
    import dataclasses

    from invoker.kg.item_context import ItemNotFoundError, build_item_context

    cfg = _load_config()
    if cfg.game_data_dir is None:
        typer.echo("INVOKER_GAME_DATA_DIR is required for show-item-context.", err=True)
        raise typer.Exit(code=1)
    try:
        context = build_item_context(cfg.game_data_dir, item, patch=patch)
    except ItemNotFoundError as exc:
        typer.echo(str(exc), err=True)
        raise typer.Exit(code=1) from exc
    typer.echo(json.dumps(dataclasses.asdict(context), indent=2))


@app.command("generate-concept")
def generate_concept_cmd(
    slug: str = typer.Argument(..., help="Corpus page slug, e.g. evasion."),
    patch: str = typer.Option(..., help="Patch context recorded on the artifact."),
    host: str = typer.Option("liquipedia_dota2", help="Corpus host key."),
    effort: str | None = typer.Option(None, help="Generation effort level override."),
) -> None:
    """Generate one concept article + card into data/kb/<patch>/concepts/.

    Uses the claude -p transport (subscription-billed). Citation marks that
    do not resolve against the context packet abort the run.
    """
    from invoker.corpus.store import CorpusStore
    from invoker.gen.claude_cli import ClaudeCliClient
    from invoker.gen.client import GenerationError
    from invoker.gen.concepts import generate_concept
    from invoker.paths import corpus_dir, kb_dir

    cfg = _load_config()
    try:
        artifact, path = generate_concept(
            CorpusStore(corpus_dir(cfg.data_dir)),
            ClaudeCliClient(),
            host_key=host,
            slug=slug,
            patch=patch,
            kb_dir=kb_dir(cfg.data_dir, patch),
            effort=effort,
        )
    except GenerationError as exc:
        typer.echo(str(exc), err=True)
        raise typer.Exit(code=1) from exc
    typer.echo(f"Wrote {path} + {artifact.article_file}")
    typer.echo(
        f"{len(artifact.citations)} distinct citations, "
        f"card: {len(artifact.card.sentences)} sentences "
        f"(model {artifact.article_provenance.model}, "
        f"transport {artifact.article_provenance.transport})"
    )


@app.command("render-kb")
def render_kb_cmd(
    patch: str = typer.Option(..., help="Patch whose KB artifacts to render."),
    out: KbSiteOutOption = KB_SITE_OUT_DEFAULT,
) -> None:
    """Render the committed KB archive into a browsable static site (S5).

    Disposable derived output — never committed. Rendering verifies every
    artifact's article binding and fails on drift.
    """
    from invoker.gen.client import GenerationError
    from invoker.paths import kb_dir
    from invoker.site.render import render_kb_site

    cfg = _load_config()
    try:
        report = render_kb_site(kb_dir(cfg.data_dir, patch), patch, out / patch)
    except GenerationError as exc:
        typer.echo(str(exc), err=True)
        raise typer.Exit(code=1) from exc
    typer.echo(
        f"Rendered {report.out_dir}/index.html "
        f"({report.generated} generated, {report.missing} missing)"
    )


@app.command("run-benchmark")
def run_benchmark_cmd(
    patch: Annotated[str, typer.Option(help="Patch whose KB to answer from.")],
    case: Annotated[
        list[str] | None,
        typer.Option("--case", help="Run only these case ids (repeatable)."),
    ] = None,
    answerer_model: Annotated[
        str | None, typer.Option(help="Answerer model override.")
    ] = None,
    judge_model: Annotated[
        str | None,
        typer.Option(help="Judge model override (defaults to the answerer model)."),
    ] = None,
) -> None:
    """Run the basic-QA benchmark against the generated KB (Milestone 1 gate).

    Answers each gold case from KB artifacts + changelog only, judges facts
    and traps, checks that cited source marks resolve, and writes a run
    report under data/benchmark-runs/. Exits nonzero if any case fails.
    """
    from invoker.benchmark.loader import BenchmarkError, load_cases
    from invoker.benchmark.report import CaseResult
    from invoker.benchmark.runner import run_benchmark
    from invoker.corpus.store import CorpusStore
    from invoker.gen.claude_cli import CLI_GENERATION_MODEL, ClaudeCliClient
    from invoker.gen.client import GenerationError
    from invoker.paths import benchmark_runs_dir, corpus_dir, kb_dir

    cfg = _load_config()
    try:
        cases = load_cases()
    except BenchmarkError as exc:
        typer.echo(str(exc), err=True)
        raise typer.Exit(code=1) from exc
    if case:
        unknown = sorted(set(case) - {c.id for c in cases})
        if unknown:
            typer.echo(f"unknown case ids: {', '.join(unknown)}", err=True)
            raise typer.Exit(code=1)
        cases = [c for c in cases if c.id in set(case)]

    changelog = None
    if cfg.game_data_dir is not None:
        changelog_path = cfg.game_data_dir / patch / "changelog.json"
        if changelog_path.exists():
            changelog = json.loads(changelog_path.read_text())
    if changelog is None:
        typer.echo(
            "warning: changelog unavailable (INVOKER_GAME_DATA_DIR unset or "
            f"no changelog.json for {patch}); temporal cases will fail against "
            "the environment, not the KB",
            err=True,
        )

    def _print(result: CaseResult) -> None:
        status = "PASS" if result.passed else f"FAIL  [{', '.join(result.failures)}]"
        typer.echo(f"{result.case_id}: {status}")

    answer_model_id = answerer_model or CLI_GENERATION_MODEL
    try:
        report, report_path = run_benchmark(
            cases=cases,
            patch=patch,
            kb_dir=kb_dir(cfg.data_dir, patch),
            corpus_store=CorpusStore(corpus_dir(cfg.data_dir)),
            changelog=changelog,
            answer_backend=ClaudeCliClient(model=answer_model_id),
            judge_backend=ClaudeCliClient(model=judge_model or answer_model_id),
            out_dir=benchmark_runs_dir(cfg.data_dir, patch),
            on_result=_print,
        )
    except GenerationError as exc:
        typer.echo(str(exc), err=True)
        raise typer.Exit(code=1) from exc
    failed = sum(1 for result in report.cases if not result.passed)
    summary = f"{len(report.cases) - failed}/{len(report.cases)} cases passed"
    if report.skipped:
        summary += f", {len(report.skipped)} skipped (patch mismatch)"
    typer.echo(summary)
    typer.echo(f"Report: {report_path}")
    if failed:
        raise typer.Exit(code=1)


@app.command("snapshot-game-files")
def snapshot_game_files_cmd(
    vpk: SnapshotVpkOption,
    out: SnapshotOutOption,
    patch: SnapshotPatchOption,
    localization: SnapshotLocalizationOption = None,
    locale: SnapshotLocaleOption = None,
) -> None:
    from invoker.snapshot.game_files import SnapshotError, snapshot_game_files

    _load_config()
    try:
        result = snapshot_game_files(
            vpk,
            out,
            patch,
            localization=localization,
            locales=locale or ["english"],
        )
    except SnapshotError as exc:
        typer.echo(str(exc), err=True)
        raise typer.Exit(code=1) from exc
    typer.echo(f"Snapshot: {result.patch_dir}")
    typer.echo(f"Heroes: {result.hero_count}")
    typer.echo(f"Abilities: {result.ability_count}")
    typer.echo(f"Items: {result.item_count}")
    typer.echo(f"Neutral item sections: {result.neutral_item_count}")
    typer.echo(f"Locales: {', '.join(result.locales)}")
    if result.changelog_patch_count:
        typer.echo(
            f"Changelog: {result.changelog_patch_count} patches, "
            f"{result.changelog_note_count} notes"
        )


@app.command("export-identity-localization")
def export_identity_localization_cmd(
    patch: SnapshotPatchOption,
    out: IdentityOutOption,
    locale: SnapshotLocaleOption = None,
) -> None:
    from invoker.identity import IdentityExportError, export_identity_localization

    cfg = _load_config()
    if cfg.game_data_dir is None:
        typer.echo(
            "INVOKER_GAME_DATA_DIR is required for export-identity-localization.",
            err=True,
        )
        raise typer.Exit(code=1)
    try:
        artifact = export_identity_localization(
            cfg.game_data_dir,
            patch,
            locales=locale,
        )
    except IdentityExportError as exc:
        typer.echo(str(exc), err=True)
        raise typer.Exit(code=1) from exc
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(artifact, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
    typer.echo(f"Identity localization: {out}")
    typer.echo(f"Heroes: {len(artifact['heroes'])}")
    typer.echo(f"Items: {len(artifact['items'])}")
    typer.echo(f"Locales: {', '.join(artifact['locales'])}")


@app.command("export-localized-resources")
def export_localized_resources_cmd(
    patch: SnapshotPatchOption,
    out_dir: LocalizedResourceOutDirOption,
    locale: SnapshotLocaleOption = None,
) -> None:
    from invoker.identity import (
        LOCALIZED_RESOURCE_FILENAMES,
        IdentityExportError,
        export_localized_resources,
    )

    cfg = _load_config()
    if cfg.game_data_dir is None:
        typer.echo(
            "INVOKER_GAME_DATA_DIR is required for export-localized-resources.",
            err=True,
        )
        raise typer.Exit(code=1)
    try:
        artifacts = export_localized_resources(
            cfg.game_data_dir,
            patch,
            locales=locale,
        )
    except IdentityExportError as exc:
        typer.echo(str(exc), err=True)
        raise typer.Exit(code=1) from exc
    out_dir.mkdir(parents=True, exist_ok=True)
    for resource_type, artifact in artifacts.items():
        path = out_dir / LOCALIZED_RESOURCE_FILENAMES[resource_type]
        path.write_text(json.dumps(artifact, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
        typer.echo(f"{resource_type.capitalize()}: {path}")
    typer.echo(f"Locales: {', '.join(next(iter(artifacts.values()))['locales'])}")


@app.command("export-game-resources")
def export_game_resources_cmd(
    patch: SnapshotPatchOption,
    out_dir: GameResourceOutDirOption,
    locale: SnapshotLocaleOption = None,
) -> None:
    from invoker.identity import (
        GAME_RESOURCE_FILENAMES,
        IdentityExportError,
        export_game_resource_bundle,
    )

    cfg = _load_config()
    if cfg.game_data_dir is None:
        typer.echo(
            "INVOKER_GAME_DATA_DIR is required for export-game-resources.",
            err=True,
        )
        raise typer.Exit(code=1)
    try:
        artifacts = export_game_resource_bundle(cfg.game_data_dir, patch, locales=locale)
    except IdentityExportError as exc:
        typer.echo(str(exc), err=True)
        raise typer.Exit(code=1) from exc
    out_dir.mkdir(parents=True, exist_ok=True)
    for resource_type, filename in GAME_RESOURCE_FILENAMES.items():
        artifact = artifacts[resource_type]
        path = out_dir / filename
        path.write_text(json.dumps(artifact, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
        typer.echo(f"{resource_type.capitalize()}: {path}")
    bundle = artifacts["bundle"]
    typer.echo(f"Heroes: {bundle['counts']['heroes']}")
    typer.echo(f"Items: {bundle['counts']['items']}")
    typer.echo(f"Unknowns: {bundle['counts']['unknowns']}")
    typer.echo(f"Locales: {', '.join(bundle['locales'])}")


@app.command("build-team-profile")
def build_team_profile_cmd(
    team_id: int = typer.Option(..., "--team-id", help="OpenDota team ID to profile."),
    patch: str = typer.Option(..., help="Patch/output namespace for derived artifacts."),
    limit: int = typer.Option(
        50,
        "--limit",
        min=1,
        max=50,
        help="Recent team matches to inspect.",
    ),
    force: bool = typer.Option(
        False,
        "--force",
        help="Refresh OpenDota cache entries used by the profile build.",
    ),
    include_standins: bool = typer.Option(
        True,
        "--include-standins/--exclude-standins",
        help="Include or exclude matches where non-canonical stand-ins appeared.",
    ),
) -> None:
    """Build a derived team hero-pool profile from cached OpenDota match data."""
    import asyncio

    from invoker.pipeline.team_profile import (
        TeamProfileCurationResult,
        TeamProfileScaffoldResult,
        build_team_profile,
    )

    cfg = _load_config()
    if cfg.game_data_dir is None:
        typer.echo("INVOKER_GAME_DATA_DIR is required for build-team-profile.", err=True)
        raise typer.Exit(code=1)
    result = asyncio.run(
        build_team_profile(
            data_dir=cfg.data_dir,
            game_data_dir=cfg.game_data_dir,
            cache_dir=cfg.cache_dir,
            team_id=team_id,
            patch=patch,
            limit=limit,
            force=force,
            include_standin_matches=include_standins,
        )
    )
    if isinstance(result, TeamProfileScaffoldResult):
        typer.echo(f"Scaffolded team registry entry: {result.registry_path}")
        typer.echo(f"Discovered name: {result.discovered_name or '<unknown>'}")
        typer.echo(f"Discovered roster ({len(result.discovered_roster)} players):")
        for player in result.discovered_roster:
            label = player["name"] or "<unknown>"
            typer.echo(f"  - {player['account_id']}: {label}")
        typer.echo(
            "Assign position (1-5) to each player in the registry, "
            "then re-run build-team-profile to generate profile.json."
        )
        return
    if isinstance(result, TeamProfileCurationResult):
        typer.echo(f"Team registry needs roster curation: {result.registry_path}", err=True)
        typer.echo(
            f"Found {result.player_count} authored players for team_id={result.team_id}. "
            "Remove stand-ins so exactly 5 original roster players remain with positions 1-5, "
            "then re-run build-team-profile.",
            err=True,
        )
        raise typer.Exit(code=1)
    typer.echo(f"Team profile: {result.profile_path}")
    typer.echo(f"Team index: {result.index_path}")
    typer.echo(f"Roster hash: {result.roster_hash}")
    typer.echo(f"Matches: {result.match_count}")
    typer.echo(f"Heroes: {result.hero_count}")
    if result.missing_match_detail_count:
        typer.echo(f"Missing match details: {result.missing_match_detail_count}", err=True)


@app.command("serve-knowledge")
def serve_knowledge_cmd(
    bundle: Annotated[
        Path,
        typer.Option(
            "--bundle",
            help="Resource bundle root containing bundle.json, game_constants/, and derived/.",
        ),
    ],
    host: Annotated[str, typer.Option(help="HTTP bind host.")] = "127.0.0.1",
    port: Annotated[int, typer.Option(help="HTTP bind port.")] = 8765,
) -> None:
    """Serve the local read-only knowledge service over HTTP."""
    from invoker.service import KnowledgeService, KnowledgeServiceError
    from invoker.service.http import serve

    _load_config()
    try:
        service = KnowledgeService(bundle)
        typer.echo(f"Knowledge service: http://{host}:{port}")
        serve(service, host=host, port=port)
    except KnowledgeServiceError as exc:
        typer.echo(exc.message, err=True)
        raise typer.Exit(code=1) from exc


@app.command("vocab-audit")
def vocab_audit_cmd() -> None:
    from invoker.kg.vocab_audit import format_vocab_audit, run_vocab_audit

    cfg = _load_config()
    audit = run_vocab_audit(cfg.data_dir)
    typer.echo(format_vocab_audit(audit))
    if not audit.passed:
        raise typer.Exit(code=1)


@app.command("review-vocabulary")
def review_vocabulary_cmd(
    bucket: str | None = typer.Option(
        None,
        help="Only review one vocabulary bucket, e.g. capabilities.",
    ),
    term: str | None = typer.Option(
        None,
        help="Only review one term within the selected bucket.",
    ),
    include_reviewed: bool = typer.Option(
        False,
        "--include-reviewed",
        help="Show terms that already have a recorded review note.",
    ),
) -> None:
    from invoker.kg.vocabulary_review import (
        REVIEW_ACTIONS,
        iter_vocabulary_review_contexts,
        record_vocabulary_review,
    )

    cfg = _load_config()
    contexts = iter_vocabulary_review_contexts(
        cfg.data_dir,
        bucket=bucket,
        term=term,
        include_reviewed=include_reviewed,
    )
    if not contexts:
        typer.echo("No vocabulary terms matched the review filter.")
        return

    actions = ", ".join(sorted(REVIEW_ACTIONS | {"skip"}))
    for context in contexts:
        typer.echo("")
        typer.echo(f"{context.bucket}.{context.term}")
        typer.echo(f"status: {context.metadata.get('status', '')}")
        typer.echo(f"definition: {context.metadata.get('definition', '')}")
        if context.used_by:
            typer.echo(f"used by: {', '.join(context.used_by)}")
        else:
            typer.echo("used by: none")
        if context.consumed_by_rules:
            typer.echo(f"consumed by rules: {', '.join(context.consumed_by_rules)}")
        else:
            typer.echo("consumed by rules: none")
        desired_action = typer.prompt(
            f"Desired action ({actions})",
            default="skip",
        ).strip()
        if desired_action == "skip":
            continue
        if desired_action not in REVIEW_ACTIONS:
            typer.echo(f"Invalid action: {desired_action}", err=True)
            raise typer.Exit(code=1)
        note = typer.prompt("Human suggestion", default="").strip()
        record = record_vocabulary_review(
            cfg.data_dir,
            context,
            desired_action=desired_action,
            human_suggestion=note,
        )
        typer.echo(f"Recorded review for {record.bucket}.{record.term}")


@app.command("review-vocab-gaps")
def review_vocab_gaps_cmd(
    bucket: str | None = typer.Option(
        None,
        help="Only review vocabulary gaps for one bucket, e.g. capabilities.",
    ),
    candidate_term: str | None = typer.Option(
        None,
        help="Only review gaps with this candidate term.",
    ),
    include_reviewed: bool = typer.Option(
        False,
        "--include-reviewed",
        help="Show gaps that already have a recorded review note.",
    ),
) -> None:
    from invoker.kg.vocabulary_review import (
        GAP_REVIEW_ACTIONS,
        iter_vocabulary_gap_contexts,
        record_vocabulary_gap_review,
    )

    cfg = _load_config()
    contexts = iter_vocabulary_gap_contexts(
        cfg.data_dir,
        bucket=bucket,
        candidate_term=candidate_term,
        include_reviewed=include_reviewed,
    )
    if not contexts:
        typer.echo("No vocabulary gaps matched the review filter.")
        return

    actions = ", ".join(sorted(GAP_REVIEW_ACTIONS | {"skip"}))
    for context in contexts:
        typer.echo("")
        typer.echo(f"{context.bucket}: {context.concept}")
        typer.echo(f"hero: {context.localized_name or context.hero_slug}")
        typer.echo(f"candidate term: {context.candidate_term or '(none)'}")
        typer.echo(f"why needed: {context.why_needed}")
        typer.echo(f"evidence: {context.evidence}")
        desired_action = typer.prompt(
            f"Desired action ({actions})",
            default="skip",
        ).strip()
        if desired_action == "skip":
            continue
        if desired_action not in GAP_REVIEW_ACTIONS:
            typer.echo(f"Invalid action: {desired_action}", err=True)
            raise typer.Exit(code=1)
        note = typer.prompt("Human suggestion", default="").strip()
        record = record_vocabulary_gap_review(
            cfg.data_dir,
            context,
            desired_action=desired_action,
            human_suggestion=note,
        )
        label = record.candidate_term or record.concept
        typer.echo(f"Recorded gap review for {record.hero_slug}: {label}")


@app.command("compose-vocabulary-prompt")
def compose_vocabulary_prompt_cmd(
    bucket: str | None = typer.Option(
        None,
        help="Only include one vocabulary bucket in the prompt.",
    ),
    term: str | None = typer.Option(
        None,
        help="Only include one term within the selected bucket.",
    ),
    reviewed_only: bool = typer.Option(
        False,
        "--reviewed-only",
        help="Only include terms with recorded human review notes.",
    ),
) -> None:
    from invoker.kg.vocabulary_review import write_vocabulary_revision_prompt

    cfg = _load_config()
    result = write_vocabulary_revision_prompt(
        cfg.data_dir,
        bucket=bucket,
        term=term,
        reviewed_only=reviewed_only,
    )
    typer.echo(f"Vocabulary revision prompt: {result.prompt_path}")
    typer.echo(f"Paste LLM response into: {result.response_path}")


@app.command("parse-vocabulary-response")
def parse_vocabulary_response_cmd(
    response_path: str = typer.Argument(
        ...,
        help="Manual LLM response file produced by compose-vocabulary-prompt.",
    ),
) -> None:
    from pathlib import Path

    from invoker.kg.vocabulary_proposals import parse_vocabulary_proposals

    cfg = _load_config()
    result = parse_vocabulary_proposals(cfg.data_dir, Path(response_path))
    typer.echo(
        f"Parsed {result.parsed_count} proposal(s): "
        f"{result.added_count} added, {result.updated_count} updated"
    )
    typer.echo(f"Proposal inbox: {result.proposals_path}")


@app.command("review-vocabulary-proposals")
def review_vocabulary_proposals_cmd(
    bucket: str | None = typer.Option(None, help="Only review proposals in one bucket."),
    term: str | None = typer.Option(None, help="Only review proposals for one term."),
    proposal_id: str | None = typer.Option(None, help="Only review one proposal id."),
    include_reviewed: bool = typer.Option(
        False,
        "--include-reviewed",
        help="Include proposals that already have a human decision.",
    ),
) -> None:
    from invoker.kg.vocabulary_proposals import (
        REVIEW_STATUSES,
        VocabularyProposalError,
        iter_vocabulary_proposals,
        review_vocabulary_proposal,
    )

    cfg = _load_config()
    status = None if include_reviewed else "pending"
    proposals = iter_vocabulary_proposals(
        cfg.data_dir,
        bucket=bucket,
        term=term,
        review_status=status,
        proposal_id=proposal_id,
    )
    if not proposals:
        typer.echo("No vocabulary proposals matched the review filter.")
        return

    actions = ", ".join(sorted((REVIEW_STATUSES - {"pending"}) | {"skip"}))
    for proposal in proposals:
        typer.echo("")
        typer.echo(f"{proposal['proposal_id']}")
        typer.echo(f"{proposal['bucket']}.{proposal['term']} ({proposal['action']})")
        typer.echo(f"current review status: {proposal.get('review_status', 'pending')}")
        if proposal.get("definition"):
            typer.echo(f"definition: {proposal['definition']}")
        if proposal.get("rationale"):
            typer.echo(f"rationale: {proposal['rationale']}")
        decision = typer.prompt(f"Review decision ({actions})", default="skip").strip()
        if decision == "skip":
            continue
        if decision not in REVIEW_STATUSES - {"pending"}:
            typer.echo(f"Invalid decision: {decision}", err=True)
            raise typer.Exit(code=1)
        note = typer.prompt("Human note", default="").strip()
        try:
            result = review_vocabulary_proposal(
                cfg.data_dir,
                str(proposal["proposal_id"]),
                review_status=decision,
                human_note=note,
            )
        except VocabularyProposalError as exc:
            typer.echo(str(exc), err=True)
            raise typer.Exit(code=1) from exc
        typer.echo(f"Recorded {result.review_status} for {result.proposal_id}")


@app.command("amend-vocabulary-proposal")
def amend_vocabulary_proposal_cmd(
    proposal_id: str = typer.Argument(..., help="Proposal id to amend."),
    action: str | None = typer.Option(None, help="Replacement proposal action."),
    term: str | None = typer.Option(None, help="Replacement proposal term."),
    review_status: str | None = typer.Option(None, help="Replacement review status."),
    human_note: str | None = typer.Option(None, help="Replacement human note."),
) -> None:
    from invoker.kg.vocabulary_proposals import (
        VocabularyProposalError,
        amend_vocabulary_proposal,
    )

    cfg = _load_config()
    try:
        result = amend_vocabulary_proposal(
            cfg.data_dir,
            proposal_id,
            action=action,
            term=term,
            review_status=review_status,
            human_note=human_note,
        )
    except VocabularyProposalError as exc:
        typer.echo(str(exc), err=True)
        raise typer.Exit(code=1) from exc
    typer.echo(f"Amended proposal: {result.old_proposal_id} -> {result.new_proposal_id}")
    typer.echo(f"Proposal inbox: {result.proposal_path}")


@app.command("promote-vocabulary")
def promote_vocabulary_cmd(
    bucket: str | None = typer.Option(None, help="Only promote accepted proposals in one bucket."),
    term: str | None = typer.Option(None, help="Only promote accepted proposals for one term."),
    proposal_id: str | None = typer.Option(None, help="Only promote one accepted proposal id."),
    max_terms: int = typer.Option(
        10,
        help="Warn when a promotion round adds or renames more than this many terms.",
    ),
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        help="Validate and print what would be promoted without writing files.",
    ),
) -> None:
    from invoker.kg.vocabulary_proposals import VocabularyProposalError, promote_vocabulary

    cfg = _load_config()
    try:
        result = promote_vocabulary(
            cfg.data_dir,
            bucket=bucket,
            term=term,
            proposal_id=proposal_id,
            max_terms=max_terms,
            dry_run=dry_run,
        )
    except VocabularyProposalError as exc:
        typer.echo(str(exc), err=True)
        raise typer.Exit(code=1) from exc
    prefix = "Would promote" if dry_run else "Promoted"
    typer.echo(f"{prefix} {len(result.promoted_ids)} vocabulary proposal(s):")
    for term_name in result.promoted_terms:
        typer.echo(f"- {term_name}")
    for warning in result.warnings:
        typer.echo(f"Warning: {warning}", err=True)
    if not dry_run:
        typer.echo(f"Vocabulary: {result.vocabulary_path}")
        typer.echo(f"Proposal inbox: {result.proposals_path}")
        typer.echo(f"Notes: {result.notes_path}")


@app.command()
def bootstrap(
    patch: str = typer.Option(..., help="Patch string, e.g. 7.41b"),
    heroes: str | None = typer.Option(
        None, help="Comma-separated authored hero names, slugs, or ids."
    ),
) -> None:
    """Build derived hero facts and relations from authored YAML files."""
    from invoker.pipeline.orchestrator import run_bootstrap

    cfg = _load_config()
    if heroes is not None:
        hero_filter: set[str] | None = {t.strip() for t in heroes.split(",") if t.strip()}
    elif cfg.dev_heroes:
        hero_filter = set(cfg.dev_heroes)
    else:
        hero_filter = None

    if hero_filter:
        typer.echo(f"Hero filter active: {sorted(hero_filter)}")

    results = run_bootstrap(cfg.data_dir, patch, __version__, heroes=hero_filter)
    relations = RelationsReader.load(relations_file(cfg.data_dir, patch))
    typer.echo(f"Wrote {len(results)} hero fact view(s).")
    typer.echo(f"Wrote relations.json with {len(relations.all())} relation(s).")
    typer.echo("Manifest, summaries, and graph cache written.")


@app.command()
def status(patch: str = typer.Option(..., help="Patch to inspect.")) -> None:
    cfg = _load_config()
    p = manifest_file(cfg.data_dir, patch)
    if not p.exists():
        typer.echo(f"No manifest for {patch}.")
        raise typer.Exit(code=1)
    typer.echo(p.read_text())


@app.command()
def validate(patch: str = typer.Option(..., help="Patch to validate.")) -> None:
    from invoker.pipeline.validators import ValidationContext, validate_hero
    from invoker.pipeline.writer import read_hero

    cfg = _load_config()
    m = json.loads(manifest_file(cfg.data_dir, patch).read_text())
    ids = {e["hero_id"] for e in m.get("heroes", [])}
    ctx = ValidationContext(roster_hero_ids=ids)
    failures = 0
    for entry in m["heroes"]:
        try:
            validate_hero(read_hero(cfg.data_dir, patch, entry["hero_id"]), ctx)
        except Exception as e:
            typer.echo(f"hero {entry['hero_id']}: {e}")
            failures += 1
    try:
        RelationsReader.load(relations_file(cfg.data_dir, patch))
    except Exception as e:
        typer.echo(f"relations: {e}")
        failures += 1
    typer.echo(f"{len(m['heroes']) - failures}/{len(m['heroes'])} heroes validated.")
    if failures:
        raise typer.Exit(code=1)


@app.command()
def publish(
    patch: str = typer.Option(..., help="Patch to bundle."),
    out: PublishOutOption = PUBLISH_OUT_DEFAULT,
    force: bool = typer.Option(
        False,
        "--force",
        help="Overwrite an existing local release path.",
    ),
) -> None:
    from invoker.pipeline.release import ReleaseError, create_release_bundle

    cfg = _load_config()
    try:
        result = create_release_bundle(
            cfg.data_dir,
            patch,
            out,
            invoker_version=__version__,
            game_data_dir=cfg.game_data_dir,
            force=force,
        )
    except ReleaseError as exc:
        typer.echo(str(exc), err=True)
        raise typer.Exit(code=1) from exc
    typer.echo(f"Release directory: {result.release_dir}")
    typer.echo(f"Archive: {result.archive_path}")
    typer.echo("Checklist:")
    typer.echo("- review release.json")
    typer.echo("- review reports/validation.txt")
    typer.echo("- review reports/vocab-audit.txt")


@app.command("fetch-corpus")
def fetch_corpus_cmd(
    host: Annotated[
        str | None,
        typer.Option(help="Only fetch this host key from the corpus registry."),
    ] = None,
    patch: Annotated[
        str | None,
        typer.Option(help="Optional patch context recorded on newly fetched documents."),
    ] = None,
) -> None:
    """Fetch curated MediaWiki corpus pages into revision-pinned local documents."""
    from invoker.corpus.fetch import fetch_corpus
    from invoker.corpus.registry import RegistryError, load_registry
    from invoker.corpus.store import CorpusStore
    from invoker.paths import corpus_dir

    cfg = _load_config()
    try:
        registry = load_registry()
        reports = fetch_corpus(
            registry,
            CorpusStore(corpus_dir(cfg.data_dir)),
            only_host=host,
            patch_context=patch,
        )
    except RegistryError as exc:
        typer.echo(str(exc), err=True)
        raise typer.Exit(code=1) from exc

    any_missing = False
    for report in reports:
        typer.echo(f"Host: {report.host_key}")
        typer.echo(f"  fetched: {len(report.fetched)}")
        for slug in report.fetched:
            typer.echo(f"    + {slug}")
        typer.echo(f"  unchanged: {len(report.unchanged)}")
        if report.missing:
            any_missing = True
            typer.echo(f"  MISSING ({len(report.missing)}):", err=True)
            for title in report.missing:
                typer.echo(f"    ! {title}", err=True)
    if any_missing:
        typer.echo("Some registry pages did not resolve; fix pages.yaml.", err=True)
        raise typer.Exit(code=1)


@app.command("changelog")
def changelog_cmd(
    patch: Annotated[
        str,
        typer.Option(help="Snapshot patch directory to read changelog.json from."),
    ],
    grep: Annotated[
        str | None,
        typer.Option(help="Substring match against note text or token."),
    ] = None,
    entity: Annotated[
        str | None,
        typer.Option("--for", help="Filter by entity: hero, ability, item, or section name."),
    ] = None,
    note_patch: Annotated[
        str | None,
        typer.Option(help="Only notes from this patch version, e.g. 7.41."),
    ] = None,
    locale: Annotated[str, typer.Option(help="Locale for note text.")] = "english",
    limit: Annotated[int, typer.Option(help="Maximum entries to print.")] = 20,
) -> None:
    """Search the in-game changelog captured in a game-file snapshot."""
    from invoker.snapshot.changelog import search_changelog

    cfg = _load_config()
    if cfg.game_data_dir is None:
        typer.echo("INVOKER_GAME_DATA_DIR is not configured", err=True)
        raise typer.Exit(code=1)
    changelog_path = cfg.game_data_dir / patch / "changelog.json"
    if not changelog_path.exists():
        typer.echo(
            f"{changelog_path} not found; re-run snapshot-game-files with "
            "patchnotes files present in the extraction",
            err=True,
        )
        raise typer.Exit(code=1)

    changelog = json.loads(changelog_path.read_text())
    results = search_changelog(
        changelog,
        grep=grep,
        entity=entity,
        note_patch=note_patch,
        locale=locale,
    )
    typer.echo(f"Matches: {len(results)}")
    for entry in results[:limit]:
        date = f" ({entry['date']})" if entry.get("date") else ""
        typer.echo(f"[{entry['patch']}]{date} {entry['scope']}/{entry['entity']}")
        typer.echo(f"  {entry['text'] or '(no text for locale)'}")
    if len(results) > limit:
        typer.echo(f"... {len(results) - limit} more (raise --limit)")


@app.command("expand-corpus")
def expand_corpus_cmd(
    host: Annotated[
        str | None,
        typer.Option(help="Only expand this host key from the corpus registry."),
    ] = None,
    limit: Annotated[
        int | None,
        typer.Option(help="Stop after expanding this many pages (for partial runs)."),
    ] = None,
) -> None:
    """Fetch template-expanded HTML for fetched corpus revisions.

    Slow by design: parse calls run at the host's strict rate limit
    (~1 per 30s on Liquipedia). Incremental — already-expanded revisions
    are skipped, so re-runs only cost what changed."""
    from invoker.corpus.expand import expand_corpus
    from invoker.corpus.registry import RegistryError, load_registry
    from invoker.corpus.store import CorpusStore
    from invoker.paths import corpus_dir

    cfg = _load_config()
    try:
        registry = load_registry()

        def _progress(host_key: str, slug: str, event: str) -> None:
            marker = "+" if event == "expanded" else "!"
            typer.echo(f"  {marker} {event} {host_key}/{slug}", err=event == "failed")

        reports = expand_corpus(
            registry,
            CorpusStore(corpus_dir(cfg.data_dir)),
            only_host=host,
            limit=limit,
            progress=_progress,
        )
    except RegistryError as exc:
        typer.echo(str(exc), err=True)
        raise typer.Exit(code=1) from exc

    any_failed = False
    for report in reports:
        typer.echo(
            f"Host: {report.host_key} — expanded {len(report.expanded)}, "
            f"already current {len(report.skipped)}, failed {len(report.failed)}"
        )
        for slug, error in report.failed:
            any_failed = True
            typer.echo(f"  ! {slug}: {error}", err=True)
        if report.aborted_reason:
            typer.echo(f"  ABORTED: {report.aborted_reason}", err=True)
    if any_failed:
        raise typer.Exit(code=1)


@app.command("corpus-coverage")
def corpus_coverage_cmd(
    host: Annotated[
        str | None,
        typer.Option(help="Only report this host key from the corpus registry."),
    ] = None,
) -> None:
    """Diff each host's coverage categories against the curated registry.

    Shows what is fetched, what is deliberately omitted (with the recorded
    reason), and what is still unreviewed."""
    from invoker.corpus.coverage import corpus_coverage
    from invoker.corpus.registry import RegistryError, load_registry
    from invoker.corpus.store import CorpusStore
    from invoker.paths import corpus_dir

    cfg = _load_config()
    try:
        registry = load_registry()
        reports = corpus_coverage(
            registry,
            CorpusStore(corpus_dir(cfg.data_dir)),
            only_host=host,
        )
    except RegistryError as exc:
        typer.echo(str(exc), err=True)
        raise typer.Exit(code=1) from exc

    for report in reports:
        typer.echo(f"Host: {report.host_key}")
        if report.universe_size == 0:
            typer.echo("  no coverage_categories configured; nothing to diff against")
            continue
        typer.echo(f"  category universe: {report.universe_size} pages")
        typer.echo(f"  covered: {len(report.covered)}")
        typer.echo(f"  omitted: {len(report.omitted)}")
        for title, reason in report.omitted:
            typer.echo(f"    - {title}: {reason}")
        for prefix, reason, count in report.omitted_by_rule:
            typer.echo(f"  omitted by rule '{prefix}*': {count} pages ({reason})")
        typer.echo(f"  unreviewed: {len(report.unreviewed)}")
        for title in report.unreviewed:
            typer.echo(f"    ? {title}")
        if report.outside_categories:
            typer.echo(
                f"  registry pages outside coverage categories: {len(report.outside_categories)}"
            )
            for title in report.outside_categories:
                typer.echo(f"    ~ {title}")
        if report.unreviewed:
            typer.echo(
                "  unreviewed pages need triage: add to pages or omit (with reason) "
                "in src/invoker/corpus/pages.yaml"
            )


if __name__ == "__main__":
    app()
