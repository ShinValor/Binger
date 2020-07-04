FROM python:3.7-slim

FLASK_APP=main.py
FLASK_ENV=development
FLASK_RUN_HOST=localhost
FLASK_RUN_PORT=5000

WORKDIR /api

COPY . ./

RUN pip install -r requirements.txt

#CMD flask run --host=0.0.0.0 --port=8080
CMD flask run

