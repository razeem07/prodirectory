#!/bin/sh

# Wait for database to be ready
echo "Waiting for database..."
sleep 3

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start Gunicorn
gunicorn --bind 0.0.0.0:8000 core.wsgi:application