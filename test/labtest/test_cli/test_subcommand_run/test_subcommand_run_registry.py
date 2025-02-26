import pytest

import labtest
from labtest.labtest import main
from labtest.registry import Registry


def test_subcommand_run_name_bad(mock_sys_argv):
    registry = Registry(is_singleton=False)

    with (
        mock_sys_argv("main", "run", "name"),
        pytest.raises(ValueError, match=r"Not a registered lab test: .*"),
    ):
        main(registry=registry)


def test_subcommand_run_name_good(mock_sys_argv):
    registry = Registry(is_singleton=False)

    @labtest.register(registry)
    def mock_test_subcommand_run_name_good():
        return mock_test_subcommand_run_name_good

    with mock_sys_argv("main", "run", f"{__file__}:mock_test_subcommand_run_name_good"):
        assert main(registry=registry) is mock_test_subcommand_run_name_good


def test_subcommand_run_registry_singleton(mock_sys_argv, mock_registry):
    with (
        mock_registry(),
        mock_sys_argv(
            "main", "run", f"{__file__}:mock_test_subcommand_run_registry_singleton"
        ),
    ):

        @labtest.register
        def mock_test_subcommand_run_registry_singleton():
            return mock_test_subcommand_run_registry_singleton

        assert main() is mock_test_subcommand_run_registry_singleton
