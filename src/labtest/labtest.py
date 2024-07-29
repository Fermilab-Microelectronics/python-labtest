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
    return args.func(registry=registry, args=args)


def parse_args(args: List[str]):
    """Parsers the labtest CLI arguments

    Args:
        args: List of arguments to parse.

    Returns:
        Namespace: Returns arguments and argument values as namespace attributes.

    Raises:
        ArgumentError: If supplied arguments are invalid.

    """
    parser = argparse.ArgumentParser(
        description="Command line interface for running tests"
    )
    subparsers = parser.add_subparsers()
    subparsers.required = True

    _create_subparser_list(subparsers)
    _create_subparser_run(subparsers)

    return parser.parse_args(args)


def _create_subparser_run(subparsers) -> None:

    def _command_run(*, registry: Registry = Registry(), args) -> Callable:
        return registry.execute(args.name, *args.args)

    parser = subparsers.add_parser("run", help="run command help")
    parser.set_defaults(func=_command_run)
    parser.add_argument("name", help="Registered labtest to execute")
    parser.add_argument(
        "args", nargs=argparse.REMAINDER, help="Arguments for the labtest"
    )


def _create_subparser_list(subparsers) -> None:

    # pylint: disable-next=W0613
    def _command_list(*, registry: Registry = Registry(), args) -> None:
        for n in sorted(registry.labtests) or [
            "INFO: Did not find any registered functions"
        ]:
            print(n)

    parser = subparsers.add_parser("list", help="list command help")
    parser.set_defaults(func=_command_list)
