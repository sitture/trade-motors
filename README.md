[![Python](https://img.shields.io/badge/Python-2.7-blue.svg?style=flat-square)](/)
[![Django](https://img.shields.io/badge/Django-1.8.2-blue.svg?style=flat-square)](/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/django_publications_bootstrap.svg?style=flat-square)](https://pypi.python.org/pypi/django-publications-bootstrap)

# trade-motors

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

### Install required packages ###

```bash
pip install -r requirements.txt
```

## Running the Django server locally ##

Once the above packages are installed successfully, you should then be able to run the django server.

To run the application locally, open the file `src/gp_cars/settings/local.py` and set `DEBUG` to `True`.

```bash
cd src
python manage.py runserver
```

## Running the Tests ##

From the `src` directory, run the below to execute tests.

```bash
python manage.py test
```
