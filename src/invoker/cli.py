from __future__ import annotations

import asyncio
import json

import typer

from invoker import __version__
from invoker.config import Config
from invoker.logging import configure_logging
from invoker.paths import manifest_file

app = typer.Typer(help="Invoker - Dota 2 knowledge framework")


def _load_config() -> Config:
    cfg = Config.load()
    configure_logging(cfg.log_level)
    return cfg


@app.command()
def version() -> None:
    typer.echo(f"invoker {__version__}")


@app.command()
def bootstrap(
    patch: str = typer.Option(..., help="Patch string, e.g. 7.41b"),
    heroes: str | None = typer.Option(
        None, help="Comma-separated hero names or ids (overrides INVOKER_DEV_HEROES)."
    ),
    skip_extract: bool = typer.Option(False, help="Skip LLM extraction; use last run."),
    skip_reasons: bool = typer.Option(
        False, help="Skip reason generation; write heroes with stat edges only."
    ),
    max_reason_edges: int = typer.Option(
        5,
        help="Cap synergy and counter edges fed to the batch reason call, per hero.",
        min=0,
    ),
    manual: bool = typer.Option(
        False,
        help="Use the manual/file-based LLM client. Prompts are written to disk "
        "and the run pauses for you to paste responses; rerun to continue.",
    ),
) -> None:
    """Run the full bootstrap pipeline for a patch."""
    from invoker import __version__
    from invoker.llm import CachingLLMClient, make_client
    from invoker.pipeline.bundle import build_bundles
    from invoker.pipeline.fetch import fetch_all
    from invoker.pipeline.orchestrator import (
        HeroRawBundle,
        HeroResult,
        finalize_patch,
        run_bootstrap,
    )

    cfg = _load_config()

    # CLI flag takes precedence over env var; both are optional.
    if heroes is not None:
        hero_filter: set[str] | None = {t.strip() for t in heroes.split(",") if t.strip()}
    elif cfg.dev_heroes:
        hero_filter = set(cfg.dev_heroes)
    else:
        hero_filter = None

    if hero_filter:
        typer.echo(f"Hero filter active: {sorted(hero_filter)}")
        typer.echo(
            "Subset mode: per-hero matchups, STRATZ edges and LLM extractions "
            "run only for the filtered heroes. Global roster, ability and pro-match "
            "fetches still run. Manifest will be written as 'partial'."
        )

    typer.echo(f"Fetching raw data for {patch}...")
    raw = asyncio.run(fetch_all(cfg, patch, hero_filter=hero_filter))
    typer.echo(f"Fetched {len(raw['heroes'])} heroes.")

    bundles = build_bundles(raw, patch)
    hero_names: dict[int, str] = raw["hero_names"]

    from invoker.llm.gemini import make_model_config

    llm_kind = "manual" if manual else cfg.llm_client
    model_cfg = make_model_config(cfg.llm_model, cfg.llm_rpm, cfg.llm_rpd)
    if llm_kind == "manual":
        typer.echo("LLM: manual (file-based; prompts under data/raw/manual_prompts/)")
    else:
        typer.echo(f"LLM: {llm_kind}  model={cfg.llm_model}  rpm={cfg.llm_rpm}  rpd={cfg.llm_rpd}")
    inner = make_client(llm_kind, config=model_cfg)
    client = CachingLLMClient(inner, cfg.data_dir / "cache" / "llm")

    per_hero_calls = 1 + (0 if skip_reasons else 1)
    typer.echo(
        f"Planning up to {len(bundles) * per_hero_calls} LLM calls "
        f"({len(bundles)} heroes x {per_hero_calls} call/hero, worst case; "
        f"cache hits reduce this)."
    )

    def _on_extract(bundle: HeroRawBundle, r: HeroResult) -> None:
        status = "ok" if r.success else f"FAILED ({r.failure_reason})"
        typer.echo(f"  extract hero {bundle.hero_id:>4} {bundle.localized_name:<24} {status}")

    def _on_reason(bundle: HeroRawBundle, r: HeroResult) -> None:
        status = "ok" if r.success else f"FAILED ({r.failure_reason})"
        typer.echo(
            f"  reason  hero {bundle.hero_id:>4} {bundle.localized_name:<24} "
            f"{status}  reasons={r.reasons_written}"
        )

    typer.echo(
        "Two-pass bootstrap: extracting all hero tags first, "
        + ("then skipping reasons." if skip_reasons else "then generating reasons.")
    )

    results = run_bootstrap(
        cfg.data_dir,
        patch,
        __version__,
        bundles,
        client,
        max_reason_edges=max_reason_edges,
        skip_reasons=skip_reasons,
        hero_names=hero_names,
        on_extract=_on_extract,
        on_reason=_on_reason,
    )

    succeeded = [r for r in results if r.success]
    failed = [r for r in results if not r.success]
    reasons_written = sum(r.reasons_written for r in results)
    reasons_skipped = sum(r.reasons_skipped for r in results)
    pending_prompts: list = []
    for r in results:
        if r.pending_manual_paths:
            pending_prompts.extend(r.pending_manual_paths)

    typer.echo("")
    typer.echo("Bootstrap summary:")
    typer.echo(f"  heroes requested:  {len(bundles)}")
    typer.echo(f"  heroes written:    {len(succeeded)}")
    typer.echo(f"  heroes failed:     {len(failed)}")
    typer.echo(f"  reasons written:   {reasons_written}")
    typer.echo(f"  reasons skipped:   {reasons_skipped}")
    if failed:
        for r in failed:
            typer.echo(f"    failed hero {r.hero_id}: {r.failure_reason}")

    if pending_prompts:
        typer.echo("")
        typer.echo(f"Manual mode: {len(pending_prompts)} prompt(s) awaiting response.")
        typer.echo("Paste the JSON output for each prompt into the matching response path:")
        for p in pending_prompts:
            response = str(p).replace("manual_prompts", "manual_responses")
            response = response[:-3] + ".txt"
            typer.echo(f"  prompt:   {p}")
            typer.echo(f"  response: {response}")
        typer.echo("Then rerun the same bootstrap command to continue.")

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
