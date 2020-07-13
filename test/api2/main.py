from flask import Flask, jsonify
import requests
from flask_cors import CORS
import random

# movies = Blueprint('movies', __name__)
MAX_PAGE_NUMBER = 500

movies = Flask(__name__)
CORS(movies)
# movies.secret_key = r'Y\xf7\xec\xe3m\x99r\x19Acvc\x9d*l[\xdxcvcd\xa1\xf9\'

API_KEY = "30b80750bf23b8b0b21e102d46f16d72"
DEFAULT_OPTIONS = {
    "api_key": API_KEY,
    "language": "en-US",
    "sort_by": "popularity.desc"
}

MOVIE_RECCS_URL = "https://api.themoviedb.org/3/movie/{}/recommendations"
MOVIE_SIMS_URL = "https://api.themoviedb.org/3/movie/{}/similar"
MOVIE_DETAILS_URL = "https://api.themoviedb.org/3/movie/{}"

MOVIE_POPULAR_URL = "https://api.themoviedb.org/3/movie/popular"
MOVIE_DISCOVER_URL = "https://api.themoviedb.org/3/discover/movie"

MOVIE_NOW_PLAYING_URL = "https://api.themoviedb.org/3/movie/now_playing"
MOVIE_TOP_RATED_URL = "https://api.themoviedb.org/3/movie/top_rated"


GENRE_IDS_TO_NAME = {
    12: "Adventure",
    14: "Fantasy",
    16: "Animation",
    18: "Drama",
    27: "Horror",
    28: "Action",
    35: "Comedy",
    36: "History",
    37: "Western",
    53: "Thriller",
    80: "Crime",
    99: "Documentary",
    878: "Science Fiction",
    9648: "Mystery",
    10402: "Music",
    10749: "Romance",
    10751: "Family",
    10752: "War",
    10759: "Action & Adventure",
    10762: "Kids",
    10763: "News",
    10764: "Reality",
    10765: "Sci-Fi & Fantasy",
    10766: "Soaps",
    10767: "Talk",
    10768: "War & Politics",
    10770: "TV Movie"
}


@ movies.route("/movie/recommendations/<id>", methods=['GET'])
def get_movie_reccomendation(id):

    api_url = MOVIE_RECCS_URL

    req = requests.get(url=api_url.format(id), params={
                       "api_key": "30b80750bf23b8b0b21e102d46f16d72"})
    data = req.json()['results']

    return jsonify(data)


@ movies.route('/movie/similar/<id>', methods=['GET'])
def gwt_similar_movies(id):
    api_url = MOVIE_SIMS_URL
    id = str(id)

    req = requests.get(url=api_url.format(id), params={
                       "api_key": "30b80750bf23b8b0b21e102d46f16d72"})
    # print(req.json())
    data = req.json()["results"]
    print(data)

    return jsonify(data)


@ movies.route('/movie/<id>', methods=['GET'])
def get_movie_info(id):

    api_url = MOVIE_DETAILS_URL

    options = DEFAULT_OPTIONS.copy()

    req = requests.get(url=api_url.format(id), params=options)
    data = req.json()

    data['genres'] = [x['name'] for x in data['genres']]

    return jsonify(data)


@movies.route('/movie/cast/<id>', methods=['GET'])
def get_movie_cast(id):

    options = DEFAULT_OPTIONS.copy()
    api_url = f"https://api.themoviedb.org/3/movie/{id}/credits"

    response = requests.get(url=api_url, params=options)
    top_5_cast = (response.json()['cast'])[:5]

    items = []
    for cast in top_5_cast:
        cast_info = {}
        cast_info["character"] = cast["character"]
        cast_info["name"] = cast["name"]
        cast_info["profile_path"] = cast["profile_path"]
        items.append(cast_info)

    return jsonify(items)


@movies.route('/movie/oldest')
def get_oldest():

    options = DEFAULT_OPTIONS.copy()
    options["page"] = 1
    options["sort_by"] = "primary_release_date.asc"

    api_url = MOVIE_DISCOVER_URL

    response = requests.get(url=api_url, params=options)
    data = response.json()

    movies = data["results"]

    for movie in movies:
        movie["genre_ids"] = [(GENRE_IDS_TO_NAME[x])
                              for x in movie["genre_ids"]]
        movie["genres"] = movie.pop("genre_ids")

    return jsonify(movies)


