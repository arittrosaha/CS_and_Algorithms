# Compute the intersection of two sorted arrays

# Prompt
# Takes two sorted arrays and returns a new array containing elements that are present in both of the input arrays.
# The input arrays may have duplicate entries, but the returned array should be free of duplicates.

# Example
# Input -> [2,3,3,5,5,6,7,7,8,12], [5,5,6,8,8,9,10,10]
# Output -> [5,6,8]

# Time: O(m), m is the largest length of the two input arrays
# Space: O(k), k is the minimum length of the two input arrays; worst case every element is unique

def intersect_two_sorted_arrays(l1, l2): 
    i, j, intersection = 0, 0, []

    while i < len(l1) and j < len(l2):
        if l1[i] == l2[j] and (l1[i] != l1[i-1] or l2[j] != l2[j-1]):
            intersection.append(l1[i])
            i, j = i+1, j+1
        elif l1[i] < l2[j]:
            i += 1
        else:
            j += 1
    
    return intersection


# print(intersect_two_sorted_arrays(
#     [2, 3, 3, 5, 5, 6, 7, 7, 8, 12], 
#     [5, 5, 6, 8, 8, 9, 10, 10]
# ))
