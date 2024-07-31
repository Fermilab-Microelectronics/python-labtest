import argparse
import importlib.util
import os
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
    for p in args.source or []:
        _import_directory(p)
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
    for _, p in subparsers.choices.items():
        p.add_argument(
            "--source",
            help="Common top-level parameter",
            metavar="source",
            action="append",
            required=False,
        )

    return parser.parse_args(args)


def _create_subparser_run(subparsers) -> None:

    def _command_run(*, registry: Registry = Registry(), args) -> Callable:
        return registry.execute(args.name)

    parser = subparsers.add_parser("run", help="run command help")
    parser.set_defaults(func=_command_run)
    parser.add_argument("name", help="Registered labtest to execute")


def _create_subparser_list(subparsers) -> None:

    # pylint: disable-next=W0613
    def _command_list(*, registry: Registry = Registry(), args) -> None:
        for n in sorted(registry.labtests) or [
            "INFO: Did not find any registered functions"
        ]:
            print(n)

    parser = subparsers.add_parser("list", help="list command help")
    parser.set_defaults(func=_command_list)


def _import_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                module_name = os.path.split(file)[-1].strip(".py")
                module_path = os.path.join(root, file)
                module_spec = importlib.util.spec_from_file_location(
                    module_name, module_path
                )
                module = importlib.util.module_from_spec(module_spec)
                module_spec.loader.exec_module(module)

                globals()[module_name] = module
