# Python API

PyShala can be used programmatically in Python applications.

## Quick Start

```python
from pyshala import run_app

run_app(
    lessons_path="/path/to/lessons",
    port=3000,
    backend_port=8000,
)
```

## API Reference

### run_app

Run the PyShala application.

```python
def run_app(
    lessons_path: str | None = None,
    port: int = 3000,
    backend_port: int = 8000,
    host: str = "0.0.0.0",
) -> None:
```

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `lessons_path` | str \| None | None | Path to lessons directory. Uses built-in lessons if None. |
| `port` | int | 3000 | Frontend port |
| `backend_port` | int | 8000 | Backend API port |
| `host` | str | "0.0.0.0" | Host address to bind |

**Example:**

```python
from pyshala import run_app

# Run with custom lessons
run_app(lessons_path="./my_lessons")

# Run with all options
run_app(
    lessons_path="/app/lessons",
    port=8080,
    backend_port=8001,
    host="127.0.0.1",
)
```

### get_lesson_loader

Get the lesson loader instance for accessing lesson data.

```python
from pyshala.services.lesson_loader import get_lesson_loader

loader = get_lesson_loader()
modules = loader.get_all_modules()
```

**Returns:** `LessonLoader` instance

### LessonLoader

Service for loading and accessing lessons.

```python
class LessonLoader:
    def get_all_modules(self) -> list[Module]:
        """Get all available modules."""

    def get_module(self, module_id: str) -> Module | None:
        """Get a specific module by ID."""

    def get_lesson(self, module_id: str, lesson_id: str) -> Lesson | None:
        """Get a specific lesson."""
```

**Example:**

```python
from pyshala.services.lesson_loader import get_lesson_loader

loader = get_lesson_loader()

# List all modules
for module in loader.get_all_modules():
    print(f"{module.name}: {len(module.lessons)} lessons")

# Get specific lesson
lesson = loader.get_lesson("python_basics", "01_hello_world")
if lesson:
    print(lesson.title)
    print(lesson.instructions)
```

### LocalExecutor

Execute Python code safely.

```python
from pyshala.services.local_executor import get_local_executor

executor = get_local_executor()
result = await executor.execute(
    code="print('Hello')",
    test_cases=[
        {"stdin": "", "expected_output": "Hello"}
    ]
)
```

**Example:**

```python
import asyncio
from pyshala.services.local_executor import get_local_executor

async def run_code():
    executor = get_local_executor()

    result = await executor.execute(
        code="x = int(input())\nprint(x * 2)",
        test_cases=[
            {
                "stdin": "5",
                "expected_output": "10",
                "description": "Doubles 5"
            }
        ],
        timeout=5.0
    )

    print(f"Passed: {result.passed}/{result.total}")
    for test in result.results:
        print(f"  {test.description}: {'PASS' if test.passed else 'FAIL'}")

asyncio.run(run_code())
```

## Data Models

### Module

```python
@dataclass
class Module:
    id: str
    name: str
    description: str
    order: int
    lessons: list[Lesson]
```

### Lesson

```python
@dataclass
class Lesson:
    id: str
    title: str
    description: str
    instructions: str
    order: int
    lesson_type: str  # "code" or "quiz"
    starter_code: str
    test_cases: list[TestCase]
    questions: list[Question]
    data_files: list[DataFile]
```

### TestCase

```python
@dataclass
class TestCase:
    stdin: str
    expected_output: str
    description: str
    hidden: bool
```

### Question

```python
@dataclass
class Question:
    id: str
    type: str  # "mcq" or "text"
    text: str
    options: list[QuestionOption]
    multi_select: bool
    correct: list[str]
```

## Integration Example

Embed PyShala in a larger application:

```python
import threading
from pyshala import run_app

def start_pyshala():
    """Run PyShala in a background thread."""
    run_app(
        lessons_path="./lessons",
        port=3000,
    )

# Start in background
thread = threading.Thread(target=start_pyshala, daemon=True)
thread.start()

# Your main application continues...
print("PyShala running at http://localhost:3000")
```
