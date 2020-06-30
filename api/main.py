from flask import Flask, Response, jsonify, request, make_response
from functools import wraps
import os,json
from firebase_admin import credentials, auth
import firebase_admin

app = Flask(__name__)

#   Update fbconfig.json with group firebase 
cred = credentials.Certificate('fbconfig.json')
firebase = firebase_admin.initialize_app(cred)


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


#   Only accessible to auth users
#   Example: /test?token=123456789
#   Returns: idToken payload in json
@app.route('/test')
@check_token
def test():
    token = request.args.get('token')
    decoded_token = auth.verify_id_token(token)
    return decoded_token

@app.route('/tmdb')
@check_token
def tmdb():
    #   Access API handler for TMDB
    #   return shows user may be interested in


@app.route('/getUserShows')
@check_token
def getUserShows():
    #   get idToken
    #   decode idToken
    #   get all of the user's interested shows from firestore
    #   format the data into json
    #   return 

@app.route('addUserShows')
@check_token
def addUserShows():
    #   get idToken
    #   decode idToken
    #   add new show to user's firestore
    #   verify that it was successfully added to firestore
    #   return