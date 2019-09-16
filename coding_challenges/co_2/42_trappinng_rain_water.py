# https://leetcode.com/problems/trapping-rain-water/

def trapping_rain_water_v1(elevation): # Time: O(n^2); Space: O(1)
    def find_water(height_idx):
        j = height_idx + 1
        while j < len(elevation):
            if elevation[j] >= elevation[height_idx]:
                nonlocal total_water

                width = (j - height_idx) + 1
                height = min(elevation[j], elevation[height_idx])
                total_area = width * height

                building_area = 0
                for h_idx in range(height_idx, j+1):
                    if elevation[h_idx] > height:
                        building_area += height
                    else:
                        building_area += elevation[h_idx]

                total_water += total_area - building_area
                return j-1

            j += 1
        return height_idx

    total_water = 0
    i = 0
    while i < len(elevation):
        i = find_water(i)
        i += 1

    return total_water


print(trapping_rain_water_v1([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

def trapping_rain_water_v2(elevation): # Time: O(n) ; Space: O(n)

    left_max = float("-inf")
    for idx, height in enumerate(elevation):
        elevation[idx] = [left_max, height, None]
        if height > left_max:
            left_max = height
    
    right_max = float("-inf")
    for idx in reversed(range(len(elevation))):
        elevation[idx][2] = right_max
        if elevation[idx][1] > right_max:
            right_max = elevation[idx][1]
    
    total_water = 0
    for element in elevation:
        left_h = element[0]
        curr_h = element[1]
        right_h = element[2]

        if left_h > curr_h < right_h and left_h >= 0 and right_h >= 0:
            total_water += min(left_h, right_h) - curr_h
    
    return total_water

# print(trapping_rain_water_v2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))


# ref -> https://www.geeksforgeeks.org/trapping-rain-water/
def trapping_rain_water_v3(elevation): # Time: O(n) ; Space: O(1)
    # initialize output
    result = 0

    # maximum element on left and right
    left_max = 0
    right_max = 0

    # indices to traverse the array
    lo = 0
    hi = len(elevation)-1

    while(lo <= hi):
        if(elevation[lo] < elevation[hi]):
            if(elevation[lo] > left_max):
                # update max in left
                left_max = elevation[lo]
            else:
                # water on curr element = max - curr
                result += left_max - elevation[lo]
            lo += 1
        else:
            if(elevation[hi] > right_max):
                # update right maximum
                right_max = elevation[hi]
            else:
                result += right_max - elevation[hi]
            hi -= 1
    return result