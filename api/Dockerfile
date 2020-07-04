FROM python:3.7-slim

ENV FLASK_APP=main.py
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=localhost
ENV FLASK_RUN_PORT=5000

WORKDIR /api

COPY . ./

RUN pip install -r requirements.txt

#CMD flask run --host=0.0.0.0 --port=8080
CMD flask run

