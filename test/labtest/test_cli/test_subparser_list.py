import pytest

from labtest.labtest import parse_args


@pytest.fixture(name="parse_args_list")
def _parse_args_list():
    def __parse_args_list(args):
        return parse_args(["list"] + args)

    return __parse_args_list


def test_subparser_list_help(parse_args_list):
    with pytest.raises(SystemExit) as e:
        parse_args_list(["-h"])
    assert e.value.code == 0


def test_subparser_list_no_args(parse_args_list):
    parse_args_list([])


def test_subparser_list_source_one_path(parse_args_list):
    assert parse_args_list(["--source", "alpha"]).source == ["alpha"]


def test_subparser_list_source_two_paths(parse_args_list):
    assert parse_args_list(["--source", "alpha", "--source", "beta"]).source == [
        "alpha",
        "beta",
    ]
