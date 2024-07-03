"""
noxfile.py Configuration file for Nox
"""

# pylint: disable=import-error
import os

import nox

nox.options.reuse_existing_virtualenvs = True


@nox.session(tags=["check"])
def lint(session):
    """Runs lint checks"""
    session.install("-e", ".[dev]")
    session.run("black", "--check", "--diff", "--color", ".")
    session.run("isort", "--check", "--diff", "--color", "--profile", "black", ".")
    session.run("pylint", "src")
    session.run("mypy", "src", "test")


@nox.session(tags=["fix"])
def style(session):
    """Runs linters and fixers"""
    session.install("-e", ".[dev]")
    session.run("black", "--verbose", ".")
    session.run("isort", "--profile", "black", ".")


@nox.session(tags=["check"])
def test(session):
    """Runs tests"""
    session.install("-e", ".[dev]")
    session.run(
        "coverage", "run", "--source=src,test", "-m", "pytest", "-sv", *session.posargs
    )
    session.run("coverage", "report", "--fail-under=100", "--show-missing")


@nox.session(default=False)
def cli(session):
    """Runs CLI"""
    session.install("-e", ".[dev]")
    session.run(*session.posargs)
