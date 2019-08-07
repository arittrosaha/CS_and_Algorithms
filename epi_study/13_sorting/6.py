# Merging Intervals

# Prompt:
# Inputs:
    # -> an array of disjoint closed intervals with integer endpoints, sorted by increasing order of left endpoint, 
    # -> an interval to be added
# Output: the union of the intervals in the array and the added interval

# Example:
# Input -> [[-4,-1], [0,2], [3,6], [7,9], [11,12], [14,17]], [1,8]
# Output -> [[-4,-1], [0,9], [11,12], [14,17]]

# Time: O(n), n is the number of elements in disjoint_intervals
# Space: O(n)

def add_interval(disjoint_intervals, new_interal):
    i, result = 0, []
    left, right = None, None
    while i < len(disjoint_intervals):
        if new_interal[0] >= disjoint_intervals[i][0] and new_interal[0] <= disjoint_intervals[i][1]:
            left = disjoint_intervals[i][0]
        if new_interal[1] >= disjoint_intervals[i][0] and new_interal[1] <= disjoint_intervals[i][1]:
            right = disjoint_intervals[i][1]
        if left is not None and right is not None:
            result.append([left, right])
            left, right = None, None
        elif left is None and right is None:
            result.append(disjoint_intervals[i])
        i += 1
    return result

print(add_interval(
    [[-4, -1], [0, 2], [3, 6], [7, 9], [11, 12], [14, 17]], 
    [1, 8]
))

