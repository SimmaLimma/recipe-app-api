FROM python:3.7-alpine
MAINTAINER Simon M

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# These lines were causing PermissionDenied error
#RUN adduser -D user
#USER user