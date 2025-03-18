#!/bin/bash
# celery-entrypoint.sh

until nc -z redis 6379; do
  echo "Waiting for Redis..."
  sleep 2
done

celery -A celery_worker.celery worker --loglevel=info
