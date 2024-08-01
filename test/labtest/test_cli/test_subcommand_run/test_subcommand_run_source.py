import pathlib
import sys

import pytest

import labtest
from labtest.labtest import main
from labtest.registry import Registry

MOCK_SOURCE_RELATIVE = "test/labtest/test_cli/mock_source"
MOCK_SOURCE_ABSOLUTE = pathlib.Path(__file__).parents[4] / MOCK_SOURCE_RELATIVE


def test_subcommand_run_source_empty(monkeypatch):
    registry = Registry(is_singleton=False)

    with monkeypatch.context() as m:
        m.setattr(sys, "argv", ["main", "run", "name", "--source", "empty"])
        with pytest.raises(ValueError, match=r"Not a registered lab test: .*"):
            main(registry=registry)


def test_subcommand_run_source_alpha(monkeypatch):
    registry = Registry(is_singleton=False)

    class MockRegistry(Registry):
        def __new__(cls, *, is_singleton: bool = True):
            return registry

    monkeypatch.setattr(labtest.decorator, "Registry", MockRegistry)

    with monkeypatch.context() as m:
        m.setattr(
            sys,
            "argv",
            [
                "main",
                "run",
                "--source",
                f"{MOCK_SOURCE_RELATIVE}",
                f"{MOCK_SOURCE_ABSOLUTE}/alpha/alpha.py:labtest_alpha",
            ],
        )
        assert main(registry=registry) == "labtest_alpha"
