import argparse
import sys
from typing import Callable, List

from labtest.registry import Registry


def main(*, registry: Registry = Registry()) -> Callable:
    """CLI interface for executing registered labtest functions

    Args:
        registry: Registry object used to register the labtests.

    Returns:
        Namespace: Returns arguments and argument values as namespace attributes.

    Raises:
        ValueError: If supplied labtest name is not a registered test name

    """
    args = parse_args(sys.argv[1:])
    return registry.execute(args.name, *args.args)


def parse_args(args: List[str]):
    """Parsers the labtest CLI arguments

    Args:
        args: List of arguments to parse.

    Returns:
        Namespace: Returns arguments and argument values as namespace attributes.

    Raises:
        ArgumentError: If supplied arguments are invalid.

    """
    parser = argparse.ArgumentParser(description="Command Line Interface")
    parser.add_argument("name", help="The labtest to execute")
    parser.add_argument(
        "args", nargs=argparse.REMAINDER, help="Arguments for the labtest"
    )
    return parser.parse_args(args)
