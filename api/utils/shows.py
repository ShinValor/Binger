"""
Module will structure the API responses so they will be used properly
"Shows" are both TV shows and Movies for this project
as there is no universal term that refers to both.
"""

import api_constants as consts

class Show:
    """
    Class to encapsulate data from TMDB query response.

    Attributes: 
        id: How TMDB identifies each "Show".
        genres: Genres for "Shows" that are a list of genre ids from the TMDB API.
        overview: Brief description of the "Show".
        popularity: The rating of the "Show" in the TMDB API
        poster_path: Path for the "show's" poster.
        release_year: The year the show was released or first aired.
        score: An int that will determine the likability score. If a show is in the RecommendationQueue
        and the API is to added it again, the score is increased instead. default is 1.
        title: The title of the "Show".
        is_movie: Boolean to determine if a "Show" is a Movie or TV Show.
    """

    def __init__(self, id, genres, overview, popularity, poster_path, release_year, title, is_movie=True):
        """
        Initializes a show class with the information passed in by the constructor.
        
        The genres that are passed are typically as a list of ids so they are 
        resolved into a list of genres with words using the 'GENRE_IDS_TO_NAME' dictionary
        from the api_constants library.
        """

        self.id = id
        self.genres = []
        self.overview = overview
        self.popularity = popularity
        self.poster_path = consts.TMDB_IMAGE_URL.format(poster_path)
        self.release_year = release_year
        self.score = 0
        self.title = title
        self.is_movie = is_movie

        for genre in genres: 
            self.genres.append(consts.GENRE_IDS_TO_NAME[genre])

    def __eq__(self, other): 
        """
        Allows for show classes to be compared to one another. If the attribute id is
        the same then the 'shows' are the same.
        """

        return self.id == other.id

    def __hash__(self):
        """
        Allows the "Show" object to be hashed and placed into hashed data strucutres.

        Returns:
            The hash of the "Show" objects id.
        """
        return hash(self.id)

    def __lt__(self, other):
        """
        Allows the 'show' objects' scores to be compared to one another for sorting.
        """

        if self.score == other.score:
            return self.popularity < other.popularity

        return self.score < other.score

    def display_info(self):
        """
        Prints information of the "Show". Primarily a troubleshooting tool most likely won't 
        be used in prod.
        """

        show_information = f"ID: {self.id}\nTitle: {self.title} ({self.release_year})\nGenres: {self.genres}"
        show_information += f"\nOverview: {self.overview}"
        show_information += f"\nPopularity: {self.popularity}"
        show_information += f"\nImage: {self.poster_path}"
        show_information += f"\nIs Movie: {self.is_movie}"
        show_information += f"\nScore: {self.score}\n"

        print(show_information)

def create_show(result_dict, is_movie):
    """
    Responsible for taking dictionary from API response and creates a class

    Args: 
        result_dict: A dictionary from the API that will be used to turn into a Show class.
        is_movie: A boolean that will determine if this "Show" is a Movie or not.

    Returns:
        A "Show" class object. 

    """
    
    show = Show(result_dict["id"],
        result_dict["genre_ids"],
        result_dict["overview"], 
        result_dict["vote_average"],
        result_dict["poster_path"], "", "", "")
    
    if is_movie:
        show.title = result_dict["title"]
        show.release_year = str(result_dict["release_date"][0:4])
        show.is_movie = True
    else: 
        show.title = result_dict["name"]
        show.release_year = str(result_dict["first_air_date"][0:4])
        show.is_movie = False

    return show

def create_show_list(list_of_results, is_movie):
    """
    Creates a list of "Shows" from the API response.

    Args: 
        list_of_results: A list of dictionaries from the API response.
        is_movie: A boolean that decides what where or not a "Show" is a Movie
        or a TV Show.

    Returns:
        Returns a list of "Show" objects.
    """

    returned_list = []
    
    if len(list_of_results) == 0:
        return returned_list

    for result in list_of_results:
        returned_list.append(create_show(result, is_movie))

    return returned_list
