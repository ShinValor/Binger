FROM python:3.7-slim

RUN apt-get update -y && apt-get install -y python-pip python-dev

COPY ./requirements.txt /api/requirements.txt

WORKDIR /api

RUN pip install -r requirements.txt

COPY . /api

EXPOSE 5000

CMD flask run --host=0.0.0.0
