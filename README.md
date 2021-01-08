## SmartDjango REST edition

A Django REST template.
Template solution for Django Web App with:

1. Django v.3+
2. Django Framework v.3+   
2. Bootstrap v.4+
3. SQLite

### Download required libraries

    pip install -r requirements.txt

### Install DB

    python manage.py createsuperuser --email admin@example.com --username admin
    python manage.py migrate
    python manage.py makemigrations smartdjangorest
    python manage.py migrate smartdjangorest
    python manage.py populate_db

### Run

    python manage.py runserver

