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
            api_handler: Class that handles all the API calls and returns clean, usable data to be used for the 
            "RecommendationQueue".
            blacklist: Contrary to its name, this attribute is a set that will hold all the ids for the "Shows"
            that have been removed from the "RecommendationQueue" so as to avoid duplicates.
        """

        self.show_dict = dict()
        self.blacklist = set()
        self.api_handler = APIHandler()
                
        initial_recommendations = self.api_handler.get_initial_shows_by_genre(genres, 3)
        
        self.add(initial_recommendations)

    def add(self, to_be_added):
        """
        Adds a single item or multiple items via a list to the "RecommendationQueue". If the item that is
        being added to the recommendation queue is already in the queue then the 'score' attribute for 
        that object is incremented. If the 'id' of the new show is not in the 'blacklist' then a new "Show" entry
        is added to the RecommendationQueue.

        Args:
            to_be_added: The item(s) to be added to the "RecommendationQueue". Assumes that
            to_be_added will be a "Show" object or a list of "Show" objects.
        """

        if type(to_be_added) == list:
            for item in to_be_added:
                self.add(item)
        else: 
            if to_be_added in self.show_dict.values():
                self.show_dict[to_be_added.id].score += 1

            if to_be_added.id not in self.blacklist:
                self.show_dict[to_be_added.id] = to_be_added

    def delete_recommendation(self, show_id):
        """
        Deletes recommendation from the "RecommendationQueue". Also adds the recommendation's id to 
        the 'blacklist', so the recommendation that is removed from the queue is not added again.

        Args:
            show_id: Item that will be deleted from the "RecommendationQueue". Assumes that 'show_id' 
            will be an id for a "Show" object.
        """

        self.blacklist.add(show_id)
        self.show_dict.pop(show_id)

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
        will be decreased to -1, indicating that this "Show" should be the lowest priority. If the 
        user comes across the "Show" again and dislikes it then the "Show" is removed from the "RecommendationQueue"
        and the "Show's" id is added to the 'blacklist'.
        """

        current_recommendation = self.current_recommendation()

        if current_recommendation.score < 0:
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

        self.delete_recommendation(self.current_recommendation().id)
        self.add(new_recs)

    def sorted_queue(self): 
        """
        Sorts the attribute the values of "show_dict".

        Returns:
            The keys of the dictionary in a sorted list.
        """

        return sorted(list(self.show_dict.values()), reverse=True)

    def print_queue(self):
        """
        Prints all the items that are in the queue in order. Used for debugging the data structure.
        """

        for item in self.sorted_queue():
            item.display_info()