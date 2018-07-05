
# Python - Object Relationships Project

## Introduction
In this lab we are going to practice object relationships in Python with an emphasis on has-many-through relationships. We will be building out a domain model for Guests, Invites, Dinner Parties, Courses, Recipes, and Reviews. A guest will have a collection of invites, which will relate a guest to a dinner party, thus creating the has many through relationship between a user and a dinner party. Just like any good dinner party there will be more than just one thing to eat, which means that a dinner party will have a collection of courses. Since not all courses will be unique across all dinner parties, a recipe will have also have many courses. A recipe also has many reviews, which are given directly by guests, so, guests will also have many reviews as well.

Read through the deliverables below to begin building out these six classes and to figure out additional information about their relationships.
> **Note:** You may not be able to build out all methods until you have set up relationships between the classes, so it is normal to jump around a bit in the building process. If you are confused about how the models below relate to each other, it may help to draw this out on a whiteboard before beginning to code.

## Objectives
* Define classes according to their approproate relationships
* Create instance and class methods that leverage the has many through relationships

### Guest
Guests
has many Invites
has many reviews

Invites
belongs to Dinner party


Dinner Parties
has many courses
has many invites

Courses


Recipes
has many courses
has many reviews

Reviews
belongs to guest

**Class Methods:**
* `Guest.all()` returns a list of all guest instances
* `Guest.most_popular()` returns the guest invited to the most dinner parties
* `Guest.toughest_critic()` returns the guest with lowest average rating for recipe reviews
* `Guest.most_active_critic()` returns the guest with most recipe reviews

**Instance Methods:**
* `guest.invites()` returns a list of all of the guest's invites
* `guest.reviews()` returns a list of all of the guest's reviews
* `guest.number_of_invites()` returns the number of dinner party invites a guest has recieved
* `guest.rsvp(invite, rsvp_status)` takes in a boolean value (True or False) and updates a guest's rsvp status. It should return the rsvp_status status
* `guest.review_recipe(recipe, rating, comment)` adds a guest's review with a rating and comment to a recipe. Returns the given recipe's reviews
* `guest.favorite_recipe()` returns the given guest's favorite recipe

### Invite
**Class Methods:**
* `Invite.all()` returns a list of all invite instances

**Instance Methods:**
* `invite.accepted` returns a boolean value (true or false) for whether the the guest accepted the invite or not
* `invite.guest` returns the given invite's guest instance
* `invite.dinner_party` returns the given invite's dinner party instance

### DinnerParty
**Class Methods:**
* `DinnerParty.all()` returns a list of all dinner party instances

**Instance Methods:**
* `dinner_party.invites()` returns a list of all of invites handed out for the party
* `dinner_party.guests()` returns a list of the party's guests
* `dinner_party.number_of_attendees()` returns the number of guests who accepted their invite for the dinner party
* `dinner_party.courses()` returns a list of the party's courses
* `dinner_party.recipes()` returns a list of all the recipes for the courses featured at the given dinner party
* `dinner_party.recipe_count()` returns the number of recipes for the given dinner party
* `dinner_party.reviews()` returns a list of reviews for the recipes of a given dinner party
* `dinner_party.highest_rated_recipe()` returns the highest rated recipe for the given dinner party

### Course
**Class Methods:**
* `Course.all()` returns a list of all course instances

**Instance Methods:**
* `course.dinner_party` returns the dinner party instance for the given course
* `course.recipe` returns the recpipe instance for the given course

### Review
**Class Methods:**
* `Review.all()` returns a list of all invite instances

**Instance Methods:**
* `review.rating` returns the given review's rating
* `review.recipe` returns the given review's recipe
* `review.reviewer` returns the given review's reviewer (guest instance)
* `review.comment` returns the given review's comment, if there is one

### Recipe
**Class Methods:**
* `Recipe.all()` returns a list of all invite instances
* `Recipe.top_three()` returns a list with the three recipe instances with the highest average rating
* `Recipe.bottom_three()` returns a list with the three recipe instances with the lowest average rating

**Instance Methods:**
* `recipe.reviews()` returns a list of reviews for the given recipe
* `recipe.top_five_reviews()` returns a list with the five review instances with the highest rating for the given recipe

## Summary


Great work! In this lab we created a pretty complex domain model and defined some neat class and instance methods to leverage these has many through relationships. We could see that without these relationships, meaning without a review linking a recipe and a guest, it would become very difficult to organize our information and query it accurately like we do in a class method that gives us the top or bottom three recipes.
