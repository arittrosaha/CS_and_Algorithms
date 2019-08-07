# Merge two sorted arrays

# Prompt:
# Combine entries of two sorted arrays of integers 
# Update the first of the combined entries of the two arrays in sorted order
# Assume the first array has enough empty entries at its end to hold the result

# Example:
# Input -> [5,13,17,None,None,None,None,None], [3,7,11,19]
# Output -> [3,5,7,11,13,17,19,None]

# Time: O(n), n is the length of the first array
# Space: O(1)

def merge_two_sorted_arrays(l1,l2): 
    first_arr_int_count = 0
    for num in l1:
        if num is not None:
            first_arr_int_count += 1
    
    total_len = first_arr_int_count + len(l2)
    i, j, k = first_arr_int_count-1, len(l2)-1, total_len-1
    while i >= 0 and j >= 0:
        if l1[i] > l2[j]:
            l1[k] = l1[i]
            i -= 1
        elif l2[j] > l1[i]:
            l1[k] = l2[j]
            j -= 1
        else:
            l1[k] = l1[i]
            i, j = i-1, j-1
        k -= 1
    while j >= 0:
        l1[k] = l2[j] 
        k, j = k-1, j-1

    return l1

print(merge_two_sorted_arrays(
    [5, 13, 17, None, None, None, None, None],
    [3, 7, 11, 19]
))
        
    
