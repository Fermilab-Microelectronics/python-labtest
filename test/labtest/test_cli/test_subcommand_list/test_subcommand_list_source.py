import pathlib
import sys

import labtest
from labtest.registry import Registry

MOCK_SOURCE_RELATIVE = "test/labtest/test_cli/mock_source"
MOCK_SOURCE_ABSOLUTE = pathlib.Path(__file__).parents[4] / MOCK_SOURCE_RELATIVE


def test_subcommand_list_source_empty(monkeypatch, capsys):
    class MockRegistry(Registry):
        pass

    monkeypatch.setattr(labtest.decorator, "Registry", MockRegistry)

    with monkeypatch.context() as m:
        m.setattr(sys, "argv", ["main", "list", "--source", "empty"])
        labtest.labtest.main()
        captured = capsys.readouterr()
        assert "INFO: Did not find any registered functions" in captured.out


def test_subcommand_list_source_one_path(monkeypatch, capsys):
    registry = Registry(is_singleton=False)

    class MockRegistry(Registry):
        def __new__(cls, *_):
            return registry

    monkeypatch.setattr(labtest.decorator, "Registry", MockRegistry)

    with monkeypatch.context() as m:
        m.setattr(sys, "argv", ["main", "list", "--source", f"{MOCK_SOURCE_RELATIVE}"])
        labtest.labtest.main(registry=registry)
        captured = capsys.readouterr()

        assert (
            f"{MOCK_SOURCE_ABSOLUTE}/alpha/alpha.py:labtest_alpha\n"
            f"{MOCK_SOURCE_ABSOLUTE}/alpha/beta/beta.py:labtest_beta_one\n"
            f"{MOCK_SOURCE_ABSOLUTE}/alpha/beta/beta.py:labtest_beta_two\n"
            f"{MOCK_SOURCE_ABSOLUTE}/alpha/gamma/gamma.py:labtest_gamma_one\n"
            f"{MOCK_SOURCE_ABSOLUTE}/alpha/gamma/gamma.py:labtest_gamma_two\n"
            in captured.out
        )


def test_subcommand_list_source_two_paths(monkeypatch, capsys):
    registry = Registry(is_singleton=False)

    class MockRegistry(Registry):
        def __new__(cls, *_):
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
                f"{MOCK_SOURCE_RELATIVE}/alpha/beta",
                "--source",
                f"{MOCK_SOURCE_RELATIVE}/alpha/gamma",
            ],
        )
        labtest.labtest.main(registry=registry)
        captured = capsys.readouterr()
        assert (
            f"{MOCK_SOURCE_ABSOLUTE}/alpha/beta/beta.py:labtest_beta_one\n"
            f"{MOCK_SOURCE_ABSOLUTE}/alpha/beta/beta.py:labtest_beta_two\n"
            f"{MOCK_SOURCE_ABSOLUTE}/alpha/gamma/gamma.py:labtest_gamma_one\n"
            f"{MOCK_SOURCE_ABSOLUTE}/alpha/gamma/gamma.py:labtest_gamma_two\n"
            in captured.out
        )
