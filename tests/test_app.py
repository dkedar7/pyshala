"""Tests for the PyShala application class."""

import sys
import tempfile
from pathlib import Path

import pytest

from pyshala import PyShala, create_app, __version__


class TestPyShalaInit:
    """Tests for PyShala initialization."""

    def test_default_initialization(self, tmp_path):
        # Create a lessons directory
        lessons_dir = tmp_path / "lessons"
        lessons_dir.mkdir()

        app = PyShala(lessons_path=str(lessons_dir))

        assert app.lessons_path == str(lessons_dir)
        assert app.host == "0.0.0.0"
        assert app.port == 3000
        assert app.backend_port == 8000
        assert app.max_execution_time == 10.0
        assert app.python_path == sys.executable
        assert app.loglevel == "info"

    def test_custom_configuration(self, tmp_path):
        lessons_dir = tmp_path / "lessons"
        lessons_dir.mkdir()

        app = PyShala(
            lessons_path=str(lessons_dir),
            host="127.0.0.1",
            port=8080,
            backend_port=9000,
            max_execution_time=30.0,
            python_path="/custom/python",
            loglevel="debug",
        )

        assert app.host == "127.0.0.1"
        assert app.port == 8080
        assert app.backend_port == 9000
        assert app.max_execution_time == 30.0
        assert app.python_path == "/custom/python"
        assert app.loglevel == "debug"

    def test_lessons_path_resolved(self, tmp_path):
        lessons_dir = tmp_path / "lessons"
        lessons_dir.mkdir()

        # Use relative-style path
        app = PyShala(lessons_path=str(lessons_dir))

        # Should be resolved to absolute path
        assert Path(app.lessons_path).is_absolute()

    def test_invalid_lessons_path_raises(self):
        with pytest.raises(ValueError, match="does not exist"):
            PyShala(lessons_path="/nonexistent/path/to/lessons")


class TestCreateApp:
    """Tests for the create_app convenience function."""

    def test_create_app_default(self, tmp_path):
        lessons_dir = tmp_path / "lessons"
        lessons_dir.mkdir()

        app = create_app(lessons_path=str(lessons_dir))

        assert isinstance(app, PyShala)
        assert app.lessons_path == str(lessons_dir)

    def test_create_app_with_kwargs(self, tmp_path):
        lessons_dir = tmp_path / "lessons"
        lessons_dir.mkdir()

        app = create_app(
            lessons_path=str(lessons_dir),
            port=8080,
            max_execution_time=20.0,
        )

        assert app.port == 8080
        assert app.max_execution_time == 20.0


class TestEnvironmentSetup:
    """Tests for environment variable setup."""

    def test_setup_environment(self, tmp_path):
        lessons_dir = tmp_path / "lessons"
        lessons_dir.mkdir()

        app = PyShala(
            lessons_path=str(lessons_dir),
            max_execution_time=15.0,
            python_path="/usr/bin/python3",
        )

        env = app._setup_environment()

        assert env["LESSONS_PATH"] == str(lessons_dir)
        assert env["MAX_EXECUTION_TIME"] == "15.0"
        assert env["PYTHON_PATH"] == "/usr/bin/python3"


class TestVersion:
    """Tests for package version."""

    def test_version_defined(self):
        assert __version__ is not None
        assert isinstance(__version__, str)

    def test_version_format(self):
        # Should be semver-like format
        parts = __version__.split(".")
        assert len(parts) >= 2
        assert all(part.isdigit() for part in parts[:2])
