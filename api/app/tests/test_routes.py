import os
import json
import pytest
import requests


url = 'http://localhost:5000'
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

def test_home():
    response = requests.get(url + '/')
    assert response.status_code == 200
    assert response.text == 'success'

"""
def test_initialize_queue():
    response = requests.get(url + '/init')
    assert response.status_code == 201


def test_get_recommendation():
    assert response.get(url + '/get_rec')
    assert response.status_code == 203


def test_clear_session():
    response = requests.get(url + '/clear')
    assert response.status_code == 200
    assert response.text == 'OK'
"""

def test_movie_summary(id = 657):
    idToken = sign_in_with_email_and_password()

    response = requests.get(url + f"/summary/{id}" + f"?token={idToken}")
    assert response.status_code == 200
    assert response.text == movie_summary_json()

def test_top_rated_show():
    idToken = sign_in_with_email_and_password()

    response = requests.get(url + '/topRated' + f"?token={idToken}")
    assert response.status_code == 200
    assert response.json() == top_rated_json()


def test_worst_rated_show():
    idToken = sign_in_with_email_and_password()
    response = requests.get(url + '/worstRated' + f"?token={idToken}")
    assert response.status_code == 200


def test_get_popular():
    idToken = sign_in_with_email_and_password()

    response = requests.get(url + '/popular' + f"?token={idToken}")
    assert response.status_code == 200


def test_get_unpopular():
    idToken = sign_in_with_email_and_password()

    response = requests.get(url + '/unpopular' + f"?token={idToken}")
    assert response.status_code == 200


def test_get_now_playing():
    idToken = sign_in_with_email_and_password()

    response = requests.get(url + '/recent' + f"?token={idToken}")
    assert response.status_code == 200


def test_get_oldest():
    idToken = sign_in_with_email_and_password()

    response = requests.get(url + '/oldest' + f"?token={idToken}")
    assert response.status_code == 200


def test_top():
    print(top_rated_json())


def sign_in_with_email_and_password():
    """
    This function is for creating an idToken for an existing Binger account 
    to test the protected routes through Pytest
    """
    email = os.environ.get('email')
    password = os.environ.get('password')
    api_key = os.environ.get('binger_api_key')
    request_ref = f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={api_key}"
    headers = {"content-type": "application/json; charset=UTF-8"}
    data = json.dumps({"email": email, "password": password, "returnSecureToken": True})
    request_object = requests.post(request_ref, headers=headers, data=data)
    return request_object.json()['idToken']


def refresh(refresh_token):
    """
    This function uses the refresh token to recreate a new idToken
    """
    api_key = os.environ.get('binger_api_key')
    request_ref = f"https://securetoken.googleapis.com/v1/token?key={api_key}"
    headers = {"content-type":"application/json; charset=UTF-8"}
    data = json.dumps({"grant_type":"refresh_token", "refresh_token":refresh_token})
    request_object = requests.post(request_ref, headers=headers, data=data)
    return request_object.json()['id_token']


def movie_summary_json(id=657):
    # Make an API request to TMDB
    api_key = os.environ.get('TMDB_KEY')
    api_url = f"https://api.themoviedb.org/3/movie/{id}?api_key={api_key}&language=en-US"
    response = requests.get(url=api_url)
    return response.json()['overview']


def top_rated_json():
    top_rated_movies = []

    options = {
        "api_key": os.environ.get("TMDB_KEY"),
        "language": "en-US",
        "sort_by": "popularity.desc"
    }
    options["page"] = 1

    api_url = f"https://api.themoviedb.org/3/movie/top_rated"
    response = requests.get(url=api_url, params=options)
    response_results = response.json()["results"]
    for item in response_results:
        movie = {
            "genres": id_to_genre(item["genre_ids"]),
            "id": item["id"],
            "is_movie": True,
            "overview": item["overview"],
            "popularity": item["popularity"],
            "poster_path": item["poster_path"],
            "release_year": str(item["release_date"][0:4]),
            "title": item["title"]
        }
        top_rated_movies.append(movie)
    return json.dumps(top_rated_movies)

"""
def worst_rated_json():
    return True

def popular_json():
    return True

def unpopular_json():
    return True

def now_playing_json():
    return True

def oldest_json():
    return True
"""

def id_to_genre(genre_ids):
    genres = []
    
    for genre in genre_ids: 
        genres.append(GENRE_IDS_TO_NAME[genre])

    return genres


