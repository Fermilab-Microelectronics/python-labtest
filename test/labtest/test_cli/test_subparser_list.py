import pytest

from labtest.labtest import parse_args


@pytest.fixture
def parse_args_list():
    def _parse_args_list(args):
        return parse_args(["list"] + args)

    return _parse_args_list


def test_subparser_list_help(parse_args_list):
    with pytest.raises(SystemExit) as e:
        parse_args_list(["-h"])
    assert e.value.code == 0


def test_subparser_list_no_args(parse_args_list):
    parse_args_list([])
