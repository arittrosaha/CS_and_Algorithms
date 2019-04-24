# Compute the spiral ordering of a 2D array

# Prompt:
# Write a program which takes an n x n 2D array and returns the spiral ordering 
# of the array.

# Examples:

# [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# => [1,2,3,6,9,8,7,4,5]

# [
#     [1,   2,  3,  4],
#     [5,   6,  7,  8],
#     [9,  10, 11, 12],
#     [13, 14, 15, 16]
# ]
# => [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]

def matrix_in_spiral_order(square_matrix):
    # base case
    if len(square_matrix) == 0:
        return []

    # spiral order is a 1d array
    spiral_order = []

    width = len(square_matrix[0])
    length = len(square_matrix)

    # handling first row (n)
    for el in square_matrix[0]:
        spiral_order.append(el)
    
    # handling right most column (n - 1)
    for j in range(1, length):
        curr_el = square_matrix[j][width-1]
        spiral_order.append(curr_el)
    
    # handling last row in reverse order (n - 1)
    for el in reversed(square_matrix[-1][0:-1]):
        spiral_order.append(el)
    
    # handling left most row in reverse order (n - 2)
    for j in reversed(range(1, length-1)):
        curr_el = square_matrix[j][0]
        spiral_order.append(curr_el)

    # selecting the next inner most spriral matrix
    next_2d_arr = []
    for j in range(1, length-1):
        curr_1d_arr = []
        for i in range(1, width-1):
            curr_1d_arr.append(square_matrix[j][i])
        next_2d_arr.append(curr_1d_arr)
    
    # making the recursive call
    inner_spiral = matrix_in_spiral_order(next_2d_arr)
    
    # combining the previous spiral after the current spiral and returning it to the previous call stack
    return spiral_order + inner_spiral

odd_spiral = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

even_spiral = [
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
]

# print(matrix_in_spiral_order(odd_spiral))  # => [1,2,3,6,9,8,7,4,5]
# print(matrix_in_spiral_order(even_spiral)) # => [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]

# EPI note:
# The naive non-uniform approach:
# -> first add the first row with n elements
# -> next add the n - 1 remaining elements of the last column
# -> next add the n - 1 remaining elements of the last row
# -> next add the n - 2 remaining elements of the first column

# The uniform approach:
# -> add the first n - 1 elements of the first row
# -> add the first n - 1 elements of the last column
# -> add the last  n - 1 elements of the last row in reverse order
# -> add the last  n - 1 elements of the first column in reverse order
# this approach creates a edge case for the center of an odd spiral matrix