@movies.route('/movie/latest')
def get_latest():

    options = DEFAULT_OPTIONS.copy()
    options["page"] = 1
    options["sort_by"] = "primary_release_date.desc"

    api_url = MOVIE_DISCOVER_URL

    response = requests.get(url=api_url, params=options)
    data = response.json()

    movies = data["results"]

    for movie in movies:
        movie["genre_ids"] = [(GENRE_IDS_TO_NAME[x])
                              for x in movie["genre_ids"]]
        movie["genres"] = movie.pop("genre_ids")

    return jsonify(movies)


@movies.route('/movie/now-playing')
def get_now_playing():

    options = DEFAULT_OPTIONS.copy()
    api_url = MOVIE_NOW_PLAYING_URL

    response = requests.get(url=api_url, params=options)

    movies = response.json()["results"]

    for movie in movies:
        movie["genre_ids"] = [(GENRE_IDS_TO_NAME[x])
                              for x in movie["genre_ids"]]
        movie["genres"] = movie.pop("genre_ids")

    return jsonify(movies)


@movies.route('/movie/popular', methods=['GET'])
def get_popular_movies():

    options = DEFAULT_OPTIONS.copy()
    api_url = MOVIE_POPULAR_URL

    response = requests.get(url=api_url, params=options)

    data = response.json()
    movies = data["results"]

    for movie in movies:
        movie["genre_ids"] = [(GENRE_IDS_TO_NAME[x])
                              for x in movie["genre_ids"]]
        movie["genres"] = movie.pop("genre_ids")

    return jsonify(movies)


@movies.route('/movie/unpopular', methods=['GET'])
def get_unpopular_movies():

    options = DEFAULT_OPTIONS.copy()
    api_url = MOVIE_DISCOVER_URL
    options["sort_by"] = "popularity.asc"

    response = requests.get(url=api_url, params=options)

    data = response.json()
    movies = data["results"]

    for movie in movies:
        movie["genre_ids"] = [(GENRE_IDS_TO_NAME[x])
                              for x in movie["genre_ids"]]
        movie["genres"] = movie.pop("genre_ids")

    return jsonify(movies)


@movies.route('/movie/ratings/worst', methods=['GET'])
def get_worst_rated_movies():

    options = DEFAULT_OPTIONS.copy()
    api_url = MOVIE_DISCOVER_URL
    options["sort_by"] = "vote_average.asc"
    options["vote_count.gte"] = 5000

    response = requests.get(url=api_url, params=options)

    data = response.json()
    movies = data["results"]

    for movie in movies:
        movie["genre_ids"] = [(GENRE_IDS_TO_NAME[x])
                              for x in movie["genre_ids"]]
        movie["genres"] = movie.pop("genre_ids")

    return jsonify(movies)


@movies.route('/movie/ratings/best', methods=['GET'])
def get_best_rated_movies():

    options = DEFAULT_OPTIONS.copy()
    api_url = MOVIE_TOP_RATED_URL

    response = requests.get(url=api_url, params=options)

    data = response.json()
    movies = data["results"]

    for movie in movies:
        movie["genre_ids"] = [(GENRE_IDS_TO_NAME[x])
                              for x in movie["genre_ids"]]
        movie["genres"] = movie.pop("genre_ids")

    return jsonify(movies)


@movies.route('/movie/random', methods=['GET'])
def get_random_movies():

    api_url = MOVIE_DISCOVER_URL

    sample_population = []

    for page_num in random.sample(range(MAX_PAGE_NUMBER), 20):
        options = DEFAULT_OPTIONS.copy()
        options["page"] = page_num

        response = requests.get(url=api_url, params=options)

        data = response.json()
        movies_set = data["results"]
        sample_population.extend(movies_set)

    movies = random.choices(sample_population, k=20)

    for movie in movies:
        movie["genre_ids"] = [(GENRE_IDS_TO_NAME[x])
                              for x in movie["genre_ids"]]
        if movie["genre_ids"]:
            movie["genres"] = movie.pop("genre_ids")

    return jsonify(movies)


movies.run(debug=True)
