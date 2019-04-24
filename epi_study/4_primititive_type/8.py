# Reverse digits
# -> A program that takes an integer and returns the integer corresponding to the 
#    digits of the input written in reverse order.
# -> Example : 42 => 24, -314 => -413
# -> Big(O) : O(n), n is the number of input's digits

def my_reverse(x):
    if x < 0:
        num = -x
    else:
        num = x

    split_digits = []
    while num:
        last_digit = num % 10
        split_digits = [last_digit] + split_digits
        num //= 10
    
    final_num = 0
    i = 0
    while i < len(split_digits):
        curr_digit = split_digits[i]
        final_num += curr_digit * (10**i)
        i += 1

    if x < 0:
        final_num = -final_num

    return final_num

# print(my_reverse(42)) # => 24
# print(my_reverse(-314)) # => -413

# EPI Solution:
def reverse(x):
    result , x_remaining = 0, abs(x)
    while x_remaining:
        result = result * 10 + x_remaining % 10
        x_remaining //= 10
    

    return -result if x < 0 else result

# print(reverse(42)) # => 24
# print(reverse(-314)) # => -413