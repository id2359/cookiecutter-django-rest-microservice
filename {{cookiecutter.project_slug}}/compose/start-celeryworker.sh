#!/usr/bin/env sh

set -o errexit
set -o pipefail
set -o nounset


python manage.py celery worker -l INFO
