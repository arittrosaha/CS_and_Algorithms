# 1
# Given an array with duplicates elements (any data type) and more than one uniques. 
# How do you return the very first unique?

# From Python 3.6 onwards, the standard dict type maintains insertion order by default.
# ref -> https://stackoverflow.com/questions/1867861/how-to-keep-keys-values-in-same-order-as-declared

import collections
def get_first_unique_v1(elements): # O(n + n) = O(n)
    # uniques = collections.defaultdict(int)
    # for element in elements:
    #     uniques[element] += 1
    # print(uniques) # => defaultdict(<class 'int'>, {True: 4, False: 3, None: 2, '67': 1, 45: 1})
    uniques = collections.Counter(elements) # O(n)
    # print(uniques)  # => Counter({True: 4, False: 3, None: 2, '67': 1, 45: 1})
    # Hashing value of True and 1 or False and 0 are the same
    for key, value in uniques.items(): # O(n)
        if value == 1:
            return key

# print(get_first_unique_v1([True, False, None, 0, 1, None, "67", True, 0, 1, 45]))         # => "67"
# print(get_first_unique_v1([True, False, None, 0, 1, None, "67", True, 0, 1, 45, "67"]))   # => 45

def get_first_unique_v2(elements):
    uniques = collections.defaultdict(int)
    for element in elements:
        if element in uniques:
            uniques[element] = -1
        else:
            uniques[element] = 1
    for key, value in uniques.items():
        if value == 1:
            return key
        
# print(get_first_unique_v2([True, False, None, 0, 1, None, "67", True, 0, 1, 45]))         # => "67"
# print(get_first_unique_v2([True, False, None, 0, 1, None, "67", True, 0, 1, 45, "67"]))   # => 45


# 2
# Given a singly linkedlist. 
# A node can have a next and a down - forking to a different linkedlist. 
# It is possible for the down branch to have more branches.
# How do you flattened them by prioritizing the down before next?




