# Docker Deployment

Deploy PyShala using Docker for consistent, isolated environments.

## Quick Start

```bash
docker run -p 3000:3000 -v /path/to/lessons:/lessons ghcr.io/dkedar7/pyshala
```

## Dockerfile

Create a custom Dockerfile for your deployment:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

# Install PyShala
RUN pip install pyshala

# Copy your lessons
COPY lessons/ /app/lessons/

# Expose ports
EXPOSE 3000 8000

# Run
CMD ["pyshala", "--lessons", "/app/lessons", "--port", "3000", "--backend-port", "8000"]
```

## Docker Compose

For production deployments:

```yaml title="docker-compose.yml"
version: '3.8'

services:
  pyshala:
    build: .
    ports:
      - "3000:3000"
      - "8000:8000"
    volumes:
      - ./lessons:/app/lessons:ro
    environment:
      - LESSONS_PATH=/app/lessons
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000"]
      interval: 30s
      timeout: 10s
      retries: 3
```

Build and run:

```bash
docker-compose up -d
```

## Volume Mounts

### Read-Only Lessons

Mount lessons as read-only for security:

```bash
docker run -v /path/to/lessons:/lessons:ro pyshala
```

### Config File

Mount a custom config:

```bash
docker run \
  -v /path/to/lessons:/lessons \
  -v /path/to/config.yaml:/config.yaml \
  -e PYSHALA_CONFIG=/config.yaml \
  pyshala
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| `LESSONS_PATH` | Path to lessons directory |
| `PYSHALA_CONFIG` | Path to config.yaml |

```yaml title="docker-compose.yml"
services:
  pyshala:
    environment:
      - LESSONS_PATH=/app/lessons
      - PYSHALA_CONFIG=/app/config.yaml
```

## Resource Limits

Set resource limits for security:

```yaml title="docker-compose.yml"
services:
  pyshala:
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 2G
        reservations:
          cpus: '0.5'
          memory: 512M
```

## Networking

### Reverse Proxy with Nginx

```nginx title="nginx.conf"
upstream pyshala_frontend {
    server pyshala:3000;
}

upstream pyshala_backend {
    server pyshala:8000;
}

server {
    listen 80;
    server_name learn.example.com;

    location / {
        proxy_pass http://pyshala_frontend;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
    }

    location /api {
        proxy_pass http://pyshala_backend;
        proxy_set_header Host $host;
    }
}
```

### Docker Compose with Nginx

```yaml title="docker-compose.yml"
version: '3.8'

services:
  pyshala:
    build: .
    expose:
      - "3000"
      - "8000"
    volumes:
      - ./lessons:/app/lessons:ro

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/conf.d/default.conf:ro
    depends_on:
      - pyshala
```

## Security Considerations

1. **Read-only volumes** - Mount lessons as read-only
2. **Resource limits** - Prevent resource exhaustion
3. **Network isolation** - Use internal networks
4. **Non-root user** - Run as non-root inside container

```dockerfile
FROM python:3.12-slim

# Create non-root user
RUN useradd -m -u 1000 pyshala
USER pyshala

WORKDIR /app
RUN pip install --user pyshala

CMD ["python", "-m", "pyshala"]
```
