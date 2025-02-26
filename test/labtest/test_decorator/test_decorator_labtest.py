from __future__ import annotations

from typing import TYPE_CHECKING

import labtest
from labtest.registry import Registry

if TYPE_CHECKING:
    import pytest


def test_decorator_labtest_one_function() -> None:
    registry = Registry(is_singleton=False)

    @labtest.register(registry)
    def mock_test_decorator_labtest_one_function() -> None:
        """mock function"""

    assert len(registry.labtests) == 1
    assert sorted(registry.labtests) == [
        f"{__file__}:mock_test_decorator_labtest_one_function"
    ]


def test_decorator_labtest_two_functions() -> None:
    registry = Registry(is_singleton=False)

    @labtest.register(registry)
    def mock_test_decorator_labtest_two_functions_alpha() -> None:
        """mock function"""

    @labtest.register(registry)
    def mock_test_decorator_labtest_two_functions_beta() -> None:
        """mock function"""

    assert len(registry.labtests) == 2
    assert sorted(registry.labtests) == [
        f"{__file__}:mock_test_decorator_labtest_two_functions_alpha",
        f"{__file__}:mock_test_decorator_labtest_two_functions_beta",
    ]


def test_decorator_labtest_no_argument(monkeypatch: pytest.MonkeyPatch) -> None:
    registry = Registry(is_singleton=False)
    monkeypatch.setattr(labtest.decorator.Registry, "__new__", lambda *_: registry)

    @labtest.register
    def mock_test_decorator_labtest_no_argument() -> None:
        """mock function"""

    assert len(registry.labtests) == 1
    assert sorted(registry.labtests) == [
        f"{__file__}:mock_test_decorator_labtest_no_argument"
    ]
