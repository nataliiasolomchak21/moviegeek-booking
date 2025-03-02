#!/bin/bash
# Install system dependencies
apt-get update && apt-get install -y libcairo2-dev

# Install Python dependencies
pip install -r requirements.txt

# Apply database migrations
python3 manage.py migrate

# Collect static files
python3 manage.py collectstatic --noinput