FROM ubuntu:16.04

RUN apt-get update -y && apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /api/requirements.txt

WORKDIR /api

RUN pip install -r requirements.txt

COPY . /api

EXPOSE 5000

CMD flask run --host=0.0.0.0
