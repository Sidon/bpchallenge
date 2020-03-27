#!/usr/bin/env bash

python manage.py collectstatic
/etc/init.d/nginx start
gunicorn bpchallenge.wsgi:application --user www-data --bind 0.0.0.0:8011 --error-logfile /var/log/gunicorn/errors --workers 3
