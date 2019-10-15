# https://leetcode.com/problems/number-of-islands/

def num_islands(grid):
    def dfs(column, row):
        if row < 0 or column < 0 or row >= len(grid[0]) or column >= len(grid) or grid[column][row] is 0:
            return

        grid[column][row] = 0

        dfs(column-1, row)
        dfs(column+1, row)
        dfs(column, row-1)
        dfs(column, row+1)
    
    num_of_islands = 0
    for column in range(len(grid)):
        for row in range(len(grid[0])):
            if grid[column][row] is 1:
                dfs(column, row)
                num_of_islands += 1
    
    return num_of_islands

grid_1 = [
    [1,1,1,1,0],
    [1,1,0,1,0],
    [1,1,0,0,0],
    [0,0,0,0,0]
]
# print(num_islands(grid_1))

grid_2 = [
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,1]
]
# print(num_islands(grid_2))

# follow up - For each island, see how many tiles away it is from the nearest body of water
# incomplete
def num_of_islands_v2(grid):
    def dfs(column, row):
        if column < 0 or row < 0 or column >= len(grid) or row >= len(grid[0]) or grid[column][row] is None:
            return None
        if grid[column][row] == 0:
            return 0
        
        grid[column][row] = None

        top = dfs(column-1,row)
        down = dfs(column+1,row)
        right = dfs(column,row+1)
        left = dfs(column,row-1)

        non_nones = [distance for distance in [top, down, right, left] if distance is not None]
        grid[column][row] = min(non_nones) + 1 if len(non_nones) > 0 else None
    
    number_of_islands = 0
    for column in range(len(grid)):
        for row in range(len(grid[0])):
            if grid[column][row] == 1:
                dfs(column, row)
                number_of_islands += 1
    
    return number_of_islands


grid_1 = [
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
# print(num_of_islands_v2(grid_1))
# print(grid_1)
# [
#     [None, None, 1, 1, 0], 
#     [None, 1, 0, 1, 0], 
#     [1, 1, 0, 0, 0], 
#     [0, 0, 0, 0, 0]
# ]

grid_2 = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1]
]
# print(num_of_islands_v2(grid_2))
# print(grid_2)
# [
#     [None, 1, 0, 0, 0], 
#     [1, 1, 0, 0, 0], 
#     [0, 0, 1, 0, 0], 
#     [0, 0, 0, 1, 1]
# ]






        
