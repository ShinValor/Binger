# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.7-slim

# Allow statements and log messages to immediately appear in the Knative logs
#ENV PYTHONUNBUFFERED True

# Expose port number
#ENV PORT 8080

# Copy local code to the container image.
#ENV APP_HOME /app
#WORKDIR $APP_HOME

#ENV FLASK_APP = main.py

# Comment out when deploying
#ENV FLASK_ENV=development
#ENV FLASK_RUN_HOST=localhost
#ENV FLASK_RUN_PORT=5000

WORKDIR /api

COPY . ./

# Install production dependencies.
RUN pip install -r requirements.txt

CMD flask run --host=0.0.0.0 --port=8080

