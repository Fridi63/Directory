FROM python:3.8.10-slim

ENV PYTHONBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

COPY . .
