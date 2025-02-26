import labtest
from labtest.registry import Registry


def test_decorator_labtest_one_function():
    registry = Registry(is_singleton=False)

    @labtest.register(registry)
    def mock_test_decorator_labtest_one_function():
        """mock function"""

    assert len(registry.labtests) == 1
    assert sorted(registry.labtests) == [
        f"{__file__}:mock_test_decorator_labtest_one_function"
    ]


def test_decorator_labtest_two_functions():
    registry = Registry(is_singleton=False)

    @labtest.register(registry)
    def mock_test_decorator_labtest_two_functions_alpha():
        """mock function"""

    @labtest.register(registry)
    def mock_test_decorator_labtest_two_functions_beta():
        """mock function"""

    assert len(registry.labtests) == 2
    assert sorted(registry.labtests) == [
        f"{__file__}:mock_test_decorator_labtest_two_functions_alpha",
        f"{__file__}:mock_test_decorator_labtest_two_functions_beta",
    ]


def test_decorator_labtest_no_argument(monkeypatch):
    registry = Registry(is_singleton=False)

    class MockRegistry(Registry):
        def __new__(cls, *_):
            return registry

    monkeypatch.setattr(labtest.decorator, "Registry", MockRegistry)

    @labtest.register
    def mock_test_decorator_labtest_no_argument():
        """mock function"""

    assert len(registry.labtests) == 1
    assert sorted(registry.labtests) == [
        f"{__file__}:mock_test_decorator_labtest_no_argument"
    ]
