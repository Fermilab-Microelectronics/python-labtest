from __future__ import annotations

import inspect
from typing import Any, Callable, Dict, List, Union


class Registry:
    """A singleton class for managing lab tests.

    This class provides methods for registering and retrieving lab tests. Instead
    of registering the tests within a  global variable, the class constructor will
    permit only a single instance that manages the tests.
    """

    _instance: Union[None, Registry] = None

    def __new__(cls, *, is_singleton: bool = True) -> Registry:
        """Returns the singleton registry instance

        Args:
            is_singleton: Controls whether to return the singleton instance or to
                create a new instance Defaults to True.

        Returns:
            Registry: Return a registry instance

        """
        if is_singleton:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance
        else:
            return super().__new__(cls)

    def __init__(self, *, is_singleton: bool = True):
        """Initializes Registry with empty lab test registry"""
        self._is_singleton: bool = is_singleton
        if not hasattr(self, "labtest_funcs"):
            self.labtest_funcs: Dict[str, Callable] = {}

    @property
    def labtests(self) -> List[str]:
        """Returns a list of the registered lab tests."""
        return list(self.labtest_funcs)

    @property
    def is_singleton(self) -> bool:
        """Returns whether instance is a singleton."""
        return self._is_singleton

    def register(self, func: Callable) -> Callable:
        """Registers a function as lab test

        Args:
            func: Function to register a function as a lab test.

        """
        module = inspect.getmodule(func)
        if module:
            self.labtest_funcs[f"{module.__name__}:{func.__name__}"] = func
        return func

    def execute(self, name: str, *args: Any, **kwargs: Any) -> Callable:
        """Executes a registered lab test

        Args:
            name: The name of the registered lab test expressed as
                "<modeule_name>:<func_name>".

        Raises:
            ValueError: If name doesn't match a registered lab test.

        """
        if name in self.labtest_funcs:
            return self.labtest_funcs[name](*args, **kwargs)
        else:
            raise ValueError(f"Not a registered lab test: {name}")
