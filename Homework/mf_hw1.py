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

# Using this format, we can loop through a list. In this example, our result
# will be 2, 3.
print([x for x in [2,3]])

# We can see this more clearly using a longer list:
print([x for x in [1, 2, 3, 4, 5]])

## [x for x in [1,2] if x == 1]

# Here we expalnd on the previous statement. Adding the 'if x == 1' statement
# iterates through the list and only returns a value if it finds a match.
print([x for x in [1,2] if x == 1])

## [y*2 for x in [[1,2],[3,4]] for y in x]

# In this statement, we multiply each element in our two lists by 2 through the
# combination of two 'for' loops. 
print([y*2 for x in [[1,2],[3,4]] for y in x])

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

# I wasn't able to find this specific function. values() allows us to check and
# see if a value exists in a dictionary
print("leave" in a_dict.values())

## _key()

# I wasn't able to find this function in the documentation.

## ‘never’ in a_dict

## del a_dict['me']

# The del function allows us to delete an entry in a dictionary.
del a_dict['me']
print(a_dict)

## a_dict.clear()

# This function removes all key value pairs from a dictionary, making it empty.
a_dict.clear()
print(a_dict)

# ╔═════════════════════╗
# ║        Sets           ║
# ╚═════════════════════╝

## add()

# Add item(s) into an existing set
set_sample = {"chocolate", "vanilla", "oreo"}
set_sample.add("mint")
print(set_sample)

## clear()

# Removes all items from a set, rendering it empty.
set_sample.clear()
print(set_sample)

## copy()

# copy() duplicates a set into a new set. Modifying the new set does not modify
# the original.
set_sample = {"chocolate", "vanilla", "oreo"}
set_sample2 = set_sample.copy()
print(set_sample2)

## difference()

# difference() will return a set that contains items that only exist in the
# first set, and not in both.
set_sample1 = {"chocolate", "vanilla", "oreo"}
set_sample2 = {"chocolate", "cherry", "mint"}
set_sample_diff = set_sample1.difference(set_sample2)
print(set_sample_diff)

## discard()

# Removes the specified item from a set.
set_sample1 = {"chocolate", "vanilla", "oreo"}
set_sample1.discard("vanilla")
print(set_sample1)

## intersection()

# Similar to difference(), intersection() will return items that exist in both
# sets.
set_sample1 = {"chocolate", "vanilla", "oreo"}
set_sample2 = {"chocolate", "cherry", "mint"}
set_sample_int = set_sample1.intersection(set_sample2)
print(set_sample_int)

## issubset()

# issubset() is TRUE if all items in the first set are also in the second set.
set_sample1 = {"chocolate", "vanilla", "oreo"}
set_sample2 = {"chocolate", "cherry", "mint"}
set_sample_subset = set_sample1.issubset(set_sample2)
print(set_sample_subset)

## pop()

set_sample1 = {"chocolate", "vanilla", "oreo"}
print(set_sample1.pop())

## remove()

# remove() works very similarly to discard(), however remove() will raise an
# error if the item doesn't exist. 
set_sample1 = {"chocolate", "vanilla", "oreo"}
try:
    set_sample1.remove("mint")
except ValueError:
    print("Value is not in the list.")

## union()

# Returns a set that contains all items from both sets, excluding duplicates
set_sample1 = {"chocolate", "vanilla", "oreo"}
set_sample2 = {"chocolate", "cherry", "mint"}
set_sample_union = set_sample1.union(set_sample2)
print(set_sample_union)

## update()

# Adds new items from the second set into the first set.
set_sample1 = {"chocolate", "vanilla", "oreo"}
set_sample2 = {"chocolate", "cherry", "mint"}
set_sample_update = set_sample1.update(set_sample2)
print(set_sample_update)

# ╔═════════════════════╗
# ║       Strings         ║
# ╚═════════════════════╝

## capitalize()

# This function will capitalize the first letter of a string and leave the rest
# alone.
sample_cap = "i am hoping to get this homework done before it's due."
print(sample_cap.capitalize())

## casefold()

#casefold() works similarly to lower(), but is a more aggressive function
sample_cap = sample_cap.capitalize()
print(sample_cap.casefold())

## center()

# The center() function will center a string in a defined length. In addition to
# defining the length, you can also define the delimiter (space is default)
sample_string = "machine_learning"
print(sample_string.center(30, "*"))

