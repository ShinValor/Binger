FROM python:3.7-slim

COPY ./requirements.txt /api/requirements.txt

ENV API_HOME /api
ENV PORT 5000

WORKDIR /api

RUN pip install -r requirements.txt

COPY . /api

CMD flask run --host=0.0.0.0
