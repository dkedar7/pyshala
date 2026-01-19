#!/bin/bash
set -e

echo "Starting PyShala..."
echo "  Lessons: ${LESSONS_PATH:-/lessons}"
echo "  App Name: ${APP_NAME:-Learn Python}"

# Start Caddy in background
echo "Starting Caddy reverse proxy..."
caddy start --config /etc/caddy/Caddyfile &

# Wait for Caddy to be ready
sleep 2

# Start Reflex backend
echo "Starting Reflex backend..."
cd /app

# Start Reflex in production mode
exec reflex run --env prod --backend-only --loglevel info
