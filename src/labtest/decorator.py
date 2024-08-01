from collections.abc import Callable
from typing import overload

from labtest.registry import Registry


@overload
def register(arg: Registry) -> Callable[[Callable], Callable]: ...


@overload
def register(arg: Callable) -> Callable: ...


def register(arg: Callable | Registry) -> Callable:
    """Decorator for registering functions as lab tests.

    Registered lab test are internally hashed using the following representation
    "<module_name>:<func_name>". The function and module names are extracted from
    the function using the inspect module.

    Args:
        arg: Either a registry object or the function to decorate.

    Returns:
        Callable: Returns the registered function

    Examples:
        The register decorator can be use both with and without a registry argument. In
        the case where the decorator is called without a registry argument, the default
        singleton registry is used.

            @labtest.register
            def labtest_func():
                ...


        In the case where a registry argument is supplied, the function is registered to
        the supplied registry object

            registry=Registry(is_singleton=False)
            @labtest.register
            def labtest_func():
                ...

    """
    if callable(arg):
        return register(Registry())(arg)

    def inner_wrapper(func: Callable) -> Callable:
        """Inner register wrapper for decorating a function.

        Registers the function with the registry provided by the parent function.

        Args:
            func: Function to decorate.

        Returns:
            Callable: Returns the registered function

        """
        return arg.register(func)

    return inner_wrapper
