# Django-select-menu
This project is for showing simple way how to make with Django a view where is template with select menu using Django models and forms. Main functions are described in `forms.py, views.py` and `models.py`. This is for you who want to learn little bit of Django and Bootstrap with it.

## How to install Django and this code?
At first you need to make sure, you have [Python](https://python.org) installed. I'm using here Python's own virtual environment. Go to directory you want to install this repository in your terminal (This is for Linux).

`$ cd [DIR]`
`$ python -m venv venv`
`$ . venv/bin/activate`
`$ pip install django django-bootstrap-v5`

Download and extract this code to this direcory. Then we need to create SQLITE database for this. It can be done using Django with the following way. Go first to the directory where is file `manage.py` and then:

`#Create Django models for the database`
`$ python manage.py makemigrations`

`#Create tables into database based on migrations`
`$ python manage.py migrate`

`#Create user for administrator site`
`$ python manage.py createsuperuser `

`#Run the server:`
`$ python manage.py runserver`

Then you can go with browser to `localhost:8000/admin/` (usually default for Django page) and add as meny projects as you like.
