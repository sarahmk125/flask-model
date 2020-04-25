 
FROM python:3.6-slim

MAINTAINER sarahmk125@gmail.com

USER root

WORKDIR /app

ADD . /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 5000

CMD flask run --host=0.0.0.0