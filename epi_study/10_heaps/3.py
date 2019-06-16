# Sort an k-sorted (almost-sorted) array

# Story Background: 
# -> Often data is almost-sorted 
# -> Example a server receives timestamped stock quotes. But due to differences in server loads and network routes, 
#    earlier quotes may arrive slightly after later quotes

# Prompt:
# Input -> a very long sequences of numbers. Each number of is at most k away from its correct sorted position.
# Output -> print the numbers in sorted order.

# Complexity analysis:
    # brute force 
        # Time O(nlogn) -> using a sort algorithm 
        # Space O(n) 
    # sort with k+1 heap
        # Time O(nlogk) -> the smallest number in a group of k + 1 numbers must be smaller than all the following numbers because all numbers are at most k integers away
        # Space O(k)

import heapq
def sort_approximately_sorted_array(sequence, k): # Time: O(nlogk) ; Space: O(k)
    min_heap = []
    
    for i in range(len(sequence) + k):
        if i < len(sequence):
            heapq.heappush(min_heap, sequence[i])
        if i >= k:
            sequence[i-k] = heapq.heappop(min_heap)

    return sequence

seq = [3,-1,2,6,4,5,8]
print(sort_approximately_sorted_array(seq, 2))  # => [-1, 2, 3, 4, 5, 6, 8]
