# https://leetcode.com/problems/candy-crush

def candy_crush(board):
    
    def check_horizontal():
        for y in range(len(board)):
            start_x, end_x = None, None
            for x in range(1, len(board[y])):
                if board[y][x] is not 0:
                    if board[y][x] is board[y][x-1]:
                        if start_x is None:
                            start_x = x-1
                            end_x = x
                        else:
                            end_x = x
                            if end_x is len(board[y])-1 and end_x - start_x >= 2:
                                for local_x in range(start_x, end_x + 1):
                                    if (y, local_x) not in total_matches:
                                        total_matches.add((y, local_x))
                    elif board[y][x] is not board[y][x-1] and start_x is not None:
                        if end_x - start_x >= 2:
                            for local_x in range(start_x, end_x + 1):
                                if (y, local_x) not in total_matches:
                                    total_matches.add((y, local_x))
                        start_x, end_x = None, None
            
    def check_vertical():
        for x in range(len(board[0])):
            start_y, end_y = None, None
            for y in range(1, len(board)):
                if board[y][x] is not 0:
                    if board[y][x] is board[y-1][x]:
                        if start_y is None:
                            start_y = y-1
                            end_y = y
                        elif start_y is not None:
                            end_y = y
                            if end_y is len(board) - 1 and end_y - start_y >= 2:
                                for local_y in range(start_y, end_y + 1):
                                    if (local_y, x) not in total_matches: total_matches.add((local_y, x))
                    elif board[y][x] is not board[y-1][x] and start_y is not None:
                        if end_y - start_y >= 2:
                            for local_y in range(start_y, end_y + 1):
                                if (local_y, x) not in total_matches: total_matches.add((local_y, x))
                        start_y, end_y = None, None
            
    def collapse():
        for cell in total_matches:
            board[cell[0]][cell[1]] = 0

        for x in range(len(board[0])):
            y_read, y_write = len(board)-1, len(board)-1
            while y_read >= 0 or y_write >= 0:
                if y_read >= 0:
                    cell = board[y_read][x]
                    if cell is not 0:
                        board[y_write][x] = cell
                        y_write -= 1
                    y_read -= 1
                else:
                    board[y_write][x] = 0
                    y_write -= 1
            
    
    not_stable = True
    while not_stable:
        not_stable = False
        total_matches = set()
        check_horizontal()
        check_vertical()
        if len(total_matches):
            not_stable = True
        collapse()

    return board


board = [
    [110,   5, 112, 113, 114], 
    [210, 211,   5, 213, 214], 
    [310, 311,   3, 313, 314], 
    [410, 411, 412,   5, 414], 
    [  5,   1, 512,   3,   3], 
    [610,   4,   1, 613, 614], 
    [710,   1,   2, 713, 714], 
    [810,   1,   2,   1,   1], 
    [  1,   1,   2,   2,   2], 
    [  4,   1,   4,   4, 1014]
    ]

print(candy_crush(board))
