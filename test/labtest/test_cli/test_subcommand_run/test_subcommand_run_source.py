from __future__ import annotations

import pathlib
from typing import TYPE_CHECKING

import pytest

from labtest.labtest import main

if TYPE_CHECKING:
    from collections.abc import Callable

MOCK_SOURCE_RELATIVE = "test/labtest/test_cli/mock_source"
MOCK_SOURCE_ABSOLUTE = pathlib.Path(__file__).parents[4] / MOCK_SOURCE_RELATIVE


def test_subcommand_run_source_empty(
    mock_sys_argv: Callable, mock_registry: Callable
) -> None:
    with (
        mock_registry(),
        mock_sys_argv("main", "run", "name", "--source", "empty"),
        pytest.raises(ValueError, match=r"Not a registered lab test: .*"),
    ):
        main()


def test_subcommand_run_source_alpha(
    mock_sys_argv: Callable, mock_registry: Callable
) -> None:
    with (
        mock_registry(),
        mock_sys_argv(
            "main",
            "run",
            "--source",
            f"{MOCK_SOURCE_RELATIVE}",
            f"{MOCK_SOURCE_ABSOLUTE}/alpha/alpha.py:labtest_alpha",
        ),
    ):
        assert main() == "labtest_alpha"
