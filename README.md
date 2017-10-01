# trade-motors [![Build Status](https://travis-ci.org/sitture/trade-motors.svg?branch=master&style=flat-square)](https://travis-ci.org/sitture/trade-motors) [![Django](https://img.shields.io/badge/django-1.8.2-blue.svg)](https://pypi.python.org/pypi/Django/1.8.2) [![django-appconf](https://img.shields.io/badge/django--appconf-1.0.1-blue.svg)](https://pypi.python.org/pypi/django-appconf/1.0.1) [![django-ckeditor](https://img.shields.io/badge/django--ckeditor-4.4.8-blue.svg)](https://pypi.python.org/pypi/django-ckeditor/4.4.8) [![django-crispy-forms](https://img.shields.io/badge/djang--cripsy--forms-1.5.1-blue.svg)](https://pypi.python.org/pypi/django-crispy-forms/1.5.1) [![django-dynamic-preferences](https://img.shields.io/badge/django--dynamic--preferences-0.5.4-blue.svg)](https://pypi.python.org/pypi/django-dynamic-preferences/0.5.4) [![django-imagekit](https://img.shields.io/badge/django--imagekit-3.2.6-blue.svg)](https://pypi.python.org/pypi/django-imagekit/3.2.6) [![django-registration](https://img.shields.io/badge/django--registration-1.0-blue.svg)](https://pypi.python.org/pypi/django-registration/1.0) [![pilkit](https://img.shields.io/badge/pilkit-1.1.12-blue.svg)](https://pypi.python.org/pypi/pilkit/1.1.12) [![Pillow](https://img.shields.io/badge/Pillow-2.8.2-blue.svg)](https://pypi.python.org/pypi/Pillow/2.8.2) [![requests](https://img.shields.io/badge/requests-2.7.0-blue.svg)](https://pypi.python.org/pypi/requests/2.7.0) [![selenium](https://img.shields.io/badge/selenium-2.47.1-blue.svg)](https://pypi.python.org/pypi/selenium/2.47.1) [![six](https://img.shields.io/badge/six-1.9.0-blue.svg)](https://pypi.python.org/pypi/six/1.9.0) [![South](https://img.shields.io/badge/South-1.0.2-blue.svg)](https://pypi.python.org/pypi/south/1.0.2) [![stripe](https://img.shields.io/badge/stripe-1.22.3-blue.svg)](https://pypi.python.org/pypi/stripe/1.22.3) [![wheel](https://img.shields.io/badge/wheel-0.24.0-blue.svg)](https://pypi.python.org/pypi/wheel/0.24.0)

A Django-based website for http://globaltrademotors.com

## Prerequisites

+ `Python 2.7`
+ `pip` https://pypi.python.org/pypi/pip

## Setting up the project

### Using a Virtual Environment (Recommended)

Create a virtual environment `trademotors` and activate.

```bash
pip install virtualenv
virtualenv trademotors
cd trademotors
source bin/activate
```

### Clone the repository

```bash
git clone git@github.com:sitture/trademotors.git .
```

### Install required packages

```bash
pip install -r requirements.txt
```

## Running the Django server locally

Once the above packages are installed successfully, you should then be able to run the django server.

To run the application locally, open the file `src/gp_cars/settings/local.py` and set `DEBUG` to `True`.

```bash
cd src
python manage.py runserver
```

## Running the Tests

From the `src` directory, run the below to execute tests.

```bash
python manage.py test
```

## Docker time
If you are comfortable using Docker, you can build this image, run it using sqlite inner database or run it using docker compose along with a MySQL server.

### Docker image
As you can imagine, the only command to build this image is:

```bash
docker build -t trade-motors:0.1.0 .
```

If the image fails on the building process, check out the log, could be failing tests.

Once the image is built, you can run it:

```bash
docker run -d -p 8000:8000 trade-motors:0.1.0
```

### Docker Compose
You can run this image using the `docker-compose.yml` file. Using it you can test this application with a MySQL Server configuration. In order to get this stack running locally:

```bash
docker-compose up -d
```

This stack uses a `.env` file containing the environment variables needed to run both web and database server.

# Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request
