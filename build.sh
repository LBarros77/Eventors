#!/usr/bin/env bash

set -o errexit  # exit on error

python3 -m pip install --user --upgrade pip
python3 -m pip install --user virtualenv

python3 -m venv .venv && source .venv/bin/activate

pip install -r requirements.txt

python3 manage.py collectstatic --no-input
python3 manage.py migrate

gunicorn umvenventos.wsgi