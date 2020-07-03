import os, json
from functools import wraps
from flask import Flask, Response, jsonify, request, make_response
from flask_cors import CORS, cross_origin
from firebase_admin import credentials, auth
from firebase_admin import firestore
import firebase_admin

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# Read env variables from config.py
app.config.from_object('config.Config')

cred = credentials.Certificate('key.json')
firebase = firebase_admin.initialize_app(cred)

db = firestore.client()

def check_token(f):
    """
    This decorator verifies user idToken for protected routes so that only valid idTokens may access them
    """
    @wraps(f)
    def wrap(*args, **kwargs):
        token = request.args.get('token')

        """
        Attempts to verify idToken and if successful then access to protected route is granted.
        Returns the appropriate error message.
        """
        try:
            auth.verify_id_token(token, check_revoked=True)

        except auth.ExpiredIdTokenError:
            return jsonify({'Error message':'Token expired'}),403

        except auth.InvalidIdTokenError:
            return jsonify({'Error message':'Invalid token'}),403

        except auth.RevokedIdTokenError:
            return jsonify({'Error message':'Token revoked'}),403

        except:
            return jsonify({'Error message':'Invalid Token'}),403

        return f(*args,**kwargs)
    return wrap

@app.route('/')
def home():
    return Response(response='success',status=200)

# Only accessible to auth users
# Example: /test?token=123456789
# Returns: idToken payload in json
@app.route('/test')
@check_token
def test():
    token = request.args.get('token')
    print("Token: ", token)
    decoded_token = auth.verify_id_token(token)
    print("Decoded Token: ", decoded_token)
    return decoded_token

@app.route('/tmdb',methods=['GET'])
@check_token
def tmdb():
    # Access API handler for TMDB
    # return shows user may be interested in
    return Response(response='success',status=200)

@app.route('/getUserShows',methods=['GET'])
@check_token
def getUserShows():
    """
    Retrieves all tv shows user is interested in from their shows collection on firestore
    """
    shows_list = []
    
    # get idToken
    token = request.args.get('token')

    # decode idToken
    decoded_token = auth.verify_id_token(token)
    uid = decoded_token['uid']

    # get all of the user's interested shows from firestore
    user_shows = db.collection('users').document(uid).collection('shows').stream()

    # Append all data into a list and return as json array
    # If user or data doesn't exist, an empty json array will be returned
    for show in user_shows:
        shows_list.append(show.to_dict())
 
    return jsonify(shows_list)


@app.route('/getUserMovies',methods=['GET'])
@check_token
def getUserMovies():
    """
    Retrieves all movies user is interested in from their movie collection on firestore
    """
    movies_list = []

    # get idToken
    token = request.args.get('token')

    # decode idToken
    decoded_token = auth.verify_id_token(token)
    uid = decoded_token['uid']

    # get all of the user's interested shows from firestore
    user_movies = db.collection('users').document(uid).collection('movies').stream()

    # Append all data into a list and return as json array
    # If user or data doesn't exist, an empty json array will be returned
    for movie in user_movies:
        movies_list.append(movie.to_dict())

    return jsonify(movies_list)

@app.route('/addUserShows',methods=['GET','POST'])
#@check_token
def addUserShows():
    data = request.get_json()
    title = data['title']
    
    # get idToken
    token = request.args.get('token')

    # decode idToken
    decoded_token = auth.verify_id_token(token)
    uid = decoded_token['uid']

    # add new show to user's firestore
    doc_ref = db.collection('users').document(uid).collection('shows').document(title)


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
    
    # verify that it was successfully added to firestore
    # return
    return Response(response='success',status=200)



def quickstart_add_data_two():
    uid = 'user2'
    # [START quickstart_add_data_two]
    doc_ref = db.collection('users').document(uid).collection('shows').document("movieName1")

    # Must be "" for valid json withour error
    doc_ref.set({
        "NameOfMovie":"The Lord of the Rings",
    }, merge=True)



#quickstart_add_data_two()
