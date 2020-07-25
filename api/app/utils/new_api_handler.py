from gevent import monkey
monkey.patch_all(thread=False, select=False)

import json
import copy

import api_constants as consts
import shows as s
import grequests
import requests


def discover_requests(genre_ids, number_of_pages=3, is_movie=True):
    """
    Builds a list of API requests for the /discover endpoint for TMDB. Two types of requests can be sent,
    One for movies and another for TV Shows, this is because of how certain quer params are handled by the TMDB API.

    Args:
        genre_ids: A list of genres that will be used to query against TMDB. See 'api_constants.py'
        for full list.
        number_of_pages: The total number of pages of information to be requested from TMDB. Max page
        size is 20 results. 
        is_movie: Boolean that decides what type of request will be sent to TMDB.

    Returns: 
        discover_requests: A list of API requests that will be sent to TMDB's discover endpoint.
    """

    discover_requests = []

    for page_num in range(1, number_of_pages + 1):
        for genre in genre_ids:
            options = copy.deepcopy(consts.DEFAULT_OPTIONS)
            options["with_genres"] = genre
            options["page"] = page_num

            if is_movie:
                options["release_date.lte"] = "2020-06-01"
                options["release_date.gte"] = "1985-01-01"
                api_url = consts.MOVIE_DISCOVER_URL
            else:
                options["first_air_date.lte"] = "2020-06-01"
                options["first_air_date.gte"] = "1985-01-01"
                api_url = consts.TV_SHOW_DISCOVER_URL

            discover_requests.append(
                grequests.get(url=api_url, params=options))

    return discover_requests


def recommendation_requests(show):
    """
    Function that builds a list of requests for recommendations endpoint 
    for TMDB when give a "Show" object. Max page size is 20 results. The /recommendation 
    endpoint only fetches a maximum of 2 pages or 40 results.

    Args:
        show: "Show" object that recommendations are based on.

    Returns:
        rec_requests: A list of API requests that will be sent to TMDB's recommendation endpoint.
    """

    rec_requests = []
    number_of_pages = 2

    if show.is_movie:
        api_url = consts.MOVIE_RECOMMENDATION_URL
    else:
        api_url = consts.TV_SHOW_RECOMMENDATION_URL

    for page_num in range(1, number_of_pages + 1):
        options = copy.deepcopy(consts.DEFAULT_OPTIONS)
        options["page"] = page_num

        rec_requests.append(grequests.get(
            url=api_url.format(show.id), params=options))

    return rec_requests


def get_discover_shows(genre_ids, number_of_pages=3):
    """
    Args:
        genre_ids: A list of ids that TMDB resolves to genres.
        number_of_pages: How many pages of data are going to be requested from TMDB. 
        Default is 3 and the max number of results returned per page is 20.

    Returns:
        shows: A list of "Show" objects derived from the /discover endpoint for
        TMDB. 
    """
    shows = []

    movie_recs = discover_requests(genre_ids, number_of_pages, True)
    tv_reqs = discover_requests(genre_ids, number_of_pages, False)

    movie_responses = grequests.map(movie_recs, size=len(movie_recs))
    tv_responses = grequests.map(tv_reqs, size=len(tv_reqs))

    shows.extend(create_show_data_list(movie_responses, True))
    shows.extend(create_show_data_list(tv_responses, False))

    return shows


def get_recommendations(show):
    """
    Args:
        show: The "ShowData" for the "Show" the user liked.

    Returns:
        recommendations: A list of recommendation "Show" objects based on the 
        arg 'show'
    """

    recommendations = []

    rec_reqs = recommendation_requests(show)
    responses = grequests.map(rec_reqs, size=len(rec_reqs))

    recommendations.extend(create_show_data_list(responses, show.is_movie))

    return recommendations


def resolve_show(show_data):
    """
    Function that will fetch the complete data for a "Show" based on the "ShowData"
    object.

    Args:
        show_data: A "ShowData" object that will be resolved to a full "Show" object.

    Returns: 
        show: The completed "Show" object.
    """
    if show_data.is_movie:
        api_url = consts.MOVIE_DETAILS_URL
    else:
        api_url = consts.TV_SHOW_DETAILS_URL

    options = copy.deepcopy(consts.DEFAULT_OPTIONS)

    req = requests.get(url=api_url.format(show_data.id), params=options)

    return s.create_show(req.json(), show_data.is_movie)


def create_show_data_list(api_responses, is_movie):
    """
    Function responsible for creating a list of "ShowData" objects.

    Args:
        api_responses: A list of responses returned from TMDB
        is_movie: A boolean to decide if the "ShowData" is for a Movie or TV Show.
    """
    items = []

    if len(api_responses) == 0:
        return items

    for response in api_responses:
        if response.status_code == 200:
            results = response.json()["results"]
            for result in results:
                items.append(s.ShowData(
                    result["id"], result["vote_average"], is_movie))

    return items


def top_rated_requests(is_movie=True):
    """
    Builds a list of API requests for the top rated movies

    Args:
        is_movie: Boolean that decides what type of request will be sent to TMDB.

    Returns: 
        top_rated_requests: A list of API requests that will be sent to TMDB's /top_rated endpoint.
    """

    top_rated_requests = []

    options = copy.deepcopy(consts.DEFAULT_OPTIONS)
    options["page"] = 1

    if is_movie:
        api_url = consts.MOVIE_TOP_RATED_URL

    top_rated_requests.append(grequests.get(url=api_url, params=options))
    return top_rated_requests


