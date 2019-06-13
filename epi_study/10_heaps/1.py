# Merge sorted files

# Prompt:
# Input: a set of sorted sequences
# Output: the union of these sequences as a sorted sequence

# Example:
# Input: [3,5,7], [0,6], [0,6,28]
# Output: [0,0,3,5,6,6,7,28]


import heapq
def merge_sorted_arrays(sorted_arrays):
    # creating the empty heap with a list
    min_heap = [] 

    # turning the given arrays into iterables
    sorted_arrays_iterators = [iter(sub_arr) for sub_arr in sorted_arrays] 

    # putting the first element from each iterator in the min_heap
    for i, it in enumerate(sorted_arrays_iterators):
        # iterating to the first element for each iterators
        # ref -> https://docs.python.org/3/library/functions.html#next
        first_element = next(it, None) # if there is no next element, the second argument will act as the default which in this case is None
        # next also keep track of the current iteration state

        if first_element: # if it is not None
            heapq.heappush(min_heap, (first_element, i)) # each element in the heap will have two information - the element and it's iterator's index 
    
    result = [] # where our result will be
    while min_heap: # while we have still elements that need to be popped from min_heap
        # we extract the smallest element from the heap and it's associated iterator index
        smallest_entry, smallest_entry_i = heapq.heappop(min_heap) # since each heap element consist of two elements, we can do double assignments
        smallest_entry_iter = sorted_arrays_iterators[smallest_entry_i] # we get the iterator in which the current element belongs

        result.append(smallest_entry) # the smallest extracted element is inserted in the resultant array
        next_element = next(smallest_entry_iter, None) # we traverse to the next element of same iterator from which the current smallest element was added to our result
        if next_element: # if there is a next element
            heapq.heappush(min_heap, (next_element, smallest_entry_i)) 
            # the next element from that same iterator is pushed to the heap which will get ordered under the hood

    return result

# -> The min-heap is initialized with the first element of each array
    # so if there are 3 arrays, we will have 3 elements and will always be that way
# -> So time O(n) is nlogk, n being the number of total elements and k being the number of arrays
    # which is better than nlogn if all the arrays were concatinated and then sorted


