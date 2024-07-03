from labtest.registry import Registry


def test_registry_register_one_function():

    def mock_test_registry_register_one_function():
        """mock function"""

    registry = Registry(is_singleton=False)
    assert (
        registry.register(mock_test_registry_register_one_function)
        is mock_test_registry_register_one_function
    )


def test_registry_register_two_functions():

    def mock_test_registry_register_two_functions_alpha():
        """mock function"""

    def mock_test_registry_register_two_functions_beta():
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
