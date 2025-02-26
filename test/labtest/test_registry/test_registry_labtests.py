from __future__ import annotations

from typing import TYPE_CHECKING

from labtest.registry import Registry

if TYPE_CHECKING:
    import pytest


def test_registry_labtests_one_function() -> None:
    registry = Registry(is_singleton=False)

    def mock_test_registry_labtests_one_function() -> None:
        """mock function"""

    registry.register(mock_test_registry_labtests_one_function)
    assert len(registry.labtests) == 1
    assert sorted(registry.labtests) == [
        f"{__file__}:mock_test_registry_labtests_one_function"
    ]


def test_registry_labtests_two_functions() -> None:
    registry = Registry(is_singleton=False)

    def mock_test_registry_labtests_two_functions_alpha() -> None:
        """mock function"""

    def mock_test_registry_labtests_two_functions_beta() -> None:
        """mock function"""

    registry.register(mock_test_registry_labtests_two_functions_alpha)
    registry.register(mock_test_registry_labtests_two_functions_beta)
    assert len(registry.labtests) == 2
    assert sorted(registry.labtests) == [
        f"{__file__}:mock_test_registry_labtests_two_functions_alpha",
        f"{__file__}:mock_test_registry_labtests_two_functions_beta",
    ]


def test_registry_labtests_singleton(monkeypatch: pytest.MonkeyPatch) -> None:
    registry = Registry(is_singleton=False)
    monkeypatch.setattr(Registry, "__new__", lambda *_: registry)

    def mock_test_registry_labtests_singleton() -> None:
        """mock function"""

    Registry().register(mock_test_registry_labtests_singleton)
    assert len(Registry().labtests) == 1
    assert sorted(Registry().labtests) == [
        f"{__file__}:mock_test_registry_labtests_singleton"
    ]