## count()

# count() will return how many times an element appears. For example, how many
# times does the number '3' appear in the first 16 digits of pi?
# 3.141592653589793
pi_count = (3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3)
print(pi_count.count(3))

## encode()

# encode() allows you to re-encode a string using a predefined method. (UTF-8 is
# default)
sample_encode = "My name is Ståle"
print(sample_encode.encode())

## find()

# Similar to index(), find will locate the first instance of the value,
# however, unlike index, find will not return an error if an instance isn't
# found.
# print(pi_count.find(10))

## partition()

# partition() will divide a string into three tuples with the second tuple as
# the specified element, and the other two strings are the values to the left
# and right of the specified element.
print(sample_cap.partition("homework"))

## replace()

# Replaces instances of the supplied element with a substitute.
print(sample_cap.replace("homework", "assignment"))

## split()

# The split() function divides a string into individual list items.
print(sample_cap.split())

## title()

# Converts a string to be titlecase.
print(sample_cap.title())

## zfill()

# zfill() pads a string with leading 0's until the specified length is reached.
# If the string is longer than the specified length, no leading 0's are added.
sample_zfill = "2472"
print(sample_zfill.zfill(5))

# ╔═════════════════════╗
# ║      Counting         ║
# ╚═════════════════════╝

from collections import Counter

from numpy import float_power

# from itertools import * (Bonus: this one is optional, but recommended)

flower_orders=['W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/R/B/Y','W/R/B/Y','W/R/B/Y','W/R/B/Y','W/R/B/Y','W/R/B/Y','B/Y','B/Y','B/Y','B/Y','B/Y','R/B/Y','R/B/Y','R/B/Y','R/B/Y','R/B/Y','W/N/R/B/V/Y','W/N/R/B/V/Y','W/N/R/B/V/Y','W/N/R/B/V/Y','W/N/R/B/V/Y','W/G','W/G','W/G','W/G','R/Y','R/Y','R/Y','R/Y','N/R/V/Y','N/R/V/Y','N/R/V/Y','N/R/V/Y','W/R/B/V','W/R/B/V','W/R/B/V','W/R/B/V','W/N/R/V/Y','W/N/R/V/Y','W/N/R/V/Y','W/N/R/V/Y','N/R/Y','N/R/Y','N/R/Y','W/V/O','W/V/O','W/V/O','W/N/R/Y','W/N/R/Y','W/N/R/Y','R/B/V/Y','R/B/V/Y','R/B/V/Y','W/R/V/Y','W/R/V/Y','W/R/V/Y','W/R/B/V/Y','W/R/B/V/Y','W/R/B/V/Y','W/N/R/B/Y','W/N/R/B/Y','W/N/R/B/Y','R/G','R/G','B/V/Y','B/V/Y','N/B/Y','N/B/Y','W/B/Y','W/B/Y','W/N/B','W/N/B','W/N/R','W/N/R','W/N/B/Y','W/N/B/Y','W/B/V/Y','W/B/V/Y','W/N/R/B/V/Y/G/M','W/N/R/B/V/Y/G/M','B/R','N/R','V/Y','V','N/R/V','N/V/Y','R/B/O','W/B/V','W/V/Y','W/N/R/B','W/N/R/O','W/N/R/G','W/N/V/Y','W/N/Y/M','N/R/B/Y','N/B/V/Y','R/V/Y/O','W/B/V/M','W/B/V/O','N/R/B/Y/M','N/R/V/O/M','W/N/R/Y/G','N/R/B/V/Y','W/R/B/V/Y/P','W/N/R/B/Y/G','W/N/R/B/V/O/M','W/N/R/B/V/Y/M','W/N/B/V/Y/G/M','W/N/B/V/V/Y/P']

# 1. Build a counter object and use the counter and confirm they have the same values.

flower_counter = Counter(flower_orders)
flower_set = set(flower_orders)
print("Is the counter the same as the orders?",list(flower_counter.keys()).sort() == list(flower_set).sort())

# 2. Count how many objects have color W in them.

# Set our counter variable to start at 0
i = 0

# Using a for loop, look for elements that contain "W". If found, increment the counter.
for item in Counter(flower_orders).elements():
    if "W" in item:
        i += 1
print("Elements with W: ", i)

# 3. Make histogram of colors

