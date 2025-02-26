from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from labtest.labtest import parse_args

if TYPE_CHECKING:
    from argparse import Namespace as Args
    from collections.abc import Callable


@pytest.fixture(name="parse_args_list")
def fixture_parse_args_list() -> Callable:
    def _fixture_parse_args_list(args: list[str]) -> Args:
        return parse_args(["list", *args])

    return _fixture_parse_args_list


def test_subparser_list_help(parse_args_list: Callable) -> None:
    with pytest.raises(SystemExit) as e:
        parse_args_list(["-h"])
    assert e.value.code == 0


def test_subparser_list_no_args(parse_args_list: Callable) -> None:
    parse_args_list([])


def test_subparser_list_source_one_path(parse_args_list: Callable) -> None:
    assert parse_args_list(["--source", "alpha"]).source == ["alpha"]


def test_subparser_list_source_two_paths(parse_args_list: Callable) -> None:
    assert parse_args_list(["--source", "alpha", "--source", "beta"]).source == [
        "alpha",
        "beta",
    ]
