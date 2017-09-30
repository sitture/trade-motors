FROM alpine:3.6

MAINTAINER Andres Julian Lopez <andres.julian.zgz@gmail.com>

RUN apk add --no-cache python py-pip gcc python-dev musl-dev

ADD . /opt/trade-motors/
WORKDIR /opt/trade-motors/
RUN pip install -r requirements.txt

ENTRYPOINT ["python","src/manage.py","runserver"]
