# https://leetcode.com/problems/sort-characters-by-frequency/

import collections
import heapq
def frequency_sort(string):
    def frequency_dict():
        alpha_dict = collections.defaultdict(int)
        for char in string:
            alpha_dict[char] += 1
        return alpha_dict

    frequency = [(-value, key) for key, value in frequency_dict().items()]
    heapq.heapify(frequency)
    return "".join([items[1] * abs(items[0]) for items in frequency])


print(frequency_sort("tree"))
print(frequency_sort("cccaaa"))
print(frequency_sort("abbA"))

# Time: O(n), n is the length of the given string
    # creating the hash map takes n
    # doing the heap sort is kind of constant because the most number of elements

