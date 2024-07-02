import argparse
import sys

from labtest.registry import Registry


def main():
    """CLI interface for executing registered labtest functions

    Raises:
        ValueError: If supplied labtest name is not a registered test name
    """
    args = parse_args(sys.argv[1:])
    Registry().execute(args.name, *args.args)


def parse_args(args):
    """Parsers the labtest CLI arguments

    Args:
        args (list): List of arguments to parse.

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
