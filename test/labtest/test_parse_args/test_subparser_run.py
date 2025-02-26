from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from labtest.labtest import parse_args

if TYPE_CHECKING:
    from argparse import Namespace as Args
    from collections.abc import Callable


@pytest.fixture(name="parse_args_run")
def fixture_parse_args_run() -> Callable:
    def _fixture_parse_args_run(args: list[str]) -> Args:
        return parse_args(["run", *args])

    return _fixture_parse_args_run


def test_subparser_run_help(parse_args_run: Callable) -> None:
    with pytest.raises(SystemExit) as e:
        parse_args_run(["-h"])
    assert e.value.code == 0


def test_subparser_run_no_args(parse_args_run: Callable) -> None:
    assert parse_args_run([""]).name == ""


def test_subparser_run_name(parse_args_run: Callable) -> None:
    assert parse_args_run(["name"]).name == "name"


def test_subparser_run_source_one_path(parse_args_run: Callable) -> None:
    args = parse_args_run(["name", "--source", "alpha"])
    assert args.name == "name"
    assert sorted(args.source) == ["alpha"]


def test_subparser_run_source_two_paths(parse_args_run: Callable) -> None:
    args = parse_args_run(["name", "--source", "alpha", "--source", "beta"])
    assert args.name == "name"
    assert sorted(args.source) == ["alpha", "beta"]
