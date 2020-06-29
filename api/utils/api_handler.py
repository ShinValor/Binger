"""
Module will handle fetching data from the TMDB API.

Module will mainly be responsible for sending requests and receiving 
data from API. API requests will be sent asynchronously using the 
grequests module with the help of modules from the requests module.

Reference: https://developers.themoviedb.org/3/getting-started/introduction
"""

import copy
import grequests
import json
import requests
import shows

import api_constants as consts

from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

class APIHandler: 
    """
    Wrapper class to make API calls easy.

    Attributes:
        number_of_sessions: The number of sessions that will be used to asynchronously fetch data 
        from the API.
        sessions: A list of requests.Sessions that are responsible for fetching data.
        retries: Retry object that defines how http retries will be handled.
    """

    def __init__(self, number_of_sessions=10):
        """
        Initializes the api handler. 

        By default, number_of_sessions is 10 but you can pass an optional int to alter
        the number of sessions the ApiHandler will use. Each of the sessions defined 
        will also be sent over https with a maximum number of retries.
        """

        self.number_of_sessions = number_of_sessions
        self.sessions = [requests.Session() for i in range(self.number_of_sessions)]
        self.retries = Retry(total=3, 
                             backoff_factor=0.1,
                             status_forcelist=[500, 502, 503, 504])   

        for session in self.sessions:
            session.mount("https://", HTTPAdapter(max_retries=self.retries))
    
    def async_request(self, url, session_id, params):
        """
        Fuction that returns a async request using the 'grequests' module.

        Args: 
            url: The url to the endpoint of the API
            sessions_id: An int that will decide which of the sessions will be used.
            session_id is modulo by the attribute 'number_of_sessions'
        """

        return grequests.get(url, 
                             session=self.sessions[session_id % self.number_of_sessions],
                             params=params)
    
    def build_show_list(self, responses, is_movie):
        """
        Function that will take API responses and builds a list of "Shows"

        Args: 
            responses: API responses that are received from TMDB requests.
            is_movie: Boolean to determine the type of "Show" list is being created.

        Returns: 
            list_of_shows: A list of "Show" objects that are to be returned.
        """

        list_of_shows = []
        
        for response in responses:
            api_results = json.loads(response.text)["results"]
            list_of_shows.extend(shows.create_show_list(api_results, is_movie))

        return list_of_shows
    
    def get_initial_show_requests(self, genres, number_of_pages, is_movie):
        """
        Function is responsible for building a list of requests that will be sent 
        to the TMDB API.

        Args:
            genres: List of genre ids
            number_of_pages: Number of pages that will be requested from the API. The 
            maximum number of results returned per page is 20.
            is_movie: Boolean to decide which endpoint to make request for. Movie or TV.

        Returns:
            show_requests: A list of requests to be sent to the API.
        """

        session_id = 0
        show_requests = []

        for i in range(1, (number_of_pages + 1)):
            for genre in genres:
                options = copy.deepcopy(consts.DEFAULT_OPTIONS)
                options["with_genres"] = genre
                options["page"] = i

                if is_movie: 
                    options["release_date.lte"] = "2020-06-01"
                    options["release_date.gte"] = "1985-01-01"
                    api_url = consts.MOVIE_DISCOVER_URL
                else: 
                    options["first_air_date.lte"] = "2020-06-01"
                    options["first_air_date.gte"] = "1985-01-01"
                    api_url = consts.TV_SHOW_DISCOVER_URL

                show_requests.append(self.async_request(api_url, session_id, options))
                session_id += 1

        return show_requests
     
    def get_initial_shows_by_genre(self, genres, number_of_pages):
        """
        Handles the initial retrieval of Movies and TV Shows from the TMDB API and will
        return a list of "Show" objects. Utilizes the class function 'get_initial_show_requests'
        to return a list of the requests that will be set to the API.

        Args:
            genres: The id(s) that are to be queried.
            number_of_pages: How many pages each are requested for each genre. Maximum returned per page is 20. 

        Returns: 
            show_list: Returns a list of "Show" objects
        """
        
        movie_requests = self.get_initial_show_requests(genres, number_of_pages, True)
        tv_show_requests = self.get_initial_show_requests(genres, number_of_pages, False)

        movie_responses = grequests.map(movie_requests, size=self.number_of_sessions)
        tv_show_responses = grequests.map(tv_show_requests, size=self.number_of_sessions)

        show_list = []
        show_list.extend(self.build_show_list(movie_responses, True))
        show_list.extend(self.build_show_list(tv_show_responses, False))
        
        return show_list

    def get_recommendation_by_show(self, show, number_of_pages=1):
        """
        Function that will request "Show" recommendations from the TMDB API.

        Args: 
            show: A show object
            number_of_pages: The number of pages that will be requested.

        Returns: 
            show_list: A list of show objects that are recommendation from the 
            arg "Show".
        """

        session_id = 0
        recommendation_requests = []
        
        options = copy.deepcopy(consts.DEFAULT_OPTIONS)
        
        if show.is_movie:
            api_url = consts.MOVIE_RECOMMENDATION_URL
        else:
            api_url = consts.TV_SHOW_RECOMMENDATION_URL

        for i in range(1, (number_of_pages + 1)):
            options["page"] = i
            recommendation_requests.append(self.async_request(api_url.format(show.id), 
                                            session_id, options))
            session_id += 1

        recommendation_responses = grequests.map(recommendation_requests, size=self.number_of_sessions)

        show_list = []    
        show_list.extend(self.build_show_list(recommendation_responses, show.is_movie))

        return show_list            
