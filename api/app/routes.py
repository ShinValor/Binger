"""
The module for the Binger api endpoints.
"""
from gevent import monkey
monkey.patch_all(thread=False, select=False)

import os, sys, json
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
from firebase_admin import credentials, auth, firestore, initialize_app
from flask import session, jsonify, Response, request
from flask_cors import CORS, cross_origin
from functools import wraps

"""
Adds the utils package locations to the path to allow for portable import.
"""
path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(path, "utils"))

from app.utils import new_api_handler
from app.utils import recommendations
from app.utils import shows


cors = CORS(app, resources={r"/*": {"origins": "*"}})

cred = credentials.Certificate('key.json')
firebase_app = initialize_app(cred)
# firebase_app = initialize_app()
db = firestore.client()

def check_token(f):
    """
    This decorator verifies user idToken for protected routes so that only valid idTokens may access them
    """
    @wraps(f)
    def wrap(*args, **kwargs):
        """
        Receives idToken from the front-end and attempts to verify idToken and if successful, then access to protected route is granted.
        If the idToken is invalid for any reason whether it's expired or revoked, a corresponding error message is returned instead and access to protected route is denied.
        """

        token = request.args.get('token')
        try:
            auth.verify_id_token(token, check_revoked=True)

        except auth.ExpiredIdTokenError:
            return jsonify({'Error message': 'Token expired'}), 403

        except auth.InvalidIdTokenError:
            return jsonify({'Error message': 'Invalid token'}), 403

        except auth.RevokedIdTokenError:
            return jsonify({'Error message': 'Token revoked'}), 403

        except:
            return jsonify({'Error message': 'Invalid Token'}), 403

        return f(*args, **kwargs)
    return wrap


@app.route('/')
def index():
    """
    Index page.
    """
    return Response(response='success', status=200)


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
        # THIS IS A PLACEHOLDER A LIST OF IDS WILL NEED TO PASSED FROM THE FRONT.
        r.initialize_recommendations([18])

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


@app.route('/getUserShows', methods=['GET'])
@check_token
def get_user_shows():
    """
    Retrieves all shows from a certain user's firestore.
    User's identity is determined by their idToken which when decoded, provides the uid

    Note: Shows represents tv shows/movies for consistency with recommendation engine documentation
    """
    shows_list = []

    # get idToken
    token = request.args.get('token')

    # decode idToken
    decoded_token = auth.verify_id_token(token)
    uid = decoded_token['uid']

    # get all of the user's interested shows from firestore
    user_shows = db.collection('users').document(
        uid).collection('shows').stream()

    # Append all data into a list and return as json array
    # If user or data doesn't exist, an empty json array will be returned
    for show in user_shows:
        shows_list.append(show.to_dict())

    return jsonify(shows_list)


@app.route('/addUserShows', methods=['GET', 'POST'])
@check_token
def add_user_shows():
    """
    Add show into user's show collection in firestore
    User's identity is determined by their idToken which when decoded, provides the uid

    Note: Shows represents tv shows/movies for consistency with recommendation engine documentation
    """
    data = request.get_json()
    title = data['title']

    # get idToken
    token = request.args.get('token')

    # decode idToken
    decoded_token = auth.verify_id_token(token)
    uid = decoded_token['uid']

    # create a reference to a new document in the user's show collection
    doc_ref = db.collection('users').document(
        uid).collection('shows').document(title)

    # Add the tv show data to the new document
    doc_ref.set({
        "id": data['id'],
        "genres": data['genres'],
        "overview": data['overview'],
        "popularity": data['popularity'],
        "poster_path": data['poster_path'],
        "release_year": data['release_year'],
        "score": data['score'],
        "title": data['title'],
        "is_movie": data['is_movie']
    })

    return Response(response='success', status=200)


