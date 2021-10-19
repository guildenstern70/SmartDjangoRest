# SmartDjango REST edition

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Django REST template with support to JWT, Redoc and Swagger UI.
Template solution for Django Web App built with:

1. Django v.3+
2. Django Framework v.3+   
3. Bootstrap v.4+
4. SQLite
5. Spectacular

## Download required libraries

    pip install -r requirements.txt

## Install DB

    python manage.py createsuperuser --email admin@example.com --username admin
    python manage.py migrate
    python manage.py makemigrations smartdjangorest
    python manage.py migrate smartdjangorest
    python manage.py populate_db

## Explore URLs

    python manage.py installed_urls

## Run

    python manage.py runserver

## JWT

1. Add user using Django Admin interface
2. Get token using 

       curl -X 'POST' \
         'http://127.0.0.1:8000/api/v1/token/' \
         -H 'accept: application/json' \
         -d '{
         "username": "your_username",
         "password": "your_password"
       }'

3. 