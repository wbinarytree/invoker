from __future__ import annotations

import typer

app = typer.Typer(help="Invoker - Dota 2 knowledge framework", no_args_is_help=True)


@app.callback()
def _main() -> None:
    """Invoker CLI entrypoint."""


@app.command()
def version() -> None:
    """Print Invoker version."""
    from invoker import __version__

    typer.echo(f"invoker {__version__}")


if __name__ == "__main__":
    app()
