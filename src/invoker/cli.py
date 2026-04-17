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
    heroes: str | None = typer.Option(
        None, help="Comma-separated hero names or ids (overrides INVOKER_DEV_HEROES)."
    ),
    skip_extract: bool = typer.Option(False, help="Skip LLM extraction; use last run."),
) -> None:
    """Run the full bootstrap pipeline for a patch."""
    from invoker import __version__
    from invoker.llm import CachingLLMClient, make_client
    from invoker.pipeline.bundle import build_bundles
    from invoker.pipeline.fetch import fetch_all
    from invoker.pipeline.orchestrator import HeroResult, finalize_patch, run_for_hero

    cfg = Config.load()

    # CLI flag takes precedence over env var; both are optional.
    if heroes is not None:
        hero_filter: set[str] | None = {t.strip() for t in heroes.split(",") if t.strip()}
    elif cfg.dev_heroes:
        hero_filter = set(cfg.dev_heroes)
    else:
        hero_filter = None

    if hero_filter:
        typer.echo(f"Hero filter active: {sorted(hero_filter)}")

    typer.echo(f"Fetching raw data for {patch}...")
    raw = asyncio.run(fetch_all(cfg, patch, force=force, hero_filter=hero_filter))
    typer.echo(f"Fetched {len(raw['heroes'])} heroes.")

    bundles = build_bundles(raw, patch)
    hero_names: dict[int, str] = raw["hero_names"]

    from invoker.llm.gemini import make_model_config
    model_cfg = make_model_config(cfg.llm_model, cfg.llm_rpm, cfg.llm_rpd)
    typer.echo(
        f"LLM: {cfg.llm_client}  model={cfg.llm_model}"
        f"  rpm={cfg.llm_rpm}  rpd={cfg.llm_rpd}"
    )
    inner = make_client(cfg.llm_client, config=model_cfg)
    client = CachingLLMClient(inner, cfg.data_dir / "cache" / "llm")

    results: list[HeroResult] = []
    for bundle in bundles:
        result = run_for_hero(
            cfg.data_dir,
            patch,
            __version__,
            bundle,
            client,
            hero_names=hero_names,
        )
        status = "ok" if result.success else f"FAILED ({result.failure_reason})"
        typer.echo(
            f"  hero {bundle.hero_id:>4} {bundle.localized_name:<24} "
            f"{status}  reasons={result.reasons_written}"
        )
        results.append(result)

    succeeded = [r for r in results if r.success]
    typer.echo(f"\n{len(succeeded)}/{len(results)} heroes succeeded.")

    if succeeded:
        finalize_patch(
            cfg.data_dir,
            patch,
            [r.hero_id for r in succeeded],
            complete=hero_filter is None and len(succeeded) == len(results),
        )
        typer.echo("Manifest and graph written.")


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
