import json
from pathlib import Path

import pytest

from invoker.patches import PatchWindowError, load_patch_windows, patch_window_for_timestamp


def test_load_patch_windows_resolves_current_manual_windows():
    windows = load_patch_windows()

    assert [window.patch for window in windows] == [
        "7.40b",
        "7.40c",
        "7.41",
        "7.41a",
        "7.41b",
        "7.41c",
    ]
    current = patch_window_for_timestamp(1778889600, windows)
    last_patch = patch_window_for_timestamp(1775606400, windows)
    recent_previous = patch_window_for_timestamp(1774656000, windows)
    older_previous = patch_window_for_timestamp(1774483200, windows)
    assert current is not None and current.patch == "7.41c"
    assert last_patch is not None and last_patch.patch == "7.41b"
    assert recent_previous is not None and recent_previous.patch == "7.41a"
    assert older_previous is not None and older_previous.patch == "7.41"


def test_patch_window_lookup_returns_none_outside_known_windows():
    windows = load_patch_windows()

    assert patch_window_for_timestamp(None, windows) is None
    assert patch_window_for_timestamp(1766447999, windows) is None


def test_load_patch_windows_rejects_overlaps(tmp_path: Path):
    path = tmp_path / "patches.json"
    path.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "windows": [
                    {
                        "patch": "7.41",
                        "start_date": "2026-03-24",
                        "end_date_exclusive": "2026-04-08",
                    },
                    {
                        "patch": "7.41b",
                        "start_date": "2026-04-07",
                        "end_date_exclusive": None,
                    },
                ],
            }
        )
    )

    with pytest.raises(PatchWindowError, match="overlaps"):
        load_patch_windows(path)
