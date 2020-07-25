import os
import json
#import pytest
import requests
import time

url = 'http://localhost:5000'
refresh_token = ''

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

"""
def top_rated_json():
    return True

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


