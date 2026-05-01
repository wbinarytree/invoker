from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import UTC, date, datetime
from importlib import resources
from pathlib import Path
from typing import Any


class PatchWindowError(ValueError):
    pass


@dataclass(frozen=True)
class PatchWindow:
    patch: str
    start_date: date
    end_date_exclusive: date | None

    def contains(self, match_date: date) -> bool:
        if match_date < self.start_date:
            return False
        return self.end_date_exclusive is None or match_date < self.end_date_exclusive


def _parse_date(value: Any, *, field: str) -> date:
    if not isinstance(value, str):
        raise PatchWindowError(f"patch window {field} must be an ISO date string")
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise PatchWindowError(f"invalid patch window {field}: {value}") from exc


def _validate_windows(windows: list[PatchWindow]) -> list[PatchWindow]:
    sorted_windows = sorted(windows, key=lambda window: window.start_date)
    previous_end: date | None = None
    previous_patch: str | None = None
    for window in sorted_windows:
        if not window.patch:
            raise PatchWindowError("patch window patch must be non-empty")
        if window.end_date_exclusive is not None and window.end_date_exclusive <= window.start_date:
            raise PatchWindowError(f"patch window {window.patch} ends before it starts")
        if previous_end is not None and window.start_date < previous_end:
            raise PatchWindowError(
                f"patch window {window.patch} overlaps previous window {previous_patch}"
            )
        previous_end = window.end_date_exclusive
        previous_patch = window.patch
    return sorted_windows


def load_patch_windows(path: Path | None = None) -> list[PatchWindow]:
    if path is None:
        raw = json.loads(resources.files("invoker").joinpath("patches.json").read_text())
    else:
        raw = json.loads(path.read_text())
    if not isinstance(raw, dict):
        raise PatchWindowError("patches.json must contain an object")
    if raw.get("schema_version") != 1:
        raise PatchWindowError("patches.json schema_version must be 1")
    entries = raw.get("windows")
    if not isinstance(entries, list):
        raise PatchWindowError("patches.json windows must be a list")

    windows: list[PatchWindow] = []
    for entry in entries:
        if not isinstance(entry, dict):
            raise PatchWindowError("patch window entries must be objects")
        patch = entry.get("patch")
        if not isinstance(patch, str):
            raise PatchWindowError("patch window patch must be a string")
        start_date = _parse_date(entry.get("start_date"), field="start_date")
        end_value = entry.get("end_date_exclusive")
        end_date = None if end_value is None else _parse_date(end_value, field="end_date_exclusive")
        windows.append(PatchWindow(patch=patch, start_date=start_date, end_date_exclusive=end_date))
    return _validate_windows(windows)


def patch_window_for_timestamp(
    start_time: int | float | None,
    windows: list[PatchWindow] | None = None,
) -> PatchWindow | None:
    if not isinstance(start_time, int | float):
        return None
    match_date = datetime.fromtimestamp(start_time, UTC).date()
    for window in windows or load_patch_windows():
        if window.contains(match_date):
            return window
    return None
