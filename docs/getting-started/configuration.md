# Configuration

## App Configuration

Customize the app by creating `config.yaml` in your lessons directory:

```yaml title="config.yaml"
# App identity
title: "My Python Course"
subtitle: "Learn Python Today"
description: "Interactive lessons with hands-on exercises"

# Navigation
about_url: "https://example.com"
about_text: "About Us"

# Branding (Lucide icon name)
icon: "book-open"
```

### Config Fields

| Field | Default | Description |
|-------|---------|-------------|
| `title` | "PyShala" | App name in navbar |
| `subtitle` | "Learn Python, One Lesson at a Time" | Home page heading |
| `description` | "Interactive lessons..." | Home page subtext |
| `about_url` | GitHub URL | About link URL |
| `about_text` | "About" | About link text |
| `icon` | "graduation-cap" | Navbar icon ([Lucide Icons](https://lucide.dev/icons)) |

### Config File Location

PyShala searches for `config.yaml` in this order:

1. Path in `PYSHALA_CONFIG` environment variable
2. `config.yaml` in the lessons directory
3. `config.yaml` in the current working directory
4. `lessons/config.yaml` relative to current directory

## Module Configuration

Each module folder should have a `module.yaml`:

```yaml title="module.yaml"
name: "Python Basics"
description: "Learn fundamental Python concepts"
order: 1

# Optional: explicit lesson ordering
lessons:
  - 01_hello_world.yaml
  - 02_variables.yaml
  - 03_data_types.yaml
  - 04_quiz.yaml
```

### Module Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Display name for the module |
| `description` | Yes | Brief description shown on module card |
| `order` | No | Sort order (default: 0) |
| `lessons` | No | Ordered list of lesson filenames |

!!! note "Lesson Ordering"
    If `lessons` is omitted, lessons are sorted alphabetically by filename. Use numeric prefixes (01_, 02_) for consistent ordering.

## Environment Variables

| Variable | Description |
|----------|-------------|
| `LESSONS_PATH` | Path to lessons directory |
| `PYSHALA_CONFIG` | Path to config.yaml |

### Example

```bash
export LESSONS_PATH=/path/to/lessons
export PYSHALA_CONFIG=/path/to/config.yaml
pyshala
```

## Directory Structure

Complete example structure:

```
lessons/
├── config.yaml                   # App configuration
├── python_basics/                # Module 1
│   ├── module.yaml
│   ├── 01_hello_world.yaml
│   ├── 02_variables.yaml
│   └── 05_basics_quiz.yaml
├── data_analysis/                # Module 2
│   ├── module.yaml
│   ├── 01_csv_basics.yaml
│   ├── sales.csv                 # Data file
│   └── 03_quiz.yaml
└── advanced/                     # Module 3
    ├── module.yaml
    └── 01_functions.yaml
```

## Next Steps

- [Code Lessons](../lessons/code-lessons.md) - Create coding exercises
- [Quiz Lessons](../lessons/quiz-lessons.md) - Add assessments
