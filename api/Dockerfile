FROM python:alpine3.7

RUN pip install -r requirements.txt

WORKDIR /api

COPY . /api

EXPOSE 5000
CMD flask run --host=0.0.0.0

