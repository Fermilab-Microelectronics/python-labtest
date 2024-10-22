import pytest

from labtest.labtest import parse_args


# ruff: noqa: FIX002 TD003
# TODO(jeff): once python is upgraded past 3.7 fix this to use capsys
def test_parse_args_command_missing():
    with pytest.raises(TypeError):
        parse_args([])


def test_parse_args_command_bad(capsys):
    with pytest.raises(SystemExit) as e:
        parse_args(["bad"])
    captured = capsys.readouterr()
    assert "invalid choice:" in captured.err
    assert e.value.code == 2


def test_parse_args_help_run():
    with pytest.raises(SystemExit) as e:
        parse_args(["run", "-h"])
    assert e.value.code == 0


def test_parse_args_help_list():
    with pytest.raises(SystemExit) as e:
        parse_args(["list", "-h"])
    assert e.value.code == 0
