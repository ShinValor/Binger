from firebase_admin import credentials, initialize_app
from flask import Flask, Response, jsonify, request, make_response
from flask_cors import CORS, cross_origin

app = Flask(__name__)

from app import routes

app.config.from_object('config')