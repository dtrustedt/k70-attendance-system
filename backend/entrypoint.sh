#!/bin/bash

# Wait for Redis
while ! nc -z redis 6379; do
  echo "Waiting for Redis..."
  sleep 1
done

# Start Flask application
exec gunicorn --bind 0.0.0.0:5000 --workers 4 "src.app:create_app()"
