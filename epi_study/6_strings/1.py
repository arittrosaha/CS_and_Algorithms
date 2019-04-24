# Interconvert strings and integers

# Prompt:
# An integer to string and a string to integer conversion function. 

# Example:
# If input is 314, output is "314"
# if input is "314", output is 314

def conversion(input):
    def string_to_int(string):
        char_digits = list(string)
        str_int = {
            "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9
        }
        int_digits = [str_int[char] for char in char_digits if char != "-"]
        integer = 0
        i = 0
        power = len(int_digits) - 1
        while i < len(int_digits):
            integer += int_digits[i] * 10**power
            i += 1
            power -= 1
        if string[0] == "-":
            integer = -integer
        return integer
    
    def int_to_string(integer):
        int_str = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        str_digits = []
        abs_int = abs(integer)
        while abs_int > 0:
            last_digit = abs_int % 10
            last_char_digit = int_str[last_digit]
            str_digits.append(last_char_digit)
            abs_int //= 10
        if integer < 0:
            str_digits.append("-")
        string = "".join(reversed(str_digits))
        return string

    if type(input) == str:
        return string_to_int(input)
    elif type(input) == int:
        return int_to_string(input)


# print(conversion(314)) # => "314"
# print(conversion(-314)) # => "-314"
# print(conversion("314")) # => 314
# print(conversion("-314")) # => -314