# Sample offline data

# Prompt:
# An Algorithm that takes an input array of distinct elements and a size, and 
# returns a subset of the given size of the array elements. All subsets should be 
# equally likely. Return the result in input array itself.

# Example:
# Input array => [3, 7, 5, 11]
# Size => 3
# One possible output => [5, 11, 3]

from random import randint

def random_sampling(s, A): # Time: O(s); Space: O(1)
    for i in range(len(A)): # max range could be s itself and in that case line 19 and 20 won't be needed
        rand_idx = randint(i, (len(A) - 1)) # find a random index from looking forward pool
        A[i], A[rand_idx] = A[rand_idx], A[i] # swap the values, then current i will hold a selected value and the pointer or i moves forward for the remaining selection
        if i == s - 1: # if i reaches s, no need to iterate further
            break
    return A[0:s]

sample_1 = [3, 7, 5, 11]
size_1 = 3
# print(random_sampling(size_1, sample_1))

def random_sampling_epi(k, A):
    for i in range(k):
        r = randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]
    return A[0:k]

sample_epi_1 = [3, 7, 5, 11]
size_epi_1 = 3
# print(random_sampling_epi(size_epi_1, sample_epi_1))

