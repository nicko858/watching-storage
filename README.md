# Watching storage

This is a simple django-site for educational purposes to learn how to use [django-orm](https://docs.djangoproject.com/en/3.0/topics/db/).

## Prerequisites

- `python3` should already be installed.
- After getting access to the project database, create file `.env` in the `project` - directory and add the following records:

```bash
    DB_HOST=<database host>
    DB_PORT=<database port>
    DB_NAME=<database name>
    DB_USER=<database user>
    DB_PASSWORD=<database password>
    # True values are y, yes, t, true, on and 1;
    # false values are n, no, f, false, off and 0.
    DEBUG_LEVEL=<debug level for django>
```

## How to install

- `git clone https://github.com/nicko858/watching-storage.git`
- `cd watching-storage`
- `pip install -r requirements.txt`

## How to run

`python3 manage.py runserver 0.0.0.0:8000`

The site will be available at `http://localhost:8000`

## Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
