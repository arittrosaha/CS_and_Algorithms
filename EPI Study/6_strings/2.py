# Base conversion

# Prompt:
# A program that does base conversion.
# The input is a string, an integer b1, and integer b2
# b1 represents the base of the given string number
# b2 is the base to which it needs to get converted

# Example:
# string = "615"
# b1 = 7
# b2 = 13
# => "1A7"

def conversion_base(num_str, b1, b2): # Time: O()
    str_to_num = {
        "0": 0, "1": 1, "2": 2, "3": 2, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15
    }
    num_to_str = {
        0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"
    }
    
    # b1 to base 10
    num_str_arr = list(num_str)
    num_10 = 0
    power = 0
    for i in reversed(range(len(num_str_arr))):
        curr_num_str = num_str_arr[i]
        curr_num = str_to_num[curr_num_str]
        num_10 += curr_num * b1**power
        power += 1

    # base 10 to b2
    num_b2_arr = []
    while num_10 > 0:
        digit = num_10 % b2
        digit_str = num_to_str[digit]
        num_b2_arr.append(digit_str)
        num_10 //= b2
    
    return "".join(reversed(num_b2_arr))

# print(conversion_base("615", 7, 13)) # => "1A7"
# print(conversion_base("1A7", 13, 7)) # => "615"
