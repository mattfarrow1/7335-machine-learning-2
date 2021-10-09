# +-+-+-+-+-+-+-+-+
# |M|L|2| |H|W| |3|
# +-+-+-+-+-+-+-+-+
# Matt Farrow

# Decision Making With Matrices

# This is a pretty simple assignment. You will do something you do everyday, but
# today it will be with matrix manipulations. The problem is: you and your work
# friends are trying to decide where to go for lunch. You have to pick a
# restaurant that’s best for everyone. Then you should decided if you should
# split into two groups so everyone is happier. Despite the simplicity of the
# process you will need to make decisions regarding how to process the data.
# This process was thoroughly investigated in the operation research community.
# This approach can prove helpful on any number of decision making problems that
# are currently not leveraging machine learning.

# You asked your 10 work friends to answer a survey. They gave you back the
# following dictionary object.

# %%
# ╔══════╗
#   Setup
# ╚══════╝

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import rankdata

# %%
# ╔══════════════════╗
#   Build Dictionaries
# ╚══════════════════╝
people = {
    "Matt": {
        "willingness to travel": 5,
        "desire for new experience": 4,
        "cost": 1,
        # "indian food": 2,
        # "mexican food": 4,
        # "hipster points": 2,
        "vegetarian": 2,
    },
    "Brent": {
        "willingness to travel": 5,
        "desire for new experience": 3,
        "cost": 3,
        # "indian food": 2,
        # "mexican food": 4,
        # "hipster points": 1,
        "vegetarian": 5,
    },
    "Laran": {
        "willingness to travel": 3,
        "desire for new experience": 4,
        "cost": 3,
        # "indian food": 1,
        # "mexican food": 2,
        # "hipster points": 2,
        "vegetarian": 1,
    },
    "Holly": {
        "willingness to travel": 1,
        "desire for new experience": 2,
        "cost": 1,
        # "indian food": 4,
        # "mexican food": 5,
        # "hipster points": 3,
        "vegetarian": 1,
    },
    "Suzanne": {
        "willingness to travel": 4,
        "desire for new experience": 4,
        "cost": 3,
        # "indian food": 5,
        # "mexican food": 2,
        # "hipster points": 5,
        "vegetarian": 4,
    },
    "Ilyssa": {
        "willingness to travel": 2,
        "desire for new experience": 1,
        "cost": 1,
        # "indian food": 3,
        # "mexican food": 5,
        # "hipster points": 3,
        "vegetarian": 4,
    },
    "Andre": {
        "willingness to travel": 5,
        "desire for new experience": 1,
        "cost": 2,
        # "indian food": 2,
        # "mexican food": 2,
        # "hipster points": 4,
        "vegetarian": 3,
    },
    "Emily": {
        "willingness to travel": 5,
        "desire for new experience": 5,
        "cost": 1,
        # "indian food": 5,
        # "mexican food": 5,
        # "hipster points": 3,
        "vegetarian": 1,
    },
    "Christina": {
        "willingness to travel": 3,
        "desire for new experience": 4,
        "cost": 4,
        # "indian food": 1,
        # "mexican food": 1,
        # "hipster points": 3,
        "vegetarian": 2,
    },
    "Harmonie": {
        "willingness to travel": 2,
        "desire for new experience": 1,
        "cost": 1,
        # "indian food": 5,
        # "mexican food": 4,
        # "hipster points": 1,
        "vegetarian": 1,
    },
}

people_prefs = [
    "willingness to travel",
    "desire for new experience",
    "cost",
    # "indian food",
    # "mexican food",
    # "hipster points",
    "vegetarian",
]

M_people = np.array(
    [[people[i][people_prefs] for people_prefs in people[i]] for i in people]
)

# Next you collected data from an internet website. You got the following
# information.

