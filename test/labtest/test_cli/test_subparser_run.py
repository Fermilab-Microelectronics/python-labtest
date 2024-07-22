import pytest

from labtest.labtest import parse_args


@pytest.fixture
def parse_args_run():
    def _parse_args_run(args):
        return parse_args(["run"] + args)

    return _parse_args_run


def test_subparser_run_command(parse_args_run):
    with pytest.raises(SystemExit) as e:
        parse_args_run(["-h"])
    assert e.value.code == 0


def test_subparser_run_name(parse_args_run):
    assert parse_args_run(["name"]).name == "name"


def test_subparser_run_missing_name(parse_args_run):
    assert parse_args_run([""]).name == ""


def test_subparser_run_one_arg(parse_args_run):
    assert parse_args_run(["name", "alpha"]).args == ["alpha"]


def test_subparser_run_two_args(parse_args_run):
    assert parse_args_run(["name", "alpha", "beta"]).args == ["alpha", "beta"]
