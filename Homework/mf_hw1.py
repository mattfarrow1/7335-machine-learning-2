# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                              ┃
# ┃  __  __         _    _            _                      _             ___   ┃
# ┃ |  \/  |__ _ __| |_ (_)_ _  ___  | |   ___ __ _ _ _ _ _ (_)_ _  __ _  |_  )  ┃
# ┃ | |\/| / _` / _| ' \| | ' \/ -_) | |__/ -_) _` | '_| ' \| | ' \/ _` |  / /   ┃
# ┃ |_|  |_\__,_\__|_||_|_|_||_\___| |____\___\__,_|_| |_||_|_|_||_\__, | /___|  ┃
# ┃                                                                |___/         ┃
# ┃                                                                              ┃
# ┃                            +-+-+-+-+-+-+-+-+ +-+                             ┃
# ┃                            |H|o|m|e|w|o|r|k| |1|                             ┃
# ┃                            +-+-+-+-+-+-+-+-+ +-+                             ┃
# ┃                                                                              ┃
# ┃                                 Matt Farrow                                  ┃
# ┃            https://github.com/mattfarrow1/7335-machine-learning-2            ┃
# ┃                                                                              ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


# Please fill in an explanation of each function and an example of how to use it below.

# ╔═════════════════════╗
# ║        Lists          ║
# ╚═════════════════════╝

## append()

# append() allows us to add an item to the end of a list. For example:
sample = ['a', 'b']  # create a list
sample.append('c')   # append 'c' to the end of the list
print(sample)        # check out results

## extend()

# extend() works similarly to append, but allows us to add a list to the end of
# another list.
sample_extend = ['c', 'd']    # create our new list to add to 'sample'
sample.extend(sample_extend)  # extend 'sample'
print(sample)                 # check out results

## index()

# By using index() we can find where an item is in a list.
print(sample.index('b'))  # see where 'b' appears in our sample

## index(value, integer)

# By specifying a value and integer within index(), we can specify where the
# function should start looking. Using our previous example, if we start at
# index position 2, we should get an error.
try:
    sample_position = sample.index('b', 2)
except ValueError:
    print("Value is not in the list.")

## insert(position)

# insert() allows us to put an item into an existing list by specifying the
# position and the item.
sample.insert(2, 7335)
print(sample)

## remove()

# remove() works the same as insert, but does not require us to specify the
# position, only the item to be removed. We'll remove the course number that we
# inserted in the previous example.
sample.remove(7335)
print(sample)

## pop()

# pop() allows us to pull an off of our list. We'll remove 'd'.
sample.pop(sample.index('d'))
print(sample)

## count()

# count() returns the number of times a value appears in a list. Let's check the
# letter 'c'.
sample_count = sample.count("c")
print(sample_count)

## reverse()

# reverse() does what it says on the tin - reverses a list.
sample_reverse = sample.reverse()
print(sample_reverse)

## sort()

# Sorts a list alphabetically. 
sample_sort = sample.sort()
print(sample_sort)

## [1]+[1]

# Using this syntax, we can combine multiple lists together using '+'.
print("[1] + [1] =", [1] + [1])

## [2]*2

# Using this syntax, we can combine lists 'n' times.
print("[2] * 2 =", [2]*2)

## [1,2][1:]

# To slice a list, excluding the first element, we can add [1:] after our list. 
print([1,2][1:])

## [x for x in [2,3]]

print("\nLIST DUPLICATION")
print("[x for x in [2,3]]\n  This duplicates the list.")
print("[x for x in [2,3]] =", [x for x in [2,3]])

## [x for x in [1,2] if x == 1]
## [y*2 for x in [[1,2],[3,4]] for y in x]
## A = [1]

# ╔═════════════════════╗
# ║       Tuples          ║
# ╚═════════════════════╝

## count()

# count() will return how many times an element appears. For example, how many
# times does the number '3' appear in the first 16 digits of pi?
# 3.141592653589793
pi_count = (3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3)
print(pi_count.count(3))

# index()

# index() will return the position of the first occurance of the value. For
# example, the first occurance of the number '9' is at index:
print(pi_count.index(9))

# build a dictionary from tuples
# unpack tuples

# ╔═════════════════════╗
# ║     Dictionary        ║
# ╚═════════════════════╝

# Key value pairs
a_dict = {'I hate':'you', 'You should':'leave'}

## keys()

# Allows us to return the keys from a dictionary. 
print(a_dict.keys())

## items()

# Allows us to return the items from a dictionary.
print(a_dict.items())

## hasvalues()

## _key()

## ‘never’ in a_dict

## del a_dict['me']

## a_dict.clear()


# Ok enough by me do the rest on your own!
# use dir() to get built in functions***

# Sets:11
# add()
# clear()
# copy()
# difference()
# discard()
# intersection()
# issubset()
# pop()
# remove()
# union()
# update()

# ╔═════════════════════╗
# ║       Strings         ║
# ╚═════════════════════╝

# capitalize()
# casefold()
# center()
# count()	
# encode()
# find()
# partition()
# replace()
# split()
# title()
# zfill()

# ╔═════════════════════╗
# ║     Collections       ║
# ╚═════════════════════╝

from collections import Counter

# from itertools import * (Bonus: this one is optional, but recommended)

