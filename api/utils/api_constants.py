"""
Module that will hold the constants for the application.

os module is used because the api key requires is stored in an environment 
variable.
"""

import os

"""
All the available genres from TMDB, Placed in constant var for easy access
instead of requesting API everytime a genre id needs to be resolved.

Acquired using TMDB API endpoints:
/genre/movie/list
/genre/tv/list

Reference: https://developers.themoviedb.org/3/genres
"""
GENRE_IDS_TO_NAME = {
    12    : "Adventure",
    14    : "Fantasy",
    16    : "Animation",
    18    : "Drama",
    27    : "Horror",
    28    : "Action",
    35    : "Comedy",
    36    : "History",
    37    : "Western",
    53    : "Thriller",    
    80    : "Crime",
    99    : "Documentary",
    878   : "Science Fiction",
    9648  : "Mystery",
    10402 : "Music",
    10749 : "Romance",
    10751 : "Family",
    10752 : "War",
    10759 : "Action & Adventure",
    10762 : "Kids", 
    10763 : "News",
    10764 : "Reality",
    10765 : "Sci-Fi & Fantasy",
    10766 : "Soaps", 
    10767 : "Talk",
    10768 : "War & Politics",
    10770 : "TV Movie"
}

"""
A dictionary of GENRE_IDS but has its keys and values swapped for resolving a
genre's name to an ID.
"""
GENRE_NAMES_TO_IDS = dict((value, key) for key, value in GENRE_IDS_TO_NAME.items())

"""
API Key needed for accessing the TMDB API. Assumes that the key is saved as an environment var
under the name 'TMDB_KEY'.
"""
API_KEY = os.environ.get("TMDB_KEY")

"""
The default payload options used for http requests. Other options will be appended as needed
via deep copying.
"""
DEFAULT_OPTIONS = {
    "api_key"     : API_KEY,
    "language"    : "en-US",
    "sort_by"     : "popularity.desc"
}

""" 
Base URL used by TMDB to resolve "show's" poster.
"""
TMDB_IMAGE_URL = "https://image.tmdb.org/t/p/w500{}"

""" 
Base URLs used by TMDB to discover initial "shows".

Reference: https://developers.themoviedb.org/3/discover/movie-discover
"""
MOVIE_DISCOVER_URL = "https://api.themoviedb.org/3/discover/movie"
TV_SHOW_DISCOVER_URL = "https://api.themoviedb.org/3/discover/tv/"

"""
Base URLs used by TMDB to get recommendations based on "show" ids.

Reference: https://developers.themoviedb.org/3/movies/get-movie-recommendations
"""
MOVIE_RECOMMENDATION_URL = "https://api.themoviedb.org/3/movie/{}/recommendations"
TV_SHOW_RECOMMENDATION_URL = "https://api.themoviedb.org/3/tv/{}/recommendations"

"""
Base URLs used by TMDB to get similar movies, these are not the same as recommendations. 
"shows" that are fetched only have similar keywords and genres.

Reference: https://developers.themoviedb.org/3/movies/get-similar-movies
"""
MOVIE_SIMILAR_URL = "https://api.themoviedb.org/3/movie/{}/similar"
TV_SHOW_SIMILAR_URL = "https://api.themoviedb.org/3/tv/{}/similar"

"""
MOVIE_DISCOVER_URL = "https://api.themoviedb.org/3/discover/movie"
TV_SHOW_DISCOVER_URL = "https://api.themoviedb.org/3/discover/tv"

"""
Base URLs used by TMDB to get recommendations based on "show" ids.
"""
MOVIE_RECOMMENDATION_URL = "https://api.themoviedb.org/3/movie/{}/recommendations"
TV_SHOW_RECOMMENDATION_URL = "https://api.themoviedb.org/3/tv/{}/recommendations"