FROM python:3.7

RUN useradd -ms /bin/bash django

USER django

ENV PYTHONUNBUFFERED 1

WORKDIR /home/django/eventors

ENV PATH $PATH:/home/django/.local/bin

COPY requirements.txt /home/django/eventors

RUN pip install -r requirements.txt

COPY . /home/django/eventors