# Library management system

It is out final project for course 'Database Management Systems 2'.

Built in Python version 3.10.0, Django version 4.0.2.

## Our requirements

- Complexity and Completeness.

- Design(UI) and creativity.

- ERD.

- Functions and Procedures(at least 4).

- Cursor (at least 4).

- Triggers (at least 3).

## Installation

1. Clone this repository.

```bash
git clone git@github.com:dhucsik/library_django
```

2. Create virutal environment and install django.

3. All requirements for pip in requirements.txt file.

4. You have to change DATABASES dict in library>settings.py file.

- For 'NAME' you have to write your port and pluggable database which will connect to your app

- For 'USER' you have to write user which will connect to your pluggable database

- For 'PASSWORD' you have to write password by which user is identified.

5. 
``` bash
path> cd library
path\library> python manage.py runserver
```