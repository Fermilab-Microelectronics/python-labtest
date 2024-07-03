from labtest.labtest import parse_args


def test_parser_args_name():
    assert parse_args(["name"]).name == "name"


def test_parser_args_missing_name():
    assert parse_args([""]).name == ""


def test_parser_args_one_arg():
    assert parse_args(["name", "alpha"]).args == ["alpha"]


def test_parser_args_two_args():
    assert parse_args(["name", "alpha", "beta"]).args == ["alpha", "beta"]
