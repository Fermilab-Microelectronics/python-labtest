from __future__ import annotations

from labtest.registry import Registry


def test_registry_register_one_function() -> None:
    def mock_test_registry_register_one_function() -> None:
        """mock function"""

    registry = Registry(is_singleton=False)
    assert (
        registry.register(mock_test_registry_register_one_function)
        is mock_test_registry_register_one_function
    )


def test_registry_register_two_functions() -> None:
    def mock_test_registry_register_two_functions_alpha() -> None:
        """mock function"""

    def mock_test_registry_register_two_functions_beta() -> None:
        """mock function"""

    registry = Registry(is_singleton=False)
    assert (
        registry.register(mock_test_registry_register_two_functions_alpha)
        is mock_test_registry_register_two_functions_alpha
    )
    assert (
        registry.register(mock_test_registry_register_two_functions_beta)
        is mock_test_registry_register_two_functions_beta
    )
