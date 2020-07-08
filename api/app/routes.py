"""
The module for the Binger api endpoints.
"""

import os, sys
import jsonpickle as jp

from app import app
"""
====================================================================================
                            VARS NEEDED FOR AUTH AND FIRESTORE
vars from the app.__init__ file that contains vars needed for auth and firestore
from app import cors, cred, firebase_app
from firebase_admin import auth, firestore 
====================================================================================
"""
from flask import session, jsonify, Response
from functools import wraps

"""
Adds the utils package locations to the path to allow for portable import.
"""
path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(path, "utils"))

from app.utils import new_api_handler
from app.utils import recommendations
from app.utils import shows

@app.route('/')
def index():
    """
    Index page.
    """
    return Response(response='success',status=200)

@app.route('/init')
def initialize_queue():
    """
    Builds the recommendations based on the list of genres passed from the frontend.
    Will store the first item of the "RecommendationQueue" in 'session' so it can
    persist through requests. The rest of the queue will be sent to firebase for the duration
    of the users interaction with the "RecommendationQueue"
    """
    if "is_initialized" not in session:
        r = recommendations.RecommendationQueue()
        r.initialize_recommendations([18]) #THIS IS A PLACEHOLDER A LIST OF IDS WILL NEED TO PASSED FROM THE FRONT.
        
        session["recommendation"] = r.current_recommendation()
        session["is_initialized"] = True

        return Response(response='Created', status=201)
    
    return Response(response='Already created', status=204)

@app.route('/get_rec')
def get_recommendation():
    """
    The "ShowData" object that is stored in 'session' will be used to resolve to
    a "Show" object and returned as JSON.
    """
    if "recommendation" in session:
        show = new_api_handler.resolve_show((session["recommendation"]))
        return show.to_json(), 203

    return Response(response="Not Found", status=404)

@app.route('/clear')
def clear_session():
    """
    Clear session data from 'session' once the user has finished with their recommendations.
    """
    session.clear()
    return Response(response='OK', status=200)

