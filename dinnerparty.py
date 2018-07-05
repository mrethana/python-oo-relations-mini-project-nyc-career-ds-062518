#python -m unittest
from invite import Invite
from guest import Guest
from recipe import Recipe
from review import Review
from course import Course
import pdb
class DinnerParty:

    _all = []

    def __init__(self, dinner_party):
        self._dinner_party = dinner_party
        DinnerParty._all.append(self)
    @classmethod
    def all(cls):
        return cls._all

    @property
    def dinner_party(self):
        return self._dinner_party

    @dinner_party.setter
    def dinner_party(self, dinner_party):
        self._dinner_party = dinner_party

    def invites(self):
        return [invite for invite in Invite._all if invite._dinner_party == self]

    def guests(self):
        return [invite._guest for invite in self.invites() if invite._accepted == True]

    def number_of_attendees(self):
        return len(self.guests())

    def courses(self):
        return [course for course in Course._all if course._dinner_party == self]

    def recipes(self):
        return [recipe._recipe for recipe in self.courses()]

    def recipe_count(self):
        return len(self.recipes())

    def reviews(self):
        return [review for review in Review._all if review._recipe in self.recipes()]

    def highest_rated_recipe(self):
         highest_rated_dict = {recipe:0 for recipe in self.recipes()}
         for review in self.reviews():
             if highest_rated_dict[review._recipe] < review._rating:
                 highest_rated_dict[review._recipe] = review._rating
         return sorted(highest_rated_dict, key = highest_rated_dict.get, reverse = True)[:1][0]
