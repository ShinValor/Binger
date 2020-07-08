from firebase_admin import credentials, initialize_app
from flask import Flask, Response, jsonify, request, make_response
from flask_cors import CORS, cross_origin
from flask_session import Session

app = Flask(__name__)

from app import routes

app.config.from_object('config')
"""
====================================================================================
                            VARS NEEDED FOR AUTH AND FIRESTORE
cors = CORS(app, resources={r"/*": {"origins": "*"}})
cred = credentials.Certificate('key.json')
firebase_app = initialize_app(cred)
====================================================================================
"""
Session(app)
