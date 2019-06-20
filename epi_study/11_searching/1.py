# Search a sorted array for first occurrence of k

# Prompt
    # Input: a sorted array and a key
    # Output: 
        # -> the index of the first occurrence of the key in the array.
        # -> if the key does not exist, then -1


# Example:
    # Input: [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 108
    # Output: 3

    # Input: [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 285
    # Output: 6


# Complexity:
    # Time:
        # v1 -> Worst case if all the elements matches key, then O(n) time
        # v2 -> Worst case time is still O(logn)
    # Space: both v1 and v2 is O(1)


def search_first_of_k_v1(array, key): # Time: O(n) ; Space: O(1)
    start, end = 0, len(array) - 1
    while start <= end:
        middle = start + ((end - start) // 2)
        if key < array[middle]:
            end = middle - 1
        elif key == array[middle]:
            while key == array[middle-1]:
                middle -= 1
            return middle
        else:
            start = middle + 1
    return -1

# arr_v1 = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
# print(search_first_of_k_v1(arr_v1, 108))
# print(search_first_of_k_v1(arr_v1, 285))


def search_first_of_k_v2(array, key): # Time: O(logn) ; Space: O(n)
    start, end = 0, len(array) - 1
    while start <= end:
        middle = start + ((end - start) // 2)
        if key < array[middle]:
            end = middle - 1
        elif key == array[middle] and key == array[middle-1]:
            end = middle - 1
        elif key == array[middle] and key != array[middle-1]:
            return middle
        else:
            start = middle + 1
    return -1

# arr_v2 = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
# print(search_first_of_k_v2(arr_v2, 108))
# print(search_first_of_k_v2(arr_v2, 285))