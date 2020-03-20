![Python application](https://github.com/Mubangizi/Epic-Mail-Backend/workflows/Python%20application/badge.svg?branch=develop)

# Epic-Mail-Backend
User mailing system

### Project Setup

Follow these steps to have a local running copy of the app.

##### Clone The Repo

`git clone https://github.com/Mubangizi/Epic-Mail-Backend.git`

If `master` is not up to date, `git checkout develop`. However, note that code on develop could be having some minor issues to sort.

##### Install PostgreSQL

Here's a great resource to check out:

[How To Install and Use PostgreSQL](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04)

Create the two databases `epicmail` (for development) and `epicmail_test_db` (for unit testing).

##### Create a Virtual Environment

App was developed with `Python 3.6`.

Make sure you have `pip` installed on your machine.

Install the dependencies.

`pip install -r requirements.txt`

Create a `.env` file (which defines the environment variables used) at the root of the app.

Add the following details, customizing as needed.

```
export FLASK_APP=server.py
export FLASK_ENV=development
export FLASK_DEBUG=1
export FLASK_RUN_PORT=5000
```

Activate the virtual environment.

`. venv/bin/activate`

Run the application.

`flask run`

##### Testing and Coverage

This app uses `pytest` to run tests.

`pytest`
