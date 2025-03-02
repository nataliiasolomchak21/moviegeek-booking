#!/bin/bash

# Ensure pip3 is available (install pip if needed)
python3 -m ensurepip --upgrade

# Install dependencies from requirements.txt
pip3 install -r requirements.txt

# Run collectstatic to gather static files
python3 manage.py collectstatic --noinput
