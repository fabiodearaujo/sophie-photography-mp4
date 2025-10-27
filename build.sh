#!/usr/bin/env bash
# Exit on error
set -o errexit

# Upgrade pip and install requirements
python3.11 -m pip install --upgrade pip
python3.11 -m pip install -r requirements.txt

# Collect static files
python3.11 manage.py collectstatic --noinput

# Apply database migrations
python3.11 manage.py migrate