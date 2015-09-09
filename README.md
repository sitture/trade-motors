# Global Trade Motors #

## Prerequisites ##

+ `Python 2.7`
+ `pip` https://pypi.python.org/pypi/pip 

## Setting up the project ##

### Using a Virtual Environment (Recommended) ###

Create a virtual environment `trademotors` and activate.

```bash
pip install virtualenv
virtualenv trademotors
cd trademotors
source bin/activate
```

### Clone the repository

```bash
git clone git@gitlab.com:sitture/trade-motors.git .
```

### Install required packages ###

```bash
pip install -r requirements.txt
```

## Running the django ##

Once the above packages are installed successfully, you should then be able to run the django server.

```bash
cd src
python manage.py runserver
```

## Running the tests ##

From the `src` directory, run the below to execute tests.

```bash
python manage.py test
```