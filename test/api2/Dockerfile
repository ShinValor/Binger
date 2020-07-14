FROM python:3.7-slim

ENV PORT 8080

WORKDIR /api

COPY . ./

RUN pip install -r requirements.txt

CMD flask run
