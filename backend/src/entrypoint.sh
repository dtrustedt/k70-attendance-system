#!/bin/bash

# Wait for Redis
until nc -z redis 6379; do
  echo "Waiting for Redis..."
  sleep 2
done

# Run database migrations
flask db upgrade

# Start Gunicorn with correct Python path
exec gunicorn --bind 0.0.0.0:5000 --pythonpath /app/src "app:create_app()"
