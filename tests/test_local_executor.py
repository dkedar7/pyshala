"""Tests for the local Python executor."""

import pytest

from pyshala.models.lesson import DataFile
from pyshala.services.local_executor import (
    ExecutionResult,
    LocalExecutor,
    TestResult,
    TestRunResults,
)


class TestExecutionResult:
    """Tests for ExecutionResult dataclass."""

    def test_success_result(self):
        result = ExecutionResult(stdout="Hello", stderr="", return_code=0)
        assert result.is_success is True
        assert result.error_message == ""

    def test_error_result(self):
        result = ExecutionResult(stdout="", stderr="Error!", return_code=1)
        assert result.is_success is False
        assert result.error_message == "Error!"

    def test_timeout_result(self):
        result = ExecutionResult(timed_out=True, return_code=-1)
        assert result.is_success is False
        assert result.error_message == "Execution timed out"

    def test_nonzero_exit_without_stderr(self):
        result = ExecutionResult(stdout="", stderr="", return_code=1)
        assert result.is_success is False
        assert "exited with code 1" in result.error_message


class TestLocalExecutor:
    """Tests for LocalExecutor class."""

    @pytest.fixture
    def executor(self):
        return LocalExecutor(timeout=5.0)

    async def test_simple_execution(self, executor):
        result = await executor.execute("print('hello')")
        assert result.is_success
        assert result.stdout.strip() == "hello"

    async def test_execution_with_stdin(self, executor):
        code = "name = input()\nprint(f'Hello, {name}!')"
        result = await executor.execute(code, stdin="World")
        assert result.is_success
        assert result.stdout.strip() == "Hello, World!"

    async def test_syntax_error(self, executor):
        result = await executor.execute("print('hello'")
        assert not result.is_success
        assert "SyntaxError" in result.stderr

    async def test_runtime_error(self, executor):
        result = await executor.execute("raise ValueError('test error')")
        assert not result.is_success
        assert "ValueError" in result.stderr

    async def test_timeout(self):
        executor = LocalExecutor(timeout=0.5)
        result = await executor.execute("import time; time.sleep(10)")
        assert result.timed_out
        assert not result.is_success

    async def test_multiple_outputs(self, executor):
        code = "for i in range(3): print(i)"
        result = await executor.execute(code)
        assert result.is_success
        assert result.stdout.strip() == "0\n1\n2"


class TestRunTests:
    """Tests for the run_tests method."""

    @pytest.fixture
    def executor(self):
        return LocalExecutor(timeout=5.0)

    async def test_all_tests_pass(self, executor):
        code = "print(input())"
        test_cases = [
            {"stdin": "hello", "expected_output": "hello", "description": "Test 1"},
            {"stdin": "world", "expected_output": "world", "description": "Test 2"},
        ]
        results = await executor.run_tests(code, test_cases)
        assert results.all_passed
        assert results.passed_count == 2
        assert results.total_tests == 2

    async def test_some_tests_fail(self, executor):
        code = "print('hello')"
        test_cases = [
            {"stdin": "", "expected_output": "hello", "description": "Pass"},
            {"stdin": "", "expected_output": "world", "description": "Fail"},
        ]
        results = await executor.run_tests(code, test_cases)
        assert not results.all_passed
        assert results.passed_count == 1
        assert results.total_tests == 2

    async def test_whitespace_handling(self, executor):
        code = "print('hello')"
        test_cases = [
            {"stdin": "", "expected_output": "hello\n", "description": "Trailing newline"},
        ]
        results = await executor.run_tests(code, test_cases)
        assert results.all_passed

    async def test_hidden_test_case(self, executor):
        code = "print(input())"
        test_cases = [
            {"stdin": "secret", "expected_output": "secret", "hidden": True},
        ]
        results = await executor.run_tests(code, test_cases)
        assert results.all_passed
        assert results.test_results[0].hidden

    async def test_error_in_code(self, executor):
        code = "raise Exception('oops')"
        test_cases = [
            {"stdin": "", "expected_output": "", "description": "Should fail"},
        ]
        results = await executor.run_tests(code, test_cases)
        assert not results.all_passed
        assert "oops" in results.test_results[0].error_message

    async def test_with_data_file(self, executor):
        """Test execution with a data file (e.g., CSV)."""
        code = """
with open('data.csv') as f:
    lines = f.readlines()
    print(len(lines))
"""
        csv_content = b"name,value\nAlice,10\nBob,20\nCharlie,30\n"
        data_files = [DataFile(name="data.csv", path="data.csv", content=csv_content)]
        test_cases = [
            {"stdin": "", "expected_output": "4", "description": "Counts CSV lines"},
        ]
        results = await executor.run_tests(code, test_cases, data_files=data_files)
        assert results.all_passed

    async def test_with_data_file_binary_content(self, executor):
        """Test that binary file content is written correctly."""
        code = """
with open('test.txt', 'rb') as f:
    content = f.read()
    print(content.decode('utf-8').strip())
"""
        data_files = [DataFile(name="test.txt", path="test.txt", content=b"hello world")]
        result = await executor.execute(code, data_files=data_files)
        assert result.is_success
        assert result.stdout.strip() == "hello world"
