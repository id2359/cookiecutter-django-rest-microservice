#!/usr/bin/env sh

set -o errexit
set -o pipefail
set -o nounset


python /code/manage.py collectstatic --noinput
python /code/manage.py migrate
python /code/manage.py initialize
gunicorn config.wsgi -w 4 -b 0.0.0.0:5000 --chdir=/code --reload
