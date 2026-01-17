#!/bin/bash
set -e

echo "Starting PyShala..."

# Start Caddy in background
echo "Starting Caddy reverse proxy..."
caddy start --config /etc/caddy/Caddyfile &

# Wait for Caddy to be ready
sleep 2

# Start Reflex backend
echo "Starting Reflex backend..."
cd /app

# Run database migrations if needed (future use)
# python -m alembic upgrade head

# Start Reflex in production mode
exec reflex run --env prod --backend-only --loglevel info
