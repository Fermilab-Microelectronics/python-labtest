from __future__ import annotations

import sys
from contextlib import contextmanager
from typing import TYPE_CHECKING

import pytest

import labtest
from labtest.registry import Registry

if TYPE_CHECKING:
    from collections.abc import Callable, Generator


@pytest.fixture(name="mock_registry")
def _mock_registry(monkeypatch: pytest.MonkeyPatch) -> Callable:
    registry = Registry(is_singleton=False)

    @contextmanager
    def _mock_registry_context() -> Generator:
        with monkeypatch.context() as m:
            m.setattr(labtest.decorator.Registry, "__new__", lambda *_: registry)
            m.setattr(labtest.labtest.Registry, "__new__", lambda *_: registry)
            yield

    return _mock_registry_context


@pytest.fixture(name="mock_sys_argv")
def _mock_sys_argv(monkeypatch: pytest.MonkeyPatch) -> Callable:

    @contextmanager
    def _mock_sys_argv_context(*args: str) -> Generator:
        with monkeypatch.context() as m:
            m.setattr(sys, "argv", args)
            yield

    return _mock_sys_argv_context
