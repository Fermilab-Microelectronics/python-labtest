"""This module creates the labtest CLI."""

from __future__ import annotations

import argparse
import importlib.util
import os
import sys
from importlib.abc import Loader
from importlib.machinery import ModuleSpec
from pathlib import Path
from typing import TYPE_CHECKING, cast

from labtest.registry import Registry

# ruff: noqa: ANN401
if TYPE_CHECKING:
    from argparse import Namespace as Args
    from collections.abc import Callable
    from typing import Any


def main(*, registry: Registry | None = None) -> Callable:
    """CLI interface for executing registered labtest functions.

    Args:
        registry: Registry object used to register the labtests. Defaults to singleton.

    Returns:
        Namespace: Returns arguments and argument values as namespace attributes.

    Raises:
        ValueError: If supplied labtest name is not a registered test name

    """
    if registry is None:
        registry = Registry()
    args = parse_args(sys.argv[1:])
    for p in args.source or []:
        _import_directory(p)
    return args.func(registry=registry, args=args)


def parse_args(args: list[str]) -> Args:
    """Parsers the labtest CLI arguments.

    Args:
        args: list of arguments to parse.

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
    _create_subparsers(subparsers)
    return parser.parse_args(args)


def _create_subparsers(subparsers: Any) -> None:
    _create_subparser_list(subparsers)
    _create_subparser_run(subparsers)
    for p in subparsers.choices.values():
        p.add_argument(
            "--source",
            help="Common top-level parameter",
            metavar="source",
            action="append",
            required=False,
        )


def _create_subparser_run(subparsers: Any) -> None:
    def _command_run(*, registry: Registry, args: Args) -> Callable:
        return registry.execute(args.name)

    parser = subparsers.add_parser("run", help="run command help")
    parser.set_defaults(func=_command_run)
    parser.add_argument("name", help="Registered labtest to execute")


def _create_subparser_list(subparsers: Any) -> None:
    def _command_list(
        *, registry: Registry, args: Args  # pylint: disable=W0613  # noqa: ARG001
    ) -> None:
        for n in sorted(registry.labtests) or [
            "INFO: Did not find any registered functions"
        ]:
            print(n)  # noqa: T201

    parser = subparsers.add_parser("list", help="list command help")
    parser.set_defaults(func=_command_list)


def _import_directory(directory: str) -> None:
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                module_name = os.path.split(file)[-1].strip(".py")
                module_path = Path(root) / file
                module_spec = cast(
                    ModuleSpec,
                    importlib.util.spec_from_file_location(module_name, module_path),
                )
                module = importlib.util.module_from_spec(module_spec)
                if isinstance(module_spec.loader, Loader):
                    module_spec.loader.exec_module(module)
                else:  # pragma: no cover
                    msg = f"Cannot import module from file {module_path}"
                    raise ValueError(msg)
