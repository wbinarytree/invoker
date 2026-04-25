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
