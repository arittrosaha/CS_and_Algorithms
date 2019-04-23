# The Sudoke checker problem

# Prompt:
# Check weather a 9 X 9 2D array representing a partially completed Sudoku is valid.
# Specifically check that no row, column, or 3 X 3 2D subarray contains duplicates.
# A 0-value in the 2D array indicates that entry is blank; every other entry is in [1, 9] 

# Example:
# partial_1 = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# ] => true

def is_valid_sudoku(partial_assignment): # Time: O(n^2); Space: O()
    for row in partial_assignment: # checking row duplicates
        row_frequency = dict()
        for n in row:
            if n in row_frequency:
                row_frequency[n] += 1
            else:
                row_frequency[n] = 1
            if row_frequency[n] > 1 and n != 0:
                return False
    
    for col_i in range(9): # checking column dupilicates
        col_frequency = dict()
        for row in partial_assignment:
            col_n = row[col_i]
            if col_n in col_frequency:
                col_frequency[col_n] += 1
            else:
                col_frequency[col_n] = 1
            if col_frequency[col_n] > 1 and col_n != 0:
                return False

    # checking 3 x 3 duplicates
    row_start = 0
    row_end = 3
    col_start = 0
    col_end = 3
    while row_end <= 9:
        frequency_sub = dict()
        for row_i in range(row_start, row_end):
            for col_i in range(col_start, col_end):
                curr_n = partial_assignment[row_i][col_i]
                if curr_n in frequency_sub:
                    frequency_sub[curr_n] += 1
                else:
                    frequency_sub[curr_n] = 1
                if frequency_sub[curr_n] > 1 and curr_n != 0:
                    return False

        col_start += 3
        col_end += 3

        if col_start >= 8 and col_end > 9:
            col_start = 0
            col_end = 3
            row_start += 3
            row_end += 3
    
    return True

partial_1 = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# print(is_valid_sudoku(partial_1))


import math
def is_valid_sudoku_epi(partial_assignment):
    def has_duplicates(arr_1d): # returns True if arr_1d has duplicates or else False
        block = list(filter(lambda x: x != 0, arr_1d)) # filtering out 0s
        return len(block) != len(set(block)) 
        # if the actual length doesn't match with duplicates free set length, then it returns True indicating it has duplicates
        # if the actual length matches with set length, then it returns False indicating no duplicates

    n = len(partial_assignment)
    if any(
            has_duplicates([partial_assignment[i][j] for j in range(n)]) # row - 2nd index moves faster than 1st
            or has_duplicates([partial_assignment[j][i] for j in range(n)]) # column - 1st index moves faster than 2nd
            for i in range(n) # this is the outer loop that is suppling the i 
        ):
        return False # if any of line 94 or 95 returns True, any() will return True for which this line's False will be returned

    # checking each 3 x 3 epi
    region_size = int(math.sqrt(n))
    return all( not has_duplicates([
            partial_assignment[a][b]
            for a in range(region_size * I, region_size * (I + 1))
            for b in range(region_size * J, region_size * (J + 1))
        ]) for I in range(region_size) for J in range(region_size)
    )

    # checking each 3 x 3 epi to my version 1
    # region_size = int(math.sqrt(n))
    # all_blocks = []
    # for J in range(region_size):
    #     block_3x3 = []
    #     for I in range(region_size):
    #         for b in range(region_size * J, region_size * (J + 1)):
    #             for a in range(region_size * I, region_size * (I + 1)):
    #                 block_3x3.append(partial_assignment[a][b])
    #     all_blocks.append(block_3x3)
    # return all(not has_duplicates(block) for block in all_blocks)

    # checking each 3 x 3 epi to my version 2
    # region_size = int(math.sqrt(n))
    # for J in range(region_size):
    #     block_3x3 = []
    #     for I in range(region_size):
    #         for b in range(region_size * J, region_size * (J + 1)):
    #             for a in range(region_size * I, region_size * (I + 1)):
    #                 block_3x3.append(partial_assignment[a][b])
    #     if has_duplicates(block_3x3):
    #         return False
    # return True

