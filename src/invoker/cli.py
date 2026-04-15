from __future__ import annotations

import asyncio
import json

import typer

from invoker import __version__
from invoker.config import Config
from invoker.paths import manifest_file

app = typer.Typer(help="Invoker - Dota 2 knowledge framework")


@app.command()
def version() -> None:
    typer.echo(f"invoker {__version__}")


@app.command()
def bootstrap(
    patch: str = typer.Option(..., help="Patch string, e.g. 7.41b"),
    force: bool = typer.Option(False, help="Ignore caches and refetch."),
    heroes: str | None = typer.Option(None, help="Comma-separated hero_ids (dev: limit scope)."),
    skip_extract: bool = typer.Option(False, help="Skip LLM extraction; use last run."),
) -> None:
    """Run the full bootstrap pipeline for a patch."""
    from invoker.pipeline.fetch import fetch_all

    cfg = Config.load()
    typer.echo(f"Fetching raw data for {patch}...")
    raw = asyncio.run(fetch_all(cfg, patch, force=force))
    typer.echo(f"Fetched {len(raw['heroes'])} heroes.")

    typer.echo(
        "Run programmatically via invoker.pipeline.orchestrator.run_for_hero + "
        "finalize_patch until the bundle-assembly helper lands."
    )


@app.command()
def status(patch: str = typer.Option(..., help="Patch to inspect.")) -> None:
    cfg = Config.load()
    p = manifest_file(cfg.data_dir, patch)
    if not p.exists():
        typer.echo(f"No manifest for {patch}.")
        raise typer.Exit(code=1)
    typer.echo(p.read_text())


@app.command()
def validate(patch: str = typer.Option(..., help="Patch to validate.")) -> None:
    from invoker.pipeline.validators import ValidationContext, validate_hero
    from invoker.pipeline.writer import read_hero

    cfg = Config.load()
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
    typer.echo(f"{len(m['heroes']) - failures}/{len(m['heroes'])} heroes validated.")
    if failures:
        raise typer.Exit(code=1)


@app.command()
def publish(patch: str = typer.Option(..., help="Patch to bundle.")) -> None:
    import tarfile

    from invoker.paths import derived_patch_dir, dist_file

    cfg = Config.load()
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
