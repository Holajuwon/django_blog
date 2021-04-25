# Django Blog App

Introduction to django project with Zuri.

## Live Site

  - [Django Blog](https://django-blogappp.herokuapp.com/)


## Get started.

To run this project.

- First clone this project to your local environment.
- Create virtual environment with
  - `python3 -m venv env`
- Use the virtual environment with
  - `source env/bin/activate` (Operating System dependent)
- Install django
  - `python -m pip install django`
- Install all packages.
  - `python -m pip install -r requirements.txt`
- Run migration file to create database with
  - `python manage.py migrate`
- Add environmental variables to a `.env` file using the keys in `.env.example`
- Start development server with
  - `python manage.py runserver`
  - OR specify port with `python manage.py runserver <port>` e.g `python manage.py runserver 5000`
  - Default port is 8000

### Note

I didn't push all the files in the local repo which includes:

- The `vscode` folder that contains my workspace configuration.
- The `env` folder that conatins the virtual environment configuration I am using.
- The `db.sqlite3 `file which is the default SQLite database created after migration.
- The `*/__pycache__` folders.
- The `.env` file
