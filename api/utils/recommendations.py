"""
Module is responsible for handling the recommendation system.

Module has a custom data structure to emulate a queuing system.
"""

import shows

from api_handler import APIHandler

class RecomendationQueue:
    """
    The custom data stucture, ReccomendationQueue, has been defined to be used as the data structure.
    This class is an encapsulated dict to maintain insertion order but allow for constant access, 
    deletion and insertion.
    """

    def __init__(self, genres=[]):
        """
        Initializes a dictionary of "Show" ids as keys and the actual "Show" object as the value. The 
        dictionary is populated with "Show" objects that are retrieved from the TMDB API using the 
        genres that are passed in by the constructor.

        Attributes: 
            show_dict: This dictionary will have a key value of the ID for movies and the value will
            be the show object. Will have a structure of "Show" id being the key and the actual "Show" 
            object being the value.
            api_handler: Class that handles all the API calls and returns "clean" data to be used for the 
            "RecommendationQueue".
        """

        self.show_dict = dict()
        self.api_handler = APIHandler()
                
        initial_recommendations = self.api_handler.get_initial_shows_by_genre(genres, 3)
        
        self.add(initial_recommendations)

    def add(self, to_be_added):
        """
        Adds a single item or multiple items via a list to the "RecommendationQueue". If the item that is
        being added to the recommendation queue is already in the recommendationqueue then the score for 
        that show is incremented.

        Args:
            to_be_added: The item(s) to be added to the "RecommendationQueue". Assumes that
            to_be_added will be a "Show" object.
        """

        if type(to_be_added) == list:
            for item in to_be_added:
                self.add(item)
        else:
            if to_be_added in self.show_dict.values():
                self.show_dict[to_be_added.id].score += 1
            else:
                self.show_dict[to_be_added.id] = to_be_added

    def delete_recommendation(self, to_be_deleted):
        """
        Deletes recommendation from the "RecommendationQueue".

        Args:
            to_be_deleted: Item that will be deleted from the "RecommendationQueue".Assumes that
            to_be_deleted will be a "Show" object.
        """

        self.show_dict.pop(to_be_deleted)

    def length(self): 
        """
        Returns: 
            The length of the "RecommendationQueue".
        """

        return len(list(self.show_dict.keys()))
    
    def current_recommendation(self):
        """
        The first item in the sorted array of "Show" objects. This is the item that the
        user will be decided if they are interested or not. 

        Returns:    
            The first item of the sorted "Show" objects that are the values of the attribute "show_dict". 
        """

        return self.sorted_queue()[0]

    def dislike_recommendation(self):
        """
        Handles the user disliking a recommendation. The score for the "Show" object 
        will be decreased to -1, indicating that this show should be the lowest priority. If the 
        user comes across the "Show" again and dislikes it then the "Show" is removed from the "RecommendationQueue".

        STUB:
            Since a user has the ability to dislike something twice, with the second time resulting in the removal of the 
            item. There should also be a way to permit this "Show" from being added back to the user's "RecommendationQueue".
            Perhaps using another dicitonary or a set to determine membership in constant time.
        """

        current_recommendation = self.current_recommendation()

        if current_recommendation.score == -1:
            self.delete_recommendation(current_recommendation.id)
        else:
            current_recommendation.score = -1

    def like_recommendation(self):
        """
        Handles the user liking a recommendation. If the user likes the recommendations then the entry will be removed
        and recommended movies will be fetched from TMDB API and added to the "RecommendationQueue". If the recommendations are 
        already in the "RecommendationQueue" then the score is increased giving them a higher weight so they can be recommended to 
        the user. Depending on how many recommendations the user has in the queue, determines how many pages of results will be fetched,
        There is also a chance that there may be no recommendations.

        STUB: The liked movie will also need to be saved to the user's profile.
        """
        if self.length() > 200: 
            page_number = 2
        else: 
            page_number = 4

        new_recs = self.api_handler.get_recommendation_by_show(self.current_recommendation(), page_number)
        self.add(new_recs)

    def sorted_queue(self): 
        """
        Sorts the attribute the values of "show_dict".

        Returns:
             the keys of the dictionary in a sorted list.
        """

        return sorted(list(self.show_dict.values()), reverse=True)

    def print_queue(self):
        """
        Prints all the items that are in the queue in order. Used for debugging the data structure.
        """

        for item in self.sorted_queue():
            item.display_info()