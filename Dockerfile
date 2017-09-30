FROM python:2
ENV PYTHONUNBUFFERED 1
EXPOSE 8000
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install MySQL-python
RUN mkdir /code
WORKDIR /code
RUN rm -rf /root/.cache
ADD . /code/
ENV DJANGO_SETTINGS_MODULE=gp_cars.settings.local
RUN cd src && python manage.py test
CMD cd src && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
