# First few fibonacci numbers - 1,1,2,3,5,8,13,21,....

# Top down approach 
# Figure 16.1 ; pdf - 249
def fibonacci_v1(n, cache={}):  # Time: O(n) ; Space: O(n)
    if n <= 1:
        return n # n can only be either 1 or 0, both base cases
    elif n not in cache:
        cache[n] = fibonacci_v1(n-1) + fibonacci_v1(n-2)
    return cache[n]

# print(fibonacci_v1(6))

# Minimizing cache space is a recurring theme in DP

# Bottom up approach
def fibonacci_v2(n): # Time: O(n) ; Space: O(1)
    if n <= 1:
        return n 
    f_minus_1, f_minus_2 = 1, 1 # caching only saves the needed last two values
    for _ in range(n-1):
        temp = f_minus_2
        f_minus_2 = f_minus_1 + f_minus_2
        f_minus_1 = temp
    return f_minus_1

# print(fibonacci_v2(6))


# not accurate - see line 46
import itertools
def find_maximum_subarray(A): # Time: O(n) ; Space: O(1)
    min_sum = max_sum = 0
    for running_sum in itertools.accumulate(A): # its n rather than n + n because a running sum can be calculated in one go along with tracking min_sum and max_sum
        # accumulate creates an a iterable with each element replaced with the running sum up to it
        min_sum = min(min_sum, running_sum)
        # min_sum is capturing the lowest point up to now
        max_sum = max(max_sum, running_sum - min_sum)
        # max_sum is checking if difference between the current found lowest point and the current running sum is bigger than previously captured max difference
    return max_sum

# print(find_maximum_subarray([-2,3,2,-1]))
# print(find_maximum_subarray([-2,3,2,-1,3,3])) 
    # the -1 is not low enough to create a split; 3 + 2 + -1 + 3 + 3 is bigger than 3 + 3
# print(find_maximum_subarray([-2,3,2,-5,3,3])) 
# print(find_maximum_subarray([-2,-4,-1,-3])) 
    # => 0, but should be -1 and thus this algorithm is not accurate


# ref -> https://www.youtube.com/watch?v=86CQq3pKSUw
def find_maximum_subarray_kadane(A):
    max_current = max_global = A[0]
    for i in range(1, len(A)):
        max_current = max(A[i], max_current + A[i])
        # if running max + current element > current element, the running max / max_current expands with this element or else it starts over at this element
        if max_current > max_global:
            max_global = max_current
    return max_global

# print(find_maximum_subarray_kadane([-2,3,2,-1]))
# print(find_maximum_subarray_kadane([-2,3,2,-1,3,3])) 
    # max_current will include the -1 because 3+2+(-1) > -1, 
    # but max_global won't be updated until the next 3 is added too
# print(find_maximum_subarray_kadane([-2, 3, 2, -5, 3, 3]))
    # max_current will include the -1 because 3+2+(-5) > -5, 
    # but max_current will start again at the next 3 because 3+2+(-5) = 0 > 3
    # then 3 + 3 will be bigger previous max_global of 3 + 2
# print(find_maximum_subarray_kadane([-2, -4, -1, -3]))
    # max_current will keep getting updated until it hits -1
    # max_global will be -2 at start but will get updated at -1