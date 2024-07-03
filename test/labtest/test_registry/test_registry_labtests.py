from labtest.registry import Registry


def test_registry_labtests_one_function():

    def mock_test_registry_labtests_one_function():
        """mock function"""

    registry = Registry(is_singleton=False)
    registry.register(mock_test_registry_labtests_one_function)
    assert len(registry.labtests) == 1
    assert sorted(registry.labtests) == [
        f"{__name__}:mock_test_registry_labtests_one_function",
    ]


def test_registry_labtests_two_functions():

    def mock_test_registry_labtests_two_functions_alpha():
        """mock function"""

    def mock_test_registry_labtests_two_functions_beta():
        """mock function"""

    registry = Registry(is_singleton=False)
    registry.register(mock_test_registry_labtests_two_functions_alpha)
    registry.register(mock_test_registry_labtests_two_functions_beta)
    assert len(registry.labtests) == 2
    assert sorted(registry.labtests) == [
        f"{__name__}:mock_test_registry_labtests_two_functions_alpha",
        f"{__name__}:mock_test_registry_labtests_two_functions_beta",
    ]
