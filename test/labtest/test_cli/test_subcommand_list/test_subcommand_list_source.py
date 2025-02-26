import pathlib

import labtest

MOCK_SOURCE_RELATIVE = "test/labtest/test_cli/mock_source"
MOCK_SOURCE_ABSOLUTE = pathlib.Path(__file__).parents[4] / MOCK_SOURCE_RELATIVE


def test_subcommand_list_source_empty(mock_sys_argv, mock_registry, capsys):
    with mock_registry(), mock_sys_argv("main", "list", "--source", "empty"):
        labtest.labtest.main()
        captured = capsys.readouterr()
        assert "INFO: Did not find any registered functions" in captured.out


def test_subcommand_list_source_one_path(mock_sys_argv, mock_registry, capsys):
    with (
        mock_registry(),
        mock_sys_argv("main", "list", "--source", f"{MOCK_SOURCE_RELATIVE}"),
    ):
        labtest.labtest.main()
        captured = capsys.readouterr()
        assert (
            f"{MOCK_SOURCE_ABSOLUTE}/alpha/alpha.py:labtest_alpha\n"
            f"{MOCK_SOURCE_ABSOLUTE}/alpha/beta/beta.py:labtest_beta_one\n"
            f"{MOCK_SOURCE_ABSOLUTE}/alpha/beta/beta.py:labtest_beta_two\n"
            f"{MOCK_SOURCE_ABSOLUTE}/alpha/gamma/gamma.py:labtest_gamma_one\n"
            f"{MOCK_SOURCE_ABSOLUTE}/alpha/gamma/gamma.py:labtest_gamma_two\n"
            in captured.out
        )


def test_subcommand_list_source_two_paths(mock_sys_argv, mock_registry, capsys):
    with (
        mock_registry(),
        mock_sys_argv(
            "main",
            "list",
            "--source",
            f"{MOCK_SOURCE_RELATIVE}/alpha/beta",
            "--source",
            f"{MOCK_SOURCE_RELATIVE}/alpha/gamma",
        ),
    ):
        labtest.labtest.main()
        captured = capsys.readouterr()
        assert (
            f"{MOCK_SOURCE_ABSOLUTE}/alpha/beta/beta.py:labtest_beta_one\n"
            f"{MOCK_SOURCE_ABSOLUTE}/alpha/beta/beta.py:labtest_beta_two\n"
            f"{MOCK_SOURCE_ABSOLUTE}/alpha/gamma/gamma.py:labtest_gamma_one\n"
            f"{MOCK_SOURCE_ABSOLUTE}/alpha/gamma/gamma.py:labtest_gamma_two\n"
            in captured.out
        )
