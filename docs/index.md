# PyShala

**A self-hosted interactive Python training platform**

PyShala provides an interactive learning environment for Python with live code execution, automated testing, and quiz-based assessments.

| | |
|---|---|
| **Live Code Execution** | Execute Python code in real-time with instant feedback. No Docker required. |
| **Automated Testing** | Define test cases with expected outputs. Support for hidden tests and edge cases. |
| **Quiz Lessons** | Multiple choice and text-based questions with automatic grading. |
| **YAML Configuration** | Simple YAML files for lessons, modules, and app settings. |

## Quick Start

```bash
# Install PyShala
pip install pyshala

# Run with sample lessons
pyshala

# Or specify your own lessons
pyshala --lessons /path/to/lessons
```

## Features

- **Interactive Code Editor** - Monaco editor with syntax highlighting and auto-completion
- **Real-time Execution** - Execute Python code with instant feedback
- **Automated Testing** - Define test cases with expected outputs
- **Quiz Support** - MCQ (single/multi-select) and text questions
- **Progress Tracking** - Session-based progress tracking
- **Customizable** - Configure app title, branding, and navigation
- **Dark Mode** - Built-in light/dark theme support
- **Self-Hosted** - Run on your own infrastructure

## Use Cases

- **Teaching Python** - Create structured courses with progressive lessons
- **Training Programs** - Build internal training platforms for teams
- **Assessments** - Combine coding exercises with knowledge quizzes
- **Self-Learning** - Create personalized learning paths

## Next Steps

- [Installation](getting-started/installation.md) - Get PyShala running
- [Quick Start](getting-started/quickstart.md) - Create your first lesson
- [Writing Lessons](lessons/overview.md) - Learn the lesson format