def get_top_rated_shows():
    """
    Function is responsible of creating a list of top rated movies from TMDB

    Returns:
        shows: A list of "Show" objects derived from the /top_rated endpoint for
        TMDB. 
    """
    shows = []

    movie_recs = top_rated_requests()
    movie_responses = grequests.map(movie_recs, size=len(movie_recs))
    shows.extend(create_show_data_list(movie_responses, True))
    return shows


def worst_rated_requests(is_movie=True):
    """
    Builds a list of API requests for the worst rated movies

    Args:
        is_movie: Boolean that decides what type of request will be sent to TMDB.

    Returns: 
        worst_rated_requests: A list of API requests that will be sent to TMDB's /top_rated endpoint.
    """

    worst_rated_requests = []

    options = copy.deepcopy(consts.DEFAULT_OPTIONS)
    options["page"] = 1
    options["sort_by"] = "vote_average.asc"

    if is_movie:
        api_url = consts.MOVIE_TOP_RATED_URL

    worst_rated_requests.append(grequests.get(url=api_url, params=options))
    return worst_rated_requests


def get_worst_rated_shows():
    """
    Function is responsible of creating a list of top rated movies from TMDB

    Returns:
        shows: A list of "Show" objects derived from the /worst_rated endpoint for
        TMDB. 
    """
    shows = []

    movie_recs = worst_rated_requests()
    movie_responses = grequests.map(movie_recs, size=len(movie_recs))
    shows.extend(create_show_data_list(movie_responses, True))
    return shows


def popular_requests(is_movie=True):
    """
    Builds a list of API requests for the most popular movies

    Args:
        is_movie: Boolean that decides what type of request will be sent to TMDB.

    Returns: 
        top_rated_requests: A list of API requests that will be sent to TMDB's /popular endpoint.
    """
    popular_requests = []

    options = copy.deepcopy(consts.DEFAULT_OPTIONS)
    options["page"] = 1

    if is_movie:
        api_url = consts.MOVIE_POPULAR_URL

    popular_requests.append(grequests.get(url=api_url, params=options))

    return popular_requests


def get_popular_shows():
    """
    Function is responsible of creating a list of most popular movies from TMDB

    Returns:
        shows: A list of "Show" objects derived from the /popular endpoint for
        TMDB. 
    """
    shows = []

    movie_recs = popular_requests()
    movie_responses = grequests.map(movie_recs, size=len(movie_recs))
    shows.extend(create_show_data_list(movie_responses, True))
    return shows


def unpopular_requests(is_movie=True):
    """
    Builds a list of API requests for the most unpopular movies

    Args:
        is_movie: Boolean that decides what type of request will be sent to TMDB.

    Returns: 
        top_rated_requests: A list of API requests that will be sent to TMDB's /unpopular endpoint.
    """
    popular_requests = []

    options = copy.deepcopy(consts.DEFAULT_OPTIONS)
    options["page"] = 1
    options["sort_by"] = "vote_average.asc"

    if is_movie:
        api_url = consts.MOVIE_POPULAR_URL

    popular_requests.append(grequests.get(url=api_url, params=options))

    return popular_requests


def get_unpopular_shows():
    """
    Function is responsible of creating a list of most popular movies from TMDB

    Returns:
        shows: A list of "Show" objects derived from the /popular endpoint for
        TMDB. 
    """
    shows = []

    movie_recs = unpopular_requests()
    movie_responses = grequests.map(movie_recs, size=len(movie_recs))
    shows.extend(create_show_data_list(movie_responses, True))
    return shows


def oldest_requests(is_movie=True):
    """
    Builds a list of API requests for the oldest movies

    Args:
        is_movie: Boolean that decides what type of request will be sent to TMDB.

    Returns: 
        top_rated_requests: A list of API requests that will be sent to TMDB's /oldest endpoint.
    """
    popular_requests = []

    options = copy.deepcopy(consts.DEFAULT_OPTIONS)
    options["page"] = 1
    options["sort_by"] = "primary_release_date.asc"

    if is_movie:
        api_url = consts.MOVIE_POPULAR_URL

    popular_requests.append(grequests.get(url=api_url, params=options))

    return popular_requests


def get_oldest_shows():
    """
    """
    shows = []

    movie_recs = oldest_requests()
    movie_responses = grequests.map(movie_recs, size=len(movie_recs))
    shows.extend(create_show_data_list(movie_responses, True))
    return shows


def get_unpopular_shows():
    """
    Function is responsible of creating a list of most popular movies from TMDB

    Returns:
        shows: A list of "Show" objects derived from the /popular endpoint for
        TMDB. 
    """
    shows = []

    movie_recs = unpopular_requests()
    movie_responses = grequests.map(movie_recs, size=len(movie_recs))
    shows.extend(create_show_data_list(movie_responses, True))
    return shows


def get_now_playing_movies(page_num=1):
    """
    Function get a list of movies in theatres. 
    """
    items = []
    options = copy.deepcopy(consts.DEFAULT_OPTIONS)
    options["page"] = page_num

    api_url = consts.MOVIE_NOW_PLAYING_URL
    response = requests.get(url=api_url, params=options)

    return response
