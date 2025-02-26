from __future__ import annotations

from typing import TYPE_CHECKING

import labtest
from labtest.labtest import main
from labtest.registry import Registry

if TYPE_CHECKING:
    from collections.abc import Callable

    import pytest


def test_subcommand_list_registry_empty(
    mock_sys_argv: Callable, capsys: pytest.CaptureFixture[str]
) -> None:
    registry = Registry(is_singleton=False)
    with mock_sys_argv("main", "list"):
        main(registry=registry)
        captured = capsys.readouterr()
        assert "INFO: Did not find any registered functions" in captured.out


def test_subcommand_list_registry_one_entry(
    mock_sys_argv: Callable, capsys: pytest.CaptureFixture[str]
) -> None:
    registry = Registry(is_singleton=False)

    @labtest.register(registry)
    def mock_test_subcommand_list_registry_one_entry() -> None:
        """mock_test_subcommand_list_registry_one_entry"""

    with mock_sys_argv("main", "list"):
        main(registry=registry)
        captured = capsys.readouterr()
        assert (
            f"{__file__}:mock_test_subcommand_list_registry_one_entry\n" in captured.out
        )


def test_subcommand_list_registry_two_entries(
    mock_sys_argv: Callable, capsys: pytest.CaptureFixture[str]
) -> None:
    registry = Registry(is_singleton=False)

    @labtest.register(registry)
    def mock_test_subcommand_list_registry_two_entries_alpha() -> None:
        """mock_test_subcommand_list_registry_two_entries_alpha"""

    @labtest.register(registry)
    def mock_test_subcommand_list_registry_two_entries_beta() -> None:
        """mock_test_subcommand_list_registry_two_entries_beta"""

    with mock_sys_argv("main", "list"):
        main(registry=registry)
        captured = capsys.readouterr()
        assert (
            f"{__file__}:mock_test_subcommand_list_registry_two_entries_alpha\n"
            f"{__file__}:mock_test_subcommand_list_registry_two_entries_beta\n"
            in captured.out
        )


def test_subcommand_list_registry_singleton(
    mock_sys_argv: Callable, mock_registry: Callable, capsys: pytest.CaptureFixture[str]
) -> None:
    with mock_registry(), mock_sys_argv("main", "list"):

        @labtest.register
        def mock_test_subcommand_list_registry_singleton() -> None:
            """mock_test_subcommand_list_registry_one_entry"""

        main()
        captured = capsys.readouterr()
        assert (
            f"{__file__}:mock_test_subcommand_list_registry_singleton\n" in captured.out
        )
