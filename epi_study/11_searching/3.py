# Search a cyclically sorted array

# Background: An array is said to be cyclically sorted if it is possible to cyclically shift its entries so that it 
# becomes sorted

# Prompt
    # Input: a cyclically sorted array
    # Output: the minimum element's index
    # Constraint: Time complexity of O(logn)
    # Assumption: No two element will be equal to each other

# Example
    # Input: [378, 478, 550, 631, 103, 203, 220, 234, 279, 368]
    # Output: 4

# Complexity analysis: 
    # -> This problem can't be solved less than O(n) if array has repeated elements. 
    # -> Example, if an array consists of n-1 1s and a single 0, that 0 cannot be detected in the worst-case without 
    #    inspecting every element

def search_smallest_epi(array): # Time: O(logn) ; Space: O(1)
    left, right = 0, len(array) - 1
    while left < right:
        mid = (left + right) // 2 
        # average of two intergers will give you the middle
        if array[mid] > array[right]: 
            # if mid is greater than the rightmost element, then at [left:mid+1] comes after the rightmost element if 
            # the circular sorted array was straightened out. Therefore, the smallest element has to be between 
            # [mid+1:rightmost+1] elements
            left = mid + 1
        else: # array[mid] < array[right] ; since no two elements are the same from seperate index, mid can only be either greater or less than
            # if mid is less than right, then smallest element cannot be greater than mid. So the smallest element can be only
            # in [left:mid+1]
            right = mid
    # the while loop will exit out when left == right, at which point both left and right will stop at the minimum element
    return left
