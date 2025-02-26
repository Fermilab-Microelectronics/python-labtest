from labtest.registry import Registry


def test_registry_labtests_one_function():
    registry = Registry(is_singleton=False)

    def mock_test_registry_labtests_one_function():
        """mock function"""

    registry.register(mock_test_registry_labtests_one_function)
    assert len(registry.labtests) == 1
    assert sorted(registry.labtests) == [
        f"{__file__}:mock_test_registry_labtests_one_function"
    ]


def test_registry_labtests_two_functions():
    registry = Registry(is_singleton=False)

    def mock_test_registry_labtests_two_functions_alpha():
        """mock function"""

    def mock_test_registry_labtests_two_functions_beta():
        """mock function"""

    registry.register(mock_test_registry_labtests_two_functions_alpha)
    registry.register(mock_test_registry_labtests_two_functions_beta)
    assert len(registry.labtests) == 2
    assert sorted(registry.labtests) == [
        f"{__file__}:mock_test_registry_labtests_two_functions_alpha",
        f"{__file__}:mock_test_registry_labtests_two_functions_beta",
    ]


def test_registry_labtests_singleton(monkeypatch):
    registry = Registry(is_singleton=False)
    monkeypatch.setattr(Registry, "__new__", lambda *_: registry)

    def mock_test_registry_labtests_singleton():
        """mock function"""

    Registry().register(mock_test_registry_labtests_singleton)
    assert len(Registry().labtests) == 1
    assert sorted(Registry().labtests) == [
        f"{__file__}:mock_test_registry_labtests_singleton"
    ]

