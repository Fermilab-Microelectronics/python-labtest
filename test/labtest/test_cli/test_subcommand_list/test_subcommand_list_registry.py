import labtest
from labtest.labtest import main
from labtest.registry import Registry


def test_subcommand_list_registry_empty(mock_sys_argv, capsys):
    registry = Registry(is_singleton=False)
    with mock_sys_argv("main", "list"):
        main(registry=registry)
        captured = capsys.readouterr()
        assert "INFO: Did not find any registered functions" in captured.out


def test_subcommand_list_registry_one_entry(mock_sys_argv, capsys):
    registry = Registry(is_singleton=False)

    @labtest.register(registry)
    def mock_test_subcommand_list_registry_one_entry():
        """mock_test_subcommand_list_registry_one_entry"""

    with mock_sys_argv("main", "list"):
        main(registry=registry)
        captured = capsys.readouterr()
        assert (
            f"{__file__}:mock_test_subcommand_list_registry_one_entry\n" in captured.out
        )


def test_subcommand_list_registry_two_entries(mock_sys_argv, capsys):
    registry = Registry(is_singleton=False)

    @labtest.register(registry)
    def mock_test_subcommand_list_registry_two_entries_alpha():
        """mock_test_subcommand_list_registry_two_entries_alpha"""

    @labtest.register(registry)
    def mock_test_subcommand_list_registry_two_entries_beta():
        """mock_test_subcommand_list_registry_two_entries_beta"""

    with mock_sys_argv("main", "list"):
        main(registry=registry)
        captured = capsys.readouterr()
        assert (
            f"{__file__}:mock_test_subcommand_list_registry_two_entries_alpha\n"
            f"{__file__}:mock_test_subcommand_list_registry_two_entries_beta\n"
            in captured.out
        )


def test_subcommand_list_registry_singleton(mock_sys_argv, mock_registry, capsys):
    with mock_registry(), mock_sys_argv("main", "list"):

        @labtest.register
        def mock_test_subcommand_list_registry_singleton():
            """mock_test_subcommand_list_registry_one_entry"""

        main()
        captured = capsys.readouterr()
        assert (
            f"{__file__}:mock_test_subcommand_list_registry_singleton\n" in captured.out
        )
