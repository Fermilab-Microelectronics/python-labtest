from typing import Callable

from labtest.registry import Registry


def register(registry: Registry = Registry()) -> Callable:
    """Decorator for registering functions as lab tests.

    Registered lab test are internally hashed using the following representation
    "<module_name>:<func_name>". The function and module names are extracted from
    the function using the inspect module.

    Args:
        registry: Registry object used to register lab test. Defaults to Registry().

    Returns:
        Callable: Returns the registered function
    """

    def inner_wrapper(func: Callable) -> Callable:
        """Inner wrapper for decorator a function.

        Registers the function with the registry provided by the parent function.

        Args:
            func: Function to decorate.

        Returns:
            Callable: Returns the registered function
        """
        return registry.register(func)

    return inner_wrapper
