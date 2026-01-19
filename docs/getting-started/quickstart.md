# Quick Start

## Run with Sample Lessons

PyShala includes sample lessons to get you started:

```bash
pyshala
```

Open your browser to [http://localhost:3000](http://localhost:3000) to see the app.

## CLI Options

```bash
pyshala --help
```

| Option | Default | Description |
|--------|---------|-------------|
| `--lessons` | Built-in | Path to lessons directory |
| `--port` | 3000 | Frontend port |
| `--backend-port` | 8000 | Backend port |
| `--host` | 0.0.0.0 | Host address |

### Examples

```bash
# Custom lessons directory
pyshala --lessons /path/to/my/lessons

# Custom ports
pyshala --port 8080 --backend-port 8001

# Bind to localhost only
pyshala --host 127.0.0.1
```

## Create Your First Lesson

### 1. Create Directory Structure

```
my-lessons/
├── config.yaml          # App configuration (optional)
└── python_basics/       # Module folder
    ├── module.yaml      # Module metadata
    └── 01_hello.yaml    # Lesson file
```

### 2. Create Module Configuration

```yaml title="python_basics/module.yaml"
name: "Python Basics"
description: "Learn fundamental Python concepts"
order: 1
```

### 3. Create a Code Lesson

```yaml title="python_basics/01_hello.yaml"
title: "Hello, World!"
description: "Your first Python program"
order: 0

instructions: |
  # Hello, World!

  Write a program that prints "Hello, World!"

  ## The print() Function

  In Python, use `print()` to display text:

  ```python
  print("Hello, World!")
  ```

  ## Your Task

  Print exactly: `Hello, World!`

starter_code: |
  # Write your code below


test_cases:
  - description: "Prints greeting"
    expected_output: "Hello, World!"
```

### 4. Run Your Lessons

```bash
pyshala --lessons my-lessons
```

## Using Python API

You can also run PyShala programmatically:

```python
from pyshala import run_app

run_app(
    lessons_path="/path/to/lessons",
    port=3000,
    backend_port=8000,
)
```

## Next Steps

- [Configuration](configuration.md) - Customize app settings
- [Code Lessons](../lessons/code-lessons.md) - Learn the full lesson format
- [Quiz Lessons](../lessons/quiz-lessons.md) - Add knowledge assessments
