from flask import Flask, request, jsonify, Blueprint
import requests
from firebase_admin import credentials, firestore, initialize_app
recommendation_system = Blueprint('recommendation_system', __name__)


API_KEY = "30b80750bf23b8b0b21e102d46f16d72"
DEFAULT_OPTIONS = {
    "api_key": API_KEY,
    "language": "en-US",
    "sort_by": "popularity.desc"
}

MOVIE_RECCS_URL = "https://api.themoviedb.org/3/movie/{}/recommendations"
MOVIE_SIMS_URL = "https://api.themoviedb.org/3/movie/{}/similar"
MOVIE_DISCOVER_URL = "https://api.themoviedb.org/3/discover/movie"


# Initialize Firestore DB
default_app = initialize_app(credentials.Certificate('key.json'))
db = firestore.client(default_app)
db_ref = db.collection('recommendations')


@recommendation_system.route('/game/recommendation/intialize')
def intialize():
    # return "ok"
    user_uid = request.args.get('user_uid')
    genres = request.args.get('interested_genres')
    genres = genres.split(',')

    intial_movies = discover_requests(genres)[:5]

    new_dict = {str(x['id']): x for x in intial_movies}
    db_ref.document(user_uid).set(new_dict)

    # print(db_ref.document(user_uid).get().to_dict())
    return jsonify({"status": "Recomendation is intialized"}, new_dict)


@recommendation_system.route('/game/recommendation/reply')
def user_reply():
    # return "ok"
    user_uid = request.args.get('user_uid')
    movie_id = request.args.get('movie_id')
    movie_reply = request.args.get('movie_reply')

    if movie_reply == "like":

        current_recs = db_ref.document(user_uid).get().to_dict()
        print(current_recs)
        list_version = [current_recs[str(x)] for x in current_recs]
        x = TMDB_Recomendations(movie_id)
        list_version.extend(x[:5])

        freq = {}
        x = 0
        while x != len(list_version):
            movie = list_version[x]
            if movie['id'] in freq:
                freq[movie["id"]]['freq'] += 1
                list_version.pop(x)
                x -= 1
            else:
                freq[movie["id"]] = {'index': x, 'freq': 1}
            x += 1

        for x in list_version:
            if 'freq' not in x:
                x['freq'] = freq[x['id']]['freq']
            else:
                x['freq'] += freq[x['id']]['freq']

        list_version.sort(key=lambda movie: movie['popularity'], reverse=True)
        list_version.sort(key=lambda movie: movie['freq'], reverse=True)

        dict_version = {str(x['id']): x for x in list_version}
        db_ref.document(user_uid).set(dict_version)
        # return jsonify(list_version)
    else:
        pass
    return jsonify("ok")


@recommendation_system.route('/game/recommendation/request')
def user_request():

    user_uid = request.args.get('user_uid')

    current_recs = db_ref.document(user_uid).get().to_dict()
    list_version = [current_recs[str(x)] for x in current_recs]
    list_version.sort(key=lambda movie: movie['popularity'], reverse=True)
    list_version.sort(key=lambda movie: movie['freq'], reverse=True)

    to_send = list_version.pop(0)

    dict_version = {str(x['id']): x for x in list_version}
    db_ref.document(user_uid).set(dict_version)

    return jsonify(to_send)


def discover_requests(genre_ids, number_of_pages=3):

    genre = "|".join(map(str, genre_ids))
    discover_requests = []

    for page_num in range(1, number_of_pages + 1):
        options = DEFAULT_OPTIONS.copy()
        options["with_genres"] = genre
        options["page"] = page_num

        options["release_date.lte"] = "2020-06-01"
        options["release_date.gte"] = "1985-01-01"
        api_url = MOVIE_DISCOVER_URL

        res = requests.get(url=api_url, params=options)
        discover_requests.extend(res.json()['results'])

    return discover_requests


def TMDB_Recomendations(movie_id):
    tmdb_recs = []

    req = requests.get(url=MOVIE_RECCS_URL.format(movie_id), params=DEFAULT_OPTIONS)
    tmdb_recs.extend(req.json()['results'])
    req = requests.get(url=MOVIE_SIMS_URL.format(movie_id), params=DEFAULT_OPTIONS)
    tmdb_recs.extend(req.json()['results'])
    # print(tmdb_recs)
    return tmdb_recs
