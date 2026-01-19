"""Tests for the lesson loader service."""

import tempfile
from pathlib import Path

import pytest
import yaml

from pyshala.services.lesson_loader import LessonLoader


@pytest.fixture
def temp_lessons_dir():
    """Create a temporary lessons directory with test content."""
    with tempfile.TemporaryDirectory() as tmpdir:
        lessons_path = Path(tmpdir)

        # Create a module directory
        module_dir = lessons_path / "python_basics"
        module_dir.mkdir()

        # Create module.yaml
        module_yaml = {
            "name": "Python Basics",
            "description": "Learn Python fundamentals",
            "order": 1,
            "lessons": ["01_hello.yaml", "02_variables.yaml"],
        }
        with open(module_dir / "module.yaml", "w") as f:
            yaml.dump(module_yaml, f)

        # Create lesson files
        lesson1 = {
            "title": "Hello World",
            "description": "Your first program",
            "instructions": "# Hello\nPrint hello world.",
            "starter_code": "# Write code here",
            "order": 0,
            "test_cases": [
                {"stdin": "", "expected_output": "Hello, World!", "description": "Basic test"}
            ],
        }
        with open(module_dir / "01_hello.yaml", "w") as f:
            yaml.dump(lesson1, f)

        lesson2 = {
            "title": "Variables",
            "description": "Learn about variables",
            "instructions": "# Variables\nStore data in variables.",
            "starter_code": "x = 5",
            "order": 1,
            "test_cases": [
                {"stdin": "10", "expected_output": "10", "description": "Echo input"}
            ],
        }
        with open(module_dir / "02_variables.yaml", "w") as f:
            yaml.dump(lesson2, f)

        yield lessons_path


@pytest.fixture
def loader(temp_lessons_dir):
    """Create a LessonLoader with the temp directory."""
    return LessonLoader(str(temp_lessons_dir))


class TestLessonLoader:
    """Tests for LessonLoader class."""

    def test_load_all(self, loader):
        modules = loader.load_all()
        assert len(modules) == 1
        assert modules[0].id == "python_basics"
        assert modules[0].name == "Python Basics"
        assert len(modules[0].lessons) == 2

    def test_get_module(self, loader):
        module = loader.get_module("python_basics")
        assert module is not None
        assert module.name == "Python Basics"
        assert module.description == "Learn Python fundamentals"

    def test_get_module_not_found(self, loader):
        module = loader.get_module("nonexistent")
        assert module is None

    def test_get_lesson(self, loader):
        lesson = loader.get_lesson("python_basics", "01_hello")
        assert lesson is not None
        assert lesson.title == "Hello World"
        assert lesson.description == "Your first program"
        assert len(lesson.test_cases) == 1

    def test_get_lesson_not_found(self, loader):
        lesson = loader.get_lesson("python_basics", "nonexistent")
        assert lesson is None

    def test_lesson_order(self, loader):
        module = loader.get_module("python_basics")
        assert module.lessons[0].id == "01_hello"
        assert module.lessons[1].id == "02_variables"

    def test_get_next_lesson(self, loader):
        next_lesson = loader.get_next_lesson("python_basics", "01_hello")
        assert next_lesson is not None
        assert next_lesson.id == "02_variables"

    def test_get_next_lesson_at_end(self, loader):
        next_lesson = loader.get_next_lesson("python_basics", "02_variables")
        assert next_lesson is None

    def test_get_previous_lesson(self, loader):
        prev_lesson = loader.get_previous_lesson("python_basics", "02_variables")
        assert prev_lesson is not None
        assert prev_lesson.id == "01_hello"

    def test_get_previous_lesson_at_start(self, loader):
        prev_lesson = loader.get_previous_lesson("python_basics", "01_hello")
        assert prev_lesson is None

    def test_get_all_modules(self, loader):
        modules = loader.get_all_modules()
        assert len(modules) == 1
        assert modules[0].id == "python_basics"


class TestLessonLoaderAutoDiscover:
    """Tests for auto-discovery when no lessons list is specified."""

    def test_auto_discover_lessons(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            lessons_path = Path(tmpdir)
            module_dir = lessons_path / "auto_module"
            module_dir.mkdir()

            # No module.yaml - should auto-create module from dir name
            # Create lessons without explicit order
            for name in ["03_third.yaml", "01_first.yaml", "02_second.yaml"]:
                lesson = {"title": name.replace(".yaml", "").replace("_", " ").title()}
                with open(module_dir / name, "w") as f:
                    yaml.dump(lesson, f)

            loader = LessonLoader(str(lessons_path))
            module = loader.get_module("auto_module")

            assert module is not None
            assert module.name == "Auto Module"  # Generated from dir name
            assert len(module.lessons) == 3


class TestLessonLoaderExternalInstructions:
    """Tests for loading instructions from external files."""

    def test_external_instructions_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            lessons_path = Path(tmpdir)
            module_dir = lessons_path / "test_module"
            module_dir.mkdir()

            # Create instructions markdown file
            instructions_content = "# External Instructions\n\nThis is loaded from a file."
            with open(module_dir / "instructions.md", "w") as f:
                f.write(instructions_content)

            # Create lesson referencing external instructions
            lesson = {
                "title": "Test Lesson",
                "instructions_file": "instructions.md",
                "test_cases": [],
            }
            with open(module_dir / "lesson.yaml", "w") as f:
                yaml.dump(lesson, f)

            loader = LessonLoader(str(lessons_path))
            loaded_lesson = loader.get_lesson("test_module", "lesson")

            assert loaded_lesson is not None
            assert "External Instructions" in loaded_lesson.instructions
            assert "loaded from a file" in loaded_lesson.instructions
