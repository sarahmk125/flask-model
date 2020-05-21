 
FROM python:3.6-slim

MAINTAINER sarahmk125@gmail.com

USER root

WORKDIR /app

ADD . /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    apt-get update -yqq && \
    apt-get install curl zip unzip -yqq && \
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    export $(xargs < .env)

EXPOSE 5000

CMD flask run --host=0.0.0.0
