import re
import sys

import pytest

import labtest
from labtest.registry import Registry

MOCK_SOURCE = "test/labtest/test_cli/mock_source"


def test_subcommand_list_source_empty(monkeypatch, capsys):
    registry = Registry(is_singleton=False)

    class MockRegistry(Registry):
        def __new__(cls, *, is_singleton: bool = True):
            return registry

    monkeypatch.setattr(labtest.decorator, "Registry", MockRegistry)

    with monkeypatch.context() as m:
        m.setattr(sys, "argv", ["main", "list", "--source", f"{MOCK_SOURCE}/empty"])
        labtest.labtest.main()
        captured = capsys.readouterr()
        assert "INFO: Did not find any registered functions" in captured.out


def test_subcommand_list_source_one_path(monkeypatch, capsys):
    registry = Registry(is_singleton=False)

    class MockRegistry(Registry):
        def __new__(cls, *, is_singleton: bool = True):
            return registry

    monkeypatch.setattr(labtest.decorator, "Registry", MockRegistry)

    with monkeypatch.context() as m:
        m.setattr(sys, "argv", ["main", "list", "--source", f"{MOCK_SOURCE}"])
        labtest.labtest.main(registry=registry)
        captured = capsys.readouterr()
        assert re.fullmatch(
            f".*?{MOCK_SOURCE}/alpha/alpha.py:labtest_alpha_one\n"
            f".*?{MOCK_SOURCE}/alpha/alpha.py:labtest_alpha_two\n"
            f".*?{MOCK_SOURCE}/alpha/beta/beta.py:labtest_beta_one\n"
            f".*?{MOCK_SOURCE}/alpha/beta/beta.py:labtest_beta_two\n"
            f".*?{MOCK_SOURCE}/alpha/gamma/gamma.py:labtest_gamma_one\n"
            f".*?{MOCK_SOURCE}/alpha/gamma/gamma.py:labtest_gamma_two\n",
            captured.out,
        )


def test_subcommand_list_source_two_paths(monkeypatch, capsys):
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
                "list",
                "--source",
                f"{MOCK_SOURCE}/alpha/beta",
                "--source",
                f"{MOCK_SOURCE}/alpha/gamma",
            ],
        )
        labtest.labtest.main(registry=registry)
        captured = capsys.readouterr()
        assert re.fullmatch(
            f".*?{MOCK_SOURCE}/alpha/beta/beta.py:labtest_beta_one\n"
            f".*?{MOCK_SOURCE}/alpha/beta/beta.py:labtest_beta_two\n"
            f".*?{MOCK_SOURCE}/alpha/gamma/gamma.py:labtest_gamma_one\n"
            f".*?{MOCK_SOURCE}/alpha/gamma/gamma.py:labtest_gamma_two\n",
            captured.out,
        )
