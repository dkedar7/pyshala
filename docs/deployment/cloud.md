# Cloud Deployment

Deploy PyShala to various cloud platforms.

## Railway

[Railway](https://railway.app) offers simple deployment from GitHub.

### Setup

1. Fork or push PyShala to your GitHub repo
2. Connect Railway to your GitHub
3. Create new project from repo
4. Set environment variables:
   - `LESSONS_PATH=/app/lessons`

### railway.json

```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "pyshala --port $PORT --host 0.0.0.0",
    "healthcheckPath": "/",
    "healthcheckTimeout": 100
  }
}
```

## Render

[Render](https://render.com) supports Docker and Python deployments.

### render.yaml

```yaml
services:
  - type: web
    name: pyshala
    env: python
    buildCommand: pip install pyshala
    startCommand: pyshala --port $PORT --host 0.0.0.0
    envVars:
      - key: LESSONS_PATH
        value: /app/lessons
```

## Fly.io

[Fly.io](https://fly.io) provides global edge deployment.

### fly.toml

```toml
app = "my-pyshala"
primary_region = "ord"

[build]
  builder = "paketobuildpacks/builder:base"

[env]
  LESSONS_PATH = "/app/lessons"

[http_service]
  internal_port = 3000
  force_https = true
  auto_stop_machines = true
  auto_start_machines = true

[[services]]
  internal_port = 8000
  protocol = "tcp"

  [[services.ports]]
    port = 8000
```

### Deploy

```bash
fly launch
fly deploy
```

## Google Cloud Run

### Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /app
RUN pip install pyshala

COPY lessons/ /app/lessons/

ENV LESSONS_PATH=/app/lessons

CMD exec pyshala --port $PORT --host 0.0.0.0
```

### Deploy

```bash
gcloud run deploy pyshala \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

## AWS

### Elastic Beanstalk

Create `Procfile`:

```
web: pyshala --port $PORT --host 0.0.0.0
```

Create `requirements.txt`:

```
pyshala
```

### ECS / Fargate

Use the Docker deployment with ECS task definitions.

## Azure

### App Service

Create `startup.txt`:

```bash
pyshala --port 8000 --host 0.0.0.0
```

Configure in Azure Portal:
- Runtime: Python 3.12
- Startup Command: `startup.txt`

## Heroku

### Procfile

```
web: pyshala --port $PORT --host 0.0.0.0
```

### Deploy

```bash
heroku create my-pyshala
git push heroku main
```

## Environment Variables

All platforms support environment variables:

| Variable | Description |
|----------|-------------|
| `LESSONS_PATH` | Path to lessons directory |
| `PYSHALA_CONFIG` | Path to config.yaml |
| `PORT` | Port (usually set by platform) |

## HTTPS

Most platforms provide automatic HTTPS. For custom domains:

1. Add custom domain in platform settings
2. Configure DNS CNAME record
3. Enable SSL/TLS certificate

## Scaling

### Horizontal Scaling

PyShala is stateless and can scale horizontally:

```yaml
# docker-compose with replicas
services:
  pyshala:
    deploy:
      replicas: 3
```

### Considerations

- Session state is per-browser (no server-side sessions)
- Code execution happens on the server
- Consider memory limits for concurrent executions