from matplotlib import pyplot as plt
colors = [y for x in flower_orders for y in x.split('/')]
plt.hist(colors)
plt.show()

# 4. Rank the pairs of colors in each order regardless of how many colors are in
#    an order.

from itertools import combinations

# I think that this is asking for an ordered list of flower pairs. I should be
# able to use the same idea that we saw earlier with: [y*2 for x in
# [[1,2],[3,4]] for y in x].
flower_pairs = [y for x in flower_orders for y in combinations(x.split('/'), 2)]
flower_pair_counter = Counter(flower_pairs)

for i in flower_pair_counter:
    print(f'{i} : {flower_pair_counter[i]}')

# 5. Rank the triplets of colors in each order regardless of how many colors are
#    in an order.

# I should simply be able to reuse the same code from above, dividing by 3
# instead of 2.
flower_triplets = [y for x in flower_orders for y in combinations(x.split('/'), 3)]
flower_triplet_counter = Counter(flower_triplets)

for i in flower_triplet_counter:
    print(f'{i} : {flower_triplet_counter[i]}')

# 6. Make dictionary color for keys and values are what other colors it is
#    ordered with.

# Get the unique colors used in flower_orders
print(set(colors))
# Y, V, W, G, R, P, N, B, O, M

# Build a fuction that names each of the unique colors in flower_orders
def get_color_name(flower_color):
    translator = {"Y" : "Yellow",
                  "V" : "Violet",
                  "W" : "White",
                  "G" : "Green",
                  "R" : "Red",
                  "P" : "Purple",
                  "N" : "Navy",
                  "B" : "Blue",
                  "O" : "Orange",
                  "M" : "Magenta"}

    return translator.get(flower_color, "Invalid Color")

# Set up an empty dictionary
color_dictionary = {}

# Create a for loop to iterate over each element and define the color name
for item in Counter(flower_orders).elements():
    colors = item.split("/")
    
    for color in colors:
        
        color_dictionary[color] = get_color_name(color)

# Print the completed dictionary
print(color_dictionary)

# 7. Make a graph showing the probability of having an edge between two colors
#    based on how often they co-occur. (a numpy square matrix)

# I think I can start with the same code as from question #4:
flower_pairs = [y for x in flower_orders for y in combinations(x.split('/'), 2)]
flower_pair_counter = Counter(flower_pairs)

# Set up an empty dictionary
flower_dictionary = {}

# Get the total number of counts in order to calculate probability
flower_total = sum([y for x, y in flower_pair_counter.items()])

# For each pair, calculate the probability
for key, value in flower_pair_counter.items():
    flower_dictionary[key] = value/flower_total

# Print the results
print(flower_dictionary)

# 8. Make 10 business questions related to the questions we asked above.

#    1. How many total orders have been placed?
#    2. How many of each flower do I need?
#    3. What is the most popular color combination?
#    4. What is the least popular color combination?
#    5. Do any of the orders line up to events that we should plan for in the
#       future?
#    6. What is the least popular color? 
#    7. Are there additional combinations and/or colors that should be explored?
#    8. Do these orders impact my supply chain in any way, or would my vendors
#       be interested in the orders in order to better prepare for future
#       harvests?
#    9. Can I expect a similar breakdown of orders in the future?
#    10. If so, are there popular combinations that I would be safe starting to
#        pull together ahead of time?

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
print(text)

# 2. Remove spaces

text_no_sp = text.replace(" ", "")
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

def construct_transition_dictionary(list_of_lists):
    all_transition_tuples = []
    for l in list_of_lists:
        for idx in range(len(l) - 1):
            all_transition_tuples.append((l[idx], l[idx + 1]))
    cnt = Counter(all_transition_tuples)
    ret = {}
    for k, v in cnt.items():
        total = sum([y for x, y in cnt.items() if x[0] == k[0]])
        ret[k] = v/float(total)
    return ret

sample_transition_dictionary = construct_transition_dictionary(text_clean)
sample_transition_dictionary

state_space = list(set([x for y in sample_transition_dictionary.keys() for x in y]))
state_space

build_save_graph(sample_transition_dictionary, state_space, save_loc = '')

# 5. Make a 26x26 graph of 4. in numpy



# #optional
# 6. plot graph of transition probabilities from letter to letter

# Unrelated:
# 7. Flatten a nested list
# Cool intro python resources:
# https://thomas-cokelaer.info/tutorials/python/index.html
