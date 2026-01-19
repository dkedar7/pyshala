"""Tests for the PyShala CLI."""

import sys
from unittest.mock import patch, MagicMock

import pytest

from pyshala.cli import main


class TestCLI:
    """Tests for the CLI interface."""

    def test_version_flag(self, capsys):
        with patch.object(sys, "argv", ["pyshala", "--version"]):
            result = main()

        assert result == 0
        captured = capsys.readouterr()
        assert "pyshala" in captured.out
        assert "0.1.0" in captured.out

    def test_version_short_flag(self, capsys):
        with patch.object(sys, "argv", ["pyshala", "-v"]):
            result = main()

        assert result == 0
        captured = capsys.readouterr()
        assert "pyshala" in captured.out

    def test_invalid_lessons_path(self, capsys):
        with patch.object(sys, "argv", ["pyshala", "/nonexistent/path"]):
            result = main()

        assert result == 1
        captured = capsys.readouterr()
        assert "Error" in captured.err
        assert "does not exist" in captured.err

    def test_run_with_valid_path(self, tmp_path):
        lessons_dir = tmp_path / "lessons"
        lessons_dir.mkdir()

        with patch.object(sys, "argv", ["pyshala", str(lessons_dir)]):
            with patch("pyshala.cli.PyShala") as mock_pyshala:
                mock_app = MagicMock()
                mock_pyshala.return_value = mock_app

                result = main()

                assert result == 0
                mock_pyshala.assert_called_once()
                mock_app.run.assert_called_once_with(env=None)

    def test_custom_port(self, tmp_path):
        lessons_dir = tmp_path / "lessons"
        lessons_dir.mkdir()

        with patch.object(sys, "argv", ["pyshala", str(lessons_dir), "--port", "8080"]):
            with patch("pyshala.cli.PyShala") as mock_pyshala:
                mock_app = MagicMock()
                mock_pyshala.return_value = mock_app

                main()

                call_kwargs = mock_pyshala.call_args[1]
                assert call_kwargs["port"] == 8080

    def test_custom_host(self, tmp_path):
        lessons_dir = tmp_path / "lessons"
        lessons_dir.mkdir()

        with patch.object(sys, "argv", ["pyshala", str(lessons_dir), "--host", "127.0.0.1"]):
            with patch("pyshala.cli.PyShala") as mock_pyshala:
                mock_app = MagicMock()
                mock_pyshala.return_value = mock_app

                main()

                call_kwargs = mock_pyshala.call_args[1]
                assert call_kwargs["host"] == "127.0.0.1"

    def test_prod_env(self, tmp_path):
        lessons_dir = tmp_path / "lessons"
        lessons_dir.mkdir()

        with patch.object(sys, "argv", ["pyshala", str(lessons_dir), "--env", "prod"]):
            with patch("pyshala.cli.PyShala") as mock_pyshala:
                mock_app = MagicMock()
                mock_pyshala.return_value = mock_app

                main()

                mock_app.run.assert_called_once_with(env="prod")

    def test_all_options(self, tmp_path):
        lessons_dir = tmp_path / "lessons"
        lessons_dir.mkdir()

        with patch.object(sys, "argv", [
            "pyshala", str(lessons_dir),
            "--host", "127.0.0.1",
            "--port", "8080",
            "--backend-port", "9000",
            "--max-execution-time", "30.0",
            "--python-path", "/usr/bin/python3",
            "--loglevel", "debug",
        ]):
            with patch("pyshala.cli.PyShala") as mock_pyshala:
                mock_app = MagicMock()
                mock_pyshala.return_value = mock_app

                main()

                call_kwargs = mock_pyshala.call_args[1]
                assert call_kwargs["lessons_path"] == str(lessons_dir)
                assert call_kwargs["host"] == "127.0.0.1"
                assert call_kwargs["port"] == 8080
                assert call_kwargs["backend_port"] == 9000
                assert call_kwargs["max_execution_time"] == 30.0
                assert call_kwargs["python_path"] == "/usr/bin/python3"
                assert call_kwargs["loglevel"] == "debug"

    def test_keyboard_interrupt(self, tmp_path, capsys):
        lessons_dir = tmp_path / "lessons"
        lessons_dir.mkdir()

        with patch.object(sys, "argv", ["pyshala", str(lessons_dir)]):
            with patch("pyshala.cli.PyShala") as mock_pyshala:
                mock_app = MagicMock()
                mock_app.run.side_effect = KeyboardInterrupt()
                mock_pyshala.return_value = mock_app

                result = main()

                assert result == 0
                captured = capsys.readouterr()
                assert "Shutting down" in captured.out
