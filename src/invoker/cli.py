from __future__ import annotations

import json

import typer

from invoker import __version__
from invoker.config import Config
from invoker.kg.reader import RelationsReader
from invoker.logging import configure_logging
from invoker.paths import manifest_file, relations_file

app = typer.Typer(help="Invoker - Dota 2 knowledge framework")


def _load_config() -> Config:
    cfg = Config.load()
    configure_logging(cfg.log_level)
    return cfg


@app.command()
def version() -> None:
    typer.echo(f"invoker {__version__}")


@app.command("draft-facts")
def draft_facts_cmd(
    hero: str = typer.Argument(..., help="Hero localized name, slug, or numeric id."),
    patch: str = typer.Option(
        "authoring",
        help="Cache namespace for OpenDota prompt inputs; does not affect authored YAML format.",
    ),
) -> None:
    from invoker.kg.authoring import draft_facts

    cfg = _load_config()
    result = draft_facts(cfg.data_dir, hero, patch=patch)
    if result.pending:
        typer.echo(f"Prompt written: {result.prompt_path}")
        typer.echo(f"Paste the LLM response into: {result.response_path}")
        raise typer.Exit(code=0)
    typer.echo(f"Wrote draft facts: {result.authored_path}")


@app.command("validate-facts")
def validate_facts_cmd(
    hero: str = typer.Argument(..., help="Hero localized name, slug, or numeric id."),
) -> None:
    from invoker.kg.authoring import (
        resolve_authored_file,
        validate_authored_file,
    )

    cfg = _load_config()
    path = resolve_authored_file(cfg.data_dir, hero)
    profile = validate_authored_file(path)
    typer.echo(f"{path}: valid ({profile.localized_name})")


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
