from __future__ import annotations

from pathlib import Path

import yaml
from pydantic import ValidationError

from invoker.corpus.schemas import CorpusRegistry

PACKAGED_REGISTRY = Path(__file__).with_name("pages.yaml")


class RegistryError(RuntimeError):
    pass


def select_host_keys(registry: CorpusRegistry, only_host: str | None) -> list[str]:
    """Host keys to operate on, validating an explicit --host selection."""
    host_keys = list(registry.hosts)
    if only_host is None:
        return host_keys
    if only_host not in registry.hosts:
        raise RegistryError(
            f"unknown corpus host {only_host!r}; registry has: {', '.join(host_keys)}"
        )
    return [only_host]


def load_registry(path: Path | None = None) -> CorpusRegistry:
    registry_path = path or PACKAGED_REGISTRY
    if not registry_path.exists():
        raise RegistryError(f"corpus registry not found: {registry_path}")
    raw = yaml.safe_load(registry_path.read_text())
    try:
        return CorpusRegistry.model_validate(raw)
    except ValidationError as exc:
        raise RegistryError(f"invalid corpus registry {registry_path}: {exc}") from exc
