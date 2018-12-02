[![Build Status](https://travis-ci.org/DamianMcNulty/ecommerce.svg?branch=master)](https://travis-ci.org/DamianMcNulty/ecommerce)

1. python -m virtualenv env
2. .\env\Scripts\activate
3. pip install -r requirements.txt
4. django-admin startproject django_auth .
5. django-admin startapp accounts
6. python3 manage.py makemigrations
6. python manage.py migrate
7. python manage.py runserver
8. python manage.py createsuperuser
9. python manage.py collectstatic