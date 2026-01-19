# CLI Reference

PyShala provides a command-line interface for running the training platform.

## Basic Usage

```bash
pyshala [OPTIONS]
```

## Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--lessons` | PATH | Built-in | Path to lessons directory |
| `--port` | INT | 3000 | Frontend port |
| `--backend-port` | INT | 8000 | Backend API port |
| `--host` | TEXT | 0.0.0.0 | Host address to bind |
| `--version` | FLAG | - | Show version and exit |
| `--help` | FLAG | - | Show help and exit |

## Examples

### Run with Default Settings

```bash
pyshala
```

Opens at [http://localhost:3000](http://localhost:3000) with built-in sample lessons.

### Custom Lessons Directory

```bash
pyshala --lessons /path/to/my/lessons
```

### Custom Ports

```bash
pyshala --port 8080 --backend-port 8001
```

### Bind to Localhost Only

```bash
pyshala --host 127.0.0.1
```

### Production Deployment

```bash
pyshala --lessons /app/lessons --host 0.0.0.0 --port 80 --backend-port 8000
```

## Environment Variables

CLI options can also be set via environment variables:

| Variable | Equivalent Option |
|----------|-------------------|
| `LESSONS_PATH` | `--lessons` |
| `PYSHALA_CONFIG` | Path to config.yaml |

```bash
export LESSONS_PATH=/path/to/lessons
pyshala
```

## Exit Codes

| Code | Description |
|------|-------------|
| 0 | Success |
| 1 | Error (invalid options, missing files, etc.) |

## Logs

PyShala logs to stdout. Set log level via Reflex configuration.
