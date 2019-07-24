# Find the kth largest element

# Prompt: 
# Find the kth largest element of an array. 
# The 1st largest element is simply the largest element. The nth largest element is the smallest element, where n is the array's length.

# Example:
# [3,2,1,5,4] 
# - A[3] is 1st largest element
# - A[0] is 3rd largest element
# - A[2] is 5th largest element

# Complexity analysis
# -> sorting with nlogn
# -> heap sort with nlogk 
# both does more work than needed by sorting all the elements

import random
import operator

def find_kth_largest(k, A): # Time: O(n); Space: O(1)
    def find_kth(comparator):
        # A[left : new_pivot_idx] - elements greater than pivot
        # A[new_pivot_idx+1 : right+1] - elements less than pivot

        def partition_around_pivot(left, right, pivot_idx):
            pivot_value = A[pivot_idx] # its value is saved because its position will move around
            new_pivot_idx = left # the new_pivot_idx starts at left and will keep on incrementating 
            A[pivot_idx], A[right] = A[right], A[pivot_idx] # the pivot gets placed to the right for now
            for i in range(left, right):
                # if A[i] is greater than pivot_value, that element is placed at the new_pivot_idx place and then incremented
                if comparator(A[i], pivot_value): 
                    A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i] 
                    new_pivot_idx += 1
            # after all greater values are placed between left:new_pivot_index, 
            # and the remaining lesser values between new_pivot_index:right,
            # the original index value from right is brought to the new_pivot_index,
            # thus making new_pivot_idx+1:right+1 carry only the greater value
            A[right], A[new_pivot_idx] = A[new_pivot_idx], A[right] 
            return new_pivot_idx

        left, right = 0, len(A) - 1
        while left <= right:
            pivot_idx = random.randint(left, right)
            new_pivot_idx = partition_around_pivot(left, right, pivot_idx)
            # if there exactly k-1 elements greater than pivot, the pivot must be the kth largest
            if new_pivot_idx == k - 1: # if 3rd largest element is in question, after partition the 3rd largest value will be at (3-1) or 2nd index
                return A[new_pivot_idx]
            elif new_pivot_idx > k - 1: # the kth largest is in the left hand side of the partition
                right = new_pivot_idx - 1
            else: # new_pivot_idx < k - 1 ; the kth largest is in the right hand side of the partition
                left = new_pivot_idx + 1

    return find_kth(operator.gt) # gt stands for greater than
    # ref -> https://docs.python.org/2/library/operator.html#operator.gt


