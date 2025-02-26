import pytest

from labtest.registry import Registry


def test_registry_execute_empty_registry():
    registry = Registry(is_singleton=False)
    with pytest.raises(ValueError, match=r"Not a registered lab test: .*"):
        registry.execute("name")


def test_registry_execute_no_args():
    def mock_test_registry_execute_no_args():
        return "mock_test_registry_execute_no_args"

    registry = Registry(is_singleton=False)
    registry.register(mock_test_registry_execute_no_args)
    assert (
        registry.execute(f"{__file__}:mock_test_registry_execute_no_args")
        == "mock_test_registry_execute_no_args"
    )


def test_registry_execute_with_args():
    def mock_test_registry_execute_with_args(*args):
        return args

    registry = Registry(is_singleton=False)
    registry.register(mock_test_registry_execute_with_args)
    assert registry.execute(
        f"{__file__}:mock_test_registry_execute_with_args", "a", "b"
    ) == ("a", "b")


def test_registry_execute_with_kwargs():
    def mock_test_registry_execute_with_kwargs(**kwargs):
        return kwargs

    registry = Registry(is_singleton=False)
    registry.register(mock_test_registry_execute_with_kwargs)
    assert registry.execute(
        f"{__file__}:mock_test_registry_execute_with_kwargs", a="a", b="b"
    ) == {"a": "a", "b": "b"}


def test_registry_execute_with_mixed_wargs():
    def mock_test_registry_execute_with_kwargs(*args, **kwargs):
        return (args, kwargs)

    registry = Registry(is_singleton=False)
    registry.register(mock_test_registry_execute_with_kwargs)
    assert registry.execute(
        f"{__file__}:mock_test_registry_execute_with_kwargs", "a", "b", c="c", d="d"
    ) == (("a", "b"), {"c": "c", "d": "d"})
