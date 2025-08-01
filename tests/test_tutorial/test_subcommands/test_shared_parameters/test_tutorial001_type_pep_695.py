import subprocess
import sys

from typer.testing import CliRunner

from docs_src.subcommands.shared_parameters import tutorial001_type_pep695 as mod

runner = CliRunner()


def test_help() -> None:
    result = runner.invoke(mod.app, ["--help"])
    assert result.exit_code == 0
    assert "Commands" in result.output
    assert "greet" in result.output
    assert "farewell" in result.output


def test_command_greet_help() -> None:
    result = runner.invoke(mod.app, ["greet", "--help"])
    assert result.exit_code == 0
    assert "Greet the user with their name and title." in result.output

def test_command_farewell_help() -> None:
    result = runner.invoke(mod.app, ["farewell", "--help"])
    assert result.exit_code == 0
    assert "Bid farewell to the user with their name and title." in result.output


def test_command_greet() -> None:
    result = runner.invoke(mod.app, ["greet", "Stark"])
    assert result.exit_code == 0
    assert "Hello, Mr Stark" in result.output

def test_command_greet_with_title() -> None:
    result = runner.invoke(mod.app, ["greet", "Strange", "--title", "Dr"])
    assert result.exit_code == 0
    assert "Hello, Dr Strange" in result.output

def test_command_farewell() -> None:
    result = runner.invoke(mod.app, ["farewell", "Stark"])
    assert result.exit_code == 0
    assert "Goodbye, Mr Stark" in result.output

def test_command_farewell_with_title() -> None:
    result = runner.invoke(mod.app, ["farewell", "Strange", "--title", "Dr"])
    assert result.exit_code == 0
    assert "Goodbye, Dr Strange" in result.output

def test_script() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, "--help"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
    )
    assert "Usage" in result.stdout
