from __future__ import annotations

from labtest.registry import Registry


def test_registry_attribute_is_singleton_by_default() -> None:
    assert Registry().is_singleton is True


def test_registry_attribute_is_singleton_when_is_singleton_is_true() -> None:
    assert Registry(is_singleton=True).is_singleton is True


def test_registry_attribute_is_not_singleton_when_is_singleton_is_false() -> None:
    assert Registry(is_singleton=False).is_singleton is False


def test_registry_is_singleton_by_default() -> None:
    assert Registry() is Registry()
    assert Registry().is_singleton is True


def test_registry_is_singleton_when_is_singleton_is_true() -> None:
    assert Registry() is Registry(is_singleton=True)
    assert Registry(is_singleton=True).is_singleton is True


def test_registry_is_not_singleton_when_is_singleton_is_false() -> None:
    assert Registry() is not Registry(is_singleton=False)
    assert Registry(is_singleton=True) is not Registry(is_singleton=False)
    assert Registry(is_singleton=False) is not Registry(is_singleton=False)
    assert Registry(is_singleton=False).is_singleton is False
