"""Tests for data models."""

import pytest

from pyshala.models.lesson import DataFile, Lesson, TestCase
from pyshala.models.module import Module


class TestTestCase:
    """Tests for TestCase model."""

    def test_from_dict(self):
        data = {
            "stdin": "5",
            "expected_output": "25",
            "description": "Square of 5",
            "hidden": True,
        }
        tc = TestCase.from_dict(data)
        assert tc.stdin == "5"
        assert tc.expected_output == "25"
        assert tc.description == "Square of 5"
        assert tc.hidden is True

    def test_from_dict_defaults(self):
        tc = TestCase.from_dict({})
        assert tc.stdin == ""
        assert tc.expected_output == ""
        assert tc.description == ""
        assert tc.hidden is False

    def test_to_dict(self):
        tc = TestCase(stdin="x", expected_output="y", description="test", hidden=True)
        data = tc.to_dict()
        assert data["stdin"] == "x"
        assert data["expected_output"] == "y"
        assert data["description"] == "test"
        assert data["hidden"] is True


class TestDataFile:
    """Tests for DataFile model."""

    def test_from_dict(self):
        data = {"name": "data.csv", "path": "files/data.csv"}
        df = DataFile.from_dict(data)
        assert df.name == "data.csv"
        assert df.path == "files/data.csv"
        assert df.content is None

    def test_to_dict(self):
        df = DataFile(name="test.json", path="test.json", content=b'{"a": 1}')
        data = df.to_dict()
        assert data["name"] == "test.json"
        assert data["path"] == "test.json"
        assert "content" not in data  # Content not serialized


class TestLesson:
    """Tests for Lesson model."""

    def test_from_dict(self):
        data = {
            "id": "lesson1",
            "title": "Intro",
            "description": "First lesson",
            "instructions": "# Hello",
            "starter_code": "print('hi')",
            "order": 1,
            "test_cases": [{"stdin": "", "expected_output": "hi"}],
        }
        lesson = Lesson.from_dict(data, module_id="mod1")
        assert lesson.id == "lesson1"
        assert lesson.title == "Intro"
        assert lesson.module_id == "mod1"
        assert lesson.order == 1
        assert len(lesson.test_cases) == 1
        assert lesson.test_cases[0].expected_output == "hi"

    def test_from_dict_defaults(self):
        lesson = Lesson.from_dict({})
        assert lesson.id == ""
        assert lesson.title == "Untitled Lesson"
        assert lesson.order == 0
        assert lesson.test_cases == []

    def test_to_dict(self):
        lesson = Lesson(
            id="l1",
            title="Test",
            description="desc",
            instructions="inst",
            starter_code="code",
            order=0,
            module_id="m1",
            test_cases=[TestCase(stdin="a", expected_output="b")],
        )
        data = lesson.to_dict()
        assert data["id"] == "l1"
        assert data["title"] == "Test"
        assert data["module_id"] == "m1"
        assert len(data["test_cases"]) == 1


class TestModule:
    """Tests for Module model."""

    def test_from_dict(self):
        data = {
            "name": "Python Basics",
            "description": "Learn Python",
            "order": 1,
            "lessons": ["01_intro.yaml", "02_vars.yaml"],
        }
        module = Module.from_dict(data, module_id="python_basics")
        assert module.id == "python_basics"
        assert module.name == "Python Basics"
        assert module.description == "Learn Python"
        assert module.order == 1
        assert module.lesson_files == ["01_intro.yaml", "02_vars.yaml"]

    def test_from_dict_defaults(self):
        module = Module.from_dict({}, module_id="test")
        assert module.id == "test"
        assert module.name == "Untitled Module"
        assert module.order == 0
        assert module.lesson_files == []

    def test_to_dict(self):
        lesson = Lesson(id="l1", title="Lesson 1")
        module = Module(
            id="m1",
            name="Module 1",
            description="desc",
            order=0,
            lessons=[lesson],
        )
        data = module.to_dict()
        assert data["id"] == "m1"
        assert data["name"] == "Module 1"
        assert data["lesson_count"] == 1
        assert len(data["lessons"]) == 1
