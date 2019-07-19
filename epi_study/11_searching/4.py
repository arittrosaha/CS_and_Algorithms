# Compute the integer square root

# Prompt:
# A program which takes a nonnegative integer and returns the largest integer
# whose square is less than or equal to the given number.

# Example:
# Input - 16; Output - 4
# Input - 300; Output - 17 because 17^2 = 289 < 300, and 18^2 = 324 > 300

def square_root(k):
    left, right = 0, k
    while left <= right:
        m = (right + left) // 2
        if m**2 <= k:
            left = m+1
        elif m**2 > k:
            right = m-1
    return left-1

# print(square_root(16))
# print(square_root(300))


# For cases of perfect square:
    # Line 13 - its left <= right rather than left < right because at equal, we still want left to increase by 1 more
    # Line 15 - we want left to increase by one more even at equal so that left goes beyond right for the while to end
    # Line 19 - substract 1 to offset the left increase
# For cases of imperfect square:
    # left will naturally increase one more than result but the offset in line 19 corrects that

        