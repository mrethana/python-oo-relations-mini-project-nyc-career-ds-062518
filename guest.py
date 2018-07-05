from invite import Invite
from review import Review

class Guest:

    _all = []

    def __init__(self, guest):
        self._guest = guest
        Guest._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def most_popular(cls):
        all_guests = [invite._guest for invite in Invite._all]
        guest_dict = dict.fromkeys(set(all_guests), 0)
        for guest in all_guests:
            guest_dict[guest] += 1
        return sorted(guest_dict, key = guest_dict.get, reverse =True)[:1][0]

    @classmethod
    def toughest_critic(cls):
        critic_dict = {review._guest: [] for review in Review._all}
        for review in Review._all:
            critic_dict[review._guest].append(review._rating)
        for guest,list in critic_dict.items():
            list = round(sum(list)/len(list),2)
            critic_dict[guest] = list
        return sorted(critic_dict, key = critic_dict.get, reverse = False)[:1][0]


    @classmethod
    def most_active_critic(cls):
        active_dict = {review._guest: 0 for review in Review._all}
        for review in Review._all:
            active_dict[review._guest] += 1
        return sorted(active_dict, key = active_dict.get, reverse = True)[:1][0]

    def invites(self):
        return [invite for invite in Invite._all if self == invite._guest]

    def reviews(self):
        return [review for review in Review._all if self == review._guest]

    def number_of_invites(self):
        return len(self.invites())

    def rsvp(self, invite, rsvp_status):
        if self == invite._guest:
            invite._rsvp_status = rsvp_status
        return rsvp_status

    def review_recipe(self, recipe, rating, comment):
        new_review = Review(self, recipe, rating, comment)
        return [review for review in Review._all if recipe == review._recipe]

    def favorite_recipe(self):
        fav_recipe_dict = {review._recipe: 0 for review in self.reviews()}
        for review in self.reviews():
            if review._rating > fav_recipe_dict[review._recipe]:
                fav_recipe_dict[review._recipe] = review._rating
        return sorted(fav_recipe_dict, key = fav_recipe_dict.get, reverse = True)[:1][0]
        # max_rating = 0
        # for review in self.reviews():
        #     if review._rating > max_rating:
        #         max_rating = review._rating

    @property
    def guest(self):
        return self._guest

    @guest.setter
    def guest(self, guest):
        self._guest = guest


# Class
# Guest.all() returns a list of all guest instances
# Guest.most_popular() returns the guest invited to the most dinner parties
# Guest.toughest_critic() returns the guest with lowest average rating for recipe reviews
# Guest.most_active_critic()

# Instance
# guest.invites() returns a list of all of the guest's invites
# guest.reviews() returns a list of all of the guest's reviews
# guest.number_of_invites() returns the number of dinner party invites a guest has recieved
# guest.rsvp(invite, rsvp_status) takes in a boolean value (True or False) and updates a guest's rsvp status. It should return the rsvp_status status
# guest.review_recipe(recipe, rating, comment) adds a guest's review with a rating and comment to a recipe. Returns the given recipe's reviews
# guest.favorite_recipe() returns the given guest's favorite recipe
