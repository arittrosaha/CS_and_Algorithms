# Generate all nonattacking placements of n-Queens

# Background: A nonattacking placement of queens is one in which no two queens are in the same row, column, or diagonal

# Prompt: A program that returns all distinct nonattacking placements of n queens on an n x n chessboard, where n is an input

# Time Complexity:
# Brute force - O(n ^ n) time complexity. This means it will look through every position on an NxN board, N times, for N queens. 
# Refactored brute force - Prevent it from checking queens occupying the same row as each other, it will still be brute force, but the possible board states drop from 16, 777, 216 to a little over 40, 000 and has a time complexity of O(n!).
# Backtracking - This is over 100 times as fast as brute force and has a time complexity of O(2^n).
# ref -> https://medium.com/@jmohon1986/timeout-the-story-of-n-queens-time-complexity-c80636d92f8b

def n_queens(n):
    def solve_n_queens(row):
        if row == n: # base case
            result.append(list(col_placement))
            # result.append(col_placement) will append the reference to col_placement created at line 37. So if col_placement is changed for a new tree route, the old insertion also changes
            # result.append(list(col_placement)) creates a copy, so doesn't pass the reference and thus previous records will not get affected by future manipulation of col_placement
            return

        for col in range(n):
            if all(
                abs(c - col) not in (0, row - i)  
                for i, c in enumerate(col_placement[:row])
                # checking previous queen placement:
                    # c - previous columns
                    # i - previous rows
                # possible queen placement:
                    # col - current column ; iterates through all per row
                    # row - current row ; updates every call stack
                # abs(c - col) not in (0, row - i):
                    # Same row detection - if the abs(c - col) is 0, that means a queen exist in c and it is the same column as col because the difference between the two is 0
                    # Diagonal detection - if the abs(c - col) / Δx is a value that is the same as row - i / Δy, that means a queen exist at (c, i) and the current (col, row) is at a diagonal 
                        #   col       c          c    col            
                        #  [ -, -, -, q]  i     [q, _, _, _]  i
                        #  [ -, -, -, -]        [-, -, -, -]  
                        #  [ -, -, -, -]        [-, -, ?, -] row
                        #  [ ?, -, -, -] row    [_, -, -, -]
            ):
                col_placement[row] = col
                solve_n_queens(row + 1)
    
    result, col_placement = [], [0] * n 
    # col_placement of [1, 3, 0, 2], means a queen exist in column 1 - row 0, column 3 - row 1, column 0 - row 2, column 2 - row 3
    # the values in col_placement indicates the column number and the index represents the corresponding row
    solve_n_queens(0)
    return result

print(n_queens(4))  # => [[1, 3, 0, 2], [2, 0, 3, 1]]
