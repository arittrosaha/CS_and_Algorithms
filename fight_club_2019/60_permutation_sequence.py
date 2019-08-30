# https://leetcode.com/problems/permutation-sequence/

import math

def getPermutation(n, k):
    # creates an array of all string numbers from 1 to n - the possible choices for each permutation
    nums = [str(i) for i in range(1, n + 1)]
    # k - 1
    return _getPermutation(nums, k - 1)

def _getPermutation(numbers, k):
    # if only one number remains, then that is the last option you have to return
    if len(numbers) == 1:
        return numbers[0]
    # if there are n! permutations, then there are n x (n-1)! seperate groups of permutations
    zone_size = math.factorial(len(numbers) - 1)
    # the specific zone can be get to by looking at how many times the zone_size goes into k, and the last time it goes is the zone in question
    zone_num = k // zone_size
    # all numbers in stable order is sliced except the current selected number based on the zone_num in preparation for the next call stack
    next_numbers = numbers[:zone_num] + numbers[zone_num+1:]
    # zone_num * zone_size is the count of all permutations from the first zone up until the zone_num
    # the next k is basically then the number after substracting all previous zones' permutations from k
    next_k = k - (zone_num * zone_size)
    # each zone's first choice goes by the zone_num (zone's number), thus acting as index position in the numbers array
    # each zone's first choice is the choice for the current stack
    # the remaining choices from the recursive call are concatinated to the current choice before returning 
    return numbers[zone_num] + _getPermutation(next_numbers, next_k)

print(getPermutation(4, 11))