restaurants = {
    "Lazy Dog": {
        "distance": 5,
        "novelty": 3,
        "cost": 3,
        # "average rating": 4.5,
        # "cuisine": 5,
        "vegetarians": 3,
    },
    "P.F. Chang's": {
        "distance": 2,
        "novelty": 2,
        "cost": 4,
        # "average rating": 3.8,
        # "cuisine": 3,
        "vegetarians": 5,
    },
    "Paleo's Pizza": {
        "distance": 3,
        "novelty": 2,
        "cost": 3,
        # "average rating": 4.9,
        # "cuisine": 4,
        "vegetarians": 5,
    },
    "Fuzzy's": {
        "distance": 5,
        "novelty": 3,
        "cost": 5,
        # "average rating": 3.5,
        # "cuisine": 3,
        "vegetarians": 4,
    },
    "Empress of China": {
        "distance": 5,
        "novelty": 2,
        "cost": 2,
        # "average rating": 4.0,
        # "cuisine": 2,
        "vegetarians": 2,
    },
    "Whataburger": {
        "distance": 4,
        "novelty": 5,
        "cost": 5,
        # "average rating": 5,
        # "cuisine": 5,
        "vegetarians": 1,
    },
    "Chipotle": {
        "distance": 5,
        "novelty": 2,
        "cost": 4,
        # "average rating": 2.6,
        # "cuisine": 3,
        "vegetarians": 5,
    },
    "Farina's": {
        "distance": 3,
        "novelty": 4,
        "cost": 2,
        # "average rating": 4.8,
        # "cuisine": 5,
        "vegetarians": 5,
    },
    "Napoli's": {
        "distance": 3,
        "novelty": 4,
        "cost": 1,
        # "average rating": 5,
        # "cuisine": 4,
        "vegetarians": 4,
    },
    "Tolbert's": {
        "distance": 3,
        "novelty": 3,
        "cost": 3,
        # "average rating": 4.7,
        # "cuisine": 4,
        "vegetarians": 2,
    },
}

# Transform the restaurant data into a matrix(M_resturants) use the same column
# index.

restaurant_prefs = [
    "distance",
    "novelty",
    "cost",
    # "average rating",
    # "cuisine",
    "vegetarian",
]

M_restaurants = np.array(
    [
        [restaurants[i][restaurant_prefs] for restaurant_prefs in restaurants[i]]
        for i in restaurants
    ]
)

# The most important idea in this project is the idea of a linear combination.
# Informally describe what a linear combination is  and how it will relate to
# our restaurant matrix.

# A linear combination is a set of terms, multiplied by a constant, and then
# added together. In our example, multiplying our people matrix by the
# restaurants matrix will result in a preference score for each
# person/restaurant combination that can then be added together to determine the
# best restaurant for the group to eat at.

# Choose a person and compute (using a linear combination) the top restaurant
# for them. What does each entry in the resulting vector represent?

Matt_ranking = np.dot(M_restaurants, M_people[0].transpose())
Matt_ranking

# The resulting vector represents the scores that Matt assigned to each
# restaurant.

# Next, compute a new matrix (M_usr_x_rest i.e. an user by restaurant) from all
# people. What does the a_ij matrix represent?

M_usr_x_rest = np.dot(M_restaurants, M_people.transpose())

# Similar to the previous problem, where we looked at Matt's scores, each row
# represents a person, and each column represents a restaurant. The resulting
# matrix values are each person's score for that particular restaurant.

# Sum all columns in M_usr_x_rest to get the optimal restaurant for all users.
# What do the entries represent?

col_sum = np.sum(M_usr_x_rest, axis=1)

# The entries in col_sum represent the cumulative score that each restaurant
# earned based on each person's ratings.

# Now convert each row in the M_usr_x_rest into a ranking for each user and call
# it M_usr_x_rest_rank. Do the same as above to generate the optimal restaurant
# choice.

M_usr_x_rest_rank = M_usr_x_rest.argsort(axis=0).argsort(axis=0) + 1

# Find the optimal restaurant choice for the ten people
rank_sum = np.sum(M_usr_x_rest_rank, axis=1)

# Rank the restaurant choices by both ranking as well as by their original
# scores to compare them
rank_ranking = len(rank_sum) - rankdata(rank_sum, method="ordinal") + 1
score_ranking = len(col_sum) - rankdata(col_sum, method="ordinal") + 1

rank_ranking
score_ranking

# Why is there a difference between the two? What problem arrives? What does it
# represent in the real world?

# The difference between rank_ranking and score_ranking has to do with the fact
# that converting the scores into rankings removes the range between scores.

# How should you preprocess your data to remove this problem?

# Find user profiles that are problematic, explain why?

# Think of two metrics to compute the disatistifaction with the group. Should
# you split in two groups today?

# Ok. Now you just found out the boss is paying for the meal. How should you
# adjust? Now what is the best restaurant?

# Tomorrow you visit another team. You have the same restaurants and they told
# you their optimal ordering for restaurants. Can you find their weight matrix?


# %%
