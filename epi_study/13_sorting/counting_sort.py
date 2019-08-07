# Counting sort
# ref -> https://www.youtube.com/watch?v=OKd534EWcdk

# Time: O(n), n is the number of elements if range of possible numbers is capped at certain level
# Space: O(k), k is the value of max element

def counting_sort(l):
    # creating a list with max_ele+1 index positions
    # +1 because of the zero index offset
    # default value for this list has to be 0 rather than None because of the arithmetic operations that will happen in line 27 with each position's value
    max_ele = 0
    for ele in l:
        if ele > max_ele:
            max_ele = ele

    list_of_k = [0] * (max_ele+1)
    for ele in l:
        list_of_k[ele] += 1

    # adding the previous frequency to the current frequency for each element
    # this step intuitively creates the last index position of an element from the input list
    for i in range(1,max_ele+1): 
        list_of_k[i] = list_of_k[i] + list_of_k[i-1]

    # shifting the frequencies by 1 position towards the right
    # this step intuitively creates the starting index position of an element from the input list
    for i in reversed(range(max_ele+1)): 
        list_of_k[i] = list_of_k[i-1]
    list_of_k[0] = 0

    # creating a list with index positions for all elements of the input list
    # default value for this list could be None because no arithmetic operations will happen
    sorted_list = [None] * len(l) 

    for ele in l:
        # list_of_k[ele] extracts each elements starting position which then gets used to the appropriate location in the sorted_list 
        sorted_list[list_of_k[ele]] = ele
        # once the an element has been placed in their appropriate place, the position gets update by 1 in preperation for the next same element
        list_of_k[ele] += 1

    return sorted_list

print(counting_sort([1, 0, 3, 1, 3, 1]))  # => [0, 1, 1, 1, 3, 3]
