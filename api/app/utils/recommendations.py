"""
Module is responsible for handling the recommendation system.

Module has a custom data structure to emulate a queuing system.

Module is not being used and should be deprecated.
"""
 
from gevent import monkey
monkey.patch_all(thread=False, select=False)

import shows
import new_api_handler

class RecommendationQueue:
    """
    The custom data stucture, RecommendationQueue, has been defined to be used as the data structure.
    This class is an encapsulated dict to maintain insertion order but allow for constant access, 
    deletion and insertion.
    """

    def __init__(self):
        """
        Initializes a dictionary of "Show" ids as keys and the "Show" object as the value.

        Attributes: 
            queue: This dictionary will have a key value of the ID for "Shows" and the value will
            be the "Show" object. Will have a structure of "S" id being the key and the "ShowData" being the value.
            This decision was made because the "Show" objects were very memory intensive.
            blacklist: Contrary to its name, this attribute is a set that will hold all the ids for the "Shows"
            that have been removed from the "RecommendationQueue" so as to avoid duplicates.
            is_initialized: A boolean that determines if the "RecommendationQueue" has had the initial recommendations
            added to it. False by default.
        """

        self.queue = dict()
        self.blacklist = set()
        self.is_initialized = False

    def initialize_recommendations(self, genre_ids):
        """
        Populates the 'queue' attribute with the initial recommendations based 
        on the genre ids that are passed.

        Args:
            genre_ids: List of the ids that are for genres in TMDB.       
        """

        if not self.is_initialized:
            self.add_multiple_recommendations(new_api_handler.get_discover_shows(genre_ids))
            self.is_initialized = True

    def add_multiple_recommendations(self, item_list):
        """
        Adds multiple items via a list to the "RecommendationQueue". If the item that is
        being added to the recommendation queue is already in the queue then the 'score' attribute for 
        that object is incremented. If the 'id' of the new item is not in the 'blacklist' then a new "Show" entry
        is added to the RecommendationQueue.

        Args:
            item_list: A list of show objects to be added to the "RecommendationQueue". Assumes that
            item_list will be a list of "Show" objects.
        """

        if type(item_list) != list:
            return
        
        for item in item_list:
            if item.id in self.queue.keys():
                self.queue[item.id].score += 1

            if item.id not in self.blacklist and item.id not in self.queue.keys():
                self.queue[item.id] = item
            
    def delete_recommendation(self, show_id):
        """
        Deletes recommendation from the "RecommendationQueue". Also adds the recommendation's id to 
        the 'blacklist', so the recommendation that is removed from the 'queue' is not added again.

        Args:
            show_id: Item that will be deleted from the "RecommendationQueue". Assumes that 'show_id' 
            will be an id for a "Show" object.
        """

        if not self.is_initialized:
            return 

        self.blacklist.add(show_id)
        self.queue.pop(show_id)

    
    def current_recommendation(self):
        """
        The first item in the sorted array of "Show" objects. This is the item that the
        user will be decided if they are interested or not. 

        Returns:    
            The first item of the sorted "ShowData" objects that are the values of the attribute 'queue'. 
        """
        if not self.is_initialized:
            return
        
        return self.sorted_queue()[0]

    def dislike_recommendation(self):
        """
        Handles the user disliking a recommendation. The score for the "ShowData" object 
        will be decreased to -1, indicating that this "Show" should be the lowest priority. If the 
        user comes across the "Show" again and dislikes it then the "Show" is removed from the "RecommendationQueue"
        and the "Show's" id is added to the 'blacklist'.
        """

        if not self.is_initialized:
            return

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
        the user.

        STUB: The liked movie will also need to be saved to the user's profile.
        """
        
        if not self.is_initialized:
            return

        new_recs = new_api_handler.get_recommendations(self.current_recommendation())

        self.delete_recommendation(self.current_recommendation().id)
        self.add_multiple_recommendations(new_recs)

    def sorted_queue(self): 
        """
        Sorts the attribute the values of 'queue'.

        Returns:
            The keys of the dictionary in a sorted list.
        """

        return sorted(list(self.queue.values()), reverse=True)

    def print_queue(self):
        """
        Prints all the items that are in the queue in order. Used for debugging the data structure.
        """

        if not self.is_initialized:
            return

        for item in self.sorted_queue():
            print(item)

    def length(self): 
        """
        Returns: 
            The length of the "RecommendationQueue".
        """
        
        return len(list(self.queue.keys()))