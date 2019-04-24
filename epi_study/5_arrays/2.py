# Increment an arbitrary-precision integer

# Prompt: 
# A program which takes an array of digits encoding a nonnegative decimal integer D and
# updates the array to represent the integer D + 1.

# Example:
# [1, 2, 9] => [1, 3, 0]

def plus_one(A): # Time: O(n); Space: O(1)
    new_digits = []
    carry = None
    for i in reversed(range(len(A))): # processing it reverse will be faster than unshifting a new array
        if i == len(A) - 1: # add 1 to the last index
            sum = A[i] + 1
        elif carry: # add the carry if there is a carry from the previous iteration
            sum = A[i] + carry
        elif carry == None: # do nothing if there is no previous carry for index that is not the last 
            sum = A[i]

        remainder = sum % 10 # this will give the last digit of the sum
        div = sum // 10 # the floored quotient is the carry

        if div != 0:  # if the floored quotient is more than 0, it implies the sum consist of 2 digits
            carry = div # in that case, the outstanding digit needs to be carried over
        elif div == 0: # if the div is 0, there is no carry, 
            carry = None  # so the carry needs to be Noned for the next iteration

        new_digits.append(remainder) # the resultant remaineder is the correct digit for that iteration
    
    if carry:
        new_digits.append(carry) 
        # if there is an outstanding carry after the for loop, it implies the resultant sum is one digit longer
        # than the given number, so the outstanding carry will be sum's first digit

    new_digits.reverse() # reverse the digits before returning
    return new_digits

digit_1 = [1, 2, 9]
digit_2 = [1, 2, 8]
digit_3 = [9, 9, 9]
# print(plus_one(digit_1))  # => [1, 3, 0]
# print(plus_one(digit_2))  # => [1, 2, 9]
# print(plus_one(digit_3))  # => [1, 0, 0, 0]

def plus_one_epi(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A

digit_1_epi = [1, 2, 9]
digit_2_epi = [1, 2, 8]
digit_3_epi = [9, 9, 9]
# print(plus_one_epi(digit_1_epi))  # => [1, 3, 0]
# print(plus_one_epi(digit_2_epi))  # => [1, 2, 9]
# print(plus_one_epi(digit_3_epi))  # => [1, 0, 0, 0]
