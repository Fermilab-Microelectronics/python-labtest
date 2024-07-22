import sys

import pytest

import labtest
from labtest.labtest import main
from labtest.registry import Registry


def test_subcommand_list_registry_empty(monkeypatch, capsys):
    registry = Registry(is_singleton=False)

    with monkeypatch.context() as m:
        m.setattr(sys, "argv", ["main", "list"])
        main(registry=registry)
        captured = capsys.readouterr()
        assert "INFO: Did not find any registered functions" in captured.out


def test_subcommand_list_registry_one_entry(monkeypatch, capsys):
    assert 1 == 2


def test_subcommand_list_registry_two_entries(monkeypatch, capsys):
    assert 1 == 2