@app.route('/summary/<id>')
@check_token
def movie_summary(id):
    """
    When movie id is passed, the summary for the movie is returned
    """
    # get idToken
    token = request.args.get('token')

    # decode idToken
    decoded_token = auth.verify_id_token(token)
    uid = decoded_token['uid']

    my_show_data = shows.ShowData(id, popularity=0)
    show = new_api_handler.resolve_show(my_show_data)

    show_json_data = show.to_json()
    overview = json.loads(show_json_data)

    return overview["overview"]


# Requires optimization
@app.route('/topRated')
@check_token
def top_rated_show():
    """
    Retrieves the top 20 movie results from TMDB
    """
    # get idToken and pageNum
    token = request.args.get('token')
    page_num = request.args.get('page') if not request.args.get('page') else 1

    # decode idToken
    decoded_token = auth.verify_id_token(token)
    uid = decoded_token['uid']

    top_rated_shows = []
    json_list = []

    show = new_api_handler.get_top_rated_shows(page_num)
    for i in show:
        data = new_api_handler.resolve_show(i)
        json_data = data.to_json()
        a = json.loads(json_data)
        json_list.append(a)
    return jsonify(json_list)


# Requires optimization
@app.route('/worstRated')
@check_token
def worst_rated_show():
    """
    Retrieves the worst 20 movie results from TMDB
    """
    # get idToken
    token = request.args.get('token')
    page_num = request.args.get('page') if not request.args.get('page') else 1

    # decode idToken
    decoded_token = auth.verify_id_token(token)
    uid = decoded_token['uid']

    top_rated_shows = []
    json_list = []

    show = new_api_handler.get_worst_rated_shows(page_num)
    for i in show:
        data = new_api_handler.resolve_show(i)
        json_data = data.to_json()
        a = json.loads(json_data)
        json_list.append(a)
    return jsonify(json_list)


@app.route('/popular')
@check_token
def get_popular():
    """
    Retrieves the most popular movies from TMDB
    """
    # get idToken
    token = request.args.get('token')
    page_num = request.args.get('page') if not request.args.get('page') else 1

    # decode idToken
    decoded_token = auth.verify_id_token(token)
    uid = decoded_token['uid']

    json_list = []

    show = new_api_handler.get_popular_shows(page_num)
    for i in show:
        data = new_api_handler.resolve_show(i)
        json_data = data.to_json()
        json_list.append(json.loads(json_data))

    return jsonify(json_list)


@app.route('/unpopular')
@check_token
def get_unpopular():
    """
    Retrieves the least popular movies from TMDB
    """
    # get idToken
    token = request.args.get('token')
    page_num = request.args.get('page') if not request.args.get('page') else 1

    # decode idToken
    decoded_token = auth.verify_id_token(token)
    uid = decoded_token['uid']

    json_list = []

    show = new_api_handler.get_unpopular_shows(page_num)
    for i in show:
        data = new_api_handler.resolve_show(i)
        json_data = data.to_json()
        json_list.append(json.loads(json_data))

    return jsonify(json_list)


@app.route('/recent')
@check_token
def get_now_playing():
    """
    Retrieves movies now playing in theatres
    """
    # get idToken
    token = request.args.get('token')
    page_num = request.args.get('page') if not request.args.get('page') else 1

    # decode idToken
    decoded_token = auth.verify_id_token(token)
    uid = decoded_token['uid']

    movies = new_api_handler.get_now_playing_movies(page_num)
    movie_results = movies.json()["results"]
    return json.dumps(movie_results)


@app.route('/oldest')
@check_token
def get_oldest():
    """
    Retrieves the oldest movies from TMDB
    """
    # get idToken and requested page number
    token = request.args.get('token')
    page_num = request.args.get('page') if not request.args.get('page') else 1

    # decode idToken
    decoded_token = auth.verify_id_token(token)
    uid = decoded_token['uid']

    json_list = []

    show = new_api_handler.get_oldest_shows(page_num)
    for i in show:
        data = new_api_handler.resolve_show(i)
        json_data = data.to_json()
        json_list.append(json.loads(json_data))

    return jsonify(json_list)
