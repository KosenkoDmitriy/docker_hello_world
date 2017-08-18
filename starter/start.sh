#!/bin/bash
set +e
# Call collectstatic (customize the following line with the minimal environment variables needed for manage.py to run):
/venv/bin/python manage.py migrate --settings=${DJANGO_SETTINGS_MODULE} --noinput
/venv/bin/python manage.py collectstatic --settings=${DJANGO_SETTINGS_MODULE} --noinput

exec "$@"