import random


class player:
    def __init__(self, name, fav_weapons):
        self.name = name
        self.last_visited_places = []
        self.fav_weapons = fav_weapons

    def visit_places(self, places_to_visit):
        self.last_visited_places = random.sample(places_to_visit, random.randint(1, 3))

    def suspect(self):
        """ the function choosing a random 2 places from the last visited places of the player
         and 1 gun from his favorite guns
         returns: (2 places,one gun)
         """
        # Choose 2 random places and 1 weapon for each suspected player
        places = random.sample(self.last_visited_places, min(len(self.last_visited_places), 2))
        weapon = random.choice(self.fav_weapons)
        return [places, weapon]
