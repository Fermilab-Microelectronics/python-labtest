"""This module provides the Registry class."""

from __future__ import annotations

import inspect
import os
from typing import TYPE_CHECKING

# ruff: noqa: ANN401
if TYPE_CHECKING:
    from collections.abc import Callable
    from typing import Any

    from typing_extensions import Self


class Registry:
    """A singleton class for managing lab tests.

    This class provides methods for registering and retrieving lab tests. Instead
    of registering the tests within a  global variable, the class constructor will
    permit only a single instance that manages the tests.
    """

    _instance: None | Self = None

    def __new__(cls, *, is_singleton: bool = True) -> Self | Registry:
        """Returns the singleton registry instance.

        Args:
            is_singleton: Controls whether to return the singleton instance or to
                create a new instance Defaults to True.

        Returns:
            Self: Return a registry instance

        """
        if is_singleton:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance
        else:
            return super().__new__(cls)

    def __init__(self, *, is_singleton: bool = True) -> None:
        """Initializes Registry with empty lab test registry.

        Args:
            is_singleton: Controls whether to return the singleton instance or to
                create a new instance Defaults to True.

        """
        self._is_singleton: bool = is_singleton
        if not hasattr(self, "labtest_funcs"):
            self.labtest_funcs: dict[str, Callable] = {}

    @property
    def labtests(self) -> list[str]:
        """Returns a list of the registered lab tests."""
        return list(self.labtest_funcs)

    @property
    def is_singleton(self) -> bool:
        """Returns whether instance is a singleton."""
        return self._is_singleton

    def register(self, func: Callable) -> Callable:
        """Registers a function as lab test.

        Args:
            func: Function to register a function as a lab test.

        Returns:
            Callable: Returns the registered function.

        Raises:
            ValueError: If function source file cannot be determined.

        """
        if sourcefile := inspect.getsourcefile(func):
            filename = os.path.realpath(sourcefile)
            self.labtest_funcs[f"{filename}:{func.__name__}"] = func
        else:  # pragma: no cover
            msg = f"Cannot find source file for {func.__name__}"
            raise ValueError(msg)
        return func

    def execute(self, name: str, *args: Any, **kwargs: Any) -> Any:
        """Executes a registered lab test.

        Args:
            name: The name of the registered lab test expressed as
                "<modeule_name>:<func_name>".
            *args: Positional arguments passed to the registered function.
            **kwargs: Keyword arguments passed to the registered function.

        Returns:
            Any: Returns the result of the function.

        Raises:
            ValueError: If name doesn't match a registered lab test.

        """
        if name in self.labtest_funcs:
            return self.labtest_funcs[name](*args, **kwargs)
        else:
            msg = f"Not a registered lab test: {name}"
            raise ValueError(msg)