flower_orders=['W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/R/B/Y','W/R/B/Y','W/R/B/Y','W/R/B/Y','W/R/B/Y','W/R/B/Y','B/Y','B/Y','B/Y','B/Y','B/Y','R/B/Y','R/B/Y','R/B/Y','R/B/Y','R/B/Y','W/N/R/B/V/Y','W/N/R/B/V/Y','W/N/R/B/V/Y','W/N/R/B/V/Y','W/N/R/B/V/Y','W/G','W/G','W/G','W/G','R/Y','R/Y','R/Y','R/Y','N/R/V/Y','N/R/V/Y','N/R/V/Y','N/R/V/Y','W/R/B/V','W/R/B/V','W/R/B/V','W/R/B/V','W/N/R/V/Y','W/N/R/V/Y','W/N/R/V/Y','W/N/R/V/Y','N/R/Y','N/R/Y','N/R/Y','W/V/O','W/V/O','W/V/O','W/N/R/Y','W/N/R/Y','W/N/R/Y','R/B/V/Y','R/B/V/Y','R/B/V/Y','W/R/V/Y','W/R/V/Y','W/R/V/Y','W/R/B/V/Y','W/R/B/V/Y','W/R/B/V/Y','W/N/R/B/Y','W/N/R/B/Y','W/N/R/B/Y','R/G','R/G','B/V/Y','B/V/Y','N/B/Y','N/B/Y','W/B/Y','W/B/Y','W/N/B','W/N/B','W/N/R','W/N/R','W/N/B/Y','W/N/B/Y','W/B/V/Y','W/B/V/Y','W/N/R/B/V/Y/G/M','W/N/R/B/V/Y/G/M','B/R','N/R','V/Y','V','N/R/V','N/V/Y','R/B/O','W/B/V','W/V/Y','W/N/R/B','W/N/R/O','W/N/R/G','W/N/V/Y','W/N/Y/M','N/R/B/Y','N/B/V/Y','R/V/Y/O','W/B/V/M','W/B/V/O','N/R/B/Y/M','N/R/V/O/M','W/N/R/Y/G','N/R/B/V/Y','W/R/B/V/Y/P','W/N/R/B/Y/G','W/N/R/B/V/O/M','W/N/R/B/V/Y/M','W/N/B/V/Y/G/M','W/N/B/V/V/Y/P']

# 1. Build a counter object and use the counter and confirm they have the same values.

flower_counter = Counter(flower_orders)
flower_set = set(flower_orders)
print("Is the counter the same as the orders?",list(flower_counter.keys()).sort() == list(flower_set).sort())

# 2. Count how many objects have color W in them.

flower_w = [x for x in flower_counter if 'W' in x]
print("There are", len(flower_w), "orders with 'W' in them.")

# 3. Make histogram of colors

# from matplotlib import pyplot as plt
# colors = [y for x in flower_orders for y in x.split('/')]
# plt.hist(colors)
# plt.show()

# # Hint from JohnP - Itertools has a permutation function that might help with these next two.

# 4. Rank the pairs of colors in each order regardless of how many colors are in
#    an order.
import itertools

# 5. Rank the triplets of colors in each order regardless of how many colors are
#    in an order.


# 6. Make dictionary color for keys and values are what other colors it is
#    ordered with.


# 7. Make a graph showing the probability of having an edge between two colors
#    based on how often they co-occur. (a numpy square matrix)


# 8. Make 10 business questions related to the questions we asked above.

import string
dead_men_tell_tales = ['Four score and seven years ago our fathers brought forth on this',
'continent a new nation, conceived in liberty and dedicated to the',
'proposition that all men are created equal. Now we are engaged in',
'a great civil war, testing whether that nation or any nation so',
'conceived and so dedicated can long endure. We are met on a great',
'battlefield of that war. We have come to dedicate a portion of',
'that field as a final resting-place for those who here gave their',
'lives that that nation might live. It is altogether fitting and',
'proper that we should do this. But in a larger sense, we cannot',
'dedicate, we cannot consecrate, we cannot hallow this ground.',
'The brave men, living and dead who struggled here have consecrated',
'it far above our poor power to add or detract. The world will',
'little note nor long remember what we say here, but it can never',
'forget what they did here. It is for us the living rather to be',
'dedicated here to the unfinished work which they who fought here',
'have thus far so nobly advanced. It is rather for us to be here',
'dedicated to the great task remaining before us--that from these',
'honored dead we take increased devotion to that cause for which',
'they gave the last full measure of devotion--that we here highly',
'resolve that these dead shall not have died in vain, that this',
'nation under God shall have a new birth of freedom, and that',
'government of the people, by the people, for the people shall',
'not perish from the earth.']

# 1. Join everything

# Loop over the text and join it together
text = ''.join(str(i) for i in dead_men_tell_tales)
print("")
print(text)

# 2. Remove spaces

text_no_sp = text.replace(" ", "")
print("")
print(text_no_sp)

# 3. Occurrence probabilities for letters

# Before counting the probabilities, we need to convert all of the text to
# lowercase and remove punctuation.

text_clean = text_no_sp.lower()
import re
text_clean =re.sub(r'[^\w\s]', '', text_clean)

text_counter = Counter(text_clean)
text_letters = len(text_clean)

print('')
for key in sorted(text_counter, key = text_counter.get, reverse = True):
    print(key, "appears", round((text_counter[key] / text_letters*100), 2), "% of the time.")

# 4. Tell me transition probabilities for every letter pairs
# 5. Make a 26x26 graph of 4. in numpy



# #optional
# 6. plot graph of transition probabilities from letter to letter

# Unrelated:
# 7. Flatten a nested list
# Cool intro python resources:
# https://thomas-cokelaer.info/tutorials/python/index.html
