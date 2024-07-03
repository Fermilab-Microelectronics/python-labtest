import sys

import pytest

import labtest
from labtest.labtest import main
from labtest.registry import Registry


def test_main_test_name_bad(monkeypatch):
    registry = Registry(is_singleton=False)

    with monkeypatch.context() as m:
        m.setattr(sys, "argv", ["main", "name"])
        with pytest.raises(ValueError, match=r"Not a registered lab test: .*"):
            main(registry=registry)


def test_main_test_name_good(monkeypatch):
    registry = Registry(is_singleton=False)

    @labtest.register(registry)
    def mock_test_main_test_name_good():
        return mock_test_main_test_name_good

    with monkeypatch.context() as m:
        m.setattr(sys, "argv", ["main", f"{__name__}:mock_test_main_test_name_good"])
        assert main(registry=registry) is mock_test_main_test_name_good
