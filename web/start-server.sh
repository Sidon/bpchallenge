#!/usr/bin/env bash

/etc/init.d/nginx start
gunicorn base_django.wsgi:application --user www-data --bind 0.0.0.0:8011 --error-logfile /var/log/gunicorn/errors --workers 3
