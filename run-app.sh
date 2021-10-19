#!/bin/bash
#
#
# Project SmartDjango REST
# Copyright (c) Alessio Saltarin 2021
# This software is licensed under MIT license
#
#

echo "building db..."
python manage.py migrate
python manage.py createsuperuser --noinput
echo "make migrations..."
python manage.py makemigrations smartdjangorest
echo "migrate..."
python manage.py migrate smartdjangorest
python manage.py populate_db
python manage.py collectstatic --noinput
echo [$0] Starting Django REST Server...
exec gunicorn -w 3 smartdjangorest.wsgi:application --bind 0.0.0.0:8080
