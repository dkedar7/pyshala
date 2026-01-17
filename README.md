# PyShala

A self-hosted interactive Python training platform for delivering custom lessons with live code execution and automated feedback.

## Features

- **Interactive Lessons**: Write and run Python code directly in the browser
- **Automated Testing**: Instant feedback with pass/fail results for each test case
- **Progress Tracking**: Track completed lessons across sessions
- **Custom Content**: Create your own lessons using simple YAML files
- **Data File Support**: Lessons can include CSV, JSON, and other data files
- **Self-Hosted**: Deploy on your own infrastructure with Docker

## Quick Start

### Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/dkedar7/pyshala.git
   cd pyshala
   ```

2. **Start Judge0 (code execution engine)**
   ```bash
   docker compose -f docker-compose.dev.yml up -d
   ```

3. **Install Python dependencies**
   ```bash
   pip install -e .
   ```

4. **Run the Reflex app**
   ```bash
   reflex run
   ```

5. **Open your browser** at http://localhost:3000

### Production Deployment

1. **Build and run with Docker Compose**
   ```bash
   docker compose up -d
   ```

2. **Access the app** at http://localhost:8080

## Creating Lessons

Lessons are defined using YAML files in the `lessons/` directory.

### Directory Structure

```
lessons/
├── python_basics/           # Module directory
│   ├── module.yaml          # Module metadata
│   ├── 01_hello_world.yaml  # Lesson file
│   ├── 02_variables.yaml
│   └── sales_data.csv       # Data file for lessons
└── control_flow/
    ├── module.yaml
    └── 01_if_statements.yaml
```

### Module Configuration (`module.yaml`)

```yaml
name: "Python Basics"
description: "Learn the fundamentals of Python programming"
order: 1

lessons:
  - 01_hello_world.yaml
  - 02_variables.yaml
```

### Lesson Configuration

```yaml
title: "Hello, World!"
description: "Write your first Python program"
order: 0

instructions: |
  # Hello, World!

  Use the `print()` function to display text.

  ## Your Task
  Print "Hello, World!"

starter_code: |
  # Write your code here

test_cases:
  - description: "Prints greeting"
    stdin: ""
    expected_output: "Hello, World!"

# Optional: include data files
data_files:
  - name: data.csv
    path: data.csv
```

### Test Case Options

| Field | Description |
|-------|-------------|
| `stdin` | Input provided to the program |
| `expected_output` | Expected stdout output |
| `description` | Test description shown to learner |
| `hidden` | If true, test details hidden from learner |

## Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `JUDGE0_URL` | `http://localhost:2358` | Judge0 API endpoint |
| `LESSONS_PATH` | `./lessons` | Path to lesson files |
| `DATABASE_PATH` | `./data/progress.db` | SQLite database path |
| `API_URL` | `http://localhost:8080` | Public Reflex API URL |
| `MAX_EXECUTION_TIME` | `10` | Max code execution time (seconds) |
| `MAX_MEMORY_KB` | `128000` | Max memory for code execution |

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    PyShala Container                     │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐ │
│  │   Caddy     │  │   Reflex    │  │  Lesson Loader  │ │
│  │   (Proxy)   │──│   Backend   │──│    (YAML)       │ │
│  └─────────────┘  └─────────────┘  └─────────────────┘ │
│         │                │                              │
│         │                ▼                              │
│         │        ┌─────────────┐                       │
│         │        │   SQLite    │                       │
│         │        │  (Progress) │                       │
│         │        └─────────────┘                       │
└─────────┼───────────────────────────────────────────────┘
          │
          ▼
┌─────────────────┐
│    Judge0 CE    │
│ (Code Execution)│
└─────────────────┘
```

## Tech Stack

- **Frontend/Backend**: [Reflex](https://reflex.dev) (Python)
- **Code Editor**: Monaco Editor via reflex-monaco
- **Code Execution**: [Judge0 CE](https://judge0.com)
- **Database**: SQLite (progress tracking)
- **Reverse Proxy**: Caddy

## License

MIT License - see [LICENSE](LICENSE) for details.
