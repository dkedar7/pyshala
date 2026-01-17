# PyShala Dockerfile
# Multi-stage build for production deployment

# ============================================
# Stage 1: Build the Reflex application
# ============================================
FROM python:3.12-slim AS builder

# Install build dependencies
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js (required for Reflex frontend build)
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY pyshala/ ./pyshala/
COPY rxconfig.py .

# Initialize Reflex and build frontend
RUN reflex init
RUN reflex export --frontend-only --no-zip

# Move built frontend to /srv
RUN mv .web/_static /srv/static

# ============================================
# Stage 2: Production runtime image
# ============================================
FROM python:3.12-slim

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Caddy for reverse proxy
RUN curl -L "https://github.com/caddyserver/caddy/releases/download/v2.8.4/caddy_2.8.4_linux_amd64.tar.gz" \
    | tar -xz -C /usr/local/bin caddy

# Set working directory
WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy application code
COPY --from=builder /app/pyshala ./pyshala
COPY --from=builder /app/rxconfig.py .
COPY --from=builder /app/.web ./.web

# Copy built frontend
COPY --from=builder /srv/static /srv/static

# Copy Caddyfile
COPY Caddyfile /etc/caddy/Caddyfile

# Create directories for data and lessons
RUN mkdir -p /data /lessons

# Environment variables
ENV PYTHONUNBUFFERED=1 \
    PORT=8080 \
    API_URL=http://localhost:8080 \
    JUDGE0_URL=http://judge0:2358 \
    LESSONS_PATH=/lessons \
    DATABASE_PATH=/data/progress.db

# Expose port
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/ || exit 1

# Start script
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
