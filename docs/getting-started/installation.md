# Installation

## Requirements

- Python 3.10 or higher
- pip or uv package manager

## Install from PyPI

=== "pip"

    ```bash
    pip install pyshala
    ```

=== "uv"

    ```bash
    uv pip install pyshala
    ```

=== "pipx"

    ```bash
    pipx install pyshala
    ```

## Verify Installation

```bash
pyshala --version
```

## Install from Source

For development or to get the latest changes:

```bash
git clone https://github.com/dkedar7/pyshala.git
cd pyshala
pip install -e ".[dev]"
```

## Dependencies

PyShala automatically installs the following dependencies:

| Package | Purpose |
|---------|---------|
| `reflex` | Web framework |
| `reflex-monaco` | Code editor component |
| `pyyaml` | YAML parsing |
| `httpx` | HTTP client |
| `markdown` | Markdown rendering |

## Next Steps

- [Quick Start](quickstart.md) - Run PyShala and create your first lesson
