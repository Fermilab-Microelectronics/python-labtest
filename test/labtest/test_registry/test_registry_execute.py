from __future__ import annotations

import pytest

from labtest.registry import Registry


def test_registry_execute_empty_registry() -> None:
    registry = Registry(is_singleton=False)
    with pytest.raises(ValueError, match=r"Not a registered lab test: .*"):
        registry.execute("name")


def test_registry_execute_no_args() -> None:
    def func_no_args() -> None:
        pass

    registry = Registry(is_singleton=False)
    registry.register(func_no_args)
    assert registry.execute(f"{__file__}:func_no_args") is None


def test_registry_execute_with_args() -> None:
    def func_with_args(*args: str) -> tuple[str, ...]:
        return args

    registry = Registry(is_singleton=False)
    registry.register(func_with_args)
    assert registry.execute(f"{__file__}:func_with_args", "a", "b") == ("a", "b")


def test_registry_execute_with_kwargs() -> None:
    def func_with_kwargs(**kwargs: str) -> dict[str, str]:
        return kwargs

    registry = Registry(is_singleton=False)
    registry.register(func_with_kwargs)
    assert registry.execute(f"{__file__}:func_with_kwargs", a="a", b="b") == {
        "a": "a",
        "b": "b",
    }


def test_registry_execute_with_mixed_wargs() -> None:
    def func_with_kwargs(
        *args: str, **kwargs: str
    ) -> tuple[tuple[str, ...], dict[str, str]]:
        return (args, kwargs)

    registry = Registry(is_singleton=False)
    registry.register(func_with_kwargs)
    assert registry.execute(f"{__file__}:func_with_kwargs", "a", "b", c="c", d="d") == (
        ("a", "b"),
        {"c": "c", "d": "d"},
    )
