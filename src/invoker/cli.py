from __future__ import annotations

import json
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
        "authoring",
        help="Cache namespace for OpenDota prompt inputs; does not affect authored YAML format.",
    ),
) -> None:
    from invoker.kg.authoring import draft_facts

    cfg = _load_config()
    failures = 0
    for hero in heroes:
        try:
            result = draft_facts(cfg.data_dir, hero, patch=patch)
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
def publish(patch: str = typer.Option(..., help="Patch to bundle.")) -> None:
    import tarfile

    from invoker.paths import derived_patch_dir, dist_file

    cfg = _load_config()
    src = derived_patch_dir(cfg.data_dir, patch)
    if not src.exists():
        typer.echo(f"No derived data for {patch}.")
        raise typer.Exit(code=1)
    dst = dist_file(cfg.data_dir, patch)
    dst.parent.mkdir(parents=True, exist_ok=True)
    with tarfile.open(dst, "w:gz") as tar:
        tar.add(src, arcname=f"invoker-kb-{patch}")
    typer.echo(f"Wrote {dst}")


if __name__ == "__main__":
    app()
