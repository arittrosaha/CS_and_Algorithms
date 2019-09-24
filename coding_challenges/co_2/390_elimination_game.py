# https://leetcode.com/problems/elimination-game/

def last_remaining(n): # Time: O(logn) ; Space: O(1)
    left = True
    # iterate from left to right 
    
    head = 1 
    # head is the first element, therefore needs to be updated everytime there is a new head after eliminations from each iteration
        # if iterating from the left, first element is obviously eliminated, so the head needs to be updated
        # if iterating from the right, and the total number of elements or n is odd as of then, then head needs to be updated as the first elements will be eliminated
            # like 2 4 6 8 10, we move from 10, we will take out 10, 6 and 2, head is deleted and move to 4
            # like 2 4 6 8 10 12, we move from 12, we will take out 12, 8, 4, head is still remaining 2

    step = 1
    # step is increased by a factor of 2 every iteration.
        # a step of 2 over a previous step of 2 built upon and so on ... is basically an increase factor of 2 at each update

    # n is acting as the remaining number of elements
        # it gets reduced by half after each iteration since every other elements gets eliminated

    while n > 1:
        if left or n % 2 == 1:
            head += step
            # to update head, the previous step is added because the previous step get it to the halfway element between the adjacent elements to be eliminated
        n //= 2
        # this division can be done using n >>= 1 because shifting by 1 bit to the right essentially is dividing by 2
        step *= 2
        # n <<= because left shifting by 1 bit essentially means multiplying by 2
        left = not left
        
    return head

# print(last_remaining(9))  # => 6
# print(last_remaining(24)) # => 14


# Great explantion bellow:
# https://leetcode.com/problems/elimination-game/discuss/87119/JAVA%3A-Easiest-solution-O(logN)-with-explanation
