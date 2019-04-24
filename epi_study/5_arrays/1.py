# The Dutch national flag problem

# Point 1: traditionally, quicksort(less than or equal) + [pivot] + quicksort(greater than)
# Point 2: now lets do, quicksort(less than) + [equal to including pivot] + quicksort(greater than)

# Prompt:
# A program that takes in an array A and an index i into A, and rearranges the
# elements such that all elements less than A[i] appear first, followed by
# elements equal to the pivot, followed by elements greater than the pivot.


def dutch_flag_partition_v1(pivot_index, A): # Time O(n); Space O(n)
    pivot_num = A[pivot_index]
    left_of_pivot = [n for n in A if n < pivot_num]
    same_as_pivot = [n for n in A if n == pivot_num]
    right_of_pivot = [n for n in A if n > pivot_num]

    return left_of_pivot + same_as_pivot + right_of_pivot

nums_arr = [0, 1, 2, 0, 2, 1, 1]
# print(dutch_flag_partition_v1(3, nums_arr)) # => [0, 0, 1, 2, 2, 1, 1]
# print(dutch_flag_partition_v1(2, nums_arr)) # => [0, 1, 0, 1, 1, 2, 2]

def dutch_flag_partition_v2(pivot_index, A): # Time: O(n^2); Space: O(1)
    pivot = A[pivot_index]
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            # print("before", A, "i:", i, "A[i]:", A[i], "j:", j, "A[j]:", A[j])
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break
        # print("after ", A, "i:", i, "A[i]:", A[i], "j:", j, "A[j]:", A[j])
        # print("-----")
    for i in reversed(range(len(A))):
        for j in reversed(range(i)):
            # print("before", A, "i:", i, "A[i]:", A[i], "j:", j, "A[j]:", A[j])
            if A[j] > pivot:
                A[j], A[i] = A[i], A[j]
                break
    return A
        # print("after ", A, "i:", i, "A[i]:", A[i], "j:", j, "A[j]:", A[j])
        # print("-----")

    
nums_arr1 = [0, 1, 2, 0, 2, 1, 1]
# print(dutch_flag_partition_v2(3, nums_arr1)) # => [0, 0, 1, 1, 2, 2, 1]
# print(dutch_flag_partition_v2(2, nums_arr1)) # => [1, 0, 0, 1, 1, 2, 2]

def dutch_flag_partition_v3(pivot_index, A): # Time: O(n); Space: O(1)
    pivot = A[pivot_index]
    smaller = 0
    for i in range(len(A)):
        # print("before", A, "i:", i, "A[i]:", A[i], "smaller:", smaller)
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
        # print("after ", A, "i:", i, "A[i]:", A[i], "smaller:", smaller)
        # print("----------")
    
    larger = len(A)-1
    for i in reversed(range(len(A))):
    # for i in range(len(A)):
        # print("before", A, "i:", i, "A[i]:", A[i], "larger:", larger)
        if A[i] > pivot:
            A[larger], A[i] = A[i], A[larger]
            larger -= 1
        # print("after ", A, "i:", i, "A[i]:", A[i], "larger:", larger)
        # print("----------")
    
    return A

nums_arr2 = [0, 1, 2, 0, 2, 1, 1]
# print(dutch_flag_partition_v3(3, nums_arr2)) # => [0, 0, 1, 1, 2, 2, 1]
# print(dutch_flag_partition_v3(2, nums_arr2)) # => [0, 1, 0, 1, 1, 2, 2]


def dutch_flag_partition_v4(pivot_index, A): # Time: Absolute O(n); Space: O(1)
    i, smaller, larger, pivot = 0, 0, len(A), A[pivot_index]
    while i < larger:
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller, i = smaller + 1, i + 1
        elif A[i] == pivot:
            i += 1
        else:
            larger -= 1
            A[i], A[larger] = A[larger], A[i]
    
    return A
        
nums_arr3 = [0, 1, 2, 0, 2, 1, 1]
# print(dutch_flag_partition_v4(3, nums_arr3))  # => [0, 0, 2, 2, 1, 1, 1]
# print(dutch_flag_partition_v4(2, nums_arr3))  # => [0, 0, 1, 1, 1, 2, 2]

# The reason i is not incremented after larger number is swapped with a higher index
# position is because the swap brings back an unclassified number back to the
# original index.

# [:smaller] + [smaller:i] +  [i:larger]  + [larger:]
#   bottom   +    middle   + unclassified +    top