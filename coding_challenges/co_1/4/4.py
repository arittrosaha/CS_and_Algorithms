def collapse_height(heights):
    collapsed = []
    j = 0
    i = 0
    while i < len(heights):
        j += 1
        while j < len(heights) and heights[j] == heights[i]:
            j += 1
        collapsed.append(heights[i])
        i = j
    return collapsed


def num_castles(heights):
    castle_count = 0
    collapsed = collapse_height(heights)
    for i in range(len(collapsed)):
        if i == 0:
            castle_count += 1
        elif i == len(collapsed) - 1:
            castle_count += 1
        elif collapsed[i] < collapsed[i-1] and collapsed[i] < collapsed[i+1]:
            castle_count += 1
        elif collapsed[i] > collapsed[i-1] and collapsed[i] > collapsed[i+1]:
            castle_count += 1

    return castle_count


# print(collapse_height([2,2,3,4,3,3,2,2,1,1,2,5]))
# print(collapse_height([-3, -3]))
print(num_castles([2, 2, 3, 4, 3, 3, 2, 2, 1, 1, 2, 5]))
print(num_castles([-3, -3]))